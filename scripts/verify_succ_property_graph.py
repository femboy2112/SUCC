#!/usr/bin/env python3
"""Lint and summarize the SUCC property dependency graph.

This is a proof-OBLIGATION inventory, not a theorem prover.
An edge is a declared research prerequisite, not a logical implication.
No network, zeta-zero oracle or arbitrary code execution is used.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT = REPO_ROOT / "research/2026-10-13/SUCC_PROPERTY_PROOF_GRAPH.json"
STATUSES = {"CLASSICAL", "PROVED_LOCAL", "TESTED_MODEL", "HYPOTHESIS",
            "UNVERIFIED", "REFUTED"}
LAYERS = {"carrier", "arithmetic", "archimedean", "operator", "positivity",
          "approximation", "certification", "rh_exit"}
EXIT_IDS = ("R01", "R02", "R03")


def _deps(row: dict[str, Any]) -> list[str]:
    return list(row.get("requires_all", [])) + [
        y for group in row.get("requires_any", []) for y in group
    ]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    raw_nodes = data.get("nodes")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise ValueError("nodes must be a nonempty list")
    if data.get("schema_version") != "1.0":
        errors.append("unsupported schema version")
    if data.get("root_exit") != "R04":
        errors.append("root exit must be R04")
    by_id: dict[str, dict[str, Any]] = {}
    for row in raw_nodes:
        if not isinstance(row, dict):
            errors.append("non-object node")
            continue
        key = row.get("id")
        if not isinstance(key, str) or not key:
            errors.append("invalid node ID")
            continue
        if key in by_id:
            errors.append(f"duplicate node {key}")
        by_id[key] = row
        if row.get("layer") not in LAYERS:
            errors.append(f"{key}: unexpected layer")
        if row.get("status") not in STATUSES:
            errors.append(f"{key}: unexpected status")
        if not isinstance(row.get("title"), str) or not row["title"].strip():
            errors.append(f"{key}: missing title")
        if not isinstance(row.get("scope"), str) or not row["scope"].strip():
            errors.append(f"{key}: missing proof scope")
        if not isinstance(row.get("next_probe"), str) or not row["next_probe"].strip():
            errors.append(f"{key}: missing discriminating probe")
        if not isinstance(row.get("requires_all"), list):
            errors.append(f"{key}: requires_all must be a list")
        any_groups = row.get("requires_any")
        if not isinstance(any_groups, list) or any(
            not isinstance(g, list) or not g for g in any_groups
        ):
            errors.append(f"{key}: requires_any must be nonempty AND groups")
        if not isinstance(row.get("requires_all"), list) or not isinstance(any_groups, list):
            continue
        dep_groups = [row["requires_all"]] + [g for g in any_groups if isinstance(g, list)]
        for group in dep_groups:
            for dep in group:
                if not isinstance(dep, str):
                    errors.append(f"{key}: non-string predecessor")
                elif dep == key:
                    errors.append(f"{key}: self-dependency")
    if len(by_id) != len(raw_nodes):
        errors.append("malformed/duplicate nodes")
    for key, row in by_id.items():
        try:
            deps = _deps(row)
        except (TypeError, KeyError):
            continue
        for dep in deps:
            if dep not in by_id:
                errors.append(f"{key}: unknown predecessor {dep}")
            elif by_id[dep].get("status") == "REFUTED":
                errors.append(f"{key}: REFUTED claim used as a premise: {dep}")

    done: set[str] = set()
    active: set[str] = set()
    ordering: list[str] = []

    def visit(key: str) -> None:
        if key in done:
            return
        if key in active:
            errors.append(f"dependency cycle through {key}")
            return
        active.add(key)
        for dep in _deps(by_id[key]):
            if dep in by_id:
                visit(dep)
        active.remove(key)
        done.add(key)
        ordering.append(key)

    for key in by_id:
        visit(key)

    for key in (*EXIT_IDS, "R04"):
        if key not in by_id:
            errors.append(f"missing RH exit: {key}")
        elif by_id[key].get("status") == "REFUTED":
            errors.append(f"RH exit {key} cannot be REFUTED premise")

    if "R04" in by_id:
        actual = {tuple(g) for g in by_id["R04"].get("requires_any", [])}
        expected = {(x,) for x in EXIT_IDS}
        if actual != expected:
            errors.append("R04 must retain three ALTERNATIVE, not conjunctive, RH routes")
        if by_id["R04"].get("status") in {"PROVED_LOCAL", "CLASSICAL"} and not (
            data.get("reviewed_global_proof_receipt")
            and data.get("independent_source_audit_receipt")
        ):
            errors.append("cannot promote RH without global proof and source audit receipts")

    if "P07" in by_id and "P03" not in _deps(by_id["P07"]):
        errors.append("global Weil sign must depend on completed source identification")
    if "N05" in by_id and "N01" not in _deps(by_id["N05"]):
        errors.append("global L2 density must depend on actual residue probe carrier")
    if "S05" in by_id and "H10" not in _deps(by_id["S05"]):
        errors.append("spectral correspondence must depend on source-derived completion")
    if "A09" in by_id and "A07" not in _deps(by_id["A09"]):
        errors.append("Euler discrimination must include source mutations")
    if data.get("base", {}).get("from_pr") != 59:
        errors.append("unexpected pinned zero-centered source branch")
    if not all(isinstance(x, str) and x for x in data.get("canonical_negative_controls", [])):
        errors.append("negative controls missing")
    if errors:
        raise ValueError("\n".join(sorted(set(errors))))
    statuses = dict(sorted(Counter(v["status"] for v in raw_nodes).items()))
    layers = dict(sorted(Counter(v["layer"] for v in raw_nodes).items()))
    direct = {
        key: {
            "status": by_id[key]["status"],
            "all": by_id[key]["requires_all"],
            "alternatives": by_id[key]["requires_any"],
        }
        for key in (*EXIT_IDS, "R04")
    }
    return {
        "status": "TYPED_DEPENDENCY_GRAPH_VALID",
        "proves_RH": False,
        "is_proof_checker": False,
        "node_count": len(raw_nodes),
        "layers": layers,
        "statuses": statuses,
        "topological_order": ordering,
        "rh_exits": direct,
        "stale_snapshot_requires_explicit_reconciliation": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", type=Path, default=DEFAULT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.graph.read_text(encoding="utf-8"))
    result = verify(data)
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
