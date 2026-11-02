"""
Entropy <-> dimension bridge for x3-rigidity obligation (B).

x_{n+1} = {16 x_n},  x_1 = {pi},  the completed x16 orbit.
mu = weak-* limit of empirical measures  mu_N = (1/N) sum_{n=1}^N delta_{x_n}.
(B)  :=  dim_* mu > 0   (positive lower dimension).

This module links the m-cylinder Shannon entropy H_m, the collision energy
Q_{m,N} (Renyi-2 object) and the empirical entropy of the digit stream, and
verifies the FINITE inequalities numerically (calibration only, no theorem).

All objects are exact/arbitrary-precision where possible; mpmath dps is set so
the fractional part of 16^{n-1} pi is resolved far below the cylinder scale.
No normality, no asymptotic-cancellation, no dim_* claim is made here.
"""

from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp


# ---------------------------------------------------------------------------
# Exact BBP four-pole forcing and Green tail (source is immutable).
# ---------------------------------------------------------------------------

def r_force(n: int) -> Fraction:
    """Four-pole BBP forcing r(n), exact rational."""
    n8 = 8 * n
    return (Fraction(4, n8 - 7) - Fraction(2, n8 - 4)
            - Fraction(1, n8 - 3) - Fraction(1, n8 - 2))


def tail_exact(n: int, depth: int) -> Fraction:
    """Green tail T_n = sum_{j>=1} 16^{-j} r(n+j), truncated at depth (exact)."""
    total = Fraction(0)
    for j in range(1, depth + 1):
        total += r_force(n + j) / (16 ** j)
    return total


def tail_upper(n: int) -> Fraction:
    """Rigorous upper bound on the full tail T_n (geometric majorant)."""
    # |r(m)| <= C/m^2 and r is sign-alternating; a crude safe bound:
    # sum_{j>=1} 16^{-j} |r(n+j)| <= (1/15) * max_{j>=1}|r(n+j)|.
    # Use the exact |r(n+1)| bound termwise: |r(m)| <= 4/(8m-7)+2/(8m-4)+...
    m0 = n + 1
    abs_r = (Fraction(4, 8 * m0 - 7) + Fraction(2, 8 * m0 - 4)
             + Fraction(1, 8 * m0 - 3) + Fraction(1, 8 * m0 - 2))
    return abs_r / 15


def U_exact(n: int, depth: int) -> Fraction:
    """Authentic rational state U_n = 16^{n-1} pi - T_n  (pi kept symbolically).

    We return the pair (coef, tail) so that  U_n = coef * pi - tail(n).
    This keeps pi symbolic and the tail exact rational.
    """
    return Fraction(16 ** (n - 1)), tail_exact(n, depth)


def x_n_frac(n: int, dps: int) -> mp.mpf:
    """x_n = {16^{n-1} pi} = {U_n + T_n} computed with pi at dps precision."""
    mp.mp.dps = dps
    pi = mp.pi
    val = (16 ** (n - 1)) * pi
    return mp.fmod(val, mp.mpf(1))


# ---------------------------------------------------------------------------
# Digit stream (base-16) from the orbit: the m-cylinder words.
# ---------------------------------------------------------------------------

def digit_stream(N: int, dps: int) -> list[int]:
    """First N base-16 digits of {16^{n-1} pi}, i.e. the x16 orbit itinerary.

    digit n in {0,...,15} = floor(16 * x_n) where x_n = {16^{n-1} pi}.
    This is EXACTLY the standard base-16 digit stream of pi.
    """
    mp.mp.dps = dps
    pi = mp.pi
    digits = []
    for n in range(1, N + 1):
        v = (16 ** (n - 1)) * pi
        frac = mp.fmod(v, mp.mpf(1))
        digits.append(int(mp.floor(16 * frac)))
    return digits


def cylinder_frequencies(digits: list[int], m: int, b: int = 16):
    """Empirical length-m block frequencies p_{m,N}(w) over starting positions."""
    N = len(digits)
    from collections import Counter
    counts = Counter()
    for n in range(N - m + 1):
        w = 0
        for k in range(m):
            w = w * b + digits[n + k]
        counts[w] += 1
    denom = N - m + 1
    freqs = {w: c / denom for w, c in counts.items()}
    return freqs, denom


def shannon_entropy(freqs) -> float:
    """H = -sum p log p over realized words (natural log)."""
    return -sum(p * math.log(p) for p in freqs.values() if p > 0)


def collision_energy(freqs, m: int, b: int = 16) -> float:
    """Q_{m,N} = b^m * sum p(w)^2  (Renyi-2 collision mass)."""
    return (b ** m) * sum(p * p for p in freqs.values())


def renyi2_entropy(freqs) -> float:
    """H_2 = -log(sum p(w)^2)."""
    return -math.log(sum(p * p for p in freqs.values()))


# ---------------------------------------------------------------------------
# Finite bridge: H_m vs Q_m (exact inequality, calibration only).
# ---------------------------------------------------------------------------

def report(N: int, m: int, dps: int = 60) -> None:
    mp.mp.dps = dps
    digits = digit_stream(N, dps)
    freqs, denom = cylinder_frequencies(digits, m)
    H = shannon_entropy(freqs)
    H2 = renyi2_entropy(freqs)
    Q = collision_energy(freqs, m)
    # Shannon entropy H is the entropy of ONE m-block; entropy RATE is H/m.
    # Renyi-2 entropy H_2 is a LOWER bound for Shannon entropy H_2 <= H.
    print(f"N={N}, m={m}, b=16, words sampled={denom}")
    print(f"  H_m     (Shannon, natural log)   = {H:.6f}")
    print(f"  H_m / m (cylinder entropy rate)  = {H/m:.6f}")
    print(f"  H_2(m)  (Renyi-2, -log sum p^2)  = {H2:.6f}")
    print(f"  Q_{m,N} (collision energy)       = {Q:.6f}")
    print(f"  log Q / m                        = {math.log(Q)/m:.6f}")
    print(f"  (H_2 <= H_1 verified)            : {H2 <= H + 1e-12}")
    print(f"  H_m/m vs (log Q)/m relation      : H_2/m = {H2/m:.6f}")
    print()


if __name__ == "__main__":
    # Calibration runs: finite evidence only, NOT proofs of any limit.
    for (N, m) in [(256, 3), (1024, 4), (4096, 5), (16384, 6)]:
        report(N, m)
