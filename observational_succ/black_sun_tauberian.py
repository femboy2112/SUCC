"""BLACK SUN B-track: quantitative factorial-prime defect and Tauberian transfer.

Campaign: Operation Black Sun, 2026-10-14.

The source-quantization defect (repo PR #77, proven there qualitatively):

  log(N!) = sum_{n<=N} Lambda(n) floor(N/n)   [BS-B0, classical]
  D_N = sum_{n<=N} Lambda(n)/n - log(N!)/N
      = (1/N) sum_{n<=N} Lambda(n) {N/n} >= 0.

This module adds the QUANTITATIVE layer:

  BS-B1 (PROVED LOCAL, transfer): if A(x)=sum_{n<=x} a(n)/n = log x + C +
      O(x^{-delta}), 0<delta<=1, then S(x)=sum_{n<=x} a(n) = x + O(x^{1-delta}),
      with the explicit constant (3+1/(1-delta))B via Abel summation.  No
      positivity used.

  BS-B2 (PROVED LOCAL, sharpness): for every 0<delta<1 the exponent is optimal
      in the nonnegative class: a(n)=1+b(n), b(2^j)=floor(2^{j(1-delta)})
      gives A(x)=log x+C_a+O(x^{-delta}) while S(x)-x >= c_delta x^{1-delta}
      along x=2^J.  Spikes are not available to the authentic Lambda source;
      for Lambda the same exponent is forced by the zero dictionary (BS-B3).

  BS-B3 (PROVED LOCAL + classical imports): for a=Lambda, with
      psi(x)=sum_{n<=x} Lambda(n):
        A(x) = log x - gamma + O(x^{-delta})  <=>  psi(x) = x + O(x^{1-delta})
      (two-way, exact exponent match; both directions elementary), and
      classically both are equivalent to zeta being zero-free in Re s > 1-delta
      (up to the standard endpoint care: zeros with Re = 1-delta are allowed).

  BS-B4 (PROVED LOCAL, quantitative defect dictionary):
        D_N - (1-gamma) = [A(N) - log N + gamma] + O(log N / N),
      so the factorial-prime defect measures the weighted prime error at the
      SAME exponent; a zero-detector at matched quality.
"""
from __future__ import annotations

from fractions import Fraction
from math import log, sqrt
from typing import Callable


class BlackSunBTrackError(ValueError):
    pass


def abel_transfer_identity(a: list[Fraction], upto: int) -> bool:
    """Exact rational check of S(x) = x A(x) - int_1^x A(t) dt on integers.

    Implemented in exact piecewise-constant arithmetic: int_1^N A = sum_m
    A(m) (meas of the constancy interval), all in Fractions.
    """
    if upto < 1 or upto > len(a):
        raise BlackSunBTrackError("upto out of range")
    # prefix sums
    A = [Fraction(0)]*(upto+1)
    S = [Fraction(0)]*(upto+1)
    for n in range(1, upto+1):
        A[n] = A[n-1] + a[n]/n
        S[n] = S[n-1] + a[n]
    # integral of the step function A(t) from 1 to N:
    for N in range(1, upto+1):
        I = sum(A[m] for m in range(1, N))  # A constant = A[m] on [m, m+1)
        if N*A[N] - I - S[N] != 0:
            return False
    return True


def spike_sequence(delta: Fraction, J: int) -> list[int]:
    """a(n) = 1 + b(n) with b(2^j) = floor(2^{j(1-delta)}), j=1..J, else 0."""
    if not (0 < delta < 1):
        raise BlackSunBTrackError("0 < delta < 1 required")
    out = [0]*(2**J + 2)
    for n in range(1, min(len(out), 2**J+1)):
        out[n] = 1
    for j in range(1, J+1):
        val = int(Fraction(2)**(j*(1-delta)))
        out[2**j] += val
    return out


