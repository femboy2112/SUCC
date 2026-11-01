"""Exact source-Wilson, positive-moment, seed-Fisher and adversarial tests."""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'research/2026-11-01/holonomy_seed_geometry'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

m=load('hsg_exact_module',BASE/'holonomy_geometry.py')
o=load('hsg_independent_oracle',BASE/'independent_oracle.py')

class SourceAndWilsons(unittest.TestCase):
    def test_authentic_combined_rational(self):
        for n in range(1,101):self.assertEqual(m.r(n),m.r_combined(n))
    def test_independent_source(self):
        for n in range(1,101):self.assertEqual(m.r(n),o.original_combined(n))
    def test_initial_pole_exact(self):
        self.assertEqual(m.r(1),F(47,15));self.assertEqual(m.r(2),F(106,819))
    def test_positive_monotone(self):
        for n in range(1,110):self.assertGreater(m.r(n),m.r(n+1))
    def test_adjacent_curvature_positive_and_decreasing(self):
        for n in range(1,100):self.assertGreater(m.curvature(n),m.curvature(n+1))
    def test_finite_affine_inverse(self):
        for n in range(1,40):
            f=m.source_step(n);inv=m.affine_inverse(f)
            self.assertEqual(m.affine_compose(f,inv),(F(1),F()))
            self.assertEqual(m.affine_compose(inv,f),(F(1),F()))
    def test_noncommuting_path_order(self):
        for i in range(1,9):
            for j in range(i+1,10):
                self.assertEqual(m.affine_order_commutator(i,j),(F(1),F(15)*(m.r(i)-m.r(j))))
    def test_first_source_commutator(self):
        self.assertEqual(m.affine_order_commutator(1,2)[1],F(12301,273))
    def test_commutator_order_reverse(self):
        for i,j in [(1,2),(2,3),(4,7)]:
            self.assertEqual(m.affine_order_commutator(i,j)[1],-m.affine_order_commutator(j,i)[1])
    def test_integrated_unweighted_source_curvature(self):
        for n in range(1,55):
            self.assertEqual(m.integrated_curvature(n),47-15*m.r(n))
    def test_unweighted_circle_phase_quantization(self):
        # Their phases agree exactly modulo 1 for every integer h.
        for n in [1,2,3,6,16,37]:
            for h in [-11,-1,1,2,7]:
                self.assertEqual((h*m.integrated_curvature(n))%1,(-15*h*m.r(n))%1)
    def test_finite_unweighted_holonomy_nontrivial(self):
        self.assertNotEqual(m.integrated_curvature(3)%1,F(0))
    def test_reconstruct_source_selected_state(self):
        for n in range(1,24):self.assertEqual(m.curvature_reconstruction(n),m.orbit(n))
    def test_reconstruct_altered_exact_seeds(self):
        for s in [F(-7,19),F(5,11),F(0),F(1,5)]:
            for n in range(1,16):self.assertEqual(m.curvature_reconstruction(n,s),m.orbit(n,s))
    def test_independent_orbit(self):
        for n in range(1,25):self.assertEqual(m.orbit(n),o.original_orbit(n))
    def test_independent_curvature_reconstruction(self):
        for n in range(1,25):self.assertEqual(m.curvature_reconstruction(n),o.original_weighted_curvature_state(n))
    def test_path_order_bad_reversal_differs(self):
        r1=m.r(1);r2=m.r(2)
        self.assertEqual(m.affine_compose(m.source_step(2),m.source_step(1))[1]-(m.affine_compose(m.source_step(1),m.source_step(2))[1]),15*(r1-r2))
    def test_rational_curvature_pi_approximations_decreasing(self):
        for n in range(0,10):self.assertGreater(m.pi_upper(n),m.pi_upper(n+1))
    def test_rational_machin_pi_enclosure(self):
        lo,hi=m.machin_pi_interval(24)
        self.assertTrue(F(3)<lo<hi<F(22,7))
        self.assertLess(hi-lo,F(1,10**32))
    def test_curvature_pi_upper_and_error_enclosure(self):
        lo,hi=m.machin_pi_interval(36)
        for n in range(1,10):
            rpi=m.pi_upper(n)
            self.assertGreater(rpi,hi)
            self.assertLess(rpi-lo,m.pi_error_bound(n))
    def test_curvature_pi_remainder_is_smaller_than_base_bbp(self):
        lo,hi=m.machin_pi_interval(40)
        for n in range(1,9):
            self.assertLess(m.pi_upper(n)-lo,hi-m.partial_pi(n))
    def test_curvature_decay_one_extra_power(self):
        # Exact finite checks, NOT a proof of the n->infinity asymptotic.
        for n in range(10,60):
            c=m.curvature(n)
            self.assertTrue(F(6,n**3)<c<F(10,n**3))
    def test_wilson_tilt_mass_exact(self):
        for n in range(1,80):
            self.assertEqual(sum((m.curvature(j) for j in range(1,n+1)),F()),m.finite_curvature_mass(n))
            self.assertTrue(F(0)<m.finite_curvature_mass(n)<47)
    def test_wilson_tilt_o_one_bound(self):
        for n in [1,2,4,8,32,100]:
            self.assertEqual(m.local_wilson_tilt_rational_error_bound(n,3),F(47*44*3,7*n))
    def test_wilson_tilt_cannot_supply_normality(self):
        # A perfectly coherent phase stream z_n=1 remains within O(1/N)
        # of perfect coherence after multiplication by local e(h d_n).
        for n in [1,8,32,128]:
            self.assertLess(F(47*44,7*n),F(300,n))
    def test_zero_and_invalid_source_rejected(self):
        for n in [0,-1,1.5,True]:
            with self.assertRaises(ValueError):m.r(n)
    def test_invalid_seed_rejected(self):
        with self.assertRaises(TypeError):m.orbit(3,seed=0.1)

