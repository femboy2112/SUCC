"""Finite exact positive and hostile controls for the 16-solenoid natural extension.

These checks are not an infinite mathematical proof, nor a test of pi normality.
Run: python -m unittest discover -s tests -p test_solenoid_digit_bridge.py -v
"""
import unittest
from collections import Counter
from fractions import Fraction as Q

from observational_succ.solenoid_digit_bridge import (
    RADIX, FiniteSolenoidChart, authentic_four_pole,
    canceled_four_pole, bbp_zero_seed_state,
    digit_archive_residue, rational_character_split, two_adic_residue,
)


def de_bruijn(k: int, n: int) -> tuple[int, ...]:
    """Independent FKM universal-cycle generator. Small test-only input."""
    a = [0] * (k*n + 1)
    answer = []

    def recurse(t, p):
        if t > n:
            if n % p == 0:
                answer.extend(a[1:p+1])
        else:
            a[t] = a[t-p]
            recurse(t+1, p)
            for j in range(a[t-p]+1, k):
                a[t] = j
                recurse(t+1, t)

    recurse(1, 1)
    return tuple(answer)


class SolenoidDigitBridgeTest(unittest.TestCase):
    def test_forward_winding_exact_with_adic_character(self):
        samples = [Q(-9,5), Q(-1), Q(0), Q(3,19), Q(47,15), Q(32,3), Q(12345,17)]
        for value in samples:
            with self.subTest(value=value):
                chart = FiniteSolenoidChart.from_unwrapped(value, 3)
                for n in range(6):
                    self.assertEqual(chart, FiniteSolenoidChart.from_unwrapped(16**n*value, 3))
                    for k in range(4):
                        for h in (-3, -1, 1, 5):
                            self.assertEqual(chart.character_phase(h, k),
                                             (Q(h*16**n) * value / 16**k) % 1)
                    chart, digit = chart.advance()
                    self.assertTrue(0 <= digit <= 15)

    def test_inverse_uses_lost_adic_digit(self):
        for value in (Q(-9, 5), Q(47,15), Q(32, 3), Q(17,19)):
            before = FiniteSolenoidChart.from_unwrapped(value, 4)
            after, digit = before.advance()
            inverse, old_digit = after.inverse_with_precision_loss()
            self.assertEqual(old_digit, digit)
            self.assertEqual(inverse, FiniteSolenoidChart.from_unwrapped(value,3))
            self.assertEqual(inverse.advance()[0],
                             FiniteSolenoidChart(after.circle, after.memory % (16**3),3))

    def test_bidirectional_hex_digits_are_winding_memory(self):
        number = Q(int('a3f527bc',16), 16**8-1)  # periodic 8-digit phase
        chart = FiniteSolenoidChart.from_unwrapped(number, 5)
        digits = []
        for n in range(28):
            for k in range(1, min(5, n)+1):
                expected = sum(digits[-j]*16**(j-1) for j in range(1,k+1))
                self.assertEqual(chart.memory % 16**k, expected)
            chart, digit = chart.advance()
            digits.append(digit)
            self.assertEqual(chart.memory, digit_archive_residue(tuple(digits),5))

    def test_exact_archive_equals_integer_winding(self):
        alpha = Q(int('a3f527bc',16), 16**8-1)
        chart = FiniteSolenoidChart.from_unwrapped(alpha, 4)
        for n in range(25):
            integer_part = (16**n*alpha).numerator // (16**n*alpha).denominator
            self.assertEqual(chart.memory,integer_part % 16**4)
            chart,_ = chart.advance()

    def test_de_bruijn_finite_haar_and_long_word_counterfeit(self):
        # Every two-hex-digit block occurs ONCE in one 256-step period,
        # yet alpha is rational and NOT normal. This is a critical control.
        digits = de_bruijn(16,2)
        self.assertEqual(len(digits),256)
        pairs = Counter((digits[i-1],digits[i]) for i in range(256))
        self.assertEqual(len(pairs),256)
        self.assertTrue(all(v==1 for v in pairs.values()))
        numerator = sum(d *16**(255-i) for i,d in enumerate(digits))
        alpha = Q(numerator, 16**256-1)
        chart = FiniteSolenoidChart.from_unwrapped(alpha, 2)
        observed = Counter()
        for n in range(257):
            if n>0:
                digit_next=(16*chart.circle).numerator//(16*chart.circle).denominator
                observed[(chart.memory%16,digit_next)]+=1
            chart,_=chart.advance()
        self.assertEqual(len(observed), 256)
        self.assertTrue(all(v==1 for v in observed.values()))
        # Only 256 triples exist in a period: cannot be uniform among 4096.
        self.assertLessEqual(len({(digits[i-2],digits[i-1],digits[i])
                                  for i in range(256)}), 256)

    def test_periodic_source_and_clock_do_not_force_haar(self):
        clock = [n % 16 for n in range(16)]
        self.assertEqual(set(clock), set(range(16)))
        zero = FiniteSolenoidChart.from_unwrapped(Q(0), 2)
        for _ in clock:
            self.assertEqual(zero.circle,0)
            self.assertEqual(zero.memory,0)
            zero,digit=zero.advance()
            self.assertEqual(digit,0)

    def test_adic_state_not_real_winding(self):
        # U=32/3 belongs to 16 Z2, yet its real winding is 10 mod16.
        self.assertEqual(two_adic_residue(Q(32,3),1),0)
        self.assertEqual(two_adic_residue(Q(0),1),0)
        self.assertEqual(FiniteSolenoidChart.from_unwrapped(Q(32,3),1).memory,10)
        self.assertEqual(FiniteSolenoidChart.from_unwrapped(Q(0),1).memory,0)

    def test_odd_denominator_character_compensation(self):
        for value in (Q(-9,5),Q(0),Q(47,15),Q(32,3),Q(12345,17)):
            for k in (1,2,3):
                for h in (-7,-1,1,3,11):
                    real,adic,complement=rational_character_split(value,k,h)
                    self.assertEqual(real,(adic+complement)%1)
        # Even at complete p-adic residue zero, the real fractional
        # character is nonzero: the complementary denominator owns it.
        real,adic,complement=rational_character_split(Q(32,3),1,1)
        self.assertEqual(adic,0)
        self.assertNotEqual(real,0)
        self.assertEqual(real,complement)

    def test_original_four_signed_poles_and_zero_initial_seed(self):
        self.assertEqual(bbp_zero_seed_state(0),0)
        state=Q(0)
        for n in range(1,12):
            source=authentic_four_pole(n)
            self.assertEqual(source,canceled_four_pole(n))
            self.assertEqual(source.denominator%2,1)
            state=16*state+source
            self.assertEqual(state,bbp_zero_seed_state(n))
            self.assertEqual(state.denominator%2,1)
            self.assertEqual(FiniteSolenoidChart.from_unwrapped(state,3).character_phase(1,0),state%1)

    def test_native_four_pole_authenticator_if_available(self):
        # In a full SUCC checkout this checks against the native source.
        # The isolated artifact does not ship upstream code and skips it.
        try:
            from observational_succ.succ_internal_matrix_walk import authentic_r
        except ModuleNotFoundError:
            self.skipTest("upstream SUCC module absent in isolated artifact")
        for n in range(1,100):
            self.assertEqual(authentic_r(n), authentic_four_pole(n))

    def test_rejects_false_precision_and_even_denominators(self):
        with self.assertRaises(ValueError):
            FiniteSolenoidChart.from_unwrapped(0.25,2)
        with self.assertRaises(ValueError):
            two_adic_residue(Q(1,2),2)
        with self.assertRaises(ValueError):
            FiniteSolenoidChart.from_unwrapped(Q(0),1).inverse_with_precision_loss()
        with self.assertRaises(ValueError):
            FiniteSolenoidChart.from_unwrapped(Q(0),2).character_phase(1,3)


if __name__=='__main__':
    unittest.main()
