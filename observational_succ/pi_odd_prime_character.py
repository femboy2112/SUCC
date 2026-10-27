"""Exact local--global additive-character decomposition for odd-denominator rationals.

For a reduced A/B with B positive and odd, CRT gives
    A/B mod 1 = sum_{p^k || B} (A*(B/p^k)^(-1) mod p^k)/p^k mod 1.
Thus the real Fourier phase is a product of odd-prime local characters.
This is a deterministic identity, NOT a claim of independent local phases.

Factorization is explicitly bounded to keep this a small finite oracle.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import prod


def _odd_prime_powers(B: int, trial_limit: int = 100000) -> tuple[tuple[int,int], ...]:
    if type(B) is not int or B < 1 or B % 2 == 0:
        raise ValueError('positive odd denominator required')
    if type(trial_limit) is not int or trial_limit < 3:
        raise ValueError('positive factoring budget required')
    powers=[]
    remaining=B
    p=3
    while p*p<=remaining:
        if p>trial_limit:
            raise ValueError('prime factorization exceeds declared trial bound')
        if remaining%p==0:
            exponent=0
            while remaining%p==0:
                remaining//=p
                exponent+=1
            powers.append((p,exponent))
        p+=2
    if remaining>1:
        powers.append((remaining,1))
    assert prod(p**k for p,k in powers)==B
    return tuple(powers)


def odd_prime_phase_factors(value: Q, h:int=1, trial_limit:int=100000) -> tuple[tuple[int,int,Q], ...]:
    """Return (odd prime, valuation, exact phase modulo 1) for e(h*value).

    Standard local additive characters use the opposite sign, so the
    adelic product e(h*value)*product_p psi_p(h*value)=1.
    """
    if type(value) not in (int,Q) or type(h) is not int:
        raise ValueError('exact rational and integral character required')
    u=Q(value)
    if u.denominator%2==0:
        raise ValueError('not Z2-integral: denominator has a 2-adic part')
    A=h*u.numerator
    B=u.denominator
    output=[]
    for p,k in _odd_prime_powers(B,trial_limit):
        modulus=p**k
        cofactor=B//modulus
        residue=A*pow(cofactor,-1,modulus)%modulus
        output.append((p,k,Q(residue,modulus)))
    actual=(sum((part for _,_,part in output),Q()))%1
    if actual!=(h*u)%1:
        raise ArithmeticError('local-global CRT phase product failed')
    return tuple(output)


def rank_filtered_phase(value:Q, h:int, primes:tuple[int,...]) -> tuple[Q,Q,Q]:
    """Signed phase selected prime subset + residual + original real phase.

    Filtering source primes does not sample independent randomness.
    """
    if type(primes) is not tuple or any(type(p) is not int for p in primes):
        raise ValueError('tuple of prime labels required')
    factors=odd_prime_phase_factors(value,h)
    selection=set(primes)
    known=sum((phase for p,k,phase in factors if p in selection),Q())%1
    residual=sum((phase for p,k,phase in factors if p not in selection),Q())%1
    actual=(h*Q(value))%1
    assert (known+residual)%1==actual
    return known,residual,actual
