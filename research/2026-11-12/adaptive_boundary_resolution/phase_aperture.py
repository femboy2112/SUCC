"""Exact Q(i) controls for classical angular coefficient extraction.

The general root-of-unity theorem is proved in PHASE_APERTURE.md. Here only
four phases are represented explicitly. report() is deterministic, returns
JSON-serializable data, runs its own finite assertions, and writes no files.
Source authenticity, total mass, and any support ceiling remain hypotheses.
"""
from fractions import Fraction as Q
from math import isqrt

from complex_banks import (
    Gaussian, I, ZERO, Bank, natural, rational,
    omega_sieve, source_response, bank_response,
)


def radius(value, *, allow_unit=False):
    value = rational(value)
    if not 0 < value <= 1 or (value == 1 and not allow_unit):
        raise ValueError("radius must lie in (0,1), or at the declared unit endpoint")
    return value


def histogram(value):
    result = tuple(rational(count) for count in value)
    if any(count < 0 for count in result):
        raise ValueError("nonnegative masses are required")
    return result


def alias_average(counts, R=Q(1, 2), points=4):
    """Exact surviving-grade expression, valid for any integer phase count."""
    counts, R = histogram(counts), radius(R, allow_unit=True)
    natural(points, 1)
    return sum((count * R**h for h, count in enumerate(counts) if h % points == 0), Q())


def four_nodes(R=Q(1, 2)):
    R = radius(R, allow_unit=True)
    return (Gaussian(R), R * I, Gaussian(-R), -R * I)


def four_responses(counts, R=Q(1, 2)):
    counts = histogram(counts)
    return tuple(sum((count * z**h for h, count in enumerate(counts)), ZERO)
                 for z in four_nodes(R))


def corrected_lower(average, mass, R=Q(1, 2), points=4):
    average, mass, R = rational(average), rational(mass), radius(R)
    natural(points, 1)
    if mass < 0:
        raise ValueError("nonnegative mass budget required")
    r = R**points
    return (average - r * mass) / (1 - r)


def four_phase_bank(R=Q(1, 2)):
    """Requires exact mass F(1); node 1 carries the negative coefficient."""
    R = radius(R)
    r = R**4
    terms = [(z, Gaussian(1 / (4 * (1 - r)))) for z in four_nodes(R)]
    terms.append((Gaussian(1), Gaussian(-r / (1 - r))))
    return Bank(tuple(terms))


def noisy_interval(average_center, average_error, mass,
                   R=Q(1, 2), points=4):
    """Conditional real interval for c0; average_error bounds |Ahat-A|."""
    center, error, mass = map(rational, (average_center, average_error, mass))
    if error < 0 or mass < 0:
        raise ValueError("nonnegative error and mass budget required")
    lower = max(Q(), corrected_lower(center - error, mass, R, points))
    upper = min(mass, center + error)
    if upper < lower:
        raise ValueError("packet contradicts the declared nonnegative source model")
    return lower, upper


def _json_complex(z):
    return {"real": str(z.real), "imag": str(z.imag)}


def report():
    """Frozen calibration controls; none is an asymptotic or blind holdout."""
    checks = 0

    def check(condition, message):
        nonlocal checks
        if not condition:
            raise AssertionError(message)
        checks += 1

    R, points = Q(1, 2), 4
    bank = four_phase_bank(R)
    check(bank.dominant_circle()["positive_real_coefficient"] == -Q(1, 15),
          "the mass correction must be the negative dominant node")
    alias_histogram = (0, 0, 0, 0, 1)
    alias_responses = four_responses(alias_histogram, R)
    alias = sum(alias_responses, ZERO) / 4
    check(alias == Gaussian(Q(1, 16)), "grade four must alias positively")
    check(alias.real == alias_average(alias_histogram, R, points),
          "four complex responses must match the grade average")
    check(corrected_lower(alias.real, 1, R, points) == 0,
          "mass correction must reject a false zero-grade witness")
    boundary_histogram = (1, 15)
    boundary_average = alias_average(boundary_histogram, R, points)
    check(boundary_average == 1 and corrected_lower(boundary_average, 16, R, points) == 0,
          "the integer witness threshold must be strict")

    # At R=1, all four samples confuse grade zero with grade four.
    check(four_responses((1,), Q(1)) == four_responses(alias_histogram, Q(1)),
          "unit-circle finite samples must retain the high-grade ambiguity")
    check(alias_average((2, 3, 5, 7), Q(1), 4) == 2,
          "an authenticated ceiling H<4 must remove every nonzero alias")

    # A tiny downward observation error invalidates raw floor(Ahat).
    noisy_center, noisy_error = Q(99, 100), Q(1, 100)
    interval = noisy_interval(noisy_center, noisy_error, 1, R, points)
    check(noisy_center.numerator // noisy_center.denominator == 0,
          "the noisy-floor mutant must actually lose the integer")
    check(0 < interval[0] <= 1 <= interval[1] and interval[1] == 1,
          "the validated interval must retain the authentic count one")

    rows = []
    for n in (67, 263):
        omega = omega_sieve(2 * n)
        grades = tuple(omega[n + a] + omega[n - a] - 2 for a in range(n - 1))
        counts = tuple(grades.count(h) for h in range(max(grades) + 1))
        responses = tuple(source_response(z, n) for z in four_nodes(R))
        average = sum(responses, ZERO) / 4
        grade_average = alias_average(counts, R, points)
        corrected = corrected_lower(grade_average, n - 1, R, points)
        direct_count = sum(
            all(m % divisor for divisor in range(2, isqrt(m) + 1))
            and all(k % divisor for divisor in range(2, isqrt(k) + 1))
            for m, k in ((n - a, n + a) for a in range(n - 1))
        )
        check(average == Gaussian(grade_average), "arithmetic complex/grade average mismatch")
        check(corrected == bank_response(bank, n), "mass-corrected bank mismatch")
        check(counts[0] == direct_count, "factorization grading must agree with trial primality")
        check(corrected <= direct_count <= grade_average, "certified bracket failed")
        check(grade_average - direct_count <= R**points * (n - 1 - direct_count),
              "the positive alias budget failed")
        rows.append({
            "midpoint": n,
            "mass": n - 1,
            "radius": str(R),
            "phase_points": points,
            "complex_responses": [_json_complex(z) for z in responses],
            "phase_average": str(grade_average),
            "mass_corrected_lower": str(corrected),
            "actual_zero_count": direct_count,
            "a_priori_grade_ceiling": (n * n).bit_length() - 3,
            "calibration_not_holdout": True,
        })
    return {
        "scope": "Exact finite phase controls; classical algebra; no asymptotic inference.",
        "checks": checks,
        "radius": str(R),
        "phase_points": points,
        "synthetic_grade_four_average": str(alias.real),
        "synthetic_corrected_lower": "0",
        "unit_circle_grade_zero_and_four_indistinguishable": True,
        "strict_budget_boundary": {"mass": 16, "zero_count": 1, "corrected_lower": "0"},
        "noisy_floor_mutant": {
            "center": str(noisy_center), "error": str(noisy_error),
            "raw_floor": 0, "certified_interval": [str(x) for x in interval],
        },
        "arithmetic": rows,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(report(), indent=2, sort_keys=True))
