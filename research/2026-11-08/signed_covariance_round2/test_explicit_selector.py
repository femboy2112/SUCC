from fractions import Fraction as Q
import unittest
from explicit_selector import select, primes_to, order16_factored, classical_cap8, eighth_root_interval
from lag_instrument import SCALE


class SelectorTests(unittest.TestCase):
    def test_integer_root_enclosures(self):
        for r in (Q(0), Q(1), Q(1, 3), Q(1, 2**80), Q(7, 9)):
            box = eighth_root_interval(r)
            self.assertLessEqual(Q(box.lo, SCALE)**8, r)
            self.assertGreaterEqual(Q(box.hi, SCALE)**8, r)
            self.assertLessEqual(box.hi-box.lo, 1)

    def test_selector_predicates(self):
        for A in (5, 23, 101, 353, 1009):
            for C in (1, 2, 3):
                result = select(A, C)
                if result:
                    p, m = result
                    self.assertEqual(p % 8, 1)
                    self.assertGreater(m**3, p)
                    self.assertGreater(m*m*p.bit_length()**(2*C), p)
                    self.assertLessEqual(p, 4*A)

    def test_factored_orders_against_orbits(self):
        for p in primes_to(500):
            if p == 2:
                continue
            orbit, value = set(), 1
            while value not in orbit:
                orbit.add(value)
                value = value*16 % p
            self.assertEqual(order16_factored(p), len(orbit))

    def test_cap_normalization(self):
        self.assertEqual(classical_cap8(17, 16), Q(17**4, 16**8))
        self.assertEqual(classical_cap8(17, 1), Q(1))
        for p in (41, 97, 193):
            m = order16_factored(p)
            self.assertLessEqual(classical_cap8(p, m), 1)

    def test_invalid_domains_and_empty_selector(self):
        self.assertIsNone(select(1))
        for A, C in ((0, 2), (3, 0), (True, 2), (2, 1.5)):
            with self.assertRaises(ValueError):
                select(A, C)
        for p, m in ((15, 2), (17, 3), (2, 1), (17, 0)):
            with self.assertRaises(ValueError):
                classical_cap8(p, m)


if __name__ == '__main__':
    unittest.main()
