"""Exact, source-typed finite probes for carrier-relative path measure.

Research prototype. No normality theorem. Standard library only.
Every main arithmetic calculation uses Fraction; roots of unity are
represented by exact residue counts in Z[q]/(q^(m/2)+1), for m a power of 2.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from typing import Iterable


def bbp_forcing(n: int) -> Fraction:
    """Original four signed BBP poles, n>=1; do not alter this source."""
    if n < 1:
        raise ValueError("BBP forcing index must be positive")
    return (Fraction(4, 8 * n - 7) - Fraction(2, 8 * n - 4)
            - Fraction(1, 8 * n - 3) - Fraction(1, 8 * n - 2))


def bbp_orbit(count: int) -> tuple[Fraction, ...]:
    """U_0=0, U_(n+1)=16U_n+r(n+1). Returns U_0..U_(count-1)."""
    if count < 0:
        raise ValueError("count must be nonnegative")
    states = []
    u = Fraction(0)
    for n in range(count):
        states.append(u)
        u = 16 * u + bbp_forcing(n + 1)
    return tuple(states)


def bbp_tail_upper(n: int) -> Fraction:
    """T_n=sum_{k>n}16^(n-k)r(k) <= 1/((8n+1)(8n+2))."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    return Fraction(1, (8 * n + 1) * (8 * n + 2))


def bbp_tail_partial(n: int, extra: int) -> Fraction:
    """First 'extra' positive terms of the exact BBP Green future tail."""
    if n < 0 or extra < 0:
        raise ValueError("nonnegative n and extra required")
    return sum((Fraction(1, 16**j) * bbp_forcing(n + j)
                for j in range(1, extra + 1)), Fraction(0))


def affine_next(n: int, x: Fraction) -> Fraction:
    """T_n(x)=16x+r(n+1)."""
    if n < 0:
        raise ValueError("time index must be nonnegative")
    return 16 * Fraction(x) + bbp_forcing(n + 1)


def prime_square_defect(n: int, p: int) -> Fraction:
    """T_n(p*x)-p*T_n(x)=(1-p)*r(n+1), independent of x."""
    if p < 2:
        raise ValueError("p must be >=2 (primality not required for this identity)")
    return (1 - p) * bbp_forcing(n + 1)


def cyclotomic_two_power(coefficients: Iterable[int], order: int) -> tuple[int, ...]:
    """Exact element of Z[q]/Phi_order(q), for order 2,4,8,... .

    Phi_(2^a)(q)=q^(2^(a-1))+1, so coefficients have a canonical
    degree-<order/2 representation. Zero tuple iff polynomial vanishes
    at a primitive order-th complex root of unity.
    """
    if order < 2 or order & (order - 1):
        raise ValueError("order must be a power of two >=2")
    half = order // 2
    out = [0] * half
    for exponent, coeff in enumerate(coefficients):
        residue = exponent % order
        out[residue % half] += coeff if residue < half else -coeff
    return tuple(out)


@lru_cache(maxsize=None)
def gaussian_pascal(n: int, k: int) -> tuple[int, ...]:
    """Coefficients of the inversion-weighted Pascal path sum [n choose k]_q.

    A path is a length-n bitword with k ones; its exponent is the number
    of ordered 0-before-1 pairs (a path-area / inversion statistic).
    """
    if n < 0:
        raise ValueError("n must be nonnegative")
    if k < 0 or k > n:
        return (0,)
    if k == 0 or k == n:
        return (1,)
    a = gaussian_pascal(n - 1, k)
    b = gaussian_pascal(n - 1, k - 1)
    shift = n - k
    length = max(len(a), len(b) + shift)
    ans = [0] * length
    for i, x in enumerate(a):
        ans[i] += x
    for i, x in enumerate(b):
        ans[i + shift] += x
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return tuple(ans)


