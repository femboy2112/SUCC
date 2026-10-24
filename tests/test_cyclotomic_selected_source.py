"""Independent exact arithmetic and certified signed controls for selected sources."""
from collections import Counter
from fractions import Fraction as Q
from math import gcd
from itertools import combinations_with_replacement
import unittest

from observational_succ import cyclotomic_selected_source as c
from observational_succ.bbp_source_memory import forcing
from observational_succ.pi_source_genesis import forced_states, window_pi_interval


class SelectedSourceCertificates(unittest.TestCase):
    def test_full_prime_power_projection_and_addition(self):
        for p in (2, 3, 5, 17):
            for k in (1, 2, 3):
                q = Q(7, p**k*19)
                part = c.primary_component(q, p)
                self.assertNotEqual((q-part).denominator % p, 0)
                self.assertEqual((part*p**k).denominator, 1)
                for r in (Q(1, 7), Q(3, p**2), Q(-9, 23)):
                    self.assertEqual(c.primary_component(q+r, p),
                                     (part+c.primary_component(r, p)) % 1)

    def test_authentic_prime_window_from_unwrapped_arithmetic(self):
        for p in (17, 41, 73, 89, 97, 113, 193):
            w = c.prime_window(p)
            self.assertEqual(w.initial, 0)
            lift = Q()
            for n in range(1, 4*w.m+1):
                # Independent convolution, before reducing integer carries.
                lift = sum((16**(n-k)*forcing(k) for k in range(1, n+1)), Q())
                if n >= w.m+1:
                    t = n-w.m-1
                    self.assertEqual(lift % 1, w.states[t])
                    self.assertEqual(c.primary_component(lift, p), w.local[t])
            for t in range(3*w.m-1):
                self.assertEqual(w.complement[t+1],
                    (16*w.complement[t]+forcing(w.m+2+t)) % 1)
            self.assertEqual(3*w.m % w.period, 0)

    def test_machin_selected_dyadic_is_independently_bbp_certified(self):
        for depth in (2, 7, 18, 30):
            control = c.dyadic_initial_control(depth)
            lo, hi = window_pi_interval(depth+8)
            initial = control['initial']
            self.assertLess(max(abs(initial+lo/16), abs(initial+hi/16)),
                            Q(1, 2*16**depth))
            self.assertLessEqual(control['error_upper'], Q(1, 2*16**depth))
            self.assertLessEqual(c.coalescence_depth(initial), depth)

    def test_dyadic_control_preserves_odd_clocks_and_eventually_coalesces(self):
        for depth in (5, 11):
            delta = c.dyadic_initial_control(depth)['initial']
            original = forced_states(depth+3)
            changed = forced_states(depth+3, delta)
            K = c.coalescence_depth(delta)
            for n, (x, y) in enumerate(zip(original, changed)):
                self.assertEqual((y-x) % 1, (16**n*delta) % 1)
                for p in (3, 5, 7, 17, 41):
                    self.assertEqual(c.primary_component(x, p), c.primary_component(y, p))
                if n >= K:
                    self.assertEqual(x, y)
            if K:
                self.assertNotEqual(original[K-1], changed[K-1])
        self.assertIsNone(c.coalescence_depth(Q(1, 3)))

    def test_same_forcing_coherent_window_is_certified_not_float(self):
        one = c.ComplexBox(Q(1), Q(1), Q(), Q())
        for p in (17, 41, 73):
            depth = (p-1)//2+2
            control = c.dyadic_initial_control(depth)
            w = c.prime_window(p, control['initial'])
            full = c.character_mean(w.states)
            budget = c.coherent_window_error(p, depth, initial_error=control['error_upper'])
            self.assertLess((full-one).modulus_squared_upper(), budget**2)
            self.assertLess(budget, Q(1, 50))
            self.assertGreater(full.real_low, Q(99, 100))

    def test_twisted_lag_expansion_as_exact_group_algebra(self):
        for p in (17, 41, 73, 97, 113):
            L = c.order(16, p)
            for h in (1, -2):
                for k in range(L):
                    direct, lags = Counter(), Counter()
                    for s in range(L):
                        for t in range(L):
                            phase = Q(4*h*(pow(16, s, p)-pow(16, t, p)), p)-Q(k*(s-t), L)
                            direct[phase % 1] += 1
                    for d in range(L):
                        for t in range(L):
                            phase = Q(4*h*(pow(16, d, p)-1)*pow(16, t, p), p)-Q(k*d, L)
                            lags[phase % 1] += 1
                    self.assertEqual(direct, lags)

    def test_all_twists_obey_certified_lag_bound(self):
        for p in (17, 41, 73, 113):
            certificate = c.twisted_clock_certificate(p)
            for box in certificate['twisted']:
                self.assertLessEqual(box.modulus_squared_upper(),
                                     certificate['twist_upper_squared'])
            self.assertLess(certificate['twist_upper_squared'], 1)

    def test_authentic_mixed_spectral_bound(self):
        for p in (17, 41, 73):
            w = c.prime_window(p)
            data = c.spectral_interference_certificate(w)
            self.assertLess(data['actual'].modulus_squared_upper(),
                            data['interference_upper']**2)
            self.assertGreater(data['wiener_upper'], 0)

    def test_integer_square_root_outward_and_signed_scaling(self):
        for x in (Q(), Q(1, 3), Q(2), Q(100, 7)):
            upper = c.sqrt_upper(x, 23)
            self.assertGreaterEqual(upper**2, x)
            if x:
                self.assertLess((upper-Q(1, 2**23))**2, x)
        box = c.ComplexBox(Q(-2), Q(3), Q(-4), Q(5))
        self.assertEqual(c.box_scale(box, -2), c.ComplexBox(Q(-6), Q(4), Q(-10), Q(8)))

    def test_clock_profile_against_independent_first_collision_search(self):
        for base in (2, 6, 16):
            for h in (-6, 1, 9):
                for modulus in range(1, 65):
                    seen, value, n = {}, h % modulus, 0
                    while value not in seen:
                        seen[value] = n
                        n += 1
                        value = base*value % modulus
                    profile = c.clock_profile(base, h, modulus)
                    self.assertEqual(profile['transient'], seen[value])
                    self.assertEqual(profile['period'], n-seen[value])
                    self.assertEqual(profile['first_repeat_index'], n)

    def test_linear_ternary_tomography_clock_and_fourth_moment_mutant(self):
        for h in (1, -2, 3, 27):
            for N in (1, 2, 3, 9, 17, 40):
                m = c.ternary_tomography_clock(h, N)
                self.assertEqual(len({h*pow(16, j, m) % m for j in range(N)}), N)
                self.assertGreaterEqual(c.clock_profile(16, h, m)['period'], N)
        self.assertEqual(c.fourth_alias_polynomial(16, 1, 3, 27),
                         {0: 15, -270: 2, 270: 2})
        self.assertEqual(c.fourth_alias_polynomial(16, 1, 3, 521), {0: 15})

    def test_inverse_observer_first_visibility_exact(self):
        for base in (2, 3, 16):
            for depth in range(7):
                for H in (1, 2, 15, 16, 31, 257):
                    delay = c.inverse_observer_delay(base, depth, H)
                    self.assertLessEqual(base**(depth-delay), H)
                    for j in range(delay):
                        self.assertTrue(all(h % base**(depth-j) != 0 for h in range(1, H+1)))

    def test_source_membership_and_domain_mutants_rejected(self):
        for fake in (9, 25, 65, 121):
            with self.assertRaises(ValueError):
                c.prime_window(fake)
        with self.assertRaises(ValueError):
            c.prime_window(17, Q(1, 17))
        with self.assertRaises(ValueError):
            c.prime_window(17, 0.1)
        with self.assertRaises(ValueError):
            c.twisted_clock_certificate(17, 17)
        for bad in (True, -1, 2.0):
            with self.assertRaises(ValueError):
                c.dyadic_initial_control(bad)

    def test_first_equal_count_power_carry_and_source_corrected_sign(self):
        for base in (2, 3, 4, 16):
            for count in range(1, base+1):
                values = [sum(base**j for j in powers)
                          for powers in combinations_with_replacement(range(3), count)]
                self.assertEqual(len(values), len(set(values)))
            self.assertEqual(base*base**0+base**2, (base+1)*base)
        for n in (0, 1, 3, 9):
            for lag in (1, 3):
                for order in range(5):
                    defect = c.corrected_carry_defect(n, lag, order)
                    self.assertGreater((-1)**(order+1)*defect, 0)
                    self.assertLess(abs(defect), c.corrected_carry_upper(n, lag, order))
                    y = forced_states(n+lag+1)
                    q = lambda k: y[k]+c.pell_tail_approximation(k, order)
                    direct = 16*q(n)+q(n+lag+1)-q(n+1)-16*q(n+lag)
                    self.assertEqual(direct % 1, defect % 1)

    def test_corrected_origin_error_budget_against_independent_tail_intervals(self):
        from observational_succ.bbp_source_memory import tail_interval
        for start in (1, 4):
            for order in (0, 2, 4):
                length = 7
                error_upper = Q()
                for n in range(start, start+length):
                    lo, hi = tail_interval(n, 35)
                    A = c.pell_tail_approximation(n, order)
                    error_upper += max(abs(lo-A), abs(hi-A))**2
                # Chord <= 2*pi*phase; this independently controls the finite
                # squared-error sum against the all-length moment envelope.
                self.assertLess(Q(44, 7*length)**2*error_upper,
                    c.corrected_origin_l2_squared_upper(1, start, length, order))


if __name__ == '__main__':
    unittest.main()
