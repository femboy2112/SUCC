"""Exact controls for joint conditioning, trimming and literal carry transport."""
from fractions import Fraction as Q
from itertools import product
from math import lcm
import unittest

from observational_succ.joint_observer_entropy import (
    WordLaw, bbp_safe_retained_indices, bbp_safe_start,
    collision_data_processing, conditional_collision_chain,
    empirical_block_law, one_cell_collision_transport,
    relative_second_moment, trimmed_entropy_budget,
)


def uniform_word_law(base, depth):
    return WordLaw(base, depth, tuple(
        (w, Q(1, base**depth)) for w in product(range(base), repeat=depth)))


def sum_zero_law(base, depth):
    return WordLaw(base, depth, tuple(
        (w, Q(1, base**(depth-1)))
        for w in product(range(base), repeat=depth) if sum(w) % base == 0))


def exact_log_comparison(terms):
    """Compare a small rational linear combination of logs without floats."""
    denominator = lcm(*(coefficient.denominator for coefficient, _ in terms))
    value = Q(1)
    for coefficient, argument in terms:
        exponent = coefficient*denominator
        assert exponent.denominator == 1 and argument > 0
        value *= argument**int(exponent)
    return value


class WordLawDomains(unittest.TestCase):
    def test_probability_and_digit_domains(self):
        for args in ((1, 1, (((0,), 1),)), (2, True, (((0,), 1),)),
                     (2, 1, (((False,), 1),)), (2, 1, (((2,), 1),)),
                     (2, 1, (((0, 1), 1),)), (2, 1, (((0,), 1.0),)),
                     (2, 1, (((0,), True),)), (2, 1, (((0,), Q(1, 2)),)),
                     (2, 1, (((0,), 2), ((1,), -1)))):
            with self.subTest(args=args), self.assertRaises(ValueError):
                WordLaw(*args)

    def test_duplicates_and_zero_masses_are_canonicalized(self):
        law = WordLaw(2, 1, (((0,), Q(1, 4)), ((0,), Q(3, 4)), ((1,), 0)))
        self.assertEqual(law.atoms, (((0,), Q(1)),))
        self.assertEqual(law.prefix(0).atoms, (((), Q(1)),))
        with self.assertRaises(ValueError):
            law.prefix(2)

    def test_absolute_continuity_and_space_are_checked(self):
        actual = uniform_word_law(2, 2)
        singular_reference = WordLaw(2, 2, (((0, 0), 1),))
        with self.assertRaises(ValueError):
            relative_second_moment(actual, singular_reference)
        with self.assertRaises(ValueError):
            conditional_collision_chain(actual, uniform_word_law(3, 2))
        with self.assertRaises(ValueError):
            collision_data_processing(actual, actual, {(0, 0): 0})


