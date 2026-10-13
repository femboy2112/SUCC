"""Exact mutation controls and independent enumerators for swarm D25--D32."""
from fractions import Fraction as F
from itertools import product
import unittest

from observational_succ.swarm_dynamics import (
    DynamicsError, FiniteDynamics, FiniteStochasticDynamics, rational, tv,
    stochastic_phase_source, noisy_latent_source, tent_cylinder, tent_uncertainty,
    window_transport, les_fourier_counterexample, causal_past, boost, decode_delays,
)


class SourceFactorTests(unittest.TestCase):
    def test_exact_input_and_source_metadata_controls(self):
        for value in (True, 0.5, "1/2", None):
            with self.assertRaises(DynamicsError):
                rational(value)
        for metadata in (("", "q", 0), ("s", "", 0), ("s", "q", -1), ("s", "q", True)):
            with self.assertRaises(DynamicsError):
                FiniteDynamics(*metadata, (0,), (0,))

    def test_malformed_carriers_and_laws_rejected(self):
        for successor, reports in (((0,), ()), ((1,), (0,)), ((True,), (0,)), ((0, 0), (0,))):
            with self.assertRaises(DynamicsError):
                FiniteDynamics("s", "q", 0, successor, reports)
        for rows in (((F(1, 2),),), ((-1,),), ((1, 0),), ((0.5,),), ()):
            with self.assertRaises(DynamicsError):
                FiniteStochasticDynamics("s", "q", 0, rows, (0,))

    def test_exhaustive_factor_equals_koopman_indicator_invariance(self):
        checked = 0
        for n in range(1, 5):
            for successor in product(range(n), repeat=n):
                for reports in product((0, 1), repeat=n):
                    system = FiniteDynamics("exhaustive", "binary", 0, successor, reports)
                    # Independent invariant-algebra test: each output indicator
                    # pulled back by F must be constant on each q fiber.
                    invariant = all(
                        (reports[successor[a]] == label) == (reports[successor[b]] == label)
                        for label in (0, 1) for a in range(n) for b in range(n)
                        if reports[a] == reports[b])
                    self.assertEqual(system.deterministic_factor()["valid"], invariant)
                    checked += 1
        self.assertEqual(checked, 4330)

    def test_smallest_nontrivial_nonfactor_receipt(self):
        # Two states cannot fail when q is nonconstant; three suffice.
        system = FiniteDynamics("hidden", "lossy", 0, (0, 2, 2), (0, 0, 1))
        receipt = system.deterministic_factor()
        self.assertFalse(receipt["valid"])
        self.assertEqual(receipt["witness_states"], (0, 1))
        self.assertEqual(receipt["distinct_next_reports"], (0, 1))

    def test_exact_special_phase_family_and_weight_mutation(self):
        for bias in (0, F(1, 5), F(1, 3), F(1, 2), F(7, 8), 1):
            source = stochastic_phase_source(bias)
            closure = source.closure()
            self.assertTrue(closure["strongly_lumpable"])
            self.assertEqual(closure["kernel"], ((0, 1), (1, 0)))
            self.assertEqual(closure["delta"], 0)
            for state in range(3):
                initial = tuple(int(i == state) for i in range(3))
                self.assertEqual(source.horizon_comparison(initial, 17)["tv"], 0)

    def test_source_transition_mutation_breaks_phase(self):
        mutant = FiniteStochasticDynamics("phase-mutant", "phase", 0,
                                         ((1, 0, 0), (0, 0, 1), (F(1, 2), F(1, 2), 0)),
                                         (0, 0, 1))
        closure = mutant.closure()
        self.assertFalse(closure["strongly_lumpable"])
        self.assertEqual(closure["delta"], F(1, 2))

    def test_constant_null_observer_is_lawful_but_loses_source(self):
        system = FiniteDynamics("three-cycle", "null", 0, (1, 2, 0), (0, 0, 0))
        self.assertTrue(system.deterministic_factor()["valid"])
        self.assertFalse(system.delay_quotient()["injective"])


