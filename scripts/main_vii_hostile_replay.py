#!/usr/bin/env python3
"""Classify the unchanged nine historical fixtures against an exact checkout.

Run each checkout in a fresh process. Historical exposure is expected evidence
of a defect, never a passing repaired-head regression. Documentation judgments
below are narrow inspected-text controls, not mathematical source authentication.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

_LEGACY = Path(__file__).with_name("cloud_hostile_holdouts.py")
_spec = importlib.util.spec_from_file_location("historical_cloud_f", _LEGACY)
_legacy = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_legacy)


def classify(record, source_texts):
    state, identifier = record["state"], record["id"]
    if state == "exposed":
        return "STILL EXPOSED"
    if state == "not_exposed":
        return "FIXED"
    if state == "rejected_or_exception":
        allowed = {"ProofContractError", "FrozenInstanceError", "ProofAuthorityError"}
        if identifier.startswith("F06"):
            allowed |= {"ValueError", "TypeError", "GoldbachCircleError"}
        return "FIXED" if record.get("exception") in allowed else "INVALID TEST"
    if state == "source_review_required":
        if identifier.startswith("F07") and all(s in source_texts["abc"] for s in
                ("ordinary", "NOT an implementation", "none of its remainder bounds")):
            return "FIXED"
        if identifier.startswith("F08") and (
                "S(N) = 2*C_2 * prod_{p | N, p odd} (p-1)/(p-2)" in source_texts["goldbach"]):
            return "FIXED"
        return "INAPPLICABLE"
    return "NEW FAILURE"


def replay(target):
    raw = _legacy.target_audit(target)
    texts = {"abc": (target/"observational_succ/abc_decomposition.py").read_text(),
             "goldbach": (target/"observational_succ/goldbach_circle.py").read_text()}
    for record in raw["findings"]:
        record["classification"] = classify(record,texts)
    raw["interpretation"] = "Historical defects and repaired regressions have opposite expectations."
    raw["fixture_script_sha256"] = hashlib.sha256(_LEGACY.read_bytes()).hexdigest()
    raw["classifier_script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-repo", type=Path, required=True)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--require-fixed",action="store_true")
    args = parser.parse_args()
    report = replay(args.target_repo)
    serialized = json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(serialized)
    print(serialized)
    if args.require_fixed and any(r["classification"] != "FIXED" for r in report["findings"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
