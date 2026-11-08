from fractions import Fraction as Q
import unittest
from lag_instrument import (Box, Interval, SCALE, ONE, ZERO, phase, mean,
                            lag_means, sliding_energy, energy_from_lags,
                            signed_transport, verdict)


def gaussian(a, b=0):
    return Box(Interval.ratio(a), Interval.ratio(b))


class LagInstrumentTests(unittest.TestCase):
    def test_exact_boundary_for_constant_phase(self):
        for A in (2, 5, 17):
            for H in range(1, A+1):
                expected = 1-Q(H*H-1, 3*A*H)
                got = sliding_energy([gaussian(1)]*A, H)
                self.assertLessEqual(Q(got.lo, SCALE), expected)
                self.assertGreaterEqual(Q(got.hi, SCALE), expected)

    def test_independent_direct_gaussian_windows(self):
        values = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 0), (-1, 0), (0, 1)]
        boxes = [gaussian(*v) for v in values]
        A = len(values)
        for H in range(1, A+1):
            numerator = 0
            for t in range(1-H, A):
                selected = [values[t+j] for j in range(H) if 0 <= t+j < A]
                numerator += sum(v[0] for v in selected)**2 + sum(v[1] for v in selected)**2
            exact = Q(numerator, A*H*H)
            direct = sliding_energy(boxes, H)
            from_lags, _ = energy_from_lags(lag_means(boxes, H), H)
            for got in (direct, from_lags):
                self.assertLessEqual(Q(got.lo, SCALE), exact)
                self.assertGreaterEqual(Q(got.hi, SCALE), exact)

    def test_signed_interference_is_not_unsigned(self):
        values = [gaussian((-1)**n) for n in range(16)]
        signed, unsigned = energy_from_lags(lag_means(values, 4), 4)
        self.assertLess(signed.hi, SCALE//10)
        self.assertGreater(unsigned.lo, SCALE*8//10)

    def test_periodic_control_requires_every_harmonic(self):
        base = [gaussian(1), gaussian(0, 1), gaussian(-1), gaussian(0, -1)]*4
        self.assertEqual(verdict(sliding_energy(base, 4), 1, 10), 'PASS_FINITE')
        self.assertEqual(verdict(sliding_energy([gaussian(1)]*16, 4), 1, 2), 'REFUTED_FINITE')

    def test_phase_transport_and_bilinear_covariance(self):
        a = [gaussian(1), gaussian(0, 1), gaussian(-1), gaussian(0, -1)]
        full = [gaussian(0, 1)]*4
        cov, marg = signed_transport(a, full)
        self.assertTrue((cov+marg).im.overlaps(ONE))
        self.assertLess(abs(cov.re.lo), 10)
        self.assertGreater(cov.im.lo, SCALE-10)

    def test_nonunit_diagonal_is_explicit(self):
        values = [gaussian(2)]*5
        lags = lag_means(values, 3)
        right, _ = energy_from_lags(lags, 3, Interval.ratio(4))
        wrong, _ = energy_from_lags(lags, 3)
        direct = sliding_energy(values, 3)
        self.assertTrue(right.overlaps(direct))
        self.assertFalse(wrong.overlaps(direct))

    def test_rational_phase_conjugate_control(self):
        a = [phase(n, 17) for n in range(8)]
        full = [gaussian(1)]*8
        cov, marg = signed_transport(a, full)
        self.assertTrue((cov+marg).re.overlaps(ONE))
        self.assertTrue((cov+marg).im.overlaps(ZERO))

    def test_invalid_apertures(self):
        for H in (0, -1, 3, True, 1.5):
            with self.assertRaises(ValueError):
                sliding_energy([gaussian(1)]*2, H)
        with self.assertRaises(ValueError):
            signed_transport([], [])


if __name__ == '__main__':
    unittest.main()
