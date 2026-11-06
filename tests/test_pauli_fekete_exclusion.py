"""Focused classical anti-occupancy and authentic BBP-source exclusion tests.

All finite: this does NOT prove pi normality or a source Fekete limit.
"""
from fractions import Fraction as F
from pathlib import Path
from math import log, pi
import importlib.util
import unittest

path=Path(__file__).resolve().parents[1]/'research/2026-11-05/pauli_fekete/source_exclusion_probe.py'
spec=importlib.util.spec_from_file_location('source_exclusion_probe',path)
p=importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

class PauliFekete(unittest.TestCase):
    def test_01_independent_rational_four_pole_source(self):
        self.assertEqual(p.source(1),F(47,15))
        for n in (2,7,17,33,53):
            self.assertEqual(p.source(n),p.source_independent(n))

    def test_02_roots_saturate_fekete_at_three_fresh_sizes(self):
        for N in (9,17,33):
            xs=[F(j,N) for j in range(N)]
            self.assertAlmostEqual(p.energy(xs),log(N)/N,places=11)
            for m in (3,5):
                self.assertAlmostEqual(p.frame_purity(xs,m),1/m,places=11)

    def test_03_half_circle_has_exclusion_but_nonzero_fourier_mode(self):
        for N in (9,17,33):
            xs=[F(j,2*N) for j in range(N)]
            self.assertGreater(abs(p.mode(xs,1)),.63)
            self.assertGreater(p.frame_purity(xs,3),1/3+.15)
            self.assertLess(p.energy(xs),0)
            # All distinct; exact minimal circle distance is 1/(2N).
            self.assertEqual(min((xs[j]-xs[i])%1 for i in range(N) for j in range(i+1,N)),F(1,2*N))

    def test_04_wrong_seed_carries_same_forcing_but_fails_repulsion(self):
        for A in (9,17,33):
            xs=p.coherent_epoch(A)
            bound=(A-1)/A*(log(pi/32)-2*log(A))
            self.assertLess(p.energy(xs),bound)
            self.assertGreater(abs(p.mode(xs,1)),.9999)

    def test_05_actual_original_source_holds_finite_vandermonde_bound(self):
        for A in (9,17,33):
            xs=p.original_epoch(A)
            self.assertLessEqual(p.energy(xs),log(A)/A+1e-11)
            for M in (3,5,9):
                self.assertGreaterEqual(p.frame_purity(xs,M),1/M-1e-11)

    def test_06_regularized_log_kernel_bounds_fourier_characters(self):
        for N in (9,17,33):
            for xs in (p.original_epoch(N),p.coherent_epoch(N),[F(j,2*N) for j in range(N)]):
                kernel,rhs=p.positive_kernel(xs)
                self.assertLessEqual(kernel,rhs+1e-10)

    def test_07_ordered_collision_profile_half_circle(self):
        N=33
        xs=[F(j,2*N) for j in range(N)]
        for t in (F(1,8),F(1,4)):
            C=F(sum(1 for i in range(N) for j in range(N) if i!=j and
                    min((xs[i]-xs[j])%1,(xs[j]-xs[i])%1)<=t),N*N)
            self.assertGreater(C,2*t)

    def test_08_vandermonde_is_not_necessary_for_normality(self):
        # Repeating a single phase in an otherwise well-spread finite sequence
        # makes the whole Slater determinant zero; finite witness only.
        xs=[F(0),F(0)]+[F(j,17) for j in range(1,16)]
        self.assertEqual(xs[0],xs[1])
        # The source-aware test would refuse log-energy instead of claiming Haar.
        with self.assertRaises(AssertionError):
            p.energy(xs)

if __name__=='__main__':unittest.main()
