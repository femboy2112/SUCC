"""Exact reproduction of every Gemini Crucible refutation (Part II)."""
import unittest

import sympy as sp

from observational_succ.gemini_crucible import (
    claim_1_1_restricted_coercivity,
    claim_1_2_sufficient_not_necessary,
    claim_1_3_memory_debt,
    claim_1_4_data_processing,
    claim_1_5_prime_clock,
    claim_1_6_prime_weight_asymptotic,
    claim_1_7_float_diagnostic,
    claim_1_8_master_identity,
    derive_primitive_valuation_law,
    merging_channel,
    primitive_valuation_law,
    ris_local_moment,
    run_full_crucible,
    spectral_leakage_min_norm,
    total_variation,
)
from observational_succ.quantitative_rigidity import Rat


class Test_1_1(unittest.TestCase):
    def test_refuted_with_exact_negative_vector(self):
        v = claim_1_1_restricted_coercivity()
        self.assertEqual(v.status, "REFUTED")
        self.assertEqual(v.witness["true schur A-BD^-1B^*"], Rat(-62, 19))
        self.assertEqual(v.witness["surrogate A-kappa^-1 BB^*"], 1)   # surrogate says >0
        self.assertEqual(v.witness["v^T M v"], Rat(-62, 19))          # truth says <0


class Test_1_2(unittest.TestCase):
    def test_misleading(self):
        v = claim_1_2_sufficient_not_necessary()
        self.assertEqual(v.status, "MISLEADING")
        self.assertEqual(v.witness["surrogate"], -3)
        self.assertEqual(v.witness["true_schur"], Rat(24, 25))


class Test_1_3(unittest.TestCase):
    def test_lift_nonunique_and_leakage_vacuous(self):
        v = claim_1_3_memory_debt()
        self.assertEqual(v.status, "REFUTED")
        self.assertEqual(v.witness["source_lifts_of_ooo"], 8)
        gamma = sp.Symbol("gamma", positive=True)
        self.assertEqual(sp.simplify(spectral_leakage_min_norm(gamma, 4, 2) - gamma), 0)
        self.assertEqual(sp.simplify(spectral_leakage_min_norm(gamma, 2, 1) - gamma), 0)


class Test_1_4(unittest.TestCase):
    def test_tv_no_strict_contraction(self):
        v = claim_1_4_data_processing()
        self.assertEqual(v.status, "REFUTED")
        self.assertEqual(v.witness["TV_in"], Rat(1, 2))
        self.assertEqual(v.witness["TV_out"], Rat(1, 2))
        self.assertNotEqual(v.witness["ker_component"], 0)

    def test_tv_and_channel_directly(self):
        p = [Rat(2, 5), Rat(1, 10), Rat(1, 2)]
        q = [Rat(0), Rat(0), Rat(1)]
        self.assertEqual(total_variation(p, q), Rat(1, 2))
        self.assertEqual(merging_channel(p), [Rat(1, 2), Rat(1, 2)])
        self.assertEqual(merging_channel(q), [Rat(0), Rat(1)])
        self.assertEqual(total_variation(merging_channel(p), merging_channel(q)), Rat(1, 2))

    def test_strict_contraction_when_fiber_cancels(self):
        # positive control: a difference that DOES cancel in a merged fiber contracts
        p = [Rat(1, 2), Rat(1, 2), Rat(0)]
        q = [Rat(0), Rat(0), Rat(1)]
        tv_in = total_variation(p, q)                 # 1
        tv_out = total_variation(merging_channel(p), merging_channel(q))  # (1,0)vs(0,1)->1
        # here fibers do not cancel either; construct genuine cancellation:
        p2 = [Rat(3, 4), Rat(0), Rat(1, 4)]
        q2 = [Rat(0), Rat(3, 4), Rat(1, 4)]
        self.assertEqual(total_variation(p2, q2), Rat(3, 4))
        # merged fiber {1,2}: (3/4) vs (3/4) -> cancels fully, coord 3 equal
        self.assertEqual(total_variation(merging_channel(p2), merging_channel(q2)), 0)


class Test_1_5(unittest.TestCase):
    def test_derived_matches_corrected_law(self):
        p, k, derived = derive_primitive_valuation_law()
        self.assertEqual(sp.simplify(derived - primitive_valuation_law(p, k)), 0)

    def test_normalization_and_p2(self):
        v = claim_1_5_prime_clock()
        self.assertEqual(v.status, "REFUTED")
        norms = v.witness["normalization_at_primes"]
        self.assertEqual(norms[2], 1)           # 3/(2+1) = 1: always one even entry
        self.assertEqual(norms[3], Rat(3, 4))
        self.assertEqual(norms[5], Rat(3, 6))
        self.assertEqual(v.witness["at_p=2"], 1)

    def test_ris_local_moment_converges_and_exact(self):
        # at t=0 the local moment is the total probability = 1 (exact, concrete prime)
        self.assertEqual(ris_local_moment(sp.Integer(3), 0), 1)
        self.assertEqual(ris_local_moment(sp.Integer(5), 0), 1)
        # t=1/2 < 1 converges to an exact algebraic value (carries sqrt(3), not
        # rational); t>=1 would diverge.
        m = ris_local_moment(sp.Integer(3), Rat(1, 2))
        self.assertTrue(m.is_finite)
        self.assertTrue(float(m.evalf()) > 1)   # > 1 since ris factor >= 1


class Test_1_6(unittest.TestCase):
    def test_misclassified_rh_strength(self):
        v = claim_1_6_prime_weight_asymptotic()
        self.assertEqual(v.status, "MISCLASSIFIED")
        self.assertIn("RH", v.witness["strength"])


class Test_1_7(unittest.TestCase):
    def test_float_diagnostic_unsound(self):
        v = claim_1_7_float_diagnostic()
        self.assertEqual(v.status, "REFUTED")
        self.assertTrue(v.witness["naive_rigid"])
        self.assertFalse(v.witness["truly_psd"])
        self.assertFalse(v.witness["high_block_psd"])


class Test_1_8(unittest.TestCase):
    def test_not_adopted_defects_not_additive_and_gap_vanishes(self):
        v = claim_1_8_master_identity()
        self.assertEqual(v.status, "NOT_ADOPTED")
        self.assertFalse(v.witness["defect_additivity"]["additivity_holds_when_coupled"])
        prof = v.witness["gap_profile"]
        self.assertEqual(prof[0][0], 2)
        # last block min eigenvalue strictly smaller than the first -> no uniform gap
        self.assertTrue(sp.Rational(prof[-1][1]) < sp.Rational(prof[0][1]))


class TestWholeCrucible(unittest.TestCase):
    def test_all_eight_verdicts_present_and_valid(self):
        verdicts = run_full_crucible()
        self.assertEqual(len(verdicts), 8)
        ids = {v.claim_id for v in verdicts}
        self.assertEqual(ids, {"1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8"})
        # the false restricted-coercivity result is explicitly REFUTED
        by_id = {v.claim_id: v for v in verdicts}
        self.assertEqual(by_id["1.1"].status, "REFUTED")
        # the master identity is NOT promoted
        self.assertEqual(by_id["1.8"].status, "NOT_ADOPTED")
        for v in verdicts:
            self.assertTrue(v.as_record()["replacement"])  # every claim has a fix


if __name__ == "__main__":
    unittest.main()
