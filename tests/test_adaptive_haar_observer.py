"""Exact hidden-link laws, independent posterior oracles and policy mutations."""
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import exp, log

from observational_succ.adaptive_haar_observer import (
    BinaryProbe, ConnectionBelief, DEEP_PROBE, OUTCOMES, STATES,
    MAX_POLICY_ACTIONS, MAX_REPETITIONS, MAX_SERIES_TERMS,
    gibbs_probe_policy, hidden_link_haar_coefficient,
    hidden_link_information_interval, hidden_link_information_nats,
    observe, posterior_link_after_successes, structural_probe,
    structural_promotion_energy, target_detail_energy,
    target_information_nats, target_response_joint, two_stage_information_plan,
)
from observational_succ.aphex_haar_feedback import fit_sign_coupling
from observational_succ.contextual_heuristics import ModelProbe
from observational_succ.heuristic_evidence_martingales import lr_step
from observational_succ.recursive_observer import update_current


def decimal_fraction(value):
    return Decimal(value.numerator) / Decimal(value.denominator)


def decimal_information(p):
    """Independent high-precision logarithmic oracle, not the series implementation."""
    value = decimal_fraction(p)
    if p == 0:
        return Decimal(0)
    if p == 1:
        return Decimal(2).ln()
    return ((1 + value) * (1 + value).ln() +
            (1 - value) * (1 - value).ln()) / 2


