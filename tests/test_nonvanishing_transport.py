"""Exact finite->global transport criterion: Gamma survival + atomic refusal.

Every certificate value is an exact Fraction; no float is trusted as a proof.
The Gamma rank-one coefficient must stay bounded away from 0 and transport to a
nonvanishing limit; the atomic-Haar analog must VANISH and be REFUSED.
"""
from fractions import Fraction as F
import unittest

from observational_succ.nonvanishing_transport import (
    Section, TransportError, atomic_haar_refusal, atomic_haar_vanishing_coefficients,
    gamma_rank_one_coefficient, gamma_transport_certificate,
    nonvanishing_transport_report, transport_criterion,
)
from observational_succ.infinite_gamma_carleman import alpha, exp_negative_interval


class GammaRankOneCoefficient(unittest.TestCase):
    def test_exact_bracket_is_an_ordered_enclosure_of_the_true_sum(self):
        for J in (16, 32, 64):
            r = gamma_rank_one_coefficient(J)
            lo, hi = r["coeff_lower"], r["coeff_upper"]
            self.assertIs(type(lo), F)
            self.assertIs(type(hi), F)
            self.assertLessEqual(lo, hi)
            # Independent exact recomputation of the finite sum enclosure.
            s = F(1, 128)
            clo = chi = F(0)
            for j in range(J):
                elo, ehi = exp_negative_interval(alpha(j) * s, 8)
                w2 = F(1, (j + 1) ** 2)
                clo += w2 * elo
                chi += w2 * ehi
            self.assertEqual(lo, clo)
            self.assertEqual(hi, chi)

    def test_structural_floor_is_first_term_and_strictly_positive(self):
        s = F(1, 128)
        floor_expected = exp_negative_interval(alpha(0) * s, 8)[0]
        for J in (16, 32, 64):
            r = gamma_rank_one_coefficient(J)
            self.assertEqual(r["structural_floor"], floor_expected)
            self.assertGreater(r["structural_floor"], 0)
            # Every coefficient is bounded below by the persistent floor.
            self.assertGreaterEqual(r["coeff_lower"], r["structural_floor"])

    def test_coefficient_is_strictly_increasing_in_J_and_bounded_by_pi2_over_6(self):
        lowers = [gamma_rank_one_coefficient(J)["coeff_lower"] for J in (16, 32, 64)]
        self.assertTrue(all(lowers[i] < lowers[i + 1] for i in range(len(lowers) - 1)))
        # ||v||^2 = sum 1/(j+1)^2 < pi^2/6 < 165/100 is a hard rational ceiling.
        for J in (16, 32, 64):
            r = gamma_rank_one_coefficient(J)
            self.assertLess(r["coeff_upper"], F(165, 100))

    def test_cauchy_remainder_is_a_valid_shrinking_upper_bound(self):
        rems = [gamma_rank_one_coefficient(J)["cauchy_remainder_upper"] for J in (16, 32, 64)]
        self.assertTrue(all(r > 0 for r in rems))
        self.assertTrue(all(rems[i] > rems[i + 1] for i in range(len(rems) - 1)))
        # Enclosures of successive sections must share a common limit value.
        data = [gamma_rank_one_coefficient(J) for J in (16, 32, 64)]
        inter_lo = max(d["coeff_lower"] for d in data)
        inter_hi = min(d["coeff_upper"] + d["cauchy_remainder_upper"] for d in data)
        self.assertLessEqual(inter_lo, inter_hi)

    def test_window_and_type_guards(self):
        with self.assertRaises(TransportError):
            gamma_rank_one_coefficient(16, s=0.1)          # float cannot certify
        with self.assertRaises(TransportError):
            gamma_rank_one_coefficient(16, s=F(1, 2))      # outside Taylor window
        with self.assertRaises(TransportError):
            gamma_rank_one_coefficient(0)                  # nonpositive order


class TransportCriterion(unittest.TestCase):
    def test_monotone_bounded_floored_sequence_is_certified(self):
        secs = [Section(1, F(1, 2), F(6, 10), F(1, 10)),
                Section(2, F(11, 20), F(6, 10), F(1, 20)),
                Section(3, F(57, 100), F(6, 10), F(1, 100))]
        v = transport_criterion(secs, uniform_bound=F(1), floor=F(1, 2))
        self.assertTrue(v["certified_nonvanishing"])
        self.assertEqual(v["certified_global_floor"], "1/2")
        self.assertFalse(v["refusal_reasons"])

    def test_decreasing_sequence_is_refused(self):
        secs = [Section(0, F(1, 2), F(1, 2), F(0)),
                Section(1, F(1, 4), F(1, 4), F(0)),
                Section(2, F(1, 8), F(1, 8), F(0))]
        v = transport_criterion(secs, uniform_bound=F(1), floor=F(1, 2))
        self.assertFalse(v["certified_nonvanishing"])
        self.assertTrue(v["vanishing_signature"])
        self.assertIn("no_persistent_floor_coefficient_not_monotone", v["refusal_reasons"])

    def test_nonpositive_floor_is_refused(self):
        secs = [Section(1, F(1, 2), F(6, 10), F(0)), Section(2, F(11, 20), F(6, 10), F(0))]
        v = transport_criterion(secs, uniform_bound=F(1), floor=F(0))
        self.assertFalse(v["certified_nonvanishing"])
        self.assertIn("floor_not_positive", v["refusal_reasons"])

    def test_breaching_uniform_bound_is_refused(self):
        secs = [Section(1, F(1, 2), F(6, 10), F(0)), Section(2, F(11, 20), F(9), F(0))]
        v = transport_criterion(secs, uniform_bound=F(1), floor=F(1, 2))
        self.assertFalse(v["certified_nonvanishing"])
        self.assertIn("uniform_boundedness_failed", v["refusal_reasons"])

    def test_structure_guards(self):
        with self.assertRaises(TransportError):
            transport_criterion([Section(1, F(1, 2), F(6, 10), F(0))], F(1), F(1, 2))
        with self.assertRaises(TransportError):
            Section(1, F(6, 10), F(1, 2), F(0))            # unordered enclosure
        with self.assertRaises(TransportError):
            Section(1, F(1, 2), F(6, 10), F(-1))           # negative remainder


