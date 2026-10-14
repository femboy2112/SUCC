"""Route B: exact NB/BD finite facts. mpmath 60 dps high precision (NOT interval; Observed/Corroborated, not a sec-8 certificate)."""
import unittest
from fractions import Fraction as F
from math import lcm
import mpmath as mp
mp.mp.dps = 60

def rr(m, n):
    L = lcm(m, n); tot = mp.mpf(0)
    for r in range(1, L):
        c = mp.mpf((r % m) * (r % n)) / (m * n)
        if c:
            tot += c * (mp.digamma(mp.mpf(r + 1) / L) - mp.digamma(mp.mpf(r) / L)) / L
    return tot

def beta(m):
    s = mp.mpf(0)
    for r in range(1, m):
        s += r * (mp.loggamma(mp.mpf(r) / m) - mp.loggamma(mp.mpf(r + 1) / m) + mp.digamma(mp.mpf(r + 1) / m) / m)
    return s / m

def dist_E(N):
    ns = list(range(2, N + 1))
    G = mp.matrix(len(ns), len(ns)); b = mp.matrix(len(ns), 1)
    for i, m in enumerate(ns):
        b[i] = mp.log(m) / m
        for j, n in enumerate(ns):
            G[i, j] = rr(m, n)
    return 1 - (b.T * mp.lu_solve(G, b))[0]

def dist_D(N, extra_inf=True):
    ns = list(range(1, N + 1))
    kappa = mp.log(2 * mp.pi) - mp.euler - 1
    G = mp.matrix(N, N); b = mp.matrix(N, 1)
    for i, m in enumerate(ns):
        b[i] = (mp.log(m) + 1 - mp.euler) / m
        for j, n in enumerate(ns):
            r = rr(m, n) if (m > 1 and n > 1) else mp.mpf(0)
            G[i, j] = r + (beta(m) if m > 1 else 0) / n + (beta(n) if n > 1 else 0) / m + kappa / (m * n) + (mp.mpf(1) / (m * n) if extra_inf else 0)
    return 1 - (b.T * mp.lu_solve(G, b))[0]

def mobius(n):
    r, p, x = 1, 2, n
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0: return 0
            r = -r
        p += 1
    if x > 1: r = -r
    return r

def Mert(k): return sum(mobius(i) for i in range(1, k + 1))

def interp(K, k, mK):
    # SUCC source-first interpolant: -mu(n) on clocks n<=K, plus (K+1)*m_K on clock K+1; clock_n(k)=(k mod n)/n
    v = -sum(F(mobius(n) * (k % n), n) for n in range(1, K + 1))
    return v + (K + 1) * mK * F(k % (K + 1), K + 1)

class NB(unittest.TestCase):
    def test_E2_E3_closed_forms(self):
        self.assertLess(abs(dist_E(2) - (1 - mp.log(2))), mp.mpf(10) ** -40)
        s3 = mp.sqrt(3) * mp.pi
        G22 = mp.log(2) / 4; G23 = (2 * mp.log(2) + mp.log(3)) / 12 - s3 / 54; G33 = 2 * mp.log(3) / 9 - s3 / 81
        b2 = mp.log(2) / 2; b3 = mp.log(3) / 3
        E3 = 1 - (b2 ** 2 * G33 - 2 * b2 * b3 * G23 + b3 ** 2 * G22) / (G22 * G33 - G23 ** 2)
        self.assertLess(abs(E3 - dist_E(3)), mp.mpf(10) ** -40)
        self.assertLess(abs(E3 - mp.mpf('0.0957477839277540266143081193401')), mp.mpf(10) ** -28)
    def test_D1_D2_pinned_values_and_comparability(self):
        c = mp.log(2 * mp.pi) - mp.euler
        self.assertLess(abs(c - mp.mpf('1.26066')), mp.mpf('1e-5'))
        self.assertLess(abs(dist_D(1) - (1 - (1 - mp.euler) ** 2 / c)), mp.mpf(10) ** -40)
        self.assertLess(abs(dist_D(2) - mp.mpf('0.289964573742202731811')), mp.mpf(10) ** -18)
        self.assertLess(abs(dist_D(3) - mp.mpf('0.09383722849698329190428')), mp.mpf(10) ** -20)
        prev = None
        for N in range(2, 9):
            E, D = dist_E(N), dist_D(N)
            self.assertLess(D, E); self.assertLessEqual(E, c * D)
            if prev is not None: self.assertLess(E, prev)
            prev = E
        self.assertLess(abs(dist_E(7) - mp.mpf('0.02438836788524400644614166')), mp.mpf(10) ** -20)
        self.assertLess(abs(dist_D(7) - mp.mpf('0.02430210054347671988410429')), mp.mpf(10) ** -20)
        self.assertGreater(dist_E(2) / dist_D(2), mp.mpf('1.058'))   # E*_N is NOT d_N^2
    def test_D4_source_first_error_formula_exact(self):
        for K in range(2, 41):
            mK = sum(F(mobius(n), n) for n in range(1, K + 1))
            for k in range(1, K + 1):
                self.assertEqual(interp(K, k, mK), 1)
            MK = Mert(K)
            for k in range(K + 1, 2 * K + 2):
                self.assertEqual(1 - interp(K, k, mK), (K + 1) * mK + Mert(k) - MK, msg=(K, k))
    def test_D4_l2_residual_lower_bound_plateau(self):
        for K, lb in ((13, mp.mpf('0.0329')), (30, mp.mpf('0.0367'))):
            mK = sum(F(mobius(n), n) for n in range(1, K + 1))
            tot = mp.mpf(0)
            for k in range(1, 20001):
                e = 1 - interp(K, k, mK)
                tot += mp.mpf(e.numerator) ** 2 / e.denominator ** 2 / (k * (k + 1))
            self.assertGreater(tot, lb)   # finite observation only: partial sums are lower bounds
    def test_D6_blackout_bound_vacuous(self):
        for N, Ex in ((8, mp.mpf('0.0242')), (14, mp.mpf('0.0185')), (30, mp.mpf('0.0145'))):
            L = lcm(*range(2, N + 1))
            self.assertLess(mp.mpf(1) / L ** 2, mp.mpf('2e-6') if N == 8 else mp.mpf('1e-11'))
            self.assertLess(mp.mpf(1) / L ** 2, Ex * mp.mpf('1e-4'))
        self.assertEqual(lcm(*range(2, 31)), 2329089562800)
    def test_D7_baez_duarte_ck(self):
        mp.mp.dps = 400
        try:
            def ck(k): return sum((-1) ** j * mp.binomial(k, j) / mp.zeta(2 * j + 2) for j in range(k + 1))
            self.assertLess(abs(ck(0) - mp.mpf('0.607927101854')), mp.mpf('1e-11'))
            self.assertLess(abs(ck(1) - mp.mpf('-0.316011301068')), mp.mpf('1e-11'))
            self.assertLess(abs(ck(10) - mp.mpf('-0.0691390655051')), mp.mpf('1e-12'))
            self.assertLess(abs(ck(100) - mp.mpf('-0.00147737763416')), mp.mpf('1e-13'))
            self.assertLess(abs(100 ** 2 * ck(100) + mp.mpf('14.77')), mp.mpf('0.01'))   # k^2 c_k near -14.77 at k=100 (approaching -16.42)
        finally:
            mp.mp.dps = 60

if __name__ == '__main__':
    unittest.main()
