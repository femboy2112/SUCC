"""Exact finite hostile controls for formal 0- and logarithmic 1-boundaries."""
import unittest
from fractions import Fraction as Q
from itertools import product
from math import comb

from observational_succ.bbp_zero_one_characters import (
    BETA, ASYMPTOTIC_MASS, MOMENT_KERNEL, authentic_r, canceled_r,
    source_moment,source_at_zero_jet,polynomial_evaluate,
    zero_jet_of_polynomial,one_jet_of_polynomial,jet_character_phase,
    mutant_multiplier,mutant_source,mutant_rational_extension,mutant_state,
    two_adic_unit,source_prefix_at_beta,discontinuity_witness,
    regularized_slope_rational_certificate,residual_weighted_norm_prefix,
    rational_eval_tail_bound,modadic_odd_rational,mutant_stationary_clock,
    mutant_modular_states
)

class ZeroOneCharactersTest(unittest.TestCase):
    def test_original_four_poles_and_mellin_atom(self):
        for n in range(1,101):
            self.assertEqual(authentic_r(n), canceled_r(n))
            self.assertEqual(authentic_r(n), source_moment(n))
            self.assertEqual(authentic_r(n).denominator%2,1)
        self.assertEqual(sum(MOMENT_KERNEL),0)
        self.assertEqual(sum(j*c for j,c in enumerate(MOMENT_KERNEL)),-15)
        self.assertEqual(ASYMPTOTIC_MASS,Q(15,64))

    def test_rational_zero_jet_is_original_source(self):
        for depth in (1,2,4,12):
            self.assertEqual(source_at_zero_jet(depth),tuple(authentic_r(n) for n in range(1,depth+1)))

    def test_one_jet_exact_binomial_conversion(self):
        # f(q)=(1+q)^3, f(1-s)=(2-s)^3
        f=(Q(1),Q(3),Q(3),Q(1))
        self.assertEqual(one_jet_of_polynomial(f,5),(Q(8),Q(-12),Q(6),Q(-1),Q(0)))
        self.assertEqual(zero_jet_of_polynomial(f,5),f+(Q(0),))

    def test_additive_character_group_law(self):
        a=(Q(1,3),Q(2,7),Q(5,11))
        b=(Q(3,5),Q(-2,9),Q(4,13))
        weights=(Q(3,4),Q(1,2),Q(-5,8))
        x=jet_character_phase(a,weights)
        y=jet_character_phase(b,weights)
        together=jet_character_phase(tuple(a[j]+b[j] for j in range(3)),weights)
        self.assertEqual((x+y)%1,together)
        self.assertTrue(0<=together<1)

    def test_all_mutants_same_k_zero_jet_and_j_one_jet(self):
        for K,J in ((1,2),(2,3),(4,4)):
            m=mutant_multiplier(K,J)
            self.assertEqual(polynomial_evaluate(m,BETA),0)
            self.assertEqual(zero_jet_of_polynomial(m,K),(Q(1),)+(Q(0),)*(K-1))
            self.assertEqual(one_jet_of_polynomial(m,J),(Q(1),)+(Q(0),)*(J-1))
            for n in range(1,K+1):
                self.assertEqual(mutant_source(n,K,J),authentic_r(n))
            for n in range(K+J+1,K+J+8):
                self.assertEqual(mutant_source(n,K,J),mutant_rational_extension(n,K,J))
                self.assertEqual(mutant_source(n,K,J).denominator%2,1)
            self.assertNotEqual(mutant_source(K+1,K,J),authentic_r(K+1))

    def test_mutant_late_two_adic_isometry_exact(self):
        for K,J in ((1,2),(2,3)):
            for x,y in ((0,1),(5,10),(2,16),(17,81),(127,511)):
                lhs=mutant_rational_extension(x,K,J)-mutant_rational_extension(y,K,J)
                self.assertTrue(two_adic_unit(lhs/Q(x-y)))
                self.assertEqual(mutant_rational_extension(x,K,J).denominator%2,1)

    def test_mutant_zero_seed_nonnormal_selector_control(self):
        # M(1/16)=0 implies selected completed carrier = 0, not pi:
        # U_n = - sum_{j>=1}16^{-j}r_mut(n+j) -> 0.
        # The finite exact recurrence exhibits the late-time decay after
        # its large early transient; the infinite assertion needs a proof.
        for K,J in ((1,2),(2,2)):
            u=mutant_state(100,K,J)
            self.assertLess(abs(u),Q(1,1000))
            self.assertEqual(mutant_state(0,K,J),0)

    def test_evaluation_is_not_continuous_in_either_formal_adic_topology(self):
        for n in (2,4,8):
            poly,at=discontinuity_witness(n,False)
            self.assertEqual(zero_jet_of_polynomial(poly,n),(Q(0),)*n)
            self.assertEqual(at,Q(1,2))
            poly,at=discontinuity_witness(n,True)
            self.assertEqual(one_jet_of_polynomial(poly,n),(Q(0),)*n)
            self.assertEqual(at,Q(1,2))

    def test_original_prefix_and_mutant_finite_identity(self):
        for K,J in ((1,2),(3,3)):
            poly=mutant_multiplier(K,J)
            # formal coefficient convolution of G with M
            for n in range(1,20):
                expected=sum((poly[j]*authentic_r(n-j) for j in range(min(n,len(poly))) if poly[j]),Q())
                self.assertEqual(mutant_source(n,K,J),expected)
        for n in (1,5,30):
            self.assertLess(source_prefix_at_beta(n),Q(22,7))

    def test_regularized_slope_rational_interval(self):
        import math
        c=15/64
        closed=(c+19*math.log(2)/32
                -(5+9*math.sqrt(2))*math.pi/128
                -9*math.sqrt(2)*math.log(1+math.sqrt(2))/64)
        for N in (2,8,32,128):
            center,radius=regularized_slope_rational_certificate(N)
            self.assertLessEqual(abs(float(center)-closed),float(radius))
        self.assertLess(residual_weighted_norm_prefix(30),Q(10))

    def test_source_prefix_has_rigorous_pi_bracket(self):
        import math
        for depth in (3,8,20):
            approx=source_prefix_at_beta(depth)
            error=rational_eval_tail_bound(depth)
            self.assertGreaterEqual(math.pi,float(approx))
            self.assertLessEqual(math.pi,float(approx+error)+1e-15)

    def test_residual_n_inverse_cube_bound_samples(self):
        c=ASYMPTOTIC_MASS
        for n in range(2,400):
            defect=authentic_r(n)-c/Q(n*n)
            self.assertGreater(defect,0)
            self.assertLessEqual(defect,Q(1,n**3))

    def test_nonnormal_mutant_still_exact_late_source_clock(self):
        K,J=1,2
        for depth in (1,2):
            M=16**depth
            first=K+J+depth
            actual=mutant_modular_states(first+M,depth,K,J)
            full=[]
            for n in range(first,first+M):
                window=mutant_stationary_clock(n,depth,K,J)
                self.assertEqual(actual[n],window)
                full.append(window)
            self.assertEqual(set(full),set(range(M)))

    def test_native_original_source_when_installed(self):
        try:
            from observational_succ.succ_internal_matrix_walk import authentic_r as native
        except ModuleNotFoundError:
            self.skipTest("full upstream SUCC implementation absent from isolated tree")
        for n in range(1,101):
            self.assertEqual(authentic_r(n),native(n))

    def test_fail_fast_on_type_and_domain_errors(self):
        for call in [lambda:authentic_r(0),lambda:mutant_multiplier(0,2),
                     lambda:jet_character_phase([Q(1)],[Q(1),Q(2)]),
                     lambda:mutant_source(0,2,2),lambda:polynomial_evaluate([1],.5),
                     lambda:one_jet_of_polynomial([1],0)]:
            with self.assertRaises(ValueError):call()

if __name__=='__main__':unittest.main()
