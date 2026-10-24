"""Exact Lucas incidence, symmetric quotients and base-transfer obstructions.

These are finite, source-agnostic combinatorial operators. They do not prove
anything about the real-circle distribution of the authenticated BBP orbit.
Integer/Fraction computations only; no numerical probability approximations.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb, isqrt


def _nat(value: int, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")
    return value


def _prime(p: int) -> int:
    if type(p) is not int or p < 2 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("p must be prime")
    return p


def _exact(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ValueError("exact integer or Fraction required")
    return Fraction(value)


def digit_histogram(p: int, depth: int, n: int) -> tuple[int, ...]:
    """Histogram of the first `depth` base-p digits of n, including zeros."""
    _prime(p); _nat(depth, "depth"); _nat(n, "n")
    if n >= p**depth:
        raise ValueError("n does not fit in the declared depth")
    hist = [0] * p
    for _ in range(depth):
        hist[n % p] += 1
        n //= p
    return tuple(hist)


def lucas_unit(p: int, n: int, k: int) -> bool:
    """Whether binomial(n,k) is nonzero mod prime p, including k>n."""
    _prime(p); _nat(n, "n"); _nat(k, "k")
    while n or k:
        if k % p > n % p:
            return False
        n //= p
        k //= p
    return True


def lucas_row_support(p: int, n: int) -> int:
    """Product of (n_i+1) for base-p digits of n (Lucas/Fine)."""
    _prime(p); _nat(n, "n")
    result = 1
    while n:
        result *= 1 + n % p
        n //= p
    return result


def lucas_alphabet_size(p: int) -> int:
    return _prime(p) * (p + 1) // 2


def lucas_total(p: int, depth: int) -> int:
    _nat(depth, "depth")
    return lucas_alphabet_size(p)**depth


def pair_to_address(p: int, depth: int, n: int, k: int) -> int:
    """Base-L_p address: digit (a,b), b<=a, gets a(a+1)/2+b."""
    _prime(p); _nat(depth, "depth"); _nat(n, "n"); _nat(k, "k")
    if max(n, k) >= p**depth:
        raise ValueError("pair does not fit in the declared depth")
    address, stride = 0, 1
    radix = lucas_alphabet_size(p)
    for _ in range(depth):
        a, b = n % p, k % p
        if b > a:
            raise ValueError("pair is outside Lucas support")
        address += (a * (a + 1) // 2 + b) * stride
        stride *= radix
        n //= p
        k //= p
    return address


def address_to_pair(p: int, depth: int, address: int) -> tuple[int, int]:
    _prime(p); _nat(depth, "depth"); _nat(address, "address")
    radix = lucas_alphabet_size(p)
    if address >= radix**depth:
        raise ValueError("address does not fit in the declared depth")
    n = k = 0
    place = 1
    for _ in range(depth):
        label = address % radix
        a = 0
        while label >= a + 1:
            label -= a + 1
            a += 1
        n += a * place
        k += label * place
        place *= p
        address //= radix
    return n, k


def zeta_apply(p: int, depth: int, values: tuple[int | Fraction, ...]) -> tuple[Fraction, ...]:
    """Tensor J_p^depth, J_p[a,b]=1 if b<=a; no dense matrix."""
    _prime(p); _nat(depth, "depth")
    size = p**depth
    if len(values) != size:
        raise ValueError("one exact value per base-p source digit word required")
    answer = [_exact(v) for v in values]
    for i in range(depth):
        stride = p**i
        for block in range(0, size, p*stride):
            for offset in range(stride):
                running = Fraction(0)
                for digit in range(p):
                    j = block + digit*stride + offset
                    running += answer[j]
                    answer[j] = running
    return tuple(answer)


def lucas_residue_apply(p: int, depth: int, values: tuple[int, ...]) -> tuple[int, ...]:
    """Actual Pascal coefficients modulo p, NOT just their Lucas support.

    For p=2 this equals zeta_apply reduced modulo 2. For p>2 the
    nontrivial units binomial(a,b) mod p must be retained.
    """
    _prime(p); _nat(depth, "depth")
    size = p**depth
    if len(values) != size or any(type(v) is not int for v in values):
        raise ValueError("one integer field value per source digit word required")
    answer = [v % p for v in values]
    for i in range(depth):
        stride = p**i
        for block in range(0, size, p*stride):
            for offset in range(stride):
                column = [answer[block + d*stride + offset] for d in range(p)]
                for a in range(p):
                    answer[block + a*stride + offset] = sum(
                        comb(a,b)*column[b] for b in range(a+1)) % p
    return tuple(answer)


def histogram_average(p: int, depth: int, values: tuple[int | Fraction, ...]) -> dict[tuple[int, ...], Fraction]:
    """Conditional average over all permutations of p-adic digit positions."""
    _prime(p); _nat(depth, "depth")
    if len(values) != p**depth:
        raise ValueError("one value per base-p source digit word required")
    sums: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    counts: dict[tuple[int, ...], int] = defaultdict(int)
    for n, value in enumerate(values):
        h = digit_histogram(p, depth, n)
        sums[h] += _exact(value)
        counts[h] += 1
    return {h: sums[h] / counts[h] for h in counts}


def histogram_zeta_apply(p: int, depth: int, hist_values: dict[tuple[int, ...], int | Fraction]) -> dict[tuple[int, ...], Fraction]:
    """Induced tensor zeta on symmetric histogram functions; exact intertwiner."""
    _prime(p); _nat(depth, "depth")
    allowed = set(digit_histogram(p, depth, n) for n in range(p**depth))
    if set(hist_values) != allowed:
        raise ValueError("complete valid histogram family required")
    typed = {h: _exact(hist_values[h]) for h in allowed}
    result = {}
    for outer in allowed:
        multiplicities = {(0,)*p: 1}
        for a in range(p):
            for _ in range(outer[a]):
                updated: dict[tuple[int, ...], int] = defaultdict(int)
                for inner, coefficient in multiplicities.items():
                    for b in range(a+1):
                        target = list(inner)
                        target[b] += 1
                        updated[tuple(target)] += coefficient
                multiplicities = updated
        result[outer] = sum((coefficient*typed[inner] for inner, coefficient in multiplicities.items()), Fraction(0))
    return result


def histogram_symmetrization_tv(
    p: int, depth: int, weights: tuple[int | Fraction, ...]
) -> Fraction:
    """Exact TV of a source law from its coordinate-permutation average.

    A bound on any [0,1]-valued positional gate's symmetrization defect,
    not a bound on pi without an authenticated source-to-state map.
    """
    _prime(p); _nat(depth, "depth")
    if len(weights) != p**depth:
        raise ValueError("one nonnegative weight per source digit word required")
    w = tuple(_exact(v) for v in weights)
    if any(v < 0 for v in w) or sum(w, Fraction(0)) != 1:
        raise ValueError("normalized nonnegative exact probability law required")
    average = histogram_average(p,depth,w)
    return sum((abs(value-average[digit_histogram(p,depth,n)])
                for n,value in enumerate(w)),Fraction(0)) / 2


def binomial_transform(values: tuple[int | Fraction, ...]) -> tuple[Fraction, ...]:
    """Rank quotient of the p=2 tensor zeta operator."""
    if not values:
        raise ValueError("nonempty finite rank family required")
    typed = tuple(_exact(v) for v in values)
    return tuple(sum((comb(n,k)*typed[k] for k in range(n+1)), Fraction(0)) for n in range(len(typed)))


def uniform_embedding_tv(p: int, q: int, depth: int) -> Fraction:
    """TV between uniform q-Lucas cells and embedded uniform p-cells (p<q)."""
    _prime(p); _prime(q); _nat(depth, "depth")
    if p >= q:
        raise ValueError("natural digit inclusion requires p<q")
    return 1 - Fraction(lucas_alphabet_size(p), lucas_alphabet_size(q))**depth


def four_bit_rank_residual(depth: int) -> Fraction:
    """Optimal L2 MSE predicting low-four-bit-zero from popcount(n).

    Source: n is uniform on {0,1}^depth and k=0 (an admissible Lucas cell).
    NOT the actual BBP source or the uniform distribution on all Lucas cells.
    """
    _nat(depth, "depth")
    if depth < 4:
        raise ValueError("at least four binary digits required")
    copies = comb(depth, 4)
    second = sum((Fraction(comb(4,s)*comb(depth-4,4-s), 2**(8-s))
                  for s in range(5) if 0 <= 4-s <= depth-4), Fraction(0)) / copies
    return Fraction(1,16) - second
