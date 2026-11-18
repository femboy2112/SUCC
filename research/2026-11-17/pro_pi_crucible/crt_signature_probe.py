"""Exact finite calibration of M-02; no EPS cutoff or asymptotic claim.

Predeclared checks: enumerate all fractional numerators directly, compare
the complete signature with the theorem's progression, check both directions,
the exact word count, and the zero-word criterion. Include q > K and q = 1
controls so injectivity is not silently assumed outside its domain.
No repository modules or external numerical libraries are used.
"""

from fractions import Fraction as F
from math import gcd, prod
import json


def factor(n):
    result = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = 1
    return result


def phi(n):
    result = n
    for p in factor(n):
        result = result//p*(p-1)
    return result


def r(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def residue(z, modulus):
    return z.numerator*pow(z.denominator, -1, modulus) % modulus


def check(u, selected, shell, name):
    n, den = u.numerator, u.denominator
    pi = prod(selected)
    assert den % pi == 0 and den % 2 == 1
    q = den//pi
    assert gcd(pi, q) == 1
    assert all(factor(den)[p] == 1 for p in selected)
    k = 16**shell
    a = residue(u, k)
    r0 = n % pi
    actual_word = (n//den) % k
    target_principal = tuple(residue(p*u, p) for p in selected)
    progression = {}
    for t in range(q):
        numer = r0+t*pi
        if gcd(numer, q) != 1:
            continue
        word = (a-pow(den, -1, k)*r0-pow(q, -1, k)*t) % k
        v = F(word) + F(numer, den)
        assert v.denominator == den
        assert residue(v, k) == a
        assert tuple(residue(p*v, p) for p in selected) == target_principal
        assert (v.numerator//v.denominator) % k == word
        progression[t] = word
    assert len(progression) == phi(q)
    if q <= k:
        assert len(set(progression.values())) == phi(q)
    assert actual_word in progression.values()
    t0 = (q*a-pow(pi, -1, k)*r0) % k
    # The one-candidate iff statement is used only under q <= K.
    if q <= k:
        zero_possible = t0 < q and gcd(r0+t0*pi, q) == 1
        assert (0 in progression.values()) == zero_possible

    direct = None
    # Independent reverse enumeration for small denominators. No M-02 formula
    # is used to select the fractional numerator or the integer word here.
    if den <= 300:
        direct = {}
        for fractional_numer in range(den):
            for word in range(k):
                v = F(word) + F(fractional_numer, den)
                if v.denominator != den or residue(v, k) != a:
                    continue
                if tuple(residue(p*v, p) for p in selected) != target_principal:
                    continue
                assert fractional_numer % pi == r0
                direct[(fractional_numer-r0)//pi] = word
        assert direct == progression
    return {'name':name,'B':shell,'Q':str(den),'Pi':str(pi),'q':q,
            'admissible_t':len(progression),'distinct_words':len(set(progression.values())),
            'phi_q':phi(q),'q_le_radix':q <= k,'authentic_word_in_set':True,
            'zero_word_present':0 in progression.values(),'t0':t0,
            'reverse_enumeration_performed':direct is not None}


u6 = F(0)
for clock in range(1, 7):
    u6 = 16*u6+r(clock)
selected6 = tuple(p for p, exponent in factor(u6.denominator).items() if p > 7)
rows = [check(F(7,15),(3,),1,'small two-prime example'),
        check(F(11,105),(3,5,7),1,'q equals one'),
        check(F(7,255),(3,5),1,'q exceeds radix; no injectivity claim'),
        check(u6,selected6,3,'literal U6, all denominator primes above seven')]
assert rows[-1]['q'] == 525 and rows[-1]['admissible_t'] == 240
print(json.dumps({'status':'PASS','scope':'Four finite M-02 calibrations; no EPS threshold asserted for Y=7 at n=6',
                  'cases':rows},indent=2))
