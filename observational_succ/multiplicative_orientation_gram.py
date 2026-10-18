"""Arithmetic versus Archimedean positive Gram completions of the same SUCC/FUCC prime jets.

Finite exact integer/Fraction probes of classical identities. No Weil positivity,
adelic trace, or RH is proved. Read research/2026-10-18/MULTIPLICATIVE_ORIENTATION_GRAM.md.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt


class MultiplicativeGramError(ValueError):
    """Outside exact finite positive integer carrier or declared test domain."""


def _integer(n):
    if type(n) is not int or n < 1 or n > 100_000:
        raise MultiplicativeGramError("positive source integer <= 100000 required")
    return n


def _coefficient(x):
    if type(x) not in (int, Fraction):
        raise MultiplicativeGramError("exact integer or Fraction coefficients required")
    return Fraction(x)


def prime_valuations(n):
    """Genuine unique-factorization prime coordinates; 6 is not a local place."""
    n = _integer(n)
    result = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def totient(n):
    n = _integer(n)
    result = n
    for p in prime_valuations(n):
        result = result // p * (p-1)
    return result


def divisors(n):
    _integer(n)
    smaller, larger = [], []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            smaller.append(d)
            if d*d != n:
                larger.append(n//d)
    return tuple(smaller + list(reversed(larger)))


def overlap(m, n, *, chart="arithmetic"):
    m, n = _integer(m), _integer(n)
    if chart == "arithmetic":
        return gcd(m, n)
    if chart == "archimedean":
        return min(m, n)
    raise MultiplicativeGramError("chart must be arithmetic or archimedean")


def normalized_overlap_squared(m, n, *, chart="arithmetic"):
    """Exact square of the normalized entry K=overlap/sqrt(m*n)."""
    a = overlap(m, n, chart=chart)
    return Fraction(a*a, m*n)


def quadratic_certificate(labels, coefficients, *, chart="arithmetic"):
    """Exact unnormalized Gram quadratic and independent incidence-square oracle.

    Normalized K is a positive diagonal congruence of this exact Gram.
    """
    if type(labels) not in (tuple, list) or not labels or len(labels) > 16:
        raise MultiplicativeGramError("1..16 source labels required")
    if type(coefficients) not in (tuple, list) or len(coefficients) != len(labels):
        raise MultiplicativeGramError("one coefficient per source label required")
    ns = tuple(_integer(n) for n in labels)
    cs = tuple(_coefficient(c) for c in coefficients)
    q = sum((cs[i]*cs[j]*overlap(ns[i], ns[j], chart=chart)
             for i in range(len(ns)) for j in range(len(ns))), Fraction(0))
    if chart == "arithmetic":
        ds = sorted({d for n in ns for d in divisors(n)})
        witness = tuple((d, totient(d),
                         sum((cs[i] for i, n in enumerate(ns) if n % d == 0), Fraction(0)))
                        for d in ds)
    elif chart == "archimedean":
        cuts, prev = sorted(set(ns)), 0
        terms = []
        for t in cuts:
            value = sum((cs[i] for i, n in enumerate(ns) if n >= t), Fraction(0))
            terms.append((t, t-prev, value))
            prev = t
        witness = tuple(terms)
    else:
        raise MultiplicativeGramError("unknown chart")
    squares = sum((w*x*x for _, w, x in witness), Fraction(0))
    if squares != q or q < 0:
        raise AssertionError("independent incidence identity failed")
    return {"chart":chart, "labels":ns, "quadratic":q,
            "positive_sum_of_squares":squares, "feature_receipt":witness,
            "normalized_kernel_PSD_by_congruence":True,
            "completed_Weil_identified":False, "RH_proved":False}


def cross_prime_contrast(m=2, n=3):
    """Difference of two PSD kernels has +/- directions on incomparable pairs."""
    m, n = _integer(m), _integer(n)
    delta = min(m, n) - gcd(m, n)
    return {"labels":(m, n), "unnormalized_offdiagonal_difference":delta,
            "difference_diagonal":(0, 0), "positive_vector_quadratic":2*delta,
            "negative_vector_quadratic":-2*delta,
            "incomparable":m % n != 0 and n % m != 0,
            "both_completions_PSD":True, "Weil_distribution_equated":False}


def log_valuation_negative_type(labels, coefficients):
    """Zero-sum signed coefficients yield a positive prime-filtration energy.

    -1/2 sum_ij c_i*c_j*d(n_i,n_j)
       = sum_p log(p) sum_{h>=0} (sum_{i: v_p(n_i)>h} c_i)^2.
    Return exact nonnegative rational COEFFICIENTS of symbolic log(p).
    The mathematical theorem extends by conjugation to complex coefficients.
    """
    if type(labels) not in (tuple, list) or not labels or len(labels)>32:
        raise MultiplicativeGramError("1..32 source integers required")
    if type(coefficients) not in (tuple, list) or len(coefficients)!=len(labels):
        raise MultiplicativeGramError("matching exact coefficients required")
    ns = tuple(_integer(n) for n in labels)
    cs = tuple(_coefficient(c) for c in coefficients)
    if sum(cs, Fraction(0)) != 0:
        raise MultiplicativeGramError("zero total coefficient required")
    valuations = tuple(prime_valuations(n) for n in ns)
    primes = sorted({p for row in valuations for p in row})
    result = {}
    for p in primes:
        vs = tuple(row.get(p, 0) for row in valuations)
        direct = -Fraction(1, 2)*sum((cs[i]*cs[j]*abs(vs[i]-vs[j])
                                     for i in range(len(ns)) for j in range(len(ns))), Fraction(0))
        squares = sum((sum((cs[i] for i in range(len(ns)) if vs[i]>h),
                           Fraction(0))**2 for h in range(max(vs))), Fraction(0))
        if direct != squares or direct < 0:
            raise AssertionError("valuation negative-type identity failed")
        result[p] = direct
    return {"labels":ns, "prime_log_energy_coefficients":result,
            "positive_on_zero_sum":True, "sum_coefficients":Fraction(0),
            "this_is_completed_Weil_form":False, "RH_proved":False}


def prime_power_projection(n):
    """Genuine prime-power label or None for 1 and multi-prime composites."""
    valuations = prime_valuations(n)
    return next(iter(valuations.items())) if len(valuations)==1 else None


def prime_jet_Weil_weight_contract(n):
    """Arithmetic magnitude at p^k, NOT signed completed Weil distribution.

    K(1,p^k)=p^-k/2 and primitive valuation energy/step is log(p).
    Projecting onto a single-prime jet removes fake composite impulses.
    """
    n = _integer(n)
    pk = prime_power_projection(n)
    if pk is None:
        return {"n":n, "is_prime_power":False, "source_von_mangoldt_weight":0,
                "Weil_signed_distribution_matched":False}
    p, k = pk
    energy = log_valuation_negative_type((1, n), (1, -1))["prime_log_energy_coefficients"]
    if energy != {p:Fraction(k)}:
        raise AssertionError("prime clock valuation inconsistent")
    return {"n":n, "is_prime_power":True, "p":p, "k":k,
            "half_density_amplitude_squared":normalized_overlap_squared(1, n),
            "raw_valuation_energy_coeff_logp":energy[p],
            "primitive_energy_coefficient_logp":energy[p]/k,
            "Weil_weight_symbolic":f"log({p})/sqrt({n})",
            "Weil_signed_distribution_matched":False, "RH_proved":False}


def archimedean_log_discontinuity(n):
    """n/(n+1)->1, but arithmetic K(n,n+1)->0, Arch K(n,n+1)->1."""
    n = _integer(n)
    return {"pair":(n,n+1),
            "arithmetic_normalized_squared":normalized_overlap_squared(n,n+1),
            "archimedean_normalized_squared":normalized_overlap_squared(
                n,n+1,chart="archimedean"),
            "log_gap_ratio":Fraction(n+1,n),
            "same_log_continuous_extension_possible":False}
