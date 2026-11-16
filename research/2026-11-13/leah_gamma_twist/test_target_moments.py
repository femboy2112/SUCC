"""Non-vacuous source, sign, coupling and error controls for target moments."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from math import comb

from observational_succ.duck_bbp import forcing, tail_interval
from observational_succ.pi_succ_character_intervals import fourier_rect
from observational_succ.selected_orbit import SelectedOrbit
from observational_succ.zero_anchored_haar import certified_phase_grid

from target_moments import (
    packet_from_exact_phases, packet_from_grid, target_interval,
    signed_moment_coordinates, verify_packet_source, rational_display,
    exponential_upper,
)


def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


class TargetMomentTests(unittest.TestCase):
    def test_grid_and_independent_fraction_moments(self):
        for denominator, terms in product((16, 32, 256), (1, 2, 4, 6)):
            points = tuple(range(denominator))
            a = packet_from_grid(points, denominator, terms)
            b = packet_from_exact_phases(
                tuple(Q(2*k+1, 2*denominator) for k in points), terms)
            self.assertEqual(a, b)

    def test_known_exact_roots(self):
        controls = ((Q(), (1, 0)), (Q(1, 4), (0, 1)),
                    (Q(1, 2), (-1, 0)), (Q(3, 4), (0, -1)))
        for z, value in controls:
            for q in (1, 2, 4, 6):
                r = target_interval(packet_from_exact_phases((z,), q))
                for key, v in zip(("real", "imag"), value):
                    self.assertLessEqual(r[key][0], v)
                    self.assertGreaterEqual(r[key][1], v)

    def test_independent_direct_character_oracle(self):
        phases = tuple(Q(a, 257) for a in (0, 1, 7, 31, 128, 222, 256))
        for h, radix, q in product((-17, -1, 1, 2, 8, 15, 17), (16, 256), (2, 6)):
            r = target_interval(packet_from_exact_phases(phases, q, radix), h)
            direct = fourier_rect(phases, h)
            self.assertTrue(overlaps(r["real"], direct[0]))
            self.assertTrue(overlaps(r["imag"], direct[1]))

    def test_complete_roots_have_zero_target(self):
        phases = tuple(Q(j, 16) for j in range(16))
        r = target_interval(packet_from_exact_phases(phases, 6))
        self.assertLessEqual(r["real"][0], 0)
        self.assertGreaterEqual(r["real"][1], 0)
        self.assertLessEqual(r["imag"][0], 0)
        self.assertGreaterEqual(r["imag"][1], 0)
        self.assertTrue(all(x == 0 for x in signed_moment_coordinates(
            packet_from_exact_phases(phases, 6))[0]))

    def test_periodic_digit_balance_does_not_give_normality(self):
        # Actual radix orbit with repeating word 0123456789abcdef.
        numerator = sum(d*16**(15-d) for d in range(16))
        seed = Q(numerator,16**16-1)
        phases = tuple((16**n*seed) % 1 for n in range(16))
        self.assertEqual((16**16*seed) % 1, seed)
        self.assertEqual(sorted(int(16*z) for z in phases),list(range(16)))
        packet = packet_from_exact_phases(phases,6)
        self.assertTrue(all(c == 0 for c in signed_moment_coordinates(packet)[0]))
        # The actual first Fourier mean is nevertheless separated from zero.
        direct = fourier_rect(phases,1)
        self.assertTrue(any(lo > 0 or hi < 0 for lo,hi in direct))
        r = target_interval(packet)
        self.assertTrue(overlaps(r['real'],direct[0]))
        self.assertTrue(overlaps(r['imag'],direct[1]))

    def test_reversing_only_the_digit_character_is_detected(self):
        z = Q(7,64)  # a=1, y=3/4; the future coordinate is held fixed.
        reversed_digit_phase = Q(63,64)  # a=-1 mod16, same y.
        right = target_interval(packet_from_exact_phases((z,),6))
        wrong = target_interval(packet_from_exact_phases((reversed_digit_phase,),6))
        self.assertFalse(overlaps(right['imag'],wrong['imag']))

    def test_same_marginals_different_pairing(self):
        left = (Q(1, 64), Q(35, 64))
        right = (Q(3, 64), Q(33, 64))
        # Same first-digit marginal (0,8), same future marginal (1/4,3/4).
        for f in (lambda z: int(16*z), lambda z: (16*z) % 1):
            self.assertEqual(sorted(map(f, left)), sorted(map(f, right)))
        a = target_interval(packet_from_exact_phases(left, 6))
        b = target_interval(packet_from_exact_phases(right, 6))
        self.assertGreater(a["real"][0], 0)
        self.assertLess(b["real"][1], 0)
        # Replacing the joining by the product kills the informative scalar.
        independent = tuple((Q(d)+y)/16 for d,y in product((0,8),(Q(1,4),Q(3,4))))
        r = target_interval(packet_from_exact_phases(independent, 6))
        self.assertLessEqual(r["real"][0], 0)
        self.assertGreaterEqual(r["real"][1], 0)

    def test_omitting_taylor_debt_is_detected(self):
        r = target_interval(packet_from_exact_phases((Q(),), 1))
        self.assertLess(r["truncated_real"][1], 1)
        self.assertEqual(r["real"][1], 1)

    def test_omitting_phase_transport_is_detected(self):
        packet = packet_from_grid((63,), 256, 6)
        r = target_interval(packet)
        exact = fourier_rect((Q(1, 4),), 1)
        self.assertFalse(overlaps(r["real"], exact[0]))
        paid = target_interval(packet, phase_error=Q(1,512))
        self.assertTrue(overlaps(paid["real"], exact[0]))

    def test_phase_rotation_mutation(self):
        # Dropping e(h/32) rotates the nearly exact target for z=0.
        direct = fourier_rect((Q(-1,32),), 1)
        r = target_interval(packet_from_exact_phases((Q(),), 6))
        self.assertFalse(overlaps(r["imag"], direct[1]))

    def test_source_grid_against_exact_recurrence_and_tail(self):
        cert = certified_phase_grid(17, 17, depth=6, guard=16)
        orbit = SelectedOrbit()
        for n,k in enumerate(cert.points, cert.start):
            lo,hi = tail_interval(n, 16)
            a,b = orbit.state(n)+lo, orbit.state(n)+hi
            integer_part = a.numerator//a.denominator
            self.assertEqual(integer_part, b.numerator//b.denominator)
            self.assertGreater(a-integer_part, Q(k,cert.denominator))
            self.assertLess(b-integer_part, Q(k+1,cert.denominator))
        packet = packet_from_grid(cert.points,cert.denominator,6)
        self.assertTrue(verify_packet_source(cert, packet))
        self.assertFalse(verify_packet_source(
            replace(cert, points=(cert.points[0]+1,)+cert.points[1:]), packet))

    def test_alias_does_not_authenticate_zero(self):
        true, alias = SelectedOrbit(), SelectedOrbit(Q(1,16))
        self.assertNotEqual(true.seed, alias.seed)
        for n in range(1,35):
            self.assertEqual(true.state(n), alias.state(n))

    def test_conditioning_and_display(self):
        r = target_interval(packet_from_exact_phases((Q(),),6))
        self.assertLess(r["coefficient_norm_upper"], Q(61,50))
        self.assertLess(r["taylor_remainder"], Q(1,10**7))
        self.assertEqual(rational_display((Q(-1,3),Q(1,3)),3),
                         ("-0.334","0.334"))

    def test_binomial_prefix_ambiguity(self):
        # Exact probability witnesses for TM-03: no float matching tolerance.
        for q in range(1, 9):
            r = Q(9, 10)
            phases = [[], []]
            for k in range(q+1):
                u = -r+2*r*k/q
                phases[k % 2].extend([(u+1)/32]*comb(q,k))
            packets = [packet_from_exact_phases(tuple(p), q) for p in phases]
            self.assertEqual(packets[0], packets[1])
            # The next power detects the hidden signed finite difference.
            longer = [packet_from_exact_phases(tuple(p), q+1) for p in phases]
            self.assertNotEqual(longer[0].moments_by_digit,
                                longer[1].moments_by_digit)
            if q <= 6:
                direct = [fourier_rect(tuple(p), 1) for p in phases]
                self.assertTrue(any(not overlaps(a,b)
                                    for a,b in zip(*direct)))

    def test_malformed_or_forged_inputs(self):
        for f in (
            lambda: packet_from_grid((0,),17,2),
            lambda: packet_from_grid((0.0,),16,2),
            lambda: packet_from_grid((),16,2),
            lambda: packet_from_exact_phases((0.5,),2),
            lambda: target_interval(packet_from_exact_phases((Q(),),2),0),
            lambda: target_interval(packet_from_exact_phases((Q(),),2),
                                    pi_range=(Q(31,10),Q(311,100))),
            lambda: exponential_upper(Q(1)),
        ):
            with self.assertRaises((ValueError,TypeError)):
                f()


if __name__ == "__main__":
    unittest.main()
