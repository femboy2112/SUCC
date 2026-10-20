"""Firewall tests for the typed source -> signed completed Weil interface.

These tests PROVE the interface's firewall properties operationally:
  * ``identified`` is structurally never True (adversarial battery + source scan);
  * every one of the five constructed negative controls is rejected;
  * the summed-inverse guard refuses to sum the #181/#182 alternatives;
  * the actual current best source construction yields identified:False with the
    exact open obligations (the signed source->Weil morphism and the S_4 sign);
  * no float and no nontrivial zeta-zero ordinate can enter as a certificate.
"""
import re
import unittest
from fractions import Fraction as F

from observational_succ.source_weil_interface import (
    SourceWeilInterfaceError,
    SourceWeilOffer,
    certify_source_to_weil,
    reconfirm_s4_ambiguous,
    PrimeTwoInverseEstimate,
    prime_two_inverse_estimates_181_182,
    summed_inverse_guard,
    genuine_source_offer,
    control_positive_gram_as_signed_form,
    control_fake_composite_lambda6,
    control_non_euler_matched,
    control_zeta_zero_ordinate_input,
    control_finite_window_as_all_height,
    all_negative_controls,
    ALL_OBLIGATIONS,
    MORPHISM_EQUALITY,
    POSITIVITY_PROOF,
)
import observational_succ.source_weil_interface as swi


def _rejected_inputs(verdict):
    return {r["input"] for r in verdict["rejected_inputs"]}


class GenuineConstructionTests(unittest.TestCase):
    def setUp(self):
        self.verdict = certify_source_to_weil(genuine_source_offer())

    def test_genuine_is_not_identified(self):
        self.assertIs(self.verdict["identified"], False)
        self.assertIs(self.verdict["RH_proved"], False)

    def test_genuine_has_no_rejected_inputs(self):
        # The honest genuine offer passes every REJECT gate.
        self.assertEqual(self.verdict["rejected_inputs"], ())

    def test_genuine_missing_exactly_the_two_cardinal_obligations(self):
        self.assertEqual(
            set(self.verdict["missing_obligations"]),
            {MORPHISM_EQUALITY, POSITIVITY_PROOF},
        )

    def test_genuine_satisfies_the_eight_supplyable_obligations(self):
        satisfied = set(self.verdict["satisfied_obligations"])
        expected = set(ALL_OBLIGATIONS) - {MORPHISM_EQUALITY, POSITIVITY_PROOF}
        self.assertEqual(satisfied, expected)

    def test_open_obligation_names_s4_and_morphism(self):
        text = self.verdict["open_obligation"]
        self.assertIn("S_4", text)
        self.assertIn("morphism", text)
        self.assertIn("AMBIGUOUS", text)


class NegativeControlTests(unittest.TestCase):
    def test_a_positive_gram_rejected(self):
        v = certify_source_to_weil(control_positive_gram_as_signed_form())
        self.assertIs(v["identified"], False)
        self.assertIn("offered_form", _rejected_inputs(v))

    def test_b_fake_composite_lambda6_rejected(self):
        v = certify_source_to_weil(control_fake_composite_lambda6())
        self.assertIs(v["identified"], False)
        self.assertIn("prime_power_tape", _rejected_inputs(v))
        # a rejected source input also leaves its obligation unmet
        self.assertIn("genuine_prime_power_inputs", v["missing_obligations"])

    def test_c_non_euler_rejected(self):
        v = certify_source_to_weil(control_non_euler_matched())
        self.assertIs(v["identified"], False)
        self.assertIn("euler_product", _rejected_inputs(v))

    def test_d_zeta_zero_ordinate_rejected(self):
        v = certify_source_to_weil(control_zeta_zero_ordinate_input())
        self.assertIs(v["identified"], False)
        self.assertIn("zero_ordinate_inputs", _rejected_inputs(v))
        self.assertIs(v["firewall"]["no_nontrivial_zero_ordinate_input"], False)

    def test_e_finite_window_as_all_height_rejected(self):
        v = certify_source_to_weil(control_finite_window_as_all_height())
        self.assertIs(v["identified"], False)
        self.assertIn("positivity_scope", _rejected_inputs(v))

    def test_every_control_is_rejected_and_unidentified(self):
        for name, offer in all_negative_controls().items():
            with self.subTest(control=name):
                v = certify_source_to_weil(offer)
                self.assertIs(v["identified"], False)
                self.assertTrue(v["rejected_inputs"],
                                f"{name} produced no rejected inputs")


class SummedInverseGuardTests(unittest.TestCase):
    def test_guard_refuses_to_sum_alternatives(self):
        a, b = prime_two_inverse_estimates_181_182()
        with self.assertRaises(SourceWeilInterfaceError):
            summed_inverse_guard(a, b, operation="sum")

    def test_guard_selects_the_better_single_enclosure(self):
        a, b = prime_two_inverse_estimates_181_182()
        better = summed_inverse_guard(a, b, operation="select_better")
        self.assertIs(better, a)                       # PR181, the larger lower bound
        self.assertGreaterEqual(better.loewner_lower_min_eig, b.loewner_lower_min_eig)

    def test_guard_rejects_unknown_operation(self):
        a, b = prime_two_inverse_estimates_181_182()
        with self.assertRaises(SourceWeilInterfaceError):
            summed_inverse_guard(a, b, operation="average")

    def test_estimate_refuses_float(self):
        with self.assertRaises(SourceWeilInterfaceError):
            PrimeTwoInverseEstimate("PRx", "rid", 0.1)   # float is not a certificate

    def test_guard_requires_estimate_objects(self):
        a, _ = prime_two_inverse_estimates_181_182()
        with self.assertRaises(SourceWeilInterfaceError):
            summed_inverse_guard(a, "not-an-estimate", operation="sum")


