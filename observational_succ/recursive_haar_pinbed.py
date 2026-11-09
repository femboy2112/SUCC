"""One-digit conditional Haar recursion for the source-anchored BBP circle.

General deterministic theorem (no claim of BBP normality):
- T*x = {16 x}; B_a*y = (a+y)/16; C = average_a B_a*;
- Q = C T* = average_{a=0..15} (x -> x+a/16 mod1)*;
- for interval 1-Wasserstein: d(mu,Haar) <= (16 d(mu,Qmu)+d(mu,T*mu))/15.
Both coefficients are sharp. Qmu=mu and T*mu=mu together force Haar.

All finite distributions are checked with exact fractions. The circle is
represented as [0,1) for interval W1; DO NOT confuse interval distance with
shortest circular arc distance. Only counting identities and diagnostic code.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from typing import Sequence

B = 16
Law = tuple[tuple[Q, Q], ...]


def _check_law(law: Law) -> None:
    if not law:
        raise ValueError("a law needs at least one atom")
    if sum((w for _, w in law), Q()) != 1:
        raise ValueError("mass must equal one")
    if any(not isinstance(x, Q) or not isinstance(w, Q)
           or not (0 <= x < 1) or w < 0 for x, w in law):
        raise ValueError("exact rational circle coordinates and masses required")


def canonical_law(points: Sequence[Q]) -> Law:
    if not points:
        raise ValueError("cannot form a law of an empty sample")
    counts = Counter(points)
    n = len(points)
    law = tuple(sorted(((x, Q(c, n)) for x, c in counts.items())))
    _check_law(law)
    return law


def normalized_atoms(items: Sequence[tuple[Q, Q]]) -> Law:
    counts: dict[Q, Q] = {}
    for x, w in items:
        if not isinstance(x, Q) or not isinstance(w, Q):
            raise TypeError("Fraction atoms and masses required")
        counts[x] = counts.get(x, Q()) + w
    law = tuple(sorted((x, w) for x, w in counts.items() if w))
    _check_law(law)
    return law


def shift_law(law: Law) -> Law:
    _check_law(law)
    return normalized_atoms([((B*x) % 1, w) for x, w in law])


def uniform_inverse_law(law: Law) -> Law:
    """Cmu: choose a *new* uniform leading digit and retain tail y~mu."""
    _check_law(law)
    return normalized_atoms([((Q(a)+y)/B, w/B)
                             for y, w in law for a in range(B)])


def digit_averaging_law(law: Law) -> Law:
    """Qmu = (1/16)sum translate_{a/16} mu = C T* mu exactly."""
    _check_law(law)
    return normalized_atoms([((x+Q(a, B)) % 1, w/B)
                             for x, w in law for a in range(B)])


def interval_w1(left: Law, right: Law) -> Q:
    """Exact interval Wasserstein-1 between rational atomic probability laws."""
    _check_law(left)
    _check_law(right)
    jumps: dict[Q, Q] = {}
    for x, m in left:
        jumps[x] = jumps.get(x, Q()) + m
    for x, m in right:
        jumps[x] = jumps.get(x, Q()) - m
    prev, delta, area = Q(), Q(), Q()
    for x in sorted(jumps):
        area += (x-prev)*abs(delta)
        delta += jumps[x]
        prev = x
    if delta != 0:
        raise AssertionError("total probability mismatch")
    return area


def _abs_linear_integral(cdf: Q, left: Q, right: Q) -> Q:
    """Exact integral of |cdf - t| over an interval."""
    if not (0 <= left <= right <= 1):
        raise ValueError("interval outside the unit cell")
    if cdf <= left:
        return (right*right-left*left)/2 - cdf*(right-left)
    if cdf >= right:
        return cdf*(right-left) - (right*right-left*left)/2
    return ((cdf-left)**2 + (right-cdf)**2)/2


def interval_w1_haar(law: Law) -> Q:
    """Exact W1 distance to Lebesgue(Haar), integrating |CDF_mu(t)-t|."""
    _check_law(law)
    cdf, left, area = Q(), Q(), Q()
    for x, m in law:
        area += _abs_linear_integral(cdf, left, x)
        cdf += m
        left = x
    area += _abs_linear_integral(cdf, left, Q(1))
    return area


def sharp_recursive_haar_certificate(law: Law) -> dict[str, Q]:
    """Deterministic sharp theorem, *not* a certificate of pi normality."""
    _check_law(law)
    symmetry = interval_w1(law, digit_averaging_law(law))
    stationarity = interval_w1(law, shift_law(law))
    actual = interval_w1_haar(law)
    bound = (B*symmetry+stationarity)/(B-1)
    if actual > bound:
        raise AssertionError("recursive Haar inequality violated")
    return {"symmetry_defect": symmetry,
            "stationarity_defect": stationarity,
            "distance_to_haar": actual,
            "rigidity_upper_bound": bound}


def word_counts_cyclic(digits: Sequence[int], depth: int) -> Counter[int]:
    if not digits or not (0 <= depth <= len(digits)) or type(depth) is not int:
        raise ValueError("nonempty digit list, 0<=depth<=N")
    if any(type(d) is not int or not 0 <= d < B for d in digits):
        raise ValueError("hexadecimal digits required")
    if depth == 0:
        return Counter({0: len(digits)})
    n = len(digits)
    counts: Counter[int] = Counter()
    for i in range(n):
        key = 0
        for j in range(depth):
            key = B*key + digits[(i+j)%n]
        counts[key] += 1
    return counts


def conditional_first_digit_defect(digits: Sequence[int], tail_depth: int) -> Q:
    """Exact L1(mu_[first digit, next j] - Haar16 x mu_[next j]).

    Cyclic observation ensures the original tail-j marginal equals the
    current prefix-j marginal; for a real, noncyclic prefix pay endpoints.
    """
    n = len(digits)
    if type(tail_depth) is not int or tail_depth < 0 or tail_depth+1 > n:
        raise ValueError("0 <= tail_depth < N required")
    low = word_counts_cyclic(digits, tail_depth)
    high = word_counts_cyclic(digits, tail_depth+1)
    base = B**tail_depth
    discrepancy = sum(abs(B*high.get(a*base+w, 0)-c)
                      for w, c in low.items() for a in range(B))
    return Q(discrepancy, B*n)


def word_l1_uniform(digits: Sequence[int], depth: int) -> Q:
    n = len(digits)
    if type(depth) is not int or not 1 <= depth <= n:
        raise ValueError("1<=depth<=N required")
    counts = word_counts_cyclic(digits, depth)
    symbols = B**depth
    # Explicitly include the 16^depth - support missing words.
    amount = sum(abs(symbols*v-n) for v in counts.values())
    amount += (symbols-len(counts))*n
    return Q(amount, n*symbols)


def word_energy(digits: Sequence[int], depth: int) -> Q:
    n = len(digits)
    c = word_counts_cyclic(digits, depth)
    return Q(B**depth * sum(v*v for v in c.values())-n*n, n*n)


def recursive_cylinder_certificate(digits: Sequence[int], depth: int) -> dict:
    """Both exact recursion and Fourier/Parseval bound, no stochastic premise."""
    if not 1 <= depth <= len(digits):
        raise ValueError("1<=depth<=N")
    defect = [conditional_first_digit_defect(digits, j) for j in range(depth)]
    marginal_l1 = word_l1_uniform(digits, depth)
    if marginal_l1 > sum(defect, Q()):
        raise AssertionError("conditional Haar recursion failed")
    if any(defect[j]>defect[j+1] for j in range(depth-1)):
        raise AssertionError("future-conditioning defect unexpectedly decreased")
    last_flux = word_energy(digits, depth)-word_energy(digits, depth-1)
    if defect[-1]**2 > last_flux:
        raise AssertionError("Cauchy/Parseval energy bound failed")
    return {"defects": tuple(defect), "word_l1": marginal_l1,
            "sum_defect_upper": sum(defect,Q()),
            "single_deep_defect_upper": depth*defect[-1],
            "new_coordinate_energy": last_flux}


def periodic_completed_point(word: Sequence[int]) -> Q:
    """A rational point with the exactly repeating specified hexadecimal word."""
    if not word or any(type(d) is not int or not 0 <= d < B for d in word):
        raise ValueError("nonempty hexadecimal word")
    a = 0
    for digit in word:
        a = B*a+digit
    return Q(a, B**len(word)-1)


def periodic_orbit_law(word: Sequence[int]) -> Law:
    x = periodic_completed_point(word)
    phases = []
    for _ in word:
        phases.append(x)
        x = (B*x)%1
    return canonical_law(phases)


def grouped_bbp_forcing(block: int, digits_per_block: int) -> Q:
    """One authentic radix-16^g injection equals g consecutive 4-pole steps.

    No new forcing/seed is invented. Source-specific but not statistical.
    """
    if (type(block) is not int or block < 1 or type(digits_per_block) is not int
            or digits_per_block < 1):
        raise ValueError("positive integer block and group size required")
    from .duck_bbp import forcing
    g = digits_per_block
    return sum((B**(g-j) * forcing(g*(block-1)+j)
                for j in range(1,g+1)),Q())


def grouped_bbp_orbit(blocks: int, digits_per_block: int) -> tuple[Q, ...]:
    """Literal zero-seeded grouped states U_0,U_g,...,U_{g*blocks}."""
    if type(blocks) is not int or blocks < 0:
        raise ValueError("nonnegative integer blocks required")
    if type(digits_per_block) is not int or digits_per_block < 1:
        raise ValueError("positive integer block size required")
    states = [Q()]
    for k in range(1,blocks+1):
        states.append(B**digits_per_block*states[-1]
                      +grouped_bbp_forcing(k,digits_per_block))
    return tuple(states)
