"""Exact finite verification, independent source checks and hostile controls."""
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ import pi_source_genesis as g
from observational_succ.bbp_source_memory import (
    forcing, tail_interval, rational_counterfeit_tail,
    rational_counterfeit_forcing, high_order_partial_fractions,
    high_order_rational_forcing, false_deepseek_cost_bound_witness)


def overlaps(a, b):
    return (max(a.real_low, b.real_low) <= min(a.real_high, b.real_high)
            and max(a.imag_low, b.imag_low) <= min(a.imag_high, b.imag_high))


class SourceGenesisExact(unittest.TestCase):
    def test_endpoint_coefficients_independent_division_and_pell(self):
        # Independent division of H(1+s)/(16-(1+s)^8), before cancellation.
        H = (4, 4, 4, 2, 1)
        a = []
        for k in range(21):
            hk = sum(H[j]*comb(j, k) for j in range(k, len(H)))
            a.append((Q(hk)+sum(comb(8, j)*a[k-j]
                                for j in range(1, min(8, k)+1)))/15)
        self.assertEqual(tuple(a), g.endpoint_coefficients(20))
        p = [0, 1]
        for _ in range(12):
            p.append(2*p[-1]+p[-2])
        for k, value in enumerate(a):
            self.assertEqual(value, p[k//2+1]*p[(k+1)//2+1])

    def test_global_beta_envelopes_against_positive_green_sum(self):
        for n in (0, 1, 2, 5, 11, 40, 101):
            actual_low, actual_high = tail_interval(n, 30)
            for order in range(9):
                low, high = g.tail_beta_interval(n, order)
                self.assertLess(low, actual_low)
                self.assertGreater(high, actual_high)
        self.assertEqual(g.tail_beta_interval(0, 0), (0, Q(1, 2)))
        self.assertEqual(g.tail_beta_interval(1, 1), (Q(7, 990), Q(1, 90)))

    def test_finite_difference_sign_certificates(self):
        for n in range(5):
            for k in range(7):
                lower = Q()
                for j in range(k+1):
                    lo, hi = tail_interval(n+j, 25)
                    c = (-1)**j*comb(k, j)
                    lower += c*(lo if c > 0 else hi)
                self.assertGreater(lower, 0)

    def test_total_tail_one_sixtieth_certificate(self):
        # For n>=5, sum B_n <=1/(4*(16*5-5))=1/300.
        bound = sum((tail_interval(n, 4)[1] for n in range(1, 5)), Q())+Q(1, 300)
        self.assertLess(bound, Q(1, 60))

    def test_exact_initial_state_separation(self):
        authentic = g.forced_states(20)
        changed = g.forced_states(20, Q(1, 3))
        self.assertEqual(authentic[1], Q(2, 15))
        self.assertEqual(changed[1], Q(7, 15))
        for n in range(21):
            self.assertEqual((changed[n]-authentic[n]) % 1, Q(1, 3))
        self.assertNotEqual(changed[1], Q(1, 3))

    def test_lag_telescoping_independent_finite_sum(self):
        for start, length, lag in ((1, 7, 3), (4, 3, 7), (2, 5, 0), (3, 0, 8)):
            low, high = g.lag_tail_mass_interval(start, length, lag)
            # Midpoint values separately, with independently summed radii.
            mid = err = Q()
            for j in range(length):
                a, b = tail_interval(start+j, 15)
                c, d = tail_interval(start+j+lag, 15)
                mid += (a+b-c-d)/2
                err += (b-a+d-c)/2
            self.assertLessEqual(low, mid+err)
            self.assertGreaterEqual(high, mid-err)
            if length and lag:
                self.assertGreater(low, 0)
                self.assertLess(8*high, g.lag_transport_budget(1, start, length, lag))

    def test_horizon_matched_source_vs_independent_machin(self):
        ml, mu = g.machin_pi_interval(90)
        for horizon in (1, 3, 10, 32):
            for lookahead in (0, 2, 7):
                lo, hi = g.window_pi_interval(horizon, lookahead)
                self.assertLess(lo, ml)
                self.assertGreater(hi, mu)
                for lag in (0, horizon-1):
                    actual_budget = 8*(hi-lo)*(16**lag-1)*Q(16**(horizon-lag)-1, 15)
                    self.assertLessEqual(actual_budget,
                                         g.window_lag_transport_budget(1, horizon, lag, lookahead))

    def test_character_interval_known_values_and_wrap(self):
        for phase, real, imag in ((0, 1, 0), (Q(1,4), 0, 1),
                                   (Q(1,2), -1, 0), (Q(3,4), 0, -1), (1, 1, 0)):
            box = g.character_interval(phase, phase)
            self.assertTrue(box.real_low <= real <= box.real_high)
            self.assertTrue(box.imag_low <= imag <= box.imag_high)
        box = g.character_interval(Q(999, 1000), Q(1001, 1000))
        self.assertTrue(box.real_low <= 1 <= box.real_high)
        self.assertTrue(box.imag_low < 0 < box.imag_high)

    def test_signed_correlations_three_sources(self):
        for h, horizon, lag in ((1, 4, 1), (-1, 5, 2), (2, 8, 3), (1, 12, 11)):
            bbp = g.correlation_interval(h, horizon, lag)
            machin = g.correlation_interval(h, horizon, lag, source="machin")
            self.assertTrue(overlaps(bbp, machin))
            forced = g.correlation_interval(h, horizon, lag, source="forced")
            self.assertLess((bbp-forced).modulus_squared_upper(),
                            g.lag_transport_budget(h, 1, horizon-lag, lag)**2)
            partial = g.correlation_interval(h, horizon, lag, source="partial", lookahead=0)
            self.assertLess((bbp-partial).modulus_squared_upper(),
                            g.window_lag_transport_budget(h, horizon, lag)**2)
            # Opposite Fourier sign is conjugation, not absolute-value data.
            opposite = g.correlation_interval(-h, horizon, lag)
            conjugate = g.ComplexBox(bbp.real_low, bbp.real_high, -bbp.imag_high, -bbp.imag_low)
            self.assertTrue(overlaps(opposite, conjugate))

    def test_positive_rank_counterfeit_has_no_cancellation(self):
        y = Q()
        for n in range(1, 30):
            y = (16*y+rational_counterfeit_forcing(n)) % 1
            self.assertEqual((y+rational_counterfeit_tail(n)) % 1, 0)
        # Generic circle and source counterexamples occupy different classes.
        self.assertEqual((16*Q(1,3)) % 1, Q(1,3))
        self.assertNotEqual(rational_counterfeit_forcing(1), forcing(1))
        self.assertEqual(false_deepseek_cost_bound_witness()["lhs_over_sqrt2"], Q(4,3))
        for k in range(1, 7):
            for n in (1, 3, 17):
                self.assertEqual(high_order_partial_fractions(n, k), high_order_rational_forcing(n, k))

    def test_odd_truncation_dyadic_conductor_and_preperiod(self):
        for m in range(1, 32, 2):
            p = g.window_pi_interval(m)[0]
            q = p.denominator
            valuation = (q & -q).bit_length()-1
            self.assertEqual(valuation, 4*(m-1))
            reduced = p*16**(m-1)
            self.assertEqual(reduced.denominator % 2, 1)
            if m > 1:
                self.assertEqual((p*16**(m-2)).denominator % 16, 0)

    def test_lag_observation_does_not_identify_initial_state(self):
        actual = g.forced_states(16)
        for shift in (Q(1,15), Q(1,3), Q(2,5)):
            changed = g.forced_states(16, shift)
            for j in range(1, 9):
                for lag in (1, 3, 7):
                    self.assertEqual((changed[j+lag]-changed[j]) % 1,
                                     (actual[j+lag]-actual[j]) % 1)

    def test_corrected_error_positive_decreasing_and_mass_bound(self):
        for order in range(5):
            for start in (1, 3, 9):
                total_upper = Q()
                for n in range(start, start+12):
                    low, high = tail_interval(n, 35)
                    b0, b1 = g.tail_beta_interval(n, order)
                    # P_K is lower for K even, upper for K odd.
                    p = b0 if order % 2 == 0 else b1
                    error_low, error_high = ((low-p, high-p) if order % 2 == 0
                                             else (p-high, p-low))
                    self.assertGreater(error_low, 0)
                    total_upper += error_high
                    nl, nu = tail_interval(n+1, 35)
                    c0, c1 = g.tail_beta_interval(n+1, order)
                    np = c0 if order % 2 == 0 else c1
                    next_high = nu-np if order % 2 == 0 else np-nl
                    self.assertLess(next_high, error_low)
                self.assertLess(8*total_upper,
                                g.corrected_lag_transport_budget(1, start, order))

    def test_3adic_complete_orbit_resonance(self):
        from observational_succ.circle_time_carry import orbit_3adic
        for level in range(2, 5):
            orbit = orbit_3adic(level)
            # Complete actual rational source; every lag at the period resonates.
            self.assertEqual(pow(16, len(orbit), 3**level), 1)
            for residue in orbit:
                self.assertEqual(Q((16**len(orbit)-1)*residue, 3**level) % 1, 0)

    def test_type_and_domain_guards(self):
        for bad in (-1, True, 1.0):
            with self.assertRaises(ValueError):
                g.endpoint_coefficients(bad)
        with self.assertRaises(ValueError):
            g.forced_states(3, 0.1)
        with self.assertRaises(ValueError):
            g.correlation_interval(1, 3, 3)
        with self.assertRaises(ValueError):
            g.character_interval(1, 0)


if __name__ == "__main__":
    unittest.main()
