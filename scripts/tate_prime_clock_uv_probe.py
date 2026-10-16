"""Deterministic, exact-rational DYSPON-SPHERE clock / first-prime receipt.

Run from a complete source checkout; the authentic source-pinning check
requires original SUCC provenance. No sampling or zero lookup is involved.
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from observational_succ.tate_prime_clock_uv import (
    shift_path_geometry, exact_two_cell_negative_witness,
    genuine_first_prime_sparse_weil_certificate,
)


def exact_receipt():
    window = shift_path_geometry(F(1, 2), F(3, 4))
    witness = exact_two_cell_negative_witness(F(1, 2), F(3, 4))
    original = genuine_first_prime_sparse_weil_certificate()
    return {
        "schema": "SUCC_TATE_PRIME_CLOCK_UV_v2",
        "status": "SOURCE_RESTRICTED_POSITIVITY_NOT_RH",
        "synthetic_rational_clock": {
            "a": "1/2",
            "b": "3/4",
            "path_vertices": window["maximum_essential_chain_vertices"],
            "brownian_energy": str(witness["brownian_energy"]),
            "prime_only_signed_energy": str(witness["original_shape_prime_signed_energy"]),
            "sharp_relative_negative": str(witness["sharp_relative_negative"]),
            "not_a_genuine_prime": True,
        },
        "original_zeta_source": {
            "a": str(original["radius"]),
            "prime_labels": list(original["actual_prime_power_labels"]),
            "test_support_measure_max": str(original["support_measure_max"]),
            "gamma_modes_in_analytic_lower_bound": original["gamma_clock_modes"],
            "gamma_exact_rational_lower": str(original["gamma_exact_L2_lower"]),
            "uniform_margin_exact_lower": str(original["uniform_source_margin_exact_lower"]),
            "real_contact_strictly_below": str(original["completed_real_contact_strict_upper"]),
            "prime_shift_strictly_below": str(original["first_prime_shift_strict_upper"]),
            "negative_pole_strictly_below": str(original["negative_pole_strict_upper"]),
            "Weil_L2_margin_strictly_above": str(original["original_completed_Weil_L2_margin_strictly_above"]),
            "all_tests_at_a_half": False,
            "RH_proved": False,
        },
    }


if __name__ == "__main__":
    data = exact_receipt()
    if sys.argv[1:] == ["--verify"]:
        path = Path(__file__).resolve().parents[1] / "research/2026-10-15/TATE_PRIME_CLOCK_UV_RECEIPT.json"
        expected = json.loads(path.read_text(encoding="utf-8"))
        if data != expected:
            raise SystemExit("DYS-UV exact receipt diverges from original source")
        print("DYS-UV original-source receipt verified")
    elif not sys.argv[1:]:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        raise SystemExit("usage: python scripts/tate_prime_clock_uv_probe.py [--verify]")
