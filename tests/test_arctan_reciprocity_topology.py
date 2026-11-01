"""AR-09 exact source-rational / irrational-mirror topology and band controls."""
import importlib.util
import pathlib
import sys
import unittest
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'arctan_reciprocity'
spec=importlib.util.spec_from_file_location('succ_topology_'+str(id(object())),ROOT/'topology_probe.py')
t=importlib.util.module_from_spec(spec);sys.modules[spec.name]=t;spec.loader.exec_module(t)

class ExactMirrorTopology(unittest.TestCase):
    def test_original_source(self):
        self.assertEqual(t.original_source(1),F(47,15))
        self.assertEqual(t.original_source(2),F(106,819))

    def test_rational_source_orbit(self):
        for n in (1,2,3,16,64):
            vals=t.original_orbit(n)
            self.assertEqual(len(vals),n)
            self.assertTrue(all(type(v) is F for v in vals))

    def test_gaussian_rational_nontorsion(self):
        self.assertTrue(t.mirror_is_nontorsion(F(106,819)))
        self.assertTrue(t.mirror_is_nontorsion(F(1,480)))
        for q in (0,1,-1):self.assertFalse(t.mirror_is_nontorsion(F(q)))

    def test_total_variation_exact_all_n_certificate(self):
        for n in (1,2,3,4,8,16,35,65):
            s=t.certified_bbp_mirror_tv(n)
            self.assertTrue(s['mutually_singular'])
            self.assertEqual(s['total_variation_probability_metric'],1)
            self.assertEqual(s['variation_norm_of_difference'],2)

    def test_grid_fourier_exact(self):
        for M in (3,7,17,64,257):
            for h in range(-M-2,M+3):
                self.assertEqual(t.grid_fourier_character(M,h),int(h%M==0))

    def test_band_zero_but_maximal_total_variation(self):
        for M in (3,17,257):
            s=t.calibrated_grid_observer(M,M-1)
            self.assertTrue(s['all_nonzero_band_coefficients_identically_zero'])
            self.assertEqual(s['total_variation_probability_metric'],1)

    def test_invalid_domains(self):
        with self.assertRaises(t.TopologyError):t.original_orbit(0)
        with self.assertRaises(t.TopologyError):t.original_source(False)
        with self.assertRaises(t.TopologyError):t.mirror_is_nontorsion(0.123)
        with self.assertRaises(t.TopologyError):t.calibrated_grid_observer(17,17)
        with self.assertRaises(t.TopologyError):t.grid_fourier_character(1,1)

if __name__=='__main__':unittest.main()
