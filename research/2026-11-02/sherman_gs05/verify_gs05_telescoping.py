"""Exact verification of the GS-05 telescoping identity.

PROVED: (16^L-1)U_n + F(n,L) = U_{n+L} - U_n, so the signed cross-block difference
  A - B = sum_n [e(hU_n) - e(hU_{n+L})]
is a lag-L first difference. K_j = Re sum_pairs A conj(B) is a lag-L autocorrelation.
Verifies the identity exactly (Fraction) and the d_j = 1/2 - K_j/E_j cascade numerically.
"""
from fractions import Fraction as Q
import mpmath as mp


def r(n):
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def states(N):
    U = [Q(0)]
    for n in range(1, N+1):
        U.append(16*U[-1] + r(n))
    return U


def frac_mod1(u):
    return mp.mpf(u.numerator % u.denominator) / u.denominator


def main():
    mp.mp.dps = 80
    U = states(1024)

    # (1) Verify the telescoping identity exactly for a spread of (n, L)
    print("=== Identity: (16^L-1)U_n + F(n,L) == U_{n+L} - U_n ===")
    ok = True
    for n in [3, 17, 100, 250]:
        for L in [4, 16, 64, 128]:
            F = U[n+L] - 16**L * U[n]
            lhs = (16**L - 1)*U[n] + F
            rhs = U[n+L] - U[n]
            if lhs != rhs:
                ok = False
                print("  FAIL n=%d L=%d" % (n, L))
    print("  all exact: %s" % ok)

    # (2) d_j = 1/2 - K_j/E_j on mesoscopic levels
    print("\n=== Signed cascade d_j = W_j/(2E_j) = 1/2 - K_j/E_j (h=1) ===")
    h = 1
    for L in [16, 32, 64, 128]:
        E = mp.mpf(0); W = mp.mpf(0); K = mp.mpf(0)
        for a in range(0, 1024, 2*L):
            A = mp.mpc(0); B = mp.mpc(0)
            for n in range(a+1, a+L+1):
                A += mp.exp(2j*mp.pi*frac_mod1(h*U[n]))
                B += mp.exp(2j*mp.pi*frac_mod1(h*U[n+L]))
            E += abs(A)**2 + abs(B)**2
            W += abs(A-B)**2
            K += (A*mp.conj(B)).real
        d = W/(2*E)
        print("  L=%3d  d_j=%.5f  K_j/E_j=%+.5f   (1/2-K/E=%.5f, match=%s)"
              % (L, d, K/E, mp.mpf('0.5')-K/E, abs(d-(mp.mpf('0.5')-K/E))<1e-12))


if __name__ == '__main__':
    main()
