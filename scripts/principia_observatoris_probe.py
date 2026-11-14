#!/usr/bin/env python3
"""Replay a bounded exact Principia certificate bank and native source adapter."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import hashlib
import json
from fractions import Fraction as Q

from observational_succ.principia_observatoris import (
    LinearModel, predictive_completion, quotient_defect, linear_separator,
    difference_model, bbp_forcing, bbp_rank_predictor, bbp_rank_error_bound,
)
from observational_succ.bbp_euler_mascheroni import forcing as native_forcing


def main():
    root = Path(__file__).resolve().parents[1]
    p, a = ((1, 0),), ((0, 1), (0, 0))
    closure = predictive_completion(p, (a,))
    defect = quotient_defect(p, a)
    assert closure["added_coordinates"] == 1 and not defect["descends"]
    left = LinearModel("left", (((0, 0), (0, 1)),), ((1,), (1,)), ((Q(-1, 6), Q(1, 2)),))
    right = LinearModel("right", (((2, 0), (0, 3)),), ((1,), (1,)), ((Q(1, 2), Q(-1, 6)),))
    separation = linear_separator(difference_model(left, right))
    assert separation["word"] == (0, 0, 0)
    source_indices = tuple(range(1, 129)) + (257, 1009, 4093)
    assert all(bbp_forcing(n) == native_forcing(n) for n in source_indices)
    forcing = []
    for start in (1, 7, 41):
        for d in range(1, 6):
            fit = bbp_rank_predictor(start, d)
            assert all(fit["model"].response((0,)*k)[0][0] == bbp_forcing(start+k)
                       for k in range(2*d))
            lower = bbp_rank_error_bound(start, d)
            assert 0 < lower <= fit["next_error"]
            forcing.append({"start": start, "dimension": d, "matched_count": 2*d,
                            "next_error": str(fit["next_error"]),
                            "all_model_error_lower_bound": str(lower)})
    paths = ("observational_succ/principia_observatoris.py",
             "observational_succ/bbp_euler_mascheroni.py",
             "scripts/principia_observatoris_probe.py")
    record = {
        "status": "EXACT_FINITE_CHECKS_PASS", "source_files": {
            path: hashlib.sha256((root/path).read_bytes()).hexdigest() for path in paths},
        "quotient_defect": defect, "minimal_refinement": closure,
        "sharp_linear_separator": separation,
        "native_bbp_cross_checks": len(source_indices), "forcing_certificates": forcing,
        "authority": "Finite rational model replay; universal results have separate paper proofs",
        "physical_events": 0, "new_lean_pass": False,
        "pi_normality": "OPEN", "scholarly_priority": "NOT_CLAIMED",
    }
    print(json.dumps(record, indent=2, default=str))


if __name__ == "__main__":
    main()
