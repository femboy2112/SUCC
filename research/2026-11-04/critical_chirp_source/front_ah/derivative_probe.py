"""Exact checks of the BBP tail derivative sandwich; not asymptotic evidence."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import factorial
from pathlib import Path

F = Fraction
HOLDOUT = (17, 193, 1021)
ORDERS = tuple(range(6))
SOURCE_SHA = "c9dfcdf057c4870f113e898464e4821c2ff5fedf"


def _arguments(n: int, k: int) -> None:
    if type(n) is not int or n < 1 or type(k) is not int or k < 0:
        raise ValueError("integer n>=1 and k>=0 required")


def signed_pole_derivative(n: int, k: int, *, omit_last: bool = False) -> F:
    """Return (-1)^k r^(k)(n) directly from the original four poles."""
    _arguments(n, k)
    poles = ((4, 7), (-2, 4), (-1, 3), (-1, 2))
    if omit_last:
        poles = poles[:-1]
    return factorial(k) * 8**k * sum(
        (F(c, (8 * n - a) ** (k + 1)) for c, a in poles), F(0)
    )


def positive_moment_derivative(n: int, k: int) -> F:
    """Independent positive beta-difference decomposition of (1-t)B(t)."""
    _arguments(n, k)
    coefficients = (4, 4, 4, 2, 1)
    value = F(0)
    for j, coefficient in enumerate(coefficients):
        a = 8 * n - 7 + j
        value += coefficient * (F(1, a ** (k + 1)) - F(1, (a + 1) ** (k + 1)))
    return factorial(k) * 8**k * value


def tail_derivative_interval(n: int, k: int, terms: int = 24) -> tuple[F, F]:
    _arguments(n, k)
    if type(terms) is not int or terms < 1:
        raise ValueError("positive integer terms required")
    lower = sum(
        (signed_pole_derivative(n + j, k) / 16**j for j in range(1, terms + 1)),
        F(0),
    )
    # Complete monotonicity of the positive moment proves this remainder bound.
    upper = lower + positive_moment_derivative(n + terms + 1, k) / (15 * 16**terms)
    return lower, upper


def claimed_interval(n: int, k: int) -> tuple[F, F]:
    _arguments(n, k)
    leading = F(factorial(k + 1), 64 * n ** (k + 2))
    error = F(7 * factorial(k + 2), 1024 * n ** (k + 3))
    return leading - error, leading


def row(n: int, k: int) -> dict:
    lower, upper = tail_derivative_interval(n, k)
    claimed_lower, claimed_upper = claimed_interval(n, k)
    source_equal = all(
        signed_pole_derivative(n + j, k) == positive_moment_derivative(n + j, k)
        for j in range(1, 26)
    )
    inside = claimed_lower < lower < upper < claimed_upper
    assert source_equal and inside
    return {
        "n": n,
        "derivative_order": k,
        "four_pole_equals_positive_moment": source_equal,
        "strict_interval_containment": inside,
        "tail_lower": str(lower),
        "tail_upper": str(upper),
        "claimed_lower": str(claimed_lower),
        "claimed_upper": str(claimed_upper),
    }


def receipt() -> dict:
    rows = [row(n, k) for n in HOLDOUT for k in ORDERS]
    raw = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    # A changed-forcing control has an O(1/n) contribution and violates k=0.
    mutant_lower = sum(
        (signed_pole_derivative(17 + j, 0, omit_last=True) / 16**j for j in range(1, 25)),
        F(0),
    )
    mutation_detected = mutant_lower > claimed_interval(17, 0)[1]
    assert mutation_detected
    return {
        "source_sha": SOURCE_SHA,
        "status": "finite exact checks; paper proof separate; selected Weyl gate OPEN",
        "holdout_n": list(HOLDOUT),
        "derivative_orders": list(ORDERS),
        "rows_sha256": hashlib.sha256(raw).hexdigest(),
        "dropped_fourth_pole_detected": mutation_detected,
        "rows": rows,
    }


def output() -> str:
    return json.dumps(receipt(), sort_keys=True, indent=2) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    result = output()
    if args.write:
        args.write.write_text(result)
    if args.verify:
        if args.verify.read_text() != result:
            raise AssertionError("tail derivative receipt mismatch")
        print("TAIL_DERIVATIVE_RECEIPT_VERIFIED")
    if not args.write and not args.verify:
        print(result)
