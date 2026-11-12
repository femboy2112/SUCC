"""Exact finite factorization/phase-cylinder SUCC experiments. Python >=3.10.

Paper model only. Neither this algorithm nor its finite checks prove Goldbach.
All phase-averaging identities are evaluated via integer root-of-unity congruences;
there is no floating-point cancellation posing as an exact certificate.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from math import isqrt


@lru_cache(None)
def prime_factors(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError('positive integers only')
    result = []
    m = n
    p = 2
    while p*p <= m:
        while m % p == 0:
            result.append(p)
            m //= p
        p += 1 if p == 2 else 2
    if m > 1:
        result.append(m)
    return tuple(result)


def is_prime(n: int) -> bool:
    return n > 1 and prime_factors(n) == (n,)


def omega(n: int) -> int:
    return len(prime_factors(n))


def defect(n: int) -> int:
    """B=(Omega-1)_+, whose zero sector comprises 1 and primes."""
    return max(omega(n)-1, 0)


def divisor_count(n: int) -> int:
    c = Counter(prime_factors(n))
    result = 1
    for exponent in c.values():
        result *= exponent + 1
    return result


def split_terms(n: int) -> tuple[tuple[int, int], ...]:
    """Ordered reduced coproduct Delta|n> = sum_(ab=n,a,b>=2)|a,b>."""
    if n < 1:
        raise ValueError('positive integers only')
    terms = []
    for a in range(2, isqrt(n)+1):
        if n % a == 0:
            b = n // a
            terms.append((a,b))
            if a != b:
                terms.append((b,a))
    return tuple(sorted(terms))


def commutator_number_eigenvalue(n: int) -> int:
    """P_H[Q*,Q]P_H |n> = (tau(n)-2)|n> for n>=2, 0 for 1."""
    return max(divisor_count(n)-2, 0)


def categorical_walk(n: int) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Unique deterministic factor extraction; context retains original product."""
    if n < 1:
        raise ValueError('positive integers only')
    m, ctx = n, ()
    states = [(m,ctx)]
    while m > 1 and not is_prime(m):
        p = prime_factors(m)[0]
        m //= p
        ctx = tuple(sorted(ctx + (p,)))
        states.append((m,ctx))
    assert all(m0 * __import__('math').prod(c0) == n for m0,c0 in states)
    return tuple(states)


def first_primes(count: int) -> tuple[int, ...]:
    result = []
    n = 2
    while len(result) < count:
        if categorical_walk(n)[-1][0] == n:  # Only n=prime survives when n>=2.
            result.append(n)
        n += 1
    return tuple(result)


def pair_grade(n: int, d: int) -> int:
    if n < 2 or abs(d) > n-2:
        raise ValueError('need n>=2, and both endpoints >=2')
    return defect(n+d)+defect(n-d)


def phase_polynomial(n: int, *, signed: bool = False) -> dict[int,int]:
    """Coefficient of z^k counts midpoint positions of defect k."""
    ds = range(-n+2,n-1) if signed else range(n-1)
    return dict(sorted(Counter(pair_grade(n,d) for d in ds).items()))


def exact_phase_average(n: int, M: int, *, signed: bool = False) -> int:
    """M-root angular average, EXACT: only modes divisible by M survive."""
    if M < 1:
        raise ValueError('positive phase count required')
    return sum(v for k,v in phase_polynomial(n,signed=signed).items() if k%M==0)


def safe_phase_count(n: int) -> int:
    """M > max pair_grade(n,d), using ab=n^2-d^2<=n^2 and Omega(k)<=log2(k)."""
    if n < 2:
        raise ValueError('n>=2')
    return 2*n.bit_length()


def witnesses(n: int, *, signed: bool = False) -> tuple[int,...]:
    ds = range(-n+2,n-1) if signed else range(n-1)
    return tuple(d for d in ds if is_prime(n+d) and is_prime(n-d))


def wiggle_edges(n: int, *, parity_restricted: bool = True) -> tuple[tuple[int,int],...]:
    """Nearest-neighbor d -> d+2 edges on the finite midpoint fiber."""
    if n < 2:
        raise ValueError('n>=2')
    ds = range(n-1)
    allowed = [d for d in ds if not parity_restricted or n==2 or (n+d)%2]
    positions = set(allowed)
    return tuple((d,d+2) for d in allowed if d+2 in positions)


def commutator_frobenius_square(n: int) -> int:
    """||[H,W_2]||_F^2, H=diag(pair_grade), W_2 adjacency; exact."""
    return 2*sum((pair_grade(n,b)-pair_grade(n,a))**2 for a,b in wiggle_edges(n))


def counterfeit_commutator_no_witness() -> tuple[int, int]:
    """Positive spectral grades with nonzero wiggle commutator but no zero grade."""
    grade = (1,2,1,2,1)
    energy = 2*sum((grade[k+1]-grade[k])**2 for k in range(len(grade)-1))
    return sum(x==0 for x in grade), energy


def plaquette_holonomy(grade00: int, grade01: int, grade11: int, grade10: int) -> int:
    """Total oriented discrete gradient on a closed square: always zero."""
    return (grade01-grade00)+(grade11-grade01)+(grade10-grade11)+(grade00-grade10)


def prime_birth_commutator(n: int, p: int) -> int:
    """[B,V_p]|n> coefficient in |pn>; p must be prime."""
    if n<1 or not is_prime(p):
        raise ValueError('n>=1 and p prime')
    return defect(p*n)-defect(n)


def sample_report() -> dict:
    rows=[]
    for n in [2,3,4,10,32,64,100,256,1024]:
        M=safe_phase_count(n)
        rows.append({'n':n,'M':M,'phase_poly':phase_polynomial(n),
                     'witnesses':list(witnesses(n)),
                     'G':len(witnesses(n)),
                     'phase_avg_exact':exact_phase_average(n,M),
                     'alias_M2':exact_phase_average(n,2),
                     'wiggle_commutator_Frob2':commutator_frobenius_square(n)})
    return {'scope':'exact finite only; Goldbach OPEN','prime_prefix':first_primes(20),
            'rows':rows,'counterfeit':counterfeit_commutator_no_witness()}


if __name__=='__main__':
    import json
    print(json.dumps(sample_report(),indent=2))
