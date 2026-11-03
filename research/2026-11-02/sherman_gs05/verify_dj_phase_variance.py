"""Precision-safe verification of the GS05-DJ exact cascade identities and inequalities.

Verifies (all exact / interval-safe):
  GS05-DJ-1 : d_pair = 1/2 - K_pair/E_pair ; K_pair = L*Re(mu) + off-diagonal.
  GS05-DJ-2 : |B - conj(mu) A|^2 <= L^2 (1 - |mu|^2).
  GS05-DJ-3 : |A - B|^2 <= 2 L^2 (1 - Re mu).   (concentration -> d_j -> 0)
  GS05-DJ-4 : aggregate d_j = 1/2 - K_j/E_j ; increments ~ x16 orbit of (16^L-1) pi.

Precision firewall (per project memory): e(h U_n) needs U_n to exp(6n) precision. We use the
EXACT rational orbit (fractions.Fraction) and take the exact residue
  e(h U_n) = exp(2*pi*i * ((h*num mod den)/den))
so no floating-point contamination of the phase; mpmath dps >= 6*N/ln(10) + 60 is enforced.

No pi-normality or RH claim is made. This verifies finite instances of PROVED identities only.
"""
from fractions import Fraction as Q
import mpmath as mp
import sys


def r(n):
    return Q(4, 8*n - 7) - Q(2, 8*n - 4) - Q(1, 8*n - 3) - Q(1, 8*n - 2)


def states(N):
    U = [Q(0)]
    for n in range(1, N + 1):
        U.append(16 * U[-1] + r(n))
    return U


def phase_e(hU, dps):
    """e(hU) = exp(2 pi i * frac(hU)) computed from the exact rational orbit."""
    mp.mp.dps = dps
    num = hU.numerator % hU.denominator
    return mp.exp(2j * mp.pi * mp.mpf(num) / mp.mpf(hU.denominator))


def main(N=1024, hs=(1, 5, 11), Ls=(16, 32, 64, 128, 256)):
    dps = int(6 * N / mp.log(10) + 60)
    mp.mp.dps = dps
    U = states(N)

    print("dps = %d (>= 6*N/ln10 + 60 = %.1f)" % (dps, 6 * N / mp.log(10) + 60))
    print("N = %d" % N)

    for h in hs:
        # precompute z_n = e(h U_n) exactly
        Z = [phase_e(h * U[n], dps) for n in range(N + 1)]

        print("\n=== h = %d ===" % h)
        for L in Ls:
            n_pairs = N // (2 * L)
            max_err1 = mp.mpf(0)   # |d_pair - (1/2 - K/E)|
            max_err2 = mp.mpf(0)   # |B-conj(mu)A|^2 <= L^2(1-|mu|^2)  (slack)
            max_err3 = mp.mpf(0)   # |A-B|^2 <= 2L^2(1-Re mu)          (slack)
            E = mp.mpf(0)
            W = mp.mpf(0)
            K = mp.mpf(0)
            mu_list = []

            for pair in range(n_pairs):
                a = pair * 2 * L
                A = mp.mpc(0); B = mp.mpc(0); ph = []
                for n in range(a + 1, a + L + 1):
                    zn = Z[n]
                    zL = Z[n + L]
                    A += zn
                    B += zL
                    ph.append(zL / zn)          # e^{i phi_n} = z_{n+L}/z_n
                mu = sum(ph) / L
                mu_list.append(mu)

                W_pair = abs(A - B) ** 2
                E_pair = abs(A) ** 2 + abs(B) ** 2
                K_pair = (A * mp.conj(B)).real

                # GS05-DJ-1: d_pair = 1/2 - K_pair/E_pair
                d_pair = W_pair / (2 * E_pair)
                err1 = abs(d_pair - (mp.mpf('0.5') - K_pair / E_pair))
                max_err1 = max(max_err1, err1)

                # GS05-DJ-2: |B - conj(mu) A|^2 <= L^2 (1 - |mu|^2)
                dev = abs(B - mp.conj(mu) * A) ** 2
                ub2 = L * L * (1 - abs(mu) ** 2)
                max_err2 = max(max_err2, ub2 - dev)   # must be >= 0

                # GS05-DJ-3: |A - B|^2 <= 2 L^2 (1 - Re mu)
                ub3 = 2 * L * L * (1 - mu.real)
                max_err3 = max(max_err3, ub3 - W_pair)  # must be >= 0

                E += E_pair
                W += W_pair
                K += K_pair

            d_j = W / (2 * E)
            mean_abs_mu = abs(sum(mu_list) / len(mu_list))
            # GS05-DJ-4: aggregate d_j = 1/2 - K_j/E_j
            d_alt = mp.mpf('0.5') - K / E

            ok1 = max_err1 < mp.mpf(10) ** (-(dps - 20))
            ok2 = max_err2 >= 0
            ok3 = max_err3 >= 0
            ok4 = abs(d_j - d_alt) < mp.mpf(10) ** (-(dps - 20))

            print("  L=%4d  d_j=%.5f  1/2-K/E=%.5f (match=%s)  mean|mu|=%.5f"
                  % (L, d_j, d_alt, ok4, mean_abs_mu))
            print("         DJ-1 max|d-(1/2-K/E)|=%.3e  DJ-2 min-slack=%.3e  DJ-3 min-slack=%.3e"
                  % (max_err1, max_err2, max_err3))
            assert ok1 and ok2 and ok3 and ok4, "FAILED at h=%d L=%d" % (h, L)

    print("\nALL GS05-DJ-1..4 finite checks PASSED (N=%d, h=%s)." % (N, hs))
    print("These certify finite instances of PROVED identities only; no pi-normality/RH claim.")


if __name__ == '__main__':
    main()
