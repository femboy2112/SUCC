"""Exact source, hostile transport, and phase-sensitive inverse controls."""
from fractions import Fraction as Q
from hashlib import sha1
from pathlib import Path
import unittest

from observational_succ import source_faithful_weil as sfw
from observational_succ import source_weil_hierarchy as src
from observational_succ.tate_suzuki_shorting import (
    TateSourcePassport, ShortingContractError, gammas_from_prime_mutation,
    PINNED_TAPE,
)
from observational_succ.tate_weil_distribution import TateWeilSource


class LogAddressSynthesis(unittest.TestCase):
    def test_independent_interval_intersection_box(self):
        # Overlap of [0,1] and [log2,1+log2]; no fitted normalization.
        g = sfw.box_log_gram(1, 2, 0)
        log2 = src.log2_iv()
        self.assertLessEqual(g.lo, 1-log2.lo)
        self.assertGreaterEqual(g.hi, 1-log2.hi)
        self.assertGreater(g.lo, Q(3, 10))

    def test_disjoint_box_null_control(self):
        # log4>1, so these source atoms have disjoint supports.
        g = sfw.box_log_gram(1, 4, 0)
        self.assertEqual((g.lo, g.hi), (0, 0))

    def test_unit_block_growth_fresh_regimes(self):
        for N in (1, 4, 16, 31):
            with self.subTest(N=N):
                energy = sfw.box_log_energy({n: 1 for n in range(N, 2*N+1)}, 0)
                self.assertGreaterEqual(energy.lo/(N+1),
                                        sfw.unweighted_cluster_lower(N))
        # Reject the false claim that unweighted J is a contraction.
        self.assertGreater(sfw.unweighted_cluster_lower(16), 1)

    def test_half_density_uniform_global_bound_controls(self):
        bound = sfw.compact_seed_synthesis_bound(1, 1)
        for coefficients in ({1: 1}, {n: 1 for n in range(13, 32)},
                             {1: 1, 2: -3, 3: 2, 11: -1, 97: 4}):
            energy = sfw.box_log_energy(coefficients)
            norm2 = sum(a*a for a in coefficients.values())
            self.assertLess(energy.hi, bound*norm2)
            self.assertGreater(energy.hi, 0)

    def test_weighted_covariance_gram_withheld_primes(self):
        for p in (2, 3, 5, 7):
            for n, m in ((1, 2), (7, 11), (31, 37)):
                a = sfw.box_log_gram(p*n, p*m)
                b = sfw.box_log_gram(n, m)/p
                self.assertLessEqual(a.lo, b.hi)
                self.assertLessEqual(b.lo, a.hi)
                # A unitary covariance law would wrongly omit 1/p.
                original = sfw.box_log_gram(n, m)
                if original.lo:
                    self.assertLess(a.hi, original.lo)

    def test_weighting_is_not_isometry(self):
        a = sfw.box_log_gram(7, 7)
        self.assertLessEqual(a.lo, Q(1, 7))
        self.assertGreaterEqual(a.hi, Q(1, 7))
        self.assertLess(a.hi, 1)

    def test_sharpening_distribution_cost_diverges(self):
        for width in (Q(1), Q(1, 4), Q(1, 16), Q(1, 64)):
            gram = sfw.box_log_gram(1, 1, width=width)
            self.assertLessEqual(gram.lo, 1/width)
            self.assertGreaterEqual(gram.hi, 1/width)
            upper = sfw.compact_seed_synthesis_bound(width, 1/width)
            self.assertEqual(upper/(1/width), 1+width)
        with self.assertRaises(ValueError):
            sfw.box_log_gram(1, 1, width=0)

    def test_subcritical_and_supercritical_finite_oracles(self):
        for alpha in (0, Q(1, 2), 1):
            energy = sfw.box_log_energy({2: 1, 3: -1}, alpha)
            self.assertGreater(energy.lo, 0)
        self.assertLess(sfw.box_log_energy({4: 1}, 1).hi,
                        sfw.box_log_energy({4: 1}, Q(1, 2)).lo)

    def test_strict_types_and_domains(self):
        for bad in (0, -1, True, 2.0):
            with self.assertRaises(ValueError):
                sfw.box_log_gram(bad, 1)
        with self.assertRaises(ValueError):
            sfw.box_log_gram(1, 1, Q(1, 3))
        with self.assertRaises(ValueError):
            sfw.box_log_energy({1: 0.5})
        with self.assertRaises(ValueError):
            sfw.compact_seed_synthesis_bound(0, 1)


