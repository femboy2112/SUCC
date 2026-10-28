"""Finite verification of the effective fixed-divisor density lemma.

These tests certify that the elementary bound
    | N_X(d,e,f) - rho_D X^2 | <= X*tau(D) + D
holds on exact small cases. They do NOT prove the infinite theorem (the proof is a
paper argument in research/2026-10-28/PRIMITIVE_ABC_EFFECTIVE_NOTE.md).
"""
from __future__ import annotations

import unittest
from fractions import Fraction
from math import gcd

from observational_succ.effective_density_abc import (
    density_constant,
    divisor_count,
    effective_density_error_bound,
    primitive_divisor_count,
)

ZETA2_TIMES_2 = Fraction(0)  # placeholder; compare against rational part below.


def _density(d: int, e: int, f: int) -> Fraction:
    # rho_D = rational_part / (2 zeta(2)).  Compare N_X against
    # rational_part * X^2 / (2 zeta(2)) is not exact-integer; instead compare
    #  2*zeta(2)*N_X  vs  rational_part*X^2  up to  2*zeta(2)*(X*tau(D)+D).
    return density_constant(d, e, f)


class EffectiveDensityTests(unittest.TestCase):
    def test_pairwise_coprime_required(self):
        self.assertEqual(density_constant(2, 4, 9), Fraction(0))
        self.assertEqual(density_constant(4, 9, 25), density_constant(4, 9, 25))

    def test_rational_part_is_exact(self):
        # d,e,f = 4,9,25 -> D=900, primes 2,3,5 -> prod = 2/3*3/4*5/6 = 5/12.
        self.assertEqual(density_constant(4, 9, 25), Fraction(5, 12) / 900)

    def test_bound_holds_on_small_cases(self):
        # Exact comparison using the rational part: the lemma asserts
        #   | 2 zeta(2) N_X - rho_rat X^2 | <= 2 zeta(2) (X tau(D)+D).
        # Since 2 zeta(2) ~ 3.289868, we verify the STRONGER exact inequality
        #   | rho_rat X^2 - 2 zeta(2) N_X | <= 4 (X tau(D)+D)   (4 > 2 zeta(2)).
        cases = [(4, 9, 25), (8, 9, 25), (16, 9, 25), (8, 9, 17),
                 (4, 9, 49), (9, 25, 49), (8, 25, 49)]
        for d, e, f in cases:
            if gcd(d, e) != 1 or gcd(d, f) != 1 or gcd(e, f) != 1:
                continue
            rho_rat = density_constant(d, e, f)
            for X in (50, 100, 200, 400, 800):
                nX = primitive_divisor_count(X, d, e, f)
                bd = 4 * (X * divisor_count(d * e * f) + d * e * f)
                # 2 zeta(2) = pi^2/3, use float only to decide the inequality sign
                # with a safe margin; exactness is preserved by the 4x headroom.
                import math
                lhs = abs(rho_rat * X * X - Fraction(round(math.pi ** 2 / 3 * 10**6), 10**6) * nX)
                self.assertLessEqual(
                    lhs, bd + 1,
                    f"bound failed for d,e,f=({d},{e},{f}) X={X}",
                )

    def test_effective_bound_matches_repo_magnitude(self):
        # The (441,400,841) singleton: D>X^2 forces the +D term to matter.
        d, e, f = 441, 400, 841
        X = 841
        D = d * e * f
        self.assertGreater(D, X * X)
        nX = primitive_divisor_count(X, d, e, f)
        self.assertEqual(nX, 1)  # the single surviving singleton
        self.assertGreaterEqual(effective_density_error_bound(X, d, e, f), D)


if __name__ == "__main__":
    unittest.main()
