"""Exact finite prime-wave arithmetic on a declared additive carrier.

Fourier coefficients are rational and frequencies are integer residues.
No floating-point phase test is used to decide divisibility or primality.
The written derivations in PRIME_WAVES.md identify these exact algorithms
with the circle averages. This module is not a physical wave simulator.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt, prod

from cylinder import omega
import prime_observer as po


def signed_integer(value: int) -> int:
    if type(value) is not int:
        raise ValueError("exact integer required")
    return value


def primes_through(limit: int) -> tuple[int, ...]:
    """Trial-division producer, distinct from the marking-sieve reference."""
    po.integer(limit)
    return tuple(n for n in range(2, limit + 1) if po.least_divisor(n) == n)


def prime_tuple(primes) -> tuple[int, ...]:
    values = tuple(primes)
    for p in values:
        po.integer(p, 2)
        if po.least_divisor(p) != p:
            raise ValueError("prime moduli required")
    if len(set(values)) != len(values):
        raise ValueError("distinct prime moduli required for the CRT product")
    return tuple(sorted(values))


def divisor_pulse(modulus: int, n: int) -> int:
    """The exact value of mean_j exp(2*pi*i*j*n/modulus)."""
    po.integer(modulus, 1)
    signed_integer(n)
    return int(n % modulus == 0)


def ramanujan_prime(p: int, n: int) -> int:
    p, = prime_tuple((p,))
    return p * divisor_pulse(p, n) - 1


def survivor_wave(p: int, n: int) -> Fraction:
    """Mean-one, nonnegative periodic packet, not a probability at n."""
    p, = prime_tuple((p,))
    return Fraction(p, p - 1) * (1 - divisor_pulse(p, n))


def local_pair_factor(p: int, target: int) -> Fraction:
    p, = prime_tuple((p,))
    signed_integer(target)
    admissible = p - (1 if target % p == 0 else 2)
    return Fraction(p * admissible, (p - 1) ** 2)


def cyclic_product(left: dict[int, Fraction], right: dict[int, Fraction],
                   modulus: int) -> dict[int, Fraction]:
    """Pointwise wave product, represented by cyclic Fourier convolution."""
    po.integer(modulus, 1)
    for spectrum in (left, right):
        for frequency, coefficient in spectrum.items():
            signed_integer(frequency)
            if type(coefficient) not in (int, Fraction):
                raise ValueError("exact rational Fourier coefficients required")
    out = Counter()
    for a, x in left.items():
        for b, y in right.items():
            out[(a + b) % modulus] += Fraction(x) * Fraction(y)
    return {a: value for a, value in sorted(out.items()) if value}


def survivor_spectrum(primes) -> tuple[int, dict[int, Fraction]]:
    """Fourier expansion of product_p w_p on one shared CRT period."""
    primes = prime_tuple(primes)
    modulus = prod(primes)
    spectrum = {0: Fraction(1)}
    for p in primes:
        local = {a * (modulus // p): Fraction(-1, p - 1)
                 for a in range(1, p)}
        local[0] = Fraction(1)
        spectrum = cyclic_product(spectrum, local, modulus)
    return modulus, spectrum


def periodic_pair_receipt(primes, target: int) -> dict:
    """Compare an actual full-period residue count with the CRT product."""
    primes = prime_tuple(primes)
    signed_integer(target)
    modulus, phi = prod(primes), prod(p - 1 for p in primes)
    residues = tuple(n for n in range(modulus)
                     if gcd(n, modulus) == gcd(target - n, modulus) == 1)
    expected_count = prod(p - (1 if target % p == 0 else 2) for p in primes)
    direct_correlation = Fraction(modulus * len(residues), phi * phi)
    factor_product = prod((local_pair_factor(p, target) for p in primes),
                          start=Fraction(1))
    return {"modulus": modulus, "target": target, "residues": residues,
            "count": len(residues), "crt_count": expected_count,
            "normalized_correlation": direct_correlation,
            "factor_product": factor_product}


def corrected_prime_mask(window: int, cutoff: int | None = None) -> tuple[int, ...]:
    """Commuting divisor-pulse sieve with the n=p exception restored.

    Exact on [2,window] when cutoff >= isqrt(window); smaller cutoffs are
    permitted as explicit under-resolution experiments, not prime decisions.
    """
    po.integer(window, 2)
    cutoff = isqrt(window) if cutoff is None else po.integer(cutoff, 1)
    primes = primes_through(cutoff)
    return (0, 0) + tuple(int(all(n == p or not divisor_pulse(p, n)
                                for p in primes))
                         for n in range(2, window + 1))


def valuation_from_pulses(p: int, n: int) -> int:
    p, = prime_tuple((p,))
    po.integer(n, 1)
    power, count = p, 0
    while power <= n:
        count += divisor_pulse(power, n)
        power *= p
    return count


def pair_count(mask: tuple[int, ...], target: int) -> int:
    po.integer(target, 4)
    if any(type(value) is not int or value not in (0, 1) for value in mask):
        raise ValueError("exact binary mask required")
    if len(mask) <= target - 2:
        raise ValueError("mask must include the complete target interval")
    return sum(mask[n] * mask[target - n] for n in range(2, target - 1))


def endpoint_decomposition(target: int, cutoff: int) -> dict:
    """Exact expansion of (A_z+E_z)*(A_z+E_z), including prime2."""
    po.integer(target, 4)
    po.integer(cutoff, 1)
    primes = primes_through(cutoff)
    modulus = prod(primes)
    small = set(primes)

    def bulk(n):
        return int(2 <= n <= target - 2 and gcd(n, modulus) == 1)

    bulk_pairs = sum(bulk(n) * bulk(target - n)
                     for n in range(2, target - 1))
    mixed_pairs = 2 * sum(bulk(target - p) for p in primes
                          if p <= target - 2)
    small_pairs = sum(target - p in small for p in primes
                      if 2 <= p <= target - 2)
    return {"target": target, "cutoff": cutoff, "modulus": modulus,
            "bulk_pairs": bulk_pairs, "mixed_pairs": mixed_pairs,
            "small_pairs": small_pairs,
            "total": bulk_pairs + mixed_pairs + small_pairs,
            "exact_prime_cutoff": cutoff >= isqrt(target - 2)}


def sum_histogram(labels) -> dict[int, int]:
    values = tuple(labels)
    for value in values:
        po.integer(value)
    return dict(sorted(Counter(a + b for a in values for b in values).items()))


def difference_histogram(labels) -> dict[int, int]:
    values = tuple(labels)
    for value in values:
        po.integer(value)
    return dict(sorted(Counter(a - b for a in values for b in values).items()))


HOMOMETRIC_A = (2, 3, 6, 12, 14, 19)
HOMOMETRIC_B = (2, 3, 10, 13, 15, 19)
MOD30_SWAPPED_PRIMES = (7, 11, 13, 17, 19, 23)
MOD30_PERMUTATION = {p: 31 * p for p in MOD30_SWAPPED_PRIMES}
MOD30_PERMUTATION.update({31 * p: p for p in MOD30_SWAPPED_PRIMES})


def mod30_relabel(n: int) -> int:
    """Finite involution preserving every residue modulo30 and fixing1,2,3,5."""
    po.integer(n, 1)
    return MOD30_PERMUTATION.get(n, n)


def mod30_product(a: int, b: int) -> int:
    return mod30_relabel(mod30_relabel(a) * mod30_relabel(b))


def residue_degree_histogram(window: int, modulus: int, *, transported=False) -> dict:
    po.integer(window, 2)
    po.integer(modulus, 1)
    if type(transported) is not bool:
        raise ValueError("transported must be boolean")
    return dict(sorted(Counter((n % modulus,
                                omega(mod30_relabel(n) if transported else n))
                               for n in range(2, window + 1)).items()))
