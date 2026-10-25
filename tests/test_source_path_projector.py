"""Exact source-projector checks and selected/ensemble negative controls."""

from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.source_path_projector import (
    bbp_circle_carrier, bbp_prefix_inclusion, cartesian_interference,
    character_delta_certificate, character_sum, circle_encoding,
    circle_inclusion_transport, cyclic_path, cyclotomic_polynomial,
    dual_observable_transport, enumerate_projector, interference_projector,
    observable_transform, path_defects, projector_weight,
    quotient_path_transport, rational_residue, selector_path_mass,
)


def literal_bbp(n):
    return (Q(4, 8*n-7)-Q(2, 8*n-4)
            -Q(1, 8*n-3)-Q(1, 8*n-2))


def scalar_coefficients(q, value):
    return (Q(value),)+(Q(),)*(len(cyclotomic_polynomial(q))-2)


class CharacterOrthogonality(unittest.TestCase):
    def test_known_cyclotomic_polynomials(self):
        expected = {2: (1, 1), 3: (1, 1, 1), 4: (1, 0, 1),
                    5: (1, 1, 1, 1, 1), 6: (1, -1, 1),
                    7: (1, 1, 1, 1, 1, 1, 1),
                    8: (1, 0, 0, 0, 1), 9: (1, 0, 0, 1, 0, 0, 1),
                    10: (1, -1, 1, -1, 1)}
        for q, polynomial in expected.items():
            self.assertEqual(cyclotomic_polynomial(q), polynomial)

    def test_root_sum_for_every_constraint_and_unit_calibration(self):
        for q in (3, 5, 7, 9, 11):
            for defect in range(q):
                for unit in (1, -1, q+1):
                    cert = character_delta_certificate(q, defect, unit)
                    self.assertEqual(cert["value"], int(defect == 0))
                    self.assertTrue(cert["phase_is_faithful"])
                    self.assertEqual(sum(cert["raw_normalized_coefficients"]), 1)

    def test_nonunit_phase_admits_a_false_constraint(self):
        true = character_delta_certificate(9, 3)
        mutated = character_delta_certificate(9, 3, 3)
        self.assertEqual(true["value"], 0)
        self.assertEqual(mutated["value"], 1)
        self.assertFalse(mutated["phase_is_faithful"])
        self.assertFalse(mutated["authentic_constraint"])

    def test_character_sum_signed_weights_and_empty_sum(self):
        self.assertEqual(character_sum(5, (0, 0), (Q(3, 2), Q(-1, 2))),
                         scalar_coefficients(5, 1))
        self.assertEqual(character_sum(7, ()), scalar_coefficients(7, 0))
        self.assertEqual(character_sum(9, tuple(range(9))),
                         scalar_coefficients(9, 0))


