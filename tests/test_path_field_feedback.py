"""Exact probes for declared path models and the selected-source factor firewall.

The graph Dirichlet equation and the Beta integral are checked independently of
their production formulas. None is evidence of stochastic feedback in BBP.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
import unittest

from observational_succ import path_field_feedback as pf
from observational_succ import bidirectional_source_histories as bh
from observational_succ.growing_dtn_history import ConductiveState
from observational_succ.lambda_source_duality import Cyclo16, original_history
from observational_succ.succ_internal_matrix_walk import PhasePoly, authentic_r


def beta_integral_integer_parameters(left, right, alpha, beta):
    """Independent polynomial integration, not the production rising products."""
    def integral(a, b):
        return sum((Q((-1) ** k * comb(b - 1, k), a + k) for k in range(b)), Q())
    return integral(alpha + left, beta + right) / integral(alpha, beta)


class ConditioningTests(unittest.TestCase):
    def test_terminal_conditioning_telescope_and_preserve_equal_endpoint_odds(self):
        layers, kernels, initial = pf.branch_timeline(3, "fixed")
        success = {state: Q(state == (2, 1)) for state in layers[-1]}
        messages = bh.dual_labelled_messages(layers, kernels, initial, success)
        conditioned = bh.conditioned_bidirectional_path_law(layers, kernels, initial, success)
        original = bh.source_path_law(layers, kernels, initial)
        self.assertEqual(messages["Z"], Q(3, 8))
        for path, weight in conditioned["forward_histories"].items():
            self.assertEqual((original[path], weight), (Q(1, 8), Q(1, 3)))
            transformed = Q(1)
            for time, (label, target) in enumerate(path[1:]):
                source = path[0] if time == 0 else path[time][1]
                transformed *= messages["doob"][time][source][(label, target)]
            self.assertEqual(transformed, weight)
        self.assertEqual(conditioned["forward_histories"], conditioned["backward_histories"])

    def test_native_conditioning_preserves_the_geometry_order_defect(self):
        layers, kernels, initial = pf.branch_timeline(3, "harmonic")
        success = {state: Q(state == (2, 1)) for state in layers[-1]}
        original = bh.source_path_law(layers, kernels, initial)
        selected = bh.conditioned_bidirectional_path_law(layers, kernels, initial, success)
        self.assertEqual(selected["Z"], Q(11, 40))
        words = {"".join(label for label, _ in path[1:]): weight
                 for path, weight in selected["forward_histories"].items()}
        self.assertEqual(words, {"LLR": Q(3, 11), "LRL": Q(4, 11), "RLL": Q(4, 11)})
        for path, probability in original.items():
            word = "".join(label for label, _ in path[1:])
            self.assertEqual(probability, pf.branch_path_probability(word, "harmonic"))

    def test_native_zero_event_rejected_and_timeline_stops_before_breakthrough(self):
        layers, kernels, initial = pf.branch_timeline(3, "harmonic")
        with self.assertRaises(bh.SourceHistoryError):
            bh.conditioned_bidirectional_path_law(layers, kernels, initial, {s: 0 for s in layers[-1]})
        with self.assertRaises(pf.PathFieldError):
            pf.branch_timeline(4, "harmonic")
        for horizon in (-1, True, 13):
            with self.assertRaises(pf.PathFieldError):
                pf.branch_timeline(horizon, "fixed")


class FeedbackModelsTests(unittest.TestCase):
    def test_three_different_predictions_after_one_realized_left_edge(self):
        predictions = {
            model: pf.branch_path_probability("LL", model) / pf.branch_path_probability("L", model)
            for model in ("fixed", "reinforced", "harmonic")
        }
        self.assertEqual(predictions, {"fixed": Q(1, 2), "reinforced": Q(2, 3), "harmonic": Q(3, 5)})
        self.assertEqual(pf.TwoArmField(3, 1, 0).currents, (Q(1, 2), Q(1, 3)))

    def test_field_profiles_solve_the_declared_dirichlet_problem(self):
        for length in (2, 3, 5, 8):
            for left, right in product(range(length), repeat=2):
                field = pf.TwoArmField(length, left, right)
                for arm, realized, current in zip("LR", (left, right), field.currents):
                    profile = field.potential_profile(arm)
                    self.assertEqual(profile[:realized + 1], (Q(0),) * (realized + 1))
                    self.assertEqual(profile[-1], 1)
                    for node in range(realized + 1, length):
                        self.assertEqual(2 * profile[node], profile[node - 1] + profile[node + 1])
                    for node in range(realized, length):
                        self.assertEqual(profile[node + 1] - profile[node], current)
                self.assertEqual(field.next_left * sum(field.currents), field.currents[0])

    def test_native_conductive_state_independently_recomputes_the_field(self):
        for length, left, right in ((3, 0, 0), (3, 1, 0), (3, 2, 1), (5, 1, 3)):
            vertices = ("s",) + tuple(f"{arm}{j}" for arm in "LR" for j in range(1, length + 1))
            edges = tuple(("s" if j == 1 else f"{arm}{j-1}", f"{arm}{j}", Q(1))
                          for arm in "LR" for j in range(1, length + 1))
            grounded = ("s",) + tuple(f"{arm}{j}" for arm, count in zip("LR", (left, right))
                                      for j in range(1, count + 1))
            boundary = grounded + (f"L{length}", f"R{length}")
            network = ConductiveState(vertices, boundary, edges)
            native = network.potential((Q(0),) * len(grounded) + (Q(1), Q(1)))
            field = pf.TwoArmField(length, left, right)
            for arm in "LR":
                self.assertEqual((native["s"],) + tuple(native[f"{arm}{j}"] for j in range(1, length + 1)),
                                 field.potential_profile(arm))

    def test_equal_final_geometry_retains_order_sensitive_path_weights(self):
        self.assertEqual(pf.branch_path_probability("LLR", "harmonic"), Q(3, 40))
        self.assertEqual(pf.branch_path_probability("LRL", "harmonic"), Q(1, 10))
        self.assertEqual(pf.branch_path_probability("RLL", "harmonic"), Q(1, 10))
        for word in ("LLR", "LRL", "RLL"):
            self.assertEqual(pf.branch_path_probability(word, "fixed"), Q(1, 8))
            self.assertEqual(pf.branch_path_probability(word, "reinforced"), Q(1, 12))
        # A terminal-count Doob reweighting cannot change this within-fiber ratio.
        self.assertEqual(pf.branch_path_probability("LLR", "harmonic") /
                         pf.branch_path_probability("LRL", "harmonic"), Q(3, 4))

    def test_general_local_order_defect_has_the_proved_rational_value(self):
        for length in (3, 5, 8):
            for left, right in product(range(length - 1), repeat=2):
                field = pf.TwoArmField(length, left, right)
                lr = field.next_left * (1 - pf.TwoArmField(length, left + 1, right).next_left)
                rl = (1 - field.next_left) * pf.TwoArmField(length, left, right + 1).next_left
                a, b = length - left, length - right
                self.assertEqual(lr - rl, Q(a - b, (a + b) * (a + b - 1)))
                self.assertEqual(lr / rl, Q(b * (a - 1), a * (b - 1)))

    def test_probability_mass_before_breakthrough_and_terminal_stop(self):
        for model in ("fixed", "reinforced", "harmonic"):
            for horizon in range(4):
                mass = sum((pf.branch_path_probability("".join(word), model)
                            for word in product("LR", repeat=horizon)), Q())
                self.assertEqual(mass, 1)
        with self.assertRaises(pf.PathFieldError):
            pf.branch_path_probability("LLLR", "harmonic")
        with self.assertRaises(pf.PathFieldError):
            pf.branch_path_probability("LX", "fixed")
        with self.assertRaises(pf.PathFieldError):
            pf.TwoArmField(3, -1, 0)

    def test_polya_and_static_beta_equal_for_every_checked_word(self):
        for alpha, beta in ((1, 1), (2, 3), (4, 1)):
            for horizon in range(7):
                for word_tuple in product("LR", repeat=horizon):
                    word = "".join(word_tuple)
                    independent = beta_integral_integer_parameters(
                        word.count("L"), word.count("R"), alpha, beta)
                    self.assertEqual(pf.static_beta_path_probability(word, alpha, beta), independent)
                    self.assertEqual(pf.branch_path_probability(
                        word, "reinforced", alpha=alpha, beta=beta), independent)

    def test_equivalence_for_noninteger_rational_prior_and_reset_intervention(self):
        for word in ("", "LLR", "RLRLL", "RRRLLLR"):
            self.assertEqual(pf.static_beta_path_probability(word, Q(1, 2), Q(3, 2)),
                             pf.branch_path_probability(word, "reinforced", alpha=Q(1, 2), beta=Q(3, 2)))
        # Different declared interventions: reset count weights while preserving
        # the observer's information about an unchanged latent theta.
        reset_reinforcement = pf.polya_next_left(0, 0)
        posterior_static_bias = pf.static_beta_path_probability("LL") / pf.static_beta_path_probability("L")
        self.assertEqual((reset_reinforcement, posterior_static_bias), (Q(1, 2), Q(2, 3)))

    def test_invalid_reinforcement_parameters_are_not_silently_probabilities(self):
        for alpha, beta in ((0, 1), (-1, 1), (0.5, 1), (True, 1)):
            with self.assertRaises(pf.PathFieldError):
                pf.static_beta_path_probability("L", alpha, beta)
            with self.assertRaises(pf.PathFieldError):
                pf.branch_path_probability("", "reinforced", alpha=alpha, beta=beta)


class DeterministicFactorTests(unittest.TestCase):
    def test_auxiliary_mixing_leaves_selected_factor_character_unit(self):
        for weights in ((Q(1, 2), Q(1, 2)), (Q(1, 7), Q(2, 7), Q(4, 7))):
            for value in (Q(0), Q(3, 7), Q(-5, 13), Q(11)):
                for frequency in (-17, 1, 8, 31):
                    certificate = pf.deterministic_factor_character(weights, (value,) * len(weights), value, frequency)
                    self.assertEqual(certificate.character, PhasePoly.monomial(frequency * value))
                    self.assertEqual(certificate.character_square, PhasePoly.one())
        # A field-only centered observable may mix to zero in this same row.
        self.assertEqual(Q(1, 2) * 1 + Q(1, 2) * -1, 0)

    def test_even_tiny_projection_leakage_is_rejected_but_null_states_are_allowed(self):
        weights = (Q(999999, 1000000), Q(1, 1000000))
        self.assertEqual(pf.projection_leakage(weights, (Q(2, 3), Q(1, 3)), Q(2, 3)), Q(1, 1000000))
        with self.assertRaises(pf.PathFieldError):
            pf.deterministic_factor_character(weights, (Q(2, 3), Q(1, 3)), Q(2, 3), 1)
        certificate = pf.deterministic_factor_character((1, 0), (Q(2, 3), Q(1, 3)), Q(2, 3), 1)
        self.assertEqual(certificate.character_square, PhasePoly.one())

    def test_approximate_factor_bound_is_sharp_and_requires_half_mass_for_zero(self):
        for epsilon in (Q(0), Q(1, 7), Q(1, 3), Q(1, 2)):
            bound = pf.factor_character_modulus_lower_bound((1 - epsilon, epsilon), (Q(0), Q(1, 2)), Q(0))
            character = Cyclo16.one() * (1 - epsilon) + Cyclo16.zeta(8) * epsilon
            self.assertEqual(character, Cyclo16.one() * bound)
            self.assertEqual(bound, 1 - 2 * epsilon)
        for epsilon in (Q(1, 2), Q(3, 4), Q(1)):
            weights = (1 - epsilon, Q(1, 2), epsilon - Q(1, 2))
            self.assertEqual(pf.projection_leakage(weights, (Q(0), Q(1, 2), Q(1)), Q(0)), epsilon)
            self.assertEqual(pf.factor_character_modulus_lower_bound(weights, (Q(0), Q(1, 2), Q(1)), Q(0)), 0)
            character = (Cyclo16.one() * weights[0] + Cyclo16.zeta(8) * weights[1] +
                         Cyclo16.one() * weights[2])
            self.assertEqual(character, Cyclo16.zero())

    def test_authentic_bbp_holdouts_use_the_full_native_source_authenticator(self):
        states = original_history(64)
        for index in (1, 2, 7, 16, 32, 64):
            for frequency in (1, 8, 17):
                expected = states[index - 1]
                certificate = pf.authenticated_bbp_factor_character(
                    states, index, (Q(2, 5), Q(3, 5)), (expected, expected), frequency)
                self.assertEqual(certificate.forcing, authentic_r(index))
                self.assertEqual(16 * certificate.current + certificate.forcing, expected)
                self.assertEqual(certificate.factor.character, PhasePoly.monomial(frequency * expected))
                self.assertEqual(certificate.factor.character_square, PhasePoly.one())

    def test_changed_seed_and_source_and_auxiliary_projection_are_all_rejected(self):
        original = original_history(8)
        changed_seed = tuple(value + Q(16 ** n, 7) for n, value in enumerate(original, 1))
        changed_source = original[:3] + (original[3] + Q(1, 101),) + original[4:]
        for states in (changed_seed, changed_source):
            with self.assertRaises(pf.PathFieldError):
                pf.authenticated_bbp_factor_character(states, 4, (1,), (states[3],), 1)
        with self.assertRaises(pf.PathFieldError):
            pf.authenticated_bbp_factor_character(original, 4, (Q(1, 2), Q(1, 2)),
                                                 (original[3], original[3] + Q(1, 16)), 1)

    def test_firewall_does_not_forbid_time_average_cancellation(self):
        # The deterministic flip has unit conditional characters and zero mean
        # over every even horizon. Auxiliary no-attenuation is not a time no-go.
        for horizon in (2, 4, 10, 32):
            self.assertEqual(sum((-1) ** n for n in range(horizon)), 0)
        for value in (Q(0), Q(1, 2)):
            expected = Q(1, 2) - value
            self.assertEqual(pf.deterministic_factor_character((1,), (expected,), expected, 1).character_square,
                             PhasePoly.one())

    def test_factor_dimensions_and_nonexact_weights_rejected(self):
        for weights, values in (((Q(1),), ()), ((0.5, 0.5), (Q(0), Q(0))),
                                ((Q(1, 3), Q(1, 3)), (Q(0), Q(0)))):
            with self.assertRaises(pf.PathFieldError):
                pf.deterministic_factor_character(weights, values, Q(0), 1)


if __name__ == "__main__":
    unittest.main()
