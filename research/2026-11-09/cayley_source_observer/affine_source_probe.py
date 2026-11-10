"""Finite calibration of the paper source-clock action, not a C-monoid compiler.

This late constructive probe was not part of the frozen parity experiment.
The four-pole prefix and canonical combined forcing provide distinct arithmetic
implementations. The universal authority is AFFINE_SOURCE_ACTION.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import json

from observational_succ.duck_bbp import forcing, lifted_orbit


def four_poles(j):
    return Q(4, 8*j-7)-Q(2, 8*j-4)-Q(1, 8*j-3)-Q(1, 8*j-2)


@lru_cache(None)
def prefix(n):
    return sum((four_poles(j)/16**j for j in range(1, n+1)), Q())


def action(a, b, state):
    n, u = state
    m = a*n+b
    return m, 16**m*(u/16**n-prefix(n)+prefix(m))


def serial(state, steps):
    n, u = state
    for _ in range(steps):
        n += 1
        u = 16*u+forcing(n)
    return n, u


def finite_tail(n, horizon):
    return sum((forcing(j)/16**(j-n) for j in range(n+1, horizon+1)), Q())


def run():
    counts = {k: 0 for k in (
        "serial_source", "compositions", "seed_preservation",
        "finite_completion", "clocked_circle_descent", "source_gauge")}
    for n in range(5):
        for u in (Q(0), Q(1,7), Q(-3,2), Q(7)):
            state = n, u
            for a in range(1,4):
                for b in range(3):
                    m, v = action(a,b,state)
                    assert (m,v) == serial(state,(a-1)*n+b)
                    counts["serial_source"] += 1
                    assert v/16**m-prefix(m) == u/16**n-prefix(n)
                    counts["seed_preservation"] += 1
                    horizon = m+3
                    assert v+finite_tail(m,horizon) == 16**(m-n)*(u+finite_tail(n,horizon))
                    counts["finite_completion"] += 1
                    shifted = action(a,b,(n,u+3))[1]
                    assert (shifted-v) == 3*16**(m-n)
                    counts["clocked_circle_descent"] += 1
                    # K sends the BBP source to zero forcing while retaining its seed.
                    assert v-16**m*prefix(m) == 16**(m-n)*(u-16**n*prefix(n))
                    counts["source_gauge"] += 1
                    for c in range(1,4):
                        for d in range(3):
                            assert action(a,b,action(c,d,state)) == action(a*c,a*d+b,state)
                            counts["compositions"] += 1
    for p in range(2,6):
        for n in range(5):
            state = n, lifted_orbit(n)
            assert action(p,0,serial(state,1)) == serial(action(p,0,state),p)
            assert action(p,0,serial(state,1)) != serial(action(p,0,state),1)
            assert action(p,0,state) == (p*n,lifted_orbit(p*n))
        assert action(p,0,(0,Q())) != serial((0,Q()),p)
    assert action(2,0,(0,Q()))[1] % 1 == 0
    assert action(2,0,(1,Q()))[1] % 1 == Q(106,819)
    root=Path(__file__).resolve().parents[3]
    paths=("observational_succ/duck_bbp.py",
           "research/2026-11-09/cayley_source_observer/affine_source_probe.py")
    return {"status":"PASS_EXACT_FINITE", "grid":{"n":"0..4","u":["0","1/7","-3/2","7"],
            "a_c":"1..3","b_d":"0..2","braid_p":"2..5"},
            "counts":counts,"braid_cases":20,"false_commutation_cases":20,
            "false_fixed_iterate_cases":4,"clock_forgetting_output_phases":["0","106/819"],
            "source_hashes":{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths},
            "preregistered_parity_protocol":False,"c_monoid_compiler_proved":False,
            "selected_signed_cancellation_proved":False}


if __name__ == "__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
