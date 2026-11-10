import unittest
from fractions import Fraction as Q
from math import isqrt

from resonance import (Interval, SCALE, phase, sqrt_interval, nonlinear_floor,
                       error_record, unit_model, order16, source_xi, forcing, evaluate)


class ResonanceTests(unittest.TestCase):
    def test_square_root_outward(self):
        for numerator in range(100):
            for denominator in (1, 3, 17):
                x = Q(numerator, denominator)
                s = sqrt_interval(Interval.ratio(numerator, denominator))
                self.assertLessEqual(Q(s.lo, SCALE)**2, x)
                self.assertGreaterEqual(Q(s.hi, SCALE)**2, x)
        with self.assertRaises(ValueError):
            sqrt_interval(Interval(-1, 1))

    def test_source_forcing_positive_monotone_bound(self):
        for n in range(1, 1000):
            direct = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            self.assertEqual(forcing(n), direct)
            self.assertGreater(direct, forcing(n+1))
            self.assertLessEqual(direct, Q(15, (8*n-7)*(8*n-6)))

    def test_reduced_alias_cannot_get_nonlinear_floor(self):
        p = 41
        m, xi = order16(p), source_xi(p)
        self.assertGreater(m, 2)
        P = [-pow(xi, m, p), -1] + [0]*(m-2) + [1]
        with self.assertRaises(ValueError):
            nonlinear_floor(p, 1, P)
        with self.assertRaises(ValueError):
            nonlinear_floor(p, 1, [0, -1])

    def test_low_order_bound_can_be_vacuous(self):
        record = nonlinear_floor(41, 1, [0, 0, 1])
        self.assertEqual(record['floor'].lo, 0)
        self.assertEqual(record['floor'].hi, 0)
        for p in (4201, 4217, 4337):
            self.assertGreater(nonlinear_floor(p, 1, [0, -1, 1])['floor'].lo, 0)

    def test_lift_identity_independent_replica_algorithm(self):
        # Three replicas with deliberately differing phases; comparison uses
        # pairwise scalar cosines rather than the implementation's Box error.
        p = 41
        v = unit_model(p, 1, [2, -1, 1], 1, 7)
        b = [phase(3*n*n+2*n+1, 113) for n in range(3*len(v))]
        rec = error_record(b, v)
        # Independent angle-difference identity bypasses complex products.
        scalar = Interval.ratio(0)
        for n in range(3*len(v)):
            x = source_xi(p)*pow(16,n%len(v),p)%p
            angle = Q(3*n*n+2*n+1,113)-Q(1,7)-Q(evaluate([2,-1,1],x,p),p)
            scalar = scalar + Interval.ratio(2)-phase(angle.numerator,angle.denominator).re*Interval.ratio(2)
        scalar = scalar.divide(3*len(v))
        self.assertTrue(rec['full_l2_squared'].overlaps(scalar))
        self.assertTrue(rec['full_l2_squared'].overlaps(rec['lifted_squared']))
        self.assertTrue(rec['lift_bound_strictly_certified'])

    def test_affine_anchor_fifteenth_roots(self):
        # Exact exponent congruences, including h-character fixed points
        # which need not be fixed states of the underlying circle.
        for h in (1, 3, 5, 7):
            for k in range(15):
                theta = Q(k, 15*h)
                for n in range(1, 15):
                    self.assertEqual((h*(16**n-1)*theta).denominator, 1)
        p, h = 73, 3
        for c in (-h, 0, 4):
            for k in range(15):
                # v_next/v^16 has exact exponent -15k/15 modulo integers.
                for r in range(order16(p)):
                    x = source_xi(p)*pow(16,r,p)%p
                    y = 16*x%p
                    exponent = Q(k,15)+Q(c*y,p)-16*(Q(k,15)+Q(c*x,p))
                    self.assertEqual(exponent.denominator, 1)


if __name__ == '__main__':
    unittest.main()
