#!/usr/bin/env python3
"""Independent exact arithmetic controls; no SUCC arithmetic modules imported.

The proof is in the companion referee dossier. Finite runs test implementations
and falsifying mutations, not universal claims. Farey-tree generation differs
from the production divisor and CRT census implementations.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path


def farey_interior(bound):
    """Reduced fractions in (0,1), by the neighboring-Farey recurrence."""
    a, b, c, d = 0, 1, 1, bound
    result = []
    while c < d:
        result.append((c, d))
        k = (bound + b) // d
        a, b, c, d = c, d, k*c-a, k*d-b
    return result


def radical(n):
    result, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            result *= p
            while n % p == 0:
                n //= p
        p += 1
    return result*n


def mobius(n):
    sign, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            sign = -sign
            n //= p
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def divisor_weight(n, t):
    """Möbius inversion at integer t; deliberately not prime-power formula."""
    return sum(mobius(d)*(n//d//radical(n//d))**t for d in divisors(n))


def raw_count(x, d, e, f):
    """Direct integer census; no modular inversion or lattice implementation."""
    return sum(1 for a in range(d, int(x)+1, d)
               for b in range(e, int(x-a)+1, e) if (a+b) % f == 0)


def audit(max_x=35, max_divisor=9):
    slope_cases = lattice_cases = mobius_cases = expansion_cases = 0
    census = []
    # Real cutoffs are exact fractions, including both sides of integer edges.
    cutoffs = [Fraction(n, 2) for n in range(0, 2*max_x+2)]
    triples = [(d,e,f) for d in range(1,max_divisor+1)
               for e in range(1,max_divisor+1)
               for f in range(1,max_divisor+1)
               if gcd(d,e)*gcd(d,f)*gcd(e,f) == 1]
    for x in range(2,max_x+1):
        points = farey_interior(x)
        brute = {(a,c) for c in range(2,x+1) for a in range(1,c) if gcd(a,c)==1}
        assert set(points) == brute
        total_h = sum(a*(c-a)*c//radical(a*(c-a)*c) for a,c in points)
        census.append([x,len(points),total_h])
        for d,e,f in triples:
            selected = [(a,c) for a,c in points
                        if a%d == 0 and (c-a)%e == 0 and c%f == 0]
            product = d*e*f
            assert len(selected) <= 1+Fraction(x*x,product)
            # Farey recurrence already orders slopes, so check signed spacing.
            for (a,c),(aa,cc) in zip(selected,selected[1:]):
                determinant = aa*c-a*cc
                assert determinant > 0 and determinant % product == 0
                assert Fraction(determinant,c*cc) >= Fraction(product,x*x)
            slope_cases += 1
            via_mobius = sum(mobius(k)*raw_count(Fraction(x,k),
                d//gcd(d,k),e//gcd(e,k),f//gcd(f,k))
                for k in range(1,x//2+1))
            assert via_mobius == len(selected)
            mobius_cases += 1
    for x in cutoffs:
        for d,e,f in triples:
            count = raw_count(x,d,e,f)
            error = abs(count-x*x/Fraction(2*d*e*f))
            assert error <= x/d+x/Fraction(2*e*f)
            lattice_cases += 1
    for n in range(1,151):
        for t in (0,1,2,3):
            assert sum(divisor_weight(d,t) for d in divisors(n)) == (n//radical(n))**t
            for d in divisors(n):
                g = divisor_weight(d,t)
                assert g >= 0
                if g:
                    assert d <= (n//radical(n))**2
            expansion_cases += 1
    # Mutation: dropping common-divisor k that shares an occupied prime is wrong.
    x,d,e,f = 12,2,1,1
    actual = sum(a%d==0 for a,c in farey_interior(x))
    wrong = sum(mobius(k)*raw_count(Fraction(x,k),d,e,f)
                for k in range(1,x//2+1) if gcd(k,d*e*f)==1)
    assert wrong != actual
    # Mutation: the singleton in the slope bound cannot be discarded.
    a,b,c = 441,400,841
    product = a*b*c
    assert gcd(a,b)==1 and product > c*c
    return {"scope":"finite independent controls, not a universal proof",
            "parameters":{"max_x":max_x,"max_divisor":max_divisor},
            "slope_cases":slope_cases,"raw_lattice_cases":lattice_cases,
            "full_mobius_cases":mobius_cases,"divisor_expansion_cases":expansion_cases,
            "integer_first_moment_census":census,
            "census_sha256":hashlib.sha256(json.dumps(census).encode()).hexdigest(),
            "coprime_k_mutation":{"X":x,"d":d,"e":e,"f":f,
                                  "actual":actual,"wrong":wrong},
            "singleton_mutation":{"a":a,"b":b,"c":c,"D":product,
                                  "density_only_bound":str(Fraction(c*c,product))},
            "failures":0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-x",type=int,default=35)
    parser.add_argument("--max-divisor",type=int,default=9)
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    result = audit(args.max_x,args.max_divisor)
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(output)
    print(output)


if __name__ == "__main__":
    main()
