"""Standalone SymPy derivation, distinct code path from Fraction source lab."""
from pathlib import Path
import importlib.util
import unittest

PATH=Path(__file__).resolve().parents[1]/'research/2026-11-03/causal_lorentz_gluing/independent_symbolic.py'
S=importlib.util.spec_from_file_location('causal_lorentz_symbolic',PATH)
M=importlib.util.module_from_spec(S);S.loader.exec_module(M)

class SympyOracle(unittest.TestCase):
    def test_all_exact_independent_symbolic_relations(self):
        d=M.proof_checks()
        self.assertEqual(d['gamma'],'257/32')
        self.assertEqual(d['beta'],'255/257')
        self.assertTrue(d['Lorentz_metric_preserved'])
        self.assertFalse(d['selected_pi_normality_proved'])

if __name__=='__main__':unittest.main()
