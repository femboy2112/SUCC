"""Correct-precision finite diagnostic for the Prime–Cofactor Non-Conspiracy Conjecture.

Computes M/T = sum_p |R_p(h)|^2 / sum_p |W_p|^2 for primes p<=X, p=5 mod 8,
where R_p(h) = sum_{n=a_p}^{b_p} e(h U_n) is the authentic-orbit Weyl sum over the
prime window [a_p, b_p] = [(p+3)/8, (p+1)/2).

CRITICAL PRECISION RULE: the phase e(h U_n) needs the exact rational U_n to ~exp(6n)
precision. Two independent methods:
  (1) exact Fraction U_n (mp.dps >= 800 for n<=250);
  (2) digit-orbit y_n = {16 y_{n-1}} from y_1={pi} (mp.dps >= 0.6 * X).

A "coherence" result M/T -> 1 is ALWAYS a precision bug (insufficient digits).

No normality claim. Diagnostic only.
"""
from fractions import Fraction
from mpmath import mp, mpf, pi, fmod, cos, sin
import sympy as sp


def r_frac(n):
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def U_exact(n):
    u = Fraction(0)
    for j in range(1, n+1):
        u = 16*u + r_frac(j)
    return u


def method_exact(X, h, dps=800):
    """Exact Fraction U_n; accurate but slow for large X."""
    mp.dps = dps
    M = 0.0
    Ttr = 0.0
    for p in range(5, X+1):
        if p % 8 != 5 or not sp.isprime(p):
            continue
        a = (p+3)//8
        b = (p+1)//2
        sx = 0.0
        sy = 0.0
        for n in range(a, b):
            Un = U_exact(n)
            ph = fmod(h * mpf(Un.numerator)/mpf(Un.denominator), 1)
            th = 2*mp.pi*ph
            sx += cos(th)
            sy += sin(th)
        M += float(sx*sx + sy*sy)
        Ttr += float((b-a)**2)
    return M/Ttr


def method_digit(X, h, dps):
    """Digit orbit y_n = {16^{n-1} pi}; fast, needs dps >= 0.6*X."""
    mp.dps = dps
    P = mp.pi
    Nmax = X//2 + 2
    y = [None]*(Nmax+1)
    y[1] = fmod(P, 1)
    for n in range(2, Nmax+1):
        y[n] = fmod(16*y[n-1], 1)
    # tiny Green tail T_n (float suffices; T_n < (8n+1)^{-2})
    Tarr = [0.0]*(Nmax+1)
    for n in range(1, Nmax+1):
        s = 0.0
        pw = 16.0
        for j in range(1, 31):
            s += r_frac(n+j) / pw
            pw *= 16.0
        Tarr[n] = float(s)
    M = 0.0
    Ttr = 0.0
    for p in range(5, X+1):
        if p % 8 != 5 or not sp.isprime(p):
            continue
        a = (p+3)//8
        b = (p+1)//2
        sx = 0.0
        sy = 0.0
        for n in range(a, b):
            ph = fmod(h*(y[n] - Tarr[n]), 1)
            th = 2*mp.pi*ph
            sx += cos(th)
            sy += sin(th)
        M += float(sx*sx + sy*sy)
        Ttr += float((b-a)**2)
    return M/Ttr


def main():
    print("Exact-Fraction method (mp.dps=800):")
    for X in [200, 500]:
        print(f"  X={X}: M/T = {method_exact(X, 1):.5f}")
    print("Digit-orbit method (mp.dps >= 0.6*X):")
    for X, dps in [(1000, 900), (2000, 1600)]:
        print(f"  X={X}: M/T = {method_digit(X, 1, dps):.5f}")
    print("\n(Values should be small and decreasing. M/T -> 1 is a precision bug.)")


if __name__ == "__main__":
    main()
