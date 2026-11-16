"""Finite exact controls for detector laws; no stochastic or float verdicts."""
from fractions import Fraction as Q
from itertools import product
from math import comb
import unittest

from observational_succ.phase_detection import (
    MAX_CIRCLE, MAX_SHAPE, MAX_TRIALS,
    counterseed_escape_interval, detection_probability,
    detection_probability_bounds, forget_clock, gamma_inverse_squared,
    gamma_recovery_mse, gamma_rotation_response, minimum_detection_trials,
    phase_rotation_law, propensity_certificate, recover_retained_phase,
    retained_clock_error_bound,
)


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cscale(a, t):
    return a[0]*t, a[1]*t


def cdivide(a, b):
    norm = b[0]**2+b[1]**2
    return (a[0]*b[0]+a[1]*b[1])/norm, (a[1]*b[0]-a[0]*b[1])/norm


def cnorm(a):
    return a[0]**2+a[1]**2


def response_oracle(shape, rate, omega):
    """Binomial expansion; production uses repeated complex multiplication."""
    real, imag = Q(), Q()
    for k in range(shape+1):
        term = comb(shape, k)*rate**(shape-k)*omega**k
        if k % 2:
            imag += (-1)**((k-1)//2)*term
        else:
            real += (-1)**(k//2)*term
    scale = rate**shape/(rate*rate+omega*omega)**shape
    return real*scale, imag*scale


class GammaResponseTests(unittest.TestCase):
    def test_frozen_response_grid_independent_binomial_oracle(self):
        for shape, rate, omega in product((1, 2, 5, 12), (Q(1, 3), Q(1), Q(5, 2)),
                                          (Q(-3, 2), Q(), Q(1), Q(7))):
            with self.subTest(shape=shape, rate=rate, omega=omega):
                value = gamma_rotation_response(shape, rate, omega)
                self.assertEqual(value, response_oracle(shape, rate, omega))
                self.assertEqual(cnorm(value)*gamma_inverse_squared(shape, rate, omega), 1)

    def test_shape_addition_and_frequency_sign(self):
        for left, right, omega in product((1, 3, 7), (1, 2, 5), (Q(1, 3), Q(2))):
            a = gamma_rotation_response(left, 2, omega)
            b = gamma_rotation_response(right, 2, omega)
            self.assertEqual(cmul(a, b), gamma_rotation_response(left+right, 2, omega))
            negative = gamma_rotation_response(left, 2, -omega)
            self.assertEqual(negative, (a[0], -a[1]))

    def test_zero_intensity_is_no_smoothing_no_recovery_noise(self):
        for shape in (1, 12, MAX_SHAPE):
            self.assertEqual(gamma_rotation_response(shape, Q(2, 3), 0), (1, 0))
            self.assertEqual(gamma_inverse_squared(shape, Q(2, 3), 0), 1)
            self.assertEqual(gamma_recovery_mse(shape, Q(2, 3), 0, 17), 0)

    def test_locked_mean_damps_while_inverse_cost_grows(self):
        intensities = (0, 1, 3, 15)
        norms = [cnorm(gamma_rotation_response(2, 1, w)) for w in intensities]
        costs = [gamma_inverse_squared(2, 1, w) for w in intensities]
        self.assertTrue(all(a > b for a, b in zip(norms, norms[1:])))
        self.assertTrue(all(a < b for a, b in zip(costs, costs[1:])))
        self.assertEqual(costs[-1], 226**2)

    def test_exact_mse_by_complete_product_enumeration(self):
        quarter = ((Q(1), Q()), (Q(), Q(1)), (Q(-1), Q()), (Q(), Q(-1)))
        ensembles = (
            (1, ((quarter[0], Q(1, 2)), (quarter[1], Q(1, 2))), (Q(1, 2), Q(1, 2))),
            (2, ((quarter[1], Q(3, 4)), (quarter[3], Q(1, 4))), (Q(), Q(1, 2))),
        )
        for shape, noise, response in ensembles:
            for size in (1, 3, 5):
                source = [quarter[(3*j+1) % 4] for j in range(size)]
                target = cscale(tuple(map(sum, zip(*source))), Q(1, size))
                expectation, mse = (Q(), Q()), Q()
                for indices in product(range(2), repeat=size):
                    probability, total = Q(1), (Q(), Q())
                    for phase, index in zip(source, indices):
                        rotation, weight = noise[index]
                        probability *= weight
                        total = cadd(total, cmul(phase, rotation))
                    recovered = cdivide(cscale(total, Q(1, size)), response)
                    expectation = cadd(expectation, cscale(recovered, probability))
                    error = cadd(recovered, cscale(target, -1))
                    mse += probability*cnorm(error)
                self.assertEqual(expectation, target)
                self.assertEqual(mse, gamma_recovery_mse(shape, 1, 1, size))

    def test_reusing_one_clock_does_not_buy_independent_sample_variance(self):
        response = (Q(1, 2), Q(1, 2))
        mse = Q()
        for eta in ((Q(1), Q()), (Q(), Q(1))):
            recovered = cdivide(eta, response)  # all source phases are one
            mse += cnorm(cadd(recovered, (Q(-1), Q())))/2
        self.assertEqual(mse, 1)
        self.assertNotEqual(mse, gamma_recovery_mse(1, 1, 1, 5))

    def test_retained_clock_precision_cost_and_cap(self):
        self.assertEqual(retained_clock_error_bound(10, Q(1, 100)), Q(1, 10))
        self.assertEqual(retained_clock_error_bound(-1000, Q(1, 100)), 2)
        self.assertEqual(retained_clock_error_bound(0, 100), 0)
        self.assertEqual(retained_clock_error_bound(100, 0), 0)

    def test_gamma_domain_guards(self):
        for args in ((0, 1, 1), (MAX_SHAPE+1, 1, 1), (True, 1, 1),
                     (1, 0, 1), (1, -1, 1), (1, 1.0, 1), (1, 1, 1.0)):
            with self.assertRaises(ValueError):
                gamma_rotation_response(*args)
        with self.assertRaises(ValueError):
            gamma_recovery_mse(1, 1, 1, 0)
        with self.assertRaises(ValueError):
            retained_clock_error_bound(1, -1)


class RetainedClockTests(unittest.TestCase):
    def test_forgotten_uniform_clock_erases_distinct_source_laws(self):
        for size in (2, 3, 5, 8, 11):
            uniform = (Q(1, size),)*size
            locked = (Q(1),)+(Q(),)*(size-1)
            nonuniform = (Q(2, 3),)+(Q(1, 3*(size-1)),)*(size-1)
            joints = [phase_rotation_law(source, uniform) for source in (locked, uniform, nonuniform)]
            self.assertTrue(all(forget_clock(joint) == uniform for joint in joints))
            self.assertEqual(len(set(joints)), 3)

    def test_retained_clock_exactly_recovers_every_source_control(self):
        for size in (2, 3, 5, 8, 11):
            sources = ((Q(1),)+(Q(),)*(size-1), (Q(1, size),)*size,
                       (Q(2, 3),)+(Q(1, 3*(size-1)),)*(size-1))
            clocks = ((Q(1, size),)*size, (Q(),)*(size-1)+(Q(1),))
            for source, clock in product(sources, clocks):
                joint = phase_rotation_law(source, clock)
                self.assertEqual(recover_retained_phase(joint), source)

    def test_zero_clock_keeps_original_source(self):
        source = (Q(1, 2), Q(1, 3), Q(1, 6))
        self.assertEqual(forget_clock(phase_rotation_law(source, (1, 0, 0))), source)

    def test_clock_source_dependence_breaks_independent_response_not_decoding(self):
        # S uniform, C=-S, Y=0: the true source is uniform, output is locked.
        dependent_joint = ((Q(1, 3),)*3, (Q(),)*3, (Q(),)*3)
        self.assertEqual(forget_clock(dependent_joint), (1, 0, 0))
        self.assertEqual(recover_retained_phase(dependent_joint), (Q(1, 3),)*3)
        independent = phase_rotation_law((Q(1, 3),)*3, (Q(1, 3),)*3)
        self.assertNotEqual(dependent_joint, independent)

    def test_clock_domain_guards(self):
        for law in ((), (1, 1), (Q(3, 2), Q(-1, 2)), (1.0,), (1,)* (MAX_CIRCLE+1)):
            with self.assertRaises(ValueError):
                phase_rotation_law(law, law)
        with self.assertRaises(ValueError):
            phase_rotation_law((1,), (1, 0))
        for joint in (((1, 0),), ((1, 1), (0, 0)), ((1.0,),)):
            with self.assertRaises(ValueError):
                recover_retained_phase(joint)


class PropensityTests(unittest.TestCase):
    def test_uniform_policy_is_identity_on_mean(self):
        report = propensity_certificate((1, 0, -1, Q(1, 3)), (Q(1, 4),)*4)
        self.assertEqual(report.target_mean, Q(1, 12))
        self.assertEqual(report.selected_mean, report.target_mean)
        self.assertEqual(report.corrected_mean, report.target_mean)

    def test_favorable_policy_changes_naive_frequency_not_population(self):
        report = propensity_certificate((1, 0), (Q(99, 100), Q(1, 100)))
        self.assertEqual(report.selected_mean, Q(99, 100))
        self.assertEqual(report.target_mean, Q(1, 2))
        self.assertEqual(report.corrected_mean, Q(1, 2))
        self.assertEqual(report.corrected_variance, Q(1, 396))

    def test_one_success_in_eight_cannot_become_population_density(self):
        report = propensity_certificate((1,)+(0,)*7, (Q(9, 10),)+(Q(1, 70),)*7)
        self.assertEqual(report.selected_mean, Q(9, 10))
        self.assertEqual(report.corrected_mean, Q(1, 8))
        self.assertEqual(report.corrected_variance, Q(1, 576))

    def test_rare_important_region_has_quantitative_recovery_cost(self):
        report = propensity_certificate((0, 1), (Q(99, 100), Q(1, 100)))
        self.assertEqual(report.corrected_mean, Q(1, 2))
        self.assertEqual(report.corrected_second_moment, 25)
        self.assertEqual(report.corrected_variance, Q(99, 4))

    def test_predictable_policy_mixture_remains_unbiased(self):
        policies = ((Q(1, 2), Q(1, 2)), (Q(9, 10), Q(1, 10)))
        reports = [propensity_certificate((-1, 2), q) for q in policies]
        self.assertEqual(Q(2, 7)*reports[0].corrected_mean+Q(5, 7)*reports[1].corrected_mean, Q(1, 2))
        self.assertNotEqual(reports[0].selected_mean, reports[1].selected_mean)

    def test_propensity_support_and_exactness_guards(self):
        for values, policy in (((0, 1), (1, 0)), ((0, 1), (1,)), ((0, 1.0), (Q(1, 2),)*2)):
            with self.assertRaises(ValueError):
                propensity_certificate(values, policy)


class DetectionTests(unittest.TestCase):
    def test_frozen_bernoulli_grid(self):
        for probability, trials in product((Q(), Q(1, 17), Q(1, 2), Q(1)), (0, 1, 2, 7, 19)):
            failure = Q(1)
            for _ in range(trials):
                failure *= 1-probability
            self.assertEqual(detection_probability(2*probability, trials), 1-failure)

    def test_complete_event_tree_agrees_with_detection_probability(self):
        p, success = Q(1, 3), Q()
        for outcomes in product((0, 1), repeat=4):
            weight = Q(1)
            for outcome in outcomes:
                weight *= p if outcome else 1-p
            if any(outcomes):
                success += weight
        self.assertEqual(success, Q(65, 81))
        self.assertEqual(detection_probability(2*p, 4), success)

    def test_copying_one_result_is_not_fresh_repetition(self):
        p = Q(1, 3)
        copied_success = sum((p if outcome else 1-p for outcome in (0, 1) if any((outcome,)*4)), Q())
        self.assertEqual(copied_success, p)
        self.assertNotEqual(copied_success, detection_probability(2*p, 4))

    def test_probability_interval_and_budget_minimality(self):
        self.assertEqual(detection_probability_bounds(Q(1, 3), Q(2, 3), 2), (Q(11, 36), Q(5, 9)))
        for escape, tolerance in product((Q(1, 17), Q(1, 2), Q(3, 2)), (Q(1, 2), Q(1, 10))):
            trials = minimum_detection_trials(escape, tolerance, max_trials=256)
            self.assertIsNotNone(trials)
            self.assertGreaterEqual(detection_probability(escape, trials), 1-tolerance)
            self.assertLess(detection_probability(escape, trials-1), 1-tolerance)

    def test_exhausted_budget_reports_none_without_infinite_claim(self):
        self.assertIsNone(minimum_detection_trials(Q(1, 1000), Q(1, 100), max_trials=8))
        self.assertIsNone(minimum_detection_trials(0, Q(1, 2)))
        self.assertEqual(minimum_detection_trials(2, Q(1, 100)), 1)

    def test_detection_domain_and_normalization_mutations(self):
        self.assertEqual(detection_probability(1, 1), Q(1, 2))
        self.assertNotEqual(detection_probability(1, 1), 1)  # omitted escape/2
        for escape, count in ((-1, 1), (3, 1), (1, -1), (1, MAX_TRIALS+1), (1.0, 1), (1, True)):
            with self.assertRaises(ValueError):
                detection_probability(escape, count)
        with self.assertRaises(ValueError):
            detection_probability_bounds(1, 0, 1)
        for tolerance in (0, 1, Q(-1, 2)):
            with self.assertRaises(ValueError):
                minimum_detection_trials(1, tolerance)


class CounterseedTests(unittest.TestCase):
    def test_source_bounds_against_direct_four_pole_oracle(self):
        def r(n):
            return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        for shell, depth in product((1, 2, 5, 11), (1, 3, 7)):
            lower, upper = Q(), Q()
            for n in range(shell, 2*shell):
                partial = sum((r(n+j)/16**j for j in range(1, depth+1)), Q())
                tail_upper = partial+r(n+depth+1)/(15*16**depth)
                lower += 12*partial*partial
                upper += Q(968, 49)*tail_upper*tail_upper
            self.assertEqual(counterseed_escape_interval(shell, tail_depth=depth), (lower/shell, upper/shell))

    def test_counterseed_bounds_positive_nested_and_quartic_upper(self):
        for shell in (1, 2, 5, 11):
            bounds = [counterseed_escape_interval(shell, tail_depth=d) for d in (1, 3, 7)]
            for low, high in bounds:
                self.assertGreater(low, 0)
                self.assertLess(low, high)
                self.assertLess(high, Q(968, 49*4096*shell**4))
            self.assertTrue(all(a[0] < b[0] and a[1] > b[1] for a, b in zip(bounds, bounds[1:])))

    def test_finite_counterseed_detection_is_positive_but_not_uniform(self):
        bounds1 = detection_probability_bounds(*counterseed_escape_interval(1), 19)
        bounds11 = detection_probability_bounds(*counterseed_escape_interval(11), 19)
        self.assertGreater(bounds11[0], 0)
        self.assertLess(bounds11[1], bounds1[0])
        self.assertLess(bounds11[1], Q(1, 100000))

    def test_counterseed_domains(self):
        for shell, depth in ((0, 1), (129, 1), (True, 1), (1, 0), (1, 33), (1, 1.0)):
            with self.assertRaises(ValueError):
                counterseed_escape_interval(shell, tail_depth=depth)


if __name__ == "__main__":
    unittest.main()
