"""Exact compiler controls; fixtures are not claimed to be BBP phase values."""
import itertools
import math
import unittest
from fractions import Fraction as Q

from observational_succ import interference_forms as F
from observational_succ.collective_spectral import Gaussian as G, HermitianForm


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def multiply(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def pair(z):
    return z.real, z.imag


def conjugate(z):
    return z[0], -z[1]


def norm(z):
    return z[0] ** 2 + z[1] ** 2


def direct_form(matrix, values):
    total = (Q(), Q())
    for i, row in enumerate(matrix):
        for j, entry in enumerate(row):
            total = add(total, multiply(multiply(conjugate(pair(values[i])), pair(entry)),
                                        pair(values[j])))
    assert total[1] == 0
    return total[0]


def phase_fixtures(size):
    result = []
    for j in range(size):
        t = Q((3 * j + 1) % 11, 11)
        result.append(G((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)))
    return tuple(result)


def fixture_matrix(size):
    rows = [[G()] * size for _ in range(size)]
    for i in range(size):
        rows[i][i] = G(Q((-1) ** i * (i + 1), 3))
        for j in range(i + 1, size):
            rows[i][j] = G(Q((i + 2) * (j + 3) % 7 - 3, 5),
                           Q((i + 1) * (j + 1) % 5 - 2, 7))
            rows[j][i] = G(rows[i][j].real, -rows[i][j].imag)
    return tuple(tuple(row) for row in rows)


def channels(size):
    return tuple(F.source_character(j + 1) for j in range(size))


def exact_power(z, exponent):
    value = (Q(1), Q())
    for _ in range(exponent):
        value = multiply(value, pair(z))
    return G(*value)


class SourceCharacterTests(unittest.TestCase):
    def test_literal_four_pole_replay_on_fresh_clocks(self):
        state = Q()
        states = [state]
        for n in range(1, 42):
            forcing = (Q(4, 8 * n - 7) - Q(2, 8 * n - 4)
                       - Q(1, 8 * n - 3) - Q(1, 8 * n - 2))
            state = 16 * state + forcing
            states.append(state)
        for n in range(19, 42):
            with self.subTest(clock=n):
                self.assertEqual(F.source_character(n, -3).exact_turns(), -3 * states[n])
                echo = F.SourceCharacter(((n - 1, -16), (n, 1)))
                expected = (Q(4, 8 * n - 7) - Q(2, 8 * n - 4)
                            - Q(1, 8 * n - 3) - Q(1, 8 * n - 2))
                self.assertEqual(echo.exact_turns(), expected)

    def test_source_words_merge_labels_and_reference_orientation(self):
        first = F.SourceCharacter(((23, 2), (19, -1)), Q(1, 4))
        second = F.SourceCharacter(((19, 3), (23, -2)), Q(1, 2))
        combined = first.multiply(second)
        self.assertEqual(combined.powers, ((19, 2),))
        self.assertEqual(combined.reference_turns, Q(3, 4))
        self.assertEqual((combined.exact_turns() - first.exact_turns()
                          - second.exact_turns()) % 1, 0)
        self.assertEqual(first.multiply(first.conjugate()), F.reference_character())
        self.assertEqual(first.power(-1), first.conjugate())
        self.assertEqual(first.power(0), F.reference_character())
        self.assertNotEqual(F.source_character(0), F.reference_character())
        self.assertEqual(F.source_character(0).exact_turns(), 0)
        # A large intermediate union must not charge cancelled source factors.
        positive = F.SourceCharacter(tuple((n, 1) for n in range(1, 18)))
        negative = F.SourceCharacter(tuple((n, -1) for n in range(2, 34)))
        self.assertEqual(positive.multiply(negative).powers,
                         ((1, 1),) + tuple((n, -1) for n in range(18, 34)))

    def test_gaussian_phase_conversion_refuses_generic_source_phase(self):
        self.assertEqual(F.reference_character(Q(1, 4)).quarter_turn_value(), G(0, 1))
        self.assertEqual(F.reference_character(Q(-1, 4)).quarter_turn_value(), G(0, -1))
        self.assertEqual(F.source_character(0).quarter_turn_value(), G(1))
        with self.assertRaises(ValueError):
            F.source_character(1).quarter_turn_value()
        with self.assertRaises(ValueError):
            F.reference_character(Q(1, 3)).quarter_turn_value()

    def test_tensor_products_have_joint_labels_and_cartesian_order(self):
        left = (F.source_character(19), F.source_character(23, -1))
        right = (F.reference_character(Q(1, 4)), F.source_character(41, 2))
        lifted = F.tensor_channels(left, right)
        self.assertEqual(lifted[0].powers, ((19, 1),))
        self.assertEqual(lifted[0].reference_turns, Q(1, 4))
        self.assertEqual(lifted[-1].powers, ((23, -1), (41, 2)))
        for channel, (a, b) in zip(lifted, itertools.product(left, right)):
            self.assertEqual((channel.exact_turns() - a.exact_turns() - b.exact_turns()) % 1, 0)


class SignedCompilerTests(unittest.TestCase):
    def test_indefinite_complex_forms_against_independent_arithmetic(self):
        for size in range(1, 9):
            with self.subTest(size=size):
                matrix = fixture_matrix(size)
                values = phase_fixtures(size)
                form = F.HermitianResponse(channels(size), matrix)
                program = form.compile()
                expected = direct_form(matrix, values)
                self.assertEqual(form.evaluate_fixture(values), expected)
                self.assertEqual(program.evaluate_fixture(values), expected)
                self.assertEqual(program.as_form().matrix, matrix)
                self.assertLessEqual(len(program.terms), 2 * size * size - size)
                expected_mass = sum(abs(matrix[i][i].real) for i in range(size)) + 4 * sum(
                    abs(matrix[i][j].real) + abs(matrix[i][j].imag)
                    for i in range(size) for j in range(i + 1, size))
                self.assertEqual(program.measurement_mass, expected_mass)
                self.assertTrue(all(0 <= p <= 1 for p in program.intensities_fixture(values)))

    def test_predeclared_holdout_dimensions(self):
        for size in (11, 13, 17):
            matrix = fixture_matrix(size)
            values = tuple(z if j % 3 else G(0) for j, z in enumerate(phase_fixtures(size)))
            program = F.HermitianResponse(channels(size), matrix).compile()
            self.assertEqual(program.evaluate_fixture(values), direct_form(matrix, values))

    def test_imaginary_cross_term_sign_mutation_is_detected(self):
        matrix = ((G(), G(0, 1)), (G(0, -1), G()))
        values = (G(1), G(0, 1))
        correct = F.HermitianResponse(channels(2), matrix)
        self.assertEqual(correct.compile().evaluate_fixture(values), -2)
        reversed_orientation = tuple(tuple(entry.conjugate() for entry in row) for row in matrix)
        self.assertEqual(F.HermitianResponse(channels(2), reversed_orientation)
                         .compile().evaluate_fixture(values), 2)
        self.assertEqual(HermitianForm(matrix).quadratic(values), 2)

    def test_signed_cancellation_is_not_positive_energy(self):
        form = F.HermitianResponse(channels(2), ((G(1), G()), (G(), G(-1))))
        program = form.compile()
        values = (G(1), G(0, 1))
        self.assertEqual(program.evaluate_fixture(values), 0)
        unsigned = sum(abs(term.weight) * intensity for term, intensity in
                       zip(program.terms, program.intensities_fixture(values)))
        self.assertEqual(unsigned, 2)
        self.assertEqual(program.measurement_mass, 2)

    def test_reference_recovers_both_linear_components(self):
        labels = channels(3)
        coefficients = (G(Q(2, 3), Q(-1, 5)), G(0, Q(3, 7)), G(Q(-4, 9)))
        values = phase_fixtures(3)
        reference = F.reference_character(Q(1, 4))
        real_form, imag_form = F.linear_response_forms(labels, coefficients, reference)
        raw = (Q(), Q())
        for a, z in zip(coefficients, values):
            raw = add(raw, multiply(pair(a), pair(z)))
        expected = multiply((Q(), Q(-1)), raw)
        actual_values = (G(0, 1),) + values
        self.assertEqual(real_form.channels[0], reference)
        self.assertEqual(real_form.compile().evaluate_fixture(actual_values), expected[0])
        self.assertEqual(imag_form.compile().evaluate_fixture(actual_values), expected[1])

    def test_general_row_gram_uses_conjugate_first(self):
        row = (G(Q(1, 3), Q(1, 6)), G(0, Q(-1, 4)))
        program = F.IntensityProgram(channels(2), (F.IntensityTerm(Q(-5, 7), row),))
        form = program.as_form()
        for i in range(2):
            for j in range(2):
                expected = multiply(conjugate(pair(row[i])), pair(row[j]))
                self.assertEqual(pair(form.matrix[i][j]), tuple(Q(-5, 7) * x for x in expected))
        self.assertEqual(form.compile().evaluate_fixture(phase_fixtures(2)),
                         program.evaluate_fixture(phase_fixtures(2)))

    def test_arbitrary_complex_quadratic_has_two_real_compilers(self):
        matrix = ((G(1, 2), G(Q(2, 3), Q(-4, 5))),
                  (G(Q(-1, 7), Q(3, 2)), G(-1, 1)))
        values = phase_fixtures(2)
        expected = (Q(), Q())
        for i in range(2):
            for j in range(2):
                expected = add(expected, multiply(multiply(conjugate(pair(values[i])),
                                                           pair(matrix[i][j])), pair(values[j])))
        forms = F.complex_quadratic_forms(channels(2), matrix)
        actual = tuple(form.compile().evaluate_fixture(values) for form in forms)
        self.assertEqual(actual, expected)

    def test_zero_program_has_no_sampling_oracle(self):
        program = F.HermitianResponse(channels(1), ((G(),),)).compile()
        self.assertEqual(program.terms, ())
        self.assertEqual(program.sampling_probabilities, ())
        self.assertEqual(program.evaluate_fixture((G(1),)), 0)
        self.assertEqual(program.independent_trial_budget(Q(1, 10), Q(1, 20)), 0)
        with self.assertRaises(ValueError):
            program.score(0, 1)


class ResponseAndResourceTests(unittest.TestCase):
    def test_weighted_pair_dispersion_equals_full_pair_enumeration(self):
        values = phase_fixtures(5)
        weights = (Q(1, 10), Q(1, 5), Q(), Q(3, 10), Q(2, 5))
        program = F.pair_dispersion_program(channels(5), weights)
        direct = Q()
        mean = (Q(), Q())
        for weight, value in zip(weights, values):
            mean = add(mean, tuple(weight * x for x in pair(value)))
        for i in range(5):
            for j in range(5):
                difference = (values[i].real - values[j].real, values[i].imag - values[j].imag)
                direct += weights[i] * weights[j] * norm(difference) / 2
        self.assertEqual(program.evaluate_fixture(values), direct)
        self.assertEqual(direct, 1 - norm(mean))
        self.assertEqual(program.measurement_mass, 2 * (1 - sum(w * w for w in weights)))

    def test_reference_escape_and_spread_are_different_obligations(self):
        labels = channels(4)
        escape = F.reference_escape_program(labels)
        spread = F.pair_dispersion_program(labels)
        for locked, expected in ((G(1), 0), (G(0, 1), 1), (G(-1), 2)):
            self.assertEqual(escape.evaluate_fixture((G(1),) + (locked,) * 4), expected)
            self.assertEqual(spread.evaluate_fixture((locked,) * 4), 0)
        self.assertEqual(escape.measurement_mass, 2)

    def test_global_rotation_is_invisible_without_a_reference(self):
        values = phase_fixtures(5)
        rotated = tuple(G(-value.imag, value.real) for value in values)
        spread = F.pair_dispersion_program(channels(5))
        energy = F.weighted_mean_energy_program(channels(5))
        reference = F.reference_escape_program(channels(5))
        self.assertEqual(spread.evaluate_fixture(values), spread.evaluate_fixture(rotated))
        self.assertEqual(energy.evaluate_fixture(values), energy.evaluate_fixture(rotated))
        self.assertNotEqual(reference.evaluate_fixture((G(1),) + values),
                            reference.evaluate_fixture((G(1),) + rotated))

    def test_copied_pair_indices_erase_real_dispersion(self):
        values = (G(1), G(-1))
        true_response = F.pair_dispersion_program(channels(2)).evaluate_fixture(values)
        copied_response = sum(norm((z.real - z.real, z.imag - z.imag)) for z in values) / 4
        self.assertEqual(true_response, 1)
        self.assertEqual(copied_response, 0)

    def test_purity_matches_independent_frequency_gram(self):
        values = phase_fixtures(4)
        weights = (Q(1, 10), Q(1, 5), Q(3, 10), Q(2, 5))
        width = 5
        gram = [[(Q(), Q()) for _ in range(width)] for _ in range(width)]
        for value, weight in zip(values, weights):
            vector = [pair(exact_power(value, h)) for h in range(width)]
            for i in range(width):
                for j in range(width):
                    entry = multiply(vector[i], conjugate(vector[j]))
                    gram[i][j] = add(gram[i][j], tuple(weight * x for x in entry))
        expected = sum(norm(entry) for row in gram for entry in row) - width
        lifted_values = tuple(exact_power(value, h) for h in range(1, width) for value in values)
        program = F.fourier_purity_program(channels(4), width, weights)
        self.assertEqual(program.evaluate_fixture(lifted_values), expected)
        self.assertEqual(program.measurement_mass, width * (width - 1))

    def test_finite_mode_success_does_not_pay_all_modes(self):
        values = (G(1), G(0, 1), G(-1), G(0, -1))
        for width, expected in ((4, 0), (5, 2)):
            program = F.fourier_purity_program(channels(4), width)
            lifted = tuple(exact_power(value, h) for h in range(1, width) for value in values)
            self.assertEqual(program.evaluate_fixture(lifted), expected)

    def test_third_interaction_survives_identical_lower_marginals(self):
        independent = tuple(itertools.product((-1, 1), repeat=3))
        locked = tuple(row for row in independent if math.prod(row) == 1)
        for degree in (1, 2):
            for subset in itertools.combinations(range(3), degree):
                self.assertEqual(sum(math.prod(row[j] for j in subset) for row in independent), 0)
                self.assertEqual(sum(math.prod(row[j] for j in subset) for row in locked), 0)
        label = F.tensor_channels((F.source_character(19),), (F.source_character(23),),
                                  (F.source_character(41),))[0]
        response, _ = F.linear_response_forms((label,), (1,))
        joint_independent = sum((response.evaluate_fixture((G(1), G(math.prod(row))))
                                 for row in independent), Q()) / len(independent)
        joint_locked = sum((response.evaluate_fixture((G(1), G(math.prod(row))))
                            for row in locked), Q()) / len(locked)
        self.assertEqual(joint_independent, 0)
        self.assertEqual(joint_locked, 1)

    def test_exact_signed_sampling_law_is_unbiased(self):
        form = F.HermitianResponse(channels(3), fixture_matrix(3))
        program = form.compile()
        values = phase_fixtures(3)
        probabilities = program.sampling_probabilities
        intensities = program.intensities_fixture(values)
        self.assertEqual(sum(probabilities), 1)
        expected = Q()
        for j, (selection, intensity) in enumerate(zip(probabilities, intensities)):
            expected += selection * (intensity * program.score(j, 1)
                                      + (1 - intensity) * program.score(j, 0))
            self.assertLessEqual(abs(program.score(j, 1)), program.measurement_mass)
        self.assertEqual(expected, direct_form(form.matrix, values))

    def test_independent_budget_against_exact_binomial_tail_and_copy_control(self):
        program = F.weighted_mean_energy_program(channels(2))
        self.assertEqual(program.intensities_fixture((G(1), G(0, 1))), (Q(1, 2),))
        error, delta = Q(1, 4), Q(1, 8)
        count = program.independent_trial_budget(error, delta)
        self.assertEqual(count, 128)
        tail = sum((Q(math.comb(count, k), 2 ** count) for k in range(count + 1)
                    if abs(Q(k, count) - Q(1, 2)) >= error), Q())
        self.assertLess(tail, delta)
        # Reusing one fair coin for every observation leaves failure probability 1.
        copied_failure = sum(Q(1, 2) for value in (0, 1)
                             if abs(Q(value) - Q(1, 2)) >= error)
        self.assertEqual(copied_failure, 1)

    def test_deterministic_noise_and_phase_error_budgets(self):
        program = F.HermitianResponse(channels(3), fixture_matrix(3)).compile()
        epsilon = Q(1, 1000)
        worst_bias = sum(term.weight * (epsilon if term.weight > 0 else -epsilon)
                         for term in program.terms)
        self.assertEqual(program.intensity_noise_bound(epsilon), worst_bias)
        escape = F.reference_escape_program(channels(1))
        self.assertEqual(escape.phase_error_pi_units((0, Q(1, 4))), 1)
        difference = abs(escape.evaluate_fixture((G(1), G(0, 1)))
                         - escape.evaluate_fixture((G(1), G(1))))
        self.assertEqual(difference, 1)
        self.assertLess(difference, 3 * escape.phase_error_pi_units((0, Q(1, 4))))


class InputBudgetTests(unittest.TestCase):
    def test_exact_types_and_source_domains_are_enforced(self):
        for bad in (True, 1.0, "1"):
            with self.subTest(value=bad):
                with self.assertRaises(ValueError):
                    F.source_character(bad)
                with self.assertRaises(ValueError):
                    F.source_character(1, bad)
                with self.assertRaises(ValueError):
                    F.reference_character(bad)
                with self.assertRaises(ValueError):
                    F.HermitianResponse(channels(1), ((bad,),))
        for clock in (-1, F.MAX_SOURCE_CLOCK + 1):
            with self.assertRaises(ValueError):
                F.source_character(clock)
        with self.assertRaises(ValueError):
            F.SourceCharacter(((1, F.MAX_HARMONIC), (1, 1)))
        with self.assertRaises(ValueError):
            F.SourceCharacter(tuple((j, 1) for j in range(F.MAX_SOURCE_FACTORS + 1)))

    def test_matrix_and_normalization_guards(self):
        bad_matrices = (((G(0, 1),),), ((G(), G(1)), (G(), G())), ((G(),), (G(),)))
        for matrix in bad_matrices:
            with self.assertRaises(ValueError):
                F.HermitianResponse(channels(len(matrix)), matrix)
        for row in ((1, 1), (G(Q(3, 5), Q(4, 5)), 0)):
            with self.assertRaises(ValueError):
                F.IntensityTerm(1, row)
        with self.assertRaises(ValueError):
            F.IntensityTerm(0, (1,))
        with self.assertRaises(ValueError):
            F.IntensityTerm(1, (0,))
        with self.assertRaises(ValueError):
            F.weighted_mean_energy_program(channels(2), (Q(-1), Q(2)))
        with self.assertRaises(ValueError):
            F.weighted_mean_energy_program(channels(2), (Q(1, 3), Q(1, 3)))
        with self.assertRaises(ValueError):
            F.weighted_mean_energy_program(channels(1)).evaluate_fixture((G(2),))

    def test_finite_size_and_trial_domains_are_enforced(self):
        with self.assertRaises(ValueError):
            F.tensor_channels(channels(8), channels(8))
        with self.assertRaises(ValueError):
            F.tensor_channels(*((F.reference_character(),),) * (F.MAX_TENSOR_FACTORS + 1))
        with self.assertRaises(ValueError):
            F.fourier_purity_program(channels(17), 3)
        with self.assertRaises(ValueError):
            F.reference_escape_program(channels(F.MAX_CHANNELS))
        with self.assertRaises(ValueError):
            F.HermitianResponse(("completed-Y",), ((1,),))
        term = F.IntensityTerm(1, (1,))
        with self.assertRaises(ValueError):
            F.IntensityProgram(channels(1), (term,) * (F.MAX_TERMS + 1))
        program = F.weighted_mean_energy_program(channels(1))
        for error, delta in ((0, Q(1, 2)), (Q(-1), Q(1, 2)), (1, 0), (1, 1),
                             (True, Q(1, 2)), (Q(1, 2), 0.1)):
            with self.assertRaises(ValueError):
                program.independent_trial_budget(error, delta)
        for outcome in (True, 0.5, -1, 2):
            with self.assertRaises(ValueError):
                program.score(0, outcome)


if __name__ == "__main__":
    unittest.main()
