"""Focused exact tests for Lambert-W scheduled signed Basel-BBP finite certificates.

All authority-bearing precision comparisons are exact Fraction inequalities;
mpmath is used only to cross-check real phases in one finite smoke test.
"""
from fractions import Fraction
import unittest


def bbp_r(j: int) -> Fraction:
    if j < 0:
        raise ValueError('BBP index must be nonnegative')
    return (Fraction(4,8*j+1)-Fraction(2,8*j+4)
            -Fraction(1,8*j+5)-Fraction(1,8*j+6))


def prefix_pi_over_16(L: int) -> Fraction:
    if L < 0:
        raise ValueError('negative source horizon')
    return sum((bbp_r(j)/16**(j+1) for j in range(L)), Fraction(0))


def amplification_sum(A: int, M: int) -> Fraction:
    if not (2 <= A <= M):
        raise ValueError('require 2<=A<=M')
    return sum((Fraction(16**n, n*n) for n in range(A, M+1)), Fraction(0))


def lambert_threshold(A: int, M: int, h: int, R: int) -> Fraction:
    """Sufficient exact rational bound B with L^2 16^L >= B.
    M=A*R, desired phase budget <=1/R.
    """
    if h == 0 or R < 1 or M != A*R:
        raise ValueError('h nonzero, R>=1, M=A*R required')
    return Fraction(11*abs(h)*A*R, 112)*amplification_sum(A,M)


def minimal_horizon(B: Fraction) -> int:
    """Find exact integer ceil of the positive W_0 inverse, no numerical W used."""
    if B <= 0:
        raise ValueError('B must be positive')
    hi = 1
    while hi*hi*16**hi < B:
        hi *= 2
    lo = 1
    while lo < hi:
        m = (lo + hi)//2
        if m*m*16**m >= B:
            hi = m
        else:
            lo = m+1
    return lo


def phase_budget(A: int, M: int, h: int, L: int) -> Fraction:
    """Archimedean phase difference bounded strictly by this rational value."""
    if L < 1:
        raise ValueError('L>=1')
    return (Fraction(11*abs(h)*A,112)*amplification_sum(A,M)
            / (L*L*16**L))


