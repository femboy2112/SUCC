#!/usr/bin/env python3
"""
OPTIMAL L2(w) approximation of the constant 1 by the first N residue clocks.

Setup (from task):
  r_n(k) = (k mod n)/n   for cells k >= 1   (least nonneg residue; r_n in {0,1/n,...,(n-1)/n})
  weight  w_k = 1/(k(k+1))
  inner product  <f,g> = sum_{k>=1} f(k) g(k) / (k(k+1))

  E_N* = min_{rational a_2..a_N} || 1 - sum_{n=2}^{N} a_n r_n ||^2
       = 1 - b^T G^{-1} b
  with Gram matrix G_{mn} = <r_m, r_n>, target b_n = <1, r_n>.

Because r_m r_n is periodic of period L = lcm(m,n), the Gram entries reduce to
  <r_m, r_n> = sum_{r=0}^{L-1} (r mod m)/m * (r mod n)/n * S_r(L)
  S_r(L) = sum_{k>=1, k == r (mod L)} 1/(k(k+1))
which is a digamma-type sum (no elementary closed form).

S_r(L) is computed TWO independent ways (Instrument Rule #2):
  (a) digamma closed form:  S_r(L) = (1/L) [ psi((k0+1)/L) - psi(k0/L) ], k0 = r if r>=1 else L
  (b) mp.nsum with convergence acceleration (independent algorithm)

Calibration receipt (N=2 closed form, from task):
  single clock r_2, optimal a = 2, E_2* = 1 - ln 2 = 0.30685281944005469058...

Everything is arbitrary precision (mpmath dps = 60); nothing here is a proof.
"""
import mpmath as mp
from math import lcm, gcd

mp.mp.dps = 60
PREC = 60

def mobius(n):
    # simple mobius for n in 2..8 (also works generally for small n)
    if n < 1:
        raise ValueError
    if n == 1:
        return 1
    mu = 1
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0:
                return 0
            mu = -mu
        p += 1
    if x > 1:
        mu = -mu
    return mu

# ---- S_r(L): two independent implementations ----
def S_residue_digamma(r, L):
    """sum_{k>=1, k==r mod L} 1/(k(k+1))  via digamma."""
    k0 = r if r >= 1 else L
    return (mp.psi(0, mp.mpf(k0 + 1) / L) - mp.psi(0, mp.mpf(k0) / L)) / L

def S_residue_nsum(r, L):
    """Same quantity via mpmath accelerated infinite sum (independent route)."""
    k0 = r if r >= 1 else L
    f = lambda j: 1.0 / ((k0 + j * L) * (k0 + j * L + 1))
    return mp.nsum(f, [0, mp.inf])

# ---- residue clock values ----
def r_clock(n, k):
    return mp.mpf(k % n) / n

# ---- Gram and target via digamma periodicity ----
def gram(m, n):
    L = lcm(m, n)
    acc = mp.mpf(0)
    for r in range(L):
        rm = mp.mpf(r % m) / m
        rn = mp.mpf(r % n) / n
        acc += rm * rn * S_residue_digamma(r, L)
    return acc

def target(n):
    # <1, r_n> = sum_{r=0}^{n-1} (r/n) S_r(n)
    L = n
    acc = mp.mpf(0)
    for r in range(L):
        acc += mp.mpf(r % n) / n * S_residue_digamma(r, L)
    return acc

# ---- solve least squares: E_N* = 1 - b^T G^{-1} b ----
def optimal_error(N):
    idx = list(range(2, N + 1))
    d = len(idx)
    G = mp.matrix(d, d)
    for i in range(d):
        for j in range(d):
            G[i, j] = gram(idx[i], idx[j])
    b = mp.matrix([target(n) for n in idx])
    bT = b.T
    Ginv = G ** (-1)
    # b^T G^{-1} b
    # compute as row(b) * Ginv * col(b)
    mid = bT * Ginv * b  # 1x1 matrix
    quad = mid[0, 0]
    E = mp.mpf(1) - quad
    # coefficients a = G^{-1} b
    a = Ginv * b  # column
    coeffs = [a[i, 0] for i in range(d)]
    return E, coeffs, G, b

def constrained_error(N):
    """Error under fixed coefficients a_n = -mu(n)/n (Baez-Duarte-type family)."""
    idx = list(range(2, N + 1))
    coeffs = [mp.mpf(-mobius(n)) / n for n in idx]
    # ||1 - sum a_n r_n||^2 = 1 - 2 sum a_n b_n + sum a_m a_n G_{mn}
    lin = mp.mpf(0)
    for n, c in zip(idx, coeffs):
        lin += c * target(n)
    quad = mp.mpf(0)
    for i, m in enumerate(idx):
        for j, n in enumerate(idx):
            quad += coeffs[i] * coeffs[j] * gram(m, n)
    return mp.mpf(1) - 2 * lin + quad

# =====================================================================
# CALIBRATION
# =====================================================================
print("=" * 70)
print("CALIBRATION (Instrument Rule #1)")
print("=" * 70)

# (A) verify digamma S_r sums to 1 over a period (identity: sum_{r=0}^{L-1} S_r(L) = sum_k 1/(k(k+1)) = 1)
print("\n[A] Consistency: sum_{r=0}^{L-1} S_r(L) should equal 1 (telescoping <1,1>=1)")
for L in [2, 3, 4, 5, 6, 7, 8, 12, 60, 420]:
    s = sum(S_residue_digamma(r, L) for r in range(L))
    print(f"    L={L:4d}: sum_r S_r = {mp.nstr(s, 55)}")

