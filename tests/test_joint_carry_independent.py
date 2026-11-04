"""Independent exact-valuation/arithmetic-source oracle for the new cocycle."""
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

PATH=Path(__file__).resolve().parents[1]/'research/2026-11-03/joint_carry_cocycle/joint_carry.py'
sp=importlib.util.spec_from_file_location('jc_independent',PATH)
code=importlib.util.module_from_spec(sp);sp.loader.exec_module(code)


def independent_v2(x):
    x=Fraction(x)
    if not x:return None
    def count(n):
        k=0
        while n%2==0:n//=2;k+=1
        return k
    return count(abs(x.numerator))-count(x.denominator)


def independent_principal(x):
    x=Fraction(x)
    if not x:return Fraction(0)
    denominator=x.denominator
    ppart=1
    while denominator%2==0:
        denominator//=2
        ppart*=2
    if ppart==1:return Fraction(0)
    a=x.numerator
    # Alternative Garner inverse via Euler's theorem for 2-primary units.
    inv=pow(denominator, 1 if ppart==2 else ppart//2-1, ppart)
    return Fraction((a*inv)%ppart,ppart)


class IndependentPrimePowerOracles(unittest.TestCase):
    def test_source_against_canonical_parent_mellin(self):
        # Independent source implementation shipped with #481 on the same source lineage.
        parent=Path(__file__).resolve().parents[1]/'research/2026-11-03/gaussian_unit_gluing/gaussian_unit_gluing.py'
        spec=importlib.util.spec_from_file_location('gr_481',parent)
        g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
        for n in range(1,90):
            a,b=g.mellin_channels(n)
            self.assertEqual(code.real_source(n),a)
            self.assertEqual(code.gaussian_source(n),b)

    def test_independent_euler_inverse_and_p2_valuation(self):
        for n,a,b,u in code.full_zero_seed_modular(128):
            if n==0:continue
            for x in (a,b,u,code.real_source(n),code.gaussian_source(n)):
                self.assertEqual(independent_v2(x),code.v2_rational(x))
                self.assertEqual(independent_principal(x),code.principal2(x))

    def test_source_specific_nonintegral_torsion_equality(self):
        # Exact p2 direct rational carry via independent reconstruction.
        for n,a,b,u in code.full_zero_seed_modular(128):
            if n==0:continue
            self.assertEqual((independent_principal(a)+independent_principal(b))%1,0)
            self.assertEqual(independent_principal(u),0)
            self.assertEqual((a+b)%1,u)

if __name__=='__main__':unittest.main()
