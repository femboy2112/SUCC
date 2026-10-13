"""Exact rational/adelic source receipts and hostile missing-place tests."""
import unittest
from fractions import Fraction as F
from itertools import product
from math import gcd
from observational_succ.diagonal_adele_zeta import (
    DiagonalSourceError, DiagonalCarrier, prime, factor_positive, valuation,
    valuations, fractional_padic_part, additive_reciprocity,
    multiplicative_reciprocity, modulo_padic_integral, finite_places_observe,
    padic_precision_equal, bounded_height_injection, height_limited_source,
    no_height_limit_alias, local_euler_factor, local_euler_product,
    validate_euler_places,
)

class DiagonalArithmetic(unittest.TestCase):
    def test_exhaustive_small_rational_global_characters(self):
        count=0
        for a in range(-15,16):
            for b in range(1,19):
                q=F(a,b)
                report=additive_reciprocity(q)
                self.assertEqual(report['total_integer'],int(report['finite_angle_sum']-q))
                self.assertEqual(report['finite_angle_sum']%1,q%1)
                self.assertTrue(report['diagonal_character_trivial'])
                if q:
                    mul=multiplicative_reciprocity(q)
                    self.assertEqual(mul['global_product'],1)
                    self.assertEqual(mul['arch_norm'],abs(q))
                    self.assertEqual(mul['arch_norm']*mul['finite_norm_product'],1)
                count+=1
        self.assertEqual(count,31*18)

    def test_additive_phase_one_sixth_split(self):
        q=F(1,6)
        r=additive_reciprocity(q)
        self.assertEqual(r['finite_angles'],{2:F(1,2),3:F(2,3)})
        self.assertEqual(r['real_angle'],F(-1,6))
        self.assertEqual(r['total_integer'],1)

    def test_missing_finite_place_breaks_diagonal_cancelation(self):
        q=F(1,6)
        r=additive_reciprocity(q)
        self.assertNotEqual((r['real_angle']+r['finite_angles'][2])%1,0)
        self.assertNotEqual((r['real_angle']+r['finite_angles'][3])%1,0)
        self.assertEqual((r['real_angle']+sum(r['finite_angles'].values(),F(0)))%1,0)

    def test_sign_alias_for_multiplicative_valuations(self):
        q=F(5,42)
        self.assertEqual(multiplicative_reciprocity(q)['valuations'],
                         multiplicative_reciprocity(-q)['valuations'])
        self.assertNotEqual(q,-q)

    def test_all_integer_diagonal_phases_are_trivial(self):
        for q in (-99,-1,0,1,100):
            self.assertEqual(additive_reciprocity(q)['finite_angle_sum'],0)
            self.assertEqual(additive_reciprocity(q)['real_angle']%1,0)

    def test_true_prime_gate(self):
        for p in (0,1,4,6,9,15,25,-2):
            with self.assertRaises(DiagonalSourceError):
                fractional_padic_part(F(1,6),p)
        for p in (2,3,5,7,11):
            self.assertTrue(prime(p))

    def test_exact_val_per_nonzero_rationals(self):
        self.assertEqual(valuation(F(125,6),5),3)
        self.assertEqual(valuation(F(-1,18),3),-2)
        self.assertEqual(valuations(F(-18,125)),{2:1,3:2,5:-3})
        with self.assertRaises(DiagonalSourceError):valuation(0,2)
        with self.assertRaises(DiagonalSourceError):multiplicative_reciprocity(0)

    def test_padic_part_is_integral_remainder(self):
        for a,b,p in product(range(-11,12),range(1,11),(2,3,5,7)):
            q=F(a,b)
            got=fractional_padic_part(q,p)
            self.assertTrue(F(0)<=got<1)
            self.assertTrue(q==got or valuation(q-got,p)>=0)

    def test_residue_of_p_integral_rational(self):
        self.assertEqual(modulo_padic_integral(F(1,3),2,4),11)
        self.assertEqual(modulo_padic_integral(F(5,7),2,3),3)
        with self.assertRaises(DiagonalSourceError):
            modulo_padic_integral(F(1,2),2,3)

    def test_precision_exact_and_nonintegral_quotient_not_ring(self):
        self.assertTrue(padic_precision_equal(F(1,3),F(1,3)+F(25),5,2))
        self.assertFalse(padic_precision_equal(F(1,3),F(1,3)+F(5),5,2))
        with self.assertRaises(DiagonalSourceError):
            modulo_padic_integral(F(1,9),3,1)

    def test_source_succ_fucc_square_and_local_views(self):
        carrier=DiagonalCarrier(F(2,3),"authentic-Q",0)
        for d,m in product((F(1),F(1,2),F(-2)),(F(2),F(3),F(-1))):
            r=carrier.commuting_square(d,m,{5:2,7:1})
            self.assertTrue(r['local_square_verified'])
            self.assertEqual(r['common_address'],m*(carrier.address+d))
            self.assertEqual(r['finite_views'],finite_places_observe(m*(carrier.address+d),{5:2,7:1}))
        with self.assertRaises(DiagonalSourceError):
            carrier.fucc(6,require_prime=True)
        with self.assertRaises(DiagonalSourceError):
            carrier.commuting_square(0,F(1,5),{5:2})

    def test_uniform_height_separation_certificate(self):
        report=bounded_height_injection(3,{5:1,7:1})
        self.assertEqual(report['modulus'],35)
        self.assertEqual(report['modulus_cutoff'],18)
        self.assertTrue(report['injective'])
        holdout=height_limited_source(3,{5:1,7:1})
        self.assertGreater(holdout['states'],10)
        self.assertEqual(holdout['observed_collisions'],0)

    def test_height_without_enough_primes_does_not_promise_separation(self):
        report=bounded_height_injection(3,{2:1})
        self.assertFalse(report['injective'])
        self.assertGreater(height_limited_source(3,{2:1})['observed_collisions'],0)

    def test_real_plus_padic_arch_gap_improves_certificate(self):
        weak=bounded_height_injection(3,{2:1})
        strong=bounded_height_injection(3,{2:1},certify_by_arch_gap=F(1,10))
        self.assertFalse(weak['injective'])
        self.assertTrue(strong['injective'])

    def test_no_finite_p_clocks_and_real_limit_without_height(self):
        for N in (2,10,100,1000):
            a=no_height_limit_alias({5:2,7:1},N)
            self.assertTrue(a['all_selected_prime_views_zero'])
            self.assertGreater(a['nonzero'],0)
            self.assertLess(a['arch_abs'],F(1,N))

    def test_local_p_euler_geometric_shell(self):
        self.assertEqual(local_euler_factor(2,2),F(4,3))
        self.assertEqual(local_euler_factor(3,2),F(9,8))
        with self.assertRaises(DiagonalSourceError):local_euler_factor(6,2)
        with self.assertRaises(DiagonalSourceError):local_euler_factor(2,-1)

    def test_exact_euler_prime_prefix_and_tail(self):
        out=local_euler_product(5,2)
        self.assertEqual(out['prime_places'],(2,3,5))
        self.assertEqual(out['lower'],F(25,16))
        self.assertEqual(out['upper'],F(25,16)*F(6,5))
        self.assertEqual(validate_euler_places(5,(2,3,5),2),out['lower'])

    def test_false_euler_source_fails(self):
        for a in ((2,3),(2,5),(2,3,5,5),(2,3,4,5)):
            with self.assertRaises(DiagonalSourceError):
                validate_euler_places(5,a,2)

    def test_euler_prefix_bounds_monotone(self):
        prior=None
        for n in (2,3,5,7,11,17,29):
            r=local_euler_product(n,2)
            self.assertLess(r['lower'],r['upper'])
            if prior:
                self.assertGreaterEqual(r['lower'],prior['lower'])
                self.assertLessEqual(r['upper'],prior['upper'])
            prior=r

    def test_wrong_numeric_inputs_rejected(self):
        with self.assertRaises(DiagonalSourceError):
            DiagonalCarrier(1.0)
        with self.assertRaises(DiagonalSourceError):
            additive_reciprocity(F(1,2).__float__())
        with self.assertRaises(DiagonalSourceError):
            bounded_height_injection(2,{6:1})

if __name__=='__main__':unittest.main()

class AdelicTopologyObstruction(unittest.TestCase):
    def test_true_real_and_padic_convergence_with_hidden_prime_escape(self):
        from observational_succ.diagonal_adele_zeta import finite_place_joint_limit_escape
        for P in ((2,),(2,3),(5,7),(2,3,5)):
            for n in (1,2,3,4):
                v=finite_place_joint_limit_escape(P,n)
                self.assertLess(v['real_abs'],v['real_upper_bound'])
                self.assertEqual(v['full_product_formula'],1)
                self.assertTrue(v['all_selected_clocks_read_zero'])
                self.assertFalse(v['converges_to_zero_in_full_adeles'])
                self.assertEqual(v['outside_prime_norm_product'],
                                 v['diagonal_rational'].denominator)
            q1=finite_place_joint_limit_escape(P,1)['real_abs']
            q4=finite_place_joint_limit_escape(P,4)['real_abs']
            self.assertLess(q4,q1)

    def test_fake_primes_rejected_by_limit_witness(self):
        from observational_succ.diagonal_adele_zeta import finite_place_joint_limit_escape
        for P in ((6,),(2,2),()):
            with self.assertRaises(DiagonalSourceError):
                finite_place_joint_limit_escape(P,1)
