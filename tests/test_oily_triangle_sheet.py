"""Research-only exact-rational regression tests for the Oily triangular sheet.

The tested module is path-loaded to avoid introducing a production dependency
or touching the historical BBP source modules.
"""
from __future__ import annotations

import importlib.util
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb, factorial
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "research/2026-10-29/oily_triangle_sheet/triangle_sheet_probe.py"
SPEC = importlib.util.spec_from_file_location("triangle_sheet_research_probe", PATH)
s = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(s)


class ExactOilyTriangleTests(unittest.TestCase):
    def test_original_four_pole_green_is_unchanged(self):
        for j in range(81):
            x=Q(j,80)
            original=(4-2*x**3-x**4-x**5)/(16-x**8)
            self.assertEqual(original,s.source_kernel(x))

    def test_weight_and_jet_bounds_exact(self):
        for j in range(201):
            x=Q(j,200)
            t=1-x
            w=s.source_weight(x)
            self.assertTrue(Q(1,4)<=w<=1)
            defect=1-w
            self.assertTrue(0<=defect<=3*t)
            self.assertTrue(abs(defect-2*t)<=6*t*t)
            self.assertEqual(1/w,1+2*t+2*t**3-t**4)

    def test_authentic_conditional_two_stage_packet(self):
        for j in range(31):
            x=Q(j,30)
            u,v=s.two_geometric_parameters(x)
            self.assertEqual(u+v,x)
            for k in range(21):
                z=Q(k,20)
                conditional=s.conditional_grade_pgf(x,z)
                self.assertEqual(conditional,(1-u)*(1-v)/((1-u*z)*(1-v*z)))
                self.assertEqual(s.source_kernel(x)*conditional,
                                 (1-x)/(4*(1-u*z)*(1-v*z)))

    def test_triangle_median_insertion_exhaustive(self):
        grid=tuple(Q(j,4) for j in range(5))
        count=0
        for n in range(10):
            for row in combinations_with_replacement(grid,n):
                for v in grid:
                    got=s.uniform_rank_insert(row,v)
                    expected=tuple(sorted((*row,v)))
                    self.assertEqual(got,expected)
                    for r,x in enumerate(got):
                        self.assertLessEqual(Q(0) if r==0 else row[r-1],x)
                        self.assertLessEqual(x,Q(1) if r==n else row[r])
                    count+=1
        self.assertEqual(count,10010)

    def test_second_largest_beta_moments_independent_factorials(self):
        for a in range(35):
            for k in range(12):
                independent=Q((a+2)*(a+1)*factorial(a)*factorial(k+1),factorial(a+k+2))
                self.assertEqual(s.beta_second_minimum_moment(a,k),independent)

    def test_source_rejection_rate_bounds(self):
        for a in range(100):
            tmean=s.beta_second_minimum_moment(a,1)
            t2=s.beta_second_minimum_moment(a,2)
            self.assertEqual(tmean,Q(2,a+3))
            self.assertEqual(t2,Q(6,(a+3)*(a+4)))
            self.assertEqual(s.rejection_error_bound(a),3*tmean)
            self.assertEqual(s.rejection_first_jet_error(a),6*t2)

    def test_grade_negative_binomial_and_tail(self):
        for m in range(1,80):
            total=sum((s.grade_mass(j) for j in range(m)),Q(0))
            self.assertEqual(1-total,Q(m+2,2**(m+1)))
        for j in range(50):
            # Gamma(shape 2,rate 1) mixed with Poisson(Z): (j+1)/2**(j+2)
            integral=Q(factorial(j+1),factorial(j)*2**(j+2))
            self.assertEqual(s.grade_mass(j),integral)
            self.assertEqual(s.gamma_poisson_posterior_mean(j),Q(j+2,2))

    def test_endpoint_pgf_fixed_point_and_shadow_in_quadratic_field(self):
        q=s.golden_fixed_point_certificate()
        self.assertEqual(q["z"],(Q(1),Q(-1)))
        self.assertEqual(q["G(z)"],q["z"])
        self.assertEqual(q["H(z)"],q["4lambda4"])
        self.assertEqual(s.golden_power(q["lambda"],2),q["z"])
        for z in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            self.assertEqual(s.conditional_grade_pgf(Q(1),z),s.endpoint_grade_pgf(z))

    def test_family_rank_transition(self):
        lam=(Q(0),Q(1))
        one=(Q(1),Q(0))
        for r in range(1,25):
            harmonic,geometric=s.gamma_rank_recurrence_difference(r)
            self.assertEqual(harmonic,Q(1,r))
            self.assertEqual(geometric,s.golden_power(lam,r+2))
            g=s.golden_power(lam,r)
            g2=s.golden_power(lam,r+1)
            left=s.golden_add((harmonic,Q(0)),s.golden_add(g,(-g2[0],-g2[1])))
            self.assertEqual(left,s.golden_add((harmonic,Q(0)),geometric))

    def test_source_specific_golden_coefficient_algebra(self):
        lam=(Q(0),Q(1))
        powr=lambda n:s.golden_power(lam,n)
        scale=lambda m,v:s.golden_multiply((Q(m),Q(0)),v)
        add=s.golden_add
        # C(lambda)=-9/2-7lambda^2+4lambda^3+3lambda^4.
        c=add((Q(-9,2),Q(0)),add(scale(-7,powr(2)),
              add(scale(4,powr(3)),scale(3,powr(4)))))
        self.assertEqual(c,(Q(-19,2),Q(6)))
        # Cov_Gamma(logY-exp(-lambda Y),Y^2)=5+6(lambda^2-lambda^4).
        covariance=add((Q(5),Q(0)),add(scale(6,powr(2)),scale(-6,powr(4))))
        self.assertEqual(covariance,add((Q(5),Q(0)),scale(6,powr(3))))

    def test_mellin_rank_gluing_integer_moments(self):
        for r in range(1,9):
            for k in range(5):
                for q in (Q(0),Q(1,2),Q(1)):
                    K=s.laplace_mellin_rank_integer(r,q,k)
                    K2=s.laplace_mellin_rank_integer(r+1,q,k)
                    self.assertEqual(K2/K,Q(r+k,r)/(1+q))

    def test_same_marginals_do_not_identify_joint_field(self):
        z=Q(1,2)
        self.assertEqual(s.authentic_boundary_mixed(z,0),s.falsely_identified_boundary_mixed(z,0))
        for k in range(8):
            self.assertEqual(s.authentic_boundary_mixed(1,k),
                             s.falsely_identified_boundary_mixed(1,k))
        self.assertEqual(s.authentic_boundary_mixed(z,1),Q(8,9))
        self.assertEqual(s.falsely_identified_boundary_mixed(z,1),Q(16,27))
        self.assertEqual(s.authentic_boundary_mixed(z,1)-s.falsely_identified_boundary_mixed(z,1),Q(8,27))
        for k in range(1,7):
            self.assertNotEqual(s.authentic_boundary_mixed(z,k),
                                s.falsely_identified_boundary_mixed(z,k))

    def test_matched_first_jet_mutants_are_different(self):
        for eps in [Q(0),Q(1,5),Q(1,2),Q(1)]:
            for j in range(41):
                x=Q(j,40)
                w=s.source_weight(x)
                mutant=s.source_acceptance_counterweight(x,eps)
                self.assertEqual(mutant,w*(1-eps*(1-x)**2))
                self.assertTrue(0<=mutant<=w)
                self.assertLessEqual(w-mutant,eps*(1-x)**2)
                if eps>0 and x<1:
                    self.assertLess(mutant,w)

    def test_original_source_prefix_and_tail_complement(self):
        # Coefficients (pi_coefficient, rational_coefficient) of exact T_n.
        def T(n):
            if n==0:
                return Q(1,16),Q(0)
            return Q(16**(n-1)), -s.zero_seed_prefix(n)
        self.assertEqual(s.forcing(1),Q(47,15))
        self.assertEqual(s.zero_seed_prefix(0),Q())
        for n in range(30):
            pi_coeff,rational_coeff=T(n)
            next_pi,next_rat=T(n+1)
            self.assertEqual(next_pi,16*pi_coeff)
            self.assertEqual(next_rat,16*rational_coeff-s.forcing(n+1))
            self.assertEqual(s.zero_seed_prefix(n+1),16*s.zero_seed_prefix(n)+s.forcing(n+1))

    def test_input_mutations_are_rejected(self):
        with self.assertRaises(ValueError): s.source_weight(Q(3,2))
        with self.assertRaises(ValueError): s.conditional_grade_pgf(Q(1,2),Q(3,2))
        with self.assertRaises(ValueError): s.uniform_rank_insert((Q(1,2),Q(1,4)),Q(1,3))
        with self.assertRaises(ValueError): s.uniform_rank_insert((Q(1,3),),Q(-1))
        with self.assertRaises(ValueError): s.source_acceptance_counterweight(Q(1,2),Q(2))
        with self.assertRaises(ValueError): s.forcing(0)
        with self.assertRaises(ValueError): s.grade_mass(-1)
        with self.assertRaises(ValueError): s.laplace_mellin_rank_integer(0,Q(1),0)


if __name__=="__main__":
    unittest.main()
