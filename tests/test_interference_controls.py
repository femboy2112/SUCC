"""Exact adversarial controls; generic arrays and actual radix orbits stay typed."""
from fractions import Fraction as Q
from itertools import combinations, product
import unittest

from observational_succ.duck_bbp import forcing, lifted_orbit
from observational_succ.interference_controls import (
    chi_square, coset_character_phase, cyclic_sign_correlations,
    cyclic_word_counts, de_bruijn_cycle, geometric_label_rivals,
    global_charge_gcd, leading_digit, monomial_phase_signature,
    pair_gauge_components, pair_gauge_offsets, pair_phase_signature,
    periodic_radix_point, phase_alias_modulus, power_two_character_remainder,
    radix_cycle, references_fix_pair_gauges, seed_phase_alias_spacing,
    walsh_moments, walsh_perturbation,
)


class PairGaugeTests(unittest.TestCase):
    def test_connected_graphs_exactly_retain_global_rotation(self):
        for size in (*range(1, 9), 11, 13, 17):
            phases = tuple(Q(i*i+3*i+1, 2*size+1) % 1 for i in range(size))
            rotated = tuple((x+Q(1, 3)) % 1 for x in phases)
            edges = tuple((i, i+1) for i in range(size-1))
            self.assertEqual(pair_gauge_components(size, edges), (tuple(range(size)),))
            self.assertEqual(pair_phase_signature(phases, edges), pair_phase_signature(rotated, edges))
            self.assertEqual(pair_gauge_offsets(phases, rotated, edges), (Q(1, 3),))
            self.assertTrue(references_fix_pair_gauges(size, edges, (0,)))

    def test_disconnected_components_and_a_restoring_bridge(self):
        for size in (11, 13, 17):
            cut = size//2
            phases = tuple(Q(i, size+2) for i in range(size))
            shifts = (Q(1, 3),)*cut+(Q(2, 5),)*(size-cut)
            rotated = tuple((x+s) % 1 for x, s in zip(phases, shifts))
            edges = tuple((i, i+1) for i in range(size-1) if i != cut-1)
            self.assertEqual(pair_gauge_offsets(phases, rotated, edges), (Q(1, 3), Q(2, 5)))
            self.assertEqual(pair_phase_signature(phases, edges), pair_phase_signature(rotated, edges))
            self.assertFalse(references_fix_pair_gauges(size, edges, (0,)))
            self.assertTrue(references_fix_pair_gauges(size, edges, (0, size-1)))
            bridge = edges+((0, size-1),)
            self.assertIsNone(pair_gauge_offsets(phases, rotated, bridge))
            self.assertNotEqual(pair_phase_signature(phases, bridge), pair_phase_signature(rotated, bridge))

    def test_edge_orientation_retains_signed_quadrature(self):
        phases = (Q(1, 7), Q(2, 5), Q(3, 8))
        edges = ((0, 1), (1, 2), (2, 0))
        reversed_edges = tuple((j, i) for i, j in edges)
        original = pair_phase_signature(phases, edges)
        self.assertEqual(pair_phase_signature(phases, reversed_edges), tuple(-x % 1 for x in original))
        conjugated = tuple(-x % 1 for x in phases)
        self.assertNotEqual(pair_phase_signature(phases, edges), pair_phase_signature(conjugated, edges))

    def test_balanced_tensors_do_not_remove_global_gauge(self):
        phases = (Q(1, 11), Q(2, 13), Q(3, 17))
        rows = ((1, -1, 0), (2, -3, 1), (5, 7, -12))
        rotated = tuple(x+Q(2, 7) for x in phases)
        self.assertEqual(global_charge_gcd(rows), 0)
        self.assertEqual(monomial_phase_signature(phases, rows), monomial_phase_signature(rotated, rows))

    def test_charge_two_alias_and_coprime_charge_repair(self):
        phases = (Q(1, 11), Q(3, 13))
        rotated = tuple(x+Q(1, 2) for x in phases)
        even_rows = ((1, -1), (2, 0))
        repaired = even_rows+((3, 0),)
        self.assertEqual(global_charge_gcd(even_rows), 2)
        self.assertEqual(monomial_phase_signature(phases, even_rows), monomial_phase_signature(rotated, even_rows))
        self.assertEqual(global_charge_gcd(repaired), 1)
        self.assertNotEqual(monomial_phase_signature(phases, repaired), monomial_phase_signature(rotated, repaired))

    def test_lattice_index_matters_not_only_real_span(self):
        first, second = (Q(), Q()), (Q(1, 2), Q())
        self.assertEqual(monomial_phase_signature(first, ((2, -2),)), monomial_phase_signature(second, ((2, -2),)))
        self.assertNotEqual(monomial_phase_signature(first, ((1, -1),)), monomial_phase_signature(second, ((1, -1),)))

    def test_genuine_fixed_radix_orbits_have_identical_pair_reports(self):
        zero, shifted = radix_cycle(0), radix_cycle(Q(1, 3))
        self.assertEqual(zero, (Q(),))
        self.assertEqual(shifted, (Q(1, 3),))
        # Both repeated orbit vectors have |W|=1; exact cos(2*pi/3)=-1/2.
        for size in (11, 13, 17):
            edges = tuple((i, (i+1) % size) for i in range(size))
            self.assertEqual(pair_phase_signature(zero*size, edges), pair_phase_signature(shifted*size, edges))
        self.assertEqual(1-Q(-1, 2), Q(3, 2))

    def test_pair_and_character_domain_guards(self):
        for phases, edges in (((0,), ((0, 1),)), ((0.0,), ()), ((0,), ((True, 0),))):
            with self.assertRaises(ValueError):
                pair_phase_signature(phases, edges)
        with self.assertRaises(ValueError):
            monomial_phase_signature((0, 0), ((1, 0.0),))
        with self.assertRaises(ValueError):
            references_fix_pair_gauges(3, ((0, 1),), (3,))


class SourceAliasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.clocks = tuple(range(19, 42))
        cls.states = tuple(lifted_orbit(n) for n in cls.clocks)

    def test_authentic_fresh_clocks_match_literal_four_pole_successor(self):
        for n, current, following in zip(self.clocks, self.states, self.states[1:]):
            m = n+1
            literal = Q(4, 8*m-7)-Q(2, 8*m-4)-Q(1, 8*m-3)-Q(1, 8*m-2)
            self.assertEqual(following-16*current, literal)
            self.assertEqual(forcing(m), literal)

    def test_original_forcing_seed_third_is_exact_global_phase(self):
        changed = tuple(u+Q(16**n, 3) for n, u in zip(self.clocks, self.states))
        edges = tuple((i, i+1) for i in range(len(changed)-1))
        self.assertEqual(pair_phase_signature(self.states, edges), pair_phase_signature(changed, edges))
        self.assertEqual(pair_gauge_offsets(self.states, changed, edges), (Q(1, 3),))
        self.assertNotEqual(tuple(u % 1 for u in self.states), tuple(u % 1 for u in changed))

    def test_original_forcing_late_seed_alias_is_complete_phase_blindness(self):
        changed = tuple(u+Q(16**n, 16) for n, u in zip(self.clocks, self.states))
        self.assertEqual(tuple(u % 1 for u in self.states), tuple(u % 1 for u in changed))
        self.assertNotEqual(self.states, changed)
        self.assertEqual(seed_phase_alias_spacing(tuple((n, 1) for n in self.clocks)), Q(1, 16**19))
        self.assertEqual(seed_phase_alias_spacing(((0, 1),)+tuple((n, 1) for n in self.clocks)), 1)

    def test_seed_phase_kernel_gcd_is_sharp(self):
        probes = ((2, 3), (3, 5), (4, -7))
        spacing = seed_phase_alias_spacing(probes)
        self.assertEqual(spacing, Q(1, 16**2))
        self.assertTrue(all((frequency*16**n*spacing).denominator == 1 for n, frequency in probes))
        self.assertTrue(any((frequency*16**n*spacing/2).denominator != 1 for n, frequency in probes))
        self.assertIsNone(seed_phase_alias_spacing(((19, 0), (41, 0))))

    def test_moving_denominator_harmonic_aliases_every_fresh_source_phase(self):
        frequency = phase_alias_modulus(self.states)
        self.assertGreater(frequency, 17)
        self.assertTrue(all((frequency*u).denominator == 1 for u in self.states))
        self.assertTrue(any(((frequency+1)*u).denominator != 1 for u in self.states))

    def test_digit_boundary_has_no_global_lipschitz_transfer(self):
        for depth in (2, 3, 5, 11, 13, 17):
            epsilon = Q(1, 16**depth)
            left, right = Q(1, 16)-epsilon, Q(1, 16)+epsilon
            self.assertEqual(leading_digit(left), 0)
            self.assertEqual(leading_digit(right), 1)
            self.assertEqual(right-left, 2*epsilon)
        self.assertEqual(leading_digit(Q(1, 32)), 0)
        self.assertEqual(8*Q(1, 32), Q(1, 4))  # smooth e(8x)=i, digit parity=+1

    def test_alias_domain_guards(self):
        for probes in ((), ((-1, 1),), ((1, 1.0),), ((True, 1),)):
            with self.assertRaises(ValueError):
                seed_phase_alias_spacing(probes)
        with self.assertRaises(ValueError):
            phase_alias_modulus((Q(1, 3), 0.0))