class HiddenConnectionLawTests(unittest.TestCase):
    def test_joint_law_haar_and_squared_projection_energy(self):
        for p in (Q(0), Q(1, 7), Q(1, 2), Q(6, 7), Q(1)):
            belief = ConnectionBelief.independent_fair(p)
            joint = target_response_joint(belief, DEEP_PROBE)
            self.assertEqual(joint, tuple(tuple((1 + p * t * y) / 4
                                               for y in OUTCOMES) for t in OUTCOMES))
            product_mean = sum((joint[i][j] * t * y
                                for i, t in enumerate(OUTCOMES)
                                for j, y in enumerate(OUTCOMES)), Q(0))
            self.assertEqual(product_mean, p)
            self.assertEqual(hidden_link_haar_coefficient(belief), p)
            self.assertEqual(target_detail_energy(belief), p * p)
            for y in OUTCOMES:
                probability, posterior = observe(belief, DEEP_PROBE, y)
                self.assertEqual(probability, Q(1, 2))
                self.assertEqual(posterior.target_mean, p * y)

    def test_adapter_preserves_states_and_matches_inherited_observer(self):
        beliefs = (ConnectionBelief.independent_fair(Q(2, 5)),
                   ConnectionBelief((Q(1, 7), Q(2, 7), Q(3, 7), Q(1, 7))),
                   ConnectionBelief((0, 0, 0, 1)))
        probes = (DEEP_PROBE, structural_probe(Q(3, 4), Q(1, 4)),
                  BinaryProbe("constant", (1, 1, 1, 1)))
        for probe in probes:
            instrument = probe.as_joint_instrument(cost=3)
            self.assertEqual(instrument.cost, 3)
            for x in range(4):
                for xp in range(4):
                    if xp != x:
                        self.assertEqual(instrument.joint[x][xp], (0, 0))
            for belief in beliefs:
                for index, outcome in enumerate(OUTCOMES):
                    mass, post = observe(belief, probe, outcome)
                    expected_mass, expected = update_current(belief.weights, instrument, index)
                    self.assertEqual(mass, expected_mass)
                    self.assertEqual(None if post is None else post.weights, expected)

    def test_fresh_structural_evidence_raises_or_lowers_deep_value(self):
        p, a, b = Q(1, 3), Q(3, 4), Q(1, 4)
        belief = ConnectionBelief.independent_fair(p)
        previous = p
        for n in range(1, 9):
            _, belief = observe(belief, structural_probe(a, b), 1)
            expected = p * a ** n / (p * a ** n + (1 - p) * b ** n)
            self.assertEqual(belief.connection_probability, expected)
            self.assertEqual(posterior_link_after_successes(p, a, b, n), expected)
            self.assertEqual(belief.target_positive_probability, Q(1, 2))
            self.assertTrue(belief.is_independent_fair)
            self.assertGreater(expected, previous)
            self.assertGreater(hidden_link_information_nats(expected),
                               hidden_link_information_nats(previous))
            previous = expected
        _, adverse = observe(ConnectionBelief.independent_fair(p), structural_probe(a, b), -1)
        self.assertLess(adverse.connection_probability, p)
        self.assertLess(target_detail_energy(adverse), p * p)
        self.assertLess(posterior_link_after_successes(p, b, a, 2), p)

    def test_copied_report_is_not_a_fresh_likelihood_factor(self):
        prior = ConnectionBelief.independent_fair(Q(1, 2))
        probe = structural_probe(Q(3, 4), Q(1, 4))
        _, first = observe(prior, probe, 1)
        # Conditional on a recorded + report, its copy is + with probability 1.
        copy = BinaryProbe("copy-of-recorded-positive", (1, 1, 1, 1))
        mass, repeated = observe(first, copy, 1)
        self.assertEqual(mass, 1)
        self.assertEqual(repeated, first)
        self.assertEqual(target_detail_energy(first, copy), 0)
        self.assertEqual(target_information_nats(first, copy), 0.0)
        _, false_fresh = observe(first, probe, 1)
        self.assertEqual(false_fresh.connection_probability, Q(9, 10))
        self.assertNotEqual(false_fresh, repeated)

    def test_reset_to_independence_mutation_manufactures_information(self):
        prior = ConnectionBelief.independent_fair(1)
        _, learned = observe(prior, DEEP_PROBE, 1)
        self.assertEqual(learned.connection_probability, 1)
        self.assertEqual(learned.target_positive_probability, 1)
        self.assertEqual(target_information_nats(learned), 0.0)
        self.assertEqual(target_detail_energy(learned), 0)
        with self.assertRaisesRegex(ValueError, "independent fair"):
            hidden_link_haar_coefficient(learned)
        false_reset = ConnectionBelief.independent_fair(learned.connection_probability)
        self.assertAlmostEqual(target_information_nats(false_reset), log(2))
        self.assertEqual(target_detail_energy(false_reset), 1)

    def test_nontrivial_joint_posterior_is_retained_after_deep_report(self):
        prior = ConnectionBelief.independent_fair(Q(1, 2))
        _, posterior = observe(prior, DEEP_PROBE, 1)
        self.assertEqual(posterior.weights, (Q(1, 4), Q(1, 4), Q(0), Q(1, 2)))
        self.assertEqual(posterior.connection_probability, Q(1, 2))
        self.assertEqual(posterior.target_positive_probability, Q(3, 4))
        self.assertEqual(target_detail_energy(posterior), Q(1, 12))
        self.assertLess(target_information_nats(posterior), target_information_nats(prior))
        self.assertFalse(posterior.is_independent_fair)

    def test_sign_orientation_changes_coefficient_not_information(self):
        p = Q(3, 5)
        belief = ConnectionBelief.independent_fair(p)
        opposite = BinaryProbe("opposite-link", (Q(1, 2), Q(1, 2), 1, 0))
        joint = target_response_joint(belief, opposite)
        covariance = sum((joint[i][j] * t * y for i, t in enumerate(OUTCOMES)
                          for j, y in enumerate(OUTCOMES)), Q(0))
        self.assertEqual(covariance, -p)
        self.assertEqual(target_detail_energy(belief, opposite), p * p)
        self.assertAlmostEqual(target_information_nats(belief, opposite),
                               target_information_nats(belief))

    def test_aphex_batch_normalization_agrees_for_declared_balanced_table(self):
        theta = (-1, -1, -1, -1, 1, 1, 1, 1)
        reports = (-1, -1, -1, 1, -1, 1, 1, 1)
        fit = fit_sign_coupling(theta, reports)
        self.assertEqual(fit.coefficient, Q(1, 2))
        self.assertEqual(fit.residual_energy, Q(3, 8))
        self.assertEqual(fit.coefficient ** 2,
                         target_detail_energy(ConnectionBelief.independent_fair(Q(1, 2))))

    def test_zero_prior_support_and_impossible_records(self):
        prior = ConnectionBelief.independent_fair(0)
        _, posterior = observe(prior, structural_probe(Q(3, 4), Q(1, 4)), 1)
        self.assertEqual(posterior.connection_probability, 0)
        self.assertEqual(observe(prior, structural_probe(1, 0), 1), (0, None))
        with self.assertRaisesRegex(ValueError, "impossible"):
            posterior_link_after_successes(0, 1, 0, 1)
        self.assertEqual(posterior_link_after_successes(Q(1, 2), 0, 0, 0), Q(1, 2))


