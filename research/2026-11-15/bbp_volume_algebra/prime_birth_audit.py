"""Exact finite audit of the original BBP fresh-prime phase obstruction.

No production imports, phase floats, prime-density estimates, or pi oracle.
The universal theorem is in CONSTRUCTOR_NOTES.md. This script checks its
arithmetic premises and explicit local cyclotomic automorphism certificates.
All baseline states use the literal original four poles and U_0 = 0.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import gcd, isqrt, lcm
import json


def require(condition: bool, message: str) -> None:
    """Keep audit checks active even under python -O."""
    if not condition:
        raise AssertionError(message)


def is_prime(p: int) -> bool:
    return type(p) is int and p >= 2 and all(
        p % d for d in range(2, isqrt(p) + 1)
    )


def source_four_poles(n: int) -> Q:
    return (Q(4, 8 * n - 7) - Q(2, 8 * n - 4)
            - Q(1, 8 * n - 3) - Q(1, 8 * n - 2))


def source_combined(n: int) -> Q:
    """Independent single rational expression, coefficients ascending in n."""
    numerator = 16 - 89 * n + 120 * n * n
    denominator = 21 - 206 * n + 712 * n**2 - 1024 * n**3 + 512 * n**4
    return Q(numerator, denominator)


def original_states(steps: int) -> tuple[Q, ...]:
    states = [Q(0)]
    for n in range(1, steps + 1):
        states.append(16 * states[-1] + source_four_poles(n))
    return tuple(states)


def convolution_state(n: int) -> Q:
    return sum(
        (16 ** (n - j) * source_combined(j) for j in range(1, n + 1)),
        Q(0),
    )


def p_valuation(value: Q, p: int) -> int:
    if value == 0:
        raise ValueError("zero has no finite p-valuation")
    numerator, denominator = abs(value.numerator), value.denominator
    result = 0
    while numerator % p == 0:
        numerator //= p
        result += 1
    while denominator % p == 0:
        denominator //= p
        result -= 1
    return result


def p_integral_residue(value: Q, p: int) -> int:
    if value.denominator % p == 0:
        raise ValueError("a p-integral rational is required")
    return value.numerator * pow(value.denominator, -1, p) % p


def local_certificate(p: int, h: int, states: tuple[Q, ...]) -> dict:
    """An exact CRT automorphism witness; h divisible by p is a null control."""
    if not is_prime(p) or p <= 5 or p % 8 != 1:
        raise ValueError("a prime p > 5 congruent to 1 mod 8 is required")
    if type(h) is not int:
        raise TypeError("frequency must be an exact integer")
    birth = (p + 7) // 8
    if len(states) <= birth:
        raise ValueError("state prefix does not reach the proposed birth")
    require(states[0] == 0, "original zero seed was changed")
    require(all(u.denominator % p for u in states[:birth]),
            "the prime was already present before its claimed first birth")
    cofactor = states[birth] - Q(4, p)
    require(cofactor.denominator % p != 0, "birth cofactor is not p-free")
    require(p_valuation(states[birth], p) == -1,
            "the original state does not have the expected simple p-pole")
    require(p_integral_residue(p * states[birth], p) == 4 % p,
            "the original signed first-pole coefficient changed")

    conductor = 1
    for argument in (*[h * u for u in states[:birth]], h * cofactor):
        conductor = lcm(conductor, argument.denominator)
    require(gcd(conductor, p) == 1, "prior phase conductor contains p")

    # The CRT multiplier fixes all M-th roots and sends zeta_p to zeta_p^2.
    exponent = 1 + conductor * pow(conductor, -1, p)
    require(exponent % conductor == 1 % conductor, "CRT M-residue failed")
    require(exponent % p == 2, "CRT p-residue failed")
    require(gcd(exponent, p * conductor) == 1,
            "the exponent does not define a cyclotomic automorphism")
    fixes_earlier = all(
        ((exponent - 1) * h * u).denominator == 1
        for u in states[:birth]
    )
    fixes_cofactor = ((exponent - 1) * h * cofactor).denominator == 1
    shift = ((exponent - 1) * h * states[birth]) % 1
    expected = Q(4 * h, p) % 1
    require(fixes_earlier, "an earlier phase moved")
    require(fixes_cofactor, "the p-free cofactor phase moved")
    require(shift == expected, "the newborn phase moved by the wrong amount")
    require((shift != 0) == (h % p != 0),
            "the local separation test mishandled its frequency hypothesis")
    return {
        "prime": p,
        "birth_time": birth,
        "frequency": h,
        "state_p_valuation": -1,
        "prior_conductor_bits": conductor.bit_length(),
        "prior_conductor_p_free": True,
        "automorphism_fixes_prior_phases": fixes_earlier,
        "automorphism_fixes_cofactor": fixes_cofactor,
        "newborn_argument_shift": str(shift),
        "separates_newborn_phase": shift != 0,
        "coefficient_field_degree_must_be_less_than": p - 1,
    }


def run_audit(max_prime: int = 1024) -> dict:
    if type(max_prime) is not int or not 17 <= max_prime <= 4096:
        raise ValueError("the finite audit budget requires 17 <= max_prime <= 4096")
    primes = tuple(p for p in range(17, max_prime + 1, 8) if is_prime(p))
    steps = (primes[-1] + 7) // 8
    states = original_states(steps)
    for n in range(1, steps + 1):
        require(source_four_poles(n) == source_combined(n),
                f"the two source formulas disagree at time {n}")
    for p in primes:
        birth = (p + 7) // 8
        require(states[birth] == convolution_state(birth),
                f"recurrence and finite convolution disagree at prime {p}")

    frequencies = (1, -3, 16, 17, 257)
    rows = []
    separating = 0
    null = 0
    for p in primes:
        for h in frequencies:
            certificate = local_certificate(p, h, states)
            if certificate["separates_newborn_phase"]:
                separating += 1
            else:
                null += 1
            if h == 1:
                rows.append(certificate)

    # Positive closure control: the unwrapped degree-one output is holonomic.
    for n in range(steps - 1):
        ratio = source_combined(n + 2) / source_combined(n + 1)
        residue = (states[n + 2] - (16 + ratio) * states[n + 1]
                   + 16 * ratio * states[n])
        require(residue == 0, f"the degree-one recurrence failed at time {n}")

    p = 17
    birth = (p + 7) // 8
    require(not local_certificate(p, 0, states)["separates_newborn_phase"],
            "zero frequency falsely separated")
    require(not local_certificate(p, p, states)["separates_newborn_phase"],
            "a frequency divisible by p falsely separated")

    # Mutations are diagnostics outside the original source passport.
    deleted_birth = states[birth] - Q(4, p)
    require(deleted_birth.denominator % p != 0,
            "deleting the first birth pole failed to remove that pole")
    sign_mutant = states[birth] - Q(8, p)
    require(p_integral_residue(p * sign_mutant, p) == (-4) % p,
            "the sign mutation was not actually made")
    require(p_integral_residue(p * sign_mutant, p) != 4 % p,
            "the authentic source passport accepted a sign mutation")
    changed_seed = tuple(u + Q(16**n, p) for n, u in enumerate(states))
    require(changed_seed[0] != 0 and changed_seed[0].denominator % p == 0,
            "the changed-seed control did not violate first-birth hypotheses")
    try:
        local_certificate(p, 1, changed_seed)
    except AssertionError:
        pass
    else:
        raise AssertionError("the changed-seed control was accepted")
    try:
        local_certificate(65, 1, states)
    except ValueError:
        pass
    else:
        raise AssertionError("the composite first-prime candidate was accepted")

    return {
        "status": "PASS",
        "scope": "exact finite arithmetic and local Galois certificates only",
        "source": "original four signed poles; U_0=0; gain 16",
        "max_prime_budget": max_prime,
        "prime_count": len(primes),
        "source_times_cross_checked": steps,
        "independent_convolution_endpoints": len(primes),
        "frequencies_checked": list(frequencies),
        "separating_frequency_prime_pairs": separating,
        "null_frequency_prime_pairs": null,
        "degree_one_recurrence_centers": steps - 1,
        "controls": {
            "zero_frequency": "correctly does not separate",
            "frequency_divisible_by_prime": "correctly does not separate",
            "deleted_first_pole": "simple p-pole disappears",
            "sign_mutation": "authentic coefficient passport rejects",
            "changed_seed": "zero-seed/first-birth hypotheses reject",
            "composite_candidate": "prime hypothesis rejects",
        },
        "certificates_at_frequency_one": rows,
        "universal_nonrecurrence": "proved in notes, not inferred from this run",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-prime", type=int, default=1024)
    arguments = parser.parse_args()
    print(json.dumps(run_audit(arguments.max_prime), indent=2, sort_keys=True))
