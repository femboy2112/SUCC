"""Separate exact controls for the declared adaptive-boundary probes.

Arithmetic grades are built by trial factorization and prime targets by
trial divisibility. Integer annihilators are rebuilt by elementary symmetric
sums, not the production polynomial multiplier. Results remain finite.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt, prod

import complex_banks as cb
import integer_information as ii
import pointwise_certificates as pc


MIDPOINTS = (67, 263, 521, 1033)
DEGREES = (2, 4, 6)


def _rational(value):
    if type(value) not in (int, F):
        raise ValueError("exact integer or Fraction required")
    return F(value)


def _ceil(value):
    return -((-value.numerator) // value.denominator)


def aperture_certificate(mass, damping, interval):
    """Necessary integer-target bracket from ONE authentic response interval.

    Assumes nonnegative integer grades, integral c_0, and total mass <= mass.
    No source/interval authentication or full moment-feasibility test occurs.
    A nonsingleton bracket is returned as unresolved, not guessed.
    """
    if type(mass) is not int or mass < 0:
        raise ValueError("nonnegative integer mass bound required")
    s = _rational(damping)
    if not 0 < s < 1:
        raise ValueError("damping must lie strictly between zero and one")
    interval = tuple(interval)
    if len(interval) != 2:
        raise ValueError("two exact interval endpoints required")
    lo, hi = map(_rational, interval)
    if lo > hi:
        raise ValueError("reversed interval")
    lower = max(0, _ceil(lo - mass * s))
    upper = min(mass, hi.numerator // hi.denominator)
    if lower > upper:
        raise ValueError("packet contradicts the necessary integer target bounds")
    return {
        "integer_lower": lower,
        "integer_upper": upper,
        "count_recovered": lower == upper,
        "uniform_width_budget": str(hi - lo + mass * s),
        "source_and_integrality_promises_required": True,
    }


def trial_omega(value):
    remaining, answer, divisor = value, 0, 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            answer += 1
            remaining //= divisor
        divisor += 1
    return answer + int(remaining > 1)


def trial_prime(value):
    return value >= 2 and all(value % d for d in range(2, isqrt(value) + 1))


def source_histogram(midpoint):
    grades = [trial_omega(midpoint - a) + trial_omega(midpoint + a) - 2
              for a in range(midpoint - 1)]
    return tuple(grades.count(h) for h in range(max(grades) + 1))


def response(histogram, node):
    return sum((count * node ** h for h, count in enumerate(histogram)), F())


def interpolation_weights(degree):
    nodes = [F(1, 2 ** r) for r in range(1, degree + 1)]
    return tuple(prod((-nodes[j] / (nodes[i] - nodes[j])
                       for j in range(degree) if i != j), start=F(1))
                 for i in range(degree))


def integer_controls():
    rows = []
    for base, d in product((2, 3, 5), range(1, 7)):
        roots = (1,) + tuple(base ** r for r in range(1, d + 1))
        coefficients = tuple((-1) ** k * sum(prod(group) for group in combinations(roots, k))
                             for k in range(len(roots) + 1))
        assert coefficients == ii.annihilator(base, d)
        left = tuple(max(x, 0) for x in coefficients)
        right = tuple(max(-x, 0) for x in coefficients)
        mass = sum(left)
        assert mass == sum(right) == prod(1 + base ** r for r in range(1, d + 1))
        assert left[0] - right[0] == 1
        for r in range(d + 1):
            assert response(left, F(1, base ** r)) == response(right, F(1, base ** r))
        assert mass >= base ** (d * (d + 1) // 2) + 1
        rows.append({"base": base, "channels": d, "mass": mass,
                     "equal_response_coordinates_including_mass": d + 1})
    left, right = (1, 0, 7, 6, 0), (0, 6, 0, 0, 8)
    assert sum(left) == sum(right) == 14
    assert [response(left, F(1, 2 ** r)) for r in (1, 2)] == [F(7, 2), F(49, 32)]
    assert all(response(left, F(1, 2 ** r)) == response(right, F(1, 2 ** r))
               for r in (1, 2))
    return {"construction": "elementary symmetric sums; distinct from production multiplication",
            "product_witnesses": rows, "improved_two_channel_witness_mass": 14}


def phase_prefix_controls():
    rows = []
    for cutoff in (8, 32, 64):
        delta = F(1, 4) * F(2, 3) ** cutoff
        bank = cb.Bank(((cb.Gaussian(F(1, 4)), cb.Gaussian(2 - delta)),
                        (cb.Gaussian(F(1, 2)), cb.Gaussian(-1)),
                        (cb.Gaussian(F(-3, 4)), cb.Gaussian(delta))))

        def direct(h):
            return (2 - delta) * F(1, 4) ** h - F(1, 2) ** h + delta * F(-3, 4) ** h

        assert direct(0) == bank.evaluate(0) == 1
        assert all(direct(h) < 0 for h in range(1, cutoff + 1))
        assert direct(cutoff + 4) > 0
        assert all(direct(h) == bank.evaluate(h) for h in range(cutoff + 5))
        first = bank.first_positive_grade(cutoff + 4)
        assert cutoff < first <= cutoff + 4
        rows.append({"passing_prefix": cutoff, "delta": str(delta),
                     "first_positive_grade": first,
                     "declared_failure_grade": cutoff + 4,
                     "response_at_declared_failure": str(direct(cutoff + 4)),
                     "outer_positive_real_coefficient": str(bank.dominant_circle()["positive_real_coefficient"])})
    return {"scope": "designed rational negative-node traps; no global minorant certification",
            "entries": rows}


def aperture_controls():
    cases = 0
    for hist in product(range(3), repeat=5):
        mass = sum(hist)
        if not mass:
            continue
        node = F(1, 4 * mass)
        exact = response(hist, node)
        assert exact.numerator // exact.denominator == hist[0]
        for noise in (F(-1, 4), F(), F(1, 4)):
            reported = exact + noise
            cert = aperture_certificate(mass, node, (reported - F(1, 4), reported + F(1, 4)))
            assert cert["integer_lower"] == cert["integer_upper"] == hist[0]
            cases += 1
    # Three concrete failures of dropped hypotheses.
    nonintegral_target = (F(1, 2),)
    assert response(nonintegral_target, F(1, 2)).__floor__() != nonintegral_target[0]
    assert response((0, 2), F(1, 2)).__floor__() == 1  # M*s=1, true count zero.
    authentic = response((1, 0, 0, 1), F(1, 8))
    noisy_center = authentic - F(1, 100)
    assert noisy_center.__floor__() == 0  # A noisy center cannot simply be floored.
    cert = aperture_certificate(2, F(1, 8), (noisy_center - F(1, 100), noisy_center + F(1, 100)))
    assert cert["integer_lower"] == cert["integer_upper"] == 1
    # An upper mass bound does not supply an unknown normalization scale.
    assert response((1,), F(1, 8)) / 1 == response((2,), F(1, 8)) / 2 == 1
    assert (1,)[0] != (2,)[0]
    for args in ((True, F(1, 2), (0, 1)), (2, 0.5, (0, 1)),
                 (2, F(1, 2), (2, 1)), (2, F(1, 8), (F(1, 2), F(1, 2)))):
        try:
            aperture_certificate(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid aperture packet was accepted")
    return {"histogram_noise_cases": cases,
            "mutation_controls": ["noninteger target", "M*s equals one", "flooring noisy center",
                                  "omitted actual normalization mass"],
            "damping_rule": "1/(4M)", "raw_error_radius": "1/4",
            "scope": "synthetic exact finite controls, not arithmetic asymptotics"}


def arithmetic_controls():
    rows = []
    aperture_rows = []
    for midpoint in MIDPOINTS:
        hist = source_histogram(midpoint)
        direct_count = sum(trial_prime(midpoint - a) and trial_prime(midpoint + a)
                           for a in range(midpoint - 1))
        assert hist[0] == direct_count
        assert sum(hist) == midpoint - 1
        for degree in DEGREES:
            nodes = tuple(F(1, 2 ** r) for r in range(1, degree + 1))
            values = tuple(response(hist, node) for node in nodes)
            weights = interpolation_weights(degree)
            filtered = sum((a * value for a, value in zip(weights, values)), F())
            assert filtered == pc.filtered_response(hist, degree)
            assert filtered == cb.bank_response(cb.damped_minorant(degree), midpoint)
            eps = F(1, 2 ** (degree * (degree + 1) // 2))
            assert direct_count - eps * (sum(hist) - direct_count) <= filtered <= direct_count
            integer_lower = max(0, _ceil(filtered))
            real_upper = min(F(sum(hist)), (filtered + eps * sum(hist)) / (1 + eps))
            integer_upper = real_upper.__floor__()
            assert integer_lower <= direct_count <= integer_upper
            strict = eps * (midpoint - 2) < 1
            recovered = pc.recover_integer_count(filtered, midpoint - 1, degree) if strict else None
            if strict:
                assert recovered == direct_count
            rows.append({"midpoint": midpoint, "degree": degree, "histogram": hist,
                         "direct_unordered_count": direct_count,
                         "responses": [str(x) for x in values],
                         "filtered_response": str(filtered), "positive": filtered > 0,
                         "integer_interval_from_observed_packet": [integer_lower, integer_upper],
                         "observed_packet_recovers_count": integer_lower == integer_upper,
                         "sharp_mass_completeness_budget_met": strict,
                         "recovered_count_under_budget": recovered})
        mass = midpoint - 1
        node = F(1, 4 * mass)
        value = response(hist, node)
        cert = aperture_certificate(mass, node, (value - F(1, 4), value + F(1, 4)))
        assert cert["integer_lower"] == cert["integer_upper"] == direct_count
        aperture_rows.append({"midpoint": midpoint, "node": str(node),
                              "response": str(value), "direct_unordered_count": direct_count,
                              "certificate": cert})
    return {"scope": "four preregistered midpoints; independent finite arithmetic wiring check",
            "midpoints": MIDPOINTS, "degrees": DEGREES,
            "damped_certificates": rows, "single_channel_certificates": aperture_rows,
            "Goldbach_proved": False, "asymptotic_theorem_tested": False}


def report():
    return {"integer_audit": integer_controls(),
            "phase_prefix_audit": phase_prefix_controls(),
            "aperture_audit": aperture_controls(),
            "arithmetic_audit": arithmetic_controls()}


if __name__ == "__main__":
    import json
    print(json.dumps(report(), indent=2, sort_keys=True))
