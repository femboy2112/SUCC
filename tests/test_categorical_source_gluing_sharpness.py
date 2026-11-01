"""Independent exact lower-bound test for the global BBP delay embedding."""
from __future__ import annotations
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

PATH=(Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/
      'categorical_source_gluing'/'two_frame_sharpness.py')
spec=importlib.util.spec_from_file_location('succ_categorical_gluing_sharpness_oracle',PATH)
s=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=s
spec.loader.exec_module(s)

class SharpnessTests(unittest.TestCase):
    def test_full_exact_oracle(self):
        v=s.verify()
        self.assertEqual(v['resultant_degree'],9)
        self.assertTrue(v['distinct_real_lifts'])
        self.assertTrue(v['third_frame_distinguishes_all_resultant_roots'])
    def test_resultant_exact(self):
        self.assertEqual(s.polynomial_resultant(s.F0,s.F1),s.scale(s.Q,s.RES_SCALE))
    def test_source_shift_second(self):
        # Independent direct substitution for one rational test coordinate.
        x=F(13,31);p=F(-2,7)
        f=lambda terms,u,v:sum((s.evaluate(c,u)*v**i for i,c in enumerate(terms)),F(0))
        self.assertEqual(f(s.F1,x,p),f(s.F0,x+2,p+x+1))
        self.assertEqual(f(s.F2,x,p),f(s.F0,x+4,p+2*x+4))
    def test_resultant_real_sign_change(self):
        self.assertLess(s.evaluate(s.Q,s.LEFT),0)
        self.assertGreater(s.evaluate(s.Q,s.RIGHT),0)
    def test_positive_interval_polynomials(self):
        for v in (s.A,s.B,s.add(s.scale(s.B,8),s.scale(s.A,-1)),
                  s.add(s.A,s.scale(s.B,-4))):
            self.assertGreater(s.interval_eval(v,s.LEFT,s.RIGHT)[0],0)
    def test_inverse_source_divisibility(self):
        for f in (s.F0,s.F1):
            self.assertEqual(s.p_divmod(s.substituted_numerator(f),s.Q)[1],(F(0),))
    def test_third_frame_separates(self):
        v=s.substituted_numerator(s.F2)
        self.assertEqual(len(v),16)
        self.assertEqual(len(s.modp_gcd(s.Q,v,101)),1)
        self.assertNotEqual(s.Q[-1]%101,0)
        self.assertNotEqual(v[-1]%101,0)
    def test_original_resultant_mutation_rejected(self):
        mutated=s.add(s.Q,(1,))
        self.assertNotEqual(s.polynomial_resultant(s.F0,s.F1),s.scale(mutated,s.RES_SCALE))
    def test_wrong_third_frame_mutation_detected(self):
        # The first frame trivially cannot distinguish an H2 collision.
        v=s.substituted_numerator(s.F0)
        self.assertEqual(len(s.modp_gcd(s.Q,v,101)),len(s.Q))

if __name__=='__main__':unittest.main()
