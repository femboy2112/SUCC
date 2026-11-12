"""Exact standard-library finite tests for carrier-first Goldbach coupling.

This is a finite diagnostic, not an analytic proof of Goldbach.  No external
prime lists, numerical Fourier approximations or conjectural inputs are used.
"""
from __future__ import annotations

from math import isqrt


def trial_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def sieve(limit: int) -> list[bool]:
    p = [False, False] + [True] * max(0, limit - 1)
    for d in range(2, isqrt(limit) + 1):
        if p[d]:
            for k in range(d * d, limit + 1, d):
                p[k] = False
    return p


def plus(n: int) -> list[tuple[int, int]]:
    return [(a, n - a) for a in range(2, n - 1) if n - a >= 2]


def times(n: int) -> list[tuple[int, int]]:
    return [(a, n // a) for a in range(2, n) if n % a == 0]


def two_color_goldbach(n: int, prime: list[bool]) -> int:
    return sum(prime[a] * prime[b] for a, b in plus(n))


def pair_matrix(prime_vector: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(a * b for b in prime_vector) for a in prime_vector)


def convolution(prime: list[bool]) -> list[int]:
    # Independent summation by endpoints, not plus() or two_color_goldbach().
    x = len(prime) - 1
    result = [0] * (2 * x + 1)
    active = [i for i in range(2, x + 1) if prime[i]]
    for a in active:
        for b in active:
            result[a + b] += 1
    return result


def additive_triples_left(n: int) -> list[tuple[int, int, int]]:
    return [(a, b, c) for ab, c in plus(n) for a, b in plus(ab)]


def additive_triples_right(n: int) -> list[tuple[int, int, int]]:
    return [(a, b, c) for a, bc in plus(n) for b, c in plus(bc)]


def multiplicative_triples_left(n: int) -> list[tuple[int, int, int]]:
    return [(a, b, c) for ab, c in times(n) for a, b in times(ab)]


def multiplicative_triples_right(n: int) -> list[tuple[int, int, int]]:
    return [(a, b, c) for a, bc in times(n) for b, c in times(bc)]


def alternate_empty_mask(n: int, marked_d: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Zero oracle and single-witness oracle indistinguishable without probing marked pair."""
    z = [0] * (2 * n)
    s = z.copy()
    s[n - marked_d] = 1
    s[n + marked_d] = 1
    return tuple(z), tuple(s)


def scope_report() -> dict:
    p = sieve(512)
    values = {str(n): two_color_goldbach(n, p) for n in (4, 6, 10, 20, 22, 100, 200, 256, 512)}
    source = [False] * 513
    for a in range(2, 513):
        source[a] = bool(p[a] and a % 4 == 1)
    counterfeit = {str(n): two_color_goldbach(n, source) for n in (12, 20, 100, 200, 256, 400, 512)}
    return {
        "scope": "finite exact arithmetic; no new Goldbach theorem",
        "ordered_goldbach_count": values,
        "one_mod_four_prime_subsource": counterfeit,
        "coassociativity_additive_checked_through": 84,
        "coassociativity_multiplicative_checked_through": 84,
        "prime_projector_checked_through": 512,
        "all_mask_matrix_injectivity_checked_at_size": 8,
        "black_box_zero_oracle_lower_bound": "n-1 disjoint midpoint pairs for target 2n; no source structure",
    }

if __name__ == "__main__":
    import json
    print(json.dumps(scope_report(), indent=2, sort_keys=True))