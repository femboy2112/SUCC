"""Exact controls for binary carry refinement and bounded odd-prime readout."""
import unittest
from fractions import Fraction as Q
from math import prod

from observational_succ.pi_binary_branch import (
    binary_branch_profile, centered, centered_carry, conditional_zero_upper,
    rational_residue, reconstruct_carry_law_mod_11_13, residue_marginal,
)
from observational_succ.pi_source_collision import bbp_forcing, bbp_states


class BinaryCarryTests(unittest.TestCase):
    def test_centered_half_open_convention(self):
        self.assertEqual(centered(Q(1, 2)), Q(-1, 2))
        self.assertEqual(centered(Q(-3, 2)), Q(-1, 2))
        self.assertEqual(centered(Q(7, 4)), Q(-1, 4))

    def test_inconsistent_carry_rejected(self):
        with self.assertRaises(ValueError):
            centered_carry(Q(1, 17), 0, Q(1, 17))

    def test_four_uniform_binary_fibers_on_odd_grid(self):
        # Multiplication by 16 sends these separated points into one cluster.
        xs = tuple(Q(16*j, 257) for j in range(16))
        row = binary_branch_profile(xs, (0,)*16, Q(15, 257))
        self.assertEqual(row.nested_counts, (256, 128, 64, 32, 16))
        self.assertEqual(row.conditional_retentions, (Q(1, 2),)*4)
        self.assertEqual(row.retention, Q(1, 16))

    def test_two_quaternary_halves_are_not_four_binary_halves(self):
        xs = tuple(Q(16*j, 257) for j in (0, 1, 4, 5))
        row = binary_branch_profile(xs, (0,)*4, Q(5, 257))
        self.assertEqual(row.nested_counts, (16, 8, 8, 4, 4))
        self.assertEqual(row.retention, Q(1, 4))

    def test_constant_array_retains_every_pair(self):
        row = binary_branch_profile((Q(1, 7),)*5, (Q(1, 13),)*5, Q(1, 100))
        self.assertEqual(row.nested_counts, (25,)*5)
        self.assertEqual(row.retention, 1)

    def test_actual_bbp_source_product_and_2adic_identity(self):
        for p in (41, 73, 97, 193):
            m = (p-1)//8
            source = bbp_states(4*m)
            indices = range(m+1, 4*m)
            xs = tuple(source[n] for n in indices)
            fs = tuple(bbp_forcing(n+1) for n in indices)
            ys = tuple(source[n+1] for n in indices)
            row = binary_branch_profile(xs, fs, Q(1, 16), successor=ys)
            self.assertEqual(prod(row.conditional_retentions), row.retention)
            self.assertGreaterEqual(row.zero_pairs, len(xs))
            self.assertEqual(row.residue_counts(9)[0], row.zero_pairs)
            self.assertEqual(row.residue_counts(11)[0], row.zero_pairs)
            self.assertEqual(row.residue_counts(13)[0], row.zero_pairs)
            for s, t in ((0, 0), (0, len(xs)-1), (1, len(xs)//2)):
                d = centered(xs[t]-xs[s])
                e = fs[t]-fs[s]
                after = centered(ys[t]-ys[s])
                kappa = centered_carry(d, e, after)
                self.assertEqual(kappa % 16, rational_residue(e-after, 16))

    def test_supplied_wrong_successor_rejected(self):
        with self.assertRaises(ValueError):
            binary_branch_profile((Q(1, 17),), (0,), 0, successor=(0,))

    def test_modular_zero_identification_boundary(self):
        for kappa in range(-8, 9):
            self.assertEqual(kappa == 0, kappa % 9 == 0)
            self.assertEqual(kappa == 0, kappa % 15 == 0)
        self.assertNotEqual(3 == 0, 3 % 3 == 0)
        self.assertNotEqual(8 == 0, 8 % 8 == 0)

    def test_four_conditional_halves_allowance(self):
        self.assertEqual(conditional_zero_upper(1600, (Q(1, 2),)*4,
                                                (3,)*4, 10),
                         Q(1600, 16)+Q(15, 8)*3*10)

    def test_four_marginal_halves_need_not_multiply(self):
        # Four identical fair events have intersection 1/2, not 1/16.
        weights = {(0, 0, 0, 0): Q(1, 2), (1, 1, 1, 1): Q(1, 2)}
        for bit in range(4):
            self.assertEqual(sum(w for bits, w in weights.items()
                                 if bits[bit] == 0), Q(1, 2))
        self.assertEqual(weights[(0, 0, 0, 0)], Q(1, 2))

    def test_invalid_domains(self):
        for radix in (0, 1, 3, 12, True):
            with self.assertRaises(ValueError):
                binary_branch_profile((0,), (0,), 0, radix=radix)
        for radius in (-1, Q(1, 3), 0.1):
            with self.assertRaises(ValueError):
                binary_branch_profile((0,), (0,), radius)
        with self.assertRaises(ValueError):
            binary_branch_profile((0, 0), (0, Q(1, 4)), Q(1, 4))
        with self.assertRaises(ValueError):
            rational_residue(Q(1, 3), 9)
        with self.assertRaises(ValueError):
            conditional_zero_upper(1, (Q(3, 2),), (0,), 1)


class BoundedCarryTomographyTests(unittest.TestCase):
    def test_separate_mod3_mod5_marginals_do_not_identify_zero(self):
        # This exact rectangle has zero projection on both residue rings.
        perturbation = {0: Q(1), 3: Q(-1), 5: Q(-1), 8: Q(1)}
        self.assertEqual(residue_marginal(perturbation, 3), (Q(0),)*3)
        self.assertEqual(residue_marginal(perturbation, 5), (Q(0),)*5)
        baseline = {k: Q(1, 17) for k in range(-8, 9)}
        changed = {k: baseline[k]+Q(1, 17)*perturbation.get(k, 0)
                   for k in range(-8, 9)}
        self.assertGreaterEqual(min(changed.values()), 0)
        self.assertEqual(sum(changed.values()), 1)
        self.assertNotEqual(baseline[0], changed[0])
        for modulus in (3, 5):
            self.assertEqual(residue_marginal(baseline, modulus),
                             residue_marginal(changed, modulus))

    def test_all_basis_laws_reconstructed(self):
        for k in range(-8, 9):
            law = {k: 1}
            restored = reconstruct_carry_law_mod_11_13(
                residue_marginal(law, 11), residue_marginal(law, 13))
            self.assertEqual(restored, tuple(Q(j == k) for j in range(-8, 9)))

    def test_authentic_source_carry_counts_reconstructed(self):
        source = bbp_states(48)
        xs, fs = source[13:48], tuple(bbp_forcing(n+1) for n in range(13, 48))
        row = binary_branch_profile(xs, fs, Q(1, 16), successor=source[14:49])
        restored = reconstruct_carry_law_mod_11_13(row.residue_counts(11),
                                                 row.residue_counts(13))
        expected = dict(row.signed_counts)
        self.assertEqual(restored, tuple(Q(expected.get(k, 0))
                                        for k in range(-8, 9)))

    def test_sharp_three_sup_norm_symmetric_witness(self):
        # Exact witness replaces the exploratory floating linear program.
        positive_half = {1: -1, 3: 1, 4: -1, 5: 3, 6: -2, 7: 2, 8: -2}
        v = {k: Q(positive_half.get(abs(k), 0)) for k in range(-8, 9)}
        self.assertEqual(sum(v.values()), 0)
        self.assertEqual(max(map(abs, v.values())), 3)
        for modulus in (11, 13):
            self.assertEqual(max(map(abs, residue_marginal(v, modulus))), 1)
        baseline = {k: Q(1, 17) for k in range(-8, 9)}
        changed = {k: baseline[k]+Q(1, 34)*v[k] for k in range(-8, 9)}
        self.assertGreaterEqual(min(changed.values()), 0)
        self.assertEqual(sum(changed.values()), 1)
        self.assertEqual(reconstruct_carry_law_mod_11_13(
            residue_marginal(changed, 11), residue_marginal(changed, 13)),
            tuple(changed[k] for k in range(-8, 9)))

    def test_uniform_odd_marginals_incompatible(self):
        # Their singleton zero fibers would force c_0=1/11 and c_0=1/13.
        with self.assertRaises(ValueError):
            reconstruct_carry_law_mod_11_13((Q(1, 11),)*11, (Q(1, 13),)*13)

    def test_haar_inverse_branch_projection_is_not_odd_haar(self):
        law = {k: Q(1, 16) for k in range(-7, 8)}
        law[-8] = law[8] = Q(1, 32)
        for modulus in (9, 11, 13):
            marginal = residue_marginal(law, modulus)
            self.assertEqual(marginal[0], Q(1, 16))
            self.assertNotEqual(marginal[0], Q(1, modulus))
        restored = reconstruct_carry_law_mod_11_13(
            residue_marginal(law, 11), residue_marginal(law, 13))
        self.assertEqual(restored, tuple(law[k] for k in range(-8, 9)))

    def test_bad_shapes_and_inconsistent_observations(self):
        with self.assertRaises(ValueError):
            reconstruct_carry_law_mod_11_13((0,)*10, (0,)*13)
        with self.assertRaises(ValueError):
            reconstruct_carry_law_mod_11_13((1,)+(0,)*10, (0,)*13)


if __name__ == "__main__":
    unittest.main()
