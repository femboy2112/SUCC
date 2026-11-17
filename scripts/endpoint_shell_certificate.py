#!/usr/bin/env python3
"""Exact finite BBP shell certificates from one source-rational endpoint.

No numerical pi, sampled orbit, randomized digit law, or asymptotic inference.
Run from the repository root. All reported lower bounds use integer/Fraction
arithmetic and the proved original-source bound 0 < T_N < r(N+1)/15 < 1.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.duck_bbp import forcing


def natural(value: int, name: str, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def terminal_state(n: int) -> Fraction:
    natural(n, "source depth")
    u = Fraction()
    for j in range(1, n + 1):
        u = 16 * u + forcing(j)
    return u


def grid_distance_bounds(a: int, q: int) -> tuple[int, int]:
    """Bounds Q*||t|| for t in [a/Q,(a+2)/Q], interpreted on the circle."""
    natural(q, "grid denominator", 2)
    if q % 2 or type(a) is not int or not 0 <= a < q:
        raise ValueError("an even grid denominator and 0 <= a < q are required")
    low = max(0, min(a, q - a - 2))
    high = min(q // 2, min(a, q - a) + 2)
    return low, high


def endpoint_grid_sums(c: int, max_shell: int, grid_digits: int) -> tuple[list[int], list[int]]:
    """Prefix sums of grid-distance squares for clocks 0 <= n < 2 max_shell.

    c is floor(U_N), N=2 max_shell+grid_digits. The unknown fractional endpoint
    and source tail together occupy less than two grid units at each clock.
    """
    natural(max_shell, "maximum shell")
    natural(grid_digits, "grid digits")
    if type(c) is not int:
        raise ValueError("integer terminal part required")
    q = 16 ** grid_digits
    lower, upper = [0], [0]
    for n in range(2 * max_shell):
        a = (c >> (4 * (2 * max_shell - n))) & (q - 1)
        lo, hi = grid_distance_bounds(a, q)
        lower.append(lower[-1] + lo * lo)
        upper.append(upper[-1] + hi * hi)
    return lower, upper


def finite_certificate(min_shell: int = 16, max_shell: int = 4096,
                       grid_digits: int = 6) -> dict:
    natural(min_shell, "minimum shell")
    natural(max_shell, "maximum shell")
    natural(grid_digits, "grid digits")
    if min_shell > max_shell:
        raise ValueError("minimum shell cannot exceed maximum shell")
    n = 2 * max_shell + grid_digits
    u = terminal_state(n)
    beta = forcing(n + 1) / 15
    if not 0 < beta < 1:
        raise AssertionError("the source-tail interval required by the grid proof failed")
    c = u.numerator // u.denominator
    q = 16 ** grid_digits
    low, high = endpoint_grid_sums(c, max_shell, grid_digits)
    lower_sums = [low[2*b] - low[b] for b in range(min_shell, max_shell + 1)]
    upper_sums = [high[2*b] - high[b] for b in range(min_shell, max_shell + 1)]
    phase_bounds = [Fraction(8*s, b*q*q)
                    for b, s in zip(range(min_shell, max_shell + 1), lower_sums)]
    i = min(range(len(phase_bounds)), key=phase_bounds.__getitem__)
    minimum = phase_bounds[i]
    # Hex serialization avoids Python's optional decimal-int display limit.
    canonical = f"{u.numerator:x}/{u.denominator:x}".encode("ascii")
    result = {
        "schema": "succ-endpoint-grid-certificate-v1",
        "status": "VERIFIED_FINITE",
        "source": "original four-pole BBP, literal U_0=0",
        "target_real": "pi/16 (classical BBP identity is an imported dependency)",
        "min_shell": min_shell,
        "max_shell": max_shell,
        "shell_count": max_shell - min_shell + 1,
        "source_depth": n,
        "grid_digits": grid_digits,
        "grid_denominator": q,
        "endpoint_sha256_hex_fraction": hashlib.sha256(canonical).hexdigest(),
        "endpoint_numerator_bits": u.numerator.bit_length(),
        "endpoint_denominator_bits": u.denominator.bit_length(),
        "tail_upper": str(beta),
        "completed_norm_bounds": "lower_sums[B-min_shell]/(B*Q^2) <= E_B <= upper_sums[B-min_shell]/(B*Q^2)",
        "terminal_norm_error": "|R_B-E_B| < r(2B+1)/(225*B)",
        "phase_loss_lower": "1-Re W_B >= 8*lower_sums[B-min_shell]/(B*Q^2)",
        "preregistered_claim": "1-Re W_B > 2/5 for every integer 16 <= B <= 4096 (default run only)",
        "all_exceed_two_fifths": all(v > Fraction(2, 5) for v in phase_bounds),
        "minimum_phase_lower_shell": min_shell + i,
        "minimum_phase_lower": str(minimum),
        "minimum_phase_lower_decimal_display": float(minimum),
        "lower_sums": lower_sums,
        "upper_sums": upper_sums,
        "boundary": "finite certificate only; no eventual lower bound or normality theorem"
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-shell", type=int, default=16)
    parser.add_argument("--max-shell", type=int, default=4096)
    parser.add_argument("--grid-digits", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = finite_certificate(args.min_shell, args.max_shell, args.grid_digits)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    summary = {key: value for key, value in result.items()
               if key not in {"lower_sums", "upper_sums"}}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
