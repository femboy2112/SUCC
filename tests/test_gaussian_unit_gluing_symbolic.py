"""Separate SymPy exact polynomial implementation, not blind referee."""
import importlib.util
import unittest
from pathlib import Path
P=(Path(__file__).resolve().parents[1]/'research'/'2026-11-03'
   /'gaussian_unit_gluing'/'symbolic_oracle.py')
S=importlib.util.spec_from_file_location('unit_sympy_oracle',P)
f=importlib.util.module_from_spec(S);S.loader.exec_module(f)

class SymbolicOracle(unittest.TestCase):
    def test_original_transfer_factorization_and_reconstruction(self):
        r=f.run()
        self.assertEqual(r['hankel_determinant'],4)
        self.assertEqual(r['minimal_integer_discriminant'],-2048)
        self.assertEqual(r['fourpole_resultant'],-2**15*3**2*5**2)
        self.assertEqual(r['fourpole_den_discriminant'],2**24*3**2*5**2)
        self.assertEqual(r['mutation_integral_shift'],'67/480')
        self.assertFalse(r['claims_pi_normality'])

if __name__=='__main__':unittest.main()
