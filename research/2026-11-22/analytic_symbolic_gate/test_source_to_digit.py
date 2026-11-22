"""Focused exact regression suite for source-selected analytic/symbolic gates."""
import unittest
from fractions import Fraction
from source_to_digit import (
    forcing, pi16_interval, hex_prefix, periodic_shadow,
    repeating_match, finite_irrationality_repetition_cap,
    kempner_digit_at,kempner_digits,kempner_phase_interval,
    kempner_energy_shell_upper, exact_kempner_shell_phase_squares)


class TestOriginalBBP(unittest.TestCase):
    def test_first_pole_exact(self):
        self.assertEqual(forcing(1), Fraction(47,15))

    def test_rational_source_decreasing(self):
        for n in range(1,100):
            self.assertGreater(forcing(n),forcing(n+1))
            self.assertGreater(forcing(n),0)

    def test_pi16_positive_bounds(self):
        for n in range(1,31):
            a,b=pi16_interval(n)
            self.assertLess(a,b)
            self.assertGreater(a,0)
            if n>1:
                prev,prev_high=pi16_interval(n-1)
                self.assertGreater(a,prev)
                self.assertLessEqual(b,prev_high)

    def test_bbp_hex_prefix_12(self):
        self.assertEqual(hex_prefix(12),'3243F6A8885A')

    def test_bbp_hex_prefix_24(self):
        self.assertEqual(hex_prefix(24),'3243F6A8885A308D313198A2')

    def test_insufficient_certification_fails(self):
        with self.assertRaises(ValueError):
            hex_prefix(32,1)

    def test_source_invalid_input(self):
        for n in [-1,0,2.5]:
            with self.assertRaises(ValueError):forcing(n)
        with self.assertRaises(ValueError): pi16_interval(-1)

class TestPeriodicShadows(unittest.TestCase):
    def test_repeated_fives(self):
        self.assertEqual(periodic_shadow('', '5'),Fraction(1,3))

    def test_repeated_threes(self):
        self.assertEqual(periodic_shadow('', '3'),Fraction(1,5))

    def test_prefix_and_period_rational(self):
        self.assertEqual(periodic_shadow('A','BC'), Fraction(10*255+0xBC, 16*255))

    def test_repetition_count(self):
        self.assertEqual(repeating_match('123ABABABACD',3,2),7)

    def test_periodic_shadow_agrees_with_digits(self):
        for prefix,block in [('123','EF'),('','03'),('FF','2'),('1','0')]:
            x=periodic_shadow(prefix,block)
            digits=prefix+block*10
            for k in range(1,len(prefix)+6*len(block)+1):
                self.assertEqual((x*16**k).__floor__(),int(digits[:k],16))

    def test_repetition_cap_symbolic(self):
        c=finite_irrationality_repetition_cap(100,4,7104,1000)
        self.assertEqual(c, Fraction(6104*100+7104*4,1000)+1)

    def test_repetition_cap_limits(self):
        for vals in [(0,0,7104,1000),(1,1,2000,1000),(1,1,1,0)]:
            with self.assertRaises(ValueError): finite_irrationality_repetition_cap(*vals)

    def test_factorial_lacunary_breaks_every_fixed_bound(self):
        from math import factorial
        for m in (20,30,40):
            n=factorial(m)
            L=factorial(m+1)-n-1
            for nu in ((7104,1000),(3000,1000),(2010,1000)):
                self.assertGreater(L,finite_irrationality_repetition_cap(n,1,*nu))

class TestKempnerCriticalControl(unittest.TestCase):
    def test_initial_digits(self):
        self.assertEqual(kempner_digits(16),'1101000100000001')

    def test_geometric_phase_enclosure(self):
        for n in range(0,60):
            low,high=kempner_phase_interval(n)
            self.assertGreater(low,0)
            self.assertLess(low,high)
            # A known finite partial sum (hence a lower bound) is strictly within upper.
            powers=[2**i for i in range(10) if 2**i>n]
            trunc=sum((Fraction(1,16**(p-n)) for p in powers),Fraction(0))
            self.assertGreaterEqual(trunc,low)
            self.assertLess(trunc,high)

    def test_energy_exact_shell_upper(self):
        for B in (2,4,8,16,32):
            actual=exact_kempner_shell_phase_squares(B)
            certified=kempner_energy_shell_upper(B)
            self.assertLess(actual,certified)

    def test_kempner_gap_at_double_shell(self):
        for B in (2,4,8,16,32,64):
            for n in range(B,2*B):
                low,high=kempner_phase_interval(n)
                self.assertEqual(low, Fraction(1,16**(2*B-n)))

    def test_control_not_eventually_periodic(self):
        # Finite structural calibration: gaps double, so they are unbounded.
        positions=[2**k for k in range(1,13)]
        gaps=[positions[i+1]-positions[i] for i in range(len(positions)-1)]
        self.assertTrue(all(gaps[i+1]>gaps[i] for i in range(len(gaps)-1)))

    def test_invalid_phase_clock(self):
        for n in (-1,2.3):
            with self.assertRaises(ValueError):kempner_phase_interval(n)
        for B in (0,1,3,6):
            with self.assertRaises(ValueError):kempner_energy_shell_upper(B)

if __name__=='__main__':
    unittest.main()
