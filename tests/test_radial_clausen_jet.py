"""Finite original-source test of fixed-radius radial-null observer derivative bounds.
Float diagnostics only; rigorous all-A bound appears in RELATIVE_ZERO_JETS.md.
"""
import unittest
from fractions import Fraction as F
from math import pi,log,cos
import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parent/'test_critical_carry_jets.py'
spec=importlib.util.spec_from_file_location('critical',P)
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

def energy(U,Z,A,lam,r=.5):
    vals=[float((U[n]+lam*Z[n])%1) for n in range(A,2*A)]
    total=0.
    for i,x in enumerate(vals):
        for y in vals[i+1:]:
            total+=log(1-2*r*cos(2*pi*(y-x))+r*r)
    return total/(A*A)

class RadialClausenJet(unittest.TestCase):
    def test_01_original_radial_null_source_energy_transport(self):
        for A in (139,277):
            U=c.states(2*A-1)
            Z=c.rad_states(2*A-1)
            baseline=energy(U,Z,A,F(0))
            for lam in (F(-2),F(1),F(3)):
                actual=energy(U,Z,A,lam)
                bound=(11*pi/80/A)*abs(lam)
                self.assertLessEqual(abs(actual-baseline),bound+1e-10)

    def test_02_fixed_radius_hessian_changes_sign(self):
        r=.5
        gpp_0=8*pi*pi*r/(1-r)**2
        gpp_half=-8*pi*pi*r/(1+r)**2
        self.assertGreater(gpp_0,0)
        self.assertLess(gpp_half,0)
        self.assertAlmostEqual(gpp_0,16*pi*pi)
        self.assertAlmostEqual(gpp_half,-16*pi*pi/9)

    def test_03_original_source_radial_jet_scale(self):
        Z=c.rad_states(1000)
        for A in (139,277,557):
            zmax=max(Z[A:2*A])
            self.assertLess(zmax,F(11,160*A))
            # At high H~A^2 log A first derivatives are not small.
            H=A*A
            self.assertGreater(float(H*Z[A]),A/64)

if __name__=='__main__':unittest.main()
