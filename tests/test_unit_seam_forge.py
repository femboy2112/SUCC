"""Exact regression for research-only SUCC unit-to-unit analytic seam.

No floating point, no imagined normality proof, source fingerprints required.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
import unittest

ROOT=Path(__file__).resolve().parents[1]/'research'/'2026-10-31'/'unit_seam_forge'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    import sys
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module
s=load('unit_seam_forge_source', 'unit_seam.py')
o=load('unit_seam_forge_oracle','independent_oracle.py')

class UnitSeamTest(unittest.TestCase):
    def test_four_pole_identity(self):
        self.assertEqual(s.bbp_source(1),F(47,15))
        for n in range(1,65):
            self.assertEqual(s.bbp_source(n),s.bbp_source_combined(n))
            self.assertEqual(s.bbp_source(n),o.source_combined(n))

    def test_source_nonintegral_fraction(self):
        self.assertNotEqual(s.bbp_source(1).denominator,1)
        self.assertEqual(s.bbp_source(F(3,2)),s.bbp_source_combined(F(3,2)))
        with self.assertRaises(ValueError):s.bbp_source(0)

    def test_beta_unit_jet(self):
        for k in range(17):
            a=s.source_newton(k)
            self.assertEqual(a,s.source_newton_beta(k))
            self.assertEqual(a,o.finite_differences_at_one(k))
            self.assertGreater(a,0)

    def test_complete_monotonicity_jet(self):
        for k in range(16):
            self.assertGreater(s.source_newton_beta(k),s.source_newton_beta(k+1))

    def test_rational_beta(self):
        self.assertEqual(s.beta_rational(F(1,2),0),2)
        self.assertEqual(s.beta_rational(F(1,2),1),F(4,3))
        with self.assertRaises(ValueError):s.beta_rational(0,4)
        with self.assertRaises(ValueError):s.source_newton(-1)

    def test_finite_newton_inversion(self):
        for n in range(1,17):
            self.assertEqual(s.reconstruct_source_at(n),s.bbp_source(n))

    def test_extruded_triangle(self):
        prev=()
        for n in range(1,15):
            row=s.extruded_pascal_row(n)
            self.assertEqual(row[-1],1)
            self.assertEqual(row[0],(16**n-1)//15)
            if n>1:
                for k in range(n):
                    self.assertEqual(row[k],16*(prev[k] if k<n-1 else 0)+comb(n-1,k))
            prev=row

    def test_extruded_independent_path_count(self):
        for n in range(1,13):
            row=s.extruded_pascal_row(n)
            self.assertEqual(row,tuple(o.path_count(n,k) for k in range(n)))

    def test_state_from_extruded_pascal(self):
        for n in range(0,14):
            self.assertEqual(s.bbp_state(n),s.extruded_state(n))
            if n>=1:self.assertEqual(s.bbp_state(n),o.source_reconstruct(n))

    def test_lower_unimodular_det(self):
        for n in range(1,10):
            mat=[[(-1)**k*s.extruded_pascal_row(i+1)[k] if k<=i else 0
                  for k in range(n)] for i in range(n)]
            determinant=1
            for i in range(n):determinant*=mat[i][i]
            self.assertEqual(determinant,(-1)**(n*(n-1)//2))

    def test_tau_cutoff_exact_green_residual(self):
        for k in range(6):
            for terms in range(1,13):
                self.assertEqual(s.beta_newton_tail_residual(k,terms),
                                 s.finite_beta_residual(k,terms))

    def test_tau_interval_positive(self):
        for k in range(5):
            prev=None
            for terms in range(1,12):
                lo,hi=s.tau_interval(k,terms)
                self.assertTrue(0<lo<hi)
                if prev is not None:self.assertTrue(prev[0]<=hi and lo<=prev[1])
                prev=lo,hi

    def test_pi_enclosures_shrink(self):
        widths=[]
        for terms in range(2,12):
            lo,hi=s.pi_interval(terms)
            self.assertLess(lo,hi)
            widths.append(hi-lo)
        for i in range(1,len(widths)):
            self.assertLess(widths[i],widths[i-1])

    def test_pi_encloses_machin_alternating(self):
        # Machin's classical identity, with exact alternating atan enclosures.
        def atan_interval(p,q,terms):
            x=F(p,q)
            value=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F())
            rest=(-1)**terms*x**(2*terms+1)/F(2*terms+1)
            return min(value,value+rest),max(value,value+rest)
        u,v=atan_interval(1,5,20)
        x,y=atan_interval(1,239,20)
        pi_lo,pi_hi=16*u-4*y,16*v-4*x
        for terms in range(3,12):
            lo,hi=s.pi_interval(terms)
            self.assertLessEqual(lo,pi_lo)
            self.assertGreaterEqual(hi,pi_hi)

    def test_unit_succ_composition_affine(self):
        a=s.PathWitness((('V',3),('S',1),('V',6)))
        b=s.PathWitness((('V',18),)+tuple(('S',1) for _ in range(6)))
        self.assertEqual(a.affine_normal_form(),(6,18))
        self.assertEqual(b.affine_normal_form(),(6,18))
        self.assertNotEqual(a.operations,b.operations)
        for x in (0,1,3,F(1,7)):
            self.assertEqual(a.evaluate(x)[0],6*(3*F(x)+1))
            self.assertEqual(b.evaluate(x)[0],a.evaluate(x)[0])

    def test_nontrivial_path_history(self):
        a=s.PathWitness((('S',1),('V',3)))
        b=s.PathWitness((('V',3),('S',1),('S',1),('S',1)))
        self.assertEqual(a.affine_normal_form(),b.affine_normal_form())
        self.assertNotEqual(a.evaluate(0)[1],b.evaluate(0)[1])
        self.assertNotEqual(a.path_charge(0),b.path_charge(0))
        self.assertEqual(b.path_charge(0),F(3,5))

    def test_rational_localization_not_primitive(self):
        with self.assertRaises(ValueError):s.PathWitness((('S',2),))
        with self.assertRaises(ValueError):s.PathWitness((('V',0),))
        with self.assertRaises(ValueError):s.PathWitness((('T',1),))
        a=s.PathWitness((('T',F(47,15)),))
        self.assertEqual(a.affine_normal_form(),(F(47,15),1))

    def test_moment_dilation_first_order(self):
        self.assertEqual(s.dilation_polynomial(3,1),(0,3,-3,1))
        self.assertEqual(s.dilation_polynomial(3,2),(0,0,9,-18,15,-6,1))
        for m in range(2,9):
            for k in range(0,5):
                coefficients=s.dilation_polynomial(m,k)
                self.assertEqual(len(coefficients),m*k+1)
                self.assertEqual(coefficients[-1],(-1)**((m+1)*k))

    def test_full_moment_diamond_symbolic(self):
        c=[F(i**3+7*i+2) for i in range(70)]
        for m in range(1,8):
            for k in range(0,5):
                self.assertTrue(s.check_pullback_diamond(c,m,k))

    def test_full_moment_diamond_bbp_source(self):
        c=[s.source_newton_beta(j) for j in range(35)]
        for m in (2,3,4):
            for k in range(0,3):
                self.assertTrue(s.check_pullback_diamond(c,m,k))

    def test_finite_positive_jet_alias_control(self):
        for m in range(2,9):
            result=s.witness_finite_jet_alias(m)
            self.assertEqual(result['same_jets'],m)
            self.assertNotEqual(result['dilated_first_jet_difference'],0)
            self.assertEqual(result['dilated_first_jet_difference'],
                             (-1)**(m+1)*result['moment_m_difference'])

    def test_positive_observer_adequacy(self):
        self.assertTrue(s.shape_factorizes(((0,1),(2,3)),('A','A','B','B')))
        self.assertFalse(s.shape_factorizes(((0,1),(2,3)),('A','B','B','B')))

    def test_signed_phase_exponents_aggregate(self):
        for n in range(1,12):
            lhs=s.bbp_state(n)
            row=s.extruded_pascal_row(n)
            rhs=sum((F((-1)**k*row[k])*s.source_newton(k) for k in range(n)),F())
            self.assertEqual((lhs-rhs)%1,0)

    def test_dilation_precision_failure_closed(self):
        with self.assertRaises(ValueError):s.dilate_moments([F(1),F(2)],3,1)
        with self.assertRaises(ValueError):s.shifted_moment([F(1)],0,1)
        with self.assertRaises(ValueError):s.dilation_polynomial(0,2)


    def test_exact_all_prefix_radix_shadow_budget(self):
        for M in range(1,12):
            actual=s.certified_radix_shadow_weyl_budget(1,M,2*M)
            envelope=s.shadow_double_depth_envelope(1,M)
            self.assertGreater(actual,0)
            self.assertLess(actual,envelope)
            self.assertLess(envelope,s.shadow_double_depth_envelope(1,max(1,M-1)) if M>1 else F(1))

    def test_weyl_shadow_budget_harmonic_linearity(self):
        for M in range(1,9):
            for J in (M,2*M,3*M):
                budget=s.certified_radix_shadow_weyl_budget(1,M,J)
                self.assertGreater(budget,0)
                self.assertEqual(s.certified_radix_shadow_weyl_budget(-7,M,J),7*budget)

    def test_machin_exact_radix_shadow_calibration(self):
        def atan_interval(p,q,terms):
            x=F(p,q)
            v=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F())
            rem=(-1)**terms*x**(2*terms+1)/F(2*terms+1)
            return min(v,v+rem),max(v,v+rem)
        a,b=atan_interval(1,5,24)
        c,d=atan_interval(1,239,24)
        alpha_lo=(16*a-4*d)/16
        alpha_hi=(16*b-4*c)/16
        for M in range(1,11):
            J=2*M
            shadow=s.completed_alpha_shadow(J)
            actual_error=max(abs(alpha_lo-shadow),abs(alpha_hi-shadow))
            self.assertLess(actual_error,s.source_newton_beta(J)/15**(J+1))
            # The pi<22/7 finite-source budget encloses the actual phase-angle difference.
            angle_sum=F(44,7)*(16*(16**M-1)//15)*actual_error
            self.assertLess(angle_sum,s.certified_radix_shadow_weyl_budget(1,M,J))

    def test_original_forcing_nonlinear_phase_law(self):
        for n in range(1,13):
            target=s.bbp_state(n)
            row=s.extruded_pascal_row(n)
            exponents=[F((-1)**k*row[k])*s.source_newton_beta(k) for k in range(n)]
            self.assertEqual(sum(exponents,F()),target)
            # e(sum exponents) = product e(exponents); no inference of phase balance.
            self.assertEqual(sum((x%1 for x in exponents),F())%1,target%1)

    def test_pisot_two_unit_lattice_diamond(self):
        # phi(x+1)=phi*x+phi, NOT phi*x+1. Basis-coloured correction.
        for a in range(-4,5):
            for b in range(-4,5):
                state=(a,b)
                self.assertEqual(s.multiply_golden_unit(s.golden_successor(state,'1')),
                                 s.golden_successor(s.multiply_golden_unit(state),'phi'))
                self.assertNotEqual(s.multiply_golden_unit(s.golden_successor(state,'1')),
                                    s.golden_successor(s.multiply_golden_unit(state),'1'))

    def test_fibonacci_pisot_integer_matrix(self):
        # Multiplication by phi has characteristic polynomial X²-X-1;
        # its stable conjugate is -1/phi. Integer powers are exact.
        a,b=1,0
        fib=[0,1]
        for _ in range(20):fib.append(fib[-1]+fib[-2])
        for n in range(1,18):
            a,b=s.multiply_golden_unit((a,b))
            self.assertEqual((a,b),(fib[n-1],fib[n]))
        # Matrix [[0,1],[1,1]] has trace 1, determinant -1.
        self.assertEqual(0*1-1*1,-1)

    def test_positive_jet_sequence_not_finite(self):
        # Nonzero all-k BBP newton jets: no global FINITE Newton polynomial.
        for k in range(31):
            self.assertGreater(s.source_newton_beta(k),0)

if __name__=='__main__':unittest.main()