class SourcePathProjectors(unittest.TestCase):
    def test_all_candidate_paths_preregistered_moduli_and_horizons(self):
        total = 0
        for q in (3, 5, 7, 9):
            for horizon in range(1, 5):
                source = tuple(j*j+1 for j in range(1, horizon+1))
                receipt = enumerate_projector(q, 16, source, initial=1)
                self.assertEqual(receipt["direct_accepted_paths"], 1)
                self.assertEqual(receipt["interference_total_mass"], 1)
                self.assertEqual(receipt["factorization_mismatches"], 0)
                total += receipt["candidate_paths_enumerated"]
        self.assertEqual(total, 90_280)

    def test_direct_cartesian_duals_on_every_small_candidate_path(self):
        terms = 0
        for q, source in ((3, (1, 2)), (5, (3,))):
            for path in product(range(q), repeat=len(source)+1):
                full = cartesian_interference(q, 2, source, path, initial=1)
                expected = projector_weight(q, 2, source, path, initial=1)
                self.assertEqual(full["normalized_coefficients"],
                                 scalar_coefficients(q, expected))
                terms += full["cartesian_dual_terms_enumerated"]
        self.assertEqual(terms, 729+625)

    def test_missing_initial_selector_changes_mass_and_selected_history(self):
        q, source = 7, (2, 5, 1)
        free = enumerate_projector(q, 16, source, initial=None)
        self.assertEqual(free["direct_accepted_paths"], q)
        self.assertEqual(free["interference_total_mass"], q)
        selected = cyclic_path(q, 16, source, initial=0)
        self.assertEqual(projector_weight(q, 16, source, selected, initial=0), 1)
        self.assertEqual(projector_weight(q, 16, source, selected, initial=1), 0)
        self.assertNotEqual(selected, cyclic_path(q, 16, source, initial=1))

    def test_normalization_mutation_is_detected(self):
        q, source = 3, (2, 1)
        actual = cyclic_path(q, 5, source)
        cert = cartesian_interference(q, 5, source, actual)
        total = cert["reduced_unnormalized_coefficients"][0]
        self.assertEqual(total, q**3)
        self.assertEqual(total*cert["normalization"], 1)
        self.assertNotEqual(total/Q(q**2), 1)

    def test_wrong_source_and_wrong_phase_fail_authentic_selection(self):
        q, source = 9, (1, 2)
        actual = cyclic_path(q, 16, source)
        self.assertEqual(projector_weight(q, 16, (-1, 2), actual), 0)
        mutant = enumerate_projector(q, 16, source, phase_multiplier=3)
        self.assertEqual(mutant["direct_accepted_paths"], 1)
        self.assertEqual(mutant["interference_total_mass"], 27)
        self.assertEqual(mutant["factorization_mismatches"], 26)

    def test_projection_idempotence_self_adjointness_and_prefix_marginal(self):
        for q, base, source in ((3, 2, (1, 2)), (5, 5, (2, 1)),
                                (9, 16, (1, 4, 2))):
            for prefix in product(range(q), repeat=len(source)):
                expected = projector_weight(q, base, source[:-1], prefix, initial=2)
                marginal = sum((projector_weight(q, base, source, prefix+(last,),
                                                initial=2) for last in range(q)), Q())
                self.assertEqual(marginal, expected)
                self.assertEqual(expected*expected, expected)
                self.assertIsInstance(expected, Q)  # real: conjugation fixes it

    def test_constant_and_periodic_controls_remain_legal_selected_sources(self):
        constant = cyclic_path(7, 16, (0,)*8, initial=0)
        periodic = cyclic_path(7, 16, (0,)*8, initial=1)
        self.assertEqual(constant, (0,)*9)
        self.assertEqual(periodic[:7], (1, 2, 4, 1, 2, 4, 1))
        self.assertEqual(projector_weight(7, 16, (0,)*8, constant), 1)
        self.assertEqual(projector_weight(7, 16, (0,)*8, periodic, initial=1), 1)
        # A unique path does not imply even a finite uniform occupation law.
        self.assertEqual(set(constant), {0})
        self.assertEqual(set(periodic), {1, 2, 4})


class ObservableAndSelectorTransport(unittest.TestCase):
    def test_backward_dual_formula_against_every_selected_initial_path(self):
        for q, base, source in ((3, 2, (1, 2)), (7, 16, (2, 1, 5)),
                                (11, 5, (3, 7, 2, 4))):
            frequencies = tuple((-1)**j*(j+2) for j in range(len(source)+1))
            data = dual_observable_transport(q, base, source, frequencies)
            dual = data["dual_multipliers"]
            self.assertEqual((dual[-1]+frequencies[-1]) % q, 0)
            for j in range(len(source)):
                self.assertEqual((dual[j]-base*dual[j+1]+frequencies[j]) % q, 0)
            for initial in range(q):
                path = cyclic_path(q, base, source, initial)
                direct = sum(h*x for h, x in zip(frequencies, path)) % q
                transported = (data["source_offset"]+
                               initial*data["initial_frequency"]) % q
                self.assertEqual(direct, transported)

    def test_general_selector_transform_against_full_path_sum(self):
        q, base, source = 3, 2, (1, 2)
        frequencies = (2, -1, 1)
        selectors = ((Q(1), Q(), Q()), (Q(1, 3),)*3,
                     (Q(3, 2), Q(-1, 2), Q()))
        for selector in selectors:
            powers, weights = [], []
            for path in product(range(q), repeat=3):
                powers.append(sum(h*x for h, x in zip(frequencies, path)))
                weights.append(selector_path_mass(q, base, source, path, selector))
            self.assertEqual(sum(weights), 1)
            direct = character_sum(q, tuple(powers), tuple(weights))
            formula = observable_transform(q, base, source, frequencies, selector)
            self.assertEqual(formula, direct)

    def test_uniform_endpoint_cancellation_does_not_select_one_path(self):
        q, source, frequencies = 7, (1, 3, 2), (0, 0, 0, 1)
        uniform = (Q(1, q),)*q
        selected = (Q(1),)+(Q(),)*(q-1)
        mean = observable_transform(q, 16, source, frequencies, uniform)
        chosen = observable_transform(q, 16, source, frequencies, selected)
        self.assertEqual(mean, scalar_coefficients(q, 0))
        endpoint = cyclic_path(q, 16, source)[-1]
        self.assertEqual(chosen, character_sum(q, (endpoint,)))
        self.assertNotEqual(chosen, mean)

    def test_noninvertible_base_does_not_destroy_forward_uniqueness(self):
        q, source = 9, (1, 2)
        uniform = (Q(1, q),)*q
        self.assertEqual(len({cyclic_path(q, 3, source, s)[-1] for s in range(q)}), 1)
        selected = cyclic_path(q, 3, source)
        self.assertEqual(projector_weight(q, 3, source, selected), 1)
        transformed = observable_transform(q, 3, source, (0, 0, 1), uniform)
        self.assertEqual(transformed, character_sum(q, (selected[-1],)))