class PeriodicOrbitTests(unittest.TestCase):
    def test_actual_prime_smooth_periods_are_complete_affine_cosets(self):
        for denominator, period in ((405, 27), (675, 45), (1125, 75)):
            orbit = radix_cycle(Q(1, denominator))
            self.assertEqual(len(orbit), period)
            self.assertEqual(set(orbit), {Q(1+15*j, denominator) for j in range(period)})
            self.assertEqual(tuple((16*x) % 1 for x in orbit), orbit[1:]+orbit[:1])
            for h in range(1, 18):
                self.assertIsNone(coset_character_phase(orbit, h))
            self.assertEqual(coset_character_phase(orbit, period), Q(1, 15))
            self.assertEqual(coset_character_phase(orbit, denominator), 0)

    def test_incomplete_or_arbitrary_phase_arrays_do_not_receive_coset_certificate(self):
        orbit = radix_cycle(Q(1, 405))
        for values in (orbit[:-1], orbit+(orbit[0],), (Q(), Q(1, 5), Q(2, 3))):
            with self.assertRaises(ValueError):
                coset_character_phase(values, 1)

    def test_de_bruijn_all_fixed_depth_word_tests(self):
        for base, order in ((2, 3), (2, 4), (2, 5), (16, 1), (16, 2), (16, 3)):
            word = de_bruijn_cycle(base=base, order=order)
            self.assertEqual(len(word), base**order)
            for depth in range(1, order+1):
                counts = cyclic_word_counts(word, depth, base=base)
                self.assertEqual(len(counts), base**depth)
                self.assertEqual(set(counts.values()), {base**(order-depth)})
            self.assertLess(len(cyclic_word_counts(word, order+1, base=base)), base**(order+1))

    def test_hex_de_bruijn_is_real_radix_orbit_not_a_digit_grid_surrogate(self):
        word = de_bruijn_cycle(base=16, order=2)
        point = periodic_radix_point(word)
        orbit = radix_cycle(point)
        self.assertEqual(len(orbit), 256)
        self.assertEqual(tuple(leading_digit(x) for x in orbit), word)
        self.assertEqual(tuple((16*x) % 1 for x in orbit), orbit[1:]+orbit[:1])
        surrogate = tuple(Q(d, 16) for d in word)
        self.assertNotEqual(orbit, surrogate)
        self.assertTrue(any((16*surrogate[i]) % 1 != surrogate[(i+1) % len(word)] for i in range(len(word))))
        denominator = point.denominator
        self.assertTrue(all((denominator*x).denominator == 1 for x in orbit))

    def test_radix_and_word_budget_guards(self):
        with self.assertRaises(ValueError):
            radix_cycle(Q(1, 2))
        with self.assertRaises(ValueError):
            radix_cycle(Q(1, 405), max_period=26)
        with self.assertRaises(ValueError):
            de_bruijn_cycle(base=16, order=4)
        with self.assertRaises(ValueError):
            periodic_radix_point((15, 15))
        with self.assertRaises(ValueError):
            periodic_radix_point((0, 16))


