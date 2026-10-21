"""Reproduce finite exact prime-carry / Euler pi transport receipt.

No numerical values of pi are inputs. Does not claim normality.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.pi_prime_carry_transport import (  # noqa: E402
    certified_pi_digit_prefix, certified_pi_digit_prefix_joint,
    doubling_carries, euler_prime_square_bracket, prime_carry_phase_clock,
    synchronized_pi_brackets, uniform_fourier_budget, wallis_pi_bracket,
    dyadic_midpoint_period_floor, wallis_midpoint, long_period_nonmixing_control,
)


def receipt() -> dict:
    source = ROOT / "observational_succ/pi_prime_carry_transport.py"
    cases = []
    for n in (1, 2, 3, 5, 10, 32, 100):
        lower, upper = wallis_pi_bracket(n)
        carries = doubling_carries(n)
        cases.append({
            "n": n,
            "nonzero_prime_carry_clocks": len(carries),
            "deepest_prime_power_carry": max(carries.values()),
            "wallis_interval_width": str(upper - lower),
            "certified_decimal_prefix_length_2": certified_pi_digit_prefix(n, 10, 2),
        })
    qcases = []
    for cutoff in (2, 3, 5, 11, 47, 200):
        lower, upper = euler_prime_square_bracket(cutoff)
        qcases.append({
            "prime_cutoff": cutoff,
            "pi_squared_interval_width": str(upper - lower),
        })
    denominator, residues = prime_carry_phase_clock(5, 2, 1, 12)
    return {
        "status": "exact_finite_only_no_pi_normality_claim",
        "theorem_basis": ["Wallis", "Gamma_factorials", "Legendre_Kummer", "Euler_zeta2", "Weyl_conditional"],
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "wallis_cases": cases,
        "euler_cases": qcases,
        "n_10000_certified_decimal_4": certified_pi_digit_prefix(10000, 10, 4),
        "n_10000_Q_200_joint_certified_decimal_4": certified_pi_digit_prefix_joint(10000, 200, 10, 4),
        "n_100_Q_200_joint_squared_width": str(synchronized_pi_brackets(100, 200)[1] - synchronized_pi_brackets(100, 200)[0]),
        "n_5_base_2_h_1_midpoint_phase_residue_clock": {"denominator": denominator, "residues": residues},
        "dyadic_period_samples": [
            {"level": j, "guaranteed_period_divisor": dyadic_midpoint_period_floor(j),
             "dyadic_midpoint_denominator_divisible_by_both_fermat_like_factors":
                wallis_midpoint(2 ** j).denominator %
                ((2 ** (j + 1) + 1) * (2 ** (j + 2) + 1)) == 0}
            for j in range(0, 9)
        ],
        "period_nonmixing_negative_control_N_12": {
            "period": long_period_nonmixing_control(12)[0],
            "strict_fourier_mean_distance_from_1_lt": str(long_period_nonmixing_control(12)[1]),
        },
        "symbolic_uniform_base_2_h_1_N_1000000": str(uniform_fourier_budget(2, 1, 1000000)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write reproducible JSON to this path")
    args = parser.parse_args()
    encoded = json.dumps(receipt(), indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(encoded, end="")
    else:
        args.output.write_text(encoded, encoding="utf-8")


if __name__ == "__main__":
    main()