class CarrierCoherence(unittest.TestCase):
    def test_profinite_quotient_transport(self):
        for fine, coarse, base in ((9, 3, 16), (15, 5, 2), (55, 11, 5)):
            cert = quotient_path_transport(fine, coarse, base, (7, 2, 11), initial=4)
            self.assertEqual(cert["reduced_path"], cert["coarse_path"])
            for x in cert["fine_path"]:
                self.assertEqual(Q(cert["character_frequency_scale"]*x, fine) % 1,
                                 Q(x % coarse, coarse))

    def test_denominator_inclusion_is_not_modular_reduction(self):
        cert = circle_inclusion_transport(3, 15, 16, (1, 2), initial=1)
        self.assertEqual(cert["fine_path"][0], 5)
        self.assertEqual(cert["phases"][0], Q(1, 3))
        self.assertNotEqual(cert["fine_path"][0] % 3, cert["coarse_path"][0])
        self.assertEqual(tuple(Q(x, 15) for x in cert["fine_path"]), cert["phases"])

    def test_selector_pushforward_under_quotient(self):
        # Fine normalized weights push to a different, exactly computed coarse selector.
        fine, coarse, source = 9, 3, (2, 1)
        sigma = tuple(Q(j+1, 45) for j in range(9))
        coarse_sigma = tuple(sum(sigma[s] for s in range(r, 9, 3)) for r in range(3))
        fine_paths = [(cyclic_path(fine, 16, source, s), sigma[s]) for s in range(fine)]
        for coarse_path in product(range(coarse), repeat=3):
            actual = sum((weight for path, weight in fine_paths
                          if tuple(x % coarse for x in path) == coarse_path), Q())
            expected = selector_path_mass(coarse, 16, source, coarse_path, coarse_sigma)
            self.assertEqual(actual, expected)

    def test_rational_residue_and_circle_encoding_have_different_domains(self):
        self.assertEqual(circle_encoding(Q(1, 3), 15), 5)
        self.assertEqual(rational_residue(Q(1, 3), 5), 2)
        with self.assertRaises(ValueError):
            rational_residue(Q(47, 15), 3)
        with self.assertRaises(ValueError):
            rational_residue(Q(47, 15), 5)
        with self.assertRaises(ValueError):
            circle_encoding(Q(1, 3), 5)

    def test_authentic_bbp_cyclic_path_matches_independent_four_pole_source(self):
        for horizon in range(1, 9):
            cert = bbp_circle_carrier(horizon)
            phases = [Q()]
            for n in range(1, horizon+1):
                phases.append((16*phases[-1]+literal_bbp(n)) % 1)
            self.assertEqual(cert["phases"], tuple(phases))
            self.assertEqual(cert["projector_weight"], 1)
            self.assertTrue(cert["modulus"] % 2)
            self.assertFalse(cert["expanded_fourier_sum"])
            wrong = list(cert["path"])
            wrong[-1] = (wrong[-1]+1) % cert["modulus"]
            self.assertEqual(projector_weight(cert["modulus"], 16, cert["increments"], wrong), 0)

    def test_authentic_bbp_prefix_denominator_inclusions(self):
        for short, long in ((1, 2), (2, 5), (3, 8), (8, 8)):
            cert = bbp_prefix_inclusion(short, long)
            self.assertEqual(cert["included_prefix"], cert["fine_prefix"])
            self.assertEqual(tuple(Q(x, cert["fine_modulus"])
                                   for x in cert["fine_prefix"]), cert["phases"])

    def test_circle_projector_retains_but_does_not_infer_integer_carry_lift(self):
        cert = bbp_circle_carrier(4)
        self.assertEqual(cert["literal_carries"][0], 3)
        self.assertFalse(cert["circle_projector_alone_authenticates_integer_lift"])
        for n in range(1, 5):
            self.assertEqual(cert["unwrapped_states"][n],
                             cert["phases"][n]+cert["cumulative_carries"][n])
            self.assertEqual(cert["cumulative_carries"][n],
                             16*cert["cumulative_carries"][n-1]
                             +cert["literal_carries"][n-1])
        # Adding an integer to forcing is invisible in the circle projector.
        changed = list(cert["increments"])
        changed[0] += cert["modulus"]
        self.assertEqual(cyclic_path(cert["modulus"], 16, changed), cert["path"])
        self.assertEqual((literal_bbp(1)+1) % 1, literal_bbp(1) % 1)
        self.assertNotEqual((literal_bbp(1)+1)//1, cert["literal_carries"][0])


class StrictDomainsAndBudgets(unittest.TestCase):
    def test_integer_and_rational_guards_survive_cache_warming(self):
        character_delta_certificate(3, 0)
        cyclotomic_polynomial(3)
        for bad in (True, 3.0, "3", -1, 1):
            for function in (cyclotomic_polynomial,
                             lambda q: character_delta_certificate(q, 0),
                             lambda q: cyclic_path(q, 16, (1,))):
                with self.assertRaises(ValueError):
                    function(bad)
        for bad in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                character_delta_certificate(3, bad)
            with self.assertRaises(ValueError):
                circle_encoding(bad, 15)
            with self.assertRaises(ValueError):
                rational_residue(bad, 7)

    def test_malformed_paths_selectors_and_frequencies(self):
        calls = (
            lambda: cyclic_path(3, True, (1,)),
            lambda: cyclic_path(3, 2, (1.0,)),
            lambda: path_defects(3, 2, (1,), (0,)),
            lambda: path_defects(3, 2, (1,), (0, True)),
            lambda: selector_path_mass(3, 2, (1,), (0, 1), (1, 1, 1)),
            lambda: selector_path_mass(3, 2, (1,), (0, 1), (1.0, 0, 0)),
            lambda: dual_observable_transport(3, 2, (1,), (1,)),
            lambda: character_sum(3, (1,), (Q(1), Q())),
            lambda: quotient_path_transport(9, 5, 16, (1,)),
            lambda: circle_inclusion_transport(3, 5, 16, (1,)),
            lambda: bbp_circle_carrier(0),
            lambda: bbp_prefix_inclusion(3, 2),
        )
        for call in calls:
            with self.assertRaises(ValueError):
                call()

    def test_exponential_and_expanded_modulus_limits_fail_closed(self):
        with self.assertRaises(ValueError):
            enumerate_projector(9, 16, (1,)*5)
        with self.assertRaises(ValueError):
            cartesian_interference(9, 16, (1,)*5, (0,)*6)
        with self.assertRaises(ValueError):
            character_delta_certificate(65, 0)
        with self.assertRaises(ValueError):
            observable_transform(65, 16, (1,), (0, 1), (Q(1, 65),)*65)
        # The arithmetic projector itself has no artificial small-modulus restriction.
        self.assertEqual(projector_weight(1_000_003, 16, (1,), (0, 1)), 1)


if __name__ == "__main__":
    unittest.main()