def enumerate_pascal_paths(n: int, k: int) -> tuple[int, ...]:
    """Independent direct oracle, not using the Gaussian-Pascal recurrence."""
    if n < 0 or not 0 <= k <= n:
        raise ValueError("require 0<=k<=n")
    counts = [0] * (k * (n - k) + 1)
    for one_positions in combinations(range(n), k):
        area = sum(position - index for index, position in enumerate(one_positions))
        counts[area] += 1
    while len(counts) > 1 and counts[-1] == 0:
        counts.pop()
    return tuple(counts)


def fair_pascal_measure(n: int) -> tuple[Fraction, ...]:
    """Marginal distribution on Pascal endpoints of n fair successor steps."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    from math import comb
    return tuple(Fraction(comb(n, k), 2**n) for k in range(n+1))


def integer_line_green_three_fifths(a: int, b: int) -> Fraction:
    """All-path Green sum on Z for symmetric steps, discount lambda=3/5.

    G(0,d)=sum_(length>=0) (3/5)^length P(S_length=d)
           =(5/4)*3^(-abs(d)), an exact rational resolvent.
    """
    return Fraction(5, 4 * 3**abs(a-b))


def finite_integer_line_green(a: int, b: int, max_length: int) -> Fraction:
    """Exact truncation of walk Green path sum; rigorously below full sum.

    The remainder is <= (3/5)^(max_length+1)/(1-3/5).
    """
    if max_length < 0:
        raise ValueError("max_length must be nonnegative")
    from math import comb
    d = abs(a-b)
    return sum((Fraction(comb(l,(l+d)//2)*3**l, 10**l)
                for l in range(d,max_length+1,2)), Fraction(0))


def gauge_path_phase(path: tuple[tuple[int, int], ...], potential: dict[tuple[int, int], Fraction]) -> Fraction:
    """Sum of exact endpoint-potential edge differences along a path."""
    if not path:
        raise ValueError("path must contain vertices")
    return sum((potential[v] - potential[u] for u, v in zip(path, path[1:])), Fraction(0))


def pascal_bitpath(bits: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    k = 0
    nodes = [(0, 0)]
    for i, bit in enumerate(bits):
        if bit not in (0, 1):
            raise ValueError("path bits must be 0 or 1")
        k += bit
        nodes.append((i + 1, k))
    return tuple(nodes)


def effective_resistance(vertices: int, edges: Iterable[tuple[int, int, Fraction]], s: int, t: int) -> Fraction:
    """Exact grounded-Laplacian solve; positive conductances only.

    Returns the electrical flow's minimum energy for a unit s->t demand.
    """
    if vertices < 2 or s == t or not (0 <= s < vertices and 0 <= t < vertices):
        raise ValueError("invalid vertices or endpoints")
    L = [[Fraction(0) for _ in range(vertices)] for _ in range(vertices)]
    for u, v, c in edges:
        if not (0 <= u < vertices and 0 <= v < vertices) or u == v:
            raise ValueError("invalid edge")
        c = Fraction(c)
        if c <= 0:
            raise ValueError("edge conductance must be positive")
        L[u][u] += c
        L[v][v] += c
        L[u][v] -= c
        L[v][u] -= c
    retained = [i for i in range(vertices) if i != t]
    A = [[L[i][j] for j in retained] + [Fraction(int(i == s))]
         for i in retained]
    n = vertices - 1
    for col in range(n):
        pivot = next((i for i in range(col, n) if A[i][col]), None)
        if pivot is None:
            raise ValueError("carrier is disconnected from the sink or has isolated nodes")
        A[col], A[pivot] = A[pivot], A[col]
        factor = A[col][col]
        A[col] = [z / factor for z in A[col]]
        for row in range(n):
            if row == col:
                continue
            factor = A[row][col]
            if factor:
                A[row] = [x - factor * y for x, y in zip(A[row], A[col])]
    return A[retained.index(s)][-1]


def two_adic_residue(value: Fraction, exponent: int) -> int:
    """Z_2 value reduced modulo 2^exponent, requiring an odd denominator."""
    if exponent < 1:
        raise ValueError("positive exponent required")
    x = Fraction(value)
    if x.denominator % 2 == 0:
        raise ValueError("value not 2-adically integral")
    m = 2**exponent
    return (x.numerator * pow(x.denominator, -1, m)) % m


def source_residue_pairs(exponent: int, start: int = 0) -> tuple[tuple[int, int], ...]:
    """Pair original-source indices whose 2-adic residues differ by m/2.

    Requires *verified* complete-residue property on this exact finite
    window. Does not infer any Archimedean phase opposition.
    """
    if not 1 <= exponent <= 8 or start < 0:
        raise ValueError("finite probe limited to exponents 1..8 and start>=0")
    m = 2**exponent
    orbit = bbp_orbit(start+m)[start:]
    lookup = {}
    for n, u in enumerate(orbit):
        residue = two_adic_residue(u, exponent)
        if residue in lookup:
            raise ValueError("not a complete residue system")
        lookup[residue] = n
    if len(lookup) != m:
        raise ValueError("not a complete residue system")
    return tuple((lookup[j], lookup[j + m // 2]) for j in range(m // 2))


def circle_distance_to_integer(x: Fraction) -> Fraction:
    x = Fraction(x)
    residue = x.numerator % x.denominator
    return Fraction(min(residue, x.denominator - residue), x.denominator)


def pairing_phase_error(orbit: tuple[Fraction, ...], pairs: Iterable[tuple[int, int]], h: int) -> Fraction:
    """Sum of exact errors to opposite circle phase; no trig rounding."""
    if not h:
        raise ValueError("h must be nonzero")
    used = set()
    error = Fraction(0)
    for i, j in pairs:
        if i == j or i in used or j in used or not (0 <= i < len(orbit) and 0 <= j < len(orbit)):
            raise ValueError("pairs must be a disjoint partial matching")
        used.update((i, j))
        error += circle_distance_to_integer(h * (orbit[j] - orbit[i]) - Fraction(1, 2))
    return error


def finite_matching_upper_bound(orbit: tuple[Fraction, ...], pairs: tuple[tuple[int, int], ...], h: int) -> Fraction:
    """Certified bound: |sum exp(2pi ih U_n)| <= unmatched + (44/7)*sum errors.

    Uses pi < 22/7 and |exp(2pi it)-1| <= 2pi*||t||.
    This may be vacuous; users must inspect it relative to len(orbit).
    """
    return Fraction(len(orbit) - 2 * len(pairs)) + Fraction(44, 7) * pairing_phase_error(orbit, pairs, h)


def sample_receipt() -> dict:
    """Compact exact measurements, not an asymptotic certificate."""
    samples = {}
    for exponent in (2, 3, 4, 5):
        pairs = source_residue_pairs(exponent)
        orbit = bbp_orbit(2**exponent)
        err = pairing_phase_error(orbit, pairs, 1)
        samples[str(exponent)] = {
            "states": 2**exponent,
            "pairs": len(pairs),
            "total_anti_phase_error": str(err),
            "mean_pair_error": str(err / len(pairs)),
            "certified_bound": str(finite_matching_upper_bound(orbit, pairs, 1)),
            "bound_vacuous": finite_matching_upper_bound(orbit, pairs, 1) >= len(orbit),
        }
    return {
        "bbp_r1": str(bbp_forcing(1)),
        "triangle_R_0_2": str(effective_resistance(3, [(0,1,1),(1,2,1),(0,2,1)],0,2)),
        "line_R_0_2": str(effective_resistance(3, [(0,1,1),(1,2,1)],0,2)),
        "pascal_m16_all_interior_vanish": all(
            not any(cyclotomic_two_power(gaussian_pascal(16,k),16))
            for k in range(1,16)
        ),
        "prime_square_n0_p3": str(prime_square_defect(0,3)),
        "two_adic_pairing": samples,
        "status": "finite exact probes only; selected real Fourier gate OPEN",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(sample_receipt(), indent=2, sort_keys=True))
