"""Independent exact integer/Fraction calibration for the local prime waves.

This intentionally imports no code from prime_waves.py. Ramanujan sums are
computed from their integer Mobius divisor formula, while normalized sieve
fields and reflected overlaps are computed by gcd enumeration. This is a
finite calibration, not a universal proof or an independent external review.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


@lru_cache(maxsize=None)
def prime_factors(n: int) -> tuple[int, ...]:
    return tuple(p for p in range(2, n + 1) if n % p == 0 and is_prime(p))


@lru_cache(maxsize=None)
def mobius(n: int) -> int:
    factors = prime_factors(n)
    return 0 if any(n % (p * p) == 0 for p in factors) else (-1) ** len(factors)


@lru_cache(maxsize=None)
def totient(n: int) -> int:
    return sum(gcd(k, n) == 1 for k in range(n))


@lru_cache(maxsize=None)
def ramanujan(d: int, n: int) -> int:
    """Integer divisor formula, with c_1(n)=1 including n=0."""
    return sum(k * mobius(d // k) for k in range(1, d + 1)
               if d % k == 0 and n % k == 0)


def run() -> dict:
    checks = 0
    failures = []
    section_checks: dict[str, int] = {}

    def check(condition: bool, section: str, **case: int) -> None:
        nonlocal checks
        checks += 1
        section_checks[section] = section_checks.get(section, 0) + 1
        if not condition:
            failures.append({"section": section, "case": case})

    moduli = (1, 2, 6, 30, 210)
    for Q in moduli:
        divisors = [d for d in range(1, Q + 1) if Q % d == 0]
        factors = prime_factors(Q)
        field = [Fraction(Q, totient(Q)) * int(gcd(n, Q) == 1)
                 for n in range(Q)]
        for n in range(Q):
            expansion = sum((Fraction(mobius(d), totient(d)) * ramanujan(d, n)
                             for d in divisors), Fraction(0))
            check(field[n] == expansion, "finite_ramanujan_expansion", Q=Q, n=n)
        for N in range(2 * Q):
            count = sum(gcd(n, Q) == gcd(N - n, Q) == 1 for n in range(Q))
            mean = Fraction(count * Q, totient(Q) ** 2)
            local = prod(Fraction(p, p - 1) if N % p == 0 else
                         Fraction(p * (p - 2), (p - 1) ** 2) for p in factors)
            diagonal = sum((Fraction(ramanujan(d, N), totient(d) ** 2)
                            for d in divisors), Fraction(0))
            check(mean == local, "crt_reflected_product", Q=Q, N=N)
            check(mean == diagonal, "ramanujan_reflected_diagonal", Q=Q, N=N)

    Q = 30
    divisors = [d for d in range(1, Q + 1) if Q % d == 0]
    for d in divisors:
        for e in divisors:
            for N in range(Q):
                average = Fraction(sum(ramanujan(d, n) * ramanujan(e, N - n)
                                       for n in range(Q)), Q)
                check(average == (ramanujan(d, N) if d == e else 0),
                      "primitive_denominator_orthogonality", d=d, e=e, N=N)

    for X in range(2, 121):
        z = isqrt(X)
        small_primes = [p for p in range(2, z + 1) if is_prime(p)]
        for n in range(2, X + 1):
            reconstructed = int(all(n % p for p in small_primes)) + int(n in small_primes)
            check(reconstructed == is_prime(n), "adaptive_prime_reconstruction", X=X, n=n)

    for N in range(4, 121):
        z = max(2, isqrt(N - 2))
        interval = range(2, N - 1)
        small_primes = [p for p in interval if p <= z and is_prime(p)]

        def survivor(n: int) -> int:
            return int(n in interval and all(n % p for p in small_primes))

        screened = sum(survivor(n) * survivor(N - n) for n in interval)
        edge = 2 * sum(survivor(N - p) for p in small_primes)
        corner = sum(p + q == N for p in small_primes for q in small_primes)
        actual = sum(is_prime(n) and is_prime(N - n) for n in interval)
        check(screened + edge + corner == actual, "endpoint_corrected_pair_count", N=N)

    valid30 = [n for n in range(30) if gcd(n, 30) == gcd(16 - n, 30) == 1]
    check(valid30 == [17, 23, 29], "interval_countercontrol_period")
    interval_count = sum(gcd(n, 30) == gcd(16 - n, 30) == 1 for n in range(2, 15))
    check(interval_count == 0, "interval_countercontrol_window")

    source = Path(__file__).resolve()
    return {
        "status": "FAIL" if failures else "PASS",
        "checks": checks,
        "failure_count": len(failures),
        "failures": failures,
        "section_checks": section_checks,
        "source_sha256": {source.name: hashlib.sha256(source.read_bytes()).hexdigest()},
        "implementation": "Independent integer Mobius-divisor, gcd, trial-division and Fraction replay; no prime_waves imports.",
        "scope": {
            "moduli": list(moduli),
            "pair_target_range_per_modulus": "Every integer N with 0 <= N < 2Q",
            "primitive_denominator_orthogonality": "Every d,e dividing 30 and every N modulo 30",
            "prime_reconstruction": "Every 2 <= n <= X <= 120, z=isqrt(X)",
            "ordered_pair_reconstruction": "Every integer 4 <= N <= 120, z=max(2,isqrt(N-2))",
            "universal_proof": False,
            "external_or_different_model_review": False,
        },
        "N16_Q30": {
            "period_residues": valid30,
            "normalized_mean": str(Fraction(len(valid30) * 30, totient(30) ** 2)),
            "finite_interval_screened": interval_count,
            "actual_ordered_pairs": sum(is_prime(n) and is_prime(16 - n) for n in range(2, 15)),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent / "receipts" / "WAVE_INDEPENDENT_AUDIT.json")
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "checks": report["checks"],
                      "failures": report["failure_count"], "output": str(args.output)}))
    return int(bool(report["failure_count"]))


if __name__ == "__main__":
    raise SystemExit(main())
