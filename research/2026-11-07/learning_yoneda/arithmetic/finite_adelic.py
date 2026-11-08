"""Exact finite-adic shadowing, with an explicit nonzero initial seed.

No pi digits or floating point enter the construction. These adversaries vary
with the requested future horizon. They are not counterexamples to pi normality.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt, prod
from observational_succ.selected_orbit import original_forcing


def exact_rational(value, name):
    if type(value) not in (int, Q):
        raise ValueError(f"{name} must be an exact int or Fraction")
    return Q(value)


def exact_integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


@lru_cache(maxsize=4096)
def _is_odd_prime(p):
    return p >= 3 and p % 2 == 1 and all(p % d for d in range(3,isqrt(p)+1,2))


def odd_prime(p):
    if type(p) is not int or not _is_odd_prime(p):
        raise ValueError("a genuine odd prime is required")
    return p


def prime_set(primes):
    if type(primes) not in (tuple, list, set, frozenset):
        raise ValueError("primes must be an explicitly finite collection")
    checked = tuple(odd_prime(p) for p in primes)
    if len(set(checked)) != len(checked):
        raise ValueError("duplicate primes are not permitted")
    return tuple(sorted(checked))


def forcing(n):
    exact_integer(n,"source time",1)
    return original_forcing(n)


def history(last, seed=Q(0)):
    exact_integer(last,"last time")
    values = [exact_rational(seed,"seed")]
    for n in range(1, last + 1):
        values.append(16 * values[-1] + forcing(n))
    return values


def ceilq(x):
    x = exact_rational(x,"ceiling input")
    return -((-x.numerator) // x.denominator)


def primes_through(n):
    exact_integer(n,"prime bound")
    sieve = bytearray(b'\x01') * (n+1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * ((n-p*p)//p+1)
    return tuple(i for i in range(3,n+1,2) if sieve[i])


def principal(x, p):
    """Canonical rational p-principal part in [0,1)."""
    p = odd_prime(p)
    x = exact_rational(x,"principal-part input")
    d = x.denominator
    pe = 1
    while d % p == 0:
        pe *= p
        d //= p
    if pe == 1:
        return Q(0)
    return Q((x.numerator * pow(d, -1, pe)) % pe, pe)


def residue(x, modulus):
    x = exact_rational(x,"residue input")
    exact_integer(modulus,"modulus",1)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def construct(J, A, L, K, eta, primes):
    for name,value in (("J",J),("A",A),("L",L),("K",K)):
        exact_integer(value,name)
    eta = exact_rational(eta,"eta")
    primes = prime_set(primes)
    if not (0 <= J < A and L >= 1 and K >= 0 and 0 < eta < Q(1,4)):
        raise ValueError("invalid chronology or precision")
    B = A + L - 1
    u = history(B)
    M = ceilq(u[B] / 16**(B-A))
    center = Q(M,16**A) - u[B]/16**B
    D = 2 * prod(primes)
    q_min = ceilq(Q(2**K * 16**B) / eta)
    q = 1 + D * ceilq(Q(q_min-1,D))
    m = max(1,ceilq(center*q/2**K))
    seed = Q(2**K*m,q)
    return {
        "J":J,"A":A,"L":L,"K":K,"B":B,"eta":eta,
        "primes":tuple(primes),"M":M,"center":center,"q":q,
        "m":m,"seed":seed,"original":u,"shadow":history(B,seed),
    }


def verify(witness):
    w=witness
    J,A,L,K,B,eta=(w[k] for k in ('J','A','L','K','B','eta'))
    u,v,s=w['original'],w['shadow'],w['seed']
    assert s > 0  # literal zero is deliberately NOT preserved
    assert 0 <= w['center'] < Q(1,16**A)
    assert 0 <= s-w['center'] <= eta/16**B
    assert s <= Q(1,16**A)+eta/16**B
    assert residue(s,2**K) == 0
    for n in range(B+1):
        assert v[n]-u[n] == 16**n*s
        assert residue(v[n]-u[n],2**(K+4*n)) == 0
        for p in w['primes']:
            assert principal(v[n],p) == principal(u[n],p)
    prefix_error = max(v[n]-u[n] for n in range(J+1))
    prefix_margin = min(1-(u[n] % 1) for n in range(J+1))
    assert prefix_error <= Q(16**J,16**A)+eta*Q(16**J,16**B)
    assert prefix_error < prefix_margin
    for n in range(J+1):
        assert v[n]//1 == u[n]//1
    for n in range(1,J+1):
        assert v[n]//1-16*(v[n-1]//1) == u[n]//1-16*(u[n-1]//1)
    residuals=[]
    tails=[]
    for n in range(A,B+1):
        tail=sum((forcing(j)/16**(j-n) for j in range(n+1,B+1)),Q(0))
        residual=v[n]-16**(n-A)*w['M']
        assert residual == -tail+16**n*(s-w['center'])
        assert 0 <= tail < Q(1,15*(n+1)**2)
        assert abs(residual) <= max(Q(1,15*(n+1)**2),eta*Q(16**n,16**B))
        residuals.append(residual)
        tails.append(tail)
    mean_square=sum((x*x for x in residuals),Q(0))/L
    # cos(2*pi*h*x) >= 1 - 2*pi^2*h^2*x^2 > 1-20*h^2*x^2
    lower={h:1-20*h*h*mean_square for h in (1,2,3,5)}
    return prefix_error,prefix_margin,residuals,lower
