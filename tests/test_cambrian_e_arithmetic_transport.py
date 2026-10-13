"""Source tomography and hostile arithmetic controls; no RH assertions."""
import unittest
from fractions import Fraction as F
from math import isqrt
from random import Random

from observational_succ.cambrian_e_arithmetic_transport import (
    ArithmeticTransportError, bounded_denominator_unique,
    clock_distribution_countermodel, connected_from_four_queries,
    dirichlet_exp_prefix, interior_clock_pair, selfdual_offline_family,
)
from observational_succ.gamma_interferometer import GammaInterferometer
from observational_succ.observer_reflection import RationalInterval as I
from observational_succ.source_prime_certificates import (
    CertifiedPrimeSource, rational_log_integer, rational_inverse_sqrt,
)


def independent_ramp_oracle(snapshot, *, half_density=True, phases=None, error=F(0)):
    """Independent interval implementation for the finite declared ramp law.

    Mutants use the same source coefficients while changing normalization
    or phases. It deliberately does not import the production ramp helper.
    """
    phases = phases or {}
    events = []
    for n in range(2, snapshot.horizon + 1):
        if snapshot.connected[n]:
            phase = rational_log_integer(phases.get(n, n))
            weight = rational_log_integer(n) * (
                rational_inverse_sqrt(n) if half_density else I.exact(F(1, n)))
            events.append((snapshot.connected[n], phase, weight))

    def evaluate(t):
        ans = I.exact(0)
        for b, phase, weight in events:
            active = I(max(F(0), t - phase.upper), max(F(0), t - phase.lower))
            ans = ans + (weight * active).scale(-b)
        return ans + I(-error, error)
    return evaluate


