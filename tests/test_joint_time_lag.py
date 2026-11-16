"""Exact independent formula checks and hostile controls for joint lag tools."""
import unittest
from fractions import Fraction as Q

from observational_succ.duck_bbp import forcing, tail_interval
from observational_succ.oily_signed_certificate import Interval, character_enclosure
from observational_succ.joint_time_lag import (
    gaussian_correlations, signed_fejer, schur_fejer, squared_mean,
    inverse_lag_certificate, centered, authentic_circle_path,
    source_fejer_transport_upper, source_mean_transport_upper,
    padded_window_energy, source_shell_certificate,
)


ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def direct_windows(values, h):
    n = len(values)
    energy = Q()
    for m in range(1-h, n):
        a = sum((Q(values[j][0]) for j in range(max(0, m), min(n, m+h))), Q())
        b = sum((Q(values[j][1]) for j in range(max(0, m), min(n, m+h))), Q())
        energy += a*a+b*b
    return energy/(n*h*h)


class JointTimeLagTests(unittest.TestCase):
    def test_exact_time_lag_cocycle_and_graph_resonance(self):
        for x in (Q(1, 255), Q(7, 31), Q(123, 997)):
            for n in (0, 3, 11):
                for lag, other in ((1, 2), (3, 7)):
                    d = lambda j, ell: (16**ell-1)*16**j*x
                    self.assertEqual(d(n, lag+other), d(n, lag)+d(n+lag, other))
                    # Resonant (a,b)=(-16^lag,1) has exactly zero phase.
                    self.assertEqual(-16**lag*16**n*x+16**(n+lag)*x, 0)

    def test_signed_windows_independent_and_vdc(self):
        for n in (5, 17, 53):
            for word in (tuple(ROOTS[0] for _ in range(n)),
                         tuple(ROOTS[(2*j) % 4] for j in range(n)),
                         tuple(ROOTS[j % 4] for j in range(n)),
                         tuple(ROOTS[(j*j+3*j+j//3) % 4] for j in range(n))):
                for h in (1, 2, 3, n):
                    energy = signed_fejer(word, h)
                    self.assertEqual(energy, direct_windows(word, h))
                    self.assertGreaterEqual(energy, 0)
                    self.assertLessEqual(squared_mean(word), Q(n+h-1, n)*energy)
                    rects = tuple((Interval(a, a), Interval(b, b)) for a, b in word)
                    box = padded_window_energy(rects, h)
                    self.assertEqual((box.lower, box.upper), (energy, energy))
        word = ((Q(3, 5), Q(4, 5)), (Q(5, 13), Q(-12, 13)), (0, 1))
        for h in (1, 2, 3, 7):
            self.assertEqual(signed_fejer(word, h), direct_windows(word, h))

    def test_conjugation_orientation_mutation_detected(self):
        c = gaussian_correlations(ROOTS, 2)
        self.assertEqual(c[1], (Q(), Q(3, 4)))
        # Omitting conjugation would sum i,-i,i and give i/4 instead.
        self.assertNotEqual(c[1], (Q(), Q(1, 4)))

    def test_schur_lift_window_comparison(self):
        for n in (5, 17, 53):
            values = tuple(ROOTS[(j*j+j//3) % 4] for j in range(n))
            for h in (3, 7, 19, 61):
                gh = schur_fejer(values, h)
                for j in (1, 2, 3):
                    if j > h:
                        continue
                    gj = schur_fejer(values, j)
                    r = Q(j, h)
                    excess = gh-gj-r*r
                    if excess > 0:
                        self.assertLessEqual(excess*excess, 4*gj*r*r)
                    if h % j == 0:
                        self.assertLessEqual(gh, gj)

    def test_signed_cancellation_can_disappear_under_absolute_values(self):
        values = tuple(ROOTS[n % 4] for n in range(52))
        c = gaussian_correlations(values, 13)
        absolute = sum((Q(2*(13-l), 13**2)*Q(52-l, 52)
                        for l in range(1, 13)), Q())
        self.assertGreater(absolute, Q(4, 5))
        self.assertLess(signed_fejer(values, 13), Q(1, 50))
        self.assertEqual(squared_mean(values), 0)
        self.assertTrue(all(a*a+b*b == Q(52-l, 52)**2
                            for l, (a, b) in enumerate(c)))

    def test_inverse_fifteen_aliases_and_anchor(self):
        eps = Q(1, 32)
        for n in (1, 2, 7, 19):
            for k in range(15):
                delta = Q(k, 15)+eps/(30*16**(n-1))
                result = inverse_lag_certificate(delta, n, eps)
                self.assertEqual(result['alias'], k)
                self.assertEqual(result['anchored'], k == 0)
                self.assertFalse(result['original_zero_authenticated'])

    def test_threshold_is_strict_and_period_two_breaks_inverse(self):
        delta = Q(1, 255)
        self.assertTrue(abs(centered(delta)) <= Q(1, 30))
        self.assertTrue(all(abs(centered(15*16**n*delta)) == Q(1, 17)
                            for n in range(19)))
        with self.assertRaises(ValueError):
            inverse_lag_certificate(delta, 19, Q(1, 17))
        self.assertGreater(abs(centered(delta)), Q(1, 17)/(15*16**18))

    def test_one_bad_record_defeats_average_error_version(self):
        delta = Q(1, 240)
        self.assertLess(abs(centered(delta)), Q(1, 30))
        self.assertEqual(centered(15*delta), Q(1, 16))
        self.assertTrue(all(centered(15*16**n*delta) == 0 for n in range(1, 31)))
        self.assertTrue(all(centered(16**n*delta-Q(1, 15)) == 0
                            for n in range(1, 31)))
        with self.assertRaises(ValueError):
            inverse_lag_certificate(delta, 31, Q(1, 32))

    def test_original_source_and_mutated_forcing(self):
        states = authentic_circle_path(100)
        for n in range(1, 101):
            source = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            self.assertEqual(source, forcing(n))
            self.assertEqual(states[n], (16*states[n-1]+source) % 1)
        # Flipping -2/4 adds an integer: the first circle observation is blind.
        alias = Q(4, 1)+Q(2, 4)-Q(1, 5)-Q(1, 6)
        self.assertNotEqual(forcing(1), alias)
        self.assertEqual(states[1], alias % 1)
        mutant = Q(4, 1)-Q(2, 4)+Q(1, 5)-Q(1, 6)
        self.assertNotEqual(states[1], mutant % 1)

    def test_finite_tail_difference_budget(self):
        for n in (8, 19, 53):
            for lag in (1, 3, 11):
                lo, hi = tail_interval(n, 8)
                lo2, hi2 = tail_interval(n+lag, 8)
                self.assertGreater(lo-hi2, 0)
                self.assertLess(hi-lo2, Q(lag, 32*n**3))

    def test_source_certificate_intersects_direct_completed_windows(self):
        b, h, length = 16, 2, 4
        certificate = source_shell_certificate(b, length, h)
        path = authentic_circle_path(2*b)
        rects = []
        for n in range(b, 2*b):
            lo, hi = tail_interval(n, 8)
            radius = Q(44*abs(h), 7)*(hi-lo)/2
            real, imag = character_enclosure(h*(path[n]+(lo+hi)/2))
            rects.append((Interval(real.lower-radius, real.upper+radius),
                          Interval(imag.lower-radius, imag.upper+radius)))
        direct = padded_window_energy(rects, length)
        proposed = certificate['completed_fejer']
        self.assertLessEqual(max(direct.lower, proposed.lower),
                             min(direct.upper, proposed.upper))
        self.assertTrue(certificate['original_zero_authenticated'])
        self.assertFalse(certificate['infinite_cancellation_proved'])

    def test_source_window_enclosure_against_direct_signed_lags(self):
        b, length, h = 19, 7, 3
        certificate = source_shell_certificate(b, length, h)
        path = authentic_circle_path(2*b)
        direct = Interval(Q(1, length), Q(1, length))
        for lag in range(1, length):
            for n in range(b, 2*b-lag):
                real, _ = character_enclosure(h*(path[n+lag]-path[n]))
                direct = direct + real.scale(Q(2*(length-lag), b*length**2))
        window = certificate['rational_fejer']
        self.assertLessEqual(max(direct.lower, window.lower),
                             min(direct.upper, window.upper))

    def test_source_transport_bounds_and_domains(self):
        self.assertEqual(source_fejer_transport_upper(16, 1), 0)
        self.assertLess(source_fejer_transport_upper(97, 11, 2),
                        2*source_mean_transport_upper(97, 2))
        for call in (lambda: source_shell_certificate(3, 4),
                     lambda: source_shell_certificate(16, 4, 0),
                     lambda: gaussian_correlations(((1.0, 0),), 2),
                     lambda: gaussian_correlations(((1, 1),), 2)):
            with self.assertRaises(ValueError):
                call()


if __name__ == '__main__':
    unittest.main()