class PreparatoryProbeTests(unittest.TestCase):
    def test_exact_weighted_haar_promotion_matches_full_outcome_enumeration(self):
        for p in (Q(0), Q(1, 5), Q(1, 2), Q(4, 5), Q(1)):
            for a, b in ((Q(3, 4), Q(1, 4)), (Q(1), Q(0)),
                         (Q(2, 3), Q(2, 3)), (Q(0), Q(0)), (Q(1), Q(1))):
                belief = ConnectionBelief.independent_fair(p)
                probe = structural_probe(a, b)
                total_mean, total_square = Q(0), Q(0)
                for y in OUTCOMES:
                    mass, post = observe(belief, probe, y)
                    if mass:
                        total_mean += mass * post.connection_probability
                        total_square += mass * target_detail_energy(post)
                self.assertEqual(total_mean, p)
                self.assertEqual(total_square - p * p, structural_promotion_energy(p, a, b))
                self.assertEqual(target_information_nats(belief, probe), 0.0)

    def test_information_jensen_gap_exceeds_half_structural_detail_energy(self):
        for p in (Q(1, 4), Q(1, 2), Q(3, 4)):
            belief = ConnectionBelief.independent_fair(p)
            probe = structural_probe(Q(3, 4), Q(1, 4))
            expected = 0.0
            for y in OUTCOMES:
                mass, post = observe(belief, probe, y)
                expected += float(mass) * target_information_nats(post)
            increase = expected - target_information_nats(belief)
            self.assertGreater(increase,
                               float(structural_promotion_energy(p, Q(3, 4), Q(1, 4))) / 2)

    def test_temporal_martingale_energy_identity_under_adaptive_probes(self):
        p0 = Q(2, 5)
        frontier = [(Q(1), ConnectionBelief.independent_fair(p0), ())]
        increment_sum, final_square = Q(0), p0 * p0
        adverse_path_seen = False
        for _ in range(5):
            next_frontier = []
            expected_increment, expected_p, expected_square = Q(0), Q(0), Q(0)
            for path_mass, belief, history in frontier:
                a, b = (Q(3, 4), Q(1, 4)) if not history or history[-1] == 1 else (Q(2, 3), Q(1, 3))
                for y in OUTCOMES:
                    mass, post = observe(belief, structural_probe(a, b), y)
                    weight = path_mass * mass
                    change = post.connection_probability - belief.connection_probability
                    expected_increment += weight * change * change
                    expected_p += weight * post.connection_probability
                    expected_square += weight * post.connection_probability ** 2
                    adverse_path_seen |= change < 0
                    next_frontier.append((weight, post, history + (y,)))
            increment_sum += expected_increment
            self.assertEqual(expected_p, p0)
            self.assertEqual(expected_square - final_square, expected_increment)
            self.assertEqual(expected_square - p0 * p0, increment_sum)
            self.assertLessEqual(increment_sum, p0 * (1 - p0))
            final_square, frontier = expected_square, next_frontier
        self.assertTrue(adverse_path_seen)
        self.assertEqual(len(frontier), 32)
        self.assertGreater(increment_sum, 0)

    def test_rational_information_enclosures_against_independent_decimal_logs(self):
        with localcontext() as context:
            context.prec = 90
            for p in (Q(0), Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(9, 10), Q(1)):
                expected = decimal_information(p)
                low, high = hidden_link_information_interval(p, 12)
                self.assertLessEqual(decimal_fraction(low), expected)
                self.assertLessEqual(expected, decimal_fraction(high))
                self.assertAlmostEqual(hidden_link_information_nats(p), float(expected), places=14)
                self.assertLessEqual(decimal_fraction(p * p / 2), expected)
                self.assertLessEqual(expected, Decimal(2).ln() * decimal_fraction(p * p))

    def test_two_stage_advantage_has_exact_cost_certificates(self):
        deep_cost, coarse_cost = Q(3, 20), Q(1, 100)
        quarters = hidden_link_information_interval(Q(1, 4), 16)
        halves = hidden_link_information_interval(Q(1, 2), 16)
        three_quarters = hidden_link_information_interval(Q(3, 4), 16)
        self.assertLess(halves[1], deep_cost)
        self.assertLess(quarters[1], deep_cost)
        self.assertGreater(three_quarters[0], deep_cost)
        # Even the fixed plan that always buys the deep probe is beneficial.
        self.assertGreater((quarters[0] + three_quarters[0]) / 2 -
                           coarse_cost - deep_cost, 0)
        exact_lower_net = (three_quarters[0] - deep_cost) / 2 - coarse_cost
        exact_upper_net = (three_quarters[1] - deep_cost) / 2 - coarse_cost
        self.assertGreater(exact_lower_net, 0)
        plan = two_stage_information_plan(ConnectionBelief.independent_fair(Q(1, 2)),
                                         structural_probe(Q(3, 4), Q(1, 4)),
                                         preparatory_cost=coarse_cost, deep_cost=deep_cost)
        self.assertLess(plan.direct_deep_net, 0)
        self.assertLess(plan.immediate_preparatory_net, 0)
        self.assertEqual(plan.first_action, "preparatory")
        self.assertEqual(plan.deep_after_outcome, (False, True))
        self.assertLessEqual(float(exact_lower_net) - 1e-15, plan.preparatory_then_optional_deep_net)
        self.assertLessEqual(plan.preparatory_then_optional_deep_net, float(exact_upper_net) + 1e-15)

    def test_uninformative_preparation_cost_and_known_target_controls(self):
        no_link_news = structural_probe(Q(1, 2), Q(1, 2))
        plan = two_stage_information_plan(ConnectionBelief.independent_fair(Q(1, 2)),
                                         no_link_news, preparatory_cost=Q(1, 100), deep_cost=Q(3, 20))
        self.assertEqual(plan.first_action, "stop")
        known = ConnectionBelief((0, Q(1, 2), 0, Q(1, 2)))
        self.assertEqual(target_information_nats(known), 0)
        plan = two_stage_information_plan(known, structural_probe(1, 0),
                                         preparatory_cost=Q(1, 100), deep_cost=Q(1, 100))
        self.assertEqual(plan.first_action, "stop")
        self.assertEqual(plan.deep_after_outcome, (False, False))


