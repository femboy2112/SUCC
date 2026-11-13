#!/usr/bin/env python3
"""Exact independent arithmetic audit of SOURCE_TRANSPORT.md.

No floating-point phases, repository theorem implementations, or external
packages are used. The output is a finite regression receipt, not the proof
of the manuscript's universal statements.
"""
from fractions import Fraction
import json
from pathlib import Path

F = Fraction


def source(n):
    """Literal four-pole source, with exact rational coefficients."""
    return F(4, 8*n-7) - F(2, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def tail_interval(n, terms=20):
    lower = sum((source(n+j) / 16**j for j in range(1, terms+1)), F(0))
    upper = lower + source(n+terms+1) / (15 * 16**terms)
    return lower, upper


def rational(value):
    return [value.numerator, value.denominator]


def main():
    budget_cases = 0
    for B in range(1, 101):
        prefix = [F(0)]
        for n in range(B, 2*B):
            prefix.append(prefix[-1] + F(1, n*n))
        for H in range(1, B+1):
            exact = sum((
                F(H-lag, H) * (prefix[lag] - (prefix[B] - prefix[B-lag]))
                for lag in range(1, H)
            ), F(0)) / (16*H*B)
            bound = F(H*H-1, 128*H*B**3)
            assert 0 <= exact <= bound, (B, H, exact, bound)
            budget_cases += 1

    tail_cases = []
    for n in (1, 2, 7, 31, 127, 509):
        for lag in (1, 2, 7, 31):
            lower, upper = tail_interval(n)
            later_lower, later_upper = tail_interval(n+lag)
            diff_lower, diff_upper = lower-later_upper, upper-later_lower
            bound = F(1, 64) * (F(1, n*n) - F(1, (n+lag)**2))
            assert 0 < diff_lower <= diff_upper < bound, (n, lag)
            tail_cases.append({
                "n": n,
                "lag": lag,
                "difference_lower": rational(diff_lower),
                "difference_upper": rational(diff_upper),
                "bound": rational(bound),
            })

    # Coefficient identity in ST-3, encoded in ascending powers of t.
    def multiply(a, b):
        out = [0] * (len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        return out

    denominator = multiply([1, 16, 64], [4, 32, 64])
    residual = [a-b for a, b in zip(denominator, [0, 0, 0, 768, 4096])]
    assert residual == [4, 96, 832, 2304, 0]
    assert all(c >= 0 for c in residual) and residual[0] > 0

    report = {
        "status": "PASS",
        "scope": "finite exact arithmetic regression; universal proof in SOURCE_TRANSPORT.md",
        "arithmetic": "fractions.Fraction and integer polynomial coefficients",
        "fejer_endpoint_budget_cases": budget_cases,
        "fejer_ranges": {"B": [1, 100], "H": "all integers 1 through B"},
        "tail_interval_cases": len(tail_cases),
        "tail_terms": 20,
        "tail_remainder": "16^(-20) r(n+21)/15",
        "derivative_polynomial_residual_ascending": residual,
        "tail_results": tail_cases,
    }
    destination = Path(__file__).with_name("SOURCE_AUDIT.json")
    destination.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": report["status"],
        "fejer_endpoint_budget_cases": budget_cases,
        "tail_interval_cases": len(tail_cases),
        "derivative_polynomial_identity": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
