#!/usr/bin/env python3
"""Independent exact calibration of positive Pascal prime charts and coherence.

This is a late, separately scoped paper-followup instrument. It changes no
production module or unit test frozen for the full repository validation.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.bbp_source_memory import tail_interval
from observational_succ.bbp_two_adic import rational_mod
from scripts.pi_pascal_probe import machin_interval, rational_receipt


def forcing(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


U = [Q()]
for n in range(1, 401):
    U.append(16*U[-1]+forcing(n))


def vp2(x):
    x = Q(x)
    if not x:
        raise ValueError("zero has infinite valuation")
    a, b = abs(x.numerator), x.denominator
    return (a & -a).bit_length()-(b & -b).bit_length()


def nu(j):
    return 2*j-j.bit_count()-1


def parameters(q):
    d = 1
    while 16**d < q:
        d += 2
    a = Q(q-1,16**d-1)
    return d, a, vp2(q-1)


@lru_cache(None)
def source(q, k):
    d, a, _ = parameters(q)
    return sum((comb(k,j)*a**j*(1-a)**(k-j)*U[d*j]
                for j in range(k+1)), Q())


@lru_cache(None)
def coefficient(q, j):
    if j == 0:
        return Q()
    d, a, _ = parameters(q)
    return a**j*sum((comb(j,i)*(-1)**(j-i)*U[d*i]
                    for i in range(j+1)), Q())


def chart_mod(q, n, bits):
    delta = parameters(q)[2]
    total, j = 0, 1
    while nu(j)+(j-1)*delta < bits:
        total += comb(n,j)*rational_mod(coefficient(q,j)/2**delta,bits)
        j += 1
    return total % 2**bits


def falling_derivative(n,j):
    # Exact derivative at n of product_(i=0)^(j-1)(t-i).
    value, derivative = 1, 0
    for i in range(j):
        derivative = derivative*(n-i)+value
        value *= n-i
    return derivative


@lru_cache(None)
def tail(n):
    return tail_interval(n, terms=6)


def run():
    started = time.monotonic()
    counts = Counter()
    def require(name, condition):
        if not condition:
            raise AssertionError(name)
        counts[name] += 1

    alpha = tuple(x/16 for x in machin_interval(256))
    bases = (2,3,4,5,7,9,11,13,16,17,31,37,257,65537)
    table = []
    for q in bases:
        d,a,delta = parameters(q)
        for j in range(1,33):
            c = coefficient(q,j)
            literal = sum((comb(j,i)*(-1)**(j-i)*source(q,i)
                           for i in range(j+1)),Q())
            require("literal_Newton",c==literal)
            require("Newton_valuation",vp2(c)==nu(j)+j*delta)
            require("falling_coefficient_valuation",vp2(c/factorial(j))==(delta+1)*j-1)
        for x in range(1,25):
            for y in range(x):
                require("exact_distance_similarity",vp2(source(q,x)-source(q,y))==vp2(x-y)+delta)
        for x in (0,1,2,7,31,127):
            derivative=sum((coefficient(q,j)*falling_derivative(x,j)/factorial(j)
                            for j in range(1,33)),Q())
            require("derivative_truncation_valuation",vp2(derivative)==delta)
        for k in (1,4,12,24,40,64):
            value=source(q,k)
            weights=[comb(k,j)*a**j*(1-a)**(k-j) for j in range(k+1)]
            require("positive_weight_norm",sum(weights,Q())==1 and all(w>=0 for w in weights))
            lower=sum((w*tail(d*j)[0] for j,w in enumerate(weights)),Q())
            upper=sum((w*tail(d*j)[1] for j,w in enumerate(weights)),Q())
            require("independent_Machin_shadow",lower<q**k*alpha[0]-value<q**k*alpha[1]-value<upper)
        table.append({"base":q,"odd_source_step":d,"a":str(a),"delta":delta,
                      "denominator":a.denominator,"quadratic_error_constant":str(Q(1,64)/(a*a*d*d))})

    chart_bases=(2,3,4,5,7,11,13,16)
    for bits in range(1,9):
        mod=2**bits
        charts={q:[chart_mod(q,n,bits) for n in range(mod)] for q in chart_bases}
        inverses={}
        for q,labels in charts.items():
            require("normalized_chart_permutation",sorted(labels)==list(range(mod)))
            inverse=[0]*mod
            for i,x in enumerate(labels): inverse[x]=i
            inverses[q]=inverse
        for x in range(mod):
            require("authentic_base16_anchor",charts[16][x]==rational_mod(U[x],bits))
            for p,q,r in ((16,4,2),(2,3,11),(13,7,5),(3,16,13)):
                middle=charts[q][inverses[p][x]]
                composed=charts[r][inverses[q][middle]]
                direct=charts[r][inverses[p][x]]
                require("coherent_chart_transport",composed==direct)
            middle=charts[4][2*inverses[16][x] % mod]
            composed=charts[2][2*inverses[4][middle] % mod]
            direct=charts[2][4*inverses[16][x] % mod]
            require("clock_respecting_16_4_2",composed==direct)

    # Direct rational comparison: the exponential alpha terms cancel exactly.
    blocking=[]
    for n in (8,16,32,64):
        two=source(2,4*n)-U[n]
        four=source(4,2*n)-U[n]
        require("binary_blocking_error_bound",abs(two)<tail(n)[1]
                +sum((comb(4*n,j)*Q(1,15)**j*Q(14,15)**(4*n-j)*tail(j)[1]
                      for j in range(4*n+1)),Q()))
        blocking.append({"hex_time":n,"binary_difference":rational_receipt(two),
                         "quaternary_difference":rational_receipt(four)})

    # P3^2 is not the canonical P9: preserve the failed stronger coherence.
    composed_first=(Q(169)*U[0]+52*U[1]+4*U[2])/225
    require("canonical_product_mismatch",composed_first!=source(9,1))
    require("canonical_product_differential_mismatch",vp2(composed_first)==2 and vp2(source(9,1))==3)
    require("base11_small_local_cover",(U[18]+2*U[19])/3==11*U[18]+Q(2,3)*forcing(19))

    inputs=["scripts/pi_ternary_convex_probe.py","research/2026-10-24/PI_TERNARY_CONSTRUCTOR.md",
            "research/2026-10-24/PI_TERNARY_CHART_COHERENCE.md"]
    return {"status":"EXACT_FINITE_PASSED","assertions":sum(counts.values()),
            "counts":dict(counts),"elapsed_seconds":time.monotonic()-started,
            "base_table":table,"blocking_rows":blocking,
            "scope":"Late independent exact calibration; infinite claims use paper proofs. All maps are dyadic source charts, not continuous field maps from Qp or proofs of real law preservation.",
            "source_hashes":{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("status","assertions","elapsed_seconds")}))
