import unittest
from collections import Counter
from fractions import Fraction

from cube_oracle import (ONE, clock, cube_atom, direct_histogram, squared_sum_histogram,
                         unwrapped_history, authentic, principal_part, mul, conj, avg)
from cube_oracle import fourth_moment_histogram, fourth_moment_checks


class SourceCubeTests(unittest.TestCase):
    def test_signed_histogram_equals_final_pair_square(self):
        for p in (17, 41, 73):
            for d in (1, 2, 3):
                self.assertEqual(direct_histogram(p, 3, d), squared_sum_histogram(p, 3, d)[0])

    def test_exact_degeneracy_count(self):
        for d in range(1, 6):
            m = len(clock(41))
            _, count = squared_sum_histogram(41, 2, d)
            self.assertEqual(count, m**(d-1)-(m-1)**(d-1))

    def test_zero_frequency_and_wrong_conjugations(self):
        m = len(clock(41))
        self.assertEqual(direct_histogram(41, 0, 2), Counter({0: m**3}))
        self.assertNotEqual(direct_histogram(41, 1, 2), direct_histogram(41, 1, 2, True))

    def test_source_authentication_preserves_unwrapped_boundary_and_poles(self):
        states = unwrapped_history(40)
        self.assertTrue(authentic(states))
        self.assertFalse(authentic([v % 1 for v in states]))
        self.assertFalse(authentic(unwrapped_history(40, Fraction(1, 41))))
        self.assertFalse(authentic(unwrapped_history(40, first_coefficient=5)))
        for n in range(11, 21):
            self.assertEqual(principal_part(states[n], 41), Fraction(4*pow(16, n-6, 41) % 41, 41))

    def test_dual_atom_uses_bilinear_source_pairing(self):
        a = [ONE, (Fraction(0), Fraction(1)), (Fraction(-1), Fraction(0)),
             (Fraction(0), Fraction(-1))]
        atom = cube_atom([a]*3, 2)
        self.assertEqual(atom, [conj(z) for z in a])
        self.assertEqual(avg(mul(z, b) for z, b in zip(a, atom)), ONE)
        self.assertNotEqual(avg(mul(conj(z), b) for z, b in zip(a, atom)), ONE)

    def test_domain_and_bounded_factor_requirements(self):
        for p in (2, 9, -1):
            with self.assertRaises(ValueError):
                clock(p)
        with self.assertRaises(ValueError):
            direct_histogram(41, 1, 0)
        with self.assertRaises(ValueError):
            cube_atom([[(Fraction(2), Fraction(0))]]*3, 2)
        with self.assertRaises(ValueError):
            cube_atom([[ONE]], 2)

    def test_fourth_moment_uses_temporal_fourier_resonance(self):
        for p in (17, 41, 73):
            self.assertEqual(fourth_moment_histogram(p, 2), direct_histogram(p, 2, 2))


if __name__ == "__main__":
    unittest.main()
