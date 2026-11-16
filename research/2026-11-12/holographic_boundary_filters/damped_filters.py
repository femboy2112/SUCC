"""Stable finite lower filters for integer grade zero, with no grade ceiling.

Exact rational arithmetic. The response oracle is an input hypothesis;
the arithmetic demo computes it by ordinary finite factorization. This is
not an all-midpoint Goldbach estimate or a speedup assertion.
"""
from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path

from goldbach_filters import prime_grade_histogram, direct_goldbach_count


MIDPOINTS = (10, 257, 509, 1021, 2053, 4099)
DEGREES = (2, 4, 6)


def rational(value):
    if type(value) not in (int, F):
        raise ValueError("exact integer or Fraction required")
    return F(value)


def parameters(degree: int, t: F):
    if type(degree) is not int or degree < 2 or degree % 2:
        raise ValueError("an even integer degree >=2 is required for lower filters")
    t = rational(t)
    if not 0 < t <= F(1,2):
        raise ValueError("the certified leakage regime is 0<t<=1/2")
    return degree, t


def coefficients(degree: int, t: F = F(1,2)) -> tuple[F, ...]:
    """Coefficients a_0,...,a_d of z prod(z-t^j)/prod(1-t^j)."""
    degree, t = parameters(degree, t)
    a = [F(), F(1)]
    for j in range(1, degree):
        root = t**j
        b = [F()]*(len(a)+1)
        for k, value in enumerate(a):
            b[k] -= root*value/(1-root)
            b[k+1] += value/(1-root)
        a = b
    return tuple(a)


def polynomial(a, z):
    z = rational(z)
    result = F()
    for x in reversed(a):
        result = result*z+rational(x)
    return result


def leakage(degree: int, t: F = F(1,2)) -> F:
    degree, t = parameters(degree, t)
    return t**(degree*(degree+1)//2)


def response(histogram, t: F) -> F:
    t = rational(t)
    if not 0 < t < 1:
        raise ValueError("response parameter must be in (0,1)")
    result = F()
    for h, count in enumerate(histogram):
        count = rational(count)
        if count < 0:
            raise ValueError("nonnegative grade masses required")
        result += count*t**h
    return result


def certificate(mass, intervals, degree: int, t: F = F(1,2), *, integral_counts=False):
    """Return a conditional interval for zero mass from responses F(t^r).

    Each supplied interval must enclose its genuine response and mass must
    bound the genuine total mass from above. Integral-count conclusions use
    the explicit extra promise that c_0 is an integer.
    """
    mass = rational(mass)
    if mass < 0 or type(integral_counts) is not bool:
        raise ValueError("nonnegative mass budget and boolean count promise required")
    a = coefficients(degree, t)
    if len(intervals) != degree:
        raise ValueError("one interval for every F(t^r), r=1,...,d, required")
    lo_sum = hi_sum = F()
    for weight, pair in zip(a[1:], intervals):
        if len(pair) != 2:
            raise ValueError("two rational endpoints required")
        lo, hi = map(rational, pair)
        if lo > hi:
            raise ValueError("reversed response interval")
        lo_sum += weight*(lo if weight >= 0 else hi)
        hi_sum += weight*(hi if weight >= 0 else lo)
    eps = leakage(degree, t)
    lower = max(F(), lo_sum)
    upper = min(mass, (hi_sum+eps*mass)/(1+eps))
    if upper < lower:
        raise ValueError("packet contradicts the declared nonnegative grade model")
    result = {"degree": degree, "t": str(t),
              "weights": [str(x) for x in a[1:]],
              "coefficient_l1": str(sum(map(abs,a),F())),
              "leakage_per_unit_mass": str(eps), "mass_budget": str(mass),
              "filtered_lower": str(lo_sum), "filtered_upper": str(hi_sum),
              "zero_mass_lower": str(lower), "zero_mass_upper": str(upper),
              "positive": lower > 0,
              "source_and_response_authentication_required": True}
    if integral_counts:
        integer_lower = -((-lower.numerator)//lower.denominator)
        integer_upper = upper.numerator//upper.denominator
        if integer_lower > integer_upper:
            raise ValueError("packet contradicts the integral-count promise")
        result.update(integer_lower=integer_lower, integer_upper=integer_upper,
                      count_recovered=integer_lower == integer_upper)
    return result


def histogram_certificate(histogram, degree: int, t: F = F(1,2), error: F = F()):
    """Convenience wrapper for actual nonnegative INTEGER count histograms.

    General real masses should use response() and certificate() without the
    integral-count promise. Nonintegral inputs must not be silently rounded.
    """
    histogram = tuple(histogram)
    if any(type(count) is not int or count < 0 for count in histogram):
        raise ValueError("the count wrapper requires nonnegative exact integers")
    error = rational(error)
    if error < 0:
        raise ValueError("nonnegative uncertainty required")
    _, t = parameters(degree, t)
    values = [response(histogram, t**r) for r in range(1, degree+1)]
    intervals = [(value-error,value+error) for value in values]
    return certificate(sum(histogram), intervals, degree, t, integral_counts=True)


def report():
    rows=[]
    for n in MIDPOINTS:
        histogram=prime_grade_histogram(n)
        direct=direct_goldbach_count(n)
        for degree in DEGREES:
            item=histogram_certificate(histogram,degree)
            item.update(midpoint=n, direct_unordered_count=direct,
                        response_values=[str(response(histogram, F(1,2)**r))
                                         for r in range(1, degree+1)])
            rows.append(item)
    return {"scope":"exact finite arithmetic evaluation; no all-midpoint estimate",
            "midpoints":list(MIDPOINTS), "degrees":list(DEGREES),
            "entries":rows, "Goldbach_proved":False}


if __name__ == "__main__":
    result=report()
    path=Path(__file__).with_name("DAMPED_RESULTS.json")
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"artifact":path.name,"certificates":len(result['entries']),
                      "positive":sum(x['positive'] for x in result['entries']),
                      "exact_count_recovered":sum(x['count_recovered'] for x in result['entries']),
                      "Goldbach_proved":False},sort_keys=True))
