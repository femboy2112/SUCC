#!/usr/bin/env python3
"""Certified finite law: the critical carry triple (A, m, d-m) is admissible
(16^d T_n <= 1 on [A,2A)) iff A >= 2^(2d-3) iff 16^d < (8A+1)(8A+2) (#521 CT-03).

Exact rational enclosures of T_n via the formally backed duck_bbp tail budget.
T_n is decreasing for n >= 1 because r is decreasing for m >= 2 (checked
symbolically below), so admissibility of A = N0 is decided at n = N0 and
failure of A = N0 - 1 at n = N0 - 1.  Usage: python admissibility_law.py [dmax]
Prints one JSON line; exit status 1 if any d breaks the law.
"""
import json
import sys

import sympy as sp

from observational_succ import duck_bbp


def r_decreasing_from_two() -> bool:
    m = sp.symbols("m", positive=True)
    r = sp.Rational(4) / (8 * m - 7) - sp.Rational(2) / (8 * m - 4) - sp.Rational(1) / (8 * m - 3) - sp.Rational(1) / (8 * m - 2)
    num = sp.numer(sp.together(sp.diff(r, m)))
    den = sp.denom(sp.together(sp.diff(r, m)))
    # r'(m) = num/den with den > 0 for m >= 2; shift m -> m+2 and check -num has nonnegative coefficients
    shifted = sp.Poly(sp.expand(-num.subs(m, m + 2)), m)
    den_pos = sp.Poly(sp.expand(den.subs(m, m + 2)), m)
    return all(c >= 0 for c in shifted.all_coeffs()) and all(c >= 0 for c in den_pos.all_coeffs())


def main(dmax: int) -> int:
    decreasing = r_decreasing_from_two()
    bad = []
    for d in range(2, dmax + 1):
        n0 = 2 ** (2 * d - 3)
        ct03 = (16 ** d < (8 * n0 + 1) * (8 * n0 + 2)) and not (16 ** d < (8 * (n0 - 1) + 1) * (8 * (n0 - 1) + 2))
        lo_prev, _ = duck_bbp.tail_interval(n0 - 1, d + 12)
        _, hi0 = duck_bbp.tail_interval(n0, d + 12)
        if not (ct03 and 16 ** d * hi0 <= 1 and 16 ** d * lo_prev > 1):
            bad.append(d)
    print(json.dumps({"law": "admissible(A,d) <=> A >= 2^(2d-3) <=> 16^d<(8A+1)(8A+2)",
                      "d_range": [2, dmax], "r_decreasing_m_ge_2": decreasing,
                      "exceptions": bad, "status": "CERTIFIED-FINITE" if decreasing and not bad else "FAILED"}))
    return 0 if decreasing and not bad else 1


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 200))
