"""Exact finite boundary filters for a zero-grade arithmetic sector.

The verifier proves a conditional finite inequality from a supplied filter
table and certified response intervals. It does not authenticate an external
source, its support ceiling, or the response intervals. ``prime_grade_data``
constructs those data from explicit integer factorization on one finite fiber.
No computation here proves binary Goldbach for an unbounded range.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, isqrt
import json


def exact(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("Use integers or Fractions, not floats or booleans")
    return Q(value)


def natural(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"An integer >= {minimum} is required")
    return value


@dataclass(frozen=True)
class FilterData:
    """Rows are filters on grades 0,...,L; first row is constant one.

    ``source_id`` records attribution, never a cryptographic/source proof.
    Intervals must enclose the true responses for the theorem to apply.
    """

    table: tuple[tuple[Q, ...], ...]
    intervals: tuple[tuple[Q, Q], ...]
    source_id: str

    def validate(self) -> None:
        if not self.table or not self.table[0]:
            raise ValueError("A nonempty finite filter table is required")
        width = len(self.table[0])
        if any(len(row) != width for row in self.table):
            raise ValueError("Filter rows must have the same support")
        for row in self.table:
            for value in row:
                exact(value)
        if any(value != 1 for value in self.table[0]):
            raise ValueError("The first filter must retain total mass")
        if len(self.intervals) != len(self.table):
            raise ValueError("One response interval is required per filter")
        for pair in self.intervals:
            if len(pair) != 2 or exact(pair[0]) > exact(pair[1]):
                raise ValueError("Malformed response interval")
        if self.intervals[0][0] < 0:
            raise ValueError("Mass lower bound must be nonnegative")
        if not isinstance(self.source_id, str) or not self.source_id.strip():
            raise ValueError("Explicit source attribution is required")


@dataclass(frozen=True)
class ZeroMassCertificate:
    lower_bound: Q
    combined_filter: tuple[Q, ...]

    @property
    def proves_positive(self) -> bool:
        return self.lower_bound > 0


def certify_zero_mass(data: FilterData, weights) -> ZeroMassCertificate:
    """Check q(0)=1, q(j)<=0 for j>0, then return a sound lower bound.

    The return means c_0 >= lower_bound *if* the supplied intervals describe
    a nonnegative histogram supported on the stated grades. No solver is trusted.
    """
    data.validate()
    weights = tuple(exact(value) for value in weights)
    if len(weights) != len(data.table):
        raise ValueError("One exact weight is required per filter")
    q = tuple(sum((w * row[j] for w, row in zip(weights, data.table)), Q(0))
              for j in range(len(data.table[0])))
    if q[0] != 1 or any(value > 0 for value in q[1:]):
        raise ValueError("The combined filter is not a zero-sector minorant")
    lower = sum((w * (lo if w >= 0 else hi)
                 for w, (lo, hi) in zip(weights, data.intervals)), Q(0))
    return ZeroMassCertificate(lower, q)


def moment_table(max_grade: int, degree: int) -> tuple[tuple[Q, ...], ...]:
    natural(max_grade)
    natural(degree)
    return tuple(tuple(Q(j ** k) for j in range(max_grade + 1))
                 for k in range(degree + 1))


def histogram_data(histogram, degree: int, *, source_id: str) -> FilterData:
    histogram = tuple(exact(value) for value in histogram)
    if not histogram or any(value < 0 for value in histogram):
        raise ValueError("A nonnegative finite histogram is required")
    table = moment_table(len(histogram) - 1, degree)
    moments = tuple(sum((a * b for a, b in zip(row, histogram)), Q(0))
                    for row in table)
    data = FilterData(table, tuple((value, value) for value in moments), source_id)
    data.validate()
    return data


def quadratic_filter(max_grade: int) -> tuple[Q, ...]:
    """(h-1)(h-L)/L, for 1<=h<=L; the L=0 case is trivial."""
    natural(max_grade)
    if max_grade == 0:
        return (Q(1),)
    return (Q(1), -Q(max_grade + 1, max_grade), Q(1, max_grade))


def exact_zero_projector(max_grade: int) -> tuple[Q, ...]:
    """Coefficients of product_{j=1}^L (1-h/j), an exact finite projector."""
    natural(max_grade)
    coeff = [Q(1)]
    for j in range(1, max_grade + 1):
        out = [Q(0)] * (len(coeff) + 1)
        for k, value in enumerate(coeff):
            out[k] += value
            out[k + 1] -= value / j
        coeff = out
    return tuple(coeff)


def omega(n: int) -> int:
    natural(n, 2)
    factors = 0
    p = 2
    while p * p <= n:
        while n % p == 0:
            n //= p
            factors += 1
        p += 1
    return factors + int(n > 1)


def is_prime(n: int) -> bool:
    """Separate primality route; does not call omega."""
    return n >= 2 and all(n % p for p in range(2, isqrt(n) + 1))


def prime_grade_histogram(midpoint: int) -> tuple[int, ...]:
    n = natural(midpoint, 2)
    # h=Omega(n+d)+Omega(n-d)-2 <= floor(log2(n*n))-2.
    ceiling = (n * n).bit_length() - 3
    counts = [0] * (ceiling + 1)
    for d in range(n - 1):
        h = omega(n + d) + omega(n - d) - 2
        if not 0 <= h <= ceiling:
            raise AssertionError("The arithmetic grade ceiling failed")
        counts[h] += 1
    return tuple(counts)


def prime_grade_data(midpoint: int, degree: int) -> FilterData:
    return histogram_data(
        prime_grade_histogram(midpoint), degree,
        source_id=f"all integer endpoints n+/-d >=2; n={midpoint}; trial-factor Omega",
    )


def direct_goldbach_count(midpoint: int) -> int:
    n = natural(midpoint, 2)
    return sum(is_prime(n + d) and is_prime(n - d) for d in range(n - 1))


def moment_matched_ground_twins(degree: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Exact source-blind ambiguity through the requested moment degree."""
    degree = natural(degree)
    order = degree + 1
    even = tuple(comb(order, j) if j % 2 == 0 else 0 for j in range(order + 1))
    odd = tuple(comb(order, j) if j % 2 else 0 for j in range(order + 1))
    return even, odd


