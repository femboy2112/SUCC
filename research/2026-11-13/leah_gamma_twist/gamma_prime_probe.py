"""Exact controls for GAMMA_PRIME.md; no numerical normality assertion.

The four-pole implementation below is separate from the imported combined
formula.  Infinite tails and trigonometric quantities are enclosed, never
replaced by floats.  The nonlinear energy-minimum enclosure is a consequence
of the proved branch/projection lemma, not an optimizer's empirical output.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, gcd, isqrt, lcm, prod
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.duck_bbp import forcing as combined_forcing
from observational_succ.bbp_prime_window_signed_intervals import (
    box_phase,
    machin_pi_interval,
)

BASELINE = "db9fb4b84672050efa79b13377f1e73364598a14"
PREREG_SHA256 = "3af86719e304ce8961f7ec4833f798debc5e71bb6ed70f67c95c5d23b5bb599d"
HOLDOUTS = (137, 263, 521, 1031)
OLD_CLOCK_HOLDOUTS = (31, 63, 127)
PRIME_HOLDOUTS = (137, 281, 593)
_U = [Q(0)]
_CLOCK = [1]


def natural(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def integer(value):
    if type(value) is not int:
        raise ValueError("exact integer required")
    return value


def forcing(n):
    natural(n, 1)
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def mutated_forcing(n):
    return forcing(n) + Q(1, 8*n-7)


def _extend(n):
    natural(n)
    while len(_U) <= n:
        j = len(_U)
        r = forcing(j)
        _U.append(16*_U[-1]+r)
        _CLOCK.append(lcm(_CLOCK[-1], r.denominator))


def orbit(n):
    _extend(n)
    return _U[n]


def source_clock(n):
    _extend(n)
    return _CLOCK[n]


def beta_moment(n, q):
    """Integral t^(8n)(1-t)^(q+1) dt, exactly."""
    natural(n, 1)
    natural(q)
    return Q(factorial(q+1), prod(8*n+k for k in range(1, q+3)))


def tail_beta_interval(n, mutated=False):
    i0, i1, i2 = (beta_moment(n, q) for q in range(3))
    lo, hi = i0-2*i1, min(i0, i0-2*i1+4*i2)
    if mutated:
        k_hi = Q(1, 15*(8*n+1))
        lo += k_hi-Q(8, 225)*i0
        hi += k_hi
    return lo, hi


@lru_cache(None)
def tail_series_interval(n, depth=24, mutated=False):
    """Positive monotone-source geometric remainder, independent of beta bound."""
    natural(n, 1)
    natural(depth, 1)
    source = mutated_forcing if mutated else forcing
    partial = sum((source(n+j)/16**j for j in range(1, depth+1)), Q())
    return partial, partial+source(n+depth+1)/(15*16**depth)


def polynomial(coefficients):
    c = tuple(integer(v) for v in coefficients)
    while c and not c[-1]:
        c = c[:-1]
    if not c:
        raise ValueError("nonzero polynomial required")
    return c


def poly_mul(left, right):
    left, right = polynomial(left), polynomial(right)
    result = [0]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return polynomial(result)


def poly_eval(c, value):
    result = 0
    for coefficient in reversed(polynomial(c)):
        result = result*value+coefficient
    return result


def split_one_root(c):
    """Return q,S with P=(z-1)^q S and S(1) != 0."""
    c, q = polynomial(c), 0
    while sum(c) == 0:
        quotient = [0]*(len(c)-1)
        quotient[-1] = c[-1]
        for j in range(len(c)-2, 0, -1):
            quotient[j-1] = c[j]+quotient[j]
        assert -quotient[0] == c[0]
        c, q = polynomial(quotient), q+1
    return q, c


def stencils():
    result = []
    p = (-16, 1)
    for q in range(4):
        result.append(p)
        p = poly_mul(p, (-1, 1))
    return tuple(result)+((-1, 1), (1, 0, 1))


def interval_linear(c, intervals):
    lo = hi = Q()
    for coefficient, (a, b) in zip(c, intervals):
        lo += coefficient*(a if coefficient >= 0 else b)
        hi += coefficient*(b if coefficient >= 0 else a)
    return lo, hi


def lag_tail_certificate(n, c):
    c = polynomial(c)
    q, s = split_one_root(c)
    mass = sum(abs(a) for a in s)
    first = sum(j*abs(a) for j, a in enumerate(s))
    constant = (2+Q(7*q, 2))*mass+8*first
    center = (-1)**q*8**q*sum(s)*beta_moment(n, q)
    error = 8**q*constant*beta_moment(n, q+1)
    actual = interval_linear(c, [tail_series_interval(n+j) for j in range(len(c))])
    responses = [sum((16**(j-k)*forcing(n+k) for k in range(1, j+1)), Q())
                 for j in range(len(c))]
    u_sum = sum((coefficient*orbit(n+j) for j, coefficient in enumerate(c)), Q())
    response = sum((coefficient*r for coefficient, r in zip(c, responses)), Q())
    assert u_sum == poly_eval(c, 16)*orbit(n)+response
    assert center-error <= actual[0] <= actual[1] <= center+error
    if poly_eval(c, 16) == 0:
        assert actual[0] <= -u_sum <= actual[1]
    if s == (-16, 1):
        assert (-1)**q*u_sum > 0  # Delta^q r(n+1)
    return {"coefficients": list(c), "P16": poly_eval(c, 16), "q": q,
            "center": center, "error": error, "tail_interval": actual,
            "rational_recurrence_identity": True}


def state_energy_certificate(a, length, h=1):
    """Enclose inf_s mean[1-cos(2*pi*h*U_n(s))] by the proved lemma."""
    natural(a, 1)
    natural(length, 2)
    integer(h)
    if h == 0:
        raise ValueError("nonzero frequency required")
    tails = [tail_beta_interval(n) for n in range(a, a+length)]
    lows = [abs(h)*lo for lo, _ in tails]
    highs = [abs(h)*hi for _, hi in tails]
    weights = [Q(1, 16**(length-1-j)) for j in range(length)]
    square_weight = sum((v*v for v in weights), Q())
    square_lo = sum((v*v for v in lows), Q())
    square_hi = sum((v*v for v in highs), Q())
    cross_lo = sum((v*w for v, w in zip(lows, weights)), Q())
    cross_hi = sum((v*w for v, w in zip(highs, weights)), Q())
    q_lo = max(Q(), square_lo-cross_hi**2/square_weight)
    q_hi = square_hi-cross_lo**2/square_weight
    m_bar = 20*square_hi  # 2*pi^2 < 20
    branch_margin = Q(1, 4)-Q(289, 8)*m_bar
    forcing_margin = Q(1, 2)-abs(h)*forcing(a+1)
    if branch_margin <= 0 or forcing_margin <= 0:
        raise ValueError("small-energy branch is not certified")
    pi_lo, pi_hi = machin_pi_interval(26)
    factor = 1-pi_hi**2*m_bar/24
    assert factor > 0 and 0 < q_lo <= q_hi
    energy_lo = 2*pi_lo**2*factor*q_lo/length
    energy_hi = 2*pi_hi**2*q_hi/length
    coherent_hi = 2*pi_hi**2*square_hi/length
    assert energy_lo <= energy_hi <= coherent_hi
    return {"A": a, "L": length, "h": h,
            "energy_interval": (energy_lo, energy_hi),
            "scaled_A4_interval": (a**4*energy_lo, a**4*energy_hi),
            "coherent_energy_upper": coherent_hi,
            "quadratic_projection_interval": (q_lo, q_hi),
            "branch_margin": branch_margin, "forcing_margin": forcing_margin,
            "completed_counterseed_energy": 0,
            "method": "exact rational consequences of proved branch-projection lemma"}


def is_prime(n):
    natural(n)
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n)+1))


def rational_mod_prime(value, p):
    if value.denominator % p == 0:
        raise ValueError("value is not p-integral")
    return value.numerator*pow(value.denominator, -1, p) % p


def old_cofactor_shadow(a):
    natural(a, 1)
    clock = source_clock(a)
    m = 3*a
    alpha = orbit(m)/16**m
    k = (clock*alpha+Q(1, 2)).numerator//(clock*alpha+Q(1, 2)).denominator
    seed = -Q(k, clock)
    tail_lo, tail_hi = tail_beta_interval(m)
    completion_interval = (alpha+seed+tail_lo/16**m,
                           alpha+seed+tail_hi/16**m)
    radius = 16**(2*a-1)*max(abs(v) for v in completion_interval)
    source_radius = radius+tail_beta_interval(a)[1]
    passports = []
    for n in range(a+1, 2*a):
        p = 8*n-7
        if not is_prime(p):
            continue
        assert gcd(p, clock) == 1
        original = rational_mod_prime(p*orbit(n), p)
        shifted = rational_mod_prime(p*(orbit(n)+16**n*seed), p)
        assert original == shifted == 4
        passports.append(p)
    assert passports
    return {"A": a, "M": m, "old_clock_bits": clock.bit_length(),
            "seed_is_nonzero_rational": seed != 0,
            "radius_bound": radius, "source_radius_bound": source_radius,
            "completed_mean_energy_upper": 20*radius**2,
            "source_mean_energy_upper": 20*source_radius**2,
            "short_arc_certified": radius < Q(1, 4),
            "preserved_newborn_primes": passports,
            "zero_anchor_preserved": False}


def ceil_q(value):
    return -((-value.numerator)//value.denominator)


def coset_count(lo, hi, offset, clock):
    """Count offset+k/clock in the half-open real interval [lo,hi)."""
    return ceil_q(clock*(hi-offset))-ceil_q(clock*(lo-offset))


def prime_gamma_clock(p):
    natural(p, 41)
    if p % 8 != 1 or not is_prime(p):
        raise ValueError("prime p == 1 mod 8 required")
    n = (p+7)//8
    r = forcing(n)
    forcing_clock = (p+3)*(p+4)*(p+5)//8
    assert r.denominator == p*forcing_clock
    delta_upper = Q(1, 2*p**2)-Q(1, 3*p**3)+Q(1, 4*p**4)
    delta_lower = delta_upper-Q(1, 5*p**5)
    lo = 30*delta_lower-Q(49, p**3)
    hi = 30*delta_upper-Q(49, p**3)+Q(236, p**4)
    assert lo < r < hi
    qn = source_clock(n)
    assert qn % p == 0 and (qn//p) % p != 0
    state_clock = qn//p
    numerator = qn*orbit(n)
    assert numerator.denominator == 1
    assert (numerator.numerator-4*state_clock) % p == 0
    old_address = ((numerator.numerator-4*state_clock)//p) % state_clock
    assert (Q(4, p)+Q(old_address, state_clock)) % 1 == orbit(n) % 1
    return {"p": p, "n": n, "forcing_clock": forcing_clock,
            "state_clock_bits": state_clock.bit_length(), "window_width": hi-lo,
            "forcing_coset_candidates": coset_count(lo, hi, Q(4, p), forcing_clock),
            "state_coset_capacity_on_same_window": coset_count(lo, hi, Q(4, p), state_clock),
            "newborn_residue": rational_mod_prime(p*orbit(n), p),
            "full_old_cofactor_reconstruction": True,
            "state_is_claimed_inside_forcing_window": False}


def exact_product_control(n):
    natural(n, 2)
    weighted = sum((16**(n-j)*forcing(j) for j in range(1, n+1)), Q())
    unweighted = sum((forcing(j) for j in range(1, n+1)), Q())
    assert weighted == orbit(n)
    assert unweighted != weighted
    return {"n": n, "weighted_log_derivative_is_U": True,
            "ordinary_gamma_log_derivative_is_U": False}


def rational_alias_control():
    for j in range(1, 65):
        assert Q(16**j, 15) % 1 == Q(1, 15)
    cosine_lo, cosine_hi, _, _ = box_phase(Q(1, 15))
    assert cosine_hi < 1
    return {"completed_boundary": "1/15", "R0_gap_interval": (1-cosine_hi, 1-cosine_lo),
            "frequency_15_energy": 0, "normal": False,
            "same_forcing_seed": "1/15 - pi/16", "zero_anchor_preserved": False}


def mutation_control(n):
    authentic = tail_beta_interval(n)
    mutant = tail_beta_interval(n, mutated=True)
    exact = tail_series_interval(n, mutated=True)
    assert mutant[0] <= exact[0] <= exact[1] <= mutant[1]
    assert authentic[1] < mutant[0]
    assert forcing(n) == combined_forcing(n)
    assert mutated_forcing(n) != combined_forcing(n)
    return {"n": n, "total_residue": 1,
            "n_times_mutant_tail": (n*mutant[0], n*mutant[1]),
            "authentic_identity_rejected": True, "proved_tail_limit": "1/120"}


def decimal_interval(lo, hi, digits=18):
    """Outward base-10 enclosure; integer arithmetic only."""
    scale = 10**digits
    left = (lo*scale).numerator//(lo*scale).denominator
    right = ceil_q(hi*scale)
    def show(value):
        sign = "-" if value < 0 else ""
        whole, fraction = divmod(abs(value), scale)
        return f"{sign}{whole}.{fraction:0{digits}d}"
    return {"lower": show(left), "upper": show(right), "outward_decimal_digits": digits}


def serial(value):
    if isinstance(value, Q):
        return serial((value, value))
    if isinstance(value, tuple) and len(value) == 2 and all(isinstance(v, Q) for v in value):
        extent = max(abs(v) for v in value)
        digits = 18
        if extent:
            while extent < 1:
                extent *= 10
                digits += 1
        return decimal_interval(*value, digits=digits)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


def run():
    for n in range(1, 129):
        assert forcing(n) == combined_forcing(n)
        lo, hi = tail_beta_interval(n)
        actual_lo, actual_hi = tail_series_interval(n)
        assert lo <= actual_lo <= actual_hi <= hi
    lag_results = [{"n": n, **lag_tail_certificate(n, c)} for n in HOLDOUTS for c in stencils()]
    energy_results = [state_energy_certificate(a, a) for a in HOLDOUTS]
    shadow_results = [old_cofactor_shadow(a) for a in OLD_CLOCK_HOLDOUTS]
    prime_results = [prime_gamma_clock(p) for p in PRIME_HOLDOUTS]
    assert all(item["forcing_coset_candidates"] == 1 for item in prime_results)
    assert all(item["state_coset_capacity_on_same_window"] > 1 for item in prime_results)
    return serial({
        "status": "exact finite controls; paper theorems are not inferred from these runs",
        "baseline": BASELINE,
        "execution_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "preregistration_sha256": PREREG_SHA256,
        "preregistration_utc": "2026-11-13 00:15:46 UTC",
        "provenance": "same model family; separately implemented four poles versus inherited combined formula; not external independence",
        "source_calibration_n": [1, 128],
        "lag_holdouts": lag_results,
        "state_energy_holdouts": energy_results,
        "old_cofactor_shadows": shadow_results,
        "prime_gamma_clock_holdouts": prime_results,
        "rational_alias": rational_alias_control(),
        "mutations": [mutation_control(n) for n in HOLDOUTS],
        "additional_known_result_controls": [exact_product_control(n) for n in (2, 3, 7, 16)],
        "disclosure": "Product controls were added after the prospective declaration as classical calibration, not holdouts. No numerical minimization, floating asymptotic fit, or pi digit oracle is used.",
        "R0_proved": False,
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text)
        print(json.dumps({"output": str(args.output), "sha256": hashlib.sha256(text.encode()).hexdigest(),
                          "state_energy_holdouts": result["state_energy_holdouts"],
                          "old_cofactor_shadows": result["old_cofactor_shadows"],
                          "prime_gamma_clock_holdouts": result["prime_gamma_clock_holdouts"]}, indent=2))
    else:
        print(text)
