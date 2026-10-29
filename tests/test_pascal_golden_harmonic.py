"""Independent finite exact Q(sqrt5) checks, not a proof of π normality."""
from __future__ import annotations

import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "research/2026-10-29/oily_triangle_sheet/pascal_golden_harmonic.py"
SPEC = importlib.util.spec_from_file_location("pascal_golden_harmonic_research", PATH)
s = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(s)


class GoldenPascalArithmeticTests(unittest.TestCase):
    def test_golden_mass_and_fixed_point(self):
        self.assertEqual(s.add(s.LAMBDA,s.LAMBDA_SQUARED),s.ONE)
        self.assertEqual(s.pow_element(s.LAMBDA,2),s.LAMBDA_SQUARED)
        self.assertEqual(s.golden_packet_fixed_point_residual(),s.ZERO)
        # The one-stage Oily counterfeit 1/(2-z) has no interior fixed point.
        self.assertNotEqual(s.LAMBDA_SQUARED, s.ONE)
        self.assertEqual(s.mul(s.LAMBDA_SQUARED,s.add((F(2),F(0)),s.scale(s.LAMBDA_SQUARED,-1))),s.LAMBDA)

    def test_every_golden_weighted_pascal_row_normalized(self):
        for n in range(45):
            self.assertEqual(s.pascal_row_mass(n),s.ONE)

    def test_markov_local_pascal_gluing(self):
        for n in range(35):
            for k in range(n+2):
                left=s.mul(s.LAMBDA,s.weighted_pascal(n,k)) if k<=n else s.ZERO
                right=s.mul(s.LAMBDA_SQUARED,s.weighted_pascal(n,k-1)) if k>=1 else s.ZERO
                self.assertEqual(s.weighted_pascal(n+1,k),s.add(left,right))

    def test_direct_vs_harmonic_closed(self):
        for n in range(33):
            self.assertEqual(s.harmonic_pascal_direct(n),s.harmonic_pascal_closed(n))

    def test_alternating_pascal_transform(self):
        for n in range(34):
            self.assertEqual(s.harmonic_pascal_alternating(n),s.harmonic_pascal_closed(n))

    def test_harmonic_increments(self):
        for n in range(45):
            self.assertEqual(s.add(s.harmonic_pascal_closed(n+1),s.scale(s.harmonic_pascal_closed(n),-1)),s.harmonic_increment(n))

    def test_fibonacci_pascal_diagonals(self):
        for n in range(60):
            self.assertEqual(s.fibonacci_diagonal(n),s.fibonacci(n+1))

    def test_pascal_transform_golden_reciprocity(self):
        for n in range(38):
            self.assertEqual(s.binomial_golden_transform(n),s.pow_element(s.add(s.ONE,s.LAMBDA),n))
            self.assertEqual(s.mul(s.binomial_golden_transform(n),s.pow_element(s.LAMBDA,n)),s.ONE)

    def test_wrong_seed_and_invalid_shape(self):
        for value in [-1,0.5,True,"2"]:
            with self.assertRaises(ValueError):
                s.pascal_row_mass(value)
        for n,k in [(-1,0),(1,-1),(1,2),(4,1.5)]:
            with self.assertRaises(ValueError):
                s.weighted_pascal(n,k)

    def test_wrong_golden_identification_control(self):
        # Generic p=1/2 still yields an Euler-gamma finite part, but is not
        # the Oily fixed point: this is a countermodel to unique selection.
        p=F(1,2)
        self.assertNotEqual(p*(2-p)**2,1)
        # Exact general binomial-harmonic identity at p=1/2, n<=20.
        from math import comb
        for n in range(21):
            direct=sum((F(comb(n,k),2**n)*s.harmonic(k) for k in range(n+1)),F(0))
            formula=s.harmonic(n)-sum((F(1,2**j*j) for j in range(1,n+1)),F(0))
            self.assertEqual(direct,formula)


if __name__ == "__main__":
    unittest.main()