class SeedEchoInformationGeometry(unittest.TestCase):
    def test_qfi_var_independent_oracle(self):
        for n in range(1,13):self.assertEqual(m.seed_mode_variance(n),o.geometric_qfi_var(n))
    def test_qfi_one_mode_zero(self):
        self.assertEqual(m.exact_qfi_divided_by_pi_sq(1,1),0)
    def test_qfi_is_strict_for_multiple_modes(self):
        for n in range(2,60):self.assertGreater(m.exact_qfi_divided_by_pi_sq(n,1),0)
    def test_qfi_harmonic_squared_scaling(self):
        for n in [2,3,5,12]:
            self.assertEqual(m.exact_qfi_divided_by_pi_sq(n,7),49*m.exact_qfi_divided_by_pi_sq(n,1))
    def test_exact_normalized_mode_geometric_sum(self):
        for n in range(1,20):
            x=o.geometric_shadow_mode_norm_sq(n)
            self.assertEqual(x,F(256,255*n)*(1-F(1,256**n)))
    def test_strict_shadow_bound_k5(self):
        for n in range(1,200):
            self.assertLess(m.finite_shadow_norm_upper_sq(n,1),m.k5_shadow_norm_upper_sq(n,1))
    def test_shadow_bound_h2_scaling(self):
        for n in [1,4,16,128]:
            self.assertEqual(m.finite_shadow_norm_upper_sq(n,3),9*m.finite_shadow_norm_upper_sq(n,1))
    def test_necessary_copy_count_k5(self):
        for n in [1,4,16,256]:
            self.assertGreater(m.min_copies_lower_for_helstrom_3_4(n,1),m.k5_copies_lower_for_3_4(n,1))
    def test_k5_threshold_grows_power_five(self):
        for n in [2,3,6,11]:
            self.assertEqual(m.k5_copies_lower_for_3_4(2*n,1),32*m.k5_copies_lower_for_3_4(n,1))
    def test_source_prefix_completed_q_is_rational(self):
        for k in [1,3,10,40]:
            q=m.source_prefix_q(k)
            self.assertTrue(isinstance(q,F) and q>0)
            self.assertEqual(16**k*q,m.orbit(k))
    def test_qfi_invalid_arguments(self):
        for fn in [m.exact_qfi_divided_by_pi_sq,m.finite_shadow_norm_upper_sq]:
            with self.assertRaises(ValueError):fn(0,1)
            with self.assertRaises(ValueError):fn(3,0)