class ArithmeticTomography(unittest.TestCase):
    def test_exact_formal_log_exp_inverse_on_unseen_signed_sources(self):
        rng = Random(13720261013)
        for horizon in (2, 3, 7, 16, 31):
            for _ in range(5):
                a = {1: F(1), **{n: F(rng.randrange(-3, 4), rng.randrange(1, 5))
                                for n in range(2, horizon + 1)}}
                snap = GammaInterferometer.from_prefix(a, horizon)
                rebuilt = dirichlet_exp_prefix(dict(enumerate(snap.connected)), horizon)
                self.assertEqual(rebuilt, snap.coefficients)

    def test_four_query_recovery_real_prime_powers_and_composites(self):
        source = CertifiedPrimeSource.genuine(81)
        independent = independent_ramp_oracle(source.snapshot)
        for n in (2, 3, 4, 6, 8, 9, 12, 16, 20):
            a = connected_from_four_queries(n, source.prime_psi)["coefficient_interval"]
            b = connected_from_four_queries(n, independent)["coefficient_interval"]
            truth = source.snapshot.connected[n]
            self.assertLessEqual(a.lower, truth)
            self.assertGreaterEqual(a.upper, truth)
            self.assertTrue(a.intersects(b))
            self.assertTrue(bounded_denominator_unique(a, 100))

    def test_fake_six_detected_after_actual_dirichlet_log_transport(self):
        a = {n: F(1) for n in range(1, 82)}
        a[6] = F(2)
        snap = GammaInterferometer.from_prefix(a, 81)
        oracle = independent_ramp_oracle(snap)
        r = connected_from_four_queries(6, oracle)["coefficient_interval"]
        self.assertLessEqual(r.lower, 1)
        self.assertGreaterEqual(r.upper, 1)
        self.assertGreater(r.lower, F(9, 10))
        self.assertEqual(dirichlet_exp_prefix(dict(enumerate(snap.connected)), 81)[6], 2)

    def test_nonunit_euler_coefficient_keeps_prime_support_but_fails_weights(self):
        def v2(n):
            v = 0
            while n % 2 == 0:
                n //= 2
                v += 1
            return v
        snap = GammaInterferometer.from_prefix({n: F(2) ** v2(n)
                                               for n in range(1, 82)}, 81)
        for n, truth in ((2, 2), (4, 2), (8, F(8, 3))):
            r = connected_from_four_queries(n, independent_ramp_oracle(snap))["coefficient_interval"]
            self.assertLessEqual(r.lower, truth)
            self.assertGreaterEqual(r.upper, truth)
            self.assertGreater(r.lower, 1)
        self.assertEqual(snap.diagnostic()["non_prime_power_connected_anomalies"], [])
        self.assertIn(2, snap.diagnostic()["prime_power_weight_anomalies"])

    def test_wrong_half_density_fails_declared_genuine_coefficients(self):
        snap = CertifiedPrimeSource.genuine(81).snapshot
        r = connected_from_four_queries(2, independent_ramp_oracle(snap, half_density=False))
        i = r["coefficient_interval"]
        self.assertLess(i.upper, F(3, 4))
        self.assertGreater(i.lower, F(7, 10))

    def test_wrong_log_phase_moves_impulse_to_another_event(self):
        snap = CertifiedPrimeSource.genuine(81).snapshot
        oracle = independent_ramp_oracle(snap, phases={2: 3})
        i = connected_from_four_queries(2, oracle)["coefficient_interval"]
        self.assertLess(i.upper, F(1, 100))
        self.assertGreater(i.lower, F(-1, 100))

    def test_sound_noisy_samples_recover_interval_but_do_not_force_uniqueness(self):
        snap = CertifiedPrimeSource.genuine(81).snapshot
        for error in (F(1, 1000000), F(1, 10)):
            i = connected_from_four_queries(6, independent_ramp_oracle(snap, error=error))["coefficient_interval"]
            self.assertLessEqual(i.lower, 0)
            self.assertGreaterEqual(i.upper, 0)
        i = connected_from_four_queries(6, independent_ramp_oracle(snap, error=F(1, 10)))["coefficient_interval"]
        self.assertFalse(bounded_denominator_unique(i, 100))

    def test_clock_interiors_are_certified_away_from_ramp_boundaries(self):
        for n in range(1, 41):
            u, v = interior_clock_pair(n)
            self.assertLess(rational_log_integer(n).upper, u)
            self.assertLess(u, v)
            self.assertLess(v, rational_log_integer(n + 1).lower)

    def test_exactness_and_finite_domain_guards(self):
        for n in (True, 1, 41, 2.0):
            with self.assertRaises(ArithmeticTransportError):
                connected_from_four_queries(n, lambda t: I.exact(0))
        with self.assertRaises(ArithmeticTransportError):
            connected_from_four_queries(2, lambda t: 0)
        with self.assertRaises(ArithmeticTransportError):
            dirichlet_exp_prefix({1: 0, 2: 1.0}, 2)


class CompletionObstructions(unittest.TestCase):
    def test_clock_coherence_without_bounded_padic_measure(self):
        for p in (2, 3, 5, 7):
            for level in (1, 2, 4, 8):
                r = clock_distribution_countermodel(p, level)
                self.assertEqual(r["refinement_sum"], r["coarse_cylinder"])
                self.assertEqual(r["total_mass"], 1)
                self.assertEqual(r["padic_operator_norm_lower_bound"], p ** level)
                self.assertFalse(r["uniformly_bounded_over_all_levels"])

    def test_new_offline_family_and_sharp_boundaries(self):
        r = selfdual_offline_family(3, F(4, 5))
        self.assertEqual(r["discriminant"], F(44, 25))
        self.assertEqual(r["pole_normalization"], (1, 1))
        self.assertTrue(r["zeros_inside_strip_and_off_line"])
        self.assertFalse(r["unknown_zeta_zero_positions_used"])
        for k, w in ((3, F(2, 3)), (3, F(10, 9)), (1, 1), (3, 0)):
            with self.assertRaises(ArithmeticTransportError):
                selfdual_offline_family(k, w)


if __name__ == "__main__":
    unittest.main()
