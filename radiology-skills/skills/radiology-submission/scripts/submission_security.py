#!/usr/bin/env python3
"""Shared fail-closed primitives for submission-package tools.

These helpers intentionally reject ambiguous JSON, broad/link-mediated roots,
unbounded inventories, and files that change while they are hashed.  They do
not open, extract, execute, or render author-supplied artifacts.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
import tempfile
from pathlib import Path
from typing import Any, Iterable


MAX_INVENTORY_FILES = 10_000
MAX_INVENTORY_FILE_BYTES = 2_000_000_000
MAX_INVENTORY_TOTAL_BYTES = 5_000_000_000


def is_linklike(path: Path) -> bool:
    if path.is_symlink():
        return True
    is_junction = getattr(path, "is_junction", None)
    if is_junction and is_junction():
        return True
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
    except OSError:
        return False
    return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    observed: set[str] = set()
    for key, value in pairs:
        folded = key.casefold()
        if folded in observed:
            raise ValueError(f"duplicate JSON object key is prohibited: {key}")
        observed.add(folded)
        output[key] = value
    return output


def load_json_strict(path: Path, *, max_bytes: int) -> dict[str, Any]:
    if path.stat().st_size > max_bytes:
        raise ValueError(f"JSON exceeds the {max_bytes}-byte parsing limit")
    with path.open(encoding="utf-8-sig") as handle:
        payload = json.load(handle, object_pairs_hook=reject_duplicate_pairs)
    if not isinstance(payload, dict):
        raise ValueError("JSON root must be an object")
    return payload


def authorized_package_root(raw_value: str) -> Path:
    raw = raw_value.strip()
    if not raw:
        raise ValueError("an explicit package root is required")
    if raw.startswith(("\\\\", "//", "\\\\?\\", "\\\\.\\")):
        raise ValueError("UNC and Windows device package roots are prohibited")
    requested = Path(raw).expanduser()
    if not requested.is_absolute():
        raise ValueError("package root must be an absolute path")
    lexical = Path(os.path.abspath(str(requested)))
    if lexical.parent == lexical:
        raise ValueError("filesystem roots cannot be used as package roots")
    cursor = Path(lexical.anchor)
    for part in lexical.parts[1:]:
        cursor = cursor / part
        if cursor.exists() and is_linklike(cursor):
            raise ValueError(f"package root contains a reparse point or link: {cursor}")
    resolved = lexical.resolve(strict=True)
    if not resolved.is_dir() or resolved.parent == resolved:
        raise ValueError("package root must resolve to a non-root directory")
    return resolved


def _identity(value: os.stat_result) -> tuple[int, int, int, int]:
    return (
        int(getattr(value, "st_dev", 0)),
        int(getattr(value, "st_ino", 0)),
        int(value.st_size),
        int(getattr(value, "st_mtime_ns", int(value.st_mtime * 1_000_000_000))),
    )


def bounded_sha256(path: Path, *, max_bytes: int = MAX_INVENTORY_FILE_BYTES) -> tuple[str, int]:
    if is_linklike(path):
        raise ValueError(f"refusing to hash a link or reparse point: {path}")
    before = path.stat()
    if before.st_size > max_bytes:
        raise ValueError(f"file exceeds the {max_bytes}-byte hashing limit: {path}")
    digest = hashlib.sha256()
    observed = 0
    with path.open("rb") as handle:
        opened = os.fstat(handle.fileno())
        if _identity(opened) != _identity(before):
            raise ValueError(f"file changed before hashing began: {path}")
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            observed += len(chunk)
            if observed > max_bytes:
                raise ValueError(f"file grew beyond the {max_bytes}-byte hashing limit: {path}")
            digest.update(chunk)
        after_open = os.fstat(handle.fileno())
    after_path = path.stat()
    if observed != before.st_size or _identity(after_open) != _identity(before) or _identity(after_path) != _identity(before):
        raise ValueError(f"file changed while it was being hashed: {path}")
    return digest.hexdigest(), observed


def inventory_snapshot(root: Path, *, excluded_relpaths: Iterable[str] = ()) -> dict[str, Any]:
    excluded = {value.replace("\\", "/").casefold() for value in excluded_relpaths}
    candidates: list[tuple[Path, str, int]] = []
    total_bytes = 0
    for current_root, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        current = Path(current_root)
        for dirname in list(dirnames):
            candidate = current / dirname
            if is_linklike(candidate):
                raise ValueError(f"package contains a directory link or reparse point: {candidate.relative_to(root).as_posix()}")
        for filename in filenames:
            candidate = current / filename
            relative = candidate.relative_to(root).as_posix()
            if relative.casefold() in excluded:
                continue
            if is_linklike(candidate):
                raise ValueError(f"package contains a file link or reparse point: {relative}")
            if not candidate.is_file():
                continue
            size = candidate.stat().st_size
            if size > MAX_INVENTORY_FILE_BYTES:
                raise ValueError(f"{relative} exceeds the {MAX_INVENTORY_FILE_BYTES}-byte hashing limit")
            candidates.append((candidate, relative, size))
            total_bytes += size
            if len(candidates) > MAX_INVENTORY_FILES:
                raise ValueError(f"package exceeds {MAX_INVENTORY_FILES} files")
            if total_bytes > MAX_INVENTORY_TOTAL_BYTES:
                raise ValueError(f"package exceeds the {MAX_INVENTORY_TOTAL_BYTES}-byte hashing limit")
    records: list[dict[str, Any]] = []
    final_total = 0
    for candidate, relative, _ in sorted(candidates, key=lambda value: value[1].casefold()):
        digest, observed = bounded_sha256(candidate)
        records.append({"path": relative, "bytes": observed, "sha256": digest})
        final_total += observed
    canonical = json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "algorithm": "sha256(canonical-json(sorted(path,bytes,sha256)))",
        "file_count": len(records),
        "total_bytes": final_total,
        "sha256": hashlib.sha256(canonical).hexdigest(),
        "records": records,
        "limits": {
            "max_files": MAX_INVENTORY_FILES,
            "max_file_bytes": MAX_INVENTORY_FILE_BYTES,
            "max_total_bytes": MAX_INVENTORY_TOTAL_BYTES,
        },
    }


def ensure_output_path_safe(path: Path, *, forbidden_root: Path) -> Path:
    lexical = Path(os.path.abspath(str(path.expanduser())))
    resolved = lexical.resolve(strict=False)
    try:
        resolved.relative_to(forbidden_root)
    except ValueError:
        pass
    else:
        raise ValueError("output must be outside the authorized package root")
    cursor = Path(lexical.anchor)
    for part in lexical.parts[1:]:
        cursor = cursor / part
        if cursor.exists() and is_linklike(cursor):
            raise ValueError(f"output path contains a link or reparse point: {cursor}")
    if path.exists() and not path.is_file():
        raise ValueError(f"output target is not a regular file: {path}")
    return lexical


def atomic_write_text(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    """Write a new regular file in one replace step without following a target link."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and is_linklike(path):
        raise ValueError(f"refusing to replace a link or reparse point: {path}")
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding=encoding, newline="") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()
