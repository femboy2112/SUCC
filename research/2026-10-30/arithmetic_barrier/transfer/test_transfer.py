"""Exact, mutation-sensitive finite checks; independent of parent probes."""
from collections import Counter
from fractions import Fraction as F
from math import comb, prod
import unittest

import transfer_probe as t


class TransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orbit = t.bbp_orbit(385)

    def test_authentic_recurrence_independent_pole_sum(self):
        self.assertEqual(self.orbit[1], F(47, 15))
        for n in (1, 2, 4, 9, 31, 97):
            self.assertEqual(self.orbit[n], t.direct_bbp(n))

    def test_first_packet_geometry_all_prime_classes(self):
        classes = set()
        for n in list(range(3, 41)) + [97, 127, 211, 257]:
            plus, minus = t.grid_witness_primes(n)
            for p in plus + minus:
                classes.add(p % 8)
                events = t.first_pole_events(p, n + 1)
                self.assertEqual(len(events), 1, (n, p, events))
                birth, _, multiplier, _ = events[0]
                self.assertLessEqual(birth, n)
                self.assertEqual(multiplier, 1 if p in plus else 2)
                self.assertGreater(p * p, 8 * (n + 1) - 2)
        self.assertEqual(classes, {1, 3, 5, 7})

    def test_exact_grid_denominator_obstruction_and_modular_oracle(self):
        for n in list(range(3, 65)) + [97, 127, 211, 257, 383]:
            plus, minus = t.grid_witness_primes(n)
            diff = self.orbit[n + 1] - self.orbit[n]
            self.assertEqual(diff.denominator % prod(plus + minus), 0)
            for p in plus + minus:
                self.assertEqual(t.valuation(self.orbit[n], p), -1)
                self.assertEqual(t.valuation(diff, p), -1)
                birth, _, multiplier, coeff = t.first_pole_events(p, n + 1)[0]
                expected = t.rational_mod(F(15 * coeff, multiplier), p)
                expected = expected * pow(16, n - birth, p) % p
                self.assertEqual(t.rational_mod(p * diff, p), expected)
                self.assertNotEqual(expected, 0)

    def test_translated_two_point_grid_minimum(self):
        for n in (7, 23, 64, 97):
            diff = self.orbit[n + 1] - self.orbit[n]
            q = diff.denominator
            self.assertEqual((q * diff).denominator, 1)
            for p in sum(t.grid_witness_primes(n), []):
                self.assertNotEqual(((q // p) * diff).denominator, 1)

    def test_p_integral_rational_seed_aliases_do_not_break_grid_result(self):
        for seed in (F(1, 16), F(1, 256), F(1, 3), F(2, 5), F(1, 7)):
            for n in (23, 97):
                diff = self.orbit[n + 1] - self.orbit[n] + 15 * 16 ** n * seed
                for p in sum(t.grid_witness_primes(n), []):
                    if seed.denominator % p:
                        self.assertEqual(t.valuation(diff, p), -1)

    def test_source_deletion_is_a_true_negative_control(self):
        n = 23
        plus, minus = t.grid_witness_primes(n)
        self.assertTrue(minus)
        fixed_ratio = t.bbp_orbit(n + 1, (4, 0, -1, 0))
        diff = fixed_ratio[n + 1] - fixed_ratio[n]
        for p in plus:
            self.assertEqual(t.valuation(diff, p), -1)
        for p in minus:
            self.assertGreaterEqual(t.valuation(diff, p), 0)
        wrong_ratio = t.bbp_orbit(n + 1, (5, -2, -1, -1))
        for p in plus + minus:
            self.assertEqual(t.valuation(wrong_ratio[n + 1] - wrong_ratio[n], p), -1)
        self.assertEqual(t.bbp_orbit(5, (0, 0, 0, 0)), [F()] * 6)

    def test_known_p73_strobe_cancellation_is_preserved(self):
        self.assertEqual(t.rational_mod(self.orbit[4], 73), 0)
        self.assertNotEqual(self.orbit[274].denominator % 73, 0)

    def test_stoneham_complete_cycles_two_independent_implementations(self):
        for c, maximum in ((3, 5), (5, 4)):
            for level in range(1, maximum + 1):
                vals = t.stage_residues(c, level)
                self.assertEqual(vals, t.stage_residues_oracle(c, level))
                counts = Counter(vals)
                self.assertEqual(len(counts), c ** (level - 1))
                self.assertEqual(set(counts.values()), {c * (c - 1)})
                self.assertTrue(all(int(c ** level * z) % c == 1 for z in vals))

    def test_stoneham_character_zeros_exact_cyclotomic_reduction(self):
        for c, levels in ((3, (2, 3, 5)), (5, (2, 3, 4))):
            for level in levels:
                vals = t.stage_residues(c, level)
                for h in (1, 2, 7, 17, c ** (level - 1), c ** level):
                    rem = t.prime_power_character_remainder(vals, h, c, level)
                    if h % (c ** (level - 1)):
                        self.assertFalse(any(rem))
                    else:
                        self.assertTrue(any(rem))
                        self.assertEqual(len({h * int(c ** level * z) % (c ** level)
                                              for z in vals}), 1)

    def test_stoneham_tail_and_all_horizon_interval_certificate(self):
        arcs = [(F(0), F(1, 16)), (F(15, 16), F(1, 8)),
                (F(17, 97), F(3, 101)), (F(9, 11), F(2, 17))]
        for c in (3, 5):
            for level in (1, 2, 3):
                for n in (c ** level, c ** (level + 1) - 1):
                    self.assertLess(t.stage_tail_partial(c, level, n),
                                    t.stage_tail_bound(c, level))
            for N in (31, 97, 219, 503):
                for start, length in arcs:
                    upper = t.stoneham_certified_upper(c, N, start, length)
                    self.assertLessEqual(upper, t.stoneham_hotspot_bound(c, N, length))

    def test_conductor_two_exact_sparse_digits(self):
        K, N = 8, 350
        value = sum((F(1, 2 ** k * 16 ** (2 ** k))
                     for k in range(1, K + 1)), F())
        upper = value + F(1, 2 ** K * 16 ** (2 ** (K + 1)))
        self.assertEqual(int(value * 16 ** N), int(upper * 16 ** N))
        actual = [(i + 1, d) for i, d in enumerate(t.digits(value, N)) if d]
        self.assertEqual(actual, t.sparse_two_pulses(K))

    def test_naive_bbp_stoneham_transplant_fails(self):
        counts = Counter(int(3 * (self.orbit[n] % 1)) for n in range(9, 27))
        self.assertEqual([counts[j] for j in range(3)], [9, 7, 2])
        self.assertNotEqual([counts[j] for j in range(3)], [6, 6, 6])

    def test_primary_gluing_preserves_affine_update_but_not_carry(self):
        for p in (7, 13, 17, 29):
            for n in range(1, 81):
                xprev, x = self.orbit[n - 1] % 1, self.orbit[n] % 1
                carry = int(16 * xprev + t.forcing(n))
                self.assertEqual(x, 16 * xprev + t.forcing(n) - carry)
                self.assertEqual(t.primary(x, p),
                                 (16 * t.primary(xprev, p) + t.primary(t.forcing(n), p)) % 1)
                for mask in range(16):
                    self.assertIn(t.walsh(carry % 16, mask), (-1, 1))
            self.assertEqual({t.primary(F(d, 16), p) for d in range(16)}, {F()})
            for mask in range(1, 16):
                self.assertEqual({t.walsh(d, mask) for d in range(16)}, {-1, 1})
            for k in (1, 3, 17, 101):
                x = F(1, p * (1 + k * p))
                self.assertEqual(t.primary(x, p), F(1, p))
                self.assertLess(x, F(1, p * k))

    def test_full_walsh_and_q3_q6_loss_are_retained(self):
        for a in range(16):
            for b in range(16):
                self.assertEqual(sum(t.walsh(d, a) * t.walsh(d, b)
                                     for d in range(16)), 16 if a == b else 0)
        self.assertEqual(0 % 6, 6 % 6)
        self.assertEqual(0 % 3, 6 % 3)
        self.assertNotEqual(t.walsh(0, 2), t.walsh(6, 2))

    def test_retained_posterior_triangle_and_source_mutants(self):
        for n in (1, 4, 13):
            for failures in range(4):
                for successes in range(4):
                    mass = t.positive_word_mass(n, failures, successes)
                    self.assertGreater(mass, 0)
                    self.assertEqual(mass, t.positive_word_mass(n, failures + 1, successes)
                                     + t.positive_word_mass(n, failures, successes + 1))
        for n in (1, 7, 31):
            a = 8 * n - 7
            gamma_fake = F(15, a * a)
            jet_fake = t.forcing(n) + sum(((-1) ** j * comb(3, j) * F(1, a + j)
                                          for j in range(4)), F())
            self.assertNotEqual(gamma_fake, t.forcing(n))
            self.assertGreater(jet_fake, t.forcing(n))

    def test_forward_posterior_tilt_and_unbounded_reverse_likelihood(self):
        for k, N in ((1, 10), (2, 51), (4, 274)):
            self.assertEqual(t.positive_word_mass(k, N - k, 0), t.forcing(N))
            prefactor = t.forcing(N) / t.forcing(k)
            self.assertGreater(prefactor, 0)
            self.assertLess(prefactor, 1)
            # At X=j*log(2)/8 the exact reverse density is this rational.
            for threshold in (1, 10, 10**6):
                j = 1
                while prefactor * 2 ** (j * (N - k)) <= threshold:
                    j += 1
                self.assertGreater(prefactor * 2 ** (j * (N - k)), threshold)

    def test_nonnormal_debruijn_and_kempner_calibration(self):
        cycle = t.debruijn_cycle()
        self.assertEqual(len(cycle), 256)
        pairs = Counter((cycle[i], cycle[(i + 1) % 256]) for i in range(256))
        self.assertEqual(len(pairs), 256)
        self.assertEqual(set(pairs.values()), {1})
        triples = {(cycle[i], cycle[(i + 1) % 256], cycle[(i + 2) % 256])
                   for i in range(256)}
        self.assertLess(len(triples), 16 ** 3)
        # Base-16 shifts are binary shifts by 4n. Each one bit affects at most L sites.
        for N, L in ((101, 7), (509, 13)):
            positions = {2 ** j for j in range((4 * N + L).bit_length())}
            exceptional = sum(any(4 * n + k in positions for k in range(1, L + 1))
                              for n in range(N))
            self.assertLessEqual(exceptional, L * len(positions))

    def test_exact_low_jets_and_biased_independent_walsh_controls(self):
        def source_jet(order):
            return sum(c * (-a) ** order for a, c in ((0, 4), (3, -2), (4, -1), (5, -1)))
        def cubic_jet(order):
            return sum((-1) ** j * comb(3, j) * (-j) ** order for j in range(4))
        self.assertEqual([source_jet(j) for j in range(4)], [0, 15, -59, 243])
        self.assertEqual([cubic_jet(j) for j in range(4)], [0, 0, 0, 6])
        self.assertEqual([source_jet(j) for j in (0, 1)], [0, 15])  # Q_fake=15x
        self.assertNotEqual(source_jet(2), 0)
        for j in range(3):
            self.assertEqual(source_jet(j) + cubic_jet(j), source_jet(j))
        self.assertNotEqual(source_jet(3) + cubic_jet(3), source_jet(3))
        biased = [F(1, 2)] + [F(1, 30)] * 15
        self.assertEqual(sum(biased), 1)
        for mask in range(1, 16):
            self.assertEqual(sum(biased[d] * t.walsh(d, mask) for d in range(16)), F(7, 15))
            self.assertEqual(sum(F(1, 16) * t.walsh(d, mask) for d in range(16)), 0)
        for word, future in (((0,), (15, 1)), ((3, 2), (0,)), ((15, 0, 7), (2, 3))):
            def mass(ds):
                return prod(biased[d] for d in ds)
            self.assertEqual(mass(word + future) / mass(word), mass(future))

    def test_finite_champernowne_recovery_and_approximate_grid_instrument(self):
        # A finite prefix of the classical normal construction, not a proof from counts.
        text = ''.join(format(n, 'X') for n in range(1, 257))
        by_division = []
        for n in range(1, 257):
            digits, value = [], n
            while value:
                value, digit = divmod(value, 16)
                digits.append(digit)
            by_division.extend(reversed(digits))
        self.assertEqual([int(char, 16) for char in text], by_division)
        self.assertEqual(text[:21], '123456789ABCDEF101112')
        self.assertEqual(t.smallest_covering_arc([F(1, 100), F(99, 100)]), F(1, 50))
        exact_grid = [F(1, 19) + F(j, 7) for j in range(4)]
        result = t.approximate_grid_search(exact_grid, 7, F())
        self.assertIn(7, result['feasible_q'])
        self.assertEqual(result['minimum_radius'], '0')


if __name__ == "__main__":
    unittest.main(verbosity=2)
