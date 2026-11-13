"""Exact hostile controls for the local R0 inverse statements."""

from fractions import Fraction as Q
import importlib.util
from pathlib import Path
import unittest


_SPEC = importlib.util.spec_from_file_location("r0_probe", Path(__file__).with_name("r0_probe.py"))
r0 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(r0)


class RationalBranchCertificateTests(unittest.TestCase):
    def test_preregistered_strict_margins(self):
        self.assertTrue(all(Q(v) > 0 for v in r0.rational_certificates().values()))

    def test_gram_minimizers_and_endpoint_bound(self):
        for left in range(9):
            for right in range(9):
                row = r0.gram_minimizer(left, right)
                self.assertEqual(row["y"]-16*row["x"], 1)
                self.assertEqual(sum((q*q for q in row["states"]), Q()), row["energy"])
                k = max(left, right)
                self.assertLessEqual(row["denominator"], 256+Q(255, 256**(k+1)-1))

    def test_omitted_tail_really_gives_257(self):
        self.assertEqual(r0.gram_minimizer(0, 0)["energy"], Q(1, 257))
        self.assertGreater(r0.gram_minimizer(8, 0)["energy"], Q(1, 257))

    def test_boundary_events_have_no_invented_extra_side(self):
        first = r0.gram_minimizer(0, 8)
        last = r0.gram_minimizer(8, 0)
        self.assertLess(first["energy"], Q(1, 256))
        self.assertLess(last["energy"], Q(1, 256))
        self.assertEqual(len(first["states"]), 10)
        self.assertEqual(len(last["states"]), 10)

    def test_local_cosine_coefficient_not_global(self):
        self.assertLess(Q(2), 19*Q(1, 2)**2)


class SourceAndCarryTests(unittest.TestCase):
    def test_four_poles_equal_odd_polynomial_formula(self):
        for n in range(1, 65):
            p, q = r0.source_polynomials(n)
            self.assertEqual(r0.source(n), Q(p, q))
            self.assertEqual(q % 2, 1)

    def test_prefix_horner_and_direct_series_agree(self):
        for n in (1, 2, 7, 19, 37, 64):
            direct = sum((r0.source(k)/16**k for k in range(1, n+1)), Q())
            self.assertEqual(direct, r0.source_states(n)[-1]/16**n)
            low, high = r0.completed_interval(n)
            self.assertEqual(low, direct)
            self.assertEqual(high-low, Q(1, 64*n*n*16**n))

    def test_balanced_energy_on_unrelated_exact_orbits(self):
        for denominator in (3, 5, 7, 11, 17, 257):
            for numerator in (-7, -1, 0, 1, 5, 19):
                values = [Q(numerator, denominator)*16**n for n in range(31)]
                row = r0.carry_energy_certificate(values)
                self.assertGreaterEqual(row["lower_margin"], 0)
                self.assertGreaterEqual(row["upper_margin"], 0)
                self.assertTrue(all(abs(a) <= 8 for a in row["carries"]))

    def test_endpoint_term_cannot_be_removed(self):
        values = [Q(1, 16**(7-n)) for n in range(7)]
        row = r0.carry_energy_certificate(values)
        self.assertEqual(row["carry_energy"], 0)
        self.assertGreater(row["energy"], 0)

    def test_original_source_inherited_two_adic_fingerprint(self):
        states = r0.source_states(64)
        for n in range(1, 65):
            self.assertEqual(r0.v2(states[n]), r0.v2(n))

    def test_gamma_cleared_integer_recurrence(self):
        depth = 23
        lo, hi = r0.completed_interval(depth+24)
        lifts = [r0.nearest_integer(lo*16**n) for n in range(depth+1)]
        self.assertEqual(lifts, [r0.nearest_integer(hi*16**n) for n in range(depth+1)])
        rows = r0.cleared_source_trajectory(depth, lifts)
        states = r0.source_states(depth)
        for n, d, a, z in rows:
            self.assertEqual(Q(a, d), states[n])
            self.assertEqual(z, a-d*lifts[n])
            if n:
                p, q = r0.source_polynomials(n)
                _, d0, _, z0 = rows[n-1]
                carry = lifts[n]-16*lifts[n-1]
                self.assertEqual(z, 16*q*z0+d0*(p-q*carry))

    def test_zero_alias_and_periodic_completed_controls(self):
        zero = r0.interval_orbit_report("zero", (Q(), Q()), 17, False)
        alias = r0.interval_orbit_report("alias", (Q(1, 16), Q(1, 16)), 17, False)
        periodic = r0.interval_orbit_report("periodic", (Q(1, 15), Q(1, 15)), 17, False)
        self.assertEqual(zero["actual_mean_loss_enclosure"], ["0", "0"])
        self.assertEqual(alias["actual_mean_loss_enclosure"], ["0", "0"])
        self.assertGreater(Q(periodic["actual_mean_loss_enclosure"][0]), 0)

    def test_shallit_shell_requires_endpoint_budget(self):
        row = r0.interval_orbit_report("Shallit", r0.shallit_interval(152), 64, False)
        self.assertEqual(row["balanced_carry_energy"], 0)
        self.assertGreater(Q(row["actual_mean_loss_enclosure"][0]), 0)
        self.assertLess(Q(row["actual_mean_loss_enclosure"][1]), Q(1, 100))


class HostileMutationTests(unittest.TestCase):
    def test_failed_proper_null_strengthening_is_retained(self):
        states = r0.proper_null_states(2)
        self.assertEqual(states[2], Q(268, 45045))
        self.assertEqual(r0.v2(states[2]), 2)
        self.assertNotEqual(r0.v2(states[2]), r0.v2(2))

    def test_nonproper_null_has_full_two_adic_isometry(self):
        for s in range(-37, 38):
            for t in range(-37, s):
                difference = r0.hostile_state(s)-r0.hostile_state(t)
                self.assertEqual(r0.v2(difference), r0.v2(s-t))

    def test_nonproper_source_and_sign_scope(self):
        self.assertEqual(r0.hostile_state(0), 0)
        self.assertEqual(r0.hostile_source(1), Q(-1, 1287))
        for n in range(1, 65):
            self.assertEqual(r0.hostile_source(n), r0.hostile_integral_source(n))
            self.assertEqual(r0.hostile_state(n), 16*r0.hostile_state(n-1)+r0.hostile_source(n))
            if n >= 2:
                self.assertGreater(r0.hostile_source(n), 0)

    def test_bad_contract_inputs_are_rejected(self):
        for operation in (lambda: r0.source(0), lambda: r0.gram_minimizer(-1, 0),
                          lambda: r0.gram_minimizer(0, 0, 0),
                          lambda: r0.balanced_carries([Q(1), Q(15)]),
                          lambda: r0.completed_interval(0)):
            with self.assertRaises(ValueError):
                operation()


if __name__ == "__main__":
    unittest.main()
