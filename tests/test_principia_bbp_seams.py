"""Exact mathematical checks, source mutations and capacity boundary controls."""

import unittest
from fractions import Fraction as F

from observational_succ import principia_bbp_seams as s


class BBPMomentSeamTests(unittest.TestCase):
    def test_original_four_signed_poles(self):
        for k in range(40):
            expected = F(4, 8*k+1) - F(2, 8*k+4) - F(1, 8*k+5) - F(1, 8*k+6)
            self.assertEqual(s.moment(k), expected)
            self.assertGreater(expected, 0)

    def test_one_seam_exact_value(self):
        # An independent hand-reduced first ratio, not fitted decimal data.
        self.assertEqual(s.moment(0), F(47, 15))
        self.assertEqual(s.moment(1), F(106, 819))
        self.assertEqual(s.orthogonal_polynomial(1), (-F(530,12831), F(1)))
        self.assertLess(s.evaluate(s.orthogonal_polynomial(1), 0), 0)
        self.assertGreater(s.evaluate(s.orthogonal_polynomial(1), 1), 0)

    def test_null_tower_and_first_surviving_jet(self):
        for n in range(9):
            p = s.orthogonal_polynomial(n)
            for j in range(n):
                self.assertEqual(s.moment_pair(p, j), 0)
                self.assertEqual(s.resolvent_hasse_jet(p, j), 0)
            h = s.inner(p, p)
            self.assertGreater(h, 0)
            self.assertEqual(s.moment_pair(p, n), h)
            self.assertEqual(s.resolvent_hasse_jet(p, n), h / 16**(n+1))

    def test_full_cross_coupling_not_diagonal_energy(self):
        p = s.orthogonal_polynomial(1)
        diagonal = sum(c*c*s.moment(2*i) for i,c in enumerate(p))
        self.assertNotEqual(s.inner(p,p), diagonal)
        self.assertGreater(diagonal, s.inner(p,p))

    def test_roots_of_different_scalar_channels_are_distinct(self):
        ratios = [s.moment_ratio(k) for k in range(32)]
        self.assertTrue(all(0 < x < 1 for x in ratios))
        self.assertTrue(all(x < y for x,y in zip(ratios,ratios[1:])))
        # No simultaneous null for adjacent centered monomial channels.
        for k in range(31):
            self.assertGreater(s.moment(k+2)-ratios[k]*s.moment(k+1), 0)

    def test_source_mutation_breaks_declared_null(self):
        p = s.orthogonal_polynomial(2)
        original = s.moment_pair(p,0)
        changed_first_moment = original + p[1]  # m1 -> m1+1
        self.assertEqual(original,0)
        self.assertNotEqual(changed_first_moment,0)
        self.assertNotEqual(s.moment_pair((p[0]+1,)+p[1:],0),0)

    def test_inverse_identity_exact(self):
        for size in range(1,7):
            h,inv=s.gram(size),s.inverse_gram(size)
            for i in range(size):
                for j in range(size):
                    self.assertEqual(sum(h[i][k]*inv[k][j] for k in range(size)), int(i==j))

    def test_arithmetic_residual_capacity_on_holdouts(self):
        polynomials=((1,),(-3,2),(7,-11,4),(0,0,0,5),(-4,9,-2,11,-3))
        for p in polynomials:
            bound,actual=s.verify_capacity(p)
            self.assertGreater(bound,0)
            self.assertGreaterEqual(actual,bound)
            scaled=tuple(F(9*x,14) for x in p)
            b2,a2=s.verify_capacity(scaled,denominator=14,multiple=9)
            self.assertEqual((b2,a2),(F(9,14)*bound,F(9,14)*actual))

    def test_unknown_denominator_cannot_inherit_integer_gap(self):
        p=(F(1,100),)
        self.assertLess(abs(s.moment_pair(p)),s.residual_capacity(0))
        with self.assertRaises(ValueError):s.verify_capacity(p)
        bound,actual=s.verify_capacity(p,denominator=100)
        self.assertEqual(bound,actual)

    def test_zero_field_and_false_divisibility_are_rejected(self):
        with self.assertRaises(ValueError):s.verify_capacity((0,0))
        with self.assertRaises(ValueError):s.verify_capacity((1,2),multiple=3)
        with self.assertRaises(ValueError):s.residual_capacity(2,denominator=0)

    def test_exact_input_domain(self):
        with self.assertRaises(TypeError):s.evaluate((1,),0.5)
        with self.assertRaises(TypeError):s.inner((0.5,),(1,))
        with self.assertRaises(ValueError):s.moment(True)
        with self.assertRaises(ValueError):s.orthogonal_polynomial(-1)


if __name__ == '__main__':
    unittest.main()