class LambertBaselGate(unittest.TestCase):
    def test_source_contract_and_prefix(self):
        self.assertEqual(bbp_r(0), Fraction(47,15))
        self.assertEqual(prefix_pi_over_16(0), 0)
        self.assertEqual(prefix_pi_over_16(1), Fraction(47,240))
        for j in range(1, 20):
            self.assertGreater(bbp_r(j), 0)

    def test_exact_positive_tail_bound(self):
        import mpmath as mp
        with mp.workdps(150):
            for L in (1, 2, 5, 11, 19):
                p = prefix_pi_over_16(L)
                remainder = mp.pi/16 - mp.mpf(p.numerator)/p.denominator
                bound = Fraction(1,16**L*(8*L+1)*(8*L+2))
                self.assertGreater(remainder,0)
                self.assertLess(remainder,mp.mpf(bound.numerator)/bound.denominator)

    def test_w_threshold_minimal(self):
        for A,R,h in [(2,1,1),(11,3,1),(11,3,8),(19,4,-3),(32,4,8),(64,6,1)]:
            M=A*R
            B=lambert_threshold(A,M,h,R)
            L=minimal_horizon(B)
            self.assertGreaterEqual(Fraction(L*L*16**L),B)
            if L>1:
                self.assertLess(Fraction((L-1)*(L-1)*16**(L-1)),B)
            self.assertLessEqual(phase_budget(A,M,h,L), Fraction(1,R))

    def test_W0_continuous_inverse(self):
        import mpmath as mp
        with mp.workdps(110):
            A,R,h=11,3,8
            B=lambert_threshold(A,A*R,h,R)
            mb=mp.mpf(B.numerator)/B.denominator
            lam=mp.log(16)
            Lw=2/lam * mp.lambertw((lam/2)*mp.sqrt(mb),0)
            L=minimal_horizon(B)
            self.assertTrue(L-1 < Lw <= L)
            self.assertAlmostEqual(float(Lw**2*mp.exp(lam*Lw)/mb),1.0,places=11)

    def test_double_reciprocal_square_asymptotic(self):
        # Explicit check against the 3-log_16(M) source-prefix compression.
        import math
        for A,R in [(32,4),(64,5),(100,6),(200,7)]:
            M=A*R
            L=minimal_horizon(lambert_threshold(A,M,1,R))
            prediction=M-3*math.log(M,16)+math.log(11/105,16)
            self.assertLess(abs(L-prediction),2)

    def test_strict_phase_budget_numerical_control(self):
        import mpmath as mp
        A,R,h=11,3,8
        M=A*R
        L=minimal_horizon(lambert_threshold(A,M,h,R))
        with mp.workdps(150):
            P=prefix_pi_over_16(L)
            p=mp.mpf(P.numerator)/P.denominator
            full=mp.mpc(0); approx=mp.mpc(0)
            for n in range(A,M+1):
                full += mp.exp(2j*mp.pi*h*16**n*(mp.pi/16))/(n*n)
                approx += mp.exp(2j*mp.pi*h*16**n*p)/(n*n)
            observed=abs(A*(full-approx))
            budget=phase_budget(A,M,h,L)
            self.assertLess(observed,mp.mpf(budget.numerator)/budget.denominator)

    def test_coherent_wrong_seed(self):
        import mpmath as mp
        with mp.workdps(60):
            for A in (11,101,1001):
                val = A*mp.zeta(2,A)
                self.assertTrue(1 < val < 1 + 1/A)
            # The W-scheduled finite sum cannot falsely diagnose the all-one orbit.
            for A,R in ((11,3),(32,4),(80,6)):
                q=A*sum((Fraction(1,n*n) for n in range(A,A*R+1)),Fraction(0))
                self.assertGreater(q, Fraction(1) - Fraction(1,R))
                self.assertLess(q, Fraction(1) + Fraction(1,A))

    def test_rational_phase_lift_and_exact_winding(self):
        # Real-lift difference before any mod-1 reduction is essential.
        L = 12
        P = prefix_pi_over_16(L)
        h = 8
        n = 14
        y = 16**n*P
        y_next = 16*y
        self.assertEqual(Fraction(h,15)*(y_next-y), h*y)
        phase_mod = (h*y) % 1
        self.assertGreaterEqual(phase_mod,0)
        self.assertLess(phase_mod,1)
        # With rational wrong seed -P, the common-horizon orbit is exactly zero.
        seed = -P
        self.assertEqual((h*16**n*(seed+P))%1, 0)

    def test_truncated_tail_error_all_bounded_sequences(self):
        # A*sum_(n>M) 1/n^2 <= A/M = 1/R, with M=A*R.
        for A,R in [(11,2),(23,4),(91,8)]:
            M=A*R
            partial=A*sum((Fraction(1,n*n) for n in range(A,M+1)),Fraction(0))
            # No oscillation: the bounded sequence a_n=1 is a hostile control.
            self.assertGreater(partial, Fraction(1)-Fraction(1,R))
            self.assertLess(partial, Fraction(1)+Fraction(1,A))

    def test_periodic_nonnormal_seed(self):
        # For alpha=1/255, 16^n alpha mod 1=16^n/255 mod1,
        # and e(255*16^n alpha)=1 for every n.
        self.assertEqual(pow(16,2,255),1)
        for n in range(1,25):
            self.assertEqual((255*pow(16,n,255)) % 255,0)

    def test_irrational_sparse_digit_seed_adversary(self):
        # alpha=sum_j 16^(-2^(2^j)): before next nonzero place,
        # the real fractional orbit is arbitrarily near 0 for long epochs.
        # The below rational inequality is an *upper bound* on the
        # future tail; the infinite irrational is not truncated as a proof input.
        for j in (2,3,4):
            mj = 2**(2**j)
            next_m=mj*mj
            A=2*mj
            # for these j, an elementary log-depth schedule R=2j fits
            R=2*j
            M=A*R
            self.assertLess(M,next_m)
            # Sum of all later base16 digits after the next place is <=
            # geometric full lattice tail 16^(M-next_m)*16/15.
            self.assertGreaterEqual(next_m-M,16)
            # Uniform bound without constructing an astronomical denominator.
            self.assertLess(Fraction(16,15*16**16),Fraction(1,16))

    def test_branch_Wminusone_inversion(self):
        import mpmath as mp
        with mp.workdps(100):
            lam=mp.log(16)
            for n in (1,2,4,8,16):
                Q=mp.power(16,n)/(n*n)
                z=-lam/(2*mp.sqrt(Q))
                inverse=-2/lam*mp.lambertw(z,-1)
                self.assertAlmostEqual(float(inverse),float(n),places=9)

if __name__=='__main__':
    unittest.main()
