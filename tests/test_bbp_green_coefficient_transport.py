"""Exact sources, independent rational checks and hostile Green counterfeits."""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_green_coefficient_transport import (
    geometric_green_moment, tail_coefficient, tail_asymptotic_polynomial,
    absolute_remainder_bound, recover_pole_moments,
    known_pole_weights_from_coefficients, signed_pole_hankel_determinant,
    prony_polynomial_from_coefficients, holonomic_ratio,
    holonomic_residual_interval, compact_bump_moment, compact_bump_forcing,
    zero_contact_moment,
)
from observational_succ.bbp_source_memory import (
    POLE_DATA, pole_moment, forcing, tail_interval,
)


class GreenCoefficientBridge(unittest.TestCase):
    def test_green_moments_against_independent_power_sums(self):
        expected = [Q(1,15), Q(16,225), Q(272,3375), Q(1712,16875)]
        self.assertEqual([geometric_green_moment(j) for j in range(4)],expected)
        for j in range(7):
            partial = sum((Q(k**j,16**k) for k in range(1,120)),Q())
            self.assertLess(partial, geometric_green_moment(j))
            self.assertLess(geometric_green_moment(j)-partial,Q(1,10**60))

    def test_independent_rational_coefficient_oracle(self):
        expected = [Q(), Q(1,64), -Q(7,512), Q(55,4096),
                    -Q(595,32768), Q(8551,262144),
                    -Q(149467,2097152), Q(3030175,16777216)]
        self.assertEqual([tail_coefficient(j) for j in range(8)],expected)
        # Independent signed pole offsets, no pole_moment call.
        for order in range(8):
            direct = sum((rho*sum(((-1)**order*Q(1,16**k)*(k-a)**order
                                    for k in range(1,145)),Q())
                          for a,rho in POLE_DATA),Q())
            self.assertLess(abs(expected[order]-direct), Q(1,10**110))

    def test_certified_all_horizon_inverse_power_bound(self):
        for degree in range(7):
            for n in (1,2,5,10,40,120):
                value = tail_asymptotic_polynomial(n,degree)
                error = absolute_remainder_bound(n,degree)
                lo,hi = tail_interval(n,12)
                self.assertLessEqual(value-error,lo)
                self.assertLessEqual(hi,value+error)
        for bad in (-1,1.0,True):
            with self.assertRaises(ValueError):
                tail_coefficient(bad)

    def test_fixed_and_unknown_pole_source_reconstruction(self):
        cs = [tail_coefficient(j) for j in range(8)]
        self.assertEqual(recover_pole_moments(cs),
                         tuple(pole_moment(j) for j in range(8)))
        self.assertEqual(known_pole_weights_from_coefficients(cs),
                         tuple(rho for _,rho in POLE_DATA))
        self.assertEqual(signed_pole_hankel_determinant(),
                         -Q(225,549755813888))
        self.assertEqual(prony_polynomial_from_coefficients(cs),
                         (Q(21,512),-Q(103,256),Q(89,64),-Q(2),Q(1)))
        mutated=cs[:];mutated[2]+=Q(1,1000)
        self.assertNotEqual(known_pole_weights_from_coefficients(mutated),
                            tuple(rho for _,rho in POLE_DATA))
        with self.assertRaises(ValueError):
            prony_polynomial_from_coefficients(cs[:7])
        with self.assertRaises(ValueError):
            known_pole_weights_from_coefficients(cs[:3])

    def test_nonautonomous_second_order_law(self):
        def P(n):return 120*n*n-89*n+16
        def D(n):return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        for n in range(25):
            r=holonomic_ratio(n)
            self.assertEqual(r, Q(P(n+2)*D(n+1),P(n+1)*D(n+2)))
            lo,hi=holonomic_residual_interval(n,12)
            self.assertLess(lo,0)
            self.assertGreater(hi,0)
            self.assertLess(hi-lo,Q(1,10**7))
            self.assertEqual(forcing(n+2)-r*forcing(n+1),0)

    def test_contact_and_compact_positive_tail_impostors(self):
        self.assertEqual([compact_bump_moment(k) for k in range(3)],
                         [Q(1),Q(1,6),Q(1,24)])
        self.assertEqual(compact_bump_forcing(1),Q(95,6))
        for n in range(1,80):
            self.assertGreater(compact_bump_forcing(n),0)
            self.assertEqual(16*compact_bump_moment(n-1)
                             -compact_bump_moment(n), compact_bump_forcing(n))
            self.assertEqual(zero_contact_moment(n),0)
        self.assertEqual(zero_contact_moment(0),1)
        # Contact atom changes only first forcing readout; a late-tail
        # observer cannot identify the initial phase.
        d=Q(1,20)
        for n in range(1,30):
            self.assertEqual(d*zero_contact_moment(n),0)
        self.assertEqual(16*d*zero_contact_moment(0)-d*zero_contact_moment(1),
                         16*d)
        # Compact bump is exponentially, not algebraically, visible.
        for power in range(8):
            self.assertLess(120**power*compact_bump_moment(120),Q(1,10**12))


if __name__ == '__main__':
    unittest.main()