class InteractionTests(unittest.TestCase):
    def test_prime_complement_marginals_do_not_fix_product(self):
        # State index uses bits for the two signs; mask3 is their product.
        for bias in (Q(-1), Q(), Q(1)):
            law = walsh_perturbation(2, 3, bias)
            self.assertEqual(walsh_moments(law, (1, 2)), (0, 0))
            self.assertEqual(walsh_moments(law, (3,)), (bias,))

    def test_all_proper_walsh_interactions_hide_the_final_one(self):
        for bits in (4, 5, 8):
            last = 2**bits-1
            for bias in (Q(-1), Q(1, 3), Q(1)):
                law = walsh_perturbation(bits, last, bias)
                moments = walsh_moments(law, tuple(range(2**bits)))
                self.assertEqual(moments, (Q(1),)+(Q(),)*(last-1)+(bias,))

    def test_one_missing_walsh_mask_has_an_explicit_probability_rival(self):
        bits, hidden = 5, 0b10101
        observed = tuple(mask for mask in range(1, 2**bits) if mask != hidden)
        plus, minus = walsh_perturbation(bits, hidden, 1), walsh_perturbation(bits, hidden, -1)
        self.assertEqual(walsh_moments(plus, observed), walsh_moments(minus, observed))
        self.assertNotEqual(walsh_moments(plus, (hidden,)), walsh_moments(minus, (hidden,)))

    def test_cross_digit_control_passes_low_marginals_but_has_even_fourier_mode(self):
        hidden = sum(1 << bit for bit in (0, 4, 5, 6))
        law = walsh_perturbation(8, hidden, 1)
        low_masks = tuple(mask for mask in range(1, 256) if mask.bit_count() <= 3)
        self.assertEqual(set(walsh_moments(law, low_masks)), {Q()})
        low_digit = tuple(sum((law[x] for x in range(256) if x % 16 == d), Q()) for d in range(16))
        high_digit = tuple(sum((law[x] for x in range(256) if x // 16 == d), Q()) for d in range(16))
        self.assertEqual(low_digit, (Q(1, 16),)*16)
        self.assertEqual(high_digit, (Q(1, 16),)*16)
        remainder = power_two_character_remainder(law, 2)
        self.assertEqual(len(remainder), 64)
        self.assertTrue(any(remainder))
        # Separate direct modulo-X^64+1 sum, not the implementation's grouping.
        direct = [Q()]*64
        for x, probability in enumerate(law):
            index = x % 128
            direct[index % 64] += probability*(1 if index < 64 else -1)
        self.assertEqual(remainder, tuple(direct))

    def test_uniform_character_null_and_trivial_character_controls(self):
        law = (Q(1, 16),)*16
        for h in (1, 2, 3, 4, 7, 8, 15, -3):
            self.assertFalse(any(power_two_character_remainder(law, h)))
        self.assertEqual(power_two_character_remainder(law, 0), (1,))
        self.assertEqual(power_two_character_remainder(law, 16), (1,))

    def test_all_pair_lags_can_miss_an_oriented_word(self):
        for size in (11, 13, 17):
            word = tuple(int(i in (0, 1, 3)) for i in range(size))
            reflected = tuple(word[-i % size] for i in range(size))
            signs, mirror = tuple(1-2*x for x in word), tuple(1-2*x for x in reflected)
            self.assertEqual(cyclic_sign_correlations(signs), cyclic_sign_correlations(mirror))
            self.assertFalse(any(reflected == word[j:]+word[:j] for j in range(size)))
            self.assertEqual(cyclic_word_counts(word, 4, base=2).get((1, 1, 0, 1), 0), 1)
            self.assertEqual(cyclic_word_counts(reflected, 4, base=2).get((1, 1, 0, 1), 0), 0)
            point = periodic_radix_point(word)
            mirror_point = periodic_radix_point(reflected)
            self.assertEqual(tuple(leading_digit(x) for x in radix_cycle(point)), word)
            self.assertEqual(tuple(leading_digit(x) for x in radix_cycle(mirror_point)), reflected)

    def test_interaction_domain_guards(self):
        for args in ((0, 1, 1), (9, 1, 1), (4, 0, 1), (4, 16, 1), (4, 1, 2), (4, 1, 1.0)):
            with self.assertRaises(ValueError):
                walsh_perturbation(*args)
        with self.assertRaises(ValueError):
            walsh_moments((Q(1, 2),)*2, (1, 1))
        with self.assertRaises(ValueError):
            power_two_character_remainder((Q(1, 3),)*3, 1)
        with self.assertRaises(ValueError):
            cyclic_sign_correlations((1, True, -1))


class UniversalClickControlTests(unittest.TestCase):
    def test_retained_label_and_forgotten_label_have_different_exact_cost(self):
        for period in (1, 3, 9, 27):
            control, haar = geometric_label_rivals(period)
            epsilon = Q(1, 2**period-1)
            self.assertEqual(chi_square(tuple(x for row in control for x in row),
                                        tuple(x for row in haar for x in row)), epsilon)
            control_coin = tuple(sum((row[j] for row in control), Q()) for j in (0, 1))
            haar_coin = tuple(sum((row[j] for row in haar), Q()) for j in (0, 1))
            self.assertEqual(control_coin, ((1+epsilon)/2, (1-epsilon)/2))
            self.assertEqual(haar_coin, (Q(1, 2), Q(1, 2)))
            self.assertEqual(chi_square(control_coin, haar_coin), epsilon*epsilon)

    def test_resonant_click_is_a_one_sided_discriminator(self):
        for period in (3, 9, 27):
            control, haar = geometric_label_rivals(period)
            self.assertEqual(control[-1][1], 0)
            self.assertEqual(haar[-1][1], Q(1, 2*(2**period-1)))
            self.assertEqual(control[:-1], haar[:-1])

    def test_product_chi_square_formula_by_direct_enumeration(self):
        control, haar = geometric_label_rivals(3)
        p, q = tuple(x for row in control for x in row), tuple(x for row in haar for x in row)
        for count in (1, 2, 3):
            pp, qq = [], []
            for labels in product(range(len(p)), repeat=count):
                left, right = Q(1), Q(1)
                for label in labels:
                    left *= p[label]
                    right *= q[label]
                pp.append(left)
                qq.append(right)
            self.assertEqual(1+chi_square(pp, qq), (1+chi_square(p, q))**count)

    def test_statistical_control_domains(self):
        for period in (0, 257, True):
            with self.assertRaises(ValueError):
                geometric_label_rivals(period)
        with self.assertRaises(ValueError):
            chi_square((Q(1, 2), Q(1, 2)), (1, 0))
        with self.assertRaises(ValueError):
            chi_square((1.0,), (1,))


if __name__ == "__main__":
    unittest.main()
