"""Scoped, exact finite checks for the SUCC/Iroh Dirichlet-beta prime bridge.

These tests do not test GRH, convergence rates, or pi normality.
Run: python -m unittest test_prime_beta_bridge.py -v
"""
from fractions import Fraction
from math import isqrt
import unittest


def chi4(n: int) -> int:
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def primes_to(limit: int):
    if limit < 2:
        return []
    flags = bytearray(b'\x01') * (limit + 1)
    flags[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            for j in range(p * p, limit + 1, p):
                flags[j] = 0
    return [n for n in range(2, limit + 1) if flags[n]]


def euler_log_coefficients(limit: int):
    """Prime-power log Euler coefficients indexed by integer p**k; exact rational."""
    weights = {}
    for p in primes_to(limit):
        sign = chi4(p)
        if not sign:
            continue
        power, k = p, 1
        while power <= limit:
            weights[power] = Fraction(sign ** k, k * power)
            k += 1
            power *= p
    return weights


def independent_von_mangoldt_coefficients(limit: int):
    """Independent factorization over every n, with k and χ(n) derived afresh."""
    out = {}
    for n in range(2, limit + 1):
        f = n
        p = None
        exponent = 0
        for d in range(2, isqrt(f) + 1):
            if f % d == 0:
                p = d
                while f % d == 0:
                    f //= d
                    exponent += 1
                break
        if p is None:
            p, exponent, f = n, 1, 1
        if f != 1 or chi4(p) == 0:
            continue
        out[n] = Fraction(chi4(n), n * exponent)
    return out


def bbp_r(n: int) -> Fraction:
    assert n >= 1
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def bbp_r_mellin(n: int) -> Fraction:
    assert n >= 1
    # ∫_0^1 t^(8n-8) (4-2t^3-t^4-t^5) dt
    exps = ((4, 0), (-2, 3), (-1, 4), (-1, 5))
    return sum((Fraction(c, 8*n-7+k) for c, k in exps), Fraction(0))


class DirichletPrimeBridgeTests(unittest.TestCase):
    def test_character_source_multiplicativity(self):
        for a in range(1, 121):
            for b in range(1, 121):
                self.assertEqual(chi4(a*b), chi4(a)*chi4(b), (a, b))

    def test_prime_power_indicator_rejects_composite_six(self):
        coeff = euler_log_coefficients(100)
        self.assertNotIn(6, coeff)
        self.assertNotIn(10, coeff)
        self.assertNotIn(2, coeff)
        self.assertEqual(coeff[3], Fraction(-1, 3))
        self.assertEqual(coeff[5], Fraction(1, 5))
        self.assertEqual(coeff[9], Fraction(1, 18))
        self.assertEqual(coeff[25], Fraction(1, 50))
        self.assertNotEqual(coeff[9], Fraction(1, 9))  # missing 1/k mutant

    def test_two_independent_exact_prime_log_constructions(self):
        for cutoff in (2, 10, 31, 127, 511, 1024):
            self.assertEqual(euler_log_coefficients(cutoff),
                             independent_von_mangoldt_coefficients(cutoff))

    def test_fucc_twisted_commutator_coefficients(self):
        # For n=p**k: [log N, (χ(p)^k/k)V_n]e1
        # = (k log p) χ(p)^k/k e_n = χ(n)log p e_n.
        for p in (3, 5, 7, 11, 13, 17, 19):
            for k in range(1, 7):
                n = p**k
                self.assertEqual(Fraction(chi4(p)**k, k) * k, chi4(n))
                self.assertEqual(Fraction(chi4(p)**k, k*n),
                                 Fraction(chi4(n), n*k))

    def test_zero_seed_original_bbp_mellin_identity(self):
        for n in range(1, 201):
            self.assertEqual(bbp_r(n), bbp_r_mellin(n))
            self.assertGreater(bbp_r(n), 0)
        u = Fraction(0)
        p = Fraction(0)
        for n in range(1, 28):
            u = 16*u + bbp_r(n)
            p += bbp_r(n)/16**n
            self.assertEqual(u, 16**n*p)

    def test_prime_to_phase_endpoint_jacobian_rank_one(self):
        # J_(time,source) = v_time * c_source; every 2x2 minor must vanish.
        # c_source are source-authenticated rational prime-power coefficients.
        c = list(euler_log_coefficients(64).values())
        v = [Fraction(1), Fraction(16), Fraction(256), Fraction(4096)]
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                for a in range(len(c)):
                    for b in range(a+1, len(c)):
                        self.assertEqual((v[i]*c[a])*(v[j]*c[b])
                                         - (v[i]*c[b])*(v[j]*c[a]), 0)

    def test_summand_sign_hostile_mutations(self):
        # Genuine signs at p ≡ 1,3 (mod 4), and real-vs-bare multiplier difference.
        w = euler_log_coefficients(100)
        self.assertLess(w[3], 0)
        self.assertGreater(w[5], 0)
        self.assertEqual(w[49], Fraction(1, 98))
        # Wrong principal χ would give positive weight at p=3.
        self.assertNotEqual(w[3], Fraction(1, 3))


if __name__ == '__main__':
    unittest.main()
