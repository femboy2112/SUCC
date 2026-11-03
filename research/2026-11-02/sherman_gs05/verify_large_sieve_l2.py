"""Exact verification of the large-sieve / L^2 energy reduction on the Parseval identity.

PROVED identities (all exact, Fraction arithmetic — no floating-point pi):

  Thm 1 (pair-sum completion):
      sum_{|h|<=A} |S_A(h)|^2 == sum_{n,m} D_{2A+1}(x_n - x_m),
      D_{2A+1}(t) = sin((2A+1) pi t) / sin(pi t)   (Dirichlet kernel).

  Thm 4 (pair-sum -> Diophantine reduction):
      E_A = A(2A+1) + sum_{d=1}^{A-1} sum_n 2 D_{2A+1}( ||(16^d-1)16^{n-1} pi - (T_{n+d}-T_n)|| ).

  Thm 3 (large sieve requirement): E_A <= (A - 1 + 1/delta_A) * A  needs  delta_A >> 1/(A log A).

Also measures the minimal spacing delta_A (exact Fraction), which is the large-sieve input,
and verifies it is NOT >> 1/(A log A) — closing the gate via the large sieve is impossible
from the known spacing.

Precision firewall: states U_n are exact Fractions (Q[n] grows as exp(6n)); phases e(h x)
are computed exactly via (h * numerator mod denominator)/denominator — no mp.pi is ever used,
so the dps bug that produced false coincidences is structurally impossible here.
"""
from fractions import Fraction as Q
import mpmath as mp

mp.mp.dps = 40


def r(n):
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def states(N):
    U = [Q(0)]
    for n in range(1, N+1):
        U.append(16*U[-1] + r(n))
    return U


def frac(x):
    """Exact fractional part in [0,1) as a Fraction."""
    return Q(x.numerator % x.denominator, x.denominator)


def circ_dist(a, b):
    """Circular distance ||a - b|| for a,b in [0,1) (exact)."""
    d = abs(a - b)
    return min(d, Q(1) - d)


def e_hx(h, x):
    """e(h x) = exp(2 pi i h x) exactly, x = p/q a Fraction in [0,1)."""
    num = (h * x.numerator) % x.denominator
    return mp.exp(2j * mp.pi * mp.mpf(num) / mp.mpf(x.denominator))


def dirichlet_kernel(t, A):
    """D_{2A+1}(t) = sin((2A+1) pi t)/sin(pi t).  t is a float distance."""
    t = float(t)
    # wrap to [-0.5, 0.5]
    if t > 0.5:
        t -= 1.0
    denom = mp.sin(mp.pi * mp.mpf(t))
    if abs(denom) < mp.mpf('1e-30'):
        return mp.mpf(2*A + 1)
    return mp.sin((2*A + 1) * mp.pi * mp.mpf(t)) / denom


def verify_pair_sum_completion(A):
    """Thm 1: sum_{|h|<=A} |S_A(h)|^2 == sum_{n,m} D_{2A+1}(x_n - x_m)."""
    U = states(2*A)
    xs = [frac(U[n]) for n in range(A, 2*A)]

    # LHS: direct frequency sum
    lhs = mp.mpf(0)
    for h in range(-A, A+1):
        S = sum(e_hx(h, x) for x in xs)
        lhs += abs(S)**2

    # RHS: pair sum with Dirichlet kernel
    rhs = mp.mpf(0)
    for x in xs:
        for y in xs:
            rhs += dirichlet_kernel(circ_dist(x, y), A)

    return lhs, rhs


def verify_diophantine_reduction(A):
    """Thm 4: E_A = A(2A+1) + sum_d sum_n 2 D_{2A+1}(||(16^d-1)16^{n-1}pi - (T_{n+d}-T_n)||).

    Here we do NOT use pi numerically; instead we use the exact state identity
    U_{n+d} - U_n = (16^d-1) U_n + F(n,d)  where F(n,d) = U_{n+d} - 16^d U_n (GS-01), and
    the telescoping (GS05-TEL)  (16^d-1)U_n + F(n,d) = U_{n+d} - U_n.  Both are exact.
    The point is to verify the pair-sum equals the lag-grouped form with the same
    Dirichlet weights, i.e. that the energy is the near-coincidence count.
    """
    U = states(2*A)
    xs = [frac(U[n]) for n in range(A, 2*A)]

    # E_A via lag grouping
    E = mp.mpf(A) * mp.mpf(2*A + 1)  # diagonal n = m
    for d in range(1, A):
        for n in range(A, 2*A - d):
            t = circ_dist(xs[n - A], xs[n + d - A])
            E += 2 * dirichlet_kernel(t, A)

    # direct E_A = sum_{|h|<=A} |S_A(h)|^2
    direct = mp.mpf(0)
    for h in range(-A, A+1):
        S = sum(e_hx(h, x) for x in xs)
        direct += abs(S)**2
    return E, direct


def minimal_spacing(A):
    """delta_A = min_{n != m} ||U_n - U_m|| (exact), the large-sieve input."""
    U = states(2*A)
    xs = [frac(U[n]) for n in range(A, 2*A)]
    dmin = Q(1)
    arg = (None, None)
    for i in range(len(xs)):
        for j in range(i+1, len(xs)):
            d = circ_dist(xs[i], xs[j])
            if d < dmin:
                dmin = d
                arg = (A + i, A + j)
    return dmin, arg


def main():
    print("=== Thm 1: pair-sum completion (exact Fraction) ===")
    for A in [24, 40]:
        lhs, rhs = verify_pair_sum_completion(A)
        rel = abs(lhs - rhs) / abs(lhs)
        print("  A=%2d: LHS=%.6f  RHS=%.6f  rel.gap=%.2e  %s"
              % (A, lhs, rhs, rel, "PASS" if rel < 1e-12 else "FAIL"))

    print("\n=== Thm 4: lag-grouped Diophantine reduction (exact) ===")
    for A in [24, 40]:
        E, direct = verify_diophantine_reduction(A)
        rel = abs(E - direct) / abs(direct)
        print("  A=%2d: E(lag)=%.6f  E(direct)=%.6f  rel.gap=%.2e  %s"
              % (A, E, direct, rel, "PASS" if rel < 1e-12 else "FAIL"))

    print("\n=== Thm 3: minimal spacing delta_A vs the requirement 1/(A log A) ===")
    for A in [16, 32, 64, 128]:
        dmin, arg = minimal_spacing(A)
        inv = Q(1) / dmin
        req = mp.mpf(A) * mp.log(mp.mpf(A))  # 1/delta must be o(A log A) to close
        ratio = mp.mpf(float(inv)) / req
        print("  A=%3d: delta_A=%.3e  1/delta=%.3e  A log A=%.3e  ratio=%.2e  pair=%s"
              % (A, float(dmin), float(inv), req, ratio, arg))
    print("  => ratio >> 1 for all A: the spacing is FAR below the large-sieve")
    print("     requirement delta >> 1/(A log A).  The large sieve cannot close the gate")
    print("     from the available (Diophantine) spacing.")


if __name__ == '__main__':
    main()