class PolicyEvidenceTests(unittest.TestCase):
    def test_gibbs_odds_promote_deep_probe_with_fixed_competitor(self):
        reference, temperature = (Q(2, 5), Q(3, 5)), 0.3
        low, high = hidden_link_information_nats(Q(1, 4)), hidden_link_information_nats(Q(3, 4))
        first = gibbs_probe_policy(reference, (low, 0.12), temperature)
        second = gibbs_probe_policy(reference, (high, 0.12), temperature)
        self.assertGreater(second[0], first[0])
        self.assertAlmostEqual(first[0] / first[1], float(reference[0] / reference[1]) * exp((low - 0.12) / temperature))
        self.assertAlmostEqual((second[0] / second[1]) / (first[0] / first[1]), exp((high - low) / temperature))
        changed_competitor = gibbs_probe_policy(reference, (high, 10.0), temperature)
        self.assertLess(changed_competitor[0], first[0])

    def test_zero_action_support_and_stable_large_utility_gaps(self):
        self.assertEqual(gibbs_probe_policy((0, 1), (1e300, 0)), (0.0, 1.0))
        self.assertEqual(gibbs_probe_policy((Q(1, 2), Q(1, 2)), (1e308, -1e308), 1e-308), (1.0, 0.0))
        self.assertEqual(gibbs_probe_policy((Q(1, 3), Q(2, 3)), (1e300, 1e300)),
                         gibbs_probe_policy((Q(1, 3), Q(2, 3)), (0, 0)))

    def test_nonuniform_reference_prevents_monotone_concentration_claim(self):
        reference = (Q(99, 100), Q(1, 100))
        # beta=log(99) cancels the initial 99:1 odds, giving maximum entropy.
        balanced = gibbs_probe_policy(reference, (0, 1), 1 / log(99))
        self.assertAlmostEqual(balanced[0], 0.5)
        self.assertAlmostEqual(balanced[1], 0.5)
        self.assertLess(max(balanced), max(float(p) for p in reference))
        concentrated = gibbs_probe_policy(reference, (0, 1), 0.01)
        self.assertGreater(concentrated[1], 0.999)

    def test_predictable_randomized_action_cancels_but_private_selection_does_not(self):
        prior = ConnectionBelief.independent_fair(Q(1, 2))
        public_action = BinaryProbe("selected-action", (Q(3, 4),) * 4)
        _, same = observe(prior, public_action, 1)
        self.assertEqual(same, prior)
        private_action = BinaryProbe("hidden-state-dependent-action", (Q(1, 4), Q(1, 4), Q(3, 4), Q(3, 4)))
        _, selected = observe(prior, private_action, 1)
        self.assertEqual(selected.connection_probability, Q(3, 4))
        self.assertNotEqual(selected, prior)

    def test_exact_adaptive_randomized_path_likelihood_and_lr_martingale(self):
        instruments = (structural_probe(Q(3, 4), Q(1, 4)), structural_probe(Q(2, 3), Q(1, 2)))
        models = tuple(ModelProbe(str(i), "hidden-link", ("negative", "positive"),
                                  {"null": (1 - p.positive_likelihoods[0], p.positive_likelihoods[0]),
                                   "alternative": (1 - p.positive_likelihoods[2], p.positive_likelihoods[2])})
                       for i, p in enumerate(instruments))
        prior_p = Q(2, 5)
        leaves = []

        def walk(history, belief, null_mass, alternative_mass, ratio, mutation, depth):
            if depth == 4:
                expected = prior_p * alternative_mass / (prior_p * alternative_mass + (1 - prior_p) * null_mass)
                self.assertEqual(belief.connection_probability, expected)
                self.assertEqual(ratio, alternative_mass / null_mass)
                leaves.append((null_mass, alternative_mass, ratio, mutation))
                return
            first_probability = Q(1, 3) if not history else (Q(3, 4) if history[-1] == 1 else Q(1, 4))
            for i, action_probability in enumerate((first_probability, 1 - first_probability)):
                for j, outcome in enumerate(OUTCOMES):
                    p0, p1 = models[i].law("null")[j], models[i].law("alternative")[j]
                    _, post = observe(belief, instruments[i], outcome)
                    new_ratio = lr_step(ratio, models[i], models[i].outcomes[j], null="null", alternative="alternative")
                    walk(history + (outcome,), post, null_mass * action_probability * p0,
                         alternative_mass * action_probability * p1, new_ratio,
                         mutation * action_probability * p1 / p0, depth + 1)

        walk((), ConnectionBelief.independent_fair(prior_p), Q(1), Q(1), Q(1), Q(1), 0)
        self.assertEqual(len(leaves), 256)
        self.assertEqual(sum((row[0] for row in leaves), Q(0)), 1)
        self.assertEqual(sum((row[1] for row in leaves), Q(0)), 1)
        self.assertEqual(sum((row[0] * row[2] for row in leaves), Q(0)), 1)
        # Wrongly counting the policy probability as a new evidence factor fails.
        self.assertNotEqual(sum((row[0] * row[3] for row in leaves), Q(0)), 1)


