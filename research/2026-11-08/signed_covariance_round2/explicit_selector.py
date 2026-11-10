"""Integer selector and rational eighth-power classical character bound."""
from fractions import Fraction as Q
from math import isqrt
from lag_instrument import Interval, SCALE


def primes_to(limit):
    if type(limit) is not int or limit < 0:
        raise ValueError('nonnegative integer limit required')
    sieve = bytearray(b'\1')*(limit+1)
    sieve[:min(2, limit+1)] = b'\0'*min(2, limit+1)
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p] = b'\0'*(((limit-p*p)//p)+1)
    return [p for p in range(2, limit+1) if sieve[p]]


def order16_factored(p):
    if type(p) is not int or p < 3 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError('odd prime required')
    value, divisors, d = p-1, [], 2
    while d*d <= value:
        if value % d == 0:
            divisors.append(d)
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        divisors.append(value)
    order = p-1
    for d in divisors:
        while order % d == 0 and pow(16, order//d, p) == 1:
            order //= d
    return order


def select(A, C=2):
    if type(A) is not int or A < 1 or type(C) is not int or C < 1:
        raise ValueError('positive integer epoch and logarithmic cost required')
    for p in reversed(primes_to(4*A)):
        if p % 8 == 1:
            m = order16_factored(p)
            if m**3 > p and m*m*p.bit_length()**(2*C) > p:
                return p, m
    return None


def classical_cap8(p, m):
    if type(p) is not int or p < 3 or type(m) is not int or m < 1 or (p-1) % m:
        raise ValueError('positive subgroup order dividing p-1 required')
    if any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError('prime modulus required')
    return min(Q(1), Q(p**4, m**8), Q(256*p*p, 9*m**5), Q(256*p, 9*m**3))


def eighth_root_interval(value):
    value = Q(value)
    if not 0 <= value <= 1:
        raise ValueError('eighth-power cap in [0,1] required')
    target = value.numerator*SCALE**8
    lo, hi = 0, SCALE
    while lo < hi:
        mid = (lo+hi)//2
        if mid**8*value.denominator < target:
            lo = mid+1
        else:
            hi = mid
    lower = lo if lo**8*value.denominator == target else lo-1
    return Interval(lower, lo)
