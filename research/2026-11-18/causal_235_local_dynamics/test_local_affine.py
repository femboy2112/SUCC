"""Exact two-place affine precision and chronology probes.

Classical finite algebra, specialized to the original BBP source and the
shortcut Collatz convention.  This module does not certify either conjecture.
"""
from fractions import Fraction as Q
from itertools import product
import unittest


def valuation(x, p):
    x = Q(x)
    if not x:
        raise ValueError("valuation of zero is not finite")
    if p not in (2, 3, 5):
        raise ValueError("probe supports primes 2, 3, and 5")
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def pnorm(x, p):
    v = valuation(x, p)
    return Q(1, p**v) if v >= 0 else Q(p**(-v))


def collatz_cocycle(word):
    """Return N, s, b: chronological word map is (3**s*x+b)/2**N."""
    b, s = 0, 0
    for j, bit in enumerate(word):
        if bit not in (0, 1):
            raise ValueError("parity word is binary")
        b = 3**bit * b + bit * 2**j
        s += bit
    return len(word), s, b


def cylinder_residue(word):
    n, s, b = collatz_cocycle(word)
    mod = 2**n
    return (-b * pow(3**s, -1, mod)) % mod


def observed_word(n, length):
    """Execute actual integer branches; negative inputs are explicit controls."""
    word = []
    for _ in range(length):
        bit = n % 2
        word.append(bit)
        n = (3*n + 1)//2 if bit else n//2
    return tuple(word), n


def authentic_r(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("positive source index required")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def bbp_run(length, seed=0):
    x = Q(seed)
    for n in range(1, length+1):
        x = 16*x + authentic_r(n)
    return x


def two_prime_euler_coefficient(n, fake_six=False):
    """Coefficient at n in Z_2 Z_3, optionally times a false Z_6 factor."""
    if n < 1:
        raise ValueError("positive coefficient index required")
    a = b = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    while n % 3 == 0:
        n //= 3
        b += 1
    return (min(a, b)+1 if fake_six else 1) if n == 1 else 0


class LocalAffineProbe(unittest.TestCase):
    def test_every_finite_parity_cylinder_and_ordered_cocycle(self):
        for length in range(1, 11):
            residues = set()
            for word in product((0, 1), repeat=length):
                n, s, b = collatz_cocycle(word)
                residue = cylinder_residue(word)
                residues.add(residue)
                # Two distinct positive representatives: equality is not fitted
                # solely to the least residue (which can be zero).
                for k in (1, 3):
                    x = residue + k*2**length
                    actual_word, y = observed_word(x, length)
                    self.assertEqual(actual_word, word)
                    self.assertEqual(2**n*y, 3**s*x+b)
                    self.assertNotEqual(2**n*y, 3**s*x+b+1)
            self.assertEqual(len(residues), 2**length)

    def test_exact_collatz_precision_budget(self):
        for length in range(1, 9):
            for word in product((0, 1), repeat=length):
                n, s, _ = collatz_cocycle(word)
                x = cylinder_residue(word) + 2**length
                delta = 2**(length+4) * 3**3
                w1, y1 = observed_word(x, length)
                w2, y2 = observed_word(x+delta, length)
                self.assertEqual(w1, word)
                self.assertEqual(w2, word)
                self.assertEqual(Q(y2-y1, delta), Q(3**s, 2**n))
                self.assertEqual(valuation(y2-y1, 2), 4)
                self.assertEqual(valuation(y2-y1, 3), 3+s)

    def test_bbp_precision_budget_on_actual_four_pole_forcing(self):
        for n in range(1, 21):
            delta = Q(2**5 * 3**4, 5)
            diff = bbp_run(n, delta)-bbp_run(n)
            self.assertEqual(diff, 16**n*delta)
            self.assertEqual(valuation(diff, 2), 5+4*n)
            self.assertEqual(valuation(diff, 3), 4)
            self.assertEqual(valuation(diff, 5), -1)

    def test_same_slope_different_chronology(self):
        self.assertEqual(collatz_cocycle((1, 0)), (2, 1, 1))
        self.assertEqual(collatz_cocycle((0, 1)), (2, 1, 2))
        self.assertEqual(cylinder_residue((1, 0)), 1)
        self.assertEqual(cylinder_residue((0, 1)), 2)
        self.assertEqual(observed_word(1, 2), ((1, 0), 1))
        self.assertEqual(observed_word(2, 2), ((0, 1), 2))

    def test_three_place_slope_product_formula(self):
        for n in range(1, 31):
            for s in range(n+1):
                a = Q(3**s, 2**n)
                self.assertEqual(abs(a)*pnorm(a, 2)*pnorm(a, 3), 1)
            a = Q(16**n)
            self.assertEqual(a*pnorm(a, 2)*pnorm(a, 3), 1)
        # State translations need not be supported at 2 and 3.
        q = Q(1, 5)
        self.assertEqual(abs(q)*pnorm(q, 2)*pnorm(q, 3), Q(1, 5))
        self.assertEqual(abs(q)*pnorm(q, 2)*pnorm(q, 3)*pnorm(q, 5), 1)

    def test_arbitrarily_long_real_expansion_and_negative_fixed_control(self):
        for n in range(1, 101):
            word, y = observed_word(2**n-1, n)
            self.assertEqual(word, (1,)*n)
            self.assertEqual(y, 3**n-1)
            self.assertGreater(y, 2**n-1)
            self.assertEqual(observed_word(-1, n), ((1,)*n, -1))

    def test_nonzero_word_qualification_for_old_valuation_claim(self):
        for n in range(1, 11):
            for word in product((0, 1), repeat=n):
                _, s, b = collatz_cocycle(word)
                if s:
                    self.assertEqual(valuation(b, 3), 0)
                    self.assertEqual(valuation(2**n-3**s, 3), 0)
                else:
                    self.assertEqual(b, 0)
        self.assertEqual(collatz_cocycle((0, 0)), (2, 0, 0))
        self.assertEqual(valuation(2**2-1, 3), 1)
        with self.assertRaises(ValueError):
            valuation(0, 3)

    def test_fake_composite_first_appears_at_six(self):
        for n in range(1, 6):
            self.assertEqual(two_prime_euler_coefficient(n),
                             two_prime_euler_coefficient(n, True))
        self.assertEqual(two_prime_euler_coefficient(6), 1)
        self.assertEqual(two_prime_euler_coefficient(6, True), 2)
        self.assertEqual(two_prime_euler_coefficient(36), 1)
        self.assertEqual(two_prime_euler_coefficient(36, True), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
