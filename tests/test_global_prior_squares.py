"""Finite regression for GF-07 square checkpoints, not a normality proof."""
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

_MODULE = (Path(__file__).resolve().parents[1] / "research" / "2026-11-02"
           / "global_prior_fejer" / "global_prior_fejer.py")
_SPEC = importlib.util.spec_from_file_location("succ_global_prior_square_probe", _MODULE)
f = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(f)


class GlobalPriorSquareTests(unittest.TestCase):
    def test_exact_rational_gamma_error_at_squares(self):
        # This is strict rational verification of the explicit comparison
        # constant, not certification of the observed trig values.
        for L in (2,3,4,8,16,32):
            N=L*L
            cap=f.finite_completion_error_bound(N,L,N)
            self.assertLess(cap, Fraction(11*(L+2),2520*L**5))

    def test_all_prefix_checkpoint_interpolation(self):
        for L in (3,4,5):
            B=(L+1)**2
            q=f.alpha_cutoff(B)
            c0=f.fourier_means(q,L*L,1)[1]
            for N in (L*L+1,L*L+L,(L+1)**2-1):
                c=f.fourier_means(q,N,1)[1]
                bound=(L*L/N)*abs(c0)+(N-L*L)/N
                self.assertLessEqual(abs(c),bound+1e-12)

    def test_coherent_original_source_wrong_seed_violates_gate(self):
        for L in (2,4,8):
            self.assertAlmostEqual(f.fejer_energy(Fraction(1,5),L*L,L),
                                   L+1,places=10)

    def test_selected_finite_square_probes_are_not_asymptotic(self):
        for L in (4,8,16):
            q=f.alpha_cutoff(L*L)
            E=f.fejer_energy(q,L*L,L)
            self.assertTrue(math.isfinite(E))
            self.assertGreaterEqual(E,1-1e-11)
            self.assertLess(E,2)


if __name__ == "__main__":
    unittest.main()
