"""Exact independent finite checks for the beta transport. Run with Python 3."""
from collections import Counter
from fractions import Fraction as Q
from math import comb, factorial, isqrt
import hashlib
import json
from pathlib import Path


ANGULAR = tuple(Q(x) for x in (2, 2, 1, 0, "-1/2", "-1/2", "-1/4", 0))


def selected(n, seed=0):
    value = Q(seed)
    for k in range(n):
        value = 16 * value + sum(tap / (8*k+j) for j, tap in enumerate(ANGULAR, 1))
    return value


def reflected_prefix(n):
    """Generate from the recurrence in original time, not the closed-form quotient."""
    impulse = [Q(2), Q(2)]
    for j in range(2, 8*n):
        impulse.append(impulse[j-1] - impulse[j-2]/2)
    return [(-1)**j * sum(impulse[i]*comb(i, j) for i in range(j, len(impulse)))/4
            for j in range(len(impulse))]


def negative_values(n):
    coeff = reflected_prefix(n)
    eulers = [1]
    for j in range(1, 8*n+1):
        eulers.append(-sum(comb(j, k)*eulers[k] for k in range(j-2, -1, -2)))
    first_failure = None
    for j, value in enumerate(eulers):
        difference = Q(value, 2) - sum(c*m**j for m, c in enumerate(coeff, 1))
        if difference:
            first_failure = j
            break
    assert first_failure == 8*n
    assert difference == Q(factorial(8*n), 2*16**n)
    period = sum(c/m for m, c in enumerate(coeff, 1))
    assert period == selected(n)/(4*16**(n-1))
    return {"blocks": n, "consecutive_values_equal": first_failure,
            "first_defect": str(difference), "specialization_at_one": str(period)}


def factors(n):
    counts = Counter()
    for p in range(2, isqrt(n)+1):
        while n % p == 0:
            counts[p] += 1
            n //= p
    if n > 1:
        counts[n] += 1
    return counts


def chi(n):
    return (0, 1, 0, -1)[n % 4]


def logderivative(limit):
    """Exact log-prime coefficient vectors of -(L'/L), via formal series division."""
    # Expand 4/((t-1)^2+1) at t=1, in x=1-t, normalized by 4.
    coeff = [0, 1]
    for n in range(2, limit+1):
        coeff.append(-coeff[n-2])
    tape = [{}]
    for n in range(1, limit+1):
        fac = factors(n)
        assert coeff[n] == chi(n)
        value = Counter({p: coeff[n]*k for p, k in fac.items()})
        for d in range(1, n):
            if n % d == 0:
                for p, a in tape[d].items():
                    value[p] -= coeff[n//d] * a
        row = {p:a for p, a in value.items() if a}
        if n % 2 and len(fac) == 1:
            p, k = next(iter(fac.items()))
            assert row == {p: chi(p)**k}
        else:
            assert row == {}
        tape.append(row)
    assert [Q(2)/4, Q(2)/4] != [Q(1), Q(0)]  # unreflected first two coefficients
    assert coeff[3] != 1  # even/principal-character mutation
    return {str(n): tape[n] for n in (2, 3, 9, 11, 15, 21, 27, 45, 125, 169, 243)}


def pair_epoch():
    separations = {str(seed): (selected(3, seed)-selected(2, seed)) % 1
                   for seed in (0, Q(1,5), Q(1,7))}
    unshifted = separations["0"]
    assert separations["1/5"] == unshifted
    assert separations["1/7"] not in (unshifted, (-unshifted) % 1)
    return {k:str(v) for k,v in separations.items()}


def prime_bump_intervals(p):
    """Outer enclosures for a normalized nonnegative bump of log-radius 1/64.

    The physical archimedean integral contributes between -1/32 and 0.
    atanh series encloses log(p), integer square roots enclose sqrt(p).
    """
    r = Q(p-1, p+1)
    n = 36
    partial = 2*sum(r**(2*j+1)/(2*j+1) for j in range(n))
    error = 2*r**(2*n+1)/((2*n+1)*(1-r*r))
    scale = 10**6
    lower = Q(isqrt(p*scale**2),scale)
    upper = lower + Q(1,scale)
    endpoints = [-chi(p)*partial/upper, -chi(p)*(partial+error)/lower]
    lo, hi = min(endpoints)-Q(1,32), max(endpoints)
    assert lo > 0 if p == 3 else hi < 0
    # Round outwards to thousandths using integer arithmetic.
    return [str(Q((1000*lo)//1,1000)), str(Q(-((-1000*hi)//1),1000))]


def run():
    root = Path(__file__).resolve().parent
    return {
        "scope":"finite exact tests and rational enclosures; no sampled zeros or GRH",
        "prereg_sha256":{name:hashlib.sha256((root/name).read_bytes()).hexdigest()
                         for name in ("PREREGISTRATION.md","MELLIN_PREREGISTRATION.md")},
        "mellin": [negative_values(n) for n in (1,3,9,13)],
        "fourier_separations": pair_epoch(),
        "formal_logderivative_max_n":275, "tape_examples": logderivative(275),
        "linear_bump_signed_intervals": {str(p):prime_bump_intervals(p) for p in (3,5)}
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
