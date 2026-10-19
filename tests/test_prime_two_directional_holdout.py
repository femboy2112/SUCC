"""Tests for TARGET C: prime-two normalized directional inverse on a holdout."""
import unittest
from fractions import Fraction as F

from observational_succ import prime_two_directional_holdout as H
from observational_succ import original_continuum_residual as R


def _all_rh_false(obj):
    """Every dict anywhere in the result must carry RH_proved == False."""
    if isinstance(obj, dict):
        if "RH_proved" in obj and obj["RH_proved"] is not False:
            return False
        return all(_all_rh_false(v) for v in obj.values())
    if isinstance(obj, (list, tuple)):
        return all(_all_rh_false(v) for v in obj)
    return True


class PrimeTwoDirectionalHoldoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res = H.prime_two_directional_holdout()

    # ---- firewall -------------------------------------------------------
    def test_top_level_firewall(self):
        r = self.res
        self.assertIs(r["RH_proved"], False)
        self.assertTrue(_all_rh_false(r))
        self.assertTrue(r["lambda_power_is_log_p"])
        self.assertTrue(r["no_zeta_zero_ordinate_input"])
        self.assertEqual(r["status_label"], "VERIFIED-EXACT-MODEL")

    def test_every_nested_dict_has_rh_false(self):
        for sec in ("odd_derivative", "even_derivative"):
            s = self.res["parity_sectors"][sec]
            self.assertIs(s["RH_proved"], False)
            self.assertIs(s["corrected_holdout_B_normalized_spectrum"]["RH_proved"],
                          False)
            self.assertIs(s["source_attested_budget"]["RH_proved"], False)

    # ---- windows are genuinely distinct --------------------------------
    def test_fit_and_holdout_windows_distinct(self):
        r = self.res
        self.assertTrue(r["fit_and_holdout_windows_distinct"])
        self.assertEqual(r["fit_window"]["M"], 80)
        self.assertEqual(r["holdout_window"]["M"], 192)
        self.assertNotEqual((r["fit_window"]["J"], r["fit_window"]["M"]),
                            (r["holdout_window"]["J"], r["holdout_window"]["M"]))

    def test_same_window_fit_and_holdout_rejected(self):
        with self.assertRaises(H.PrimeTwoHoldoutError):
            H.prime_two_directional_holdout(
                fit_path=H.HOLDOUT_CERTIFICATE, holdout_path=H.HOLDOUT_CERTIFICATE)

    # ---- the honest outcome: holdout stays non-PSD, S4 OPEN ------------
    def test_holdout_stays_non_psd_both_sectors(self):
        r = self.res
        self.assertFalse(r["fresh_holdout_first_window_S4_PSD"])
        self.assertFalse(r["fresh_holdout_flips_S4_sign"])
        self.assertFalse(r["S4_first_window_sign_certified"])
        self.assertEqual(r["S4_sign_status"], "OPEN")
        self.assertIn("REFUTED", r["verdict"])
        for sec in ("odd_derivative", "even_derivative"):
            s = r["parity_sectors"][sec]
            self.assertFalse(s["holdout_first_window_PSD"])
            self.assertEqual(
                s["corrected_holdout_B_normalized_spectrum"]["min_eigenvalue_sign"],
                "negative")
            # published #181 new_lower is also non-PSD under the same metric.
            self.assertEqual(
                s["published_181_B_normalized_spectrum"]["min_eigenvalue_sign"],
                "negative")

    # ---- the better single enclosure is the directional inverse --------
    def test_better_single_enclosure_is_directional(self):
        for sec in ("odd_derivative", "even_derivative"):
            s = self.res["parity_sectors"][sec]
            self.assertEqual(s["chosen_single_enclosure"], "directional_inverse")
            self.assertGreater(
                F(s["directional_inverse_saving_Gershgorin_floor"]),
                F(s["resolvent_saving_Gershgorin_floor"]))
            self.assertTrue(s["savings_were_never_summed"])

    def test_better_single_enclosure_helper(self):
        res = ((F(1), F(0)), (F(0), F(1)))        # gershgorin floor 1
        direct = ((F(3), F(1)), (F(1), F(3)))     # gershgorin floor 2 (better)
        chosen, which, floor = H.better_single_enclosure(res, direct)
        self.assertEqual(which, "directional_inverse")
        self.assertEqual(chosen, direct)
        self.assertEqual(floor, F(2))
        chosen2, which2, _ = H.better_single_enclosure(direct, res)
        self.assertEqual(which2, "center_edge_resolvent")
        self.assertEqual(chosen2, direct)

    # ---- never-sum guard ------------------------------------------------
    def test_never_sum_guard_rejects_summed_bound(self):
        res = ((F(1), F(0)), (F(0), F(1)))
        direct = ((F(2), F(0)), (F(0), F(2)))
        summed = ((F(3), F(0)), (F(0), F(3)))
        with self.assertRaises(H.PrimeTwoHoldoutError):
            H.reject_double_count(summed, res, direct)
        # a genuine single bound passes through unchanged
        self.assertEqual(H.reject_double_count(direct, res, direct), direct)

    def test_result_is_never_a_summed_bound(self):
        # The returned corrected lower must equal old + a single saving, never
        # old + gain + direct (the refuted double-count).
        fit = H._load_certificate(H.FIT_CERTIFICATE)
        hold = H._load_certificate(H.HOLDOUT_CERTIFICATE)
        for sec in ("odd_derivative", "even_derivative"):
            hp = H._sector_pieces(hold, sec)
            double = H._add(H._add(hp["old"], hp["gain"]), hp["direct"])
            corrected = tuple(tuple(F(v) for v in row) for row in
                self.res["parity_sectors"][sec][
                    "corrected_holdout_first_window_Schur_lower"])
            self.assertNotEqual(corrected, double)
            # it equals old + the chosen single enclosure
            chosen, _, _ = H.better_single_enclosure(hp["gain"], hp["direct"])
            self.assertEqual(corrected, H._add(hp["old"], chosen))

    # ---- comparator metric B -------------------------------------------
    def test_comparator_B_is_positive_definite(self):
        fit = H._load_certificate(H.FIT_CERTIFICATE)
        for sec in ("odd_derivative", "even_derivative"):
            Bm = H.build_comparator_B(fit, sec)
            self.assertGreater(Bm[0][0], 0)
            self.assertGreater(H._det(Bm), 0)

    def test_non_pd_metric_rejected(self):
        indefinite = ((F(1), F(0)), (F(0), F(-1)))
        good = ((F(1), F(0)), (F(0), F(1)))
        with self.assertRaises(H.PrimeTwoHoldoutError):
            H.b_normalized_spectrum(good, indefinite)

    # ---- exact spectrum semantics --------------------------------------
    def test_b_metric_agrees_with_ordinary_psd(self):
        # PSD under a PD metric <=> ordinary PSD (independent-metric check).
        Bm = ((F(5), F(1)), (F(1), F(4)))
        psd_lower = ((F(2), F(0)), (F(0), F(3)))
        indef_lower = ((F(1), F(2)), (F(2), F(1)))
        self.assertTrue(
            H.b_normalized_spectrum(psd_lower, Bm)["psd_in_B_metric"])
        self.assertEqual(
            H.b_normalized_spectrum(psd_lower, Bm)["psd_in_B_metric"],
            H._is_psd(psd_lower))
        self.assertFalse(
            H.b_normalized_spectrum(indef_lower, Bm)["psd_in_B_metric"])
        self.assertEqual(
            H.b_normalized_spectrum(indef_lower, Bm)["psd_in_B_metric"],
            H._is_psd(indef_lower))

    def test_min_eig_lower_bound_is_rational_and_valid(self):
        # min generalized eig lower bound is a Fraction and, for a negative
        # (B-metric) lower, is strictly negative and <= the float min eig.
        Bm = ((F(5), F(1)), (F(1), F(4)))
        neg = ((F(-2), F(0)), (F(0), F(-3)))
        spec = H.b_normalized_spectrum(neg, Bm)
        lb = spec["min_generalized_eigenvalue_rational_lower_bound"]
        self.assertIsInstance(lb, F)
        self.assertLess(lb, 0)
        # float cross check: lb <= true min generalized eigenvalue
        detB = float(H._det(Bm))
        T = float(spec["trace_pencil_T"])
        disc = float(spec["discriminant"])
        true_min = (T - disc ** 0.5) / (2 * detB)
        self.assertLessEqual(float(lb), true_min + 1e-12)

    def test_holdout_min_eig_lower_bound_negative(self):
        for sec in ("odd_derivative", "even_derivative"):
            lb = F(self.res["parity_sectors"][sec][
                "corrected_holdout_B_normalized_spectrum"][
                "min_generalized_eigenvalue_rational_lower_bound"])
            self.assertLess(lb, 0)

    # ---- provenance -----------------------------------------------------
    def test_source_provenance(self):
        self.assertEqual(self.res["source_blob"], R.SOURCE_SHA)
        for sec in ("odd_derivative", "even_derivative"):
            s = self.res["parity_sectors"][sec]
            self.assertEqual(s["source_attested_budget"]["source_blob"],
                             R.SOURCE_SHA)
            self.assertEqual(
                s["source_attested_budget"]["prime_surplus_weight_floor"],
                "12/25")

    def test_tampered_certificate_rejected(self):
        hold = H._load_certificate(H.HOLDOUT_CERTIFICATE)
        hold["source_blob"] = "deadbeef"
        # a certificate with a wrong SHA passed through _load path would fail;
        # here we check the direct consistency guard on new_lower = old + gain.
        bad = H._load_certificate(H.HOLDOUT_CERTIFICATE)
        bad["sectors"]["odd_derivative"]["new_lower"] = \
            bad["sectors"]["odd_derivative"]["old_lower"]
        with self.assertRaises(H.PrimeTwoHoldoutError):
            H._sector_pieces(bad, "odd_derivative")


if __name__ == "__main__":
    unittest.main()