class HausdorffFiniteHistoryCountermodels(unittest.TestCase):
    def test_moment_hankel_positive(self):
        for det in o.gram_determinants(5):self.assertGreater(det,0)
    def test_monic_independent_cramers(self):
        for k in range(1,5):self.assertEqual(m.orthogonal_monic(k),o.monic_polynomial_cramer(k))
    def test_monic_polynomial(self):
        for k in range(1,7):
            p=m.orthogonal_monic(k)
            self.assertEqual(len(p),k+1)
            self.assertEqual(p[-1],1)
    def test_exact_zero_first_moments(self):
        for k in range(1,7):
            p=m.orthogonal_monic(k)
            for j in range(k):self.assertEqual(m.moment_poly(p,j),0)
    def test_strictly_positive_square(self):
        for k in range(1,7):self.assertGreater(m.poly_mass_square(m.orthogonal_monic(k)),0)
    def test_P_at_16_positive(self):
        for k in range(1,7):self.assertGreater(m.poly_evaluate(m.orthogonal_monic(k),F(16)),0)
    def test_strict_resolvent_bounds(self):
        for k in range(1,7):
            lo,hi=m.stieltjes_pole_response_bounds(k)
            self.assertTrue(F(0)<lo<hi)
    def test_mutant_same_prefix_realized_states(self):
        for k in range(1,6):
            p=m.orthogonal_monic(k)
            t=F(1,2*m.poly_sup_bound(p))
            changed=[m.mutated_source_moment(k,t,n) for n in range(1,k+1)]
            self.assertEqual(changed,[m.r(n) for n in range(1,k+1)])
            u=F()
            for j,source in enumerate(changed,1):
                u=16*u+source
                self.assertEqual(u,m.orbit(j))
    def test_mutant_first_changed_positive(self):
        for k in range(1,7):
            p=m.orthogonal_monic(k)
            t=F(1,2*m.poly_sup_bound(p))
            self.assertGreater(m.mutated_source_moment(k,t,k+1)-m.r(k+1),0)
    def test_mutant_positive_density_budget(self):
        for k in range(1,7):
            p=m.orthogonal_monic(k)
            t=F(1,2*m.poly_sup_bound(p))
            self.assertEqual(t*m.poly_sup_bound(p),F(1,2))
            for u in [F(j,20) for j in range(21)]:
                self.assertGreater(1+t*m.poly_evaluate(p,u),F(0))
    def test_concrete_rational_completed_counterfeit(self):
        for k in range(1,7):
            d=m.rational_nonnormal_mutant_certificate(k,terms=60)
            lo,hi=d['pi_interval']; q=d['q']; e0,e1=d['epsilon_interval']
            self.assertGreater(q,hi/16)
            self.assertTrue(F(0)<e0<e1<F(1,2*d['C']))
            self.assertEqual(q.denominator,d['non_normal_harmonic'])
    def test_inadequate_pi_cert_rejected(self):
        with self.assertRaises(ValueError):m.rational_nonnormal_mutant_certificate(5,terms=2)
    def test_positivity_violation_rejected(self):
        p=m.orthogonal_monic(2)
        with self.assertRaises(ValueError):m.mutated_source_moment(2,F(1)/m.poly_sup_bound(p),1)
    def test_fraction_coefficients_required(self):
        with self.assertRaises(TypeError):m.moment_poly((0.5,F(1)),0)

if __name__=='__main__':unittest.main()
