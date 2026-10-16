#!/usr/bin/env python3
"""Exact declared finite models; does not evaluate the authentic Suzuki source."""
import argparse
from dataclasses import asdict
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import observer_schur as O
from observational_succ.source_field_inverse_limits import FieldSourcePassport


def model(rows, name):
    space = O.RationalSourceSpace(FieldSourcePassport(name, "low-coordinate-observer", 0),
                                  tuple(f"e{i}" for i in range(len(rows))))
    return O.QuadraticModel(space, rows)


def report():
    models = {
        "cross_term_mutant": ((0, 1), (1, 0)),
        "positive_diagonal": ((1, 0), (0, 1)),
        "positive_blocks_negative_schur": ((1, 2), (2, 1)),
        "positive_original_negative_lower_certificate": ((2, 1), (1, 1)),
        "singular_range_valid": ((3, 2, 0), (2, 2, 0), (0, 0, 0)),
        "D_zero_negative_low": ((-1, 0), (0, 0)),
    }
    examples = {}
    for name, rows in models.items():
        s = O.BlockModel(model(rows, "DECLARED_MODEL:"+name), 1)
        examples[name] = {
            "source": asdict(s.model.space), "matrix": s.model.gram,
            "energy": O.energy_factorization(s.model, s.observation),
            "sign": O.sign_factorization(s), "envelope": O.schur_envelope(s),
            "fiber_at_one": O.fiber_envelope(s, (1,)),
        }
        if O.pd(s.a) and examples[name]["envelope"]["all_fibers_finite"]:
            examples[name]["contraction"] = O.contraction_certificate(s)
    s = O.BlockModel(model(((2, 1), (1, 1)), "DECLARED_MODEL:conservative-lower"), 1)
    examples["failed_sufficient_lower"] = O.trial_enclosure(s, ((0,),), ((1,),), F(1, 10))
    files = (
        "AGENTS.md", "provenance/IMPORT_MANIFEST.json",
        "observational_succ/observer_schur.py", "tests/test_observer_schur.py",
        "scripts/observer_schur_probe.py", "observational_succ/recursive_operator_gluing.py",
        "observational_succ/source_field_inverse_limits.py",
        "observational_succ/source_weil_hierarchy.py",
        "observational_succ/four_low_schur_proof_teeth.py",
        "research/2026-10-15/FOUR_LOW_SCHUR_CROSSPOLLINATION.md",
        "reviews/2026-10-15_PROOF_TEETH_SCHUR_INDEPENDENT_AUDIT.md",
        "research/2026-10-15/proof_teeth_receipts/FINAL_VALIDATION_SUMMARY.json",
        "research/2026-10-16/OBSERVER_SCHUR_THEOREMS.md",
    )
    return {
        "schema": "observer-schur-finite-models-v1", "python": sys.version,
        "git_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "git_branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip(),
        "sha256": {name: sha256((ROOT/name).read_bytes()).hexdigest() for name in files},
        "examples": examples, "authority": "EXACT_FINITE_CHECK",
        "source_identification_discharged": False,
        "paper_theorems": [f"OS-{n:02}" for n in range(1, 9)],
        "paper_proofs_are_not_inferred_from_this_run": True,
        "Lean_kernel_replayed": False, "original_Suzuki_sign": "OPEN", "RH_proved": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(report(), indent=2, sort_keys=True, default=str)+"\n"
    if args.output:
        args.output.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
