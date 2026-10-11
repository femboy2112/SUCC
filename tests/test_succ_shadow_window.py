"""Hostile, reproducible SUCC-shadow canonical gamma selection tests.

The analytical proof uses trigamma bounds, not a numerical scan.
All integer/Gamma and winding identities are non-RH control theorems.
"""
from fractions import Fraction as Q
import unittest

import mpmath as mp

from observational_succ.succ_shadow_window import (
    ShadowWindowCertificate, WindingHistory, WindowError,
    certified_window_penalty_lower_bound, seam_gauge_witness,
    same_cell_quadratic_gauge_curvature,
    WindowResourceExhausted, observed_window, periodic_quarter_probe,
    quadratic_weight_gluing_defect, sine_gauge_witness,
    symmetric_positive_multiplicative_winding_weight_is_trivial,
    unseen_within_prefix,
)
from observational_succ.gamma_succ_path import gamma_periodic_gauge


class SuccShadowSelectionTests(unittest.TestCase):

    def test_moving_window_falsifies_nonzero_periodic_gauge(self):
        # Choose conservative EXACT finite integer witness; verify it with
        # numerics only after the mathematical inequality is certified.
        with mp.workdps(80):
            for frequency in (1,2,3,5):
                for epsilon in (Q(1,100),Q(-1,100),Q(1,10000)):
                    w=sine_gauge_witness(epsilon,frequency,max_stage=1_000_000)
                    self.assertIsInstance(w,ShadowWindowCertificate)
                    self.assertTrue(w.total_curvature_strictly_negative)
                    self.assertEqual(w.periodic_curvature,-2*abs(epsilon))
                    self.assertLess(w.gamma_curvature_upper_bound,2*abs(epsilon))
                    self.assertEqual(w.half_width,Q(1,4*frequency))
                    self.assertEqual(w.fractional_center,
                                     Q(1,4*frequency) if epsilon>0 else Q(3,4*frequency))
                    obs=observed_window(w,dps=80)
                    self.assertTrue(obs["negative"],(frequency,epsilon,obs))
                    self.assertGreater(obs["gamma_window"],0)
                    cap=mp.mpf(w.gamma_curvature_upper_bound.numerator)/w.gamma_curvature_upper_bound.denominator
                    self.assertLess(obs["gamma_window"],cap)
                    self.assertLess(obs["total"],0)

    def test_exact_gamma_baseline_is_not_rejected(self):
        with mp.workdps(75):
            for epsilon in (Q(1,200),Q(-1,200)):
                w=sine_gauge_witness(epsilon,1)
                obs=observed_window(w,dps=75)
                self.assertGreater(obs["gamma_window"],0)
                self.assertGreater(obs["gamma_window"]+mp.mpf(0),0)
                self.assertLess(obs["gamma_window"],abs(obs["gauge_window"]))

    def test_sine_gauge_integer_data_are_indistinguishable(self):
        with mp.workdps(80):
            for eps in ("0.01","-0.01"):
                for n in (1,2,5,20):
                    self.assertEqual(gamma_periodic_gauge(n,eps,dps=80),mp.gamma(n))
                z=mp.mpf("1.25")
                self.assertGreater(abs(gamma_periodic_gauge(z,eps,dps=80)
                                       -mp.gamma(z)),mp.mpf("1e-9"))

    def test_naive_quarter_grid_misses_double_frequency(self):
        self.assertEqual(periodic_quarter_probe(Q(1,100),1),Q(-1,50))
        self.assertEqual(periodic_quarter_probe(Q(1,100),2),0)
        self.assertEqual(periodic_quarter_probe(Q(1,100),4),0)
        self.assertEqual(periodic_quarter_probe(Q(1,100),3),Q(1,50))
        # The adaptive frequency-two shadow window sees a negative mode.
        self.assertTrue(sine_gauge_witness(Q(1,100),2).total_curvature_strictly_negative)

    def test_finite_prefix_can_be_blind_to_weak_gauge(self):
        for stage in (2,10,40,100):
            for freq in (1,2,5):
                epsilon=Q(1,64*freq**2*(stage+1)**2)
                self.assertTrue(unseen_within_prefix(epsilon,stage,freq))
                self.assertFalse(unseen_within_prefix(Q(1),stage,freq))
                witness=sine_gauge_witness(epsilon,freq,max_stage=1_000_000)
                self.assertGreater(witness.successor_stage,stage)
                self.assertTrue(witness.total_curvature_strictly_negative)
        # Failure to open a finite window is a budget state, not falsity.
        with self.assertRaisesRegex(WindowResourceExhausted,"No CERTIFICATE"):
            sine_gauge_witness(Q(1,10**12),1,max_stage=100000)

    def test_cellwise_convexity_is_insufficient_but_cross_seam_detects(self):
        # Stronger hostile control: a periodic continuous gauge can be
        # convex on EVERY open SUCC cell, at every integer horizon,
        # yet fail global log convexity exactly at integer boundaries.
        for e in (Q(1,2),Q(1,100),Q(1,10000)):
            for halfwidth in (Q(1,8),Q(1,4),Q(3,8)):
                self.assertGreater(same_cell_quadratic_gauge_curvature(e,halfwidth),0)
            witness=seam_gauge_witness(e)
            self.assertEqual(witness.fractional_center,0)
            self.assertEqual(witness.half_width,Q(1,4))
            self.assertEqual(witness.periodic_curvature,-Q(3,8)*e)
            self.assertTrue(witness.total_curvature_strictly_negative)
            with mp.workdps(75):
                numerical=observed_window(witness,dps=75)
                self.assertTrue(numerical["negative"],(e,numerical))
            self.assertGreater(certified_window_penalty_lower_bound(
                witness,Q(1,128)),0)
        with self.assertRaises(WindowResourceExhausted):
            seam_gauge_witness(Q(1,10**9),max_stage=10000)
        with self.assertRaises(WindowError):
            same_cell_quadratic_gauge_curvature(Q(1),Q(1,2))

    def test_no_invented_canonical_weight_on_logarithm_winding(self):
        a=WindingHistory((1,))
        inv=a.inverse()
        full=a.compose(inv)
        self.assertEqual(a.exponentiated_endpoint,1)
        self.assertEqual(inv.exponentiated_endpoint,1)
        self.assertEqual(full.exponentiated_endpoint,1)
        self.assertEqual(a.winding,1)
        self.assertEqual(inv.winding,-1)
        self.assertEqual(full.winding,0)
        self.assertEqual(full.steps,(1,-1))
        self.assertNotEqual(full.steps,WindingHistory(()).steps)
        # Generic symmetric quadratic damping fails inverse gluing:
        # W(1)W(-1)!=W(0) for positive damping, exactly.
        self.assertEqual(quadratic_weight_gluing_defect(1,-1,Q(1,2)),1)
        self.assertEqual(quadratic_weight_gluing_defect(3,2,Q(1,2)),-6)
        self.assertEqual(quadratic_weight_gluing_defect(2,-3,Q(0)),0)
        self.assertTrue(symmetric_positive_multiplicative_winding_weight_is_trivial())

    def test_weighted_shadow_selection_has_strict_rational_lower_bound(self):
        for freq in (1,2,7):
            for eps in (Q(1,100),Q(-1,10000)):
                witness=sine_gauge_witness(eps,freq)
                for weight in (Q(1,2),Q(1,1000)):
                    lower=certified_window_penalty_lower_bound(witness,weight)
                    self.assertGreater(lower,0)
                    self.assertLessEqual(lower,weight)
                    with mp.workdps(70):
                        obs=observed_window(witness,dps=70)
                        z=-obs["total"]
                        exact_nonnegative_contribution=(
                            mp.mpf(weight.numerator)/weight.denominator
                            *min(mp.mpf(1),z*z)
                        )
                        lower_m=mp.mpf(lower.numerator)/lower.denominator
                        self.assertLess(lower_m,exact_nonnegative_contribution)
        with self.assertRaises(WindowError):
            certified_window_penalty_lower_bound(
                sine_gauge_witness(Q(1,100)),Q(0))

    def test_invalid_frequency_and_numeric_sources_are_rejected(self):
        with self.assertRaises(WindowError):
            sine_gauge_witness(Q(0))
        with self.assertRaises(WindowError):
            sine_gauge_witness(0.001)
        with self.assertRaises(WindowError):
            sine_gauge_witness(Q(1,100),0)
        with self.assertRaises(WindowError):
            sine_gauge_witness(Q(1,100),4097)
        with self.assertRaises(WindowError):
            periodic_quarter_probe(Q(1),1,center=Q(1,2))
        with self.assertRaises(WindowError):
            observed_window({"fake":True})
        with self.assertRaises(WindowError):
            quadratic_weight_gluing_defect(1,1,Q(-1))
        with self.assertRaises(WindowError):
            quadratic_weight_gluing_defect(1.0,1,Q(1))
        with self.assertRaises(WindowResourceExhausted):
            WindingHistory(tuple(1 for _ in range(4097)))
        with self.assertRaises(WindowError):
            WindingHistory((1,)).compose((2,))


if __name__ == "__main__":
    unittest.main()
