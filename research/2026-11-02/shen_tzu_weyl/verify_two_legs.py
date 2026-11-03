"""Verify the WB-02 exact signed decomposition and the two-leg structure of the Weyl sum.

S_N(h)/N = g_M(h) sum_a e(ha/M)(p_a - 1/M) + C_(N,M)(h)  [cell imbalance + cofiber].
Shows the cofiber C_(N,M)(h) decays in M while cell-imbalance grows (as M -> N).
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


def frac(u):
    return u - Q(u.numerator // u.denominator)


def e(t):
    return mp.exp(2j*mp.pi*t)


def main():
    mp.mp.dps = 80
    U = states(512)
    N = 512
    print("=== WB-02 decomposition + two-leg structure (N=512) ===")
    for h in [1, 3, 5]:
        print("--- h=%d ---" % h)
        for M in [16, 32, 64, 128, 256]:
            a = []; s = []
            for n in range(1, N+1):
                f = frac(U[n])
                an = (M*f.numerator)//f.denominator
                sn = M*f - Q(an)
                a.append(an); s.append(sn)
            p = {}
            for an in a:
                p[an] = p.get(an, 0) + 1
            gM = mp.mpf(0) if h % M == 0 else (e(h/mp.mpf(M))-1)/(2j*mp.pi*h/mp.mpf(M))
            SN = mp.mpc(0)
            for n in range(1, N+1):
                SN += e(h*frac(U[n]))
            SN = SN/N
            term1 = mp.mpc(0); cofiber = mp.mpc(0)
            for an in range(M):
                pa = p.get(an, 0)
                term1 += gM * e(h*Q(an, M)) * (Q(pa, N) - Q(1, M))
                if pa == 0:
                    continue
                w = mp.mpc(0)
                for n in range(1, N+1):
                    if a[n-1] == an:
                        w += e(h*s[n-1]/M)
                w = w/N
                d = w - Q(pa, N)*gM
                cofiber += e(h*Q(an, M))*d
            imb = sum(abs(Q(p.get(an,0),N) - Q(1,M)) for an in range(M))
            print("  M=%3d  |S_N/N|=%.5f  |cofiber|=%.6f  |cell-imbalance|=%.5f  (decomp err %.1e)"
                  % (M, abs(SN), abs(cofiber), imb, abs(SN-term1-cofiber)))


if __name__ == '__main__':
    main()
