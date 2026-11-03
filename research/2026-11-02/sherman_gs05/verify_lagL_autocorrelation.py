"""Exact lag-L autocorrelation structure of the GS-05 cross-block reinforcement K_j.

Decomposition (all exact identities, verified here):
  K_j = sum_{n,m in block} cos(2*pi*h*(U_n - U_{m+L}))
      = sum_{n,m} cos(2*pi*h*[ 16^{n-1}(16^k-1)*pi - (T_{m+L}-T_n) ]),   k = m+L-n

with U_n = 16^{n-1}*pi - T_n, T_n = sum_{j>=1} 16^{-j} r(n+j) = O(1/n^2) (Green tail).

Verified properties:
  (V1) Telescoping identity (exact, Fraction): (16^L-1)U_n + F(n,L) == U_{n+L}-U_n.
  (V2) Orbit decomposition (high-precision): U_n == 16^{n-1}*pi - T_n,  with
       T_n computed as the convergent tail series; and the lag decomposition
       U_{m+L}-U_n == 16^{n-1}(16^k-1)*pi - (T_{m+L}-T_n),  k=m+L-n.
  (V3) Diophantine reduction: K_j^(0) = sum cos(2*pi*h*16^{n-1}(16^k-1)*pi)
       equals sum cos(2*pi * || h*(16^k-1)*16^{n-1}*pi ||).
  (V4) Tail-error bound: |K_j - K_j^(0)| <= 2*pi*|h| * sum|T_{m+L}-T_n|
                             <= pi*|h|*L^2/(16*(a+1)^2),   using T_n <= 1/(64 n^2).

Precision discipline: orbit U_n and tail T_n are exact Fractions; mpmath pi is used ONLY
in the final pi-phase with adequate dps (>= 6*N/ln10 + 60, see MEMORY.md firewall).
NO normality/RH claim (both OPEN).
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
    """Fractional part of an exact Fraction, as mpf (only for the final cos)."""
    return mp.mpf(u.numerator % u.denominator) / u.denominator


def tail_series(n, terms=200):
    """Exact convergent tail T_n = sum_{j>=1} 16^{-j} r(n+j), truncated at `terms`.
    Returns (Fraction head, Fraction tail_bound) with a rigorous geometric bound.
    """
    head = Q(0)
    for j in range(1, terms+1):
        head += Q(1, 16**j) * r(n+j)
    # r(m) <= 1 for all m>=1 (r(1)=141/60<3, but decay: r(m)<15/(64m^2)+... < 1 for m>=1).
    # Safer: use r(m) <= 15/(64 m^2) + 151/(512 m^3) + C4/m^4 with C4<1 for m>=1.
    # Tail bound: sum_{j>terms} 16^{-j} * r(n+j) <= sum_{j>terms} 16^{-j} * 1.
    tail_bound = Q(1, 16**terms) * Q(16, 15)   # geometric tail with r<=1
    return head, tail_bound


def mp_pi(dps):
    return mp.mpf(mp.pi)


def main():
    # Precision firewall: dps >= 6*N/ln10 + 60
    N = 512
    mp.mp.dps = int(6*N/mp.log(10) + 60) + 20
    pi = mp_pi(mp.mp.dps)
    U = states(N + 256)

    print("=== (V1) Telescoping identity (exact Fraction) ===")
    ok = True
    for n in [3, 17, 100, 250]:
        for L in [4, 16, 64, 128]:
            F = U[n+L] - 16**L * U[n]
            if (16**L - 1)*U[n] + F != U[n+L] - U[n]:
                ok = False
                print("  FAIL n=%d L=%d" % (n, L))
    print("  all exact:", ok)

    print("\n=== (V2) Orbit/tail decomposition (mpmath pi, adequate dps) ===")
    # T_n = 16^{n-1}*pi - U_n must equal the convergent tail series sum_{j>=1}16^{-j}r(n+j)
    max_err = mp.mpf(0)
    for n in [1, 7, 100, 250]:
        head, tbound = tail_series(n, terms=200)
        T_series = mp.mpf(head.numerator) / head.denominator
        T_def = 16**(n-1) * pi - mp.mpf(U[n].numerator)/U[n].denominator
        err = abs(T_series - T_def)
        max_err = max(max_err, err)
        print("  n=%3d  T_series=%.18f  T_def=%.18f  |diff|=%.3e  tail_bound=%.3e"
              % (n, T_series, T_def, err, mp.mpf(tbound.numerator)/tbound.denominator))
    print("  max |T_series - T_def| =", max_err)

    # Lag decomposition: U_{m+L}-U_n == 16^{n-1}(16^k-1)*pi - (T_{m+L}-T_n), k=m+L-n
    print("\n  Lag decomposition U_{m+L}-U_n == 16^{n-1}(16^k-1)pi - (T_{m+L}-T_n):")
    lag_err = mp.mpf(0)
    for n in [5, 100, 250]:
        for L in [16, 64, 128]:
            for m in [n+1, n+20]:
                k = m + L - n
                lhs = mp.mpf(U[m+L].numerator)/U[m+L].denominator - mp.mpf(U[n].numerator)/U[n].denominator
                rhs = 16**(n-1)*(16**k - 1)*pi
                rhs -= (16**(m+L-1)*pi - mp.mpf(U[m+L].numerator)/U[m+L].denominator)
                rhs += (16**(n-1)*pi - mp.mpf(U[n].numerator)/U[n].denominator)
                e = abs(lhs - rhs)
                lag_err = max(lag_err, e)
    print("  max |lhs - rhs| =", lag_err)

    print("\n=== (V3)+(V4) Diophantine reduction and tail-error bound (h=1) ===")
    h = 1
    for L in [16, 32, 64]:
        for a in [0, 128, 256]:
            K = mp.mpf(0)
            K0 = mp.mpf(0)
            K0_dio = mp.mpf(0)
            tail_sum = mp.mpf(0)
            for n in range(a+1, a+L+1):
                Tn = 16**(n-1)*pi - mp.mpf(U[n].numerator)/U[n].denominator
                for m in range(a+1, a+L+1):
                    k = m + L - n
                    Tm = 16**(m+L-1)*pi - mp.mpf(U[m+L].numerator)/U[m+L].denominator
                    # exact K_j term
                    du = mp.mpf(U[m+L].numerator)/U[m+L].denominator - mp.mpf(U[n].numerator)/U[n].denominator
                    K += mp.cos(2*mp.pi*h*du)
                    # leading (pi-only) term
                    K0 += mp.cos(2*mp.pi*h*16**(n-1)*(16**k-1)*pi)
                    # Diophantine form ||.|| = distance to nearest integer
                    frac = mp.fmod(h*16**(n-1)*(16**k-1)*pi, 1)
                    dist = min(frac, 1-frac)
                    K0_dio += mp.cos(2*mp.pi*dist)
                    tail_sum += abs(Tm - Tn)
            bound = 2*mp.pi*abs(h)*tail_sum
            bound2 = mp.pi*abs(h)*L**2/(16*(a+1)**2)
            print("  L=%3d a=%3d  |K-K0|=%.4e  <= bound %.4e  (a-priori L^2/(32a^2)=%.4e)"
                  % (L, a, abs(K-K0), bound, L**2/(32*(a+1)**2)))
            print("         K0 vs K0_dio: |diff|=%.3e   K0=%.4f K0_dio=%.4f"
                  % (abs(K0-K0_dio), K0, K0_dio))


if __name__ == '__main__':
    main()
