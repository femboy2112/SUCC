"""Exact finite arithmetic for the prime fixed-point dossier.

No prime oracle, floating-point threshold, or universal Goldbach claim.
The divisor source and marking-sieve reference are distinct algorithms.
The lambda observer lives separately in lambda_observer.py.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import isqrt


def integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"exact integer >= {minimum} required")
    return value


def proper_factorizations(n: int) -> tuple[tuple[int, int], ...]:
    """Ordered pairs a,b>=2 with ab=n, using a square-root scan."""
    integer(n, 1)
    pairs = []
    for a in range(2, isqrt(n) + 1):
        if n % a == 0:
            b = n // a
            pairs.append((a, b))
            if a != b:
                pairs.append((b, a))
    return tuple(sorted(pairs))


def tau(n: int) -> int:
    integer(n, 1)
    return 1 if n == 1 else 2 + len(proper_factorizations(n))


def factor_energy(n: int) -> int:
    """Diagonal of B*B on n>=2; 1 is outside this Hilbert carrier."""
    integer(n, 2)
    return len(proper_factorizations(n))


def divisor_functor(n: int) -> int:
    integer(n, 1)
    return n ** (tau(n) - 1)


def least_divisor(n: int) -> int:
    integer(n, 2)
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return d
    return n


def prime_ceiling(n: int) -> int:
    """Prime closure in the usual-order category; Euclid proves totality."""
    integer(n, 2)
    while least_divisor(n) != n:
        n += 1
    return n


def prime_stream():
    """Reference host implementation; not itself a lambda evaluator."""
    p = 2
    while True:
        yield p
        p = prime_ceiling(p + 1)


def sieve_mask(limit: int) -> tuple[int, ...]:
    """Independent reference: mark multiples, not factor each candidate."""
    integer(limit)
    flags = [1] * (limit + 1)
    flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            for k in range(p * p, limit + 1, p):
                flags[k] = 0
    return tuple(flags)


def divisor_receipt(n: int) -> dict:
    integer(n, 2)
    pairs = proper_factorizations(n)
    return {"n": n, "pairs": [list(pair) for pair in pairs],
            "energy": len(pairs), "prime": len(pairs) == 0}


def verify_divisor_receipt(receipt: dict) -> bool:
    """Full-range divisibility replay, independent of the paired producer."""
    if type(receipt) is not dict or set(receipt) != {"n", "pairs", "energy", "prime"}:
        return False
    n = receipt["n"]
    if type(n) is not int or n < 2 or type(receipt["pairs"]) is not list:
        return False
    if type(receipt["energy"]) is not int or type(receipt["prime"]) is not bool:
        return False
    pairs = receipt["pairs"]
    if any(type(p) is not list or len(p) != 2 or
           any(type(v) is not int for v in p) for p in pairs):
        return False
    expected = [[d, n // d] for d in range(2, n) if n % d == 0]
    return (pairs == expected and receipt["energy"] == len(expected)
            and receipt["prime"] is (len(expected) == 0))


def screened(n: int, cutoff: int) -> int:
    """Keep n unless a tested proper divisor 2<=d<=cutoff splits it."""
    integer(n, 2)
    integer(cutoff, 1)
    return int(all(n % d for d in range(2, min(cutoff, n - 1) + 1)))


SWAPPED_PRIMES = (53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
SWAPPED_COMPOSITES = (9, 15, 21, 25, 27, 33, 35, 39, 45, 49)
PERMUTATION = dict(zip(SWAPPED_PRIMES, SWAPPED_COMPOSITES))
PERMUTATION.update(zip(SWAPPED_COMPOSITES, SWAPPED_PRIMES))


def relabel(n: int) -> int:
    """Finite, parity-preserving involution, fixing 1 and every even n."""
    integer(n, 1)
    return PERMUTATION.get(n, n)


def transported_product(a: int, b: int) -> int:
    integer(a, 1)
    integer(b, 1)
    return relabel(relabel(a) * relabel(b))


def transported_energy(n: int) -> int:
    integer(n, 2)
    return factor_energy(relabel(n))


def _mask(values) -> tuple[int, ...]:
    values = tuple(values)
    if any(type(x) is not int or x not in (0, 1) for x in values):
        raise ValueError("mask must contain exact integer bits")
    return values


def reflection_statistics(mask) -> dict:
    """Mask indexed by k=2,...,N-2; reversed indexing implements J_N.

    eigen_plus/minus/zero are the multiplicities for P J_N P, not for
    the skew-adjoint commutator [P,J_N].
    """
    mask = _mask(mask)
    if not mask or len(mask) % 2 != 1:
        raise ValueError("an odd nonempty interval for an even N is required")
    reflected = mask[::-1]
    ordered = sum(a * b for a, b in zip(mask, reflected))
    mismatch = sum((a - b) ** 2 for a, b in zip(mask, reflected))
    center = mask[len(mask) // 2]
    return {"N": len(mask) + 3, "dimension": len(mask),
            "prime_sector": sum(mask), "ordered_pairs": ordered,
            "commutator_hs_squared": mismatch,
            "reflection_trace": center,
            "eigen_plus": (ordered + center) // 2,
            "eigen_minus": (ordered - center) // 2,
            "eigen_zero": len(mask) - ordered}


def pair_spectral_receipt(N: int, r: int | None = None, *, transported=False) -> dict:
    """Rational fixed-sum filter, source given by all proper factorizations.

    Implements the sum-energy resolvent, not the tensor-product resolvent.
    Both recover the same zero modes; their finite traces generally differ.
    """
    integer(N, 4)
    if N % 2:
        raise ValueError("even target required")
    if type(transported) is not bool:
        raise ValueError("transported must be a boolean")
    length = N - 3
    r = length.bit_length() if r is None else integer(r)
    energy = transported_energy if transported else factor_energy
    individual = [energy(k) for k in range(2, N - 1)]
    spectrum = Counter(a + b for a, b in zip(individual, individual[::-1]))
    trace = sum((Fraction(count, (1 + value) ** r)
                 for value, count in spectrum.items()), Fraction())
    zero_modes = spectrum.get(0, 0)
    bound = Fraction(length - zero_modes, 2 ** r)
    cutoff_valid = 2 ** r > length
    return {"N": N, "r": r, "dimension": length,
            "source": "transported_multiplication" if transported else "ordinary_multiplication",
            "energy_histogram": {str(k): v for k, v in sorted(spectrum.items())},
            "trace": str(trace), "zero_modes": zero_modes,
            "trace_error": str(trace - zero_modes), "error_upper": str(bound),
            "source_free_error_upper": str(Fraction(length, 2 ** r)),
            "floor": trace.numerator // trace.denominator,
            "floor_recovery_certified": cutoff_valid,
            "universal_goldbach_proved": False}


def verify_pair_spectral_receipt(receipt: dict) -> bool:
    """Recompute finite spectrum from direct full divisor scans.

    This verifier does not infer primality from a claimed trace or histogram.
    No general proof-checker or theorem-kernel authority is claimed.
    """
    if type(receipt) is not dict:
        return False
    N, r, source = receipt.get("N"), receipt.get("r"), receipt.get("source")
    if type(N) is not int or N < 4 or N % 2 or type(r) is not int or r < 0:
        return False
    if type(source) is not str or source not in ("ordinary_multiplication", "transported_multiplication"):
        return False
    if any(type(receipt.get(k)) is not int for k in
           ("dimension", "zero_modes", "floor")):
        return False
    if type(receipt.get("floor_recovery_certified")) is not bool:
        return False
    if receipt.get("universal_goldbach_proved") is not False:
        return False
    for name in ("trace", "trace_error", "error_upper", "source_free_error_upper"):
        if type(receipt.get(name)) is not str:
            return False
    histogram = receipt.get("energy_histogram")
    if type(histogram) is not dict or any(type(k) is not str or type(v) is not int
                                        for k, v in histogram.items()):
        return False
    def direct(k):
        if source == "transported_multiplication":
            k = relabel(k)
        return sum(k % d == 0 for d in range(2, k))
    energies = [direct(k) for k in range(2, N - 1)]
    expected = Counter(a + b for a, b in zip(energies, reversed(energies)))
    trace = sum((Fraction(1, (1 + a + b) ** r)
                 for a, b in zip(energies, reversed(energies))), Fraction())
    zero = expected.get(0, 0)
    try:
        return (receipt["dimension"] == N - 3 and receipt["zero_modes"] == zero
                and histogram == {str(k): v for k, v in sorted(expected.items())}
                and Fraction(receipt["trace"]) == trace
                and Fraction(receipt["trace_error"]) == trace - zero
                and Fraction(receipt["error_upper"]) == Fraction(N - 3 - zero, 2 ** r)
                and Fraction(receipt["source_free_error_upper"]) == Fraction(N - 3, 2 ** r)
                and receipt["floor"] == trace.numerator // trace.denominator
                and receipt["floor_recovery_certified"] is (2 ** r > N - 3))
    except (ValueError, ZeroDivisionError):
        return False


def haar_overlap(a, b) -> dict:
    a, b = _mask(a), _mask(b)
    if len(a) != len(b) or not a:
        raise ValueError("equal nonempty masks required")
    size = 1 << (len(a) - 1).bit_length()
    a, b = a + (0,) * (size - len(a)), b + (0,) * (size - len(b))
    constant = Fraction(sum(a) * sum(b), size)
    bands = {}
    width = 2
    while width <= size:
        band = Fraction()
        for start in range(0, size, width):
            mid, end = start + width // 2, start + width
            da = sum(a[start:mid]) - sum(a[mid:end])
            db = sum(b[start:mid]) - sum(b[mid:end])
            band += Fraction(da * db, width)
        bands[str(width)] = str(band)
        width *= 2
    overlap = sum(x * y for x, y in zip(a, b))
    return {"length": size, "A": sum(a), "B": sum(b),
            "overlap": overlap, "constant": str(constant), "bands": bands,
            "detail": str(sum(map(Fraction, bands.values()), Fraction()))}


def midpoint_masks(n: int, *, quotient_parity=False):
    integer(n, 2)
    if type(quotient_parity) is not bool:
        raise ValueError("quotient_parity must be boolean")
    primes = sieve_mask(2 * n)
    displacements = range(n - 1)
    if quotient_parity and n > 2:
        displacements = range(1 - n % 2, n - 1, 2)
    a = tuple(primes[n + d] for d in displacements)
    b = tuple(primes[n - d] for d in displacements)
    return a, b


def crt_haar_certificate(n: int, z: int, width: int) -> dict:
    """Fréchet bounds in disjoint cells of the jointly admissible interior.

    Width is in displacement coordinates, before any parity quotient.
    Marginals share the CRT restriction; no probabilistic independence follows.
    """
    integer(n, 2)
    integer(z, 2)
    integer(width, 1)
    if width & (width - 1):
        raise ValueError("dyadic cell width required")
    primes = sieve_mask(max(2 * n, z))
    screen = tuple(p for p in range(2, z + 1) if primes[p])
    rows = []
    for start in range(0, max(0, n - z), width):
        positions = tuple(d for d in range(start, min(start + width, n - z))
                          if all((n * n - d * d) % p for p in screen))
        A = sum(primes[n + d] for d in positions)
        B = sum(primes[n - d] for d in positions)
        D = len(positions)
        overlap = sum(primes[n + d] * primes[n - d] for d in positions)
        center_present = 0 in positions
        center_bit = primes[n] if center_present else 0
        free_capacity = D - int(center_present)
        coherent_lower = center_bit + max(0, A + B - 2 * center_bit - free_capacity)
        rows.append({"start": start, "capacity": D, "A": A, "B": B,
                     "lower": max(0, A + B - D), "upper": min(A, B),
                     "center_present": center_present, "center_bit": center_bit,
                     "coherent_lower": coherent_lower,
                     "actual": overlap})
    total = sum(primes[n - d] * primes[n + d] for d in range(n - 1))
    return {"n": n, "z": z, "width": width, "rows": rows,
            "lower": sum(row["lower"] for row in rows),
            "coherent_lower": sum(row["coherent_lower"] for row in rows),
            "upper": sum(row["upper"] for row in rows),
            "interior_actual": sum(row["actual"] for row in rows),
            "full_unordered_count": total}


def minimum_overlap_model(certificate: dict, *, preserve_center=False) -> dict:
    """Attain each cell's lower bound by first-A versus last-B placement.

    This synthetic cell model preserves the listed marginals, not primality.
    Without preserve_center, the shared d=0 label is relaxed into two bits.
    With it, the known center bit is retained and one global binary source
    can realize the remaining, pairwise disjoint off-center positions.
    """
    if type(preserve_center) is not bool:
        raise ValueError("preserve_center must be boolean")
    cells = []
    for row in certificate["rows"]:
        D, A, B = row["capacity"], row["A"], row["B"]
        for value in (D, A, B):
            integer(value)
        if A > D or B > D:
            raise ValueError("marginal exceeds cell capacity")
        center = int(preserve_center and row["center_present"])
        bit = row["center_bit"] if center else 0
        left = ([bit] if center else []) + [int(i < A - bit) for i in range(D - center)]
        right = ([bit] if center else []) + [int(i >= D - center - B + bit)
                                           for i in range(D - center)]
        cells.append({"a": left, "b": right})
    return {"cells": cells,
            "overlap": sum(sum(a * b for a, b in zip(c["a"], c["b"]))
                           for c in cells), "preserves_shared_center": preserve_center,
            "is_actual_prime_source": False}
