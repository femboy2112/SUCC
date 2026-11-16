"""Source-faithful finite certificates and hostile controls, not a density proof."""
from fractions import Fraction as F
import unittest

from observational_succ import carry_quadrature as m
from observational_succ.bbp_spatial_haar_lift import complete_source_states


class CarryQuadratureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.states = complete_source_states(268)

    def test_echo_exactly_matches_unwrapped_source(self):
        for n in range(4, 257):
            pulse = m.source_pulse(n)
            self.assertEqual(pulse.response,
                             self.states[n+pulse.delay]-pulse.harmonic*self.states[n])
            self.assertTrue(F(1, 128) < pulse.response < F(1, 4))

    def test_scale_boundaries_and_large_source_holdouts(self):
        for power in range(1, 12):
            for n in (4**power-1, 4**power, 4**power+1):
                if n < 4:
                    continue
                pulse = m.source_pulse(n)
                self.assertLessEqual(n*n, pulse.harmonic)
                self.assertLess(pulse.harmonic, 16*n*n)
                self.assertTrue(F(1, 128) < pulse.response < F(1, 4))

    def test_reference_and_carry_phase_exponents_exact(self):
        # The complex decoder cancels J algebraically. Verify all its exponent
        # transports against independently constructed unwrapped source states.
        for n in (4, 5, 16, 17, 63, 64, 127, 128, 255):
            pulse = m.source_pulse(n)
            u, v = self.states[n], self.states[n+pulse.delay]
            a, b = (v/4) % 1, (pulse.harmonic*u/4) % 1
            self.assertEqual((a-b) % 1, (pulse.response/4) % 1)
            self.assertEqual((a-(v % 1)/4) % 1, F(v.__floor__() % 4, 4))

    def test_authentic_closed_loops_flip_next_bit(self):
        for k in range(7):
            for n in range(48):
                delta = self.states[n+2**k]-self.states[n]
                self.assertEqual(m.dyadic_residue(delta, k+1), 2**k)
                cdelta = self.states[n+2**k].__floor__()-self.states[n].__floor__()
                ydelta = self.states[n+2**k] % 1-self.states[n] % 1
                self.assertEqual(cdelta % 2**(k+1),
                                 (2**k-m.dyadic_residue(ydelta, k+1)) % 2**(k+1))

    def test_four_pole_clock_cofactor_transport(self):
        for n, u in enumerate(self.states):
            self.assertEqual(m.dyadic_residue(u, 2), n % 4)
            self.assertEqual((n-m.dyadic_residue(u % 1, 2)) % 4, u.__floor__() % 4)
        self.assertEqual([m.carry_quadrature(c) for c in range(4)], [1, -1, -1, 1])

    def test_certified_prefix_raw_carries_vs_direct_rational_path(self):
        _, observations = m.certified_carry_observations(256, 4, 16)
        for observation in observations:
            u = self.states[observation.n]
            self.assertEqual(observation.carry_mod4, u.__floor__() % 4)
            self.assertEqual(observation.cofactor_mod4, m.dyadic_residue(u % 1, 2))
        shell = m.shell_statistics(observations, 128, 128)
        self.assertEqual(shell["selected_fraction"], "9/16")
        self.assertEqual(sum(map(sum, shell["clock_cofactor_counts"])), 128)

    def test_borrow_is_paid_and_ambiguity_not_guessed(self):
        self.assertEqual(m.borrow_decision(4, F(1, 2), F(3, 4))[0], 0)
        self.assertEqual(m.borrow_decision(4, F(0), F(1, 100000))[0], 1)
        self.assertIsNone(m.borrow_decision(4, F(0), F(1), depth=0)[0])

    def test_quantized_winding_packet_rational_lower_bound(self):
        events = 0
        for n in range(1, 256):
            k, a, b = m.nearest_winding(self.states[n], self.states[n+1])
            if k:
                events += 1
                self.assertGreater(16*abs(a)+abs(b), F(3, 4))
                self.assertGreater(16*(a*a+b*b), F(9, 257))
        self.assertGreater(events, 0)

    def test_quantized_charge_one_can_have_arbitrarily_long_period(self):
        for length in (1, 2, 3, 7, 19):
            x = F(1, 16**length-1)
            digits = []
            for _ in range(length):
                digit = (16*x).__floor__()
                digits.append(digit)
                x = 16*x-digit
            self.assertEqual(x, F(1, 16**length-1))
            self.assertEqual(sum(digits), 1)
            self.assertEqual(sum(m.selected_event(d) for d in digits), 1)

    def test_incorrect_domains_rejected(self):
        for n in (True, 0, 3, 4.0):
            with self.assertRaises(ValueError):
                m.source_pulse(n)
        with self.assertRaises(ValueError):
            m.dyadic_residue(F(1, 2), 2)
        with self.assertRaises(ValueError):
            m.borrow_decision(4, F(1), F(0))
        with self.assertRaises(ValueError):
            m.certified_carry_observations(5, 8, 4)


if __name__ == "__main__":
    unittest.main()
