#!/usr/bin/env python3
"""Finite operational observational_succ: two filtrations, shadow, probes, source.
No zeta zero inputs, no RH sign claims. Python >=3.10, standard library only.
Run: python scripts/operational_observational_succ_probe.py
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import gcd, lcm, log2
import json

def clock(n):
    return lcm(*range(1, n + 1))

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def totient(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))

def structure_birth(d):
    """The first N with d | L_N, d>=1."""
    if d == 1:
        return 1
    largest = 1
    remaining = d
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            power = 1
            while remaining % p == 0:
                power *= p
                remaining //= p
            largest = max(largest, power)
        p += 1
    if remaining > 1:
        largest = max(largest, remaining)
    return largest

def history(start, ops):
    """Execute a word on N_0, retaining every intermediate state."""
    states = [start]
    for op, value in ops:
        n = states[-1]
        if op == "multiply":
            n *= value
        elif op == "divide":
            if n % value:
                return None
            n //= value
        elif op == "succ":
            n += 1
        elif op == "inverse-succ":
            if n == 0:
                return None
            n -= 1
        else:
            raise ValueError(op)
        states.append(n)
    return states

@lru_cache(None)
def factor_paths(n, depth):
    if depth == 1:
        return ((n,),) if n >= 2 else ()
    return tuple((d,) + tail
                 for d in range(2, n)
                 if n % d == 0
                 for tail in factor_paths(n // d, depth - 1))

def convolution_shadow(n):
    """Terms of log_* a at n not involving the direct coefficient a(n),
    evaluated for a(d)=1 at all proper divisors d of n."""
    return sum((Q((-1)**(r+1) * len(factor_paths(n, r)), r)
                for r in range(2, int(log2(n)) + 1)), Q(0))

def main():
    # Test the inductive Hilbert-space filtration H_N=L^2(Z/L_N).
    rows = []
    for n in range(2, 10):
        old, new = clock(n - 1), clock(n)
        born = [d for d in divisors(new) if old % d != 0]
        newrank = sum(totient(d) for d in born)
        assert newrank == new - old
        assert new == old or (n in (2, 3, 4, 5, 7, 8, 9))
        rows.append({"N": n, "L_N": new, "innovation_rank": newrank,
                     "new_exact_conductors": born})
    assert structure_birth(6) == 3 and structure_birth(12) == 4
    for d in range(1, 101):
        assert structure_birth(d) == min(n for n in range(1, d + 1)
                                         if clock(n) % d == 0)

    # Same endpoint operator, distinct execution histories and horizons.
    short = history(2, [("divide", 2), ("multiply", 2)])
    long = history(2, [("multiply", 2), ("divide", 2)])
    assert short == [2, 1, 2] and long == [2, 4, 2]
    assert max(short) == 2 and max(long) == 4
    # At N=2, project before each operation: multiplication of |2> is
    # unobservable (|4> lies in Q_N). Project only at the end: D_2 M_2 |2>=|2>.
    assert 2 * 2 > 2 and (2 * 2) // 2 == 2

    # Mixed 2x3 conductor: hidden from either one-prime conditional probe.
    h = {n: (Q(int(n % 2 == 0)) - Q(1, 2)) *
             (Q(int(n % 3 == 0)) - Q(1, 3)) for n in range(6)}
    def conditional_mod(m):
        return {r: sum((h[n] for n in range(6) if n % m == r), Q(0))
                   / (6 // m) for r in range(m)}
    assert set(conditional_mod(2).values()) == {Q(0)}
    assert set(conditional_mod(3).values()) == {Q(0)}
    norm2 = sum((z*z for z in h.values()), Q(0)) / 6
    assert norm2 == Q(1, 18)

    # Probability snapshots: all modulo-2-only and modulo-3-only
    # observations coincide, while their mixed expectation differs.
    states = {}
    for sign in [-1, +1]:
        prob = {n: (1 + sign*h[n])/6 for n in range(6)}
        assert min(prob.values()) > 0 and sum(prob.values()) == 1
        marg2 = tuple(sum((prob[n] for n in range(6) if n % 2 == r), Q(0))
                      for r in range(2))
        marg3 = tuple(sum((prob[n] for n in range(6) if n % 3 == r), Q(0))
                      for r in range(3))
        mixed = sum((prob[n]*h[n] for n in range(6)), Q(0))
        states[str(sign)] = {"mod2": list(map(str, marg2)),
                             "mod3": list(map(str, marg3)),
                             "joint_expectation": str(mixed)}
    assert states["-1"]["mod2"] == states["1"]["mod2"]
    assert states["-1"]["mod3"] == states["1"]["mod3"]
    assert states["-1"]["joint_expectation"] != states["1"]["joint_expectation"]

    # Causal Dirichlet-convolution log: shadow before direct arrival.
    source = []
    for n in [4, 6, 8, 9, 12]:
        sh = convolution_shadow(n)
        connected = 1 + sh   # ζ has a(n)=1 for every n.
        source.append({"n": n, "shadow_before_a_n": str(sh),
                       "after_arrival_log_star_a": str(connected)})
    assert convolution_shadow(4) == -Q(1, 2)
    assert convolution_shadow(6) == -1
    assert convolution_shadow(8) == -Q(2, 3)
    assert convolution_shadow(9) == -Q(1, 2)
    assert convolution_shadow(12) == -1
    # Mutate only a(6): everything seen before event 6 is identical.
    fake_six = Q(1, 7)
    assert (1 + fake_six + convolution_shadow(6)) == fake_six

    result = {
        "status": "PASS", "scope": "finite arithmetic and probe-relative states",
        "source_zeros_read": False,
        "wavefront_filtration": rows,
        "same_endpoint_distinct_histories":
            {"short": short, "long": long, "birth_horizons": [max(short),max(long)]},
        "born_mixed_conductor_6_at_N": structure_birth(6),
        "integer_6_directly_encountered_at_N": 6,
        "mixed_h_on_Z6": {str(n): str(v) for n,v in h.items()},
        "conditional_mod2": {str(k):str(v) for k,v in conditional_mod(2).items()},
        "conditional_mod3": {str(k):str(v) for k,v in conditional_mod(3).items()},
        "mixed_h_norm_squared": str(norm2),
        "two_restricted_observation_states": states,
        "convolution_log_shadow": source,
        "fake6_connected_coefficient": str(fake_six),
        "caveats": [
            "State snapshots ± are not invariant under cyclic SUCC; they prove a restricted-probe gap only.",
            "Neither the mixed CRT mode nor the projection identity implies positivity of the Weil form.",
            "No global arithmetic-to-Archimedean Hodge polarization was constructed."
        ],
    }
    print(json.dumps(result, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
