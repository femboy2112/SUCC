"""True zeta/Suzuki source interval margins and ordinal finite-sign search."""
import unittest
from fractions import Fraction as F

from observational_succ.ordinal_suzuki_source_margins import (
    OrdinalSourceSignError,authentic_suzuki_ordinal_sign_search,
    finite_strict_sign_semidecision_theorem,original_zero_margin_stuttering_counterexample,
)
from observational_succ.suzuki_legendre_source import _pinned_source
from observational_succ.ordinal_ranked_succ import ordinal_lex_counters,ZERO


class ActualSignedSuzukiFiniteMarginalCertification(unittest.TestCase):
    def test_original_completed_zeta_strict_two_point_source_certificate(self):
        p=authentic_suzuki_ordinal_sign_search(
            F(1,4),F(1,2),(1,2,4,8,16,32,64,128))
        self.assertEqual(p["source"],"SHA_PINNED_AUTHENTIC_ZETA_SUZUKI_WEIL")
        self.assertEqual(p["signed_source_verdict"],
                         "CERTIFIED_STRICT_POSITIVE_DEFINITE_2_BY_2")
        self.assertTrue(p["strict_ordinal_decrease_each_executed_transition"])
        self.assertFalse(p["unresolved_ordinal_source_debt"])
        self.assertFalse(p["prime2_original_wavefront_sampled"])
        self.assertGreater(p["last_source_intersection"]["Kxx"][0],0)
        self.assertGreater(p["last_source_intersection"]["Kyy"][0],0)
        self.assertGreater(p["last_source_intersection"]["determinant"][0],0)
        self.assertEqual(p["ordinal_proof_rank_trace"][-1],"0")
        self.assertFalse(p["all_test_original_Weil_PSD_proved"])
        self.assertFalse(p["RH_proved"])

    def test_true_source_Gamma_regulator_intersections_are_nested_even_if_raw_are_not(self):
        p=authentic_suzuki_ordinal_sign_search(
            F(1,4),F(1,2),(1,2,4,8,16,32,64,128))
        stages=p["original_signed_source_stages"]
        for old,new in zip(stages,stages[1:]):
            self.assertGreater(old["source_gamma_tail_bound"],new["source_gamma_tail_bound"])
            self.assertGreaterEqual(new["combined_determinant_interval"][0],
                                    old["combined_determinant_interval"][0])
            self.assertLessEqual(new["combined_determinant_interval"][1],
                                 old["combined_determinant_interval"][1])
        rank_trace=p["ordinal_proof_rank_trace"]
        self.assertEqual(rank_trace[0],str(ordinal_lex_counters((1,8))))
        self.assertEqual(len(rank_trace),len(stages)+1)

    def test_actual_source_first_prime_activated_pair_without_positive_shortcut(self):
        # y=7/8 and |x-y|=3/4 both exceed the genuine log2.
        p=authentic_suzuki_ordinal_sign_search(
            F(1,8),F(7,8),(1,2,4,8,16,32,64))
        self.assertTrue(p["prime2_original_wavefront_sampled"])
        self.assertEqual(p["source"],"SHA_PINNED_AUTHENTIC_ZETA_SUZUKI_WEIL")
        self.assertIn(p["signed_source_verdict"],(
            "CERTIFIED_STRICT_POSITIVE_DEFINITE_2_BY_2",
            "CERTIFIED_NON_PSD_ORIGINAL_SOURCE",
            "SOURCE_SIGN_UNRESOLVED"))
        self.assertEqual(p["unresolved_ordinal_source_debt"],
                         p["signed_source_verdict"]=="SOURCE_SIGN_UNRESOLVED")
        self.assertFalse(p["all_test_original_Weil_PSD_proved"])
        self.assertFalse(p["RH_proved"])

    def test_source_tape_is_original_not_fake_six(self):
        src=_pinned_source()
        self.assertEqual(src.AUTHENTIC_TAPE,
                         ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2)))
        self.assertIsNone(src.real_prime_power(6))
        r=authentic_suzuki_ordinal_sign_search(F(1,4),F(1,2),(128,))
        self.assertEqual(r["signed_source_verdict"],
                         "CERTIFIED_STRICT_POSITIVE_DEFINITE_2_BY_2")
        self.assertEqual(r["Gamma_stages_completed"],1)

    def test_forced_invalid_exp_J_domain_source_and_untyped_inputs_fail(self):
        for x,y,Js in (
            (F(1,4),F(1,2),(1,4,4)),
            (F(1,4),F(1,2),(64,32)),
            (F(1,4),F(1,2),(0,)),
            (F(1,4),F(1,2),(129,)),
            (F(1,4),F(1,2),()),
            (F(1,4),F(1,2),[4,16]),
            (F(1,4),F(7,8),(128,)), # original exp evaluator radius overflow
            (F(0),F(1,2),(16,)),
            (F(1,2),F(1,2),(16,)),
            (F(1,4),F(7,8),("8",)),
            (True,F(1,2),(16,)),
            (0.25,F(1,2),(16,)),
        ):
            with self.subTest(x=x,y=y,Js=Js),self.assertRaises(OrdinalSourceSignError):
                authentic_suzuki_ordinal_sign_search(x,y,Js)


class ExactlyWhatOrdinalsCannotDecide(unittest.TestCase):
    def test_unknown_zero_margin_does_not_conjure_positive_certificate(self):
        for J in (1,2,5,17,32):
            t=original_zero_margin_stuttering_counterexample(J)
            self.assertTrue(t["all_finite_intervals_contain_zero"])
            self.assertFalse(t["strict_sign_separated_at_any_stage"])
            self.assertEqual(t["source_sign_proof_debt_after_regulator_exhausted"],"ω")
            self.assertTrue(t["ordinal_source_search_terminated"])
            self.assertFalse(t["actual_zeta_witness"])
            self.assertFalse(t["RH_proved"])

    def test_strict_sign_semidecision_requires_gap_and_all_stage_analytic_source(self):
        q=finite_strict_sign_semidecision_theorem()
        self.assertEqual(q["finite_code_regulator_cap"],128)
        self.assertFalse(q["finite_code_global_sign_decider"])
        self.assertFalse(q["all_rational_tests_sign_proved"])
        self.assertEqual(q["true_zero_margin_requires_additional_source_identity"],
                         "NOT_DECIDED_BY_SHRINKING_INTERVALS")
        self.assertFalse(q["RH_proved"])


if __name__=="__main__":
    unittest.main()
