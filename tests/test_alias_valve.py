"""Exact arithmetic tests for research/2026-11-04/alias_valve. No pi inputs."""
import importlib.util
import unittest
from pathlib import Path
from fractions import Fraction as F

P=Path(__file__).resolve().parents[1]/"research"/"2026-11-04"/"alias_valve"/"alias_valve.py"
spec=importlib.util.spec_from_file_location("alias_valve",P)
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class AliasValveExact(unittest.TestCase):
    def test_authentic_force(self):
        for n in range(1,160):
            self.assertEqual(v.force(n),v.force_closed(n))
            self.assertEqual(v.force(n).denominator%2,1)
        self.assertEqual(v.force(1),F(47,15))

    def test_independent_common_odd_modular_source(self):
        for A in (8,12,24):
            self.assertEqual(v.orbit(2*A-1),v.modular_orbit(2*A-1))

    def test_strict_oriented_lag_shear(self):
        for n in (1,2,7,16,32,129):
            for d in (1,2,3,8,31):
                self.assertGreater(v.shear(n,d),0)
                self.assertLess(v.shear(n,d),v.shear_cap(n,d))

    def test_all_sixteen_aliases_and_positive_leak(self):
        for q in (2,4,8,16):
            for den in (5,7,16,32,71):
                for a in range(-2*den,2*den+1,3):
                    x=F(a,den)
                    self.assertEqual(v.tent(16*x,q),v.tent(x,16*q)+v.lateral(x,q))
                    self.assertGreaterEqual(v.leakage(x,q),0)
                    self.assertGreaterEqual(v.lateral(x,q),0)

    def test_exact_source_valve_balance(self):
        for A,q in ((8,2),(12,4),(16,4),(24,8)):
            x=v.flux(A,q)
            self.assertEqual(x["leak"]-x["injection"],x["boundary"]+x["signed_source_flux"])
            self.assertLessEqual(abs(x["signed_source_flux"]),q*x["positive_source_shear"])
            self.assertLess(x["positive_source_shear"],x["source_shear_cap"])
            self.assertLessEqual(abs(x["normalized_imbalance"]),x["normalized_cap"])

    def test_signed_flux_has_both_signs(self):
        self.assertGreater(v.flux(12,4)["signed_source_flux"],0)
        self.assertLess(v.flux(24,8)["signed_source_flux"],0)

    def test_multiscale_release_and_exact_collision_residue(self):
        for A,q in ((8,2),(12,4),(16,4)):
            x=v.escape_receipt(v.orbit(2*A-1)[A:2*A],q,3)
            self.assertEqual(x["total"],x["release_at_J"]+x["unresolved_at_J"])
            self.assertEqual(x["exact_collision_pairs"],A)
            self.assertEqual(x["terminal_residue"],F(q,A))
            self.assertGreaterEqual(x["terminal_depth"],3)

    def test_odd_denominator_same_forcing_coherent_counterseed(self):
        for A,q in ((8,4),(12,8),(16,8)):
            seed,M,alpha=v.coherent_odd_seed(A)
            self.assertNotEqual(seed,0)
            self.assertEqual(seed.denominator%2,1)
            x=v.coherent_odd_receipt(A,q)
            self.assertTrue(x["odd_denominators"])
            self.assertGreater(x["J"],F(9*q,10))
            self.assertGreaterEqual(x["J"],x["lower_bound"])
            y=v.flux(A,q,seed)
            self.assertEqual(y["leak"]-y["injection"],y["boundary"]+y["signed_source_flux"])

    def test_fixed_point_never_releases(self):
        for q in (2,4,16):
            x=v.escape_receipt((F(1,5),)*16,q,3)
            self.assertEqual(x["total"],q)
            self.assertEqual(x["release_at_J"],0)
            self.assertEqual(x["unresolved_at_J"],q)
            self.assertEqual(x["exact_collision_pairs"],256)


if __name__=="__main__":
    unittest.main()
