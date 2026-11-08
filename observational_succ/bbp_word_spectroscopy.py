"""Exact spectral-return, cyclotomic and de Bruijn word-flow diagnostics.

This is a source/observer instrument, not a proof of base-16 pi normality.
The data source is supplied by the caller; use the existing certified zero-orbit
BBP digit routine when investigating pi. All stated energies are exact rational.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, factorial, pi, sin, cos
from typing import Sequence

BASE = 16
ORDERS = (2, 4, 8, 16)


def validate_digits(digits: Sequence[int]) -> tuple[int, ...]:
    if not digits or any(type(d) is not int or not 0 <= d < BASE for d in digits):
        raise ValueError("nonempty sequence of base-16 integer digits required")
    return tuple(digits)


def cyclotomic_balances(counts: Sequence[int], order: int) -> tuple[int, ...]:
    """Integer coordinates vanishing iff primitive order-'order' character vanishes."""
    if order not in ORDERS or len(counts) != BASE or any(type(c) is not int or c < 0 for c in counts):
        raise ValueError("order in {2,4,8,16}, nonnegative 16-bin counts required")
    mod = [sum(counts[j] for j in range(r, BASE, order)) for r in range(order)]
    return tuple(mod[r] - mod[r + order // 2] for r in range(order // 2))


def exact_reset_walk(digits: Sequence[int]) -> dict:
    """Count *every* exact spectral zero, including the 1- and 2-D returns."""
    xs = validate_digits(digits)
    balances = {m: [0] * (m // 2) for m in ORDERS}
    hits = {m: [] for m in ORDERS}
    uniform_hits = []
    counts = [0] * BASE
    best = (None, None)  # minimum positive normalized E1 among N >= 16
    for n, x in enumerate(xs, 1):
        counts[x] += 1
        for m in ORDERS:
            r = x % m
            j = r % (m // 2)
            balances[m][j] += 1 if r < m // 2 else -1
            if all(v == 0 for v in balances[m]):
                hits[m].append(n)
        if n % BASE == 0 and all(c == n // BASE for c in counts):
            uniform_hits.append(n)
        if n >= BASE:
            numerator = BASE * sum(c * c for c in counts) - n * n
            assert numerator >= 0
            current = Fraction(numerator, n * n)
            if best[0] is None or current < best[0]:
                best = (current, n)
    return {
        "prefix_length": len(xs),
        "spectral_zeros": {str(m): hits[m] for m in ORDERS},
        "exact_uniform_histogram": uniform_hits,
        "final_balances": {str(m): tuple(balances[m]) for m in ORDERS},
        "minimal_E1_after_16": {"energy": best[0], "at": best[1]},
        "final_counts": counts,
    }


def word_counts_cyclic(digits: Sequence[int], depth: int) -> Counter:
    xs = validate_digits(digits)
    n = len(xs)
    if type(depth) is not int or not 1 <= depth <= n:
        raise ValueError("1<=depth<=sample length")
    return Counter(tuple(xs[(i + j) % n] for j in range(depth)) for i in range(n))


def word_counts_linear(digits: Sequence[int], depth: int) -> Counter:
    xs = validate_digits(digits)
    if type(depth) is not int or not 1 <= depth <= len(xs):
        raise ValueError("1<=depth<=sample length")
    return Counter(tuple(xs[i:i+depth]) for i in range(len(xs)-depth+1))


def de_bruijn_divergence(counts: Counter, depth: int) -> dict:
    """At a vertex v: out-degree count minus in-degree count (boundary for open path)."""
    if type(depth) is not int or depth < 2:
        raise ValueError("de Bruijn edges require depth>=2")
    diff = defaultdict(int)
    for word, c in counts.items():
        if len(word) != depth or type(c) is not int or c < 0:
            raise ValueError("invalid word/count")
        diff[word[:-1]] += c
        diff[word[1:]] -= c
    return {k: v for k, v in diff.items() if v}


def cycle_dimension(depth: int) -> tuple[int, int, int]:
    """(edge count, divergence-free cycle-space dimension, zero-mass dimension)."""
    if type(depth) is not int or depth < 1:
        raise ValueError("depth>=1")
    edges = BASE ** depth
    vertices = BASE ** (depth - 1)
    # Strongly connected de Bruijn digraph: rank incidence = vertices-1.
    return edges, edges - vertices + 1, edges - vertices


def primitive_word_sector(counts: Counter, n: int, depth: int, order: int) -> Fraction:
    """Exact contribution from word Fourier modes with terminal character of order m.

    At depth 1 this is the primitive component of E_1. At depth k>1
    these four sectors partition E_k-E_(k-1), all by integer sum-of-squares.
    """
    if order not in ORDERS or type(depth) is not int or depth < 1 or n <= 0:
        raise ValueError("invalid order, depth or count")
    if sum(counts.values()) != n:
        raise ValueError("word count sum mismatch")
    half = order // 2
    by_context = defaultdict(lambda: [0] * half)
    for word, multiplicity in counts.items():
        if len(word) != depth or any(type(d) is not int or d not in range(BASE) for d in word):
            raise ValueError("word outside alphabet/depth")
        if type(multiplicity) is not int or multiplicity < 0:
            raise ValueError("invalid multiplicity")
        residue = word[-1] % order
        target = residue % half
        by_context[word[:-1]][target] += multiplicity if residue < half else -multiplicity
    total = sum(sum(x * x for x in vector) for vector in by_context.values())
    return Fraction(BASE ** (depth - 1) * half * total, n * n)


def word_energy(counts: Counter, n: int, depth: int) -> Fraction:
    if sum(counts.values()) != n or n < 1 or depth < 1:
        raise ValueError("invalid count")
    return Fraction((BASE ** depth) * sum(c*c for c in counts.values()) - n*n, n*n)


def spectral_refinement(digits: Sequence[int], max_depth: int = 3) -> dict:
    xs = validate_digits(digits)
    if not 1 <= max_depth <= len(xs):
        raise ValueError("1<=max_depth<=length")
    result = {}
    previous = Fraction(0)
    for depth in range(1, max_depth + 1):
        counts = word_counts_cyclic(xs, depth)
        e = word_energy(counts, len(xs), depth)
        sector = {str(m): primitive_word_sector(counts, len(xs), depth, m) for m in ORDERS}
        if sum(sector.values(), Fraction(0)) != e - previous:
            raise AssertionError("cyclotomic Parseval/refinement identity invalid")
        if depth >= 2 and de_bruijn_divergence(counts, depth):
            raise AssertionError("cyclic source word flow has divergence")
        result[str(depth)] = {
            "energy": e, "new_energy": e - previous, "primitive_sectors": sector,
            "independent_zero_mass_cycle_coordinates": cycle_dimension(depth)[-1],
            "iid_reference_energy": Fraction(BASE**depth - 1, len(xs)),
            "iid_reference_new_sector": {str(m): Fraction(BASE**(depth-1) * (m//2),len(xs)) for m in ORDERS},
            "renormalized_energy": len(xs)*e / (BASE**depth-1),
        }
        previous = e
    return result


def iid_exact_balanced_probability(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("n>=1")
    if n % BASE:
        return Fraction(0)
    m = n // BASE
    return Fraction(factorial(n), factorial(m) ** BASE * BASE**n)


def planar_return_probability(even_steps: int) -> Fraction:
    """Uniform digit null, order 4: P(S_(2n)=0)=binom(2n,n)^2/16^n."""
    if type(even_steps) is not int or even_steps < 0 or even_steps % 2:
        raise ValueError("nonnegative even number of steps required")
    n = even_steps // 2
    return Fraction(comb(2*n,n)**2, 16**n)


def circle_digit_fourier_coeff(h: int, t: int) -> complex:
    """Fourier coefficient of exp(2pi i h floor(16x)/16), in L2(T).

    Nonzero only when t = h mod 16. No pointwise convergence at digit
    boundaries is claimed. This is a *digit-step* character, not e(hU_n).
    """
    if type(h) is not int or type(t) is not int:
        raise ValueError("integer frequencies required")
    residue = h % BASE
    if not residue:
        return complex(1 if t == 0 else 0)
    if t % BASE != residue:
        return 0j
    theta = 2*pi * residue / BASE
    # 16(1-exp(-2pi i t/16))/(2pi i t), evaluated with common residue.
    return 16 * (1-complex(cos(theta), -sin(theta))) / (2j*pi*t)


def renormalized_real_energy(energy: Fraction, n: int, depth: int) -> Fraction:
    """N E_k(N)/(16**k-1): has *expectation* one for iid N>=2k."""
    if n <= 0 or depth <= 0:
        raise ValueError("positive horizon and depth")
    return Fraction(n) * energy / (BASE**depth - 1)


def first_nonzero_digit_character(h: Sequence[int]) -> int | None:
    """1-based depth of first nonzero digit frequency; None for constant."""
    if not h or any(type(a) is not int or not 0 <= a < BASE for a in h):
        raise ValueError("nonempty digit-character vector in 0..15")
    return next((j for j,a in enumerate(h,1) if a),None)


def real_fourier_alias_condition(h: Sequence[int], t: int) -> bool:
    """Exact necessary-and-sufficient frequency support of a digit Walsh character.

    For nonconstant h, let j be its first nonzero index. Then the real-circle
    Fourier coefficient is nonzero iff t / 16^(j-1) = h_j (mod 16).
    This is independent of the *later* digit-character coordinates.
    """
    j=first_nonzero_digit_character(h)
    if type(t) is not int:
        raise ValueError("integer circle Fourier frequency required")
    if j is None:
        return t==0
    q=BASE**(j-1)
    return t % q==0 and (t//q) % BASE == h[j-1]


def word_character_circle_fourier_coeff(h: Sequence[int], t: int) -> complex:
    """Exact-form (numerically evaluated) Fourier coefficient of a depth-k
    hexadecimal word character on the real unit circle.

    f_h(x)=exp(2pi i sum_j h_j d_j(x)/16), where d_j are the first k
    base-16 digits of x, as a step function away from boundaries.
    Coefficients live in one arithmetic progression of real frequencies;
    complex results are diagnostic only, while zero/support logic is exact.
    """
    h=tuple(h)
    if not real_fourier_alias_condition(h,t):
        return 0j
    if all(x==0 for x in h):
        return (1+0j) if t==0 else 0j
    from cmath import exp
    period=BASE**len(h)
    interval=(1-exp(-2j*pi*t/period))/(2j*pi*t)
    value=interval
    for j,hj in enumerate(h,1):
        ratio=exp(2j*pi*(hj/BASE - t/(BASE**j)))
        # Avoid unstable 0/0 near ratio=1; only 16 terms.
        value*=sum(ratio**a for a in range(BASE))
    return value


def full_word_reset_horizons(digits: Sequence[int], depth: int) -> list[int]:
    """Find *every possible* exact E_k=0 time in the supplied finite prefix.

    Uniform k-word counts require 16^k|N. Evaluating only those N is
    complete for the exact-zero question, but says nothing about near-zeros.
    """
    xs=validate_digits(digits)
    if type(depth) is not int or depth<1:
        raise ValueError("depth>=1")
    b=BASE**depth
    hits=[]
    for n in range(b,len(xs)+1,b):
        c=word_counts_cyclic(xs[:n],depth)
        if len(c)==b and all(v==n//b for v in c.values()):
            hits.append(n)
    return hits
