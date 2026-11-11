"""Finite rational, source, and adversarial controls for explicit-formula coupling.
Run: python -m unittest -v test_prime_weil_probe.py
"""
import unittest
from fractions import Fraction
from prime_weil_probe import (
    factor, prime_power, arithmetic_defect, mobius_convolution_a,
    dirichlet_coeff_zeta_times_mobius, ordered_prime_power_edges,
    normalized_primitive_coefficient, six_diamond, holonomy_fraction,
    phase_six_mixed_difference, original_four_pole_R, original_zero_prefix,
    prime_pair_log_ratio, ensure_rational_compiler_carry,
    phase_interval,phase_difference_interval,
)


class PrimeWeilTests(unittest.TestCase):
    def test_prime_power_classifier(self):
        self.assertEqual(prime_power(8),(2,3))
        self.assertEqual(prime_power(9),(3,2))
        self.assertIsNone(prime_power(6))
        self.assertIsNone(prime_power(1))
        self.assertEqual(factor(2**4*3**3*5),{2:4,3:3,5:1})

    def test_one_epoch_has_no_prime_power_ratio(self):
        for A in (2,3,5,7,11,31,100):
            self.assertEqual(ordered_prime_power_edges(range(A,2*A)),{})

    def test_critical_multiplicative_span_six(self):
        for m in (1,3,7,31):
            self.assertEqual(ordered_prime_power_edges(six_diamond(m)), {
                2:[(m,2*m),(3*m,6*m)],
                3:[(m,3*m),(2*m,6*m)]})

    def test_mod_six_composite_not_primitive(self):
        pairs=ordered_prime_power_edges([7,14,21,42])
        self.assertNotIn(6,pairs)
        self.assertEqual(set(pairs),{2,3})

    def test_primitive_unphased_exact_weights(self):
        c=normalized_primitive_coefficient([7,14,21,42],lambda n:Fraction(1))
        m=7
        self.assertEqual(c[2],Fraction(5,9*m*m))
        self.assertEqual(c[3],Fraction(5,12*m*m))

    def test_primitive_signed_mutation(self):
        I=six_diamond(7)
        c=normalized_primitive_coefficient(I,lambda n:Fraction(-1 if n in (14,42) else 1))
        self.assertEqual(c[2],-Fraction(5,9*7*7))
        self.assertEqual(c[3],Fraction(5,12*7*7))  # q3 edges unchanged by a two-fiber phase flip

    def test_pure_gauge_loop_any_seed(self):
        for t in range(20):
            m=t+1
            keys=six_diamond(m)
            d={n:Fraction((n*n+7*t)%101,101) for n in keys}
            self.assertEqual(holonomy_fraction(d,[m,2*m,6*m,3*m,m]),0)

    def test_mixed_difference_detects_nonconstant_phase(self):
        m=7
        d={n:Fraction(n*n,13) for n in six_diamond(m)}
        self.assertNotEqual(phase_six_mixed_difference(d,m),0)
        self.assertEqual(phase_six_mixed_difference({n:Fraction(1,3) for n in six_diamond(m)},m),0)

    def test_wrong_seed_defect_zero(self):
        for n in range(1,151):
            self.assertTrue(all(v==0 for v in arithmetic_defect(n,lambda k:Fraction(1)).values()))

    def test_primes_defect_exact(self):
        a=lambda n:Fraction((n*13+7)%23,23)
        for p in [2,3,5,7,11,29]:
            self.assertEqual(arithmetic_defect(p,a),{p:a(p)-a(1)})

    def test_composite_six_defect(self):
        a=lambda n:Fraction(n*n+1,21)
        d=arithmetic_defect(6,a)
        self.assertEqual(d[2],a(6)-a(3))
        self.assertEqual(d[3],a(6)-a(2))

    def test_defect_additive_prime_jets(self):
        a=lambda n:Fraction((n*n+3*n)%29,29)
        for n in range(1,91):
            d=arithmetic_defect(n,a)
            for p,k in factor(n).items():
                self.assertEqual(d[p],k*a(n)-sum((a(n//p**j) for j in range(1,k+1)),Fraction(0)))

    def test_mobius_deconvolution_all_n(self):
        a=lambda n:Fraction((n*3+2)%17,17)
        for n in range(1,151):
            self.assertEqual(dirichlet_coeff_zeta_times_mobius(n,a),a(n))

    def test_constant_defect_1_delta(self):
        a=lambda n:Fraction(1)
        for n in range(1,101):
            self.assertEqual(mobius_convolution_a(n,a),Fraction(1 if n==1 else 0))

    def test_exact_source_and_zero_seed(self):
        self.assertEqual(original_four_pole_R(0),Fraction(4)-Fraction(2,4)-Fraction(1,5)-Fraction(1,6))
        for L in (1,3,8,20):
            P=original_zero_prefix(L)
            self.assertGreater(P,0)
            for n in (1,2,3,6):
                y, wrong=ensure_rational_compiler_carry(L,n)
                self.assertEqual(y,16**n*P)
                self.assertEqual(wrong,0)

    def test_source_moment_positivity(self):
        for j in range(0,100):
            self.assertGreater(original_four_pole_R(j),0)

    def test_multiplicative_phase_real_lift(self):
        for n in (1,2,3,6):
            for p in (2,3):
                self.assertEqual(16**(p*n)-16**n, 16**n*prime_pair_log_ratio(n,p))


    def test_authenticated_phase_sign_certificate(self):
        # Original BBP R(j), literal zero seed, 12-term rational P_L and strict tail.
        # These rational enclosures need no pi-digit oracle, cosine, or zero locations.
        intervals = {
            (1,2):(Fraction(1,10),Fraction(1,8)),
            (3,6):(Fraction(2,5),Fraction(5,12)),
            (1,3):(Fraction(1,10),Fraction(1,9)),
            (2,6):(Fraction(3,8),Fraction(2,5)),
        }
        for edge,(left,right) in intervals.items():
            lower,upper=phase_difference_interval(*edge,L=12)
            self.assertLess(left,lower)
            self.assertLess(upper,right)
        # Hence cos edges (1->2),(1->3) >0 and (3->6),(2->6) <0.
        # The coherent wrong seed gives all four cosines +1.

    def test_authenticated_nonzero_two_three_mixed_defect(self):
        # Im[e(Y_6)-e(Y_2)-e(Y_3)+e(Y_1)] < 1-sqrt(3) < 0:
        # sin(Y_2),sin(Y_3)>sqrt(3)/2, sin(Y_6)<0, sin(Y_1)<=1.
        lower,upper=phase_interval(1,L=12)
        self.assertLess(Fraction(1,8),lower)
        self.assertLess(upper,Fraction(1,6))
        for n in (2,3):
            lower,upper=phase_interval(n,L=12)
            self.assertLess(Fraction(1,6),lower)
            self.assertLess(upper,Fraction(1,3))
        lower,upper=phase_interval(6,L=12)
        self.assertLess(Fraction(1,2),lower)
        self.assertLess(upper,Fraction(1))
        # Pure-gauge Wilson holonomy remains exactly 1 despite this nonzero mixed difference.

    def test_too_short_bbp_horizon_is_rejected(self):
        with self.assertRaises(ValueError):
            phase_interval(6,L=1)

    def test_lambda6_cannot_be_source_term(self):
        self.assertIsNone(prime_power(6))
        self.assertEqual(set(ordered_prime_power_edges([1,2,3,6])),{2,3})


if __name__=='__main__':
    unittest.main()
