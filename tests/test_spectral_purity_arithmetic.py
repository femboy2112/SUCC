"""Exact cyclotomic replay and held-out BBP source-layer controls."""
from fractions import Fraction as Q
from math import gcd, lcm
import unittest

from observational_succ.finite_fourier_carrier import CyclotomicElement
from observational_succ.integer_bbp_carrier import source_states
from observational_succ.succ_internal_matrix_walk import PhasePoly, MatrixWalk
from observational_succ.spectral_purity_arithmetic import (
    conductor_growth_certificate, conductor_growth_count_upper,
    conductor_birth_innovation_budget, conductor_locked_countermodel,
    prescribed_width, fejer_overlap,
    relative_cyclotomic_trace, source_trace_certificate,
)


def quotient(value, modulus):
    result = CyclotomicElement.scalar(modulus, 0)
    for phase, coefficient in value.terms:
        exponent = phase*modulus
        assert exponent.denominator == 1
        result += CyclotomicElement.root(modulus, exponent.numerator).scale(coefficient)
    return result


class RelativeTraceTests(unittest.TestCase):
    def test_independent_exact_cyclotomic_automorphism_average(self):
        # Calibration plus mixed-conductor holdouts. This averages actual
        # quotient elements; it does not reuse the Ramanujan trace formula.
        cases = ((9, 3, 0), (9, 3, 1), (15, 3, 0), (45, 3, 1),
                 (75, 5, 1), (63, 7, 0), (99, 11, 0), (125, 5, 2))
        for modulus, p, old_depth in cases:
            other = modulus
            while other % p == 0:
                other //= p
            fixed = other*p**old_depth
            automorphisms = [u for u in range(1, modulus)
                             if gcd(u, modulus) == 1 and (u-1) % fixed == 0]
            for exponent in range(modulus):
                formal = PhasePoly.monomial(Q(exponent, modulus))
                predicted = relative_cyclotomic_trace(formal, p, old_depth)
                actual = CyclotomicElement.scalar(modulus, 0)
                for u in automorphisms:
                    actual += CyclotomicElement.root(modulus, u*exponent)
                actual = actual.scale(Q(1, len(automorphisms)))
                self.assertEqual(quotient(predicted, modulus), actual)

    def test_trace_is_quotient_relation_not_formal_equality(self):
        formal_mean = sum((PhasePoly.monomial(Q(u, 9)) for u in (1, 4, 7)),
                          PhasePoly.zero())/3
        trace = relative_cyclotomic_trace(PhasePoly.monomial(Q(1, 9)), 3, 1)
        self.assertNotEqual(formal_mean, trace)
        self.assertEqual(trace, PhasePoly.zero())
        self.assertEqual(quotient(formal_mean, 9), quotient(trace, 9))

    def test_fixed_history_coefficients_pull_through_trace(self):
        old = PhasePoly.from_dict({Q(1, 15): Q(2), Q(2, 5): Q(-3)})
        new = PhasePoly.from_dict({Q(1, 45): Q(4), Q(2, 9): Q(1), Q(1, 3): Q(2)})
        self.assertEqual(relative_cyclotomic_trace(old*new, 3, 1),
                         old*relative_cyclotomic_trace(new, 3, 1))

    def test_generic_zero_forcing_is_not_authenticated(self):
        self.assertEqual(fejer_overlap((Q(), Q()), Q(), 5),
                         PhasePoly.monomial(0, 25))
        self.assertEqual(relative_cyclotomic_trace(PhasePoly.monomial(0, 25), 7, 0),
                         PhasePoly.monomial(0, 25))

    def test_changed_pole_weight_retains_trace_without_authentication(self):
        # Change the +4 pole to +5. A genuine new 3^2 layer survives,
        # so the same quotient trace theorem holds for this wrong source.
        old = Q(5)-Q(2, 4)-Q(1, 5)-Q(1, 6)
        force = Q(5, 9)-Q(2, 12)-Q(1, 13)-Q(1, 14)
        arrival = 16*old+force
        mutant = fejer_overlap((old,), arrival, 3)
        authentic = source_trace_certificate(2, 3, 3)
        self.assertNotEqual(mutant, authentic.selected_innovation)
        self.assertEqual(relative_cyclotomic_trace(mutant, 3, 1),
                         authentic.traced_innovation)

    def test_invalid_prime_or_nonexact_inputs(self):
        for p in (2, 9, True):
            with self.assertRaises(ValueError):
                relative_cyclotomic_trace(PhasePoly.one(), p, 0)
        with self.assertRaises(ValueError):
            fejer_overlap((Q(),), 0.0, 3)
        with self.assertRaises(ValueError):
            source_trace_certificate(3, 4, 3)  # no new 3 layer here
        with self.assertRaises(ValueError):
            source_trace_certificate(2, 4, 3)  # observer aliases mod 3


