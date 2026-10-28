"""Exact finite source-prior controls. Not a continuum/physics proof."""
import importlib.util
import sys
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("inflation_prior_minimal",ROOT/"scripts/inflation_prior_minimal.py")
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class ExactPriorSmokeTests(unittest.TestCase):
    def test_genuine_source_rates(self):
        for k in range(65):
            x=F(k,64)
            u,v=m.rates(x)
            self.assertEqual(u+v,x)
            self.assertEqual(u*v,x**3*(2-x)/4)
    def test_innovation_law_and_evidence(self):
        prior=m.finite_prior([F(1,2),F(3,4)])
        self.assertEqual(sum(prior.values()),1)
        avg,second,var=m.moments(prior)
        self.assertGreater(var,0)
        self.assertEqual(m.moments(m.after_event(prior,1))[0],second/avg)
        self.assertLess(m.moments(m.after_event(prior,0))[0],avg)
    def test_no_source_uncertainty_control(self):
        self.assertEqual(m.moments({F(1,2):F(1)})[2],0)
    def test_predictive_oily_failure(self):
        self.assertEqual(m.rate_q(1)*(1+F(5,27)),F(8,27))
        self.assertEqual(F(8,27)-F(1,4),F(5,108))
    def test_geometric_patch_scaling(self):
        for n in range(6):
            self.assertEqual(8**n,(2**n)**3)

if __name__ == '__main__':unittest.main()
