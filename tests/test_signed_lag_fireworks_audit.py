"""Exact hostile audit of inherited lag-bound interpretation.

The coherent same-forcing seed is symbolic -pi/16.  Its source tail is
enclosed using an independently combined four-pole rational source, never
by passing a floating-point approximation to an exact seed API.
"""

from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest


_ROOT = Path(__file__).resolve().parents[1]
_PATH = _ROOT / "research/2026-10-31/selected_lag_tomography/selected_lag.py"
_SPEC = importlib.util.spec_from_file_location("_fireworks_audit_lag", _PATH)
_LAG = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_LAG)
_SEED_PATH = _ROOT / "research/2026-10-31/seed_superposition/seed_superposition.py"
_SEED_SPEC = importlib.util.spec_from_file_location("_fireworks_audit_seed", _SEED_PATH)
_SEED = importlib.util.module_from_spec(_SEED_SPEC)
_SEED_SPEC.loader.exec_module(_SEED)


def independent_source(n):
    """Single rational function, algebraically equal to the four signed poles."""
    return F(120*n*n - 89*n + 16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def tail_interval(n, terms):
    """T_n from positive BBP terms plus the independently bounded remainder.

    r(m) = integral_0^1 t^(8m-8) P(t) dt with
    0 < P(t) < 15(1-t).  Therefore T_m < 1/((8m+1)(8m+2)).
    T_n = sum_(j<=terms)16^-j r(n+j) + 16^-terms T_(n+terms).
    """
    low = sum((independent_source(n+j) / 16**j
               for j in range(1, terms+1)), F(0))
    end = n + terms
    return low, low + F(1, 16**terms*(8*end+1)*(8*end+2))


class CoherentSignedInterpretationAudit(unittest.TestCase):
    def test_independently_combined_source_retains_all_four_poles(self):
        for n in range(1, 50):
            self.assertEqual(independent_source(n), _LAG.r(n))

    def test_zero_clipped_modulus_bound_is_not_a_signed_bound(self):
        # N=2,k=1,h=4: D has just one term e(-60 T_1).
        # Quarter-turn containment already proves its real part is negative.
        a, b = tail_interval(1, 4)
        lo, hi = 60*a, 60*b
        self.assertLess(F(1, 4), lo)
        self.assertLess(hi, F(3, 4))
        # Also produce a rational outward upper for Re(D)/N.
        midpoint, radius = (lo+hi)/2, (hi-lo)/2
        _, cosine_upper = _LAG.cos_interval(midpoint)
        signed_normalized_upper = (cosine_upper + F(44, 7)*radius)/2
        self.assertLess(signed_normalized_upper, F(-49, 100))
        # Historical helper is preserved. Its clipped answer can describe
        # |D|/N, but cannot be used as a lower bound on Re(D)/N.
        helper = _LAG.coherent_lag_lower_bound(2, 1, 4)
        self.assertEqual(helper["normalized_lower"], 0)
        self.assertLess(signed_normalized_upper, helper["normalized_lower"])

    def test_source_string_cannot_authenticate_literal_zero_seed(self):
        selected = _SEED.seed_phase_boundary(F(0), 7, h=3)
        changed = _SEED.seed_phase_boundary(F(1, 7), 7, h=3)
        # Historical label is shared even though the literal point differs.
        self.assertEqual(selected["source"], changed["source"])
        self.assertIn("U0=0", changed["source"])
        self.assertEqual(selected["point_seed"], 0)
        self.assertNotEqual(changed["point_seed"], 0)
        self.assertEqual(changed["point_seed"], F(1, 7))
        self.assertFalse(changed["point_equals_measure"])


if __name__ == "__main__":
    unittest.main()
