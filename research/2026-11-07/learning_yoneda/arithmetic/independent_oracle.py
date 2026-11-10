"""Independent integer implementation: combined source polynomial, no pole loop."""
from fractions import Fraction
from math import lcm


def integer_histories(B, seed_numerator, seed_denominator):
    factors = [(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3) for n in range(1,B+1)]
    denominator = lcm(*factors)
    ordinary = [0]
    shadow = [seed_numerator*denominator]
    for n,d in enumerate(factors,1):
        injection = (120*n*n-89*n+16)*(denominator//d)
        ordinary.append(16*ordinary[-1]+injection)
        shadow.append(16*shadow[-1]+seed_denominator*injection)
    return denominator, ordinary, denominator*seed_denominator, shadow


def check(witness):
    w=witness
    d,u,ds,v=integer_histories(w['B'],w['seed'].numerator,w['seed'].denominator)
    count=0
    for n in range(w['B']+1):
        assert Fraction(u[n],d)==w['original'][n]
        assert Fraction(v[n],ds)==w['shadow'][n]
        # independent nearest-integer phase representative from integer division
        r=v[n]%ds
        signed=r if 2*r <= ds else r-ds
        if n >= w['A']:
            declared=w['shadow'][n]-16**(n-w['A'])*w['M']
            assert Fraction(signed,ds)==declared
        count+=2
    return count
