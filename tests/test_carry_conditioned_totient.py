"""Exact carry/cyclotomic checks and hostile alias/source controls."""
import unittest
from fractions import Fraction as Q
from math import gcd

from observational_succ import carry_conditioned_totient as c


def independent_force(n):
    # Deliberately independent literal four-pole implementation in the oracle.
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def independent_states(count, seed=Q()):
    values = [seed]
    for n in range(1, count+1):
        values.append(16*values[-1]+independent_force(n))
    return tuple(values)


class CarryConditionedTotient(unittest.TestCase):
    def test_literal_word_and_independent_source_oracle(self):
        for depth in (1, 2, 3, 5):
            states = independent_states(32+depth)
            for word in c.authentic_carry_words(32, depth):
                n, q = word.time, word.radix_power
                expected = states[n+depth].__floor__()-q*states[n].__floor__()
                self.assertEqual(word.word, expected)
                self.assertEqual(word.word,
                                 sum(16**(depth-1-j)*v
                                     for j, v in enumerate(word.carries)))
                self.assertEqual(word.initial_phase, states[n] % 1)
                self.assertTrue(all(0 <= v <= 16 for v in word.carries))

    def test_exact_conductor_decoder_and_carry_constraint(self):
        for depth in (1, 2, 4):
            for w in c.authentic_carry_words(40, depth):
                self.assertEqual(w.conductor % 2, 1)
                self.assertEqual(w.conductor_decoded_residue, w.residue)
                self.assertEqual(w.conductor*w.word,
                                 w.radix_power*w.conductor*w.initial_phase
                                 +w.forcing_numerator-w.final_remainder)
                self.assertEqual(w.forcing_numerator,
                                 w.conductor*sum((16**(depth-j)
                                     *independent_force(w.time+j)
                                     for j in range(1, depth+1)), Q()))

    def test_primitive_dyadic_word_is_only_terminal_parity(self):
        for depth in (1, 2, 3, 7):
            for w in c.authentic_carry_words(45, depth):
                self.assertEqual(w.is_primitive, bool(w.carries[-1] % 2))
                self.assertEqual(w.word % 2, w.carries[-1] % 2)

    def test_wrong_source_decoder_mutation_is_detected(self):
        # A unit mutation in the authenticated forcing lift changes every
        # decoded residue, because the odd conductor has a dyadic inverse.
        for w in c.authentic_carry_words(16, 2):
            mutant = ((w.forcing_numerator+1-w.final_remainder)
                      *pow(w.conductor, -1, w.radix_power)) % w.radix_power
            self.assertNotEqual(mutant, w.residue)

    def test_endpoint_wrapping_is_normalized_and_exactly_invertible(self):
        for q in (2, 4, 16, 256):
            packet = c.endpoint_wrapped_packet(q)
            self.assertEqual(sum(packet), 1)
            self.assertTrue(all(v > 0 for v in packet))
            self.assertEqual(c.invert_endpoint_packet(packet),
                             (Q(1),)+(Q(),)*(q-1))

    def test_source_word_convolution_recovers_full_history_law(self):
        for depth in (1, 2):
            words = c.authentic_carry_words(24, depth)
            source = c.word_distribution(words)
            convolved = c.endpoint_carry_packet_law(words)
            self.assertEqual(sum(source), 1)
            self.assertEqual(sum(convolved), 1)
            self.assertEqual(c.invert_endpoint_packet(convolved), source)

    def test_carry_oily_totient_scalar_really_reads_terminal_parity(self):
        for depth in (1, 2):
            words = c.authentic_carry_words(20, depth)
            law = c.endpoint_carry_packet_law(words)
            odd_fraction = Q(sum(w.word % 2 for w in words), len(words))
            self.assertEqual(sum(c.primitive_projection(law)),
                             Q(4, 9)+odd_fraction/9)
            self.assertLess(sum(c.primitive_projection(law)), Q(5, 9))

    def test_exact_primitive_fourier_alias_identity(self):
        for depth in (1, 2):
            law = c.endpoint_carry_packet_law(c.authentic_carry_words(13, depth))
            q = len(law)
            primitive = c.primitive_projection(law)
            for h in (-7, 0, 1, 2, 3, 16):
                base = c.dyadic_character(law, h)
                alias = c.dyadic_character(law, h+q//2)
                self.assertEqual(c.dyadic_character(primitive, h),
                                 tuple((a-b)/2 for a, b in zip(base, alias)))

    def test_finite_source_packet_coupling_has_certified_error(self):
        for depth in (1, 2):
            words = c.authentic_carry_words(12, depth)
            endpoint = c.endpoint_carry_packet_law(words)
            finite = c.finite_source_carry_packet_law(words, 9)
            self.assertEqual(sum(finite), 1)
            self.assertTrue(all(v >= 0 for v in finite))
            budget = c.carry_packet_transport_budget(12, depth, 1, 9)
            self.assertLessEqual(sum(abs(a-b) for a, b in zip(finite, endpoint)),
                                 budget["source_packet_to_endpoint"])
            self.assertFalse(budget["proves_selected_cancellation"])

    def test_finite_changed_seed_control_preserves_forcing_not_carries(self):
        # Exact finite-depth approximation to V0=-pi/16. It proves no claim
        # about the infinite authentic zero seed. Before the cutoff all
        # states lie in (-1,0), so its literal carries are all 15.
        cutoff = 30
        seed = -sum((independent_force(j)/16**j
                     for j in range(1, cutoff+1)), Q())
        states = independent_states(cutoff, seed)
        self.assertEqual(states[-1], 0)
        self.assertTrue(all(-1 < x < 0 for x in states[:-1]))
        carries = tuple(states[n].__floor__()-16*states[n-1].__floor__()
                        for n in range(1, cutoff))
        self.assertEqual(carries, (15,)*(cutoff-1))
        authentic = c.authentic_carry_words(20, 2)
        self.assertNotEqual(tuple(w.word for w in authentic), (255,)*20)
        shifted_packet = c.cyclic_shift(c.endpoint_wrapped_packet(256), 255)
        self.assertEqual(sum(c.primitive_projection(shifted_packet)), Q(5, 9))

    def test_single_digit_marginals_do_not_determine_two_digit_character(self):
        # (0,0),(1,1) vs (0,1),(1,0): equal BOTH digit marginals and
        # primitive totals, different actual joint complex characters.
        a, b = [Q()]*256, [Q()]*256
        a[0] = a[17] = b[1] = b[16] = Q(1, 2)
        for place in (1, 16):
            marginal_a = tuple(sum(v for j, v in enumerate(a)
                                   if (j//place) % 16 == digit)
                               for digit in range(16))
            marginal_b = tuple(sum(v for j, v in enumerate(b)
                                   if (j//place) % 16 == digit)
                               for digit in range(16))
            self.assertEqual(marginal_a, marginal_b)
        self.assertEqual(sum(c.primitive_projection(a)), Q(1, 2))
        self.assertEqual(sum(c.primitive_projection(b)), Q(1, 2))
        self.assertNotEqual(c.dyadic_character(a, 1), c.dyadic_character(b, 1))

    def test_primitive_projection_loses_even_support(self):
        a, b = [Q()]*16, [Q()]*16
        a[0] = b[2] = Q(1)
        self.assertEqual(c.primitive_projection(a), c.primitive_projection(b))
        self.assertNotEqual(c.dyadic_character(a, 1), c.dyadic_character(b, 1))

    def test_budget_is_nonvacuously_improving_without_claiming_cancellation(self):
        coarse = c.carry_packet_transport_budget(128, 1, 3, 4)
        fine = c.carry_packet_transport_budget(1024, 3, 3, 20)
        self.assertLess(fine["word_to_selected"], coarse["word_to_selected"])
        self.assertLess(fine["source_packet_to_endpoint"],
                        coarse["source_packet_to_endpoint"])
        self.assertLess(fine["word_to_selected"], Q(1, 100))

    def test_domain_rejections(self):
        for args in ((True, 1), (1, 0), (2000, 1)):
            with self.assertRaises(ValueError):
                c.authentic_carry_words(*args)
        with self.assertRaises(ValueError):
            c.dyadic_character((Q(1), Q(), Q()), 1)
        with self.assertRaises(ValueError):
            c.cyclic_shift((0.5, 0.5), 1)
        with self.assertRaises(ValueError):
            c.word_distribution(())


if __name__ == "__main__":
    unittest.main()
