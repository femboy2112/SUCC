"""BLACK SUN II C-crossover: the Goldbach Fourier dichotomy and the binary
mean dictionary.

Campaign round 2, 2026-10-14. RH PROVED: NO. No zero positions used.

Objects:
  F_N(theta) = sum_{n=1}^{N-1} Lambda(n) e^{i n theta}   (windowed source sum)

  BS-G1 (PROVED LOCAL, the |F|^2 trap): the sum-diagonal and difference-
      diagonal pairings are EXACTLY dichotomous:
        (1/2pi) int F_N^2 e^{-iN theta} dtheta = sum_{n+m=N} Lambda(n)Lambda(m)
                                               =: R_Lambda(N)   (sum diagonal)
        (1/2pi) int |F_N|^2 e^{-iN theta} dtheta = 0   (difference diagonal)
      The second is identically ZERO: |F_N|^2 = sum Lambda(n)Lambda(m)
      e^{i(n-m)theta} and n - m = N has no solution with 1 <= n, m <= N-1.
      Any "positive-definite correlation" route to Goldbach through |F_N|^2
      is structurally void for the sum problem; the difference problem is
      the autocorrelation Fourier coefficient object instead.

  BS-G2 (PROVED LOCAL, hyperbola identity): mean_G(X) :=
      sum_{N<=X} R_Lambda(N) = sum_{n+m<=X} Lambda(n)Lambda(m)
      = sum_{n<=X-2} Lambda(n) psi(X-n)  exactly.

  BS-G3 (classical imports + TESTED MODEL; CORRECTED 2026-10-20): mean_G(X) =
      X^2/2 + error, with the error governed by the nontrivial zeros rho. The
      mechanism is the EXPLICIT FORMULA for psi inserted into the EXACT additive
      identity BS-G2: mean_G(X) = sum_{n<=X-2} Lambda(n) psi(X-n); writing
      psi(x) = x - sum_rho x^rho/rho - ... turns each zero into an error
      contribution, while the main term x yields X^2/2 (1+o(1)) with error
      O(X^{1+beta+eps}) set by the zero-free half-width (EXTERNAL CLASSICAL:
      Landau/Perron via the explicit formula). Numerics corroborate the X^{3/2}
      heuristic scale under RH.

      FIREWALL (additive vs multiplicative convolution). An EARLIER phrasing of
      this note -- "the Dirichlet series of R_Lambda is (zeta'/zeta)^2-type" --
      was MISLEADING (false as literally stated). R_Lambda(N) = (Lambda *+
      Lambda)(N) is the ADDITIVE convolution; its ordinary Dirichlet series has
      NO (zeta'/zeta)^2 closed form. (-zeta'/zeta)^2 is instead the Dirichlet
      series of the MULTIPLICATIVE convolution (Lambda *x Lambda)(N) =
      sum_{ab=N} Lambda(a)Lambda(b). The two differ; the smallest exact witness
      is N=5: R_Lambda(5) = (Lambda *+ Lambda)(5) = 2 log2 log3, whereas
      (Lambda *x Lambda)(5) = [5^-s](-zeta'/zeta)^2 = 0. The conclusion (X^2/2
      main term, zero-governed error) stands, but via the additive
      explicit-formula route above, NOT via any Dirichlet series of R_Lambda.
      Executable receipt: observational_succ.arithmetic_interactions
      .illegal_interchange_witness (returns N=5).

  BS-G4 (PROVED LOCAL, exact bookkeeping): R_Lambda(N) decomposes exactly
      into true-prime-pair mass and prime-power contamination:
        R_Lambda(N) = sum_{p+q=N, p,q prime} log p log q
                    + sum_{mixed prime-power terms},
      with the contamination list exact for the probed range.
"""
from __future__ import annotations

from math import log
from typing import Callable


class BlackSunGoldbachError(ValueError):
    pass


def von_mangoldt_sieve(N: int):
    """Lambda(n) for 2<=n<=N (log p iff n = p^k exactly)."""
    if N < 2:
        return [0.0]*(N+1)
    lam = [0.0]*(N+1)
    for p in range(2, N+1):
        if _is_prime(p):
            pk = p
            while pk <= N:
                lam[pk] = log(p)
                pk *= p
    return lam


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True


def prime_indicator_sieve(N: int):
    ind = [0.0]*(N+1)
    for p in range(2, N+1):
        if _is_prime(p):
            ind[p] = 1.0
    return ind


