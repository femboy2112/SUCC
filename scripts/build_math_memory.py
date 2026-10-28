#!/usr/bin/env python3
"""Deterministic, read-only-by-default SUCC mathematics discovery index.

Complements existing CLAIM_INDEX, CLAIM_LEDGER, CLAIM_NAMESPACE_REGISTRY,
property proof graph, and SOURCE provenance. It never decides proof authority.
Branch-only dossiers are included only after being merged into the checkout.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

CLAIM_ROW = re.compile(r"^\|\s*([A-Z][A-Z0-9]*-([0-9]{1,4}[A-Z]?))\s*\|")
HEADING = re.compile(r"^#{1,2}\s+(.+?)\s*$")
SOURCE_DIRS = ("research", "handoffs", "formal")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _hash(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _canonical_json(data: object) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def _first_heading(text: str) -> str:
    for line in text.splitlines():
        hit = HEADING.match(line)
        if hit:
            return hit.group(1).strip()
    return ""


def _registered_namespace_map(registry: dict) -> tuple[dict[str, list[dict]], list[str]]:
    mapping: dict[str, list[dict]] = defaultdict(list)
    warnings = []
    fq_prefixes = defaultdict(list)
    for ns in registry.get("namespaces", []):
        if not isinstance(ns, dict):
            warnings.append("malformed namespace entry")
            continue
        fq = ns.get("fq_prefix")
        if not isinstance(fq, str) or not fq:
            warnings.append(f"namespace {ns.get('namespace')}: invalid FQ prefix")
            continue
        fq_prefixes[fq].append(ns.get("namespace"))
        for path in ns.get("supplement_files", []):
            mapping[path].append(ns)
    for fq, names in fq_prefixes.items():
        if len(names) > 1:
            warnings.append(f"DUPLICATE FQ namespace prefix: {fq}: {names}")
    return mapping, warnings


def build(root: Path) -> dict:
    root = root.resolve()
    registry_file = root / "docs/CLAIM_NAMESPACE_REGISTRY.json"
    registry = json.loads(_read_text(registry_file))
    pathmap, warnings = _registered_namespace_map(registry)
    claims = []
    scanned = []
    file_details = []
    seen = set()
    docs = root / "docs"
    for path in sorted(docs.glob("CLAIM_SUPPLEMENT_*.md")):
        rel = path.relative_to(root).as_posix()
        content = _read_text(path)
        reg = pathmap.get(rel, [])
        scanned.append(rel)
        file_details.append({"path": rel, "title": _first_heading(content),
                             "sha256": _hash(path.read_bytes()), "registered_namespaces":
                             [n["namespace"] for n in reg]})
        if not reg:
            warnings.append(f"UNREGISTERED CLAIM SUPPLEMENT: {rel}")
        for lineno, line in enumerate(content.splitlines(), 1):
            match = CLAIM_ROW.match(line)
            if not match:
                continue
            bare = match.group(1)
            prefix, suffix = bare.rsplit("-", 1)
            valid = [n for n in reg if n.get("bare_prefix") == prefix]
            if len(valid) == 1:
                n = valid[0]
                key = f"{n['fq_prefix']}-{suffix.zfill(2)}"
                ns = n["namespace"]
                recognized = True
            else:
                key = f"UNREGISTERED::{rel}::{bare}"
                ns = None
                recognized = False
                warnings.append(f"NO EXACT NAMESPACE for {bare} at {rel}:{lineno}")
            if key in seen:
                warnings.append(f"DUPLICATE CLAIM KEY {key} at {rel}:{lineno}")
            seen.add(key)
            claims.append({"key": key, "bare_id": bare, "namespace": ns,
                           "registered": recognized, "path": rel, "line": lineno,
                           "raw_table_row": line.strip(),
                           "authority": "UNCLASSIFIED_RAW; read original text"})
    for src in sorted(pathmap):
        if not (root / src).is_file():
            warnings.append(f"REGISTERED SOURCE MISSING IN WORKTREE: {src}")
    sources = []
    for base in SOURCE_DIRS:
        folder = root / base
        if not folder.exists():
            continue
        for path in sorted(folder.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in (".md", ".lean"):
                continue
            content = path.read_bytes()
            text = content.decode("utf-8", errors="replace")
            sources.append({"path": path.relative_to(root).as_posix(),
                            "title": _first_heading(text), "sha256": _hash(content),
                            "size": len(content)})
    # This index does not import mathematical truth into an unreviewed status.
    return {"schema_version": "0.1", "index_scope": "CURRENT_CHECKOUT_ONLY",
            "not_a_proof_checker": True,
            "canonical_registry": "docs/CLAIM_NAMESPACE_REGISTRY.json",
            "coverage": {"registered_namespace_count": len(registry.get("namespaces", [])),
                         "claim_supplements_scanned": len(scanned),
                         "claim_rows_found": len(claims),
                         "registered_claim_rows": sum(c["registered"] for c in claims),
                         "source_documents_found": len(sources)},
            "warnings": sorted(set(warnings)), "claim_files": file_details,
            "claims": claims, "source_documents": sources}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("docs/math_memory/CLAIM_CATALOG.json"))
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--write", action="store_true")
    selection.add_argument("--check", action="store_true")
    selection.add_argument("--stdout", action="store_true")
    args = parser.parse_args(argv)
    data = build(args.root)
    render = _canonical_json(data)
    output = args.output if args.output.is_absolute() else args.root / args.output
    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render, encoding="utf-8")
    elif args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != render:
            print(f"STALE/MISSING mathematics catalog: {output}", file=sys.stderr)
            return 1
    elif args.stdout:
        sys.stdout.write(render)
        return 0
    print(_canonical_json({"coverage": data["coverage"],
                           "warnings": data["warnings"][:30],
                           "warning_count": len(data["warnings"])}), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