class ExactJointCollision(unittest.TestCase):
    def test_uniform_and_point_laws_have_known_conditional_ratios(self):
        for base, depth in ((2, 4), (3, 3), (5, 3), (16, 2)):
            uniform = conditional_collision_chain(uniform_word_law(base, depth))
            point = conditional_collision_chain(
                WordLaw(base, depth, (((0,)*depth, 1),)))
            self.assertEqual([s.ratio for s in uniform], [Q(1)]*depth)
            self.assertEqual([s.ratio for s in point], [Q(base)]*depth)

    def test_full_joint_parity_survives_every_proper_coordinate_marginal(self):
        for base, depth in ((2, 4), (3, 3), (5, 3)):
            law = sum_zero_law(base, depth)
            chain = conditional_collision_chain(law)
            self.assertEqual([s.ratio for s in chain], [Q(1)]*(depth-1)+[Q(base)])
            # Independent literal projection onto every omitted coordinate.
            for omitted in range(depth):
                marginals = {}
                for w, mass in law.atoms:
                    v = w[:omitted]+w[omitted+1:]
                    marginals[v] = marginals.get(v, Q())+mass
                self.assertEqual(set(marginals.values()), {Q(1, base**(depth-1))})
            self.assertEqual(law.collision, base)
            self.assertNotEqual(law.collision, 1)  # false product-marginal mutation

    def test_repeated_parity_blocks_have_positive_density_joint_loss(self):
        allowed = [w for w in product(range(2), repeat=4) if sum(w) % 2 == 0]
        words = [u+v for u in allowed for v in allowed]
        law = WordLaw(2, 8, tuple((w, Q(1, len(words))) for w in words))
        chain = conditional_collision_chain(law)
        self.assertEqual([s.ratio for s in chain], [1, 1, 1, 2]*2)
        self.assertEqual(law.collision, 4)

    def test_correlated_reference_keeps_its_conditional_probabilities(self):
        actual = uniform_word_law(2, 2)
        reference = WordLaw(2, 2, (((0, 0), Q(1, 2)), ((0, 1), Q(1, 4)),
                                  ((1, 0), Q(1, 8)), ((1, 1), Q(1, 8))))
        chain = conditional_collision_chain(actual, reference)
        self.assertEqual(chain[0].ratio, Q(4, 3))
        self.assertEqual(chain[1].ratio, Q(33, 32))
        self.assertEqual(chain[-1].next_second_moment, Q(11, 8))
        self.assertEqual(relative_second_moment(actual, reference), Q(11, 8))
        product_value = Q(1)
        for step in chain:
            product_value *= step.ratio
            self.assertEqual(step.ratio, 1+step.escort_conditional_excess)
        self.assertEqual(product_value, Q(11, 8))

    def test_data_processing_distinguishes_hidden_and_visible_interactions(self):
        actual, reference = sum_zero_law(2, 4), uniform_word_law(2, 4)
        first = {w: w[0] for w, _ in reference.atoms}
        parity = {w: sum(w) % 2 for w, _ in reference.atoms}
        c_first = collision_data_processing(actual, reference, first)
        c_parity = collision_data_processing(actual, reference, parity)
        self.assertEqual((c_first.before, c_first.after), (2, 1))
        self.assertEqual((c_parity.before, c_parity.after), (2, 2))


class TrimmingAndFiniteEntropy(unittest.TestCase):
    def test_rare_hotspot_has_large_l2_but_exact_small_discarded_mass(self):
        for base in (2, 3, 5, 16):
            for depth in (2, 3):
                delta = Q(1, depth)
                masses = [
                    (w, (1-delta)/base**depth + (delta if not any(w) else 0))
                    for w in product(range(base), repeat=depth)]
                law = WordLaw(base, depth, tuple(masses))
                self.assertEqual(law.collision, 1+delta**2*(base**depth-1))
                self.assertEqual(uniform_word_law(base, depth).collision, 1)

    def test_trimmed_subset_never_replaces_original_short_block_window(self):
        word = (0,)*8+(1,)*8
        result = trimmed_entropy_budget(word, 12, 3, 1, (0, 2, 4), base=2)
        self.assertEqual(result.original_short_law.atoms,
                         (((0,), Q(2, 3)), ((1,), Q(1, 3))))
        self.assertEqual(result.discarded_mass, Q(3, 4))
        self.assertEqual(result.retained_collision, 8)

    def test_symbolic_entropy_bound_checked_by_exact_integer_powers(self):
        for base in (2, 3, 5):
            for depth, k in ((2, 1), (3, 1), (4, 2)):
                horizon = 12
                word = tuple((j*j+2*j+1) % base for j in range(horizon+depth-1))
                for retained in (tuple(range(horizon)), (0, 2, 5, 9)):
                    budget = trimmed_entropy_budget(word, horizon, depth, k,
                                                     retained, base)
                    # B - D(p_k||uniform) >= 0 iff this exact rational is >= 1.
                    terms = list(budget.log_terms)
                    terms.extend((-mass, mass*base**k)
                                 for _, mass in budget.original_short_law.atoms)
                    self.assertGreaterEqual(exact_log_comparison(terms), 1)

    def test_future_digits_and_original_window_domains_are_not_optional(self):
        with self.assertRaises(ValueError):
            empirical_block_law((0, 1, 0), (2,), 2, 2)
        for retained in ((), (0, 0), (-1,), (12,), (True,)):
            with self.subTest(retained=retained), self.assertRaises(ValueError):
                trimmed_entropy_budget((0,)*16, 12, 3, 1, retained, 2)
        with self.assertRaises(ValueError):
            trimmed_entropy_budget((0,)*16, 6, 4, 1, (0,), 2)
        with self.assertRaises(ValueError):
            trimmed_entropy_budget((0,)*16, 12, 3, 4, (0,), 2)


