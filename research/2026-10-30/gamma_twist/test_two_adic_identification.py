import random
import unittest
from fractions import Fraction as F
from math import factorial

import two_adic_identification as t


class Identification(unittest.TestCase):
    def test_newton_integer_polynomial(self):
        rng = random.Random(400401)
        for _ in range(30):
            c = tuple(rng.randrange(-200, 201) for _ in range(4))
            for n in (1, 2, 3, 4, 9, 31, 97, 257):
                self.assertEqual(t.numerator(n, c), t.polynomial_reconstruction(n, c))

    def test_all_time_criterion_finite_calibration(self):
        rng = random.Random(400402)
        samples = [tuple(rng.randrange(-64, 65) for _ in range(4)) for _ in range(80)]
        samples += [tuple(2**k*a for a in t.SHARP_DIRECTION) for k in range(5)]
        for c in samples:
            for bits in (0, 1, 3, 5, 9, 12):
                predicted = t.all_time_zero_mod(c, bits)
                self.assertEqual(predicted, all(t.valuation(t.source(n, c)) >= bits
                                               for n in range(1, 5)))
                if predicted:
                    for n in (7, 19, 97, 257, 1021):
                        self.assertGreaterEqual(t.valuation(t.source(n, c)), bits)

    def test_four_orbit_samples(self):
        for c in (t.AUTH, t.AGE_DIRECTION, t.SHARP_DIRECTION, (0, 4, 0, 0),
                  tuple(128*x for x in t.AGE_DIRECTION)):
            for bits in range(13):
                self.assertEqual(t.all_time_zero_mod(c, bits),
                    all(t.valuation(t.orbit(n, c)) >= bits for n in range(1, 5)))

    def test_sharp_nine_bit_loss(self):
        self.assertEqual(t.newton_coordinates(t.SHARP_DIRECTION), (0, 0, 0, 30720))
        self.assertEqual(t.valuation(t.source(4, t.SHARP_DIRECTION)), 9)
        for bits in (9, 13, 17, 23):
            c = tuple(2**(bits-9)*a for a in t.SHARP_DIRECTION)
            self.assertTrue(t.all_time_zero_mod(c, bits))
            self.assertFalse(t.all_time_zero_mod(c, bits+1))
            self.assertEqual(min(t.valuation(x) for x in c), bits-9)

    def test_fresh_mutant_source_orbit_valuations(self):
        for bits in (5, 9, 13, 17):
            c = tuple(2**(bits+2)*a for a in t.AGE_DIRECTION)
            u = F()
            for n in range(1, 258):
                u = 16*u+t.source(n, c)
                self.assertEqual(t.valuation(u), bits)
            for n in (2, 7, 31, 97, 257):
                self.assertEqual(t.valuation(t.source(n, c)), bits)

    def test_all_jet_valuation_fresh_cases(self):
        for bits in (5, 9, 13, 17):
            c = tuple(2**(bits+2)*a for a in t.AGE_DIRECTION)
            for n in (2, 7, 31, 97, 257, -11):
                for j in range(9):
                    self.assertEqual(t.valuation(t.source(n, c, j)),
                                     bits+j+t.valuation(factorial(j)))
                    self.assertEqual(t.valuation(t.unit_log_jet(n, j, c)),
                                     bits+3+3*j+t.valuation(factorial(j)))

    def test_complete_unit_factor_precision(self):
        for bits in (1, 5, 9, 13, 17):
            for n in (2, 7, 31, 97, 257):
                base = (8*n-7)*(8*n-3)
                modulus = 2**(bits+5)
                value = (pow(base, 2**(bits+2), modulus)-1) % modulus
                self.assertEqual(value, 2**(bits+4))
        c = tuple(a+8*b for a, b in zip(t.AUTH, t.AGE_DIRECTION))
        self.assertEqual(t.unit_ratio(2, c)/t.unit_ratio(2), F(9*13)**8)

    def test_boundary_discriminator(self):
        for terms in (1, 2, 3, 8, 16, 31):
            self.assertEqual(t.valuation(t.backward_boundary(t.AGE_DIRECTION, terms)), -2)
            self.assertGreaterEqual(t.valuation(t.backward_boundary(t.AUTH, terms)), 4*terms)

    def test_integrality_and_isometry_classification(self):
        rng = random.Random(400403)
        for _ in range(40):
            A, C, D, z = [rng.randrange(-20, 21) for _ in range(4)]
            c = (A, 4*z-2*D, C, D)
            for a, b in ((0, 1), (-7, 9), (31, 63), (97, 99), (257, 769)):
                diff = t.valuation(t.source(a, c)-t.source(b, c))
                if D % 2:
                    self.assertEqual(diff, t.valuation(a-b))
                else:
                    self.assertGreaterEqual(diff, t.valuation(a-b)+1)

    def test_mutants_keep_stationary_isometry_but_not_boundary(self):
        for bits in (5, 9, 13, 17):
            c = tuple(a+2**(bits+2)*b for a, b in zip(t.AUTH, t.AGE_DIRECTION))
            self.assertEqual(t.valuation(t.backward_boundary(c, 10)), bits)
            for a, b in ((1, 3), (19, 51), (127, 255)):
                Fa = sum((16**j*t.source(a-j, c) for j in range(6)), F())
                Fb = sum((16**j*t.source(b-j, c) for j in range(6)), F())
                self.assertEqual(t.valuation(Fa-Fb), t.valuation(a-b))

    def test_p13_discriminator_and_its_failure(self):
        def mod13(q):
            return q.numerator*pow(q.denominator, -1, 13) % 13
        for bits in (5, 9, 13, 17):
            base = mod13(13*t.orbit(2))
            for factor in (1, 13):
                c = tuple(a+factor*2**(bits+2)*b
                          for a, b in zip(t.AUTH, t.AGE_DIRECTION))
                self.assertEqual(mod13(13*t.orbit(2, c)) == base, factor == 13)

    def test_input_domain(self):
        for c in ((1, 2, 3), (1.0, 2, 3, 4)):
            with self.assertRaises(ValueError):
                t.source(1, c)
        with self.assertRaises(ValueError):
            t.all_time_zero_mod(t.AUTH, -1)


if __name__ == "__main__":
    unittest.main()
