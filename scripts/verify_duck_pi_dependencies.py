#!/usr/bin/env python3
"""Check research-ledger structure, never mathematical truth or proof authority.

Statuses and kernel-record paths are assertions to audit, not authentication.
The only source check is lexical declaration presence; elaboration, exact types,
axioms, source correspondence and receipt authenticity require trusted CI/review.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


STATUSES = {"REFERENCE", "DEFINED", "CANDIDATE", "PAPER_PROVED",
            "CLASSICAL_IMPORTED", "KERNEL_CHECKED", "OPEN"}
ESTABLISHED = {"PAPER_PROVED", "CLASSICAL_IMPORTED", "KERNEL_CHECKED"}
UNRESOLVED = {"CANDIDATE", "OPEN"}


def validate_ledger(ledger, root: Path) -> list[str]:
    """Return deterministic diagnostic errors. An empty list grants no authority."""
    errors = []
    if (not isinstance(ledger, dict) or type(ledger.get("schema_version")) is not int
            or ledger["schema_version"] != 1):
        return ["unsupported ledger schema"]
    if ledger.get("diagnostic_only") is not True:
        errors.append("ledger must explicitly disclaim proof authority")
    rows = ledger.get("nodes")
    if not isinstance(rows, list) or not rows:
        return errors + ["nodes must be a nonempty list"]
    nodes = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"]:
            errors.append("malformed node identifier")
            continue
        name = row["id"]
        if name in nodes:
            errors.append(f"{name}: duplicate node identifier")
        nodes[name] = row

    def existing(path, owner):
        if not isinstance(path, str) or not path:
            errors.append(f"{owner}: malformed local reference")
            return None
        relative = Path(path)
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f"{owner}: reference escapes repository")
            return None
        target = root / relative
        if not target.resolve().is_relative_to(root.resolve()):
            errors.append(f"{owner}: reference escapes repository")
            return None
        if not target.is_file():
            errors.append(f"{owner}: missing file {path}")
            return None
        return target

    for name, row in nodes.items():
        kind, status = row.get("kind"), row.get("status")
        if not isinstance(kind, str) or kind not in {"source", "definition", "theorem", "conclusion"}:
            errors.append(f"{name}: invalid node kind")
            kind = ""
        if not isinstance(status, str) or status not in STATUSES:
            errors.append(f"{name}: invalid status")
            status = ""
        if not isinstance(row.get("statement"), str) or not row["statement"]:
            errors.append(f"{name}: precise statement missing")
        for field in ("requires", "premises"):
            refs = row.get(field)
            if not isinstance(refs, list) or any(not isinstance(x, str) for x in refs):
                errors.append(f"{name}: {field} must be node identifiers")
                continue
            if len(set(refs)) != len(refs):
                errors.append(f"{name}: duplicate {field}")
            for ref in refs:
                if ref not in nodes:
                    errors.append(f"{name}: missing node {ref}")
        premises = row.get("premises", [])
        if premises and (kind != "theorem" or row.get("form") != "implication"):
            errors.append(f"{name}: assumptions require an explicit implication theorem")
        if kind == "theorem" and (not isinstance(row.get("form"), str)
                or row["form"] not in {"unconditional", "implication"}):
            errors.append(f"{name}: theorem form missing")
        if kind == "theorem" and row.get("form") == "implication" and not premises:
            errors.append(f"{name}: implication must record its outstanding premises")
        if kind == "source" and status != "REFERENCE":
            errors.append(f"{name}: a source reference is not a proved conclusion")
        if kind == "definition" and status != "DEFINED":
            errors.append(f"{name}: a definition is not a proved conclusion")
        files = row.get("files", [])
        if not isinstance(files, list) or not files:
            errors.append(f"{name}: local provenance references missing")
        else:
            for path in files:
                existing(path, name)
        formal = row.get("formal", [])
        if not isinstance(formal, list):
            errors.append(f"{name}: malformed formal reference collection")
            formal = []
        for ref in formal:
            if not isinstance(ref, dict):
                errors.append(f"{name}: malformed formal reference")
                continue
            target = existing(ref.get("path"), name)
            declaration = ref.get("declaration")
            if not isinstance(declaration, str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_'.]*", declaration):
                errors.append(f"{name}: malformed declaration name")
            elif target and not re.search(
                r"^\s*(?:@\[[^\]]+\]\s*)?(?:theorem|lemma|def|abbrev)\s+" +
                re.escape(declaration.rsplit(".", 1)[-1]) + r"\b", target.read_text(), re.M
            ):
                errors.append(f"{name}: declaration absent from referenced source")
        if status == "KERNEL_CHECKED":
            if not formal:
                errors.append(f"{name}: kernel status lacks theorem reference")
            existing(row.get("kernel_record"), name)
        if status in ESTABLISHED:
            for ref in row.get("requires", []) if isinstance(row.get("requires"), list) else []:
                if (isinstance(ref, str) and ref in nodes
                        and isinstance(nodes[ref].get("status"), str)
                        and nodes[ref]["status"] in UNRESOLVED):
                    errors.append(f"{name}: invalid promotion over unresolved dependency {ref}")

    visiting, done = set(), set()

    def walk(name):
        if name in visiting:
            errors.append(f"{name}: dependency cycle")
            return
        if name in done:
            return
        visiting.add(name)
        row = nodes[name]
        for field in ("requires", "premises"):
            refs = row.get(field, [])
            if isinstance(refs, list):
                for ref in refs:
                    if isinstance(ref, str) and ref in nodes:
                        walk(ref)
        visiting.remove(name)
        done.add(name)

    for name in nodes:
        walk(name)

    # Here `requires` records use of a result in this diagram, not arbitrary
    # logical implication. A dependency that is itself conditional does not
    # silently discharge its assumptions. An explicit implication may retain
    # them; an established instance must name their established evidence.
    for name, row in nodes.items():
        if row.get("status") not in tuple(ESTABLISHED):
            continue
        refs = row.get("requires", [])
        premises = row.get("premises", [])
        available = {x for x in refs if isinstance(x, str)} if isinstance(refs, list) else set()
        if isinstance(premises, list):
            available.update(x for x in premises if isinstance(x, str))
        for ref in refs if isinstance(refs, list) else []:
            if not isinstance(ref, str) or ref not in nodes:
                continue
            inherited = nodes[ref].get("premises", [])
            for premise in inherited if isinstance(inherited, list) else []:
                if isinstance(premise, str) and premise not in available:
                    errors.append(f"{name}: omitted premise {premise} of dependency {ref}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--ledger", type=Path, default=Path("docs/DUCK_PI_DEPENDENCIES.json"))
    args = parser.parse_args()
    path = args.ledger if args.ledger.is_absolute() else args.root / args.ledger
    errors = validate_ledger(json.loads(path.read_text()), args.root)
    print("DIAGNOSTIC ONLY: no mathematical truth, kernel receipt, or source authority authenticated.")
    for error in errors:
        print(error)
    if not errors:
        print("Dependency graph, local references and declared-status consistency passed.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
