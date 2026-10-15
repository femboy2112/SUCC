"""Exact finite-source normalization and adversarial controls; no RH claim."""
from __future__ import annotations
import cmath
import unittest
from fractions import Fraction as F
from math import gcd, pi
from itertools import product

from observational_succ.one_object_transport import (
    OneObjectError, contact_rational_increment, contact_tail_majorant,
    screw_uniform_tail_majorant, original_prime_atoms,
    even_bump, even_bump_second, stage_identity_bump,
    analytic_shift_no_go, anchored_kernel, gram_two_point_determinant,
    connes_finite_clock_trace, connes_local_fixed_point_factor,
    connes_trace_stabilization, sonin_compact_defect_countermodel,
    sonin_log_moment_annihilator,
)


class WeilSuzukiContactTests(unittest.TestCase):
    def test_contact_increment_rational_exact(self):
        self.assertEqual(contact_rational_increment(0),0)
        self.assertEqual(contact_rational_increment(1),F(2))
        self.assertEqual(contact_rational_increment(2),F(32,15))
        for J in range(1,40):
            self.assertEqual(contact_rational_increment(J+1)-contact_rational_increment(J),
                             F(4,4*J+1)-F(2,2*J+1))
            self.assertGreater(contact_rational_increment(J+1),contact_rational_increment(J))

    def test_contact_telescoping_and_rational_majorant(self):
        import mpmath as mp
        mp.mp.dps=75
        true=mp.pi/2+mp.log(2)
        for J in (1,2,3,6,12,20,40,80):
            v=contact_rational_increment(J)
            residual=true-mp.mpf(v.numerator)/v.denominator
            upper=contact_tail_majorant(J)
            self.assertGreater(residual,0)
            self.assertLess(residual,mp.mpf(upper.numerator)/upper.denominator)
            for R in (0,F(1,2),F(2),F(4)):
                self.assertEqual(screw_uniform_tail_majorant(J,R),
                                 (1+F(R,2))*upper)

    def test_probe_rejects_spurious_source_cutoff(self):
        self.assertEqual(original_prime_atoms(F(1,2)),())
        self.assertEqual(original_prime_atoms(1),((2,2),))
        self.assertEqual(original_prime_atoms(2),((2,2),(3,3),(4,2),(5,5),(7,7)))
        self.assertNotIn(6,(n for n,p in original_prime_atoms(2)))
        for r in (True,0.5,-1,F(9),"2"):
            with self.assertRaises(OneObjectError):original_prime_atoms(r)

    def test_smooth_compact_bump_law(self):
        import mpmath as mp
        mp.mp.dps=70
        for radius in (F(1,2),F(1),F(2)):
            self.assertEqual(even_bump(0,radius),1)
            self.assertEqual(even_bump(radius,radius),0)
            self.assertEqual(even_bump_second(radius,radius),0)
            R=mp.mpf(radius.numerator)/radius.denominator
            self.assertLess(abs(mp.diff(lambda x:even_bump(x,radius),R/3,2)
                                -even_bump_second(R/3,radius)),mp.mpf('1e-60'))

    def test_original_prime_pole_gamma_contact_glue_9_holdouts(self):
        for radius,J in product((F(1,2),F(1),F(2)),(0,2,5)):
            receipt=stage_identity_bump(radius,J,60)
            self.assertLess(receipt['residual_abs'],__import__('mpmath').mpf('1e-48'))
            self.assertTrue(receipt['original_contact'])
            self.assertFalse(receipt['RH_proved'])

    def test_contact_mutation_creates_exact_detectable_defect(self):
        import mpmath as mp
        for radius in (F(1), F(2)):
            base=stage_identity_bump(radius,3,60)
            mutated=stage_identity_bump(radius,3,60,F(1,3))
            self.assertLess(abs(mutated['residual_abs']-F(1,3)),mp.mpf('1e-45'))
            self.assertFalse(mutated['original_contact'])
            self.assertLess(base['residual_abs'],mp.mpf('1e-48'))

    def test_wrong_domains_rejected(self):
        for J in (True,-1,65,2.0):
            with self.assertRaises(OneObjectError):stage_identity_bump(F(1),J)
        with self.assertRaises(OneObjectError):stage_identity_bump(F(5),3)
        with self.assertRaises(OneObjectError):contact_tail_majorant(0)


class HilbertFactorGateControls(unittest.TestCase):
    def test_rational_rank_one_positive_gram(self):
        g=lambda t:-t*t
        xs=(F(-3,2),F(0),F(1,3),F(4,5),F(2))
        for x,y in product(xs,xs):
            self.assertEqual(anchored_kernel(g,x,y),2*x*y)
            self.assertEqual(gram_two_point_determinant(g,x,y),0)

    def test_fake_non_euler_source_glues_but_no_hilbert_factor(self):
        for x,b,w in ((2,1,1),(F(3,2),F(1,4),F(1,2)),(4,1,7)):
            o=analytic_shift_no_go(x,b,w)
            self.assertTrue(o['distribution_to_primitive_commutes'])
            self.assertLess(o['gram_diagonal'],0)
            self.assertFalse(o['authentic_zeta'])
            self.assertFalse(o['hilbert_factorization_possible'])
        with self.assertRaises(OneObjectError):analytic_shift_no_go(1,2,1)

    def test_source_free_negative_kernel(self):
        g=lambda t:t*t
        self.assertEqual(anchored_kernel(g,1,1),-2)
        self.assertEqual(gram_two_point_determinant(g,1,2),0)
        with self.assertRaises(OneObjectError):anchored_kernel(lambda t:float(t),1,1)


