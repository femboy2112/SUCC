"""Root-discoverable original BBP Pisot/Gamma/Pell exact arithmetic tests."""
import importlib.util
import pathlib
from fractions import Fraction
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
SRC=ROOT/"research"/"2026-11-02"/"pisot_gamma_gluing"
spec=importlib.util.spec_from_file_location("source_pisot_gamma",SRC/"pell_gamma.py")
pg=importlib.util.module_from_spec(spec)
spec.loader.exec_module(pg)


class PisotGammaRootTests(unittest.TestCase):
    def test_complete_two_conjugate_unit(self):
        for k in range(100):
            P,Q=pg.pell(k)
            self.assertEqual(P*P-2*Q*Q,(-1)**k)
            self.assertEqual(pg.signed_sheet_coefficient(k),(1,0))
            self.assertEqual(pg.signed_sheet_coefficient(k,True),(1,0))
            self.assertEqual(pg.signed_primitive_coefficient(k),1)
            self.assertEqual(pg.signed_trace_coefficient(k),2)

    def test_gamma_source_and_finite_boundary(self):
        for n in range(1,31):
            self.assertEqual(pg.original_source(n),pg.independent_original_source(n))
            self.assertEqual(pg.state(n),16*pg.state(n-1)+pg.original_source(n))
            for b in (n,n+3,n+10):
                self.assertEqual(pg.joint_phase_exponent(n,b,4),(pg.phase_lift(n,b),0))
                self.assertTrue(pg.exact_seam_verify(n,b,b+3))
                self.assertLessEqual(pg.future(n,b),pg.original_tail_upper(n))

    def test_nonzero_irrational_single_sheet_at_all_finite_seams(self):
        for n,b in ((2,8),(9,22),(31,52)):
            x=pg.state(n)%1
            r=pg.future(n,b)
            self.assertGreater(r,0)
            for k in (1,2,3,6,11,19):
                A,B=pg.gamma_trace_exponent_error(n,b,k)
                self.assertEqual(B,-pg.pell(k)[1]*(x+r))
                self.assertLess(B,0)

    def test_birth_prime_original_cyclotomic_entry(self):
        for p in (17,41,73,89,97,113,137,193,233,241):
            b=(p+7)//8
            self.assertEqual(8*b-7,p)
            self.assertTrue(all(pg.state(j).denominator%p for j in range(b)))
            B=pg.state(b)-Fraction(4,p)
            self.assertNotEqual(B.denominator%p,0)
            self.assertEqual(pg.state(b).denominator%p,0)

    def test_exact_regulator_schedule(self):
        for a in (1,11,64,128,256,1024,8192,1000000):
            k=pg.regulator_integer_scale(a)
            self.assertGreaterEqual(k,0)
            self.assertEqual(pg.signed_sheet_coefficient(k),(1,0))
            n=a+1;b=n+20
            if a<=1024:
                self.assertLess(pg.phase_error_rational_upper(n,b,k),Fraction(1,a))


if __name__=="__main__":
    unittest.main()
