#!/usr/bin/env python3
"""Validate a host-independent action authorization and execution trace.

Passing this validator proves only that the record is internally consistent.
It does not enforce authorization at tool-call time or prove that a host receipt
was issued by a genuine host.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ACTION_OPERATIONS = {
    "READ_ONLY": {"READ", "LIST", "INSPECT", "HASH", "VALIDATE"},
    "WORKSPACE_WRITE": {"CREATE", "MODIFY", "MOVE", "DELETE"},
    "EXTERNAL_STATE_CHANGE": {
        "CREATE_EXTERNAL",
        "UPDATE_EXTERNAL",
        "DELETE_EXTERNAL",
        "SEND_MESSAGE",
        "PUBLISH",
    },
    "SUBMISSION_UPLOAD": {"UPLOAD", "REPLACE_UPLOAD", "WITHDRAW_SUBMISSION"},
    "CLINICAL_REGULATORY": {
        "ACCESS_CLINICAL",
        "CHANGE_CLINICAL_STATE",
        "SUBMIT_REGULATORY",
        "UPDATE_REGULATORY",
    },
}
ACTION_TARGET_KINDS = {
    "READ_ONLY": {
        "WORKSPACE_FILE",
        "WORKSPACE_DIRECTORY",
        "EXTERNAL_RESOURCE",
        "EXTERNAL_ACCOUNT",
    },
    "WORKSPACE_WRITE": {"WORKSPACE_FILE", "WORKSPACE_DIRECTORY"},
    "EXTERNAL_STATE_CHANGE": {"EXTERNAL_RESOURCE", "EXTERNAL_ACCOUNT"},
    "SUBMISSION_UPLOAD": {"SUBMISSION_PORTAL", "SUBMISSION_PACKAGE"},
    "CLINICAL_REGULATORY": {
        "CLINICAL_SYSTEM",
        "REGULATORY_PORTAL",
        "PATIENT_CARE_STATE",
    },
}
APPROVER_ROLES = {
    "READ_ONLY": {"POLICY", "USER", "WORKSPACE_OWNER", "RESOURCE_OWNER"},
    "WORKSPACE_WRITE": {"USER", "WORKSPACE_OWNER"},
    "EXTERNAL_STATE_CHANGE": {"USER", "RESOURCE_OWNER"},
    "SUBMISSION_UPLOAD": {"SUBMISSION_OWNER"},
    "CLINICAL_REGULATORY": {"CLINICAL_REGULATORY_AUTHORITY"},
}
AUTHORIZATION_STATES = {
    "NOT_REQUIRED",
    "REQUESTED",
    "APPROVED",
    "DENIED",
    "REVOKED",
    "EXPIRED",
}
EVIDENCE_TYPES = {
    "USER_MESSAGE",
    "HOST_APPROVAL_PROMPT",
    "SIGNED_POLICY",
    "INSTITUTIONAL_RECORD",
    "NOT_APPLICABLE",
}
EXECUTION_STATES = {"NOT_STARTED", "BLOCKED", "SUCCEEDED", "FAILED", "CANCELLED"}
EVENT_STATES = {"SUCCEEDED", "FAILED", "CANCELLED"}
ACTOR_TYPES = {"AGENT", "HUMAN", "SERVICE"}
TOOL_CALL_ID_KINDS = {"HOST", "LOCAL_CORRELATION"}
ENFORCEMENT_LEVELS = {"AUDITABLE_CONTRACT", "HOST_ENFORCED"}
HASH_RE = re.compile(r"^[0-9a-fA-F]{64}$")
TARGET_ID_RE = re.compile(r"^[a-z][a-z0-9+.-]*://\S+$")


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_trace(path: Path) -> dict[str, Any]:
    payload = json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys
    )
    if not isinstance(payload, dict):
        raise ValueError("trace root must be a JSON object")
    return payload


def canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def computed_scope_digest(payload: dict[str, Any]) -> str:
    scope = copy.deepcopy(payload.get("target_scope", {}))
    if isinstance(scope, dict):
        scope.pop("scope_sha256", None)
    return canonical_digest(scope)


def computed_aggregate_digest(payload: dict[str, Any]) -> str | None:
    execution = payload.get("execution")
    if not isinstance(execution, dict):
        return None
    events = execution.get("events")
    if not isinstance(events, list) or not events:
        return None
    return canonical_digest(events)


def computed_trace_digest(payload: dict[str, Any]) -> str:
    semantic = copy.deepcopy(payload)
    semantic.pop("trace_digest", None)
    return canonical_digest(semantic)


def refresh_trace_digests(
    payload: dict[str, Any], *, bind_authorization: bool = True
) -> dict[str, Any]:
    """Refresh deterministic digests in memory; used by fixtures and callers."""
    scope_digest = computed_scope_digest(payload)
    scope = payload.get("target_scope")
    if isinstance(scope, dict):
        scope["scope_sha256"] = scope_digest
    if bind_authorization:
        authorization = payload.get("authorization")
        if isinstance(authorization, dict):
            authorization["bound_scope_sha256"] = scope_digest
            authorization["bound_action_class"] = payload.get("action_class")
    execution = payload.get("execution")
    if isinstance(execution, dict):
        execution["aggregate_result_sha256"] = computed_aggregate_digest(payload)
    payload["trace_digest"] = computed_trace_digest(payload)
    return payload


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_hash(value: Any) -> bool:
    return isinstance(value, str) and HASH_RE.fullmatch(value) is not None


def _parse_time(value: Any, label: str, errors: list[str], *, nullable: bool = False) -> datetime | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str):
        errors.append(f"{label} must be an ISO-8601 UTC timestamp")
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{label} is not a valid ISO-8601 timestamp: {value!r}")
        return None
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        errors.append(f"{label} must include UTC offset Z or +00:00")
        return None
    return parsed.astimezone(timezone.utc)


def _validate_scope(payload: dict[str, Any], action_class: Any, errors: list[str]) -> dict[str, set[str]]:
    scope = payload.get("target_scope")
    allowed_by_target: dict[str, set[str]] = {}
    if not isinstance(scope, dict):
        errors.append("target_scope must be an object")
        return allowed_by_target
    if not _nonempty_string(scope.get("scope_id")):
        errors.append("target_scope.scope_id must be non-empty")
    targets = scope.get("targets")
    if not isinstance(targets, list) or not targets:
        errors.append("target_scope.targets must be a non-empty list")
        targets = []
    class_operations = ACTION_OPERATIONS.get(action_class, set())
    class_target_kinds = ACTION_TARGET_KINDS.get(action_class, set())
    for index, target in enumerate(targets):
        prefix = f"target_scope.targets[{index}]"
        if not isinstance(target, dict):
            errors.append(f"{prefix} must be an object")
            continue
        target_id = target.get("target_id")
        target_kind = target.get("target_kind")
        operations = target.get("allowed_operations")
        if not isinstance(target_id, str) or TARGET_ID_RE.fullmatch(target_id) is None:
            errors.append(f"{prefix}.target_id must be an exact canonical URI")
            continue
        if any(token in target_id for token in ("*", "{", "}")):
            errors.append(f"{prefix}.target_id cannot contain wildcard or template tokens")
        if target_id in allowed_by_target:
            errors.append(f"duplicate target_id in scope: {target_id}")
        if target_kind not in class_target_kinds:
            errors.append(
                f"{prefix}.target_kind {target_kind!r} is incompatible with {action_class}"
            )
        if not isinstance(operations, list) or not operations or any(
            not isinstance(operation, str) for operation in operations
        ):
            errors.append(f"{prefix}.allowed_operations must be a non-empty string list")
            operation_set: set[str] = set()
        else:
            operation_set = set(operations)
            if len(operation_set) != len(operations):
                errors.append(f"{prefix}.allowed_operations contains duplicates")
            invalid = operation_set - class_operations
            if invalid:
                errors.append(
                    f"{prefix}.allowed_operations contains operations outside {action_class}: "
                    f"{sorted(invalid)}"
                )
        allowed_by_target[target_id] = operation_set
    actual_scope_digest = scope.get("scope_sha256")
    expected_scope_digest = computed_scope_digest(payload)
    if actual_scope_digest != expected_scope_digest:
        errors.append(
            "target_scope.scope_sha256 does not match canonical target scope: "
            f"expected {expected_scope_digest}"
        )
    return allowed_by_target


def _validate_authorization(
    payload: dict[str, Any],
    action_class: Any,
    requester_id: Any,
    errors: list[str],
) -> dict[str, Any]:
    authorization = payload.get("authorization")
    parsed: dict[str, Any] = {
        "state": None,
        "approved_at": None,
        "expires_at": None,
        "revoked_at": None,
    }
    if not isinstance(authorization, dict):
        errors.append("authorization must be an object")
        return parsed
    state = authorization.get("state")
    parsed["state"] = state
    if state not in AUTHORIZATION_STATES:
        errors.append(f"invalid authorization.state {state!r}")
    if authorization.get("bound_action_class") != action_class:
        errors.append("authorization.bound_action_class does not match action_class")
    scope = payload.get("target_scope")
    scope_digest = scope.get("scope_sha256") if isinstance(scope, dict) else None
    if authorization.get("bound_scope_sha256") != scope_digest:
        errors.append("authorization.bound_scope_sha256 does not match target scope")

    approver = authorization.get("approver")
    approver_id = approver.get("actor_id") if isinstance(approver, dict) else None
    approver_role = approver.get("role") if isinstance(approver, dict) else None
    if not _nonempty_string(approver_id):
        errors.append("authorization.approver.actor_id must be non-empty")
    if approver_role not in APPROVER_ROLES.get(action_class, set()):
        errors.append(
            f"authorization approver role {approver_role!r} cannot approve {action_class}"
        )
    if action_class != "READ_ONLY" and requester_id == approver_id:
        errors.append("self-approval is forbidden for actions with side effects")

    evidence = authorization.get("evidence")
    evidence_type = evidence.get("evidence_type") if isinstance(evidence, dict) else None
    if not isinstance(evidence, dict):
        errors.append("authorization.evidence must be an object")
    else:
        if not _nonempty_string(evidence.get("evidence_id")):
            errors.append("authorization.evidence.evidence_id must be non-empty")
        if evidence_type not in EVIDENCE_TYPES:
            errors.append(f"invalid authorization evidence_type {evidence_type!r}")
        if not _nonempty_string(evidence.get("locator")):
            errors.append("authorization.evidence.locator must be non-empty")
        if not _valid_hash(evidence.get("sha256")):
            errors.append("authorization.evidence.sha256 must be 64 hexadecimal characters")
    if action_class != "READ_ONLY" and evidence_type == "NOT_APPLICABLE":
        errors.append("side-effect authorization evidence cannot be NOT_APPLICABLE")
    if action_class == "CLINICAL_REGULATORY" and evidence_type != "INSTITUTIONAL_RECORD":
        errors.append("CLINICAL_REGULATORY requires INSTITUTIONAL_RECORD authorization evidence")

    approved_at = _parse_time(
        authorization.get("approved_at"),
        "authorization.approved_at",
        errors,
        nullable=state not in {"APPROVED", "REVOKED", "EXPIRED"},
    )
    expires_at = _parse_time(
        authorization.get("expires_at"),
        "authorization.expires_at",
        errors,
        nullable=state not in {"APPROVED", "REVOKED", "EXPIRED"},
    )
    revoked_at = _parse_time(
        authorization.get("revoked_at"),
        "authorization.revoked_at",
        errors,
        nullable=True,
    )
    parsed.update(
        {
            "approved_at": approved_at,
            "expires_at": expires_at,
            "revoked_at": revoked_at,
        }
    )
    if approved_at and expires_at and expires_at <= approved_at:
        errors.append("authorization.expires_at must be after approved_at")
    if state == "REVOKED":
        if revoked_at is None:
            errors.append("REVOKED authorization requires revoked_at")
        elif approved_at and revoked_at < approved_at:
            errors.append("authorization.revoked_at cannot precede approved_at")
    elif revoked_at is not None:
        errors.append("authorization.revoked_at must be null unless state is REVOKED")

    if state == "NOT_REQUIRED":
        if action_class != "READ_ONLY":
            errors.append("only READ_ONLY actions may use authorization.state=NOT_REQUIRED")
        if approver_role != "POLICY":
            errors.append("READ_ONLY NOT_REQUIRED authorization must bind POLICY approver role")
        if evidence_type != "NOT_APPLICABLE":
            errors.append("READ_ONLY NOT_REQUIRED evidence_type must be NOT_APPLICABLE")
        if any(authorization.get(field) is not None for field in ("approved_at", "expires_at", "revoked_at")):
            errors.append("NOT_REQUIRED authorization timestamps must be null")
    if state in {"REQUESTED", "DENIED"} and any(
        authorization.get(field) is not None for field in ("approved_at", "expires_at", "revoked_at")
    ):
        errors.append(f"{state} authorization cannot contain approval/revocation timestamps")
    return parsed


def _validate_host_enforcement(
    payload: dict[str, Any], events: list[dict[str, Any]], errors: list[str]
) -> None:
    host = payload.get("host_enforcement")
    if not isinstance(host, dict):
        errors.append("host_enforcement must be an object")
        return
    level = host.get("declared_level")
    supported = host.get("runtime_authorization_enforcement")
    receipt_id = host.get("enforcement_receipt_id")
    receipt_sha = host.get("enforcement_receipt_sha256")
    if level not in ENFORCEMENT_LEVELS:
        errors.append(f"invalid host enforcement level {level!r}")
    if not isinstance(supported, bool):
        errors.append("host_enforcement.runtime_authorization_enforcement must be Boolean")
    if not _nonempty_string(host.get("host_id")):
        errors.append("host_enforcement.host_id must be non-empty")
    if supported is False:
        if level != "AUDITABLE_CONTRACT":
            errors.append(
                "host without runtime authorization support cannot claim HOST_ENFORCED"
            )
        if receipt_id is not None or receipt_sha is not None:
            errors.append("unsupported host cannot attach an enforcement receipt")
    if level == "AUDITABLE_CONTRACT" and (receipt_id is not None or receipt_sha is not None):
        errors.append("AUDITABLE_CONTRACT cannot present an enforcement receipt")
    if level == "HOST_ENFORCED":
        if supported is not True:
            errors.append("HOST_ENFORCED requires runtime_authorization_enforcement=true")
        if not _nonempty_string(receipt_id):
            errors.append("HOST_ENFORCED requires enforcement_receipt_id")
        if not _valid_hash(receipt_sha):
            errors.append("HOST_ENFORCED requires a 64-hex enforcement_receipt_sha256")
        if any(event.get("tool_call_id_kind") != "HOST" for event in events):
            errors.append("HOST_ENFORCED requires HOST tool-call IDs for every event")


def _validate_execution(
    payload: dict[str, Any],
    action_class: Any,
    requester_id: Any,
    allowed_by_target: dict[str, set[str]],
    authorization: dict[str, Any],
    validation_time: datetime,
    errors: list[str],
) -> list[dict[str, Any]]:
    execution = payload.get("execution")
    if not isinstance(execution, dict):
        errors.append("execution must be an object")
        return []
    state = execution.get("state")
    if state not in EXECUTION_STATES:
        errors.append(f"invalid execution.state {state!r}")
    tool_call_ids = execution.get("tool_call_ids")
    if not isinstance(tool_call_ids, list) or any(
        not isinstance(value, str) or not value for value in tool_call_ids
    ):
        errors.append("execution.tool_call_ids must be a list of non-empty strings")
        tool_call_ids = []
    elif len(tool_call_ids) != len(set(tool_call_ids)):
        errors.append("execution.tool_call_ids must be unique")
    events = execution.get("events")
    if not isinstance(events, list):
        errors.append("execution.events must be a list")
        events = []

    event_ids: list[str] = []
    event_times: list[datetime] = []
    normalized_events: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        prefix = f"execution.events[{index}]"
        if not isinstance(event, dict):
            errors.append(f"{prefix} must be an object")
            continue
        normalized_events.append(event)
        if event.get("sequence") != index + 1:
            errors.append(f"{prefix}.sequence must equal {index + 1}")
        tool_call_id = event.get("tool_call_id")
        if not _nonempty_string(tool_call_id):
            errors.append(f"{prefix}.tool_call_id must be non-empty")
        else:
            event_ids.append(tool_call_id)
        if event.get("tool_call_id_kind") not in TOOL_CALL_ID_KINDS:
            errors.append(f"{prefix}.tool_call_id_kind is invalid")
        if event.get("actor_id") != requester_id:
            errors.append(f"{prefix}.actor_id must match requester.actor_id")
        executed_at = _parse_time(event.get("executed_at"), f"{prefix}.executed_at", errors)
        if executed_at:
            event_times.append(executed_at)
            auth_state = authorization.get("state")
            approved_at = authorization.get("approved_at")
            expires_at = authorization.get("expires_at")
            revoked_at = authorization.get("revoked_at")
            if action_class != "READ_ONLY" and auth_state != "APPROVED":
                errors.append(f"{prefix}: side-effect execution requires APPROVED authorization")
            if auth_state == "APPROVED":
                if approved_at is None or executed_at < approved_at:
                    errors.append(f"{prefix}: execution occurred before approval")
                if expires_at is None or executed_at >= expires_at:
                    errors.append(f"{prefix}: execution occurred after authorization expiry")
            if revoked_at is not None and executed_at >= revoked_at:
                errors.append(f"{prefix}: execution occurred after authorization revocation")

        target_id = event.get("target_id")
        operation = event.get("operation")
        if target_id not in allowed_by_target:
            errors.append(f"{prefix}: target_id is outside the authorized scope")
        elif operation not in allowed_by_target[target_id]:
            errors.append(f"{prefix}: operation is outside the authorized target scope")
        if operation not in ACTION_OPERATIONS.get(action_class, set()):
            errors.append(f"{prefix}: operation is incompatible with {action_class}")
        if event.get("state") not in EVENT_STATES:
            errors.append(f"{prefix}.state is invalid")
        for field in ("before_sha256", "after_sha256", "result_sha256"):
            if not _valid_hash(event.get(field)):
                errors.append(f"{prefix}.{field} must be 64 hexadecimal characters")
        if not _nonempty_string(event.get("result_locator")):
            errors.append(f"{prefix}.result_locator must be non-empty")
        if (
            action_class == "READ_ONLY"
            and _valid_hash(event.get("before_sha256"))
            and _valid_hash(event.get("after_sha256"))
            and event.get("before_sha256") != event.get("after_sha256")
        ):
            errors.append(f"{prefix}: READ_ONLY before and after hashes must be identical")

    if event_ids != tool_call_ids:
        errors.append("execution.tool_call_ids must exactly match event order")
    aggregate = execution.get("aggregate_result_sha256")
    expected_aggregate = computed_aggregate_digest(payload)
    if events and aggregate != expected_aggregate:
        errors.append(
            "execution.aggregate_result_sha256 does not match canonical events: "
            f"expected {expected_aggregate}"
        )

    started_at = _parse_time(
        execution.get("started_at"),
        "execution.started_at",
        errors,
        nullable=not bool(events),
    )
    completed_at = _parse_time(
        execution.get("completed_at"),
        "execution.completed_at",
        errors,
        nullable=not bool(events),
    )
    if not events:
        if state not in {"NOT_STARTED", "BLOCKED"}:
            errors.append("execution without events must be NOT_STARTED or BLOCKED")
        if tool_call_ids:
            errors.append("execution without events cannot list tool-call IDs")
        if any(execution.get(field) is not None for field in (
            "started_at", "completed_at", "aggregate_result_sha256"
        )):
            errors.append("execution without events cannot contain times or aggregate hash")
        if authorization.get("state") == "APPROVED":
            expires_at = authorization.get("expires_at")
            if expires_at is not None and expires_at <= validation_time:
                errors.append("approved authorization expired before execution")
    else:
        if state not in {"SUCCEEDED", "FAILED", "CANCELLED"}:
            errors.append("execution with events must be SUCCEEDED, FAILED or CANCELLED")
        if started_at and completed_at and completed_at < started_at:
            errors.append("execution.completed_at cannot precede started_at")
        if event_times and started_at and min(event_times) < started_at:
            errors.append("an event occurred before execution.started_at")
        if event_times and completed_at and max(event_times) > completed_at:
            errors.append("an event occurred after execution.completed_at")
        event_states = [event.get("state") for event in normalized_events]
        if state == "SUCCEEDED" and any(value != "SUCCEEDED" for value in event_states):
            errors.append("SUCCEEDED execution requires every event to succeed")
        if state == "FAILED" and "FAILED" not in event_states:
            errors.append("FAILED execution requires at least one failed event")
        if state == "CANCELLED" and "CANCELLED" not in event_states:
            errors.append("CANCELLED execution requires at least one cancelled event")
    return normalized_events


def validate_trace(
    payload: dict[str, Any], *, validation_time: datetime | None = None
) -> list[str]:
    """Return all semantic errors without mutating the trace."""
    errors: list[str] = []
    validation_time = validation_time or datetime.now(timezone.utc)
    if validation_time.tzinfo is None:
        raise ValueError("validation_time must be timezone-aware")
    validation_time = validation_time.astimezone(timezone.utc)

    required_top = {
        "schema_version",
        "record_type",
        "action_id",
        "action_class",
        "requester",
        "target_scope",
        "authorization",
        "host_enforcement",
        "execution",
        "trace_digest",
    }
    missing = required_top - set(payload)
    if missing:
        errors.append(f"trace missing top-level fields {sorted(missing)}")
    if payload.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if payload.get("record_type") != "ACTION_AUTHORIZATION_EXECUTION_TRACE":
        errors.append("record_type must be ACTION_AUTHORIZATION_EXECUTION_TRACE")
    if not _nonempty_string(payload.get("action_id")):
        errors.append("action_id must be non-empty")
    action_class = payload.get("action_class")
    if action_class not in ACTION_OPERATIONS:
        errors.append(f"invalid action_class {action_class!r}")

    requester = payload.get("requester")
    requester_id = requester.get("actor_id") if isinstance(requester, dict) else None
    if not isinstance(requester, dict):
        errors.append("requester must be an object")
    else:
        if not _nonempty_string(requester_id):
            errors.append("requester.actor_id must be non-empty")
        if requester.get("actor_type") not in ACTOR_TYPES:
            errors.append(f"invalid requester.actor_type {requester.get('actor_type')!r}")
        _parse_time(requester.get("requested_at"), "requester.requested_at", errors)

    allowed_by_target = _validate_scope(payload, action_class, errors)
    authorization = _validate_authorization(payload, action_class, requester_id, errors)
    events = _validate_execution(
        payload,
        action_class,
        requester_id,
        allowed_by_target,
        authorization,
        validation_time,
        errors,
    )
    _validate_host_enforcement(payload, events, errors)

    expected_trace_digest = computed_trace_digest(payload)
    if payload.get("trace_digest") != expected_trace_digest:
        errors.append(
            "trace_digest does not match canonical trace content: "
            f"expected {expected_trace_digest}"
        )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trace", type=Path)
    parser.add_argument(
        "--validation-time",
        help="UTC ISO-8601 time used only for unexecuted approval-expiry checks",
    )
    args = parser.parse_args(argv)
    try:
        payload = load_trace(args.trace)
        validation_time = None
        if args.validation_time:
            time_errors: list[str] = []
            validation_time = _parse_time(args.validation_time, "--validation-time", time_errors)
            if time_errors or validation_time is None:
                raise ValueError("; ".join(time_errors))
        errors = validate_trace(payload, validation_time=validation_time)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors = [f"trace could not be loaded: {exc}"]
        payload = {}

    host = payload.get("host_enforcement", {}) if isinstance(payload, dict) else {}
    report = {
        "status": "PASS" if not errors else "FAIL",
        "trace": str(args.trace),
        "action_id": payload.get("action_id") if isinstance(payload, dict) else None,
        "action_class": payload.get("action_class") if isinstance(payload, dict) else None,
        "declared_enforcement_level": host.get("declared_level") if isinstance(host, dict) else None,
        "errors": errors,
        "boundary": (
            "PASS proves internal audit-contract consistency only; it does not prove runtime "
            "authorization enforcement."
        ),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
