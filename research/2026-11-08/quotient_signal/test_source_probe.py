"""Meaningful exact controls of the outward quotient implementation."""
from fractions import Fraction as Q
import unittest
from source_probe import Box, Interval, ONE, ZERO, SCALE, phase, project, diagnostics


class SourceQuotientTests(unittest.TestCase):
    def test_nonuniform_fibers_preserve_weighted_mean(self):
        values = [Box(Interval.ratio(v)) for v in (1, 3, 7, 9, 11)]
        got = project(values, (0, 0, 1, 1, 1))
        self.assertEqual([v.re.lo for v in got], [2*SCALE]*2+[9*SCALE]*3)

    def test_sharp_conjugate_and_refinement(self):
        a = [Box(ONE), Box(-ONE), Box(im=ONE), Box(im=-ONE)]
        b, z = [x.conjugate() for x in a], [Box(ONE)]*4
        coarse = diagnostics(a, b, z, [0]*4)
        fine = diagnostics(a, b, z, list(range(4)))
        self.assertEqual(coarse['residual']['re'], [SCALE, SCALE])
        self.assertEqual(coarse['demodulation_gap_squared'], [SCALE, SCALE])
        self.assertEqual(fine['residual']['re'], [0, 0])
        self.assertEqual(fine['coarse_signal']['re'], [SCALE, SCALE])

    def test_measurable_carrier_does_not_require_predictable_complement(self):
        a = [Box(ONE), Box(ONE), Box(-ONE), Box(-ONE)]
        b = [Box(ONE), Box(-ONE), Box(ONE), Box(-ONE)]
        z = [x*y for x, y in zip(a, b)]
        out = diagnostics(a, b, z, [0, 0, 1, 1])
        self.assertEqual(out['Va'], [0, 0])
        self.assertEqual(out['Vb'], [SCALE, SCALE])
        self.assertEqual(out['residual']['re'], [0, 0])

    def test_signed_cancellation_survives_magnitude_failure(self):
        a = [Box(ONE), Box(-ONE), Box(ONE), Box(-ONE)]
        b = [Box(ONE), Box(-ONE), Box(-ONE), Box(ONE)]
        z = [x*y for x, y in zip(a, b)]
        out = diagnostics(a, b, z, [0]*4)
        self.assertEqual(out['Va'], [SCALE, SCALE])
        self.assertEqual(out['Vb'], [SCALE, SCALE])
        self.assertEqual(out['W']['re'], [0, 0])

    def test_transcript_measurable_gauge_preserves_quotient(self):
        a = [Box(ONE), Box(-ONE), Box(im=ONE), Box(im=-ONE)]
        b = [Box(ONE), Box(im=ONE), Box(-ONE), Box(im=-ONE)]
        g = [Box(im=ONE), Box(im=ONE), Box(-ONE), Box(-ONE)]
        labels = [0, 0, 1, 1]
        z = [x*y for x, y in zip(a, b)]
        first = diagnostics(a, b, z, labels)
        second = diagnostics([x*y for x, y in zip(a, g)],
                             [x*y.conjugate() for x, y in zip(b, g)], z, labels)
        for key in ('coarse_signal', 'residual', 'Va', 'Vb', 'demodulation_gap_squared'):
            self.assertEqual(first[key], second[key])

    def test_invalid_partition(self):
        with self.assertRaises(ValueError):
            project([], [])
        with self.assertRaises(ValueError):
            project([Box()], [])


if __name__ == '__main__':
    unittest.main()
