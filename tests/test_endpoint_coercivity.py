"""Calibrated finite checks for the endpoint coercivity research round.

Infinite claims are supported by the accompanying paper proofs, not this suite.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import tempfile
import unittest

from scripts.endpoint_shell_certificate import (
    endpoint_grid_sums, finite_certificate, grid_distance_bounds, terminal_state,
)
from scripts.verify_endpoint_shell_certificate import replay, source


def torus(t):
    t = F(t) % 1
    return min(t, 1-t)


def norm_squared(u, b):
    return sum((torus(u/16**k)**2 for k in range(1, b+1)), F(0))/b


def odd_component(t):
    t = F(t)
    q = t.denominator
    while q % 2 == 0:
        q //= 2
    if q == 1:
        return F(0)
    return F((t.numerator*pow(t.denominator//q, -1, q)) % q, q)


class EndpointCoercivityTests(unittest.TestCase):
    def test_grid_bounds_crossing_zero_and_half(self):
        for q in (16, 32, 64):
            for a in range(q):
                low, high = grid_distance_bounds(a, q)
                for j in range(33):
                    t = F(a, q) + F(j, 16*q)
                    self.assertLessEqual(F(low, q), torus(t))
                    self.assertLessEqual(torus(t), F(high, q))

    def test_omitted_grid_width_is_rejected(self):
        # Left-endpoint distance would overstate the minimum on this interval.
        q, a, t = 16, 15, F(31, 32)
        self.assertGreater(torus(F(a, q)), torus(t))
        self.assertLessEqual(F(grid_distance_bounds(a, q)[0], q), torus(t))

    def test_endpoint_digits_match_direct_rational_probes(self):
        m, digits = 39, 4
        n, q = 2*m+digits, 16**digits
        u = terminal_state(n)
        c = u.numerator//u.denominator
        lower, upper = endpoint_grid_sums(c, m, digits)
        for clock in range(2*m):
            value = u/16**(n-clock)
            a_direct = (q*value).numerator//(q*value).denominator % q
            a_bits = (c >> (4*(2*m-clock))) & (q-1)
            self.assertEqual(a_direct, a_bits)
            beta = source(n+1)/15
            for tail in (F(0), beta/2, beta):
                d = torus((u+tail)/16**(n-clock))
                self.assertLessEqual(F(lower[clock+1]-lower[clock], q*q), d*d)
                self.assertLessEqual(d*d, F(upper[clock+1]-upper[clock], q*q))

    def test_independent_replay_and_mutated_certificate(self):
        data = finite_certificate(16, 53, 4)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/"certificate.json"
            path.write_text(json.dumps(data))
            result = replay(path)
            self.assertEqual(result["all_integer_shells_verified"], 38)
            data["lower_sums"][7] += 1
            path.write_text(json.dumps(data))
            with self.assertRaises(AssertionError):
                replay(path)

    def test_checked_in_all_integer_shell_bounds(self):
        path = Path(__file__).resolve().parents[1]/(
            "research/2026-11-16/defect_window_tomography/ENDPOINT_SHELL_CERTIFICATES.json")
        data = json.loads(path.read_text())
        self.assertEqual((data["min_shell"], data["max_shell"], data["shell_count"]),
                         (16, 4096, 4081))
        self.assertEqual(len(data["lower_sums"]), 4081)
        q = data["grid_denominator"]
        bounds = [F(8*s, b*q*q) for b, s in enumerate(data["lower_sums"], start=16)]
        self.assertGreater(min(bounds), F(1, 2))
        self.assertEqual(min(bounds), F(data["minimum_phase_lower"]))
        self.assertEqual(bounds.index(min(bounds))+16, 25)

    def test_cold_word_cover_identity_and_sharp_bulk_control(self):
        for x in (F(0), F(1, 2), F(1, 15), F(8, 17), F(7, 31), F(1)):
            for b, m in ((1, 2), (3, 8), (7, 14), (9, 27)):
                values = [16**n*x for n in range(b, m+1)]
                nearest = [(v+F(1, 2)).numerator//(v+F(1, 2)).denominator for v in values]
                t = [v-j for v, j in zip(values, nearest)]
                a = [nearest[j+1]-16*nearest[j] for j in range(m-b)]
                energy = sum(v*v for v in t[:-1])
                correction = 17*(t[-1]**2-t[0]**2)
                slack = 16*sum((t[j]+t[j+1])**2 for j in range(m-b))
                self.assertEqual(289*energy+correction-sum(v*v for v in a), slack)
                self.assertTrue(all(-8 <= v <= 8 for v in a))
                self.assertLessEqual(sum(v != 0 for v in a), 289*energy+F(17, 4))
                rebuilt = nearest[0]
                for digit in a:
                    rebuilt = 16*rebuilt+digit
                self.assertEqual(rebuilt, nearest[-1])
                self.assertLessEqual(abs(x-F(rebuilt, 16**m)), F(1, 2*16**m))
                if x == F(8, 17):
                    self.assertEqual(sum(v*v for v in a), 289*energy)
                    self.assertGreater(sum(v*v for v in a), 288*energy)

    def test_winding_erasure_keeps_odd_data_and_rejoins(self):
        for b in (1, 3, 11, 37, 73):
            u = terminal_state(2*b)
            c = u.numerator//u.denominator
            v = u-c
            shift = (c % 16**b)+16**b
            s = -F(shift, 16**(2*b))
            altered = u+16**(2*b)*s
            self.assertTrue(F(1, 16**b) <= abs(s) < F(2, 16**b))
            self.assertEqual(altered % 1, u % 1)
            self.assertEqual(norm_squared(altered, b), v*v*(1-F(1, 16**(2*b)))/(255*b))
            for clock in (0, 1, b, 2*b-1, 2*b, 3*b):
                original = F(0) if clock == 0 else terminal_state(clock)
                changed = original+16**clock*s
                self.assertEqual(odd_component(original), odd_component(changed))
                if clock >= 2*b:
                    self.assertEqual(original % 1, changed % 1)

    def test_fine_erasure_pays_fractional_part_and_tail(self):
        for b in (2, 7, 29):
            u = terminal_state(2*b)
            c = u.numerator//u.denominator
            v = u-c
            shift = c % 16**b+16**b
            for length in (1, 4, 9):
                q = 16**length
                integer = (q*v).numerator//(q*v).denominator
                s = -(F(shift)+F(integer, q))/16**(2*b)
                altered = u+16**(2*b)*s
                residual = v-F(integer, q)
                self.assertLess(norm_squared(altered, b), F(1, 255*b*q*q))
                self.assertEqual(altered % 1, residual)
                self.assertEqual(odd_component(altered), odd_component(u))
                self.assertEqual((16**(2*b+length)*s).denominator, 1)

    def test_torus_norm_shadow_and_coherent_tail_equality(self):
        for b in (1, 3, 11, 32):
            geometric = (1-F(1, 16**(2*b)))/(255*b)
            for tail in (F(1, 1024), F(1, 7), F(9, 10)):
                h2 = tail*tail*geometric
                self.assertEqual(norm_squared(-tail, b), h2)
                self.assertGreater(h2, 0)  # A zero error budget would be false.
                for y in (F(0), F(1, 3), F(8), F(16**b-1), F(12345, 67)):
                    e, r = norm_squared(y, b), norm_squared(y-tail, b)
                    if e+r > h2:
                        self.assertLessEqual((e+r-h2)**2, 4*e*r)

    def test_critical_quintic_constant_and_subleading_gap(self):
        for b in (1, 2, 9, 31, 128, 512):
            d = (16*b+1)*(16*b+2)
            beta = source(2*b+1)/15
            self.assertLess(beta, F(1, d))
            gap = F(1, 256*b*b)-F(1, d)
            self.assertGreaterEqual(gap, F(1, 1632*b**3))
            self.assertGreaterEqual(gap*gap/(255*b), F(1, 679173120*b**7))
            h2_upper = beta*beta*(1-F(1, 16**(2*b)))/(255*b)
            self.assertLess(h2_upper, F(1, 16711680*b**5))

    def test_invalid_grid_domains(self):
        for a, q in ((0, 1), (1, 3), (-1, 16), (16, 16)):
            with self.assertRaises(ValueError):
                grid_distance_bounds(a, q)
        for args in ((0, 16, 2), (32, 16, 2), (1, 16, 0)):
            with self.assertRaises(ValueError):
                finite_certificate(*args)


if __name__ == "__main__":
    unittest.main()