class StructurallyNeverIdentifiedTests(unittest.TestCase):
    def test_no_input_path_flips_identified_to_true(self):
        # A maximally-compliant adversarial offer: satisfy every supplyable gate,
        # and additionally (illegitimately) ASSERT the two proof obligations.
        adversarial = SourceWeilOffer(
            label="adversarial_maximally_compliant",
            claims_positivity=True,
            positivity_scope="first_window",
            positivity_evidence_scope="first_window",
            fake_source_control_supplied=True,
            non_euler_control_supplied=True,
            claims_signed_morphism_equality=True,
            claims_signed_positivity_proof=True,
        )
        v = certify_source_to_weil(adversarial)
        self.assertIs(v["identified"], False)
        # the morphism obligation is unconditionally unmet
        self.assertIn(MORPHISM_EQUALITY, v["missing_obligations"])
        # asserting a proof as a boolean is itself rejected (proof laundering)
        rej = _rejected_inputs(v)
        self.assertIn("claims_signed_morphism_equality", rej)
        self.assertIn("claims_signed_positivity_proof", rej)

    def test_battery_of_offers_all_unidentified(self):
        offers = [genuine_source_offer()]
        offers += list(all_negative_controls().values())
        offers.append(SourceWeilOffer(label="minimal_defaults"))
        offers.append(SourceWeilOffer(label="no_positivity_claim", claims_positivity=False))
        for offer in offers:
            with self.subTest(offer=offer.label):
                v = certify_source_to_weil(offer)
                self.assertIs(v["identified"], False)
                self.assertIn(MORPHISM_EQUALITY, v["missing_obligations"])

    def test_positivity_proof_missing_whenever_positivity_claimed(self):
        v = certify_source_to_weil(
            SourceWeilOffer(label="claims_pos", claims_positivity=True,
                            positivity_scope="first_window",
                            positivity_evidence_scope="first_window"))
        self.assertIn(POSITIVITY_PROOF, v["missing_obligations"])

    def test_source_has_no_identified_true_literal(self):
        with open(swi.__file__, "r", encoding="utf-8") as fh:
            src = fh.read()
        for bad in ('identified = True', 'identified=True',
                    '"identified": True', "'identified': True"):
            self.assertNotIn(bad, src, f"forbidden literal present: {bad!r}")
        # the only assignment to identified is to False
        self.assertIn("identified = False", src)

    def test_verdict_shape_keys_present(self):
        v = certify_source_to_weil(genuine_source_offer())
        for key in ("identified", "missing_obligations", "rejected_inputs"):
            self.assertIn(key, v)


class ExactArithmeticAndNoZeroTests(unittest.TestCase):
    def test_float_half_density_refused(self):
        with self.assertRaises(SourceWeilInterfaceError):
            SourceWeilOffer(label="float_hd", half_density=0.5)

    def test_numeric_zeta_zero_ordinate_refused_at_door(self):
        # A nontrivial zero ordinate may never be a numeric input.
        with self.assertRaises(SourceWeilInterfaceError):
            SourceWeilOffer(label="numeric_zero", zero_ordinate_inputs=(F(14, 1),))
        with self.assertRaises(SourceWeilInterfaceError):
            SourceWeilOffer(label="float_zero", zero_ordinate_inputs=(14.134,))

    def test_no_float_appears_in_a_verdict(self):
        v = certify_source_to_weil(genuine_source_offer())

        def walk(obj):
            if isinstance(obj, float):
                self.fail(f"float leaked into verdict: {obj!r}")
            if isinstance(obj, dict):
                for x in obj.values():
                    walk(x)
            elif isinstance(obj, (list, tuple)):
                for x in obj:
                    walk(x)
        walk(v)


class S4ReconfirmTests(unittest.TestCase):
    def test_reconfirm_s4_is_ambiguous(self):
        r = reconfirm_s4_ambiguous(J=3, rank=6)
        self.assertEqual(r["verdict"], "AMBIGUOUS")
        self.assertIs(r["RH_proved"], False)
        self.assertIs(r["nontrivial_zero_coordinates_used"], False)

    def test_genuine_offer_ties_positivity_to_ambiguous_s4(self):
        # Because S_4 is AMBIGUOUS, the genuine offer's positivity obligation is open.
        v = certify_source_to_weil(genuine_source_offer())
        self.assertIn(POSITIVITY_PROOF, v["missing_obligations"])
        self.assertEqual(v["s4_sign"], "OPEN (CERTIFIED AMBIGUOUS)")


class DeterminismTests(unittest.TestCase):
    def test_certify_is_deterministic(self):
        a = certify_source_to_weil(genuine_source_offer())
        b = certify_source_to_weil(genuine_source_offer())
        self.assertEqual(a["missing_obligations"], b["missing_obligations"])
        self.assertEqual(a["satisfied_obligations"], b["satisfied_obligations"])
        self.assertEqual(a["rejected_inputs"], b["rejected_inputs"])
        self.assertEqual(a["identified"], b["identified"])


if __name__ == "__main__":
    unittest.main()
