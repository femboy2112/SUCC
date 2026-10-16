#!/usr/bin/env python3
"""Deterministic stdlib-only Gamma certificates and hostile alias controls."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.collective_gamma import (
    SOURCE_COMMIT, SOURCE_MODULE_SHA256, GammaCertificateError, Strip,
    certify_gamma, cooperative_gamma, decode_lanes, is_joint_period,
    joint_period_pi, rational_gcd, uniform_error,
)


def run():
    strip = Strip(1, 4, 4)
    certificates = [certify_gamma(s, t, F(1, 8), -512, 32, strip=strip)
                    for s, t in ((1, 0), (2, 0), (F(3, 2), F(5, 3)), (4, -4))]
    if not all(c.coordinate_radius < F(1, 10**12) for c in certificates):
        raise AssertionError("The declared actual-evaluation precision target failed")
    if not certificates[0].enclosure.real.contains(1):
        raise AssertionError("Normative Gamma_R(1)=1 control failed")
    budgets = [uniform_error(h, strip, int(-64/h), int(4/h))
               for h in (F(1, 2), F(1, 4), F(1, 8))]
    if not budgets[2].alias < budgets[1].alias < budgets[0].alias:
        raise AssertionError("Mesh refinement did not improve the alias bound")

    # Fixed rational near 8*pi; no irrational input is rounded and relabelled.
    t = F(1256637, 50000)
    alias_strip = Strip(1, 1, 26)
    coarse = certify_gamma(1, t, F(1, 2), -160, 12, strip=alias_strip)
    cooperative, lanes = cooperative_gamma(1, t, F(1, 2), 2, -320, 24, strip=alias_strip)
    duplicate = decode_lanes((lanes[0][1], lanes[0][1]))
    if min(coarse.finite_sum.real.lower, duplicate.real.lower) <= F(99, 100):
        raise AssertionError("Coarse/duplicate first-alias counterexample disappeared")
    if any(max(abs(x.lower), abs(x.upper)) >= F(1, 1000)
           for x in (cooperative.enclosure.real, cooperative.enclosure.imag)):
        raise AssertionError("Cooperative near-alias enclosure too wide")
    missing_rejected = False
    try:
        cooperative_gamma(1, t, F(1, 2), 2, -320, 24, strip=alias_strip, lanes=(0,))
    except GammaCertificateError:
        missing_rejected = True
    if not missing_rejected:
        raise AssertionError("Incomplete source coverage accepted")

    meshes = (F(1, 2), F(1, 3))
    if joint_period_pi(meshes) != 24 or is_joint_period(meshes, 8) or is_joint_period(meshes, 12):
        raise AssertionError("Rational tuple-period control failed")
    files = ("observational_succ/collective_gamma.py", "tests/test_collective_gamma.py",
             "scripts/collective_gamma_probe.py", "research/2026-10-16/COLLECTIVE_GAMMA_CLOCKS.md")
    return {
        "schema": "collective-gamma-certified-evaluation-v1",
        "claims": {
            "joint_rational_period_and_tuple_only_obstruction": "PROVED PAPER",
            "line_uniform_error_at_least_Gamma_R_sigma_over_2": "PROVED PAPER",
            "whole_positive_halfplane_absolute_error_unbounded": "PROVED PAPER",
            "finite_strip_analytic_bound": "PROVED PAPER, credits BGD-3/4",
            "complete_lane_interleaving": "CLASSICAL / credits BGD-1",
            "actual_evaluated_rectangles": "RATIONAL INTERVAL CERTIFICATES, Decimal.exp trust boundary",
            "controls": "EXACT FINITE TESTS; not independent universal proofs",
            "incommensurate_Gamma_tuple_injectivity": "NOT CLAIMED",
            "kernel_checked_proof": False,
        },
        "dependencies": {
            "PR141_commit": SOURCE_COMMIT, "PR141_module_sha256": SOURCE_MODULE_SHA256,
            "concurrent_branch": "research/gamma-band-dealias-interleaving-2026-10-16",
            "concurrent_observed_commit": "6623fd11b710a40dc5f9cd2375ba74d759be0245",
            "concurrent_module_sha256": "ff01af58064f05a96aabee5bf31cdc4a56ec15d2beb9f1c79b308d709d074b37",
            "imports": "Python stdlib only; no sibling modules vendored or imported",
        },
        "owned_file_sha256": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files},
        "tuple": {"meshes": [str(h) for h in meshes], "rational_gcd": str(rational_gcd(meshes)),
                  "least_period_pi_multiplier": str(joint_period_pi(meshes)),
                  "individual_periods_are_joint": [is_joint_period(meshes, 8), is_joint_period(meshes, 12)],
                  "exact_halfplane_error_floor": "1/(81*sigma) < Gamma_R(sigma)/2"},
        "fine_certificates": [c.as_dict() for c in certificates],
        "uniform_strip_mesh_controls": [
            {"mesh": str(h), **b.as_dict()} for h, b in zip((F(1, 2), F(1, 4), F(1, 8)), budgets)],
        "near_first_alias_control": {
            "rational_height": str(t), "coarse": coarse.as_dict(),
            "cooperative": cooperative.as_dict(),
            "lane_values": [{"lane": j, "value": value.as_dict()} for j, value in lanes],
            "duplicate_lane_decoder": duplicate.as_dict(),
            "coarse_and_duplicate_real_gt_99_over_100": True,
            "cooperative_both_coordinate_magnitudes_lt_1_over_1000": True,
            "missing_lane_rejected": missing_rejected,
        },
        "limits": ["absolute right-half-plane finite-strip certificates only",
                   "no relative error, no global reconstruction, no incommensurate injectivity",
                   "no prime-source derivation or signed-Weil identification",
                   "classical analytic proofs, not proof-assistant certificates"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", action="store_true", help="all controls are always enforced")
    args = parser.parse_args()
    blob = json.dumps(run(), sort_keys=True, indent=2)+"\n"
    if args.output is None:
        print(blob, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(blob, encoding="utf-8")


if __name__ == "__main__":
    main()
