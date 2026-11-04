"""Hostile and independent-oracle tests for the mesoscopic source instrument.

Finite floating Fejer comparisons are diagnostics only. Mathematical statements
are proved in PROOFS.md. Zero seed and all four original poles are preserved.
"""
import importlib.util
import math
import random
import unittest
from fractions import Fraction
from pathlib import Path

PATH = (Path(__file__).resolve().parents[1]/'research'/'2026-11-02'
        /'mesoscopic_spectral_army'/'mesoscopic.py')
SPEC = importlib.util.spec_from_file_location('mesoscopic',PATH)
f = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(f)


def independent_fraction_orbit(N):
    z = Fraction(0)
    yield z
    for n in range(1,N+1):
        r = (Fraction(4,8*n-7)-Fraction(2,8*n-4)
             -Fraction(1,8*n-3)-Fraction(1,8*n-2))
        z = 16*z+r
        yield z


class ExactSourceLift(unittest.TestCase):
    def test_modular_vs_independent_fraction(self):
        oracle = list(independent_fraction_orbit(130))
        for n,a,D in f.original_modular_lift(130):
            self.assertEqual(Fraction(a,D), oracle[n] % 1)

    def test_online_and_global_modulus_reconstruct_same_circle(self):
        oracle=f.original_modular_lift(700)
        independent=f.online_modular_lift(700)
        for a,b in zip(oracle,independent):
            self.assertEqual(a[0],b[0])
            self.assertEqual(a[1]*b[2],b[1]*a[2])

    def test_near_pair_fast_vs_quadratic_oracle(self):
        rng=random.Random(162026)
        for mesh in (2,3,4,8,16):
            for modulus in (16,37,120):
                for N in (1,2,3,10,31):
                    residues=[rng.randrange(modulus) for _ in range(N)]
                    expected=sum(mesh*min(abs(a-b),modulus-abs(a-b))<=modulus
                                 for a in residues for b in residues)
                    self.assertEqual(f.exact_near_pair_count(residues,modulus,mesh), expected)
                    C=sum(v*v for v in f.bin_rationals([Fraction(z,modulus) for z in residues],mesh))
                    self.assertLessEqual(C,expected)
                    self.assertLessEqual(expected,3*C)

    def test_known_parent_selfscale_certificates(self):
        for A,target in {8:14,16:34,32:52,64:110,128:220,256:504}.items():
            c=f.source_epoch_counts(A,A)
            self.assertEqual(sum(c),A)
            self.assertEqual(sum(v*v for v in c), target)

    def test_mesoscopic_profiles_and_independent_bins(self):
        p=f.source_profiles(7,1,2,3)
        independent = list(independent_fraction_orbit(255))
        for A,(mesh,counts,E) in p.items():
            self.assertEqual(counts, f.bin_rationals(independent[A:2*A],mesh))
            self.assertEqual(E,f.normalized_collision(counts))
            self.assertGreaterEqual(E,1)

    def test_invalid(self):
        for call in (lambda:f.source_epoch_counts(3,2),
                     lambda:f.source_epoch_counts(8,1),
                     lambda:f.mesoscopic_mesh(2,0,1),
                     lambda:list(f.original_modular_lift(-1)),
                     lambda:f.bin_rationals([],1)):
            with self.assertRaises(ValueError):call()


class FourierBridge(unittest.TestCase):
    def test_two_sided_fejer_for_original_and_adversaries(self):
        rng=random.Random(62026)
        for mesh in (2,4,8,16,32):
            points_by_case = [
                [Fraction(1,5)]*mesh,  # period-one coherent nonnormal
                [Fraction(i,mesh) for i in range(mesh)],  # equal-spaced
                [Fraction(mesh*i+1,mesh*mesh) for i in range(mesh)],
                [Fraction(rng.randrange(4096),4096) for _ in range(mesh)],
                [Fraction(1,mesh)-Fraction(1,100000)]*mesh,
            ]
            for points in points_by_case:
                C=float(f.normalized_collision(f.bin_rationals(points,mesh)))
                Q=f.fejer_energy_float(points,mesh)
                self.assertGreaterEqual(Q+1e-9,2*C/math.pi**2)
                self.assertLessEqual(Q,(1.5+math.pi**2/6)*C+1e-9)

    def test_real_source_and_positive_small_tail_stability(self):
        for A in (8,16,32,64):
            seq=list(independent_fraction_orbit(2*A-1))[A:2*A]
            moved=[x+Fraction(1,64*n*n) for n,x in zip(range(A,2*A),seq)]
            q0=f.fejer_energy_float(seq,A)
            q1=f.fejer_energy_float(moved,A)
            self.assertLessEqual(abs(math.sqrt(max(0,q0-1))-math.sqrt(max(0,q1-1))),
                                 f.gamma_excess_sqrt_bound(A)+1e-9)

    def test_coherent_counterseed_fails_every_growing_mesh(self):
        for A in (16,64,256):
            for (p,q) in ((1,4),(1,2),(1,1)):
                mesh=f.mesoscopic_mesh(A.bit_length()-1,p,q)
                # Circle orbit of rational alpha=1/5 is exactly fixed under x -> 16x mod 1.
                # This is only a hostile orbit, not the selected BBP zero-seed trajectory.
                E=f.normalized_collision(f.bin_rationals([Fraction(1,5)]*A,mesh))
                self.assertEqual(E,mesh)


if __name__=='__main__':
    unittest.main()
