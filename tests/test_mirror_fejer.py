"""Möbius mirror Fejér positive-sheet identities; finite diagnostic only."""
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

P=(Path(__file__).resolve().parents[1]/'research'/'2026-11-02'/'mobius_mirror'/'mobius_mirror.py')
S=importlib.util.spec_from_file_location('mobius_mirror_fejer',P)
m=importlib.util.module_from_spec(S);S.loader.exec_module(m)


def energies(points,H,axis=0):
    cs=[sum((m.circle_e(h*x) for x in points),0j)/len(points)
        for h in range(H+1)]
    ED=1+2*sum((1-h/(H+1))*abs(cs[h])**2 for h in range(1,H+1))
    EM=1+2*sum((1-h/(H+1))*
             (m.circle_e(-h*axis)*cs[h]**2).real for h in range(1,H+1))
    defect=sum((1-h/(H+1))*abs(cs[h]-m.circle_e(h*axis)*cs[h].conjugate())**2
               for h in range(1,H+1))
    return ED,EM,defect


class ReflectionFejerTests(unittest.TestCase):
    def test_exact_difference_mirror_energy_identity_original(self):
        for N,H in ((16,4),(32,7),(64,11)):
            U=m.original_states(N-1)
            for a in (Fraction(0),Fraction(1,15),Fraction(34,55)):
                ED,EM,D=energies(U,H,a)
                self.assertAlmostEqual(ED-EM,D,places=11)
                self.assertGreaterEqual(D,-1e-10)

    def test_two_mirror_conditional_energy_bound_original(self):
        eta=m.golden_axis()
        for N,H in ((16,4),(32,7),(64,11)):
            U=m.original_states(N-1)
            ED,_,d0=energies(U,H,0)
            _,_,de=energies(U,H,eta)
            self.assertLessEqual(ED-1,(9*H*H/4)*(d0+de)+1e-8)

    def test_coherent_zero_seed_reflection_vanishes_but_not_energy(self):
        for N,H in ((16,4),(64,8)):
            points=[Fraction(0)]*N
            ED,EM,D=energies(points,H,Fraction(0))
            self.assertAlmostEqual(ED,H+1,places=11)
            self.assertAlmostEqual(D,0,places=11)
            self.assertAlmostEqual(ED,EM,places=11)

    def test_periodic_real_counterseed_breaks_false_cancellation(self):
        for q in (Fraction(1,5),Fraction(1,7)):
            points=[q]*32
            ED,EM,D=energies(points,8,Fraction(0))
            self.assertAlmostEqual(ED,9,places=11)
            self.assertGreater(D,0)
            self.assertLessEqual(EM,ED+1e-11)

    def test_finite_golden_fibonacci_second_axis(self):
        U=m.original_states(80)
        H=8;k=10
        axis=m.finite_golden_axis(k)
        self.assertGreaterEqual(m.fib(k),3*H)
        ED,_,d0=energies(U,H,0)
        _,_,d2=energies(U,H,axis)
        # For finite golden approximants the upper inverse condition is
        # 3|h|/2, rather than 3|h|/4 for irrational golden.
        self.assertLessEqual(ED-1,9*H*H*(d0+d2)+1e-10)

if __name__ == '__main__':unittest.main()