class ConnesTateFiniteTraceTests(unittest.TestCase):
    def test_direct_fixed_points_equal_gcd(self):
        for p,r in ((2,1),(2,3),(3,1),(3,3),(5,2),(7,1)):
            mod=p**r
            for u in range(-11,12):
                if gcd(u,p)!=1:continue
                direct=sum(1 for x in range(mod) if (u*x-x)%mod==0)
                self.assertEqual(direct,connes_finite_clock_trace(p,r,u))
                self.assertEqual(direct,gcd(u-1,mod))

    def test_true_stabilization_away_from_identity(self):
        self.assertEqual(connes_trace_stabilization(3,10,6)['traces'],(3,9,9,9,9,9))
        self.assertEqual(connes_local_fixed_point_factor(3,10),9)
        self.assertEqual(connes_local_fixed_point_factor(2,3),2)
        self.assertEqual(connes_local_fixed_point_factor(7,2),1)
        for p,u in ((2,3),(3,10),(5,26),(7,50)):
            v=connes_local_fixed_point_factor(p,u)
            seq=[connes_finite_clock_trace(p,r,u) for r in range(1,5)]
            self.assertEqual(seq[-1],v)

    def test_identity_trace_blowup_and_fake_place_refusal(self):
        self.assertEqual(connes_trace_stabilization(3,1,4)['traces'],(3,9,27,81))
        with self.assertRaises(OneObjectError):connes_local_fixed_point_factor(3,1)
        for p in (4,6,9,1,0):
            with self.assertRaises(OneObjectError):connes_finite_clock_trace(p,1,1)
        with self.assertRaises(OneObjectError):connes_finite_clock_trace(3,1,3)

    def test_fourier_intertwiner_finite_additive_clock(self):
        # Secondary complex calibration; proof uses exact character orthogonality.
        for p,r,u in ((3,2,2),(5,1,3),(7,1,2)):
            m=p**r
            vec=[(k*k+3*k+1)%11 for k in range(m)]
            ft=lambda f,k:sum(f[x]*cmath.exp(-2j*pi*k*x/m) for x in range(m))
            inv=pow(u,-1,m)
            transported=[vec[(inv*x)%m] for x in range(m)]
            for k in range(m):
                self.assertLess(abs(ft(transported,k)-ft(vec,(u*k)%m)),1e-9)
            self.assertEqual(sum((u*x)%m==x for x in range(m)),
                             sum((u*k)%m==k for k in range(m)))


class SoninDefectControls(unittest.TestCase):
    def test_arbitrarily_small_compact_defect_breaks_positive_trace(self):
        for n in (1,2,5,10,30,64,120):
            d=sonin_compact_defect_countermodel(n)
            self.assertEqual(d["positive_trace_diagonal"],F(1,2**n))
            self.assertEqual(d["rank_one_defect"],-2*d["positive_trace_diagonal"])
            self.assertEqual(d["combined_signed_eigenvalue"],-d["positive_trace_diagonal"])
            self.assertEqual(d["defect_rank"],1)
            self.assertLess(d["combined_signed_eigenvalue"],0)
            self.assertFalse(d["compactness_implies_Weil_sign"])
            self.assertFalse(d["original_zeta_source"])
        self.assertLess(sonin_compact_defect_countermodel(30)["defect_norm"],F(1,10**8))
        for bad in (0,129,True,0.5,-1):
            with self.assertRaises(OneObjectError):
                sonin_compact_defect_countermodel(bad)


class SoninMomentDomainTests(unittest.TestCase):
    def test_correct_two_weight_nulls_and_wrong_parity_mutant(self):
        c=F(1,2)
        self.assertEqual(sonin_log_moment_annihilator(F(0),c),F(0))
        self.assertEqual(sonin_log_moment_annihilator(F(1,2),c),F(0))
        self.assertEqual(sonin_log_moment_annihilator(F(1),c),F(1,2))
        self.assertEqual(sonin_log_moment_annihilator(F(-1,2),c),F(1,2))
        self.assertNotEqual(sonin_log_moment_annihilator(F(1,2),-c),0)
        for bad in (True,0.5,"1/2"):
            with self.assertRaises(OneObjectError):
                sonin_log_moment_annihilator(bad)

    def test_exact_integration_by_parts_polynomial_witness(self):
        # phi(x)=(1-x^2)^3 on [-1,1] is Cc^2;
        # v=phi''+phi'/2. Integration by parts holds without boundary terms.
        # Derivative = (-6*x+12*x^3-6*x^5),
        # second derivative = (-6+36*x^2-30*x^4).
        from mpmath import mp
        mp.dps=65
        phi=lambda t:(1-t*t)**3 if abs(t)<1 else mp.mpf(0)
        derivative=lambda t: (-6*t+12*t**3-6*t**5) if abs(t)<1 else mp.mpf(0)
        second=lambda t: (-6+36*t**2-30*t**4) if abs(t)<1 else mp.mpf(0)
        v=lambda t:second(t)+mp.mpf("0.5")*derivative(t)
        for lam in (F(0),F(1,2),F(1)):
            ell=mp.mpf(lam.numerator)/lam.denominator
            left=mp.quad(lambda t:mp.exp(ell*t)*v(t),[-1,0,1])
            p=mp.quad(lambda t:mp.exp(ell*t)*phi(t),[-1,0,1])
            e=sonin_log_moment_annihilator(lam)
            right=mp.mpf(e.numerator)/e.denominator*p
            self.assertLess(abs(left-right),mp.mpf("1e-53"))


if __name__ == '__main__':unittest.main()