class StochasticClosureTests(unittest.TestCase):
    def test_hidden_measurement_noise_refutes_markov_closure(self):
        source = noisy_latent_source(F(1, 4))
        closure = source.closure()
        self.assertFalse(closure["strongly_lumpable"])
        self.assertEqual(closure["witness_states"], (0, 2))
        self.assertEqual(closure["delta"], F(1, 4))
        # p(error)=1/2 is a calibrated null: observation carries no latent bit.
        self.assertTrue(noisy_latent_source(F(1, 2)).closure()["strongly_lumpable"])

    def test_tv_triangle_and_candidate_basis_controls(self):
        self.assertEqual(tv((F(1, 4), F(3, 4)), (F(3, 4), F(1, 4))), F(1, 2))
        with self.assertRaises(DynamicsError):
            tv((1,), (0, 1))
        with self.assertRaises(DynamicsError):
            noisy_latent_source().closure(((1,),))
        with self.assertRaises(DynamicsError):
            noisy_latent_source().horizon_comparison((1, 0, 0, 0), True)

    def test_horizon_defect_bound_on_exhaustive_exact_family(self):
        choices = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (F(1, 3),)*3)
        checked = 0
        for rows in product(choices, repeat=3):
            for reports in product((0, 1), repeat=3):
                source = FiniteStochasticDynamics("holdout", "binary", 0, rows, reports)
                for state in range(3):
                    initial = tuple(int(i == state) for i in range(3))
                    for horizon in range(5):
                        receipt = source.horizon_comparison(initial, horizon)
                        self.assertLessEqual(receipt["tv"], receipt["bound"])
                        checked += 1
        self.assertEqual(checked, 7680)

    def test_independent_path_enumerator_checks_stronger_bound(self):
        source = noisy_latent_source()
        closure = source.closure()
        kernel = closure["kernel"]
        for horizon in range(1, 6):
            actual = {}
            # Direct source path expansion, no horizon-comparison helper.
            for path in product(range(4), repeat=horizon):
                state, weight, outputs = 0, F(1), (0,)
                for nxt in path:
                    weight *= source.rows[state][nxt]
                    state = nxt
                    outputs += (source.reports[state],)
                actual[outputs] = actual.get(outputs, F(0))+weight
            predicted = {}
            for path in product(range(2), repeat=horizon):
                state, weight = 0, F(1)
                for nxt in path:
                    weight *= kernel[state][nxt]
                    state = nxt
                predicted[(0,)+path] = weight
            keys = set(actual) | set(predicted)
            error = sum((abs(actual.get(k, F(0))-predicted.get(k, F(0))) for k in keys), F(0))/2
            self.assertLessEqual(error, min(1, horizon*closure["delta"]))


class FrontierAndPDETests(unittest.TestCase):
    def test_symbolic_resolution_square_and_missing_bit_mutation(self):
        for width in range(1, 5):
            for word in product((0, 1), repeat=width+2):
                self.assertEqual(window_transport(word, width+1, 1)[:-1],
                                 window_transport(word[:-1], width, 1))
            with self.assertRaises(DynamicsError):
                window_transport((0,)*width, width, 1)
        self.assertEqual(window_transport((1, 0, 1, 1, 0), 2, 3), (1, 0))

    def test_tent_uncertainty_independent_endpoint_breakpoint_oracle(self):
        def tent(x):
            return 2*x if x <= F(1, 2) else 2-2*x
        for depth in range(7):
            for word in product((0, 1), repeat=depth):
                low, high = tent_cylinder(word)
                for horizon in range(depth+3):
                    # Include all dyadic folding points, then evaluate source
                    # iterates directly instead of using suffix identities.
                    mesh = [low, high]+[F(i, 2**horizon) for i in range(2**horizon+1)
                                        if low <= F(i, 2**horizon) <= high]
                    images = []
                    for point in mesh:
                        for _ in range(horizon):
                            point = tent(point)
                        images.append(point)
                    receipt = tent_uncertainty(word, horizon)
                    self.assertEqual(receipt["final"], (min(images), max(images)))
                    self.assertEqual(receipt["final_diameter"], F(1, 2**max(depth-horizon, 0)))

    def test_les_negative_control_and_surviving_leray_force(self):
        for frequency in (2, 3, 7, 19, 101):
            receipt = les_fourier_counterexample(frequency)
            self.assertEqual(receipt["projected_velocity"], (0, 0))
            self.assertEqual(receipt["cos_x_stress"][0][0], 1)
            self.assertEqual(receipt["sin_x_leray_divergence"], (0, F(2*frequency-1, 2)))
            for mode, vector in zip(receipt["modes"], receipt["amplitudes"]):
                self.assertEqual(sum(a*b for a, b in zip(mode, vector)), 0)
                self.assertGreater(sum(k*k for k in mode), 1)
        with self.assertRaises(DynamicsError):
            les_fourier_counterexample(1)

    def test_les_tensor_by_independent_fourier_convolution(self):
        for n in range(2, 12):
            modes = {(n, 1): (F(1, 2), F(-n, 2)),
                     (-n, -1): (F(1, 2), F(-n, 2)),
                     (n-1, 1): (F(1, 2), F(1-n, 2)),
                     (1-n, -1): (F(1, 2), F(1-n, 2))}
            stress = {}
            for k, a in modes.items():
                for l, b in modes.items():
                    target = (k[0]+l[0], k[1]+l[1])
                    if sum(x*x for x in target) <= 1:
                        value = stress.setdefault(target, [[F(0), F(0)], [F(0), F(0)]])
                        for i in range(2):
                            for j in range(2):
                                value[i][j] += a[i]*b[j]
            receipt = les_fourier_counterexample(n)
            self.assertEqual(set(stress), {(0, 0), (1, 0), (-1, 0)})
            self.assertEqual(tuple(map(tuple, stress[(0, 0)])), receipt["constant_stress"])
            self.assertEqual(tuple(tuple(2*x for x in row) for row in stress[(1, 0)]),
                             receipt["cos_x_stress"])

    def test_finite_attractor_collapses_under_lawful_factor(self):
        source = FiniteDynamics("two-fixed-points", "quotient", 0, (0, 1), (0, 0))
        self.assertTrue(source.deterministic_factor()["valid"])
        # Two disconnected fixed components map to one; cycle/component counts
        # therefore cannot be invariants of general noninjective factor maps.
        self.assertEqual(len(set(source.successor)), 2)
        self.assertEqual(len(set(source.reports)), 1)


