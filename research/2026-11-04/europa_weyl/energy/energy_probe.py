"""Exact arithmetic probes. Run this file to reproduce FINITE.json on stdout."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from math import isqrt, prod
import json


def primes_upto(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes(len(sieve[p*p::p]))
    return [p for p in range(2, limit + 1) if sieve[p]]


def primal_states(horizon):
    taps = (2, 2, 1, 0, Q(-1, 2), Q(-1, 2), Q(-1, 4), 0)
    states = [Q(0)]
    for n in range(1, horizon + 1):
        num = (((((30720*n - 63232)*n + 45792)*n - 13892)*n + 1641)*n - 48)
        den = prod([4*n-3, 4*n-1, 8*n-7, 8*n-5, 8*n-3, 8*n-1])
        force = Q(num, den)
        assert force == sum(Q(w) / (8*(n-1) + j) for j, w in enumerate(taps, 1))
        states.append(16*states[-1] + force)
    return states


def tent_intensity(values, q):
    count = len(values)
    total = Q(count)
    for a, b in combinations(values, 2):
        x = (a-b) % 1
        total += 2*max(0, 1-q*min(x, 1-x))
    return q*total / count**2


def ratio_header(x):
    # Preserve the exact quotient in hexadecimal without decimal-conversion limits.
    return {"numerator_hex": format(x.numerator, "x"), "denominator_hex": format(x.denominator, "x")}


def cohort(A):
    y = primal_states(2*A)
    ps = primes_upto(16*A)
    scale = 1
    while scale < A*A*16**(2*A):
        scale *= 3
    s = Q(round(-scale*y[2*A]/16**(2*A)), scale)
    preload = [y[n] + s * 16**n for n in range(A, 2*A)]
    arc = max(preload)-min(preload)
    bound = Q(1, 3*(8*A+1)) + Q(1, A*A)
    assert arc <= bound
    counts = {"new": 0, "old_survived": 0, "old_lost": 0, "pairs": 0}
    digest = sha256()
    for n, t in combinations(range(A, 2*A), 2):
        actual = y[t]-y[n]
        altered = preload[t-A]-preload[n-A]
        delta = altered - actual
        check = delta.denominator
        while check % 3 == 0:
            check //= 3
        assert check == 1
        counts["pairs"] += 1
        for p in ps:
            if not 4*t < p <= 8*t:
                continue
            born_late = p > 8*n
            survives = born_late or pow(16, t-n, p) != 1
            assert (actual.denominator % p == 0) == survives
            assert (altered.denominator % p == 0) == survives
            label = "new" if born_late else ("old_survived" if survives else "old_lost")
            counts[label] += 1
            digest.update(f"{n} {t} {p} {label}\n".encode())
    energies = {}
    for q in [4, 8]:
        authentic = tent_intensity(y[A:2*A], q)
        adversary = tent_intensity(preload, q)
        assert adversary >= q*(1-q*bound)
        energies[q] = {"authentic": ratio_header(authentic), "preload": ratio_header(adversary)}
    assert tent_intensity([Q(0)]*3, 4) == 4
    return {"A": A, "top_window_counts": counts, "raw_row_sha256": digest.hexdigest(),
            "preload_diameter": ratio_header(arc), "energy": energies}


if __name__ == "__main__":
    print(json.dumps([cohort(A) for A in [37, 64, 113]], indent=2))
