import unittest
from fractions import Fraction as Q
from observational_succ.carrier_relative_targets import CarrierError
from observational_succ.carrier_finite_part_observer import (
    ScaleReading, paired_finite_part, abel_reading, abel_finite_part,
)


class TwoScaleTargetTests(unittest.TestCase):
    def test_eliminates_unknown_divergent_amplitude_exactly(self):
        for a in (Q(-11), Q(0), Q(7, 3), Q(10**20)):
            for b in (Q(-1, 12), Q(0), Q(5)):
                t = Q(1, 8)
                f = lambda s: a/s**2+b
                first = ScaleReading("source", t, f(t), f(t))
                second = ScaleReading("source", 2*t, f(2*t), f(2*t))
                result = paired_finite_part(first, second, 0)
                self.assertEqual((result.lower, result.upper), (b, b))

    def test_200_corner_and_interior_remainders_are_enclosed(self):
        count = 0
        for denominator in range(2, 10):
            t, c, a, b = Q(1, denominator), Q(3, 7), Q(31), Q(-5, 9)
            grid = tuple(Q(j, 4) for j in range(5))
            for u in grid:
                for v in grid:
                    f1 = a/t**2+b+u*c*t*t
                    f2 = a/(2*t)**2+b+v*c*(2*t)**2
                    result = paired_finite_part(ScaleReading("s", t, f1, f1),
                        ScaleReading("s", 2*t, f2, f2), c)
                    self.assertLessEqual(result.lower, b)
                    self.assertGreaterEqual(result.upper, b)
                    self.assertEqual(result.upper-result.lower, 17*c*t*t/3)
                    count += 1
        self.assertEqual(count, 200)

    def test_two_extremal_remainders_attain_each_end(self):
        t, c = Q(1, 4), Q(1, 2)
        for r1, r2, which in ((Q(0), 4*c*t*t, "lower"), (c*t*t, Q(0), "upper")):
            b, a = Q(7), Q(5)
            x = a/t**2+b+r1; y = a/(2*t)**2+b+r2
            result = paired_finite_part(ScaleReading("s", t, x, x), ScaleReading("s", 2*t, y, y), c)
            self.assertEqual(getattr(result, which), b)

    def test_abel_pair_encloses_known_finite_part_with_shrinking_width(self):
        old_width = Q(100)
        for d in (2, 4, 8, 16, 32, 64):
            result = abel_finite_part(Q(1, d), 32)
            self.assertLess(result.lower, Q(-1, 12))
            self.assertGreater(result.upper, Q(-1, 12))
            self.assertLess(result.upper-result.lower, old_width)
            self.assertLess(result.upper-result.lower, Q(18, 720*d*d))
            old_width = result.upper-result.lower

    def test_higher_precision_nested_readout(self):
        for t in (Q(1), Q(1, 2), Q(1, 16)):
            x = abel_reading(t, 10); y = abel_reading(t, 20)
            self.assertLessEqual(x.lower, y.lower)
            self.assertGreaterEqual(x.upper, y.upper)

    def test_source_and_scale_changes_do_not_cancel_without_transport(self):
        a = ScaleReading("a", Q(1, 4), Q(1), Q(2))
        for b in (ScaleReading("b", Q(1, 2), Q(1), Q(2)),
                  ScaleReading("a", Q(3, 4), Q(1), Q(2))):
            with self.assertRaises(CarrierError): paired_finite_part(a, b, 1)
        with self.assertRaises(CarrierError): abel_reading(0)
        with self.assertRaises(CarrierError): abel_finite_part(1)
        with self.assertRaises(CarrierError): abel_reading(.1)


if __name__ == '__main__': unittest.main()
