#!/usr/bin/env python3
"""Exact irreducibility certificate for Pentanacci Pisot rank-four circle source.

No numerical root approximation is used for the irreducibility statement.
Uses F_5[x] Frobenius and Euclidean polynomial GCD, via ordinary integers.
Pisot-conjugate location is proved separately by Rouché in the dossier.
"""
from __future__ import annotations

P = 5
# Monic pentanacci x^5-x^4-x^3-x^2-x-1, low-degree coefficients first.
F = [-1,-1,-1,-1,-1,1]


def trim(a):
    a=[int(v)%P for v in a]
    while a and a[-1]==0:a.pop()
    return a


def remainder(a,b):
    a=trim(a);b=trim(b)
    if not b:raise ZeroDivisionError
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b):
        coeff=a[-1]*inv%P;shift=len(a)-len(b)
        for j,v in enumerate(b):a[j+shift]=(a[j+shift]-coeff*v)%P
        a=trim(a)
    return a


def multiply_mod(a,b):
    a=trim(a);b=trim(b)
    if not a or not b:return []
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]=(c[i+j]+v*w)%P
    return remainder(c,F)


def power_mod(a,n):
    if type(n) is not int or n<0:raise ValueError("nonnegative integer exponent")
    c=[1];a=remainder(a,F)
    while n:
        if n&1:c=multiply_mod(c,a)
        a=multiply_mod(a,a);n//=2
    return c


def polynomial_gcd(a,b):
    a=trim(a);b=trim(b)
    while b:a,b=b,remainder(a,b)
    return trim([v*pow(a[-1],-1,P) for v in a]) if a else []


def irreducibility_certificate():
    x=[0,1]
    x_p=power_mod(x,P)
    x_ppppp=power_mod(x,P**5)
    x_p_minus_x=[((x_p[i] if i<len(x_p) else 0)-(x[i] if i<len(x) else 0))%P
                 for i in range(max(len(x_p),len(x)))]
    return {
        "f_mod_5":trim(F),
        "x_to_5_pow_5_mod_f":x_ppppp,
        "gcd_f_x_to_5_minus_x":polynomial_gcd(F,x_p_minus_x),
        "irreducible":x_ppppp==x and polynomial_gcd(F,x_p_minus_x)==[1],
    }

if __name__=="__main__":
    import json
    receipt=irreducibility_certificate()
    assert receipt["irreducible"]
    print(json.dumps(receipt,indent=2))
    print("PASS irreducible mod 5 => irreducible over Q; rank four quotient characters")