class GammaTransportCertificate(unittest.TestCase):
    def test_authentic_gamma_model_is_verified_exact_and_nonvanishing(self):
        g = gamma_transport_certificate()
        self.assertEqual(g["status"], "VERIFIED-EXACT-MODEL")
        self.assertTrue(g["criterion_verdict"]["certified_nonvanishing"])
        self.assertTrue(g["strictly_increasing_across_orders"])
        self.assertFalse(g["RH_proved"])
        # The certified transported lower bound is a genuine positive rational.
        self.assertGreater(F(g["transported_global_coeff_lower"]), 0)
        self.assertGreater(F(g["certified_global_floor"]), 0)

    def test_transported_interval_contains_the_true_limit_value(self):
        g = gamma_transport_certificate()
        lo = F(g["transported_global_coeff_lower"])
        hi = F(g["transported_global_coeff_upper"])
        # Independent exact rational under/over estimate of c_inf by a long
        # partial sum with an exact geometric tail bound.
        s = F(1, 128)
        partial = F(0)
        last_hi = None
        for j in range(400):
            elo, ehi = exp_negative_interval(alpha(j) * s, 8) if alpha(j) * s <= 1 else (F(0), None)
            if ehi is None:
                # beyond the Taylor window: bound the whole remaining tail
                r_hi = exp_negative_interval(2 * s, 8)[1]
                tail = last_hi * r_hi / (1 - r_hi) * F(1, (j) ** 2)
                self.assertLessEqual(lo, partial + tail)
                break
            partial += F(1, (j + 1) ** 2) * elo
            last_hi = ehi
        self.assertLess(lo, hi)
        self.assertLess(lo, F(159, 100))
        self.assertGreater(hi, F(158, 100))


class AtomicHaarHostileControl(unittest.TestCase):
    def test_atomic_coefficients_are_exact_and_strictly_decreasing(self):
        co = atomic_haar_vanishing_coefficients()
        for key in ("harmonic_source_norm_squared", "haar_unit_masses"):
            vals = co[key]
            self.assertTrue(all(type(v) is F for v in vals))
            self.assertTrue(all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)))
            self.assertGreater(vals[0], 0)

    def test_criterion_refuses_both_atomic_witnesses(self):
        h = atomic_haar_refusal()
        self.assertEqual(h["status"], "HOSTILE-CONTROL-REFUSED")
        for name in ("harmonic_graph_witness", "haar_unit_mass"):
            rec = h["receipts"][name]
            self.assertTrue(rec["criterion_refused"])
            self.assertTrue(rec["strictly_decreasing"])
            self.assertFalse(rec["verdict"]["certified_nonvanishing"])
            self.assertFalse(rec["verdict"]["RH_proved"])

    def test_atomic_masses_match_independent_recomputation(self):
        from observational_succ.institute_atomic_haar import haar_unit_mass, harmonic_graph_witness
        co = atomic_haar_vanishing_coefficients(sizes=(4, 16, 64, 256), period=2)
        self.assertEqual(co["haar_unit_masses"][0], haar_unit_mass((2,)))
        self.assertEqual(co["harmonic_source_norm_squared"][0],
                         harmonic_graph_witness(4, 2)["source_norm_squared"])
        # The Euler-product atomic mass is prod (p-1)/p over the growing family.
        self.assertEqual(co["haar_unit_masses"][1], F(1, 2) * F(2, 3))


class FullReport(unittest.TestCase):
    def test_report_carries_both_outcomes_and_the_firewall_flag(self):
        rep = nonvanishing_transport_report()
        self.assertFalse(rep["RH_proved"])
        self.assertEqual(rep["gamma_model_certificate"]["status"], "VERIFIED-EXACT-MODEL")
        self.assertEqual(rep["atomic_haar_hostile_control"]["status"], "HOSTILE-CONTROL-REFUSED")
        self.assertTrue(rep["finite_J_only"])
        self.assertIn("NOT a global proof", rep["global_limit_requires"])
        self.assertTrue(rep["source_authenticated"])

    def test_every_returned_dict_declares_RH_not_proved(self):
        self.assertFalse(gamma_rank_one_coefficient(16)["RH_proved"])
        self.assertFalse(atomic_haar_vanishing_coefficients()["RH_proved"])
        self.assertFalse(atomic_haar_refusal()["RH_proved"])
        self.assertFalse(gamma_transport_certificate()["RH_proved"])
        self.assertFalse(transport_criterion(
            [Section(1, F(1, 2), F(6, 10), F(0)), Section(2, F(11, 20), F(6, 10), F(0))],
            F(1), F(1, 2))["RH_proved"])


if __name__ == "__main__":
    unittest.main()
