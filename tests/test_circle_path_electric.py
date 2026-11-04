"""Exact source and adversarial tests for BBP path groupoid / current tree."""
import sys
from pathlib import Path
import unittest
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research'/'2026-11-03'/'circle_path_electric'))
import circle_path_electric as M


class PathGroupoidTests(unittest.TestCase):
    def test_source_original_four_poles(self):
        self.assertEqual(M.authentic_r(1),Q(47,15))
        self.assertEqual(M.authentic_r(2),Q(106,819))

    def test_odd_inverse_unique(self):
        for Mmod in (1,3,5,7,15,17,31,41,101):
            for a in range(Mmod):
                x=Q(a,Mmod)
                y=(16*x)%1
                j,z=M.source_odd_predecessor(y)
                self.assertEqual(z,x)
                self.assertEqual(j,(16*x).numerator//(16*x).denominator)
                self.assertEqual(sum(t.denominator%2==1 for t in M.inverse_candidates(y)),1)

    def test_forced_odd_inverse_source(self):
        points=dict(M.phase_stream(769))
        for n in (1,2,3,31,97,193,385,769):
            y=points[n]
            prior=points[n-1]
            j,z=M.source_odd_predecessor(y,M.authentic_r(n))
            self.assertEqual(z,prior)
            self.assertEqual(j,int(16*prior))
            self.assertEqual(sum(t.denominator%2==1 for t in M.inverse_candidates(y,M.authentic_r(n))),1)

    def test_modular_independent_oracle_holdouts(self):
        q=dict(M.phase_stream(769))
        z=dict(M.modular_phase_stream(769))
        for n in (0,1,2,3,97,193,385,769):
            self.assertEqual(q[n],z[n])

    def test_discontinuous_odd_inverse(self):
        z=M.source_odd_predecessor(Q(0))[1]
        self.assertEqual(z,0)
        for k in (2,16,32,100):
            self.assertEqual(M.source_odd_predecessor(Q(1,16*k-1)),(1,Q(k,16*k-1)))
        self.assertEqual(M.source_odd_predecessor(Q(1,5)),(3,Q(1,5)))

    def test_dft_exact_group_ring(self):
        for d in range(-31,32):
            self.assertEqual(M.cyclotomic16_character_sum(d),(16,)+(0,)*7 if d%16==0 else (0,)*8)
        for j in range(16):
            self.assertEqual(M.selector_weights(j),tuple(int(a==j) for a in range(16)))

    def test_transfer_harmonics(self):
        for h in range(-256,257):
            self.assertEqual(M.transfer_frequency(h),(h%16==0,h//16 if h%16==0 else None))
            for d in range(4):
                self.assertEqual(M.transfer_depth_frequency(h,d),(h%(16**d)==0,h//(16**d) if h%(16**d)==0 else None))

    def test_periodic_wrong_orbit(self):
        self.assertEqual((16*Q(1,5))%1,Q(1,5))
        self.assertEqual(M.source_odd_predecessor(Q(1,5)),(3,Q(1,5)))
        for k in (0,1,2,3):
            self.assertEqual(M.coherent_fifth(k),16**k)


class FlowEnergyTests(unittest.TestCase):
    def test_exact_source_currents(self):
        for A in (12,32,96,192,384):
            phases=M.empirical_source_epoch(A)
            self.assertEqual(len(phases),A)
            self.assertTrue(all(x.denominator%2==1 for x in phases))
            self.assertEqual(M.collision_energy(phases,0),1)
            for k in range(3):
                a=M.branching_dissipation(phases,k)
                b=M.explicit_branch_dissipation(phases,k)
                self.assertEqual(a,b)
                self.assertGreaterEqual(a,0)
            self.assertEqual(M.exact_dissipation_sum(phases,3),M.collision_energy(phases,3)-1)

    def test_uniform_synthetic_control(self):
        phases=tuple(Q(2*j+1,2*16**2) for j in range(16**2))
        for k in (0,1,2):
            self.assertEqual(M.collision_energy(phases,k),1)
        self.assertEqual(M.collision_energy(phases,3),16)

    def test_electrical_resistance_limit(self):
        for k in (0,1,2,8,32):
            self.assertEqual(M.homogeneous_tree_unit_resistance(k),Q(1,15)*(1-Q(1,16**k)))

    def test_invalid(self):
        with self.assertRaises(ValueError):M.source_odd_predecessor(Q(1,2))
        with self.assertRaises(ValueError):M.empirical_source_epoch(0)
        with self.assertRaises(ValueError):M.collision_energy((Q(0),),-1)
        with self.assertRaises(ValueError):M.authentic_r(0)
        with self.assertRaises(ValueError):M.source_odd_predecessor(Q(1,4),Q(1,7))

if __name__=='__main__':unittest.main()
