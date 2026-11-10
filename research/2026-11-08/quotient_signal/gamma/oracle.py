"""Exact rational checks for the declared Green-tail Gamma calibration.

No pi digits, Gamma evaluator or floating-point value constructs the source.
The source, tail and constant intervals are computed independently. All
asymptotic authority belongs to THEOREMS.md, not these finite observations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
from pathlib import Path

def _positive_int(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")


@lru_cache(None)
def source(n):
    _positive_int(n)
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def source_integral(n):
    """Independent integral expansion of (1-x)*Q(x)."""
    _positive_int(n)
    q = (4, 4, 4, 2, 1)
    return sum((F(c, 8*(n-1)+k+1)-F(c, 8*(n-1)+k+2)
                for k, c in enumerate(q)), F())


def tail_interval(n, depth=24):
    _positive_int(n)
    _positive_int(depth)
    lower = sum((source(n+j)/16**j for j in range(1, depth+1)), F())
    # Remainder =16^-depth*T_(n+depth), with T_m<1/(64*m^2).
    return lower, lower+F(1, 16**depth*64*(n+depth)**2)


def _add(x, y):
    return x[0]+y[0], x[1]+y[1]


def _scale(x, q):
    endpoints = (x[0]*q, x[1]*q)
    return min(endpoints), max(endpoints)


def _mul(x, y):
    values = [a*b for a in x for b in y]
    return min(values), max(values)


def _sub(x, y):
    return x[0]-y[1], x[1]-y[0]


def _atan_inv(q, terms=80):
    value = sum((F((-1)**j, (2*j+1)*q**(2*j+1))
                 for j in range(terms)), F())
    next_term = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(value, value+next_term), max(value, value+next_term)


@lru_cache(None)
def pi_interval():
    # Machin's identity; alternating remainder independently bounds each atan.
    return _sub(_scale(_atan_inv(5), 16), _scale(_atan_inv(239), 4))


def _log_unit(x, terms=52):
    """x in [1,2]; positive atanh series with a geometric remainder."""
    if not F(1) <= x <= F(2):
        raise ValueError("unit log range required")
    z = (x-1)/(x+1)
    value = 2*sum((z**(2*k+1)/(2*k+1) for k in range(terms)), F())
    error = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return value, value+error


@lru_cache(None)
def log_interval(x):
    x = F(x)
    if x <= 0:
        raise ValueError("positive rational required")
    if x < 1:
        return _scale(log_interval(1/x), -1)
    exponent = 0
    while x >= 2:
        x /= 2
        exponent += 1
    return _add(_log_unit(x), _scale(_log_unit(F(2)), exponent))


@lru_cache(None)
def sqrt2_interval():
    scale = 1 << 160
    lower = isqrt(2*scale*scale)
    assert lower*lower <= 2*scale*scale < (lower+1)**2
    return F(lower, scale), F(lower+1, scale)


@lru_cache(None)
def constant_interval():
    p, s = pi_interval(), sqrt2_interval()
    silver = (log_interval(1+s[0])[0], log_interval(1+s[1])[1])
    part1 = _mul(p, _sub((F(7, 9600), F(7, 9600)), _scale(s, F(7, 1152))))
    part2 = _scale(log_interval(F(2)), F(53, 1440))
    part3 = _scale(_mul(s, silver), -F(7, 576))
    return _add(_add(part1, part2), part3)


@lru_cache(None)
def harmonic(n):
    _positive_int(n)
    return sum((F(1, k) for k in range(1, n+1)), F())


@lru_cache(None)
def gamma_interval(count=4096):
    """Convex-trapezoid theorem: 0<H_m-log(m)-gamma<1/(2m)."""
    h = harmonic(count)
    lo, hi = log_interval(F(count))
    return h-hi-F(1, 2*count), h-lo


def outward_dyadic(interval, bits=128):
    scale = 1 << bits
    lo = interval[0].numerator*scale//interval[0].denominator
    hi = -((-interval[1].numerator*scale)//interval[1].denominator)
    return {"lo": str(lo), "hi": str(hi), "denominator_power2": bits}


def decimal(value, places=24):
    with localcontext() as ctx:
        ctx.prec = places+5
        return str(Decimal(value.numerator)/Decimal(value.denominator))


def _source_hash(limit):
    digest = hashlib.sha256()
    u = F()
    for n in range(limit+1):
        if n:
            u = 16*u+source(n)
        # Hex integers avoid mutating the process-wide decimal safety limit.
        digest.update(f"{n}:{u.numerator:x}/{u.denominator:x}\n".encode())
    return digest.hexdigest()


def run():
    development = (64, 127)
    holdouts = (257, 521, 1031)
    cutoffs = development+holdouts
    depth = 24
    maximum = max(cutoffs)
    c = constant_interval()
    g = gamma_interval()
    q = (F(), F())
    cases = []
    pointwise_checks = 0
    for n in range(1, maximum+1):
        assert source(n) == source_integral(n)
        t = tail_interval(n, depth)
        difference = (F(1, 64*n)-n*t[1], F(1, 64*n)-n*t[0])
        assert 0 < difference[0] <= difference[1] < F(7, 512*n*n)
        pointwise_checks += 1
        q = _add(q, _scale(t, n))
        if n not in cutoffs:
            continue
        h = harmonic(n)
        cn = _sub(q, (h/64, h/64))
        gap = _sub(cn, c)
        assert 0 < gap[0] <= gap[1] < F(7, 512*n)
        estimator = _sub(_scale(_sub(q, c), 64), log_interval(F(n)))
        estimator_gap = _sub(estimator, g)
        assert 0 < estimator_gap[0] <= estimator_gap[1] < F(11, 8*n)
        # Independent finite-boundary backward recurrence. Its T_0 need not
        # equal pi/16; the exact finite completion, not pi, closes this identity.
        terminal = n+depth
        back = [F()]*(terminal+1)
        for k in range(terminal, 0, -1):
            back[k-1] = (back[k]+source_integral(k))/16
        rn = sum((source(k) for k in range(1, n+1)), F())
        an = sum((k*source(k) for k in range(1, n+1)), F())
        sn = sum(back[1:n+1], F())
        qn = sum((k*back[k] for k in range(1, n+1)), F())
        assert rn == 16*back[0]+15*sn-16*back[n]
        assert an == 16*back[0]+15*qn+16*sn-16*(n+1)*back[n]
        back_error = F(1, 64*terminal**2)*sum(
            (F(k, 16**(terminal-k)) for k in range(1, n+1)), F())
        assert max(q[0], qn) <= min(q[1], qn+back_error)
        cases.append({
            "N": n, "role": "development" if n in development else "fresh_holdout",
            "C_N": outward_dyadic(cn), "C_N_minus_C": outward_dyadic(gap),
            "N_times_gap_display": decimal(n*(gap[0]+gap[1])/2),
            "gamma_estimator": outward_dyadic(estimator),
            "gamma_estimator_display": decimal((estimator[0]+estimator[1])/2),
            "gamma_estimator_minus_gamma": outward_dyadic(estimator_gap),
            "gamma_error_upper": str(F(11, 8*n)),
            "sharp_tail_upper": str(F(7, 512*n)),
            "finite_backward_telescoping": True,
            "direct_backward_tail_intersection": True,
            "source_unwrapped_prefix_sha256": _source_hash(n),
        })

    polynomial_checks = 0
    for denominator in (7, 16, 31, 127):
        for numerator in range(denominator+1):
            x = F(numerator, denominator)
            qx = (x*x+2)*(x*x+2*x+2)
            fx = qx/(16-x**8)
            assert 0 <= 1-fx <= 2*(1-x)
            polynomial_checks += 1

    # The original source selection remains literal zero, with mutations
    # deliberately typed separately. These are finite algebraic controls.
    seed_checks = 0
    for seed in (F(), F(1, 7), -F(2, 11)):
        u = seed
        original = F()
        for n in range(1, 65):
            u = 16*u+source(n)
            original = 16*original+source_integral(n)
            assert u-original == 16**n*seed
            seed_checks += 1

    mutation_rows = []
    for n in (64, 257, 1031):
        # Mutant first pole 5/(8n-7) adds a strictly positive 1/n tail.
        lower = sum(((source(n+j)+F(1, 8*(n+j)-7))/16**j
                     for j in range(1, depth+1)), F())
        assert lower > F(1, 64*n*n)
        mutation_rows.append({"n": n, "original_n2_tail_upper_rejected": True})

    own_source = Path(__file__).read_bytes()
    theorem = Path(__file__).with_name("THEOREMS.md").read_bytes()
    return {
        "schema": "succ-quotient-gamma-calibration-v1",
        "parent": "a974db527c19708006b9f6d7f0ca01d08d1e0524",
        "arithmetic": "Fraction plus proved outward rational intervals; decimals supplementary",
        "source_prefix_hash_encoding": "n:hex(numerator)/hex(denominator), newline; literal zero included",
        "depth": depth, "constant_C": outward_dyadic(c),
        "constant_C_display": decimal((c[0]+c[1])/2),
        "gamma_interval": outward_dyadic(g),
        "gamma_interval_definition": "H_4096-log(4096)-1/8192 < gamma < H_4096-log(4096)",
        "sharp_tail_coefficient": "7/512",
        "cases": cases, "pointwise_checks": pointwise_checks,
        "polynomial_checks": polynomial_checks,
        "seed_checks": seed_checks, "mutated_four_pole_controls": mutation_rows,
        "phase_product_limit": "e(-h*(C+gamma/64))",
        "phase_product_error": "11*pi*abs(h)/(256*N), h fixed nonzero integer",
        "phase_product_authority": "paper theorem; no floating complex products used as proof",
        "covariance_bridge": "OPEN",
        "normality_proved": False, "formal_kernel_claim": False,
        "oracle_sha256": hashlib.sha256(own_source).hexdigest(),
        "theorem_sha256": hashlib.sha256(theorem).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    output = json.dumps(payload, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(output)
        print(json.dumps({"output": str(args.output), "cases": len(payload["cases"]),
                          "pointwise_checks": payload["pointwise_checks"],
                          "polynomial_checks": payload["polynomial_checks"],
                          "seed_checks": payload["seed_checks"], "status": "PASS_FINITE"}))
    else:
        print(output, end="")