class ExactInverseDefects(unittest.TestCase):
    def test_inverse_split_independent_gaussian_elimination(self):
        for e, f, g, b, c in ((2, 1, 2, 1, -1), (3, 2, 7, 5, 4),
                              (Q(7, 3), Q(1, 7), 2, Q(-1, 5), 3)):
            values = list(map(Q, (e, f, g, b, c)))
            e, f, g, b, c = values
            x2 = (c-f*b/e)/(g-f*f/e)
            x1 = (b-f*x2)/e
            row = sfw.high_split_inverse(e, f, g, b, c)
            self.assertEqual(row["total"], b*x1+c*x2)
            self.assertEqual(row["total"], row["visible"]+row["defect"])

    def test_zero_hidden_coupling_still_has_defect(self):
        result = sfw.high_split_inverse(2, 1, 2, 1, 0)
        self.assertEqual(result["defect"], Q(1, 6))
        self.assertGreater(result["total"], result["visible"])

    def test_decoupled_null_control(self):
        result = sfw.high_split_inverse(2, 0, 3, 1, 0)
        self.assertEqual(result["defect"], 0)

    def test_alignment_annihilates_defect(self):
        result = sfw.high_split_inverse(2, 1, 3, 4, 2)
        self.assertEqual(result["defect"], 0)

    def test_same_norms_can_give_opposite_schur_signs(self):
        result = sfw.phase_blind_schur_counterexample()
        self.assertEqual(result["plus_S"], Q(1, 3))
        self.assertEqual(result["minus_S"], -1)
        self.assertFalse(result["original_Weil_counterexample"])

    def test_source_unitary_flip_preserves_correction(self):
        # Conjugate high by diag(1,-1): BOTH f and c must change sign.
        a = sfw.high_split_inverse(2, 1, 2, 1, 1)
        b = sfw.high_split_inverse(2, -1, 2, 1, -1)
        self.assertEqual(a["total"], b["total"])
        wrong = sfw.high_split_inverse(2, -1, 2, 1, 1)
        self.assertNotEqual(a["total"], wrong["total"])

    def test_positive_definite_premise_cannot_be_dropped(self):
        for e, f, g in ((0, 0, 1), (1, 1, 1), (1, 2, 1)):
            with self.assertRaises(ValueError):
                sfw.high_split_inverse(e, f, g, 1, 1)


class OriginalSourceBoundary(unittest.TestCase):
    def test_actual_byte_hash_and_prime_tape(self):
        result = sfw.source_fingerprint()
        data = Path(src.__file__).read_bytes()
        independent = sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        self.assertEqual(independent, result["source_git_blob"])
        self.assertEqual(independent, "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertFalse(result["new_S4_sign_bound"])
        self.assertFalse(result["RH_proved"])

    def test_genuine_arithmetic_atom_cannot_be_positive_norm_square(self):
        result = sfw.genuine_prime_two_negative_atom()
        self.assertLess(result["atom_upper"], 0)
        self.assertGreater(result["autocorrelation_lower"], 0)
        self.assertFalse(result["completed_Weil_sign_inferred"])

    def test_all_completion_mutants_register_signed_change(self):
        differences = sfw.completion_mutation_differences()
        self.assertEqual(len(differences), 7)
        for label, interval in differences.items():
            with self.subTest(label=label):
                self.assertTrue(interval.lo > 0 or interval.hi < 0)
        self.assertLess(differences["missing_prime_power_4"].hi, 0)
        self.assertGreater(differences["fake_composite_6"].lo, 0)

    def test_outside_active_support_is_genuine_null(self):
        differences = sfw.completion_mutation_differences(Q(1, 2))
        for label in ("fake_composite_6", "missing_prime_power_4",
                      "non_euler_double_prime_2", "wrong_half_density_prime_2"):
            self.assertEqual((differences[label].lo, differences[label].hi), (0, 0))

    def test_primitive_and_repeated_power_source_mutations(self):
        for tape in (PINNED_TAPE+((6, 6),),
                     tuple(row for row in PINNED_TAPE if row[0] != 4),
                     tuple((n, 4 if n == 4 else p) for n, p in PINNED_TAPE)):
            with self.assertRaises(ShortingContractError):
                gammas_from_prime_mutation(tape)

    def test_regularized_tape_independent_prime_power_oracle(self):
        from observational_succ.suzuki_first_prime import prime_power
        tape = sfw.regularized_prime_tape(125)
        by_n = {row["n"]: row for row in tape}
        for n in range(2, 126):
            expected = prime_power(n)
            self.assertEqual(n in by_n, expected is not None)
            if expected:
                row = by_n[n]
                self.assertEqual((row["prime"], row["power"]), expected)
                self.assertEqual(row["prime"]*row["source_input"], n)
        self.assertNotIn(6, by_n)
        # Primitive log(2), not composite log(4), at the repeated prime power.
        authentic = by_n[4]["weight"]
        counterfeit = src.log_iv(4)*src.sqrt_inverse(4)
        self.assertLess(authentic.hi, counterfeit.lo)

    def test_gamma_and_conductor_contracts_reject_mutations(self):
        for kwargs in ({"real_gamma_count": 2}, {"character_parity": 1},
                       {"gaussian_scale": Q(2)}, {"conductor": 4},
                       {"half_density": Q(1)}):
            with self.assertRaises(ShortingContractError):
                TateSourcePassport(**kwargs)

    def test_both_poles_and_root_number_preserved(self):
        original = TateWeilSource()
        args = dict(conductor=1, parity=0, half_density=Q(1, 2),
                    pole_multiplicity=1, root_number=1)
        self.assertTrue(original.require_normalization(**args))
        for key, value in (("pole_multiplicity", 0), ("root_number", -1)):
            with self.assertRaises(ValueError):
                original.require_normalization(**(args | {key: value}))


if __name__ == "__main__":
    unittest.main()
