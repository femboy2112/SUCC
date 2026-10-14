"""Suzuki eq (1.3) screw function transcription + 8-point screw-Gram source-mutant control. mpmath 30 dps (Observed, NOT interval)."""
import unittest
import mpmath as mp
from functools import lru_cache
from sympy import factorint
mp.mp.dps = 30

@lru_cache(None)
def Lam(n, mode):
    # von Mangoldt variants (exact integer factorisation; cached)
    if mode == 'logn': return mp.log(n)
    f = factorint(n)
    if len(f) == 1:
        p = list(f)[0]
        if mode == 'primes_only' and n != p: return mp.mpf(0)
        return mp.log(p)
    if mode == 'fake6' and n == 6: return mp.log(6)
    return mp.mpf(0)

@lru_cache(None)
def g(t, mode='true'):
    t = abs(mp.mpf(t))
    pole = -4 * (mp.e ** (t / 2) + mp.e ** (-t / 2) - 2)
    arch = -(t / 2) * (mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi)) - mp.mpf(1) / 4 * (mp.lerchphi(1, 2, mp.mpf(1) / 4) - mp.e ** (-t / 2) * mp.lerchphi(mp.e ** (-2 * t), 2, mp.mpf(1) / 4))
    if mode == 'nogamma': arch = -mp.mpf(1) / 4 * (mp.lerchphi(1, 2, mp.mpf(1) / 4) - mp.e ** (-t / 2) * mp.lerchphi(mp.e ** (-2 * t), 2, mp.mpf(1) / 4))
    prime = mp.mpf(0)
    n = 1
    while n <= mp.e ** t:
        if n > 1: prime += Lam(n, mode) / mp.sqrt(n) * (t - mp.log(n))
        n += 1
    return pole + arch + prime

def min_eig(A, mode):
    pts = [s * (A / 4) * k for k in range(1, 5) for s in (1, -1)]
    K = mp.matrix(8, 8)
    for i, x in enumerate(pts):
        for j, y in enumerate(pts):
            K[i, j] = g(x - y, mode) - g(x, mode) - g(y, mode) + g(0, mode)
    return min(mp.eigsy(K, eigvals_only=True))

class G(unittest.TestCase):
    def test_transcription(self):
        self.assertLess(abs(g(0)), mp.mpf(10) ** -25)
        Aconst = (mp.log(2 * mp.pi) + mp.euler - 1) / 2
        self.assertLess(abs(Aconst - mp.mpf('0.7075463656554391720835857814468188553825')), mp.mpf(10) ** -25)
        t = mp.mpf('1e-4')
        rem = (g(t) - (t * mp.log(t) / 2 + Aconst * t)) / t ** 2
        self.assertLess(abs(rem + mp.mpf(7) / 8), mp.mpf('1e-5'))
    def test_true_gram_positive_mutants_negative_and_one_sided(self):
        self.assertGreater(min_eig(1, 'true'), 0.026); self.assertLess(min_eig(1, 'true'), 0.027)
        self.assertGreater(min_eig(3, 'true'), 0.023)
        for A in (1, 2, 3):
            for mode in ('primes_only', 'fake6', 'logn'):
                self.assertLess(min_eig(A, mode), -0.05, msg=(A, mode))
        self.assertLess(min_eig(1, 'primes_only') + 0.145647, 1e-4)
        self.assertGreater(min_eig(3, 'nogamma'), 0)   # sigma-error undetected by finite PSD at A=3

if __name__ == '__main__':
    unittest.main()