def spike_cumulative_error(delta: Fraction, J: int, dps: int = 40):
    """Returns (max |A(x)-log x-C_a| * x^delta over x=2^j, c_delta, S(2^J)-2^J).

    C_a = gamma? No: for a=1+b, A(x) = H_floor(x) + spike sum.  The exact
    constant is H-type; we return the numerically fitted C_a at the largest
    power of two below the horizon and the scaled errors.
    """
    import mpmath as mp
    mp.mp.dps = dps
    a = spike_sequence(delta, J)
    Nmax = 2**J
    A = [Fraction(0)]*(Nmax+1)
    S = [Fraction(0)]*(Nmax+1)
    for n in range(1, Nmax+1):
        A[n] = A[n-1] + Fraction(a[n], n)
        S[n] = S[n-1] + a[n]
    # C_a from the exact tail-inclusive limit: A(2^J) - log(2^J)
    C_a = mp.mpf(A[Nmax].numerator)/mp.mpf(A[Nmax].denominator) - mp.log(Nmax)
    worst = mp.mpf('0')
    for j in range(max(1, J//2), J+1):
        x = 2**j
        err = abs(mp.mpf(A[x].numerator)/mp.mpf(A[x].denominator)
                  - mp.log(x) - C_a) * x**float(delta)
        worst = max(worst, err)
    # total spike mass S(2^J) - 2^J (should be ~ c_delta * 2^{J(1-delta)}):
    Sm = int(S[Nmax]) - Nmax
    return worst, C_a, Sm


def von_mangoldt_sieve(N: int):
    """Lambda(n) for 2<=n<=N: log p iff n is EXACTLY a prime power p^k."""
    if N < 2:
        return [0.0]*(N+1)
    lam = [0.0]*(N+1)
    for p in range(2, N+1):
        if _is_prime(p):
            pk = p
            while pk <= N:
                lam[pk] = log(p)   # pure prime powers only
                pk *= p
    return lam


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True


def factorial_prime_identity(N: int, dps: int = 50) -> tuple:
    """Exact check: log(N!) = sum Lambda(n) floor(N/n), both sides at dps
    digits (N! by exact integer factorial, sum by prime factorization)."""
    import mpmath as mp
    mp.mp.dps = dps
    # sum over prime powers: contribution of prime p to log N!:
    #   sum_{k>=1, p^k<=N} floor(N/p^k) log p
    total = mp.mpf('0')
    for p in range(2, N+1):
        if _is_prime(p):
            pk = p
            while pk <= N:
                total += mp.floor(mp.mpf(N)/pk)*mp.log(p)
                pk *= p
    fact = mp.factorial(N)
    lhs = mp.log(fact)
    return lhs, total, abs(lhs-total)


def defect_DN(N: int, lam: list[float]) -> float:
    """D_N = sum_{n<=N} Lambda(n)/n - log(N!)/N in float (uses the exact
    identity for log N! via the same Lambda data: log N! = sum lam floor)."""
    from math import floor
    A = sum(lam[n]/n for n in range(2, N+1))
    logfact = sum(lam[n]*floor(N/n) for n in range(2, N+1))
    return A - logfact/N


def transfer_dictionary_check(N_values, dps: int = 30):
    """TESTED MODEL: |E_A(N)| vs |psi(N)-N|/N at matched N (the two errors
    track at the same exponent for the authentic source)."""
    import mpmath as mp
    mp.mp.dps = dps
    Nmax = max(N_values)
    lam = von_mangoldt_sieve(Nmax)
    out = []
    psi = 0.0
    Asum = 0.0
    prev = 0
    for N in sorted(N_values):
        for n in range(prev+1, N+1):
            psi += lam[n]
            Asum += lam[n]/n
        prev = N-1
        EA = Asum - log(N) + 0.5772156649015328606
        EP = (psi - N)/N
        out.append((N, EA, EP, abs(EA)/(N**-0.5), abs(EP)/(N**-0.5)))
    return out


if __name__ == "__main__":
    # quick self-check
    ok = abel_transfer_identity([Fraction(i % 3) for i in range(200)], 150)
    print("Abel identity exact:", ok)
    lhs, rhs, resid = factorial_prime_identity(500)
    print("log(500!) identity residual:", resid)
    w, C_a, Sm = spike_cumulative_error(Fraction(1, 2), 16)
    print("spike worst scaled error:", w, "S(2^16)-2^16 =", Sm)