def sum_counts(values) -> Counter:
    values = tuple(values)
    return Counter(a + b for a in values for b in values)


def difference_counts(values) -> Counter:
    values = tuple(values)
    return Counter(a - b for a in values for b in values)


def circular_sum_count(values, target: int, modulus: int) -> int:
    natural(modulus, 1)
    return sum(count for value, count in sum_counts(values).items()
               if (value - target) % modulus == 0)


def report() -> dict:
    data = prime_grade_data(10, 2)
    certificate = certify_zero_mass(data, quadratic_filter(4))
    twins = moment_matched_ground_twins(2)
    twin_data = [histogram_data(h, 2, source_id="binomial counterfeit") for h in twins]
    x, y = (0, 1, 4), (0, 10, 25)
    a = tuple(sorted(i + j for i in x for j in y))
    b = tuple(sorted(i + 25 - j for i in x for j in y))
    primes = tuple(p for p in range(2, 9) if is_prime(p))
    return {
        "scope": "finite exact certificate and hostile controls; Goldbach OPEN",
        "midpoint_10": {
            "support_ceiling": 4,
            "moments": [str(lo) for lo, _ in data.intervals],
            "weights": [str(value) for value in quadratic_filter(4)],
            "lower_bound": str(certificate.lower_bound),
            "direct_unordered_count": direct_goldbach_count(10),
        },
        "moment_twins": {
            "histograms": twins,
            "moments": [[str(lo) for lo, _ in d.intervals] for d in twin_data],
            "zero_grade_masses": [h[0] for h in twins],
        },
        "power_spectrum_control": {
            "a": a, "b": b,
            "same_difference_counts": difference_counts(a) == difference_counts(b),
            "sum_10_counts": [sum_counts(a)[10], sum_counts(b)[10]],
        },
        "circle_alias": {
            "source_primes": primes, "target": 8,
            "ordinary_count": sum_counts(primes)[8],
            "modulus_4_count": circular_sum_count(primes, 8, 4),
            "modulus_15_count": circular_sum_count(primes, 8, 15),
        },
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
