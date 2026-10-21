#!/usr/bin/env python3
"""Exact symbolic and rational controls, not universal proof authority."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import platform
import subprocess
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.viii_high_divisor import (  # noqa: E402
    ConicSeed, conic_selections, factorization, ris,
)


def nth_root_floor(n,k):
    """Pure integer binary search, followed by exact defining inequalities."""
    lo,hi = 0,1 << ((n.bit_length()+k-1)//k)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    result = hi if hi**k <= n else lo
    assert result**k <= n < (result+1)**k
    return result


def power_interval(n,a=5,b=7,scale=10**6):
    value = n**a*scale**b
    lower = nth_root_floor(value,b)
    upper = lower if lower**b == value else lower+1
    return Fraction(lower,scale),Fraction(upper,scale)


def weight_upper(d):
    answer = Fraction(1)
    for p,k in factorization(d):
        if k == 1:
            return Fraction()
        _,hi = power_interval(p,5*(k-1))
        lo,_ = power_interval(p,5*(k-2))
        answer *= hi-lo
    return answer


def symbolic_controls():
    u,v,r0,s0,z0,n,m = sp.symbols("u v r0 s0 z0 n m")
    Q = u*n*n+v*m*m
    L = u*r0*n+v*s0*m
    x,y,z = r0*Q-2*n*L,s0*Q-2*m*L,z0*Q
    base = u*r0*r0+v*s0*s0
    expressions = {
        "quadratic_identity": u*x*x+v*y*y-base*Q*Q,
        "first_elimination": u*r0*r0*Q-L*L+2*v*s0*m*L-v*base*m*m,
        "second_elimination": v*s0*s0*Q-L*L+2*u*r0*n*L-u*base*n*n,
        "first_linear_identity": z0*x-r0*z+2*z0*n*L,
        "second_linear_identity": z0*y-s0*z+2*z0*m*L,
    }
    result = {name:sp.expand(expr)==0 for name,expr in expressions.items()}
    assert all(result.values())
    return result


def main():
    symbolic = symbolic_controls()
    census = []
    seed = ConicSeed(1,1,2,1,1,1)
    for X in (10,50,338,1000,10000,100000):
        records = conic_selections(seed,X)
        # For these cutoffs floor(X^(1/100))=1, checked without floating point.
        assert 1 <= X < 2**100
        permitted = [r for r in records if ris(product(r.square_roots))**2 <= X]
        moment_upper = sum((power_interval(ris(r.a*r.b*r.c))[1] for r in permitted),Fraction())
        selected_upper = sum((weight_upper(r.d)*weight_upper(r.e)*weight_upper(r.f)
                              for r in permitted),Fraction())
        high = [r for r in permitted if r.D > X*X]
        # Compare rational upper endpoints with the irrational theorem budgets
        # by raising both positive quantities to integer powers.
        assert moment_upper.numerator**350 <= 23**350*X**691*moment_upper.denominator**350
        assert selected_upper.numerator**700 <= 23**700*X**1367*selected_upper.denominator**700
        assert len(records)**2 <= seed.count_coefficient_squared*X
        census.append({"X":X,"all_primitive_conic_sources":len(records),
                       "permitted_root_depth_sources":len(permitted),
                       "high_divisor_selections":len(high),
                       "moment_5_over_7_rational_upper":str(moment_upper),
                       "selected_5_over_7_rational_upper":str(selected_upper)})
    paths = ("observational_succ/viii_high_divisor.py", "tests/test_viii_high_divisor.py",
             "scripts/viii_high_divisor_probe.py", "research/2026-10-21/VIII_HIGH_DIVISOR_CONICS.md")
    receipt = {
        "schema":"succ.viii.restricted_conic.exact_probe.v1",
        "checkout":subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),
        "working_tree_dirty":bool(subprocess.check_output(["git","status","--porcelain"],cwd=ROOT,text=True).strip()),
        "python":platform.python_version(),"sympy":sp.__version__,
        "symbolic_polynomial_controls":symbolic,"census":census,
        "failures":0,"formal_status":"not Lean-formalized",
        "scope":"Finite exact checks of a declared family; paper proof supplies universal claims.",
        "source_sha256":{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))


def product(values):
    result = 1
    for value in values:
        result *= value
    return result


if __name__ == "__main__":
    main()
