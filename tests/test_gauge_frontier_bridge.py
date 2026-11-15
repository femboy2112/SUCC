"""Exact scoped tests of frontier gauge references, finite no-go and Newman logic."""
import unittest
from fractions import Fraction as F
from observational_succ.gauge_frontier_bridge import (
    forcing,bbp_state,green_truncated,green_residual,
    lagarias_lower_certificate,lagarias_rigorous_range,lagarias_rational_interval,
    polynomial_evaluate,derivative_coefficients,symmetric_xi_impostor,
    finite_phase_bound,newman_logical_status)

class GaugeFrontierTest(unittest.TestCase):
    def test_four_poles_exact_authentic(self):
        self.assertEqual(forcing(1),F(47,15))
        self.assertEqual(forcing(2),F(106,819))
        for n in range(1,21):self.assertGreater(forcing(n),0)
        with self.assertRaises(ValueError):forcing(0)

    def test_signed_green_transport_positive_defect(self):
        for n in range(0,9):
            for m in (0,1,2,3,5,9):
                self.assertEqual(green_residual(n,m), F(1,16**m)*forcing(n+m+1))
                self.assertGreater(green_residual(n,m),0)

    def test_exact_seed_cocycle_does_not_authenticate_seed(self):
        for seed in (F(0),F(1,16),F(-1,17),F(2,3)):
            for n in (0,1,2,6,12):
                self.assertEqual(bbp_state(n,seed)-bbp_state(n),16**n*seed)
        self.assertNotEqual(bbp_state(7,F(1,16)),bbp_state(7))

    def test_truncation_defect_shrinks(self):
        for n in range(5):
            r=[green_residual(n,m) for m in range(5)]
            self.assertTrue(all(a>b>0 for a,b in zip(r,r[1:])))

    def test_lagarias_n1_equality(self):
        x=lagarias_lower_certificate(1)
        self.assertEqual(x['sigma'],1)
        self.assertEqual(x['lower_gap'],0)

    def test_rational_lagarias_n2_to_128(self):
        r=lagarias_rigorous_range(128)
        self.assertTrue(r['strict_lower_bounds'])
        self.assertFalse(r['proves_RH'])
        self.assertEqual(r['minimal_lower_gap_n'],2)
        self.assertGreater(r['minimal_lower_gap'],0)

    def test_lagarias_rational_interval_both_sides(self):
        for n in range(1,129):
            c=lagarias_rational_interval(n)
            self.assertLessEqual(c['lo'],c['hi'])
            self.assertEqual(c['verdict'],'EQUALITY_AT_1' if n==1 else 'PASS')
        with self.assertRaises(ValueError):lagarias_rational_interval(512,exp_degree=2)

    def test_lagarias_underresolved_bound_is_not_false_rh(self):
        r=lagarias_lower_certificate(2,exp_degree=0,log_terms=0)
        self.assertLess(r['lower_gap'],0)
        # A failed lower enclosure is NOT a false Lagarias inequality.
        self.assertGreater(lagarias_lower_certificate(2)['lower_gap'],0)

    def test_lagarias_bad_argument_rejected(self):
        for n in (0,-1):
            with self.assertRaises(ValueError):lagarias_lower_certificate(n)
        with self.assertRaises(ValueError):lagarias_rigorous_range(0)

    def test_xi_surrogate_even_polynomial_and_imaginary_zero(self):
        sample=(F(0),F(1),F(3,2))
        data=symmetric_xi_impostor(sample,jet_order=3,off_line_imag=F(1,2))
        q=data['polynomial_w']
        self.assertTrue(data['root_exact'])
        self.assertEqual(polynomial_evaluate(q,-F(1,4)),0)
        self.assertFalse(data['preserves_zeta_Euler_source'])
        for a in sample:
            self.assertEqual(polynomial_evaluate(q,a*a),1)
            for j in range(1,4):
                self.assertEqual(polynomial_evaluate(derivative_coefficients(q,j),a*a),0)
        self.assertNotEqual(q,(F(1),))

    def test_xi_impostor_bad_samples_rejected(self):
        with self.assertRaises(ValueError):symmetric_xi_impostor(())
        with self.assertRaises(ValueError):symmetric_xi_impostor((F(0),),-1)

    def test_phase_bound_monotone_in_extra_digits(self):
        for h in (-7,1,17):
            for n in (0,1,5,16):
                a=finite_phase_bound(h,n,n+5)
                b=finite_phase_bound(h,n,n+6)
                self.assertEqual(a,16*b)
        self.assertEqual(finite_phase_bound(0,50,50),0)

    def test_phase_formula_exact_coefficient(self):
        self.assertEqual(finite_phase_bound(1,3,7),F(16**3-1,15*16**7))
        with self.assertRaises(ValueError):finite_phase_bound(1,4,3)

    def test_newman_known_lower_bound_doesnt_imply_rh(self):
        self.assertTrue(newman_logical_status(True,0))
        self.assertTrue(newman_logical_status(False,1))
        self.assertFalse(newman_logical_status(True,1))
        self.assertFalse(newman_logical_status(False,0))
        self.assertFalse(newman_logical_status(True,-1))

if __name__=='__main__':unittest.main(verbosity=2)
