"""Source-exact folded shear and quantitative valve budget."""
import importlib.util
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

FOLDER=Path(__file__).resolve().parents[1]/"research"/"2026-11-04"/"alias_valve"
sys.path.insert(0,str(FOLDER))
sp=importlib.util.spec_from_file_location("sharp_shear",FOLDER/"sharp_shear.py")
s=importlib.util.module_from_spec(sp)
sp.loader.exec_module(s)
from alias_valve import flux


class SharpOriginalShear(unittest.TestCase):
    def test_exact_double_vs_signed_fold(self):
        for A in (8,12,24,40,64):
            self.assertEqual(s.double_shear(A),s.folded_shear(A))
            self.assertGreater(s.folded_shear(A),0)

    def test_sharp_flux_budget_improves_original(self):
        for A,q in ((8,2),(12,4),(24,8),(40,8)):
            f=flux(A,q)
            self.assertEqual(s.folded_shear(A),f["positive_source_shear"])
            self.assertLessEqual(abs(f["normalized_imbalance"]),s.refined_flux_cap(A,q))
            self.assertLessEqual(s.refined_flux_cap(A,q),f["normalized_cap"])

    def test_convergence_calibrated_no_asymptotic_inference(self):
        from math import log
        C=(15/64)*(1.5-log(4))
        for A in (64,128,256):
            err=abs(float(s.folded_shear(A))-C)
            self.assertLess(err,0.06/A)

    def test_invalid(self):
        for A in (-1,0,1):
            with self.assertRaises(ValueError):s.folded_shear(A)