class PositiveTailCarryTransport(unittest.TestCase):
    def test_exact_factor_two_is_sharp_and_circle_wrap_is_retained(self):
        result = one_cell_collision_transport((Q(3, 16), Q(5, 16)),
                                              (Q(1, 8), 0), 4)
        self.assertEqual((result.before, result.after), (2, 4))
        wrap = one_cell_collision_transport((Q(15, 16), Q(1, 16)),
                                            (Q(1, 8), 0), 4)
        self.assertEqual((wrap.before, wrap.after), (2, 4))
        self.assertEqual(wrap.advancing_masses, ((3, Q(1, 2)),))
        self.assertEqual(wrap.target_cell_masses, ((0, Q(1)),))

    def test_weighted_split_matches_independent_cell_enumeration(self):
        for cells in (1, 2, 3, 5, 16):
            phases = tuple(Q(2*j+1, 2*cells) for j in range(cells))
            shifts = tuple(Q(j % 3, 3*cells) for j in range(cells))
            weights = tuple(Q(j+1, cells*(cells+1)//2) for j in range(cells))
            result = one_cell_collision_transport(phases, shifts, cells, weights)
            expected = {}
            for x, e, w in zip(phases, shifts, weights):
                target = int(cells*((x+e) % 1))
                expected[target] = expected.get(target, Q())+w
            self.assertEqual(dict(result.target_cell_masses), expected)
            self.assertLessEqual(result.after, 2*result.before)

    def test_two_cell_mutation_can_break_factor_two_and_is_rejected(self):
        # Three different cells can coalesce when the subcell condition is dropped.
        phases = (Q(0), Q(1, 3), Q(2, 3))
        shifts = (Q(2, 3), Q(1, 3), Q(0))
        self.assertEqual(3*sum((Q(1, 3)**2 for _ in phases), Q()), 1)
        self.assertEqual(len({(x+e) % 1 for x, e in zip(phases, shifts)}), 1)
        with self.assertRaises(ValueError):
            one_cell_collision_transport(phases, shifts, 3)

    def test_shift_lift_and_probability_domains_are_strict(self):
        for shift in (-Q(1, 10), Q(1, 4), Q(5, 4), 0.1, True):
            with self.subTest(shift=shift), self.assertRaises(ValueError):
                one_cell_collision_transport((0,), (shift,), 4)
        with self.assertRaises(ValueError):
            one_cell_collision_transport((0,), (0,), 4, (Q(1, 2),))

    def test_bbp_cutoff_is_minimal_and_uses_no_floating_square_root(self):
        for depth in range(33):
            cutoff = bbp_safe_start(depth)
            self.assertGreaterEqual((8*cutoff+1)*(8*cutoff+2), 16**depth)
            if cutoff:
                self.assertLess((8*cutoff-7)*(8*cutoff-6), 16**depth)
            retained = bbp_safe_retained_indices(max(0, cutoff-2), 7, depth)
            self.assertTrue(all((8*(max(0, cutoff-2)+n)+1)*
                                (8*(max(0, cutoff-2)+n)+2) >= 16**depth
                                for n in retained))
        self.assertEqual([bbp_safe_start(d) for d in range(5)], [0, 1, 2, 8, 32])
        self.assertEqual(bbp_safe_retained_indices(0, 3, 4), ())


if __name__ == "__main__":
    unittest.main()
