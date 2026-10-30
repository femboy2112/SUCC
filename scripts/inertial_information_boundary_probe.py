#!/usr/bin/env python3
"""Exact source/preparation probe and rational certificates for binary KL.

All logarithm enclosures come from a proved positive-series remainder.
Displayed decimals are directed rational roundings, not floating verdicts.
Universal analytic claims require the accompanying paper proofs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ import inertial_information_boundary as model


def _add(a, b):
    return a[0]+b[0], a[1]+b[1]


def _scale(a, c):
    return (a[0]*c, a[1]*c) if c >= 0 else (a[1]*c, a[0]*c)


def _subtract(a, b):
    return a[0]-b[1], a[1]-b[0]


def _series_log(y, terms):
    if not F(1) <= y <= F(2):
        raise ValueError("normalized log argument outside [1,2]")
    t = (y-1)/(y+1)
    power, total = t, F()
    for j in range(terms):
        total += 2*power/(2*j+1)
        power *= t*t
    remainder = 2*power/((2*terms+1)*(1-t*t))
    return total, total+remainder


@lru_cache(maxsize=16)
def _ln_two(terms):
    return _series_log(F(2), terms)


def log_interval(x, terms=24):
    """Enclose natural log of an exact positive rational with exact endpoints."""
    if type(x) not in (int, F) or x <= 0:
        raise ValueError("positive exact rational required")
    if type(terms) is not int or terms < 1:
        raise ValueError("positive integer term count required")
    x = F(x)
    k = x.numerator.bit_length()-x.denominator.bit_length()
    y = x/(F(2)**k)
    while y < 1:
        y *= 2
        k -= 1
    while y >= 2:
        y /= 2
        k += 1
    return _add(_series_log(y, terms), _scale(_ln_two(terms), k))


def binary_kl_interval(q, epsilon, terms=24):
    q, epsilon = F(q), F(epsilon)
    if not 0 <= q <= 1 or not 0 < epsilon < 1:
        raise ValueError("binary KL requires q in [0,1], epsilon in (0,1)")
    result = (F(), F())
    if q:
        result = _add(result, _scale(log_interval(q/epsilon, terms), q))
    if q != 1:
        result = _add(result, _scale(
            log_interval((1-q)/(1-epsilon), terms), 1-q))
    return result


def finite_kl_interval(q, p, terms=24):
    q, p = tuple(map(F, q)), tuple(map(F, p))
    if len(q) != len(p) or sum(q) != 1 or sum(p) != 1:
        raise ValueError("normalized equally sized probability arrays required")
    if any(x < 0 for x in q) or any(x <= 0 for x in p):
        raise ValueError("nonnegative law and strictly positive reference required")
    answer = (F(), F())
    for x, y in zip(q, p):
        if x:
            answer = _add(answer, _scale(log_interval(x/y, terms), x))
    return answer


def maximal_leakage_bracket(epsilon, budget, iterations=36):
    """Certified rational bracket for max q with binary KL(q||epsilon)<=B."""
    epsilon, budget = F(epsilon), F(budget)
    if not 0 < epsilon < 1 or budget < 0:
        raise ValueError("interior reference mass and nonnegative budget required")
    if budget == 0:
        return epsilon, epsilon
    cutoff = log_interval(1/epsilon)
    if budget >= cutoff[1]:
        return F(1), F(1)
    if budget >= cutoff[0]:
        raise ArithmeticError("cutoff needs a tighter certificate")
    low, high = epsilon, F(1)
    low_certificate, high_certificate = (F(), F()), cutoff
    for _ in range(iterations):
        middle = (low+high)/2
        for terms in (24, 48, 96):
            lower, upper = binary_kl_interval(middle, epsilon, terms)
            if upper < budget:
                low = middle
                low_certificate = lower, upper
                break
            if lower > budget:
                high = middle
                high_certificate = lower, upper
                break
        else:
            raise ArithmeticError("certified bisection could not decide a side")
    assert low_certificate[1] <= budget
    assert high_certificate[0] >= budget
    return low, high


def _decimal(value, places=12, *, upward=False):
    scale = 10**places
    raw = value*scale
    integer = (-((-raw.numerator)//raw.denominator) if upward
               else raw.numerator//raw.denominator)
    sign = "-" if integer < 0 else ""
    whole, fraction = divmod(abs(integer), scale)
    return f"{sign}{whole}.{fraction:0{places}d}"


def display_interval(interval):
    return {"lower": _decimal(interval[0]),
            "upper": _decimal(interval[1], upward=True),
            "rounding": "outward from exact rational endpoints"}


def run():
    checks = Counter()
    examples = {}
    for value in (0, -1, -16, 1, 16):
        encoded = model.signed_integer_encode(value)
        assert model.signed_integer_decode(encoded) == value
        assert len(encoded) == model.signed_integer_code_length(value)
        checks["framed_code_examples"] += 2
        examples[str(value)] = {"code": encoded, "bits": len(encoded)}
    for word, value, cost in (("", 0, 0), ("-", -1, 1), ("-R", -16, 1),
                              ("RNRN", 0, 0), ("+-", 0, 2)):
        item = model.evaluate_preparation(word)
        assert item["seed"] == value and item["cost"] == cost
        checks["preparation_vs_description"] += 1
    for base in (2, 3, 10, 16, 27):
        for h in (-7, 1, 5):
            for delta in map(F, (-16, -1, 0, 1, F(1, 16), F(1, 256), F(1, 3), F(-7, 40))):
                for n in (0, 1, 2, 5, 37, 61, 97):
                    direct = (h*base**n*delta) % 1
                    assert model.seed_phase_residue(delta, n, frequency=h, base=base) == direct
                    checks["heldout_phase_quotient"] += 1
    for n in (37, 61, 97):
        a = 8*n-7
        raw = F(4, a)-F(2, a+3)-F(1, a+4)-F(1, a+5)
        hist = model.authentic_source_history(n)
        assert hist[n]-16*hist[n-1] == raw
        assert model.homogeneous_charge(
            [F(4,8*k-7)-F(2,8*k-4)-F(1,8*k-3)-F(1,8*k-2)
             for k in range(1,n+1)], hist[n], n) == 0
        checks["authentic_source_and_charge"] += 2

    kl_cases = []
    ln2 = log_interval(2)
    assert log_interval(1) == (F(), F())
    for k in (4, 8, 16, 32, 64):
        epsilon = F(1, 2**k)
        log_inverse = log_interval(1/epsilon)
        for q in sorted({F(), epsilon/2, epsilon, 2*epsilon,
                         F(1,4), F(1,2), F(3,4), F(1)}):
            result = binary_kl_interval(q, epsilon)
            assert result[0] >= 0
            rhs = _subtract(_scale(log_inverse, q), ln2)
            assert result[0] >= rhs[1]
            checks["certified_binary_kl_and_boundary_bound"] += 2
            kl_cases.append({"epsilon": str(epsilon), "q": str(q),
                             "kl_nats": display_interval(result)})

    reference = (F(1,4), F(1,2), F(1,10), F(3,20))
    updated = (F(3,20), F(9,20), F(4,15), F(2,15))
    direct = finite_kl_interval(updated, reference)
    binary = binary_kl_interval(F(2,5), F(1,4))
    neutral = finite_kl_interval((F(1,4), F(3,4)), (F(1,3), F(2,3)))
    outside = finite_kl_interval((F(2,3), F(1,3)), (F(2,5), F(3,5)))
    chain = _add(binary, _add(_scale(neutral, F(3,5)), _scale(outside, F(2,5))))
    residual = _subtract(direct, chain)
    assert residual[0] <= 0 <= residual[1]
    omitted = _subtract(direct, binary)
    assert omitted[0] > 0
    checks["certified_kl_chain_rule"] += 1
    checks["omitted_conditional_information_mutant_rejected"] += 1

    # An audit found a possible false failure if a fine accepted endpoint
    # were rechecked with the default coarser enclosure. Retain its receipt.
    midpoint, reference_mass = F(5, 8), F(1, 4)
    coarse = binary_kl_interval(midpoint, reference_mass, 24)
    fine = binary_kl_interval(midpoint, reference_mass, 48)
    regression_budget = (coarse[1]+fine[1])/2
    assert fine[1] < regression_budget < coarse[1]
    regression_bracket = maximal_leakage_bracket(
        reference_mass, regression_budget, iterations=1)
    assert regression_bracket == (midpoint, F(1))
    assert binary_kl_interval(regression_bracket[0], reference_mass)[1] > regression_budget
    checks["retained_endpoint_precision_regression"] += 3

    optimum = []
    for k in (4, 8, 16, 32, 64):
        epsilon = F(1, 2**k)
        log_inverse = log_interval(1/epsilon)
        for budget in (F(), F(1,8), F(1), F(4)):
            bracket = maximal_leakage_bracket(epsilon, budget)
            upper_bound = min(F(1), (budget+ln2[1])/log_inverse[0])
            assert bracket[1] <= upper_bound
            checks["certified_maximum_leakage_brackets"] += 1
            optimum.append({"epsilon": str(epsilon), "budget_nats": str(budget),
                "maximal_nonneutral_probability": display_interval(bracket),
                "rational_bracket": [str(z) for z in bracket],
                "q_times_log_inverse_epsilon": display_interval(
                    (bracket[0]*log_inverse[0], bracket[1]*log_inverse[1]))})

    return {"schema": "succ.inertial-information-boundary.production-probe.v1",
        "status": "passed", "parent_commit": "b6a3815ceb505de0b1f570eae3ff5be75cdbe99c",
        "checks": dict(checks), "check_total": sum(checks.values()),
        "code_examples": examples,
        "log_certificate": {"arithmetic": "fractions.Fraction only",
            "series": "2 sum_{j<m} t^(2j+1)/(2j+1)",
            "remainder_upper": "2 t^(2m+1)/((2m+1)(1-t^2))",
            "normalization": "x=2^k y, 1<=y<2, t=(y-1)/(y+1)",
            "default_terms": 24, "floating_point_verdicts": 0},
        "binary_kl_cases": kl_cases, "optimal_leakage_cases": optimum,
        "conditional_information_mutant": {"status": "rejected",
            "positive_missing_cost": display_interval(omitted)},
        "interval_audit_regression": {"status": "passed",
            "epsilon": "1/4", "midpoint": "5/8",
            "budget": "midpoint of the 24-term and 48-term certified upper KL bounds",
            "fine_endpoint_accepted": True,
            "coarse_recheck_would_falsely_reject": True,
            "fix": "preserve the accepted endpoint enclosure and its precision"},
        "scope": {"finite_certificates": "exact rational enclosure checks",
            "universal_results": "paper proofs; finite checks are not their infinite lift",
            "physical_inertia": "HYPOTHESIS", "selected_BBP_cancellation": "OPEN"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    rendered = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(rendered)
    print(json.dumps({"status": report["status"], "check_total": report["check_total"],
                      "floating_point_verdicts": 0,
                      "output": str(args.output) if args.output else None}))
    if not args.output:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
