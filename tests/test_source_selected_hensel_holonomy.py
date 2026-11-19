"""Exact finite validations for new SUCC source-selected Hensel/chronology research.
All source data original; no probabilistic digit assumptions or asymptotic proof claim.
"""
import importlib.util
from fractions import Fraction
from math import gcd
from pathlib import Path
import unittest

SRC=(Path(__file__).resolve().parents[1]/'research'/'2026-11-19'/'source_selected_hensel_holonomy'/'probe.py')
spec=importlib.util.spec_from_file_location('shh_probe',SRC)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class SourceHenselHolonomyTests(unittest.TestCase):
    def test_original_literal_source(self):
        self.assertEqual(m.forcing(1),Fraction(47,15))
        U=m.source_state(64)
        self.assertEqual(U[0],0)
        for n in range(1,65):self.assertEqual(U[n]-16*U[n-1],m.forcing(n))

    def test_source_filter_exact(self):
        self.assertEqual(m.source_filter(),((8,1),(1,7)))
        self.assertEqual(m.det2(m.source_filter()),55)
        self.assertEqual(m.M,((0,1),(1,-1)))
        self.assertEqual(m.matmul(m.A,m.M),m.eye(2))

    def test_source_filter_mutant(self):
        self.assertEqual(m.det2(m.mutated_filter()),116)
        self.assertNotEqual(m.det2(m.mutated_filter())%11,0)
        self.assertNotEqual(m.det2(m.source_filter())%29,0)

    def test_matched_jet_mutant_breaks_two_independent_signatures(self):
        self.assertEqual(m.matched_jet_filter(),((9,0),(0,9)))
        self.assertEqual(m.det2(m.matched_jet_filter()),81)
        self.assertNotEqual(81%11,0)
        for p in (7,11,13,17,29,41):
            n=(p*p-1)//8
            d=15*(m.matched_jet_forcing(n)-m.matched_jet_forcing(n+1))
            self.assertEqual(m.valuation(d,p),-2)
            self.assertEqual(m.rational_mod_p(p*p*d,p),(-75)%p)
        for n in (10,100,1000):
            self.assertGreater(m.matched_jet_forcing(n),m.forcing(n))

    def test_source_selected_image_and_kernel(self):
        H=m.source_filter()
        self.assertEqual(m.matvec(H,(1,3),11),(0,0))
        self.assertEqual(m.matvec(m.A,(1,3),11),(4,1))
        self.assertEqual(m.matvec(m.A,(8,1),11),(9,8))

    def test_quartic_eigenchannel_and_dual(self):
        w=m.sym4_vector((8,1),11)
        self.assertEqual(w,(4,6,9,8,1))
        self.assertEqual(m.matvec(m.T,w,11),tuple(16*x%11 for x in w))
        ell=(4,2,10,10,1)
        self.assertEqual(m.leftmul(ell,m.T,11),tuple(16*x%11 for x in ell))
        self.assertEqual(sum(a*b for a,b in zip(ell,w))%11,1)

    def test_hensel_source_splitting(self):
        self.assertEqual(m.hensel_quad(8,-1,-1,11,2),85)
        self.assertEqual(m.hensel_quad(4,-1,-1,11,2),37)
        self.assertEqual((8+pow(85,-1,121))%121,92)
        self.assertEqual((8+pow(37,-1,121))%121,44)

    def test_hensel_fibonacci_vs_radix(self):
        lam=m.hensel_quad(16,-47,1,11,2)
        self.assertEqual(lam,104)
        self.assertNotEqual(lam,16)
        self.assertEqual(pow(85,8,121),lam)
        w=m.sym4_vector((85,1),121)
        self.assertEqual(m.matvec(m.T,w,121),tuple(lam*x%121 for x in w))

    def test_29_is_homogeneous_nonselected_control(self):
        self.assertEqual(m.hensel_quad(16,-7,1,29,2),683)
        self.assertNotEqual(m.det2(m.source_filter())%29,0)

    def test_moving_frames_carry_extra_precision(self):
        rho=16*pow(104,-1,121)%121
        self.assertEqual(rho,56)
        for n in range(121):
            self.assertEqual(pow(rho,n,121),(1+55*n)%121)
            self.assertEqual((pow(rho,n+1,121)*104)%121,(16*pow(rho,n,121))%121)

    def test_moving_frame_higher_precision(self):
        for k in range(4):
            mod=11**(k+3)
            lam=m.hensel_quad(16,-47,1,11,k+3)
            rho=16*pow(lam,-1,mod)%mod
            z=(pow(rho,11**k,mod)-1)%mod
            self.assertEqual(z%(11**(k+1)),0)
            self.assertNotEqual(z%(11**(k+2)),0)

    def test_spurious_complex_weyl_mean(self):
        from cmath import exp,pi
        vals=[exp(2j*pi*5*n/11) for n in range(11)]
        self.assertLess(abs(sum(vals)),1e-12)
        self.assertAlmostEqual(abs(sum(1 for _ in vals)/11),1)

    def test_order_swap_difference_at_all_calibration_clocks(self):
        for n in range(1,85):
            a,b=m.forcing(n),m.forcing(n+1)
            original=16*(16*Fraction(17,19)+a)+b
            swapped=16*(16*Fraction(17,19)+b)+a
            self.assertEqual(original-swapped,m.source_order_defect(n))
            self.assertGreater(original-swapped,0)

    def test_source_order_jacobian_four_coefficients(self):
        for n in (1,7,15,55,100,233):
            for j in range(4):
                coefficients=list(m.C)
                coefficients[j]+=1
                derivative=m.source_order_defect(n,coefficients)-m.source_order_defect(n)
                self.assertEqual(derivative,m.commutator_gradient(n)[j])

    def test_macroscopic_delayed_order_difference(self):
        for n in (7,11,17,29,55,89,144,233,610,987,1597):
            k,t=m.visibility_delay(n)
            self.assertGreaterEqual(t,Fraction(1,32))
            self.assertLess(t,Fraction(1,2))
            self.assertLess(16**(k-1)*m.source_order_defect(n),Fraction(1,32))

    def test_prime_square_ladder(self):
        for p in (7,11,13,17,19,23,29,41,47):
            n,v,lead,d=m.source_prime_square_event(p)
            self.assertEqual(v,-2)
            self.assertEqual(lead,(-60)%p)
            self.assertEqual(8*n+1,p*p)

    def test_real_asymptotic_constant(self):
        for n in (5000,10000,25000):
            v=m.source_order_defect(n)*n**3
            self.assertGreater(v,Fraction(99,100)*Fraction(225,32))
            self.assertLess(v,Fraction(101,100)*Fraction(225,32))

    def test_same_forcing_changes_seed_not_innovation(self):
        a=m.source_state(35,Fraction(0))
        b=m.source_state(35,Fraction(1,257))
        for n in range(1,36):
            self.assertEqual(a[n]-16*a[n-1],b[n]-16*b[n-1])
            self.assertEqual(b[n]-a[n],Fraction(16**n,257))

if __name__=='__main__': unittest.main()
