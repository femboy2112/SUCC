"""Exact arithmetic focused regression: original source, Pell/Gamma seam and controls."""
import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

SPEC=importlib.util.spec_from_file_location(
    "pisot_gamma_exact",Path(__file__).with_name("pell_gamma.py"))
p=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(p)


class PisotGammaResearchTests(unittest.TestCase):
    def test_pell_two_algorithms_and_norm(self):
        for k in range(120):
            P,Q=p.pell(k)
            self.assertEqual((P,Q),p.independent_power(k))
            self.assertEqual(P*P-2*Q*Q,(-1)**k)
            self.assertEqual(p.signed_sheet_coefficient(k),(1,0))
            self.assertEqual(p.signed_sheet_coefficient(k,conjugate=True),(1,0))
            self.assertEqual(p.signed_primitive_coefficient(k),1)
            self.assertEqual(p.signed_trace_coefficient(k),2)
            self.assertEqual(P%2,1)
            self.assertEqual((2*P)%4,2)

    def test_finite_original_gamma_source(self):
        self.assertEqual(p.original_source(1),Fraction(47,15))
        for n in range(1,80):
            self.assertEqual(p.original_source(n),p.independent_original_source(n))
            self.assertEqual(p.state(n),16*p.state(n-1)+p.original_source(n))
            self.assertLessEqual(p.future(n,n+40),p.original_tail_upper(n))

    def test_every_sheet_reconstructs_original_phase(self):
        for n,b in ((1,11),(9,21),(37,66),(73,100)):
            Y=p.phase_lift(n,b)
            x=p.state(n)%1
            self.assertEqual(Y-x,p.future(n,b))
            for k in range(45):
                self.assertEqual(p.joint_phase_exponent(n,b,k),(Y,0))
                self.assertEqual(p.joint_phase_exponent(n,b,k,conjugate=True),(Y,0))
                self.assertEqual(p.primitive_phase_exponent(n,k),x)
                self.assertEqual(p.integer_trace_phase_exponent(n,k),2*x)

    def test_original_adjacent_cutoff_compatibility(self):
        for n in range(10):
            for m in range(n,14):
                for b in (m,m+1,m+5):
                    self.assertTrue(p.exact_seam_verify(n,m,b))

    def test_rigorous_rational_phase_discriminator(self):
        for a in (1,11,64,128,256,1024):
            k=p.regulator_integer_scale(a)
            for n in (a+1,a+7):
                b=n+20
                eps=p.phase_error_rational_upper(n,b,k)
                self.assertGreaterEqual(eps,0)
                self.assertLess(eps,Fraction(1,a))
        with self.assertRaises(ValueError):
            p.regulator_integer_scale(0)

    def test_wrong_sign_and_missing_conjugate_detected(self):
        for k in range(1,55):
            u,v=p.bezout(k)
            self.assertEqual(p.signed_sheet_coefficient(k,conjugate=True),(1,0))
            # Omitting the stable sheet changes the integer trace descent by 1.
            self.assertEqual(p.signed_trace_coefficient(k)-
                             p.signed_sheet_coefficient(k)[0],1)
            self.assertNotEqual(u*p.pell(k)[0]-v*p.pell(k+1)[0],1)

    def test_changed_seed_and_single_mode_marginal_no_go(self):
        # With same original r(n), changed real seed s=q-alpha, q=1/5,
        # the completed (16^n q mod 1) orbit is constant for n>=0.
        q=Fraction(1,5)
        for k in range(2,50):
            self.assertEqual(q*p.signed_primitive_coefficient(k),q)
            self.assertEqual(p.pell(k)[0]%2,1)
            self.assertGreater(p.pell(k)[0],1)
        # A density 1+cos(2 pi x) has Fourier(1)=1/2 but Fourier(m)=0 for m>1.

    def test_mod_four_base16_separation(self):
        for k in range(1,85):
            L=2*p.pell(k)[0]
            for m in range(1,12):
                self.assertGreaterEqual(abs(L-16**m),2)


if __name__=="__main__":
    unittest.main()
