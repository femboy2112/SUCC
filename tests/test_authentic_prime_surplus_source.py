"""Original signed Suzuki source cross-oracle and real prime-2 surplus bounds."""
import unittest
from fractions import Fraction as F

from observational_succ.authentic_prime_surplus import (
    PrimeSurplusError, original_prime_surplus_source_passport,
    original_high_surplus_certificate, edge_mass_polynomial_in_b,
    edge_source_polynomial_for_mode, poly_int,poly_mul,poly_add,
    center_feature_gram,
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial,poly_primitive_zero_at_left,
    prime_hinge_integral_polynomial, authentic_first_prime_low_entry,
    polynomial_interval,
)
from observational_succ.source_weil_hierarchy import log2_iv,sqrt_inverse


def trimmed(x):
    x=list(x)
    while len(x)>1 and x[-1]==0:x.pop()
    return tuple(x)


class FrozenOriginalSourceTests(unittest.TestCase):
    def test_pinned_source_gamma_poles_true_prime_and_coercivity(self):
        s=original_prime_surplus_source_passport()
        self.assertEqual(s["source_sha"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(s["true_prime_power_label"],(2,2))
        self.assertEqual(s["kappa_odd"],F(63,500))
        self.assertEqual(s["kappa_even"],F(153,500))
        self.assertTrue(s["contact_and_both_poles_retained"])
        self.assertGreater(s["prime2_weight_interval"][0],F(12,25))
        self.assertGreater(s["log2_interval"][0],F(5,8))

    def test_exact_source_prime_hinge_polynomial_matches_independent_double_ibp(self):
        # Two DIFFERENT implementations: existing polynomial u-correlation
        # integral and newly constructed primitive edge-translation algebra.
        a=F(1,2)
        for i,j in ((1,1),(2,2),(5,5),(6,6),(5,7),(6,8),(5,6)):
            pi=poly_primitive_zero_at_left(legendre_polynomial(i,a),a)
            pj=poly_primitive_zero_at_left(legendre_polynomial(j,a),a)
            derived=edge_mass_polynomial_in_b(pi,pj,a)
            K=poly_int(poly_mul(pi,pj),-a,a)
            expected=trimmed(poly_add(derived,(-K,)))
            original=trimmed(prime_hinge_integral_polynomial(i,j,a))
            self.assertEqual(original,expected, (i,j))

    def test_prime_hinge_original_source_interval_cross_oracle(self):
        source_b=log2_iv()
        w=source_b*sqrt_inverse(2)
        for k in (5,6):
            p=poly_primitive_zero_at_left(legendre_polynomial(k,F(1,2)),F(1,2))
            M=edge_source_polynomial_for_mode(k)
            K=poly_int(poly_mul(p,p),-F(1,2),F(1,2))
            expected_poly=poly_add(M,(-K,))
            iv=polynomial_interval(expected_poly,source_b)*w
            actual=authentic_first_prime_low_entry(k,k)
            self.assertLessEqual(max(iv.lo,actual.lo),min(iv.hi,actual.hi))

    def test_actual_high_operator_two_rank_source_surplus(self):
        c=original_high_surplus_certificate((5,6,7,8))
        self.assertTrue(c["source_all_high_theorem_claimed_conditional"])
        self.assertEqual(c["S4_sign"],"UNVERIFIED")
        self.assertFalse(c["RH_proved"])
        self.assertEqual(c["source_kappa"],
                         (F(63,500),F(153,500),F(63,500),F(153,500)))
        base=c["base_scalar_gram"]
        cmp=c["source_non_scalar_comparator"]
        M=c["genuine_full_prime_mismatch_gram_intervals"]
        self.assertGreater(cmp[0][0],2*base[0][0])
        self.assertGreater(cmp[1][1],F(7,5)*base[1][1])
        self.assertGreater(M[0][0][0],F(1,2000))
        self.assertGreater(M[1][1][0],F(3,10000))
        # Authentic full prime (not just center features) proves source
        # gains >4x and >2x the original scalar per probe, respectively.
        self.assertGreater(F(12,25)*M[0][0][0],4*base[0][0])
        self.assertGreater(F(12,25)*M[1][1][0],2*base[1][1])
        self.assertGreater(c["p5_pole_amplitude_lower"],0)

    def test_refuses_independent_composite_prime_mutation(self):
        with self.assertRaises(PrimeSurplusError):
            original_high_surplus_certificate((5,6),prime=6)
        with self.assertRaises(PrimeSurplusError):
            original_high_surplus_certificate((5,6),prime=True)
        with self.assertRaises(PrimeSurplusError):
            original_high_surplus_certificate((4,5))
        with self.assertRaises(PrimeSurplusError):
            original_high_surplus_certificate((5,5))


if __name__=="__main__":
    unittest.main()