# (B) digamma vs nsum cross-check for a representative set
print("\n[B] Cross-check S_r: digamma vs mp.nsum (independent algorithms)")
worst = mp.mpf(0)
for L in [2, 3, 4, 5, 6, 7, 8, 12, 60]:
    for r in range(L):
        a = S_residue_digamma(r, L)
        b = S_residue_nsum(r, L)
        diff = abs(a - b)
        if diff > worst:
            worst = diff
print(f"    max |digamma - nsum| over L in {{2..8,12,60}}, all r: {mp.nstr(worst, 20)}")

# (C) N=2 closed form
print("\n[C] N=2 closed form (the stated calibration receipt)")
E2, coeffs2, G2, b2 = optimal_error(2)
ln2 = mp.log(2)
print(f"    computed a_2        = {mp.nstr(coeffs2[0], 55)}   (expected exactly 2)")
print(f"    computed E_2*       = {mp.nstr(E2, 55)}")
print(f"    1 - ln 2 (expected) = {mp.nstr(mp.mpf(1) - ln2, 55)}")
print(f"    |E_2* - (1-ln2)|    = {mp.nstr(abs(E2 - (mp.mpf(1) - ln2)), 20)}")
print(f"    G_22 = {mp.nstr(G2[0,0], 55)}  (expected ln2/4 = {mp.nstr(ln2/4, 55)})")
print(f"    b_2  = {mp.nstr(b2[0,0], 55)}  (expected ln2/2 = {mp.nstr(ln2/2, 55)})")
print(f"    1 - ln 2 (full, 60dps) = {mp.nstr(mp.mpf(1)-ln2, 60)}")

# =====================================================================
# MAIN DATA: E_N* for N = 2..8
# =====================================================================
print("\n" + "=" * 70)
print("DATA: optimal L2(w) error E_N* and optimal coefficients")
print("=" * 70)

results = {}
for N in range(2, 9):
    E, coeffs, G, b = optimal_error(N)
    results[N] = (E, coeffs)
    print(f"\nN = {N}:  E_{N}* = {mp.nstr(E, 55)}")
    print(f"    coefficients a_n (n=2..{N}):")
    for n, c in zip(range(2, N + 1), coeffs):
        print(f"        a_{n} = {mp.nstr(c, 50)}")

# =====================================================================
# SECOND IMPLEMENTATION (Instrument Rule #2): direct residual norm
#   E_N* = || 1 - sum_n a_n r_n ||^2 = sum_{r=0}^{L-1} res(r)^2 * S_r(L)
#   with L = lcm(2..N), res(r) = 1 - sum_n a_n (r mod n)/n,
#   and S_r(L) computed via mp.nsum (independent of the digamma route).
# =====================================================================
print("\n" + "=" * 70)
print("SECOND IMPLEMENTATION: direct residual-norm cross-check (nsum S_r)")
print("=" * 70)

def lcm_range(N):
    L = 1
    for n in range(2, N + 1):
        L = lcm(L, n)
    return L

for N in range(2, 9):
    E_mat, coeffs, G, b = optimal_error(N)   # route 1: matrix inverse (digamma)
    L = lcm_range(N)
    idx = list(range(2, N + 1))
    acc = mp.mpf(0)
    for r in range(L):
        res = mp.mpf(1)
        for n, c in zip(idx, coeffs):
            res -= c * mp.mpf(r % n) / n
        acc += res * res * S_residue_nsum(r, L)   # route 2: nsum S_r
    print(f"    N = {N}: matrix-inverse E = {mp.nstr(E_mat, 50)}")
    print(f"            direct-norm    E = {mp.nstr(acc, 50)}")
    print(f"            |diff|            = {mp.nstr(abs(E_mat - acc), 20)}")

# also verify E = 1 - sum_n a_n b_n identity
print("\n[B2] identity check E_N* = 1 - sum_n a_n b_n (should agree to roundoff)")
for N in range(2, 9):
    E, coeffs, G, b = optimal_error(N)
    s = sum(c * target(n) for n, c in zip(range(2, N + 1), coeffs))
    print(f"    N = {N}: 1 - sum a_n b_n = {mp.nstr(mp.mpf(1) - s, 50)}   |diff| = {mp.nstr(abs((mp.mpf(1)-s) - E), 20)}")

# =====================================================================
# SECONDARY: Baez-Duarte-type constraint a_n = -mu(n)/n
# =====================================================================
print("\n" + "=" * 70)
print("SECONDARY: error under fixed a_n = -mu(n)/n (N=2..8)")
print("=" * 70)
for N in range(2, 9):
    ce = constrained_error(N)
    print(f"    N = {N}: constrained E = {mp.nstr(ce, 55)}  (mu sequence a_n: "
          f"{[mp.nstr(mp.mpf(-mobius(n))/n, 12) for n in range(2, N+1)]})")

# =====================================================================
# SUMMARY TABLE
# =====================================================================
print("\n" + "=" * 70)
print("SUMMARY (50 significant digits)")
print("=" * 70)
print(f"{'N':>2}  {'E_N* (optimal)':>58}")
for N in range(2, 9):
    print(f"{N:>2}  {mp.nstr(results[N][0], 50)}")