def R_Lambda(N: int, lam) -> float:
    """R_Lambda(N) = sum_{n=2}^{N-2} Lambda(n) Lambda(N-n)."""
    if N < 4:
        return 0.0
    return sum(lam[n]*lam[N-n] for n in range(2, N-1))


def F_N(N: int, theta, lam) -> complex:
    return sum(lam[n]*(complex(theta)**0 if False else
                      __import__('cmath').exp(1j*n*theta))
               for n in range(1, N))


def fourier_dichotomy_check(N: int, ngrid: int = 4096):
    """Numerically verify the BS-G1 dichotomy on a theta-grid.

    Returns (c_sum, c_diff): the e^{-iN theta}-coefficient of F_N^2 (should
    be R_Lambda(N) up to grid resolution) and of |F_N|^2 (should be ~0).
    """
    import numpy as np
    lam = von_mangoldt_sieve(N)
    # F_N on the grid: c_k = (1/M) sum_j F(theta_j)^2 e^{-iN theta_j}
    thetas = 2*np.pi*np.arange(ngrid)/ngrid
    F = np.array([sum(lam[n]*np.exp(1j*n*t) for n in range(1, N))
                  for t in thetas])
    w = np.exp(-1j*N*thetas)
    c_sum = np.mean(F**2*w)
    c_diff = np.mean((np.abs(F)**2)*w)
    return c_sum, c_diff, R_Lambda(N, lam)


def hyperbola_identity(X: int, lam=None, lam2=None):
    """Exact check: sum_{N<=X} R_Lambda(N) == sum_{n<=X-2} Lambda(n) psi(X-n)."""
    if lam is None:
        lam = von_mangoldt_sieve(X)
    psi = [0.0]*(X+1)
    for n in range(2, X+1):
        psi[n] = psi[n-1]+lam[n]
    lhs = sum(R_Lambda(N, lam) for N in range(4, X+1))
    rhs = sum(lam[n]*psi[X-n] for n in range(2, X-1))
    return lhs, rhs


def mean_G_track(X_list):
    """mean_G(X) - X^2/2 vs X^{3/2}: TESTED MODEL corroboration of the
    dictionary's matched-exponent claim (RH heuristic scale)."""
    Xmax = max(X_list)
    lam = von_mangoldt_sieve(Xmax)
    out = []
    run = 0.0
    prev = 4
    for X in sorted(X_list):
        for N in range(prev+1, X+1):
            run += R_Lambda(N, lam)
        prev = X
        err = run - X*X/2
        out.append((X, err, X**1.5))
    return out


def prime_power_decomposition(N: int):
    """Exact: R_Lambda(N) split into (pure-prime-pairs, prime-power-contam).

    Returns (r_pp, r_mix, n_pairs): the pure 2-prime mass, the mixed mass,
    and the count of true prime pairs (p, q), p+q=N, p <= q.
    """
    lam = von_mangoldt_sieve(N)
    ind = prime_indicator_sieve(N)
    r_pp = 0.0
    r_mix = 0.0
    n_pairs = 0
    for n in range(2, N-1):
        m = N-n
        w = lam[n]*lam[m]
        if w == 0:
            continue
        if ind[n] and ind[m]:
            r_pp += w
            if n <= m:
                n_pairs += 1
        else:
            r_mix += w
    return r_pp, r_mix, n_pairs


if __name__ == "__main__":
    import numpy as np
    print("=== BS-G1: Fourier dichotomy (N=30) ===")
    c_sum, c_diff, r = fourier_dichotomy_check(30)
    print(f"  e^{{-iN theta}}-coeff of F^2:     {c_sum.real:+.6f} (target {r:.6f})")
    print(f"  e^{{-iN theta}}-coeff of |F|^2:    {c_diff.real:+.2e} (target 0)")
    print("=== BS-G2: hyperbola identity (X=400) ===")
    lhs, rhs = hyperbola_identity(400)
    print(f"  lhs={lhs:.4f} rhs={rhs:.4f} |diff|={abs(lhs-rhs):.2e}")
    print("=== BS-G3: mean_G tracking ===")
    for (X, err, scale) in mean_G_track([500, 1000, 3000]):
        print(f"  X={X}: mean_G - X^2/2 = {err:+.1f}  (X^1.5 = {scale:.0f})")
    print("=== BS-G4: prime-power decomposition (N=20..40, even) ===")
    for N in (20, 22, 24, 30, 36, 40):
        r_pp, r_mix, pairs = prime_power_decomposition(N)
        print(f"  N={N}: pure-prime mass {r_pp:.3f}, mixed {r_mix:.3f}, pairs={pairs}")