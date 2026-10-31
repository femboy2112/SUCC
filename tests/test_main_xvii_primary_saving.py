"""Operation Main XVII — primary-only lag-one saving (regression).

Research-status. This exercises the one NEW rigorous sub-result of Main XVII and its
load-bearing calibrations. It proves NOTHING about pi base-16 normality, the signed Weyl
gate T_N(h)=o(N), or RH: it bounds the *primary* component of a per-prime first-birth
window, isolating the (open) cofiber cross-term.

Authentic BBP forcing (n>=1), U_0=0, U_n = 16 U_{n-1} + r(n):
    r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2).
For an eligible native prime p (p % 8 in {1,5}) the first-birth window has length
L = ord_p(16); the primary residue of U_{b_p+j} is a_j/p with a_j = c_p*16^j mod p.

New sub-result (NET-XVII-1): the primary-only lag-one energy
    Etil_p(h) = (1/(L-1)) sum_{j<L-1} [1 - cos(2*pi*h*((15*c_p*16^j mod p)/p))]
satisfies   Etil_p(h) >= 1 - (sqrt(p)+2)/(L-1),
a consequence of the classical subgroup/Gauss bound |sum_{g in <16>} e_p(a g)| <= sqrt(p)
for a != 0. It is nontrivial exactly when L > sqrt(p)+2 (the SC-06 order hypothesis).

This does NOT bound the *full* window sum |S_p(h)| (the cofiber can enlarge it; cf. SC-02),
and is not a saving on dyadic time-blocks. The cofiber cross-term stays OPEN.
"""

import cmath
import math
import unittest
from fractions import Fraction


def r(n):
    return (Fraction(4, 8 * n - 7) - Fraction(2, 8 * n - 4)
            - Fraction(1, 8 * n - 3) - Fraction(1, 8 * n - 2))


def u_sequence(nmax):
    """Exact U_0..U_nmax (Fraction)."""
    seq = [Fraction(0)]
    for n in range(1, nmax + 1):
        seq.append(16 * seq[-1] + r(n))
    return seq


def mult_order(a, p):
    o, x = 1, a % p
    while x != 1:
        x = (x * a) % p
        o += 1
    return o


def eligible(p):
    return p % 8 in (1, 5)


def birth_and_coeff(p):
    if p % 8 == 1:
        return (p + 7) // 8, 4
    return (p + 3) // 8, -1  # p % 8 == 5


def frac_phase(x):
    """Exact fractional part of a Fraction, then float. Never float() a huge Fraction first."""
    return float(x - math.floor(x))


# Eligible primes with L = ord_p(16) >= sqrt(p); small enough to stay fast and exact.
ELIGIBLE = [53, 461, 521, 541]
HARMONICS = (1, 3)
TOL = 1e-9


class PrimaryOnlySaving(unittest.TestCase):
    def test_eligible_have_long_order(self):
        for p in ELIGIBLE:
            self.assertTrue(eligible(p), p)
            L = mult_order(16, p)
            self.assertGreater(L, math.isqrt(p), (p, L))

    def test_subgroup_gauss_bound(self):
        """|sum_{g in <16>} e_p(a g)| <= sqrt(p) for every a != 0 (classical)."""
        for p in ELIGIBLE:
            L = mult_order(16, p)
            subgroup = [pow(16, t, p) for t in range(L)]
            worst = 0.0
            for a in range(1, p):
                s = sum(cmath.exp(2j * math.pi * (a * g % p) / p) for g in subgroup)
                worst = max(worst, abs(s))
            self.assertLessEqual(worst, math.sqrt(p) + TOL, (p, worst))

    def test_primary_only_energy_bound(self):
        """Etil_p(h) >= 1 - (sqrt(p)+2)/(L-1), the NET-XVII-1 sub-result."""
        for p in ELIGIBLE:
            L = mult_order(16, p)
            _, c_p = birth_and_coeff(p)
            bound = 1.0 - (math.sqrt(p) + 2.0) / (L - 1)
            for h in HARMONICS:
                e = 0.0
                for j in range(L - 1):
                    res = (15 * c_p * pow(16, j, p)) % p
                    e += 1.0 - math.cos(2 * math.pi * h * res / p)
                etil = e / (L - 1)
                self.assertGreaterEqual(etil + TOL, bound, (p, h, etil, bound))
                self.assertGreater(etil, 0.3, (p, h, etil))  # genuinely nontrivial

    def test_full_sc06_energy_exceeds_quarter(self):
        """Full lag-one energy E_p(h) >= 1/4 (SC-06, OPEN as a uniform theorem; checked here)."""
        for p in ELIGIBLE:
            L = mult_order(16, p)
            b, _ = birth_and_coeff(p)
            U = u_sequence(b + L)
            for h in HARMONICS:
                e = 0.0
                for j in range(L - 1):
                    d = U[b + j + 1] - U[b + j]
                    e += 1.0 - math.cos(2 * math.pi * h * frac_phase(d))
                self.assertGreater(e / (L - 1), 0.25, (p, h, e / (L - 1)))

    def test_primary_window_correctness(self):
        """U_{b+j} == a_j/p + v_j (mod 1) with denominator(v_j) coprime to p."""
        for p in (53, 461):
            L = mult_order(16, p)
            b, c_p = birth_and_coeff(p)
            U = u_sequence(b + L)
            for j in range(L):
                a_j = (c_p * pow(16, j, p)) % p
                v = (U[b + j] - Fraction(a_j, p))
                v = v - math.floor(v)
                self.assertNotEqual(v.denominator % p, 0, (p, j))


class CoherentCounterControls(unittest.TestCase):
    """Any proof of SC-06 must EXCLUDE these; their lag-one energy must vanish."""

    def test_sc05_same_forcing_block_coherent_seed(self):
        A, B, K = 20, 40, 6
        M = B + K
        U = u_sequence(M + 1)
        q_M = sum(r(n) / Fraction(16) ** n for n in range(1, M + 1))
        s_M = Fraction(-math.floor(Fraction(16) ** M * q_M), 16 ** M)
        seeded = [U[n] + Fraction(16) ** n * s_M for n in range(M + 1)]
        for h in (1, 2, 3):
            e = 0.0
            for n in range(A, B):
                d = seeded[n + 1] - seeded[n]
                e += 1.0 - math.cos(2 * math.pi * h * frac_phase(d))
            self.assertLess(e / (B - A), 1e-8, (h, e / (B - A)))
        # contrast: the uncoordinated authentic orbit is NOT coherent on the same window
        e0 = sum(1.0 - math.cos(2 * math.pi * frac_phase(U[n + 1] - U[n]))
                 for n in range(A, B)) / (B - A)
        self.assertGreater(e0, 0.25)

    def test_at07_seven_pole_null_coherent(self):
        """z = w - 2r (BBP null), E_0=0: -1/(8n+1) < E_n < 0, phases coherent."""
        def w(n):
            return (Fraction(8, 8 * n - 6) + Fraction(4, 8 * n - 5)
                    + Fraction(4, 8 * n - 4) - Fraction(1, 8 * n - 1))
        E = [Fraction(0)]
        for n in range(1, 60):
            E.append(16 * E[-1] + (w(n) - 2 * r(n)))
        for n in range(1, 40):
            self.assertLess(E[n], 0, n)
            self.assertGreater(E[n], Fraction(-1, 8 * n + 1), n)
        e = sum(1.0 - math.cos(2 * math.pi * frac_phase(E[n + 1] - E[n]))
                for n in range(20, 40)) / 20
        self.assertLess(e, 1e-6, e)


if __name__ == "__main__":
    unittest.main()
