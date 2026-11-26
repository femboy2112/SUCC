"""Exact positive, hostile and fresh arithmetic controls for the place seam."""

import unittest
from fractions import Fraction
from random import Random

from observational_succ.principia_place_seam import (
    PlaceReadout,
    archimedean_to_prime,
    canonical_seam_germs,
    path_via_trivial,
    place_readout,
    product_formula_readouts,
    rational_capacity,
    rational_prime_exponents,
    sum_log_coefficients,
    trivial_magnitude,
)


class PlaceSeamTests(unittest.TestCase):
    def test_exact_factorization_retains_denominator_and_sign(self):
        q = Fraction(-360, 77)
        self.assertEqual(
            rational_prime_exponents(q), ((2, 3), (3, 2), (5, 1), (7, -1), (11, -1))
        )
        report = place_readout(q, 7)
        self.assertEqual(report.source, q)
        self.assertEqual(report.as_dict(), {7: Fraction(1)})

    def test_canonical_endpoints_and_shared_null(self):
        q = Fraction(45, 14)
        self.assertEqual(
            archimedean_to_prime(q, 0, 3).observation,
            place_readout(q, "infinity"),
        )
        self.assertEqual(
            archimedean_to_prime(q, 1, 3).observation,
            place_readout(q, 3),
        )
        for q in [Fraction(-77, 10), Fraction(81, 25), Fraction(1), Fraction(-1)]:
            with self.subTest(q=q):
                seam = archimedean_to_prime(q, Fraction(1, 2), 3)
                self.assertEqual(seam.observation.log_coefficients, ())
                self.assertEqual(seam.observation.source, q)
                self.assertEqual(seam.start_place, "infinity")
                self.assertEqual(seam.end_place, 3)

    def test_exact_interior_coefficients(self):
        q = Fraction(12, 5)
        self.assertEqual(
            archimedean_to_prime(q, Fraction(1, 3), 2).observation.as_dict(),
            {2: Fraction(2, 3), 3: Fraction(1, 3), 5: Fraction(-1, 3)},
        )
        self.assertEqual(
            archimedean_to_prime(q, Fraction(3, 4), 2).observation.as_dict(),
            {2: Fraction(-1)},
        )

    def test_distinct_prime_places(self):
        q = Fraction(9, 25)
        self.assertEqual(path_via_trivial(q, 0, 3, 5).observation.as_dict(), {3: -2})
        self.assertEqual(path_via_trivial(q, 1, 3, 5).observation.as_dict(), {5: 2})
        self.assertEqual(
            path_via_trivial(q, Fraction(1, 2), 3, 5).observation.as_dict(), {}
        )

    def test_same_place_can_avoid_the_trivial_seam(self):
        # Positive exponent interpolation stays on one branch. Our via-trivial
        # constructor is permitted here but a zero is not logically forced.
        for t in [Fraction(j, 17) for j in range(18)]:
            exponent = (1 - t) * Fraction(1, 4) + t * Fraction(3, 4)
            self.assertTrue(place_readout(2, "infinity", exponent).log_coefficients)

    def test_multiplicativity_on_fresh_rationals_and_rational_times(self):
        rng = Random(20261126)
        for _ in range(80):
            q = Fraction(rng.choice((-1, 1)) * rng.randint(1, 1000), rng.randint(1, 1000))
            r = Fraction(rng.randint(1, 1000), rng.randint(1, 1000))
            t = Fraction(rng.randint(0, 31), 31)
            p = rng.choice((2, 3, 5, 7, 11, 13))
            combined = archimedean_to_prime(q * r, t, p).observation.log_coefficients
            separate = sum_log_coefficients(
                archimedean_to_prime(x, t, p).observation.log_coefficients
                for x in (q, r)
            )
            self.assertEqual(combined, separate)

    def test_product_formula_same_source_fresh_holdouts(self):
        for numerator in (-1001, -343, -1, 1, 143, 4095):
            for denominator in (8, 45, 121, 221):
                q = Fraction(numerator, denominator)
                reports = product_formula_readouts(q)
                self.assertTrue(all(report.source == q for report in reports))
                self.assertEqual(
                    sum_log_coefficients(report.log_coefficients for report in reports), ()
                )

    def test_changed_source_product_formula_mutant_is_visible(self):
        reports = list(product_formula_readouts(Fraction(12, 5)))
        reports[0] = place_readout(Fraction(18, 5), "infinity")
        self.assertNotEqual(
            sum_log_coefficients(report.log_coefficients for report in reports), ()
        )

    def test_unpaid_power_normalization_mutant_is_visible(self):
        reports = list(product_formula_readouts(18))
        reports[0] = place_readout(18, "infinity", Fraction(1, 2))
        self.assertNotEqual(
            sum_log_coefficients(report.log_coefficients for report in reports), ()
        )

    def test_oriented_germs_recover_nonzero_endpoint_content(self):
        q = Fraction(18, 5)
        left, right = canonical_seam_germs(q, 3)
        self.assertEqual(dict(left), {2: -2, 3: -4, 5: 2})
        self.assertEqual(dict(right), {3: -4})
        for t in (Fraction(1, 4), Fraction(7, 16), Fraction(9, 16), Fraction(3, 4)):
            coefficients = archimedean_to_prime(q, t, 3).observation.log_coefficients
            derivative = tuple((p, c / (t - Fraction(1, 2))) for p, c in coefficients)
            self.assertEqual(derivative, left if t < Fraction(1, 2) else right)

    def test_null_magnitude_does_not_erase_source_or_equality(self):
        a, b = Fraction(7, 11), Fraction(13, 17)
        self.assertEqual(trivial_magnitude(a), trivial_magnitude(b))
        self.assertEqual(trivial_magnitude(a - a), 0)
        self.assertEqual(trivial_magnitude(b - a), 1)
        self.assertNotEqual(
            archimedean_to_prime(a, Fraction(1, 2), 2).observation.source,
            archimedean_to_prime(b, Fraction(1, 2), 2).observation.source,
        )

    def test_fake_places_and_invalid_domain_rejected(self):
        for p in (0, 1, 4, 9, 15, True, 3.0):
            with self.subTest(p=p):
                with self.assertRaises(ValueError):
                    archimedean_to_prime(3, Fraction(1, 4), p)
        for t in (-1, Fraction(5, 4)):
            with self.assertRaises(ValueError):
                archimedean_to_prime(3, t, 2)
        with self.assertRaises(ValueError):
            place_readout(2, "infinity", 2)
        with self.assertRaises(ValueError):
            place_readout(2, 3, -1)
        with self.assertRaises(ValueError):
            place_readout(0, 3)
        with self.assertRaises(ValueError):
            sum_log_coefficients([((6, Fraction(1)),)])

    def test_float_inputs_rejected_instead_of_silently_rationalized(self):
        for operation in (
            lambda: archimedean_to_prime(3.0, Fraction(1, 4), 2),
            lambda: archimedean_to_prime(3, 0.25, 2),
            lambda: place_readout(3, 2, 0.5),
            lambda: trivial_magnitude(0.0),
            lambda: rational_prime_exponents(True),
        ):
            with self.assertRaises(TypeError):
                operation()

    def test_forged_source_readout_rejected(self):
        with self.assertRaises(ValueError):
            PlaceReadout(Fraction(12), 3, Fraction(1), ((3, Fraction(-2)),))
        with self.assertRaises(TypeError):
            PlaceReadout(Fraction(3), 3, Fraction(1), ((3, -1.0),))

    def test_paid_denominator_capacity_and_mutations(self):
        report = rational_capacity(Fraction(-72, 35), 35, ((2, 3), (3, 2)))
        self.assertEqual(report.integral_witness, -72)
        self.assertEqual(report.divisor, 72)
        self.assertEqual(report.magnitude_lower_bound, Fraction(72, 35))
        # Ignoring D would invent the false lower bound 72 on |source|.
        self.assertLess(abs(report.source), report.divisor)
        for operation in (
            lambda: rational_capacity(Fraction(72, 35), 7, ((2, 3),)),
            lambda: rational_capacity(Fraction(72, 35), 35, ((2, 4),)),
            lambda: rational_capacity(72, 1, ((2, 2), (2, 2))),
            lambda: rational_capacity(72, 1, ((6, 1),)),
            lambda: rational_capacity(0, 1, ((2, 1),)),
        ):
            with self.assertRaises(ValueError):
                operation()


if __name__ == "__main__":
    unittest.main()