class CausalAndDelayTests(unittest.TestCase):
    def test_lorentz_causal_cut_covariance_exact_grid(self):
        checked = 0
        for parameter in (F(-2, 3), F(-1, 3), 0, F(1, 3), F(3, 5)):
            for event in product(range(-3, 4), repeat=2):
                for observer in ((0, 0), (2, 1), (3, -2)):
                    self.assertEqual(causal_past(event, observer),
                                     causal_past(boost(event, parameter), boost(observer, parameter)))
                    checked += 1
        self.assertEqual(checked, 735)

    def test_covariance_does_not_make_spacelike_event_accessible(self):
        event, observer = (0, 2), (1, 0)
        self.assertFalse(causal_past(event, observer))
        self.assertFalse(causal_past(boost(event, F(1, 3)), boost(observer, F(1, 3))))
        # Galilean change with v=3/5 takes a left-null displacement outside
        # the unmodified standard future cone.
        self.assertTrue(causal_past((-1, 1), (0, 0)))
        self.assertFalse(causal_past((-1, F(8, 5)), (0, 0)))

    def test_finite_delay_stabilization_exhaustive_complete_source_tables(self):
        checked = 0
        for n in range(1, 5):
            for successor in product(range(n), repeat=n):
                for reports in product((0, 1), repeat=n):
                    source = FiniteDynamics("complete", "binary", 0, successor, reports)
                    delays = source.delay_quotient()
                    self.assertTrue(delays["closed"])
                    for a in range(n):
                        for b in range(n):
                            self.assertEqual(source.delays(a, n-1) == source.delays(b, n-1),
                                             source.delays(a, n*n) == source.delays(b, n*n))
                    checked += 1
        self.assertEqual(checked, 4330)

    def test_delay_bound_sharp_and_hidden_alias_never_resolves(self):
        for n in range(2, 9):
            source = FiniteDynamics("chain", "endpoint", 0,
                tuple(min(i+1, n-1) for i in range(n)), (0,)*(n-1)+(1,))
            self.assertTrue(source.delay_quotient()["injective"])
            self.assertFalse(source.delay_quotient(n-2)["injective"])
        hidden = FiniteDynamics("invisible-tag", "constant", 0, (0, 1), (0, 0))
        self.assertEqual(hidden.delays(0, 100), hidden.delays(1, 100))

    def test_delay_noise_margin_and_ambiguous_boundary(self):
        source = FiniteDynamics("3-cycle", "pulse", 0, (1, 2, 0), (0, 0, 1))
        words = source.delay_quotient(9)["words"]
        self.assertEqual(decode_delays(words, words[0], 2)["minimum_distance"], 6)
        mutant = list(words[0])
        mutant[0], mutant[1] = 1, 1
        self.assertEqual(decode_delays(words, mutant, 2)["candidates"], (0,))
        midpoint = list(words[0])
        disagreements = [i for i, (a, b) in enumerate(zip(words[0], words[1])) if a != b]
        for i in disagreements[:3]:
            midpoint[i] = words[1][i]
        receipt = decode_delays(words, midpoint, 3)
        self.assertFalse(receipt["uniform_error_correction_certified"])
        self.assertFalse(receipt["unique"])


if __name__ == "__main__":
    unittest.main()