class InputBoundaryTests(unittest.TestCase):
    def test_exact_probabilities_reject_float_bool_and_out_of_range(self):
        for value in (True, False, 0.5, float("nan"), -1, Q(3, 2), "1/2"):
            for function in (ConnectionBelief.independent_fair, hidden_link_information_nats,
                             hidden_link_information_interval, lambda p: structural_probe(p, Q(1, 2))):
                with self.subTest(value=value, function=function):
                    with self.assertRaises(ValueError):
                        function(value)

    def test_malformed_joint_weights_and_probe_laws_rejected(self):
        for weights in ([Q(1, 4)] * 4, (Q(1, 2),) * 3, (0, 0, 0, 0), (0.5, 0, 0, 0.5), (True, 0, 0, 0)):
            with self.assertRaises(ValueError):
                ConnectionBelief(weights)
        for name, likelihoods in (("", (0, 0, 1, 1)), (False, (0, 0, 1, 1)),
                                  ("x", [0, 0, 1, 1]), ("x", (0, 0, 1)), ("x", (0, 0, 1, 2))):
            with self.assertRaises(ValueError):
                BinaryProbe(name, likelihoods)

    def test_outcome_and_budget_types_are_guarded(self):
        belief = ConnectionBelief.independent_fair(Q(1, 2))
        for outcome in (True, False, 1.0, 0, 2, "positive"):
            with self.assertRaises(ValueError):
                observe(belief, DEEP_PROBE, outcome)
        for count in (True, 1.0, -1, MAX_REPETITIONS + 1):
            with self.assertRaises(ValueError):
                posterior_link_after_successes(Q(1, 2), Q(3, 4), Q(1, 4), count)
        for terms in (True, 1.0, 0, -1, MAX_SERIES_TERMS + 1):
            with self.assertRaises(ValueError):
                hidden_link_information_interval(Q(1, 2), terms)
        with self.assertRaises(ValueError):
            DEEP_PROBE.as_joint_instrument(cost=True)
        with self.assertRaises(ValueError):
            DEEP_PROBE.as_joint_instrument(cost=0)

    def test_policy_and_plan_reject_invalid_numeric_contracts(self):
        for temperature in (0, -1, True, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                gibbs_probe_policy((Q(1, 2), Q(1, 2)), (0, 1), temperature)
        for reference, utilities in (((0, 0), (1, 2)), ((0.5, 0.5), (1, 2)),
                                     ((Q(1, 2), Q(1, 2)), (True, 0)),
                                     ((Q(1, 2), Q(1, 2)), (float("nan"), 0)),
                                     ((1,), (float("inf"),)), ((1,), (10 ** 1000,)),
                                     ((1,), (0, 1)),
                                     ((Q(1, MAX_POLICY_ACTIONS + 1),) * (MAX_POLICY_ACTIONS + 1),
                                      (0,) * (MAX_POLICY_ACTIONS + 1))):
            with self.assertRaises(ValueError):
                gibbs_probe_policy(reference, utilities)
        for bad_cost in (-1, True, float("nan"), float("inf"), "free"):
            with self.assertRaises(ValueError):
                two_stage_information_plan(ConnectionBelief.independent_fair(Q(1, 2)),
                                           structural_probe(Q(3, 4), Q(1, 4)),
                                           preparatory_cost=bad_cost, deep_cost=Q(1, 10))


if __name__ == "__main__":
    unittest.main()