class AuthenticBirthTests(unittest.TestCase):
    def test_source_trace_against_integer_carrier(self):
        for n, p, h in ((2, 3, 3), (2, 7, 4), (3, 17, 4),
                        (4, 5, 5), (7, 7, 7), (11, 3, 2),
                        (16, 11, 5), (22, 13, 8), (31, 241, 9)):
            witness = source_trace_certificate(n, h, p)
            integer = source_states(n)
            self.assertEqual(witness.original_lift,
                             Q(integer[-1].numerator, integer[-1].conductor))
            self.assertEqual(witness.old_conductor, integer[-2].conductor)
            self.assertEqual(witness.new_conductor, integer[-1].conductor)
            self.assertEqual(witness.traced_innovation, witness.predicted_trace)
            self.assertFalse(witness.selected_bound_proved)
            self.assertEqual(witness.p_free_complement.denominator % p == 0, False)
            if witness.old_depth:
                self.assertEqual(witness.traced_innovation, PhasePoly.monomial(0, h))

    def test_independent_gram_innovation(self):
        for width in (2, 3, 5):
            walk = MatrixWalk.initial(width).succ()
            for n in range(2, 6):
                q, _ = walk.innovation()
                self.assertEqual(q, fejer_overlap(walk.history,
                                                 walk.next_character_vector()[0], width))
                walk = walk.succ()

    def test_large_window_retains_frequency_alias(self):
        source = source_trace_certificate(2, 3, 3)
        old = Q(source_states(1)[-1].numerator, source.old_conductor)
        wider = fejer_overlap((old,), source.original_lift, 4)
        traced = relative_cyclotomic_trace(wider, 3, 1)
        self.assertNotEqual(traced, PhasePoly.monomial(0, 4))
        expected = (PhasePoly.monomial(0, 4)
                    + PhasePoly.monomial(3*(source.original_lift-old))
                    + PhasePoly.monomial(-3*(source.original_lift-old)))
        self.assertEqual(traced, expected)

    def test_exact_conductor_growth_and_prime_power_injection(self):
        for horizon in (1, 2, 9, 32, 65, 129):
            witness = conductor_growth_certificate(horizon)
            integers = source_states(horizon)
            independent = tuple(n for n in range(1, horizon+1)
                                if integers[n].conductor > integers[n-1].conductor)
            self.assertEqual(witness.growth_times, independent)
            powers = {(p, a) for _, p, a in witness.layers}
            self.assertEqual(len(powers), len(witness.layers))
            self.assertLessEqual(len(witness.growth_times), len(witness.layers))
            self.assertLessEqual(len(witness.layers), witness.available_prime_power_count)
            flat_weight = sum(n-1 for n in range(2, horizon+1) if n not in independent)
            self.assertEqual(witness.weighted_flat_steps, flat_weight)

    def test_predetermined_schedule_and_universal_birth_budget(self):
        for exponent, expected in ((0, 2), (1, 2), (4, 3), (9, 4),
                                   (16, 5), (25, 6), (64, 9)):
            n = 2**exponent
            self.assertEqual(prescribed_width(n), expected)
        for horizon in (9, 32, 129, 513):
            certificate = conductor_growth_certificate(horizon)
            self.assertLessEqual(len(certificate.growth_times),
                                 conductor_growth_count_upper(horizon))
            width = prescribed_width(horizon)
            weighted_growth = certificate.total_step_weight-certificate.weighted_flat_steps
            exact_budget = Q(2*(width-1)*weighted_growth, horizon*horizon)
            self.assertLessEqual(exact_budget, conductor_birth_innovation_budget(horizon))
        # A rigorous finite (very remote) nontrivial universal bound, with
        # integer logarithms and no source data. Not an asymptotic test.
        self.assertLess(conductor_birth_innovation_budget(2**65536), Q(1))

    def test_positive_wrong_source_preserves_entire_conductor_tower(self):
        mutant = conductor_locked_countermodel(65)
        authentic = source_states(65)
        self.assertFalse(mutant["authentic_four_pole_source"])
        self.assertEqual(mutant["states"][0], 0)
        self.assertEqual(mutant["conductors"], tuple(s.conductor for s in authentic))
        running = 1
        for n, force in enumerate(mutant["forcing"], 1):
            running = lcm(running, force.denominator)
            self.assertEqual(running, authentic[n].conductor)
            self.assertGreater(force, 0)
            state = mutant["states"][n]
            self.assertEqual(state % 1, 1-Q(1, authentic[n].conductor))
            self.assertNotEqual(state, Q(authentic[n].numerator, authentic[n].conductor))

    def test_conductor_is_history_lcm_even_if_current_state_cancels(self):
        # Recover Q_n from every state denominator, independently of forcing.
        for horizon in (9, 17, 65):
            integers = source_states(horizon)
            denominator = 1
            for state in integers:
                denominator = lcm(denominator,
                                  Q(state.numerator, state.conductor).denominator)
                self.assertEqual(denominator, state.conductor)


if __name__ == "__main__":
    unittest.main()
