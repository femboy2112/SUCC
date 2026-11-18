"""Actual-source prime bounds and strictly typed hostile source controls."""
from fractions import Fraction as F
import importlib.util
from math import lcm
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT / "research/2026-11-17/pro_pi_crucible"


def load(name):
    spec = importlib.util.spec_from_file_location("pro_pi_"+name, DOSSIER/(name+".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PRIME = load("prime_survival_probe")
GAMMA = load("gamma_source_probe")
FLAT = load("flat_lock_probe")
TestPositiveMomentSourceClone = GAMMA.PositiveSourceShellClone
TestFlatLockedSource = FLAT.Tests


class ProPiArithmeticTests(unittest.TestCase):
    def test_prime_cutoff_and_known_cancelled_primes(self):
        receipt = PRIME.run()
        self.assertEqual(receipt["exact_residue_checks"],1665)
        self.assertEqual(receipt["certificate_cases"],988)
        self.assertEqual(receipt["sign_mutation_rejections"],1662)
        for row in receipt["known_cancellations"]:
            self.assertTrue(row["cancelled"])
            self.assertTrue(row["cutoff_correctly_not_satisfied"])

    def test_elementary_lcm_bound_and_divisor_step(self):
        from math import comb
        values=[1]
        for k in range(1,257):
            values.append(lcm(values[-1],k))
            self.assertLessEqual(values[k],4**k)
            t=(k+1)//2
            self.assertEqual(comb(k,k//2)%(values[k]//values[t]),0)

    def test_one_global_integer_gauge_erases_every_terminal_block(self):
        u=F()
        g_previous=0
        v=F()
        for n in range(1,81):
            r=PRIME.original(n)
            u=16*u+r
            g=-((u.numerator//u.denominator)%16**(n//2))
            changed_r=r+g-16*g_previous
            v=16*v+changed_r
            self.assertEqual(v,u+g)
            self.assertEqual(v.denominator,u.denominator)
            self.assertEqual(v.numerator%v.denominator,u.numerator%u.denominator)
            self.assertEqual(changed_r.denominator,r.denominator)
            self.assertLess(abs(g),16**(n//2))
            if n%2==0:
                b=n//2
                self.assertEqual((v.numerator//v.denominator)%16**b,0)
                fraction=u-u.numerator//u.denominator
                norm=sum((GAMMA.circle_distance(v/16**k)**2 for k in range(1,b+1)),F())/b
                self.assertEqual(norm,fraction*fraction*(1-F(1,256**b))/(255*b))
            g_previous=g


if __name__ == "__main__":
    unittest.main(verbosity=2)
