"""Independent finite reconstruction and source-correlated hostile controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.beck_chevalley_source import finite_map
from observational_succ.lambda_source_duality import Cyclo16, original_history
from observational_succ.seinfeld_succ import rational_rank
from observational_succ import seinfeld_disintegration as sd


def direct_fourier(row, frequency):
    """Independent polynomial evaluation modulo z**8+1."""
    answer = [Q()] * 8
    for j, weight in enumerate(row):
        exponent = frequency * j % 16
        answer[exponent % 8] += weight if exponent < 8 else -weight
    return Cyclo16(tuple(answer))


def pushforward(mapping, weights):
    return tuple(sum((weights[i] for i, (_, target) in enumerate(mapping.pairs)
                      if target == y), Q()) for y in mapping.codomain)


class FiniteDisintegrationTests(unittest.TestCase):
    def setUp(self):
        self.mapping = finite_map(("a0", "a1", "a2", "b0", "b1"),
                                  ("A", "B", "empty"),
                                  lambda x: x[0].upper())
        self.weights = (Q(1, 4), Q(1, 8), Q(1, 8), Q(1, 6), Q(1, 3))

    def test_unequal_fibres_reconstruct_with_empty_codomain_point(self):
        law = sd.disintegrate_law(self.mapping, self.weights, source_id="unequal")
        self.assertEqual(law.marginal, (Q(1, 2), Q(1, 2), Q()))
        self.assertEqual(law.uniform_lift(), (Q(1, 6),) * 3 + (Q(1, 4),) * 2)
        self.assertEqual(law.reconstruct(), self.weights)
        self.assertEqual(law.null_dimension, 3)
        self.assertEqual(pushforward(self.mapping, law.residual), (0, 0, 0))

    def test_null_form_is_zero_on_pullbacks_but_not_all_observables(self):
        law = sd.disintegrate_law(self.mapping, self.weights, source_id="labelled")
        witness = law.null_witness()
        self.assertTrue(witness.coefficients())
        source_values = {"A": Q(13, 7), "B": Q(-11, 3), "empty": Q(999)}
        pullback = {key: source_values[y]
                    for key, (_, y) in zip(law.generator_labels, self.mapping.pairs)}
        self.assertEqual(witness.evaluate(pullback), 0)
        indicator = tuple(Q(int(i == 0)) for i in range(5))
        values = dict(zip(law.generator_labels, indicator))
        self.assertEqual(witness.evaluate(values), Q(1, 12))
        split = law.observable(indicator)
        self.assertEqual((split.total, split.uniform_lift, split.null_pairing),
                         (Q(1, 4), Q(1, 6), Q(1, 12)))

    def test_exact_marginal_only_obstruction_returns_probability_receipt(self):
        f = (0, 3, 4, -5, -5)
        alias = sd.marginal_obstruction(self.mapping, f)
        self.assertIsNotNone(alias)
        self.assertEqual(sum(alias.left), 1)
        self.assertEqual(sum(alias.right), 1)
        self.assertEqual(pushforward(self.mapping, alias.left),
                         pushforward(self.mapping, alias.right))
        self.assertNotEqual(alias.left_expectation, alias.right_expectation)
        self.assertEqual(alias.left_expectation, sum(x*y for x, y in zip(alias.left, f)))
        self.assertIsNone(sd.marginal_obstruction(self.mapping, (3, 3, 3, -5, -5)))

    def test_probability_and_null_constraints_fail_closed(self):
        for weights in ((1, 0, 0, 0, 1), (Q(-1), Q(2), 0, 0, 0),
                        (1.0, 0, 0, 0, 0), (True, 0, 0, 0, 0)):
            with self.assertRaises(ValueError):
                sd.disintegrate_law(self.mapping, weights, source_id="bad")
        for marginal, residual in (
                ((Q(1, 2), Q(1, 2), Q()), (Q(1), Q(), Q(), Q(), Q())),
                ((Q(), Q(), Q(1)), (Q(),) * 5),
                ((Q(1, 2), Q(1, 2), Q()), (Q(1), Q(-1), Q(), Q(), Q()))):
            with self.assertRaises(ValueError):
                sd.FiberDisintegration(self.mapping, "bad", marginal, residual)
        with self.assertRaises(ValueError):
            sd.disintegrate_law(self.mapping, self.weights, source_id="")


class RationalFourierResolutionTests(unittest.TestCase):
    def test_all_basis_vectors_and_signed_rational_holdouts_roundtrip(self):
        rows = [tuple(Q(int(j == k)) for j in range(16)) for k in range(16)]
        rows += [tuple(Q((-1)**j * (3*j*j+7*j+2), j+5) for j in range(16)),
                 (Q(1, 16),) * 16, (Q(),) * 16]
        for row in rows:
            packet = sd.DyadicFourier.from_weights(row)
            self.assertEqual(packet.reconstruct(), row)
            self.assertEqual(len(packet.coordinates), 15)
            self.assertEqual(sd.DyadicFourier.from_coordinates(
                packet.mass, packet.coordinates), packet)
            for h in (-33, -17, -12, -8, -1, *range(17), 25, 32):
                self.assertEqual(packet.character(h), direct_fourier(row, h))

    def test_exact_linear_dimension_is_sixteen_with_mass_and_fifteen_without(self):
        columns = []
        for j in range(16):
            row = tuple(Q(int(k == j)) for k in range(16))
            packet = sd.DyadicFourier.from_weights(row)
            columns.append((packet.mass,) + packet.coordinates)
        matrix = tuple(zip(*columns))
        self.assertEqual(rational_rank(matrix), 16)
        self.assertEqual(rational_rank(matrix[1:]), 15)

    def test_omitting_any_stratum_has_strictly_positive_aliases(self):
        for omitted in sd.DYADIC_MODES:
            # Period 16/h; opposite halves survive only the h stratum.
            half = 8 // omitted
            direction = tuple(Q(1 if j % (2*half) == 0 else
                                -1 if j % (2*half) == half else 0)
                              for j in range(16))
            plus = tuple(Q(1, 16) + x/32 for x in direction)
            minus = tuple(Q(1, 16) - x/32 for x in direction)
            self.assertGreater(min(plus), 0)
            self.assertGreater(min(minus), 0)
            p, m = (sd.DyadicFourier.from_weights(row) for row in (plus, minus))
            self.assertEqual(p.mass, m.mass)
            for h in sd.DYADIC_MODES:
                if h == omitted:
                    self.assertNotEqual(p.character(h), m.character(h))
                else:
                    self.assertEqual(p.character(h), m.character(h))

    def test_identical_all_mode_energies_do_not_recover_selected_phases(self):
        packets = [sd.DyadicFourier.from_weights(
            tuple(Q(int(j == k)) for j in range(16))) for k in range(16)]
        for packet in packets:
            self.assertEqual(packet.stratum_energies(), (8, 4, 2, 1))
        self.assertEqual(len({p.character(1) for p in packets}), 16)
        uniform = sd.DyadicFourier.from_weights((Q(1, 16),) * 16)
        self.assertEqual(uniform.stratum_energies(), (0, 0, 0, 0))
        signed = tuple(Q(j*j-4*j-3, j+3) for j in range(16))
        p = sd.DyadicFourier.from_weights(signed)
        self.assertEqual(sum(p.stratum_energies()),
                         16*sum(x*x for x in signed)-sum(signed)**2)

    def test_subfield_and_exact_type_gates(self):
        zero = Cyclo16.zero()
        for bad in ((zero,) * 3, (zero, Cyclo16.zeta(1), zero, zero),
                    (zero, zero, Cyclo16.zeta(2), zero),
                    (zero, zero, zero, Cyclo16.zeta(4))):
            with self.assertRaises(ValueError):
                sd.DyadicFourier(Q(1), bad)
        for bad in ((Q(),) * 14, (0.0,) * 15, (True,) * 15):
            with self.assertRaises(ValueError):
                sd.DyadicFourier.from_coordinates(1, bad)


class SourceLabelAndOddSelectionTests(unittest.TestCase):
    def test_joint_coupling_cannot_be_replaced_by_the_two_marginals(self):
        row0 = tuple(Q(1, 2) if j == 0 else Q() for j in range(16))
        row8 = tuple(Q(1, 2) if j == 8 else Q() for j in range(16))
        p = sd.branch_law(("alpha", "beta"), (row0, row8), source_id="direct")
        q = sd.branch_law(("alpha", "beta"), (row8, row0), source_id="swapped")
        self.assertEqual(p.marginal, q.marginal)
        for h in range(16):
            self.assertEqual(sd.labelled_character_pairing(p, h, (1, 1)),
                             sd.labelled_character_pairing(q, h, (1, 1)))
        self.assertEqual(sd.labelled_character_pairing(p, 1, (1, -1)), Cyclo16.one())
        self.assertEqual(sd.labelled_character_pairing(q, 1, (1, -1)), -Cyclo16.one())

    def test_authentic_zero_seed_source_rows_and_literal_source_witnesses(self):
        states = original_history(47)
        law = sd.authentic_branch_law(states)
        packets = sd.branch_channels(law)
        self.assertEqual(len(packets), 46)
        self.assertEqual(law.marginal, (Q(1, 46),) * 46)
        self.assertEqual(law.null_dimension, 15*46)
        previous = Q()
        for n, state in enumerate(states, 1):
            grouped = Q(4, 8*n-7)-Q(1, 8*n-3)-Q(3*n-1, (2*n-1)*(4*n-1))
            self.assertEqual(state, 16*previous+grouped)
            previous = state
        for witness, packet in packets:
            self.assertEqual(witness.current, states[witness.source_index-1] % 1)
            self.assertEqual(witness.successor, states[witness.source_index] % 1)
            self.assertEqual(witness.current, (witness.digit+witness.remainder)/16)
            self.assertEqual(witness.current.denominator % 2, 1)
            for h in sd.DYADIC_MODES:
                self.assertEqual(packet.character(h), Cyclo16.zeta(h*witness.digit)*Q(1, 46))
        self.assertEqual(pushforward(law.projection, law.residual), (Q(),) * 46)

    def test_source_time_swap_preserves_all_marginals_but_fails_odd_passport(self):
        p = sd.authentic_branch_law(original_history(3))
        labels = p.projection.codomain
        self.assertNotEqual(labels[0].digit, labels[1].digit)
        swapped = (labels[1].digit, labels[0].digit)
        rows = tuple(tuple(Q(1, 2) if j == digit else Q() for j in range(16))
                     for digit in swapped)
        q = sd.branch_law(labels, rows, source_id="explicitly-changed-selectors")
        self.assertEqual(p.marginal, q.marginal)
        for h in range(16):
            self.assertEqual(sd.labelled_character_pairing(p, h, (1, 1)),
                             sd.labelled_character_pairing(q, h, (1, 1)))
        source_pairing = sd.labelled_character_pairing(p, 1, (1, -1))
        self.assertNotEqual(source_pairing, Cyclo16.zero())
        self.assertEqual(sd.labelled_character_pairing(q, 1, (1, -1)), -source_pairing)
        for witness, digit in zip(labels, swapped):
            ghost = (digit+witness.remainder)/16
            self.assertEqual((16*ghost+witness.forcing) % 1, witness.successor)
            self.assertEqual(ghost.denominator % 2, 0)

    def test_odd_selector_mode_tag_invariant_under_conductor_enlargement(self):
        for q in (1, 3, 5, 17, 31, 97):
            for a in range(q):
                tail = Q(a, q)
                for h in (0, 1, 2, 4, 8, -6, 17):
                    tag = sd.odd_selector_tag(tail, h)
                    for conductor in (q, 5*q, 17*q):
                        enlarged = sd.odd_selector_tag(tail, h, conductor=conductor)
                        self.assertEqual(enlarged.digit, tag.digit)
                        self.assertEqual(enlarged.character_residue, tag.character_residue)
                    self.assertEqual(Cyclo16.zeta(h*tag.digit),
                                     Cyclo16.zeta(h*tag.character_residue))

    def test_deterministic_character_tag_has_exactly_the_stated_classes(self):
        from math import gcd
        for h in (0, 1, 2, 3, 4, 6, 8, 12, 16):
            order = 16//gcd(16, h)
            for j in range(16):
                for k in range(16):
                    self.assertEqual(Cyclo16.zeta(h*j) == Cyclo16.zeta(h*k),
                                     j % order == k % order)
        self.assertNotEqual(sd.odd_selector_tag(Q(1, 3)).digit,
                            sd.odd_selector_tag(Q(1, 5)).digit)

    def test_authentication_and_source_domain_mutations_fail(self):
        original = original_history(7)
        shifted = tuple(u+Q(16**n, 3) for n, u in enumerate(original, 1))
        for altered in (shifted, original[:-1]+(original[-1]+1,), original[:1], ()):
            with self.assertRaises(ValueError):
                sd.authentic_branch_law(altered)
        for tail, conductor in ((Q(1, 2), None), (Q(2, 15), 10),
                                (Q(2, 15), 17), (Q(2, 15), True)):
            with self.assertRaises(ValueError):
                sd.odd_selector_tag(tail, conductor=conductor)
        for labels, rows in ((("a", "a"), ((1,)+(0,)*15,)*2),
                             (("a",), ((1,)+(0,)*14,)),
                             (("a",), ((1.0,)+(0,)*15,))):
            with self.assertRaises(ValueError):
                sd.branch_law(labels, rows, source_id="bad")

    def test_status_preserves_the_cancellation_boundary(self):
        flags = sd.status_flags()
        self.assertTrue(flags["finite_labelled_reconstruction"])
        self.assertEqual(flags["rational_null_coordinates_per_branch_fibre"], 15)
        self.assertFalse(flags["averaging_alone_invertible"])
        self.assertFalse(flags["selected_weyl_saving_proved"])
        self.assertFalse(flags["pi_base16_normality_proved"])


if __name__ == "__main__":
    unittest.main()
