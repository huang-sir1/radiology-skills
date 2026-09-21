#!/usr/bin/env python3
"""Build, revalidate, identify and optionally archive a clean allowlisted release tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path


FORBIDDEN_DIRS = {
    "__pycache__", "node_modules", "research", "tmp", ".git", ".venv", "venv",
    ".artifact-audit", "release-build", "dist", "runtime", "runtimes",
}
FORBIDDEN_SUFFIXES = {
    ".pyc", ".pyo", ".pyd", ".dll", ".exe", ".so", ".dylib", ".log", ".tmp",
}
REQUIRED_TOP_LEVEL = {
    ".claude-plugin", ".codex-plugin", "skills", "behavior-evals", "README.md",
    "install.md", "LICENSE", ".gitignore", "RELEASE.md", "release-allowlist.txt", "scripts",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(payload: dict[str, object], field: str) -> str:
    semantic = dict(payload)
    semantic.pop(field, None)
    return hashlib.sha256(json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")).hexdigest()


def load_allowlist(root: Path) -> list[str]:
    path = root / "release-allowlist.txt"
    raw = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    entries: list[str] = []
    seen: set[str] = set()
    for value in raw:
        if not value or value.startswith("#"):
            continue
        normalized = value.rstrip("/\\").replace("\\", "/")
        candidate = Path(normalized)
        if candidate.is_absolute() or any(part in {"", ".", ".."} for part in candidate.parts):
            raise ValueError(f"unsafe allowlist entry: {value}")
        if normalized in seen:
            raise ValueError(f"duplicate allowlist entry: {value}")
        seen.add(normalized)
        entries.append(normalized)
    if set(entries) != REQUIRED_TOP_LEVEL:
        raise ValueError(
            f"allowlist top-level mismatch: missing={sorted(REQUIRED_TOP_LEVEL-set(entries))}, "
            f"extra={sorted(set(entries)-REQUIRED_TOP_LEVEL)}"
        )
    return entries


def release_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for entry in load_allowlist(root):
        target = root / entry
        if target.is_file():
            files.append(target)
            continue
        for path in target.rglob("*"):
            if not path.is_file():
                continue
            relative = path.relative_to(root)
            if any(part in FORBIDDEN_DIRS or part.startswith(".") for part in relative.parts[1:-1]):
                raise ValueError(f"forbidden release directory: {relative.as_posix()}")
            if path.suffix.lower() in FORBIDDEN_SUFFIXES:
                raise ValueError(f"forbidden release file: {relative.as_posix()}")
            files.append(path)
    return sorted(set(files), key=lambda path: path.relative_to(root).as_posix().casefold())


def file_manifest(root: Path) -> list[dict[str, object]]:
    return [
        {
            "path": path.relative_to(root).as_posix(),
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in release_files(root)
    ]


def tree_digest(entries: list[dict[str, object]]) -> str:
    lines = "".join(
        f"{entry['path']}\t{entry['size']}\t{entry['sha256']}\n"
        for entry in sorted(entries, key=lambda item: str(item["path"]).casefold())
    )
    return hashlib.sha256(lines.encode("utf-8")).hexdigest()


def copy_allowlisted(source: Path, staging: Path) -> None:
    if staging.exists():
        raise FileExistsError(f"staging path already exists; refusing overwrite: {staging}")
    try:
        staging.relative_to(source)
    except ValueError:
        pass
    else:
        raise ValueError("staging path must be outside the source product tree")
    staging.mkdir(parents=True)
    for entry in load_allowlist(source):
        source_path = source / entry
        target_path = staging / entry
        if source_path.is_dir():
            shutil.copytree(source_path, target_path)
        else:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, target_path)


def deterministic_zip(root: Path, archive: Path, entries: list[dict[str, object]]) -> None:
    if archive.exists():
        raise FileExistsError(f"archive already exists; refusing overwrite: {archive}")
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as handle:
        for entry in sorted(entries, key=lambda item: str(item["path"]).casefold()):
            relative = str(entry["path"])
            info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            handle.writestr(info, (root / relative).read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def validator_paths(quick: str, plugin: str) -> tuple[Path, Path]:
    quick_path = Path(quick).expanduser().resolve() if quick else (
        Path.home() / ".codex" / "skills" / ".system" / "skill-creator" / "scripts" / "quick_validate.py"
    ).resolve()
    plugin_path = Path(plugin).expanduser().resolve() if plugin else (
        Path.home() / ".codex" / "skills" / ".system" / "plugin-creator" / "scripts" / "validate_plugin.py"
    ).resolve()
    for path in (quick_path, plugin_path):
        if not path.is_file():
            raise FileNotFoundError(f"external release validator is missing: {path}")
    return quick_path, plugin_path


def run_gate(root: Path, python: Path, quick: Path, plugin: Path) -> str:
    result = subprocess.run([
        "pwsh", "-NoProfile", "-File", str(root / "scripts" / "validate_release_boundary.ps1"),
        "-ProductRoot", str(root), "-PythonExecutable", str(python),
        "-QuickValidatePath", str(quick), "-PluginValidatorPath", str(plugin),
    ], check=False, capture_output=True, text=True, encoding="utf-8")
    output = result.stdout + result.stderr
    if result.returncode:
        raise RuntimeError(f"release validation failed for {root}:\n{output}")
    return output


def python_toolchain(python: Path) -> dict[str, object]:
    code = (
        "import importlib.metadata,json,sys; "
        "names=['PyYAML','pypdf','Pillow']; "
        "versions={n:importlib.metadata.version(n) for n in names}; "
        "print(json.dumps({'executable':sys.executable,'version':sys.version,'packages':versions}))"
    )
    result = subprocess.run(
        [str(python), "-c", code], check=True, capture_output=True, text=True, encoding="utf-8",
    )
    return json.loads(result.stdout)


def powershell_toolchain() -> dict[str, str]:
    executable = shutil.which("pwsh")
    if not executable:
        raise FileNotFoundError("pwsh is required for the release build")
    result = subprocess.run(
        [executable, "-NoProfile", "-Command", "$PSVersionTable.PSVersion.ToString()"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    return {"executable": Path(executable).resolve().as_posix(), "version": result.stdout.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--staging-dir", required=True, type=Path)
    parser.add_argument("--python", required=True, type=Path)
    parser.add_argument("--quick-validate", default="")
    parser.add_argument("--plugin-validator", default="")
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()

    source = args.source_root.expanduser().resolve()
    staging = args.staging_dir.expanduser().resolve()
    python = args.python.expanduser().resolve()
    if not python.is_file():
        raise SystemExit(f"Python executable is missing: {python}")
    quick, plugin = validator_paths(args.quick_validate, args.plugin_validator)
    source_output = run_gate(source, python, quick, plugin)
    copy_allowlisted(source, staging)
    staging_output = run_gate(staging, python, quick, plugin)
    entries = file_manifest(staging)

    archive_record: dict[str, object] | None = None
    if args.archive:
        archive = args.archive.expanduser().resolve()
        deterministic_zip(staging, archive, entries)
        archive_record = {
            "path": archive.as_posix(), "size": archive.stat().st_size,
            "sha256": sha256_file(archive),
        }

    manifest = json.loads((staging / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    receipt: dict[str, object] = {
        "schema_version": "1.0",
        "created_on": datetime.now(timezone.utc).isoformat(),
        "product": {"name": manifest["name"], "version": manifest["version"]},
        "staging_path": staging.as_posix(),
        "source_gate": {"status": "PASS", "output_sha256": hashlib.sha256(source_output.encode()).hexdigest()},
        "staging_gate": {"status": "PASS", "output_sha256": hashlib.sha256(staging_output.encode()).hexdigest()},
        "file_count": len(entries),
        "total_bytes": sum(int(entry["size"]) for entry in entries),
        "release_tree_sha256": tree_digest(entries),
        "files": entries,
        "archive": archive_record,
        "toolchain": {
            "python": python_toolchain(python),
            "powershell": powershell_toolchain(),
            "quick_validate": {"path": quick.as_posix(), "sha256": sha256_file(quick)},
            "plugin_validator": {"path": plugin.as_posix(), "sha256": sha256_file(plugin)},
        },
        "behavior_claim": "NOT_ESTABLISHED_BY_STRUCTURAL_BUILD",
        "boundary": "Identity receipt for an allowlisted tree validated in source and clean staging; not an authenticated scientific or behavioral release decision.",
        "release_receipt_sha256": "",
    }
    receipt["release_receipt_sha256"] = canonical_digest(receipt, "release_receipt_sha256")
    receipt_path = args.receipt.expanduser().resolve() if args.receipt else Path(str(staging) + ".release-receipt.json")
    if receipt_path.exists():
        raise FileExistsError(f"receipt already exists; refusing overwrite: {receipt_path}")
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(receipt_path)
    print(receipt["release_tree_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
