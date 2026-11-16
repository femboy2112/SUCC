import unittest
from fractions import Fraction as Q
from math import log10

import borwein_ratchet as br


class BorweinRatchetTests(unittest.TestCase):
    def test_single_uniform_window_against_interval_geometry(self):
        for width in (Q(1, 3), Q(1), Q(7, 2)):
            for half_window in (Q(1, 2), Q(1), Q(2)):
                for shift in (Q(-3), Q(-1), Q(0), Q(1, 3), Q(2)):
                    length = max(Q(0), min(width, half_window - shift) -
                                 max(-width, -half_window - shift))
                    self.assertEqual(br.window_mass((width,), half_window, shift),
                                     length / (2 * width))

    def test_two_uniforms_against_triangle_area(self):
        # The sum of two U[-1,1] variables has density (2-|x|)/4 on [-2,2].
        for half_window in (Q(1, 4), Q(1, 2), Q(1), Q(3, 2), Q(2)):
            area = half_window - half_window**2 / 4
            self.assertEqual(br.window_mass((Q(1), Q(1)), half_window), area)
        self.assertEqual(br.window_mass((Q(1), Q(1)), Q(1), Q(2)), Q(1, 8))

    def test_empty_bank_probability_and_fourier_endpoints_are_distinct(self):
        for sign in (-1, 1):
            self.assertEqual(br.window_mass((), shift=Q(sign)), 1)
            self.assertEqual(br.borwein_multiplier((), Q(sign)), Q(1, 2))
        self.assertEqual(br.borwein_multiplier((), Q(0)), 1)
        self.assertEqual(br.borwein_multiplier((), Q(2)), 0)
        self.assertEqual(br.window_mass((), Q(2), Q(2)), 1)
        self.assertEqual(br.borwein_multiplier((), Q(2), Q(2)), Q(1, 2))

    def test_integer_filter_symmetry_support_and_boundary(self):
        for widths in ((Q(1, 5),), (Q(1),), (Q(1, 2), Q(1, 2)),
                       (Q(1, 3), Q(1, 5), Q(1, 7))):
            for charge in range(-5, 6):
                self.assertEqual(br.integer_charge_filter(widths, charge),
                                 br.borwein_multiplier(widths, Q(charge)))
            self.assertEqual(br.integer_charge_filter(widths, 1), Q(1, 2))
        # The support proof has no inclusion-exclusion width-count restriction.
        self.assertEqual(br.integer_charge_filter((Q(1, 12),) * 12, 1), Q(1, 2))
        for rounds in range(8):
            self.assertEqual(br.integer_filter_error(rounds), Q(1, 2)**rounds)

    def test_strict_threshold_equality_and_first_crossing(self):
        state = br.RatchetState()
        for total in (Q(1, 2), Q(1)):
            update = state.advance(Q(1, 2))
            self.assertEqual(tuple(update.releases), ())
            state = update.after
            self.assertEqual(state.radius, total)
        update = state.advance(Q(1, 2))
        self.assertEqual(tuple(update.releases), (1,))
        self.assertEqual(update.certificate(1).deficit(), Q(1, 24))
        self.assertEqual(br.window_mass((Q(1, 2),) * 3), Q(23, 24))
        for value, count in ((Q(0), 0), (Q(1), 0), (Q(2), 1),
                             (Q(2) + Q(1, 1000), 2), (Q(3), 2)):
            self.assertEqual(br.strict_tooth_count(value), count)

    def test_large_width_records_each_release_without_skipping(self):
        update = br.RatchetState().advance(Q(7, 2))
        self.assertEqual(tuple(update.releases), (1, 2, 3))
        for tooth in update.releases:
            self.assertEqual(update.certificate(tooth).deficit(),
                             1 - Q(tooth) / Q(7, 2))
        self.assertEqual(update.after.source_label, 4)

    def test_classical_one_fifteenth_leak_is_exact(self):
        widths = tuple(Q(1, denominator) for denominator in range(3, 16, 2))
        expected = Q(6879714958723010531,
                     467807924720320453655260875000)
        self.assertEqual(br.first_crossing_deficit(widths), expected)
        self.assertEqual(1 - br.window_mass(widths), expected)
        self.assertEqual(br.window_mass(widths[:-1]), 1)

    def test_odd_reciprocal_releases_and_resumption(self):
        state = br.RatchetState()
        releases = []
        checkpoint = None
        for step in range(1, 419):
            update = state.advance(Q(1, 2 * step + 1))
            self.assertLessEqual(len(update.releases), 1)
            for tooth in update.releases:
                certificate = update.certificate(tooth)
                releases.append(certificate)
                self.assertLessEqual(update.before.radius, tooth)
                self.assertGreater(update.after.radius, tooth)
                self.assertLessEqual(certificate.excess, certificate.smallest_width)
            state = update.after
            if step == 30:
                checkpoint = state
        self.assertEqual([(event.tooth, event.step) for event in releases],
                         [(1, 7), (2, 56), (3, 418)])
        self.assertEqual(state.source_label, 4)
        # Restart from the five exact registers, then compare the entire state.
        resumed = br.RatchetState(checkpoint.processed, checkpoint.radius,
                                  checkpoint.width_product, checkpoint.last_width,
                                  checkpoint.clicks)
        for step in range(31, 419):
            resumed = resumed.advance(Q(1, 2 * step + 1)).after
        self.assertEqual(resumed, state)
        # Approximation is checked only as a display diagnostic against an
        # already exact positive leakage at the first two, manageable releases.
        for certificate in releases[:2]:
            exact = certificate.deficit()
            self.assertGreater(exact, 0)
            expected_log = log10(exact.numerator) - log10(exact.denominator)
            self.assertAlmostEqual(certificate.approximate_log10_deficit(),
                                   expected_log, places=10)
        self.assertLess(releases[2].approximate_log10_deficit(), -1000)

    def test_dyadic_block_bound_and_summable_null(self):
        for k in (1, 2, 3):
            radius = sum((Q(1, 2 * j + 1) for j in range(1, 8**k)), Q(0))
            self.assertGreater(radius, k)
        state = br.RatchetState()
        for j in range(1, 65):
            update = state.advance(Q(1, 2**j))
            self.assertEqual(tuple(update.releases), ())
            state = update.after
        self.assertEqual(state.radius, 1 - Q(1, 2**64))
        self.assertEqual(state.source_label, 1)

    def test_lift_retains_wrap_and_the_positive_source_offset(self):
        origin = br.LiftedAddress.from_label(1, 5)
        wrapped = origin.successor(5)
        self.assertEqual((origin.residue, wrapped.residue), (0, 0))
        self.assertEqual((origin.turn, wrapped.turn), (0, 1))
        self.assertEqual((origin.divisor_gate(2), wrapped.divisor_gate(2)), (0, 1))
        self.assertEqual(br.LiftedAddress.from_label(3, 5).multiply(2),
                         br.LiftedAddress(5, 1, 0))
        for circumference in (2, 3, 7):
            for label in range(1, 61):
                address = br.LiftedAddress.from_label(label, circumference)
                self.assertEqual(address.label, label)
                for multiplier in range(1, 8):
                    self.assertEqual(address.successor().multiply(multiplier),
                                     address.multiply(multiplier).successor(multiplier))
                    self.assertEqual(address.divisor_gate(multiplier),
                                     int(label % multiplier == 0))

    def test_rectified_law_retains_atom_and_has_declared_drift(self):
        for threshold, expected in ((Q(-1), Q(0)), (Q(0), Q(1, 2)),
                                    (Q(1), Q(3, 4)), (Q(2), Q(1))):
            self.assertEqual(br.rectified_cdf((Q(2),), threshold), expected)
        # Independent mixture: 1/4 atom + 1/2 U[0,1] + 1/4 triangular sum.
        for threshold, expected in ((Q(0), Q(1, 4)), (Q(1, 2), Q(17, 32)),
                                    (Q(1), Q(7, 8)), (Q(3, 2), Q(31, 32))):
            self.assertEqual(br.rectified_cdf((Q(1), Q(1)), threshold), expected)
        self.assertEqual(br.rectified_cdf((), Q(0)), 1)
        self.assertEqual(br.rectified_cdf((), Q(-1)), 0)
        self.assertEqual(br.rectified_moments((Q(2),)), (Q(1, 2), Q(5, 12)))
        self.assertEqual(br.rectified_moments((Q(1), Q(1))), (Q(1, 2), Q(5, 24)))

    def test_public_summaries_reject_impossible_products(self):
        # Concrete adversarial witnesses formerly produced leakage 50 and
        # 25/12.  A finite-register representation still owes algebraic checks.
        with self.assertRaises(ValueError):
            br.ReleaseCertificate(1, 1, Q(1, 2), Q(1, 2), Q(1, 100))
        with self.assertRaises(ValueError):
            br.RatchetState(1, Q(1, 2), Q(1, 100), Q(1, 2), 0)
        with self.assertRaises(ValueError):
            br.RatchetState(1, Q(3, 4), Q(1, 2), Q(1, 2), 0)
        # For m=3,A=5/4,min=1/4, concentrating the excess gives product
        # 3/64; sharing it equally between the other two gives product 1/16.
        for impossible_product in (Q(1, 32), Q(1, 8)):
            with self.assertRaises(ValueError):
                br.RatchetState(3, Q(5, 4), impossible_product, Q(1, 4), 1)
            with self.assertRaises(ValueError):
                br.ReleaseCertificate(1, 3, Q(1, 4), Q(1, 4), impossible_product)
        for widths, product in (((Q(3, 4), Q(1, 4), Q(1, 4)), Q(3, 64)),
                                ((Q(1, 2), Q(1, 2), Q(1, 4)), Q(1, 16))):
            state = br.RatchetState(3, Q(5, 4), product, Q(1, 4), 1)
            certificate = br.ReleaseCertificate(1, 3, Q(1, 4), Q(1, 4), product)
            self.assertEqual(certificate.deficit(), 1 - br.window_mass(widths))
            self.assertEqual(state.clicks, 1)
        # With two widths both extremal bounds coincide, fixing the product.
        for impossible_product in (Q(1, 4), Q(1, 2)):
            with self.assertRaises(ValueError):
                br.RatchetState(2, Q(5, 4), impossible_product, Q(1, 2), 1)
        valid = br.ReleaseCertificate(1, 1, Q(1, 2), Q(3, 2), Q(3, 2))
        self.assertEqual(valid.deficit(), Q(1, 3))

    def test_input_and_resource_boundaries(self):
        for bad in (Q(0), Q(-1), 0.5, True, 1):
            with self.assertRaises(ValueError):
                br.RatchetState().advance(bad)
        with self.assertRaises(ValueError):
            br.RatchetState().advance(Q(1, 4)).after.advance(Q(1, 3))
        with self.assertRaises(ValueError):
            br.RatchetState(1, Q(1), Q(1), Q(1), 1)
        with self.assertRaises(ValueError):
            br.RatchetState().advance(Q(1, 2)).certificate(1)
        with self.assertRaises(ValueError):
            br.first_crossing_deficit((Q(1, 2),) * 4, 1)
        with self.assertRaises(ValueError):
            br.window_mass((Q(1, 20),) * 12)
        with self.assertRaises(ValueError):
            br.rectified_cdf((Q(1, 20),) * 9, Q(0))
        for widths in ((), (Q(2),), [Q(1)], (1,)):
            with self.assertRaises(ValueError):
                br.integer_charge_filter(widths, 1)
        with self.assertRaises(ValueError):
            br.integer_charge_filter((Q(1),), True)
        for args in ((1, 0, 0), (3, -1, 0), (3, 0, 3), (3, 0, True)):
            with self.assertRaises(ValueError):
                br.LiftedAddress(*args)
        with self.assertRaises(ValueError):
            br.LiftedAddress.from_label(0, 5)


if __name__ == "__main__":
    unittest.main()
