#!/usr/bin/env python3
"""Replay deterministic exact Reality Pin witnesses and verify their source blobs."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.reality_pin_geometry import (
    GraphPassport, boundary_moments, coordinate_boundary,
    first_return_extension, reconstruct_zero_forcing, zero_forcing_schedule,
)
from observational_succ.reality_pin_arithmetic import (
    boundary_resolvent_enclosure, finite_second_moment, galerkin_norm_bound,
)
from observational_succ.reality_pin_quantum_global import quantum_global_receipt
from observational_succ.reality_pin_selection import synthetic_rc_receipt
from observational_succ.reality_pin_continuum import (
    known_capacity_pin, line_invariants, line_response_interval, ratio_interval,
)


def git_blob(path):
    data = (ROOT / path).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def run():
    edges = ((0, 1, -1), (1, 2, -1), (1, 3, -1), (3, 4, -1), (3, 5, -1))
    passport = GraphPassport(6, (0, 2, 4, 5), edges, "synthetic-six-node-tree")
    a = ((5,-1,0,0,0,0), (-1,8,-2,-1,0,0), (0,-2,6,0,0,0),
         (0,-1,0,9,-2,-3), (0,0,0,-2,5,0), (0,0,0,-3,0,7))
    moments = boundary_moments(a, coordinate_boundary(6, passport.boundary), 5)
    recovered = reconstruct_zero_forcing(passport, moments)
    assert recovered == a
    extension = first_return_extension(
        ((4,-2,0),(-2,6,-3),(0,-3,5)), ((1,),(0,),(0,)),
        ((0,0),(0,0),(Q(2,3),Q(5,7))))
    assert extension == (6, ((Q(1684,49),),))
    quantum = quantum_global_receipt()
    assert quantum["K_rho_minus_rho_K_1_3"] == "-32/441"
    rc = synthetic_rc_receipt()
    assert not rc["physical_measurements_performed"]
    assert rc["dc_selection"]["models"] == ("direct", "series-capacitor")
    assert rc["calibration_selection"]["models"] == ("series-capacitor",)
    assert rc["heldout_selection"]["models"] == ("series-capacitor",)
    line_ratio = ratio_interval(1, Q(1, 10**8))
    line_pin = known_capacity_pin(Q(1,2), 3, Q(1,24), line_ratio, Q(1,10**6))
    assert line_pin["length"][0] < 4 < line_pin["length"][1]
    assert line_pin["conductivity"][0] < 2 < line_pin["conductivity"][1]
    assert line_invariants(2,3,4) == line_invariants(1,6,2)
    paths = sorted(
        [p.relative_to(ROOT).as_posix() for folder, pattern in (
            ("observational_succ", "reality_pin_*.py"),
            ("tests", "test_reality_pin_*.py"),
            ("scripts", "*reality_pin*.py"))
         for p in (ROOT / folder).glob(pattern)]
        + ["formal/RealityPin.lean", "lean-toolchain",
           "observational_succ/boundary_realization_selection.py",
           "observational_succ/spectral_boundary_rigidity.py"])
    return {
        "schema": "succ-reality-pin-exact-v1",
        "parent_commit": "d2f760ab9d9a11719e950caeb2d54bfa5114f495",
        "source_git_blobs": {p: git_blob(p) for p in paths},
        "geometry": {"known_labelled_tree_reconstructed": recovered == a,
                     "source_size": 6, "boundary": passport.boundary,
                     "maximum_moment_order": 5,
                     "forcing_schedule": zero_forcing_schedule(passport),
                     "block_extension_first_return_order": extension[0],
                     "block_extension_jump": str(extension[1][0][0])},
        "arithmetic": {"finite_second_moment_N7_lambda1_sigma2": str(finite_second_moment(7)),
                       "infinite_m_enclosure_N4_lambda0_sigma2_s5":
                           list(map(str, boundary_resolvent_enclosure(4,lam=0,s=5,terms=4))),
                       "norm_resolvent_horizon_bound_N4_lambda0_sigma2_s5":
                           str(galerkin_norm_bound(4,lam=0,s=5,terms=4))},
        "quantum": quantum, "synthetic_rc": rc,
        "synthetic_continuum": {
            "source_conductivity_capacity_length": ["2", "3", "4"],
            "known_capacity_pin": {k: list(map(str, line_pin[k]))
                                   for k in ("length", "conductivity")},
            "heldout_s1_over6_response": list(map(str,
                line_response_interval(2,3,4,Q(1,6)))),
            "same_complete_response_different_source": ["1", "6", "2"],
            "physical_measurements_performed": False,
        },
        "scope": {"exact_rational_oracles": True,
                  "infinite_operator_bounds_justified_by_paper_proof": True,
                  "paper_theorems_kernel_certified": False,
                  "physical_measurements_performed": False,
                  "scalar_arithmetic_cyclicity_proved": False,
                  "unknown_physical_topology_uniquely_identified": False,
                  "alpha_or_gamma_physical_prediction": False,
                  "signed_Weil_positivity_or_RH_proved": False,
                  "independent_academic_novelty_claimed": False},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = run()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check:
        frozen = ROOT / "research/2026-10-22/REALITY_PIN_EXACT_RECEIPT.json"
        if json.loads(encoded) != json.loads(frozen.read_text()):
            raise SystemExit("FAIL: exact receipt or its source fingerprints changed")
    print(encoded, end="")


if __name__ == "__main__":
    main()
