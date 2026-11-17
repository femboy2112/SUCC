"""Exact finite prime-path/CRT/negative-zeta certificates; no pi-normality claims."""
from fractions import Fraction
from itertools import combinations
from math import gcd, prod, isqrt


def primes_through(bound: int) -> tuple[int, ...]:
    """Elementary primality list, used only as a declared source oracle."""
    return tuple(n for n in range(2, bound+1)
                 if all(n % d for d in range(2, isqrt(n)+1)))


def validate_primes(primes: tuple[int, ...]) -> None:
    if len(set(primes)) != len(primes) or any(p < 2 or any(p % d == 0 for d in range(2, int(p**0.5)+1)) for p in primes):
        raise ValueError("source labels must be distinct authenticated primes")


def sieve(primes: tuple[int, ...], n: int) -> int:
    validate_primes(primes)
    return int(all(n % p for p in primes))


def signed_faces(primes: tuple[int, ...], n: int) -> int:
    """Empty-face-normalized signed sum over the divisor-path simplex."""
    validate_primes(primes)
    div = tuple(p for p in primes if n % p == 0)
    return sum((-1)**k * sum(1 for _ in combinations(div, k)) for k in range(len(div)+1))


def simplex_euler_char(primes: tuple[int, ...], n: int) -> int:
    """Unreduced ordinary Euler char, with chi(empty)=0."""
    validate_primes(primes)
    div = tuple(p for p in primes if n % p == 0)
    return sum((-1)**(k-1) * sum(1 for _ in combinations(div, k)) for k in range(1,len(div)+1))


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError(n)
    if n == 1:
        return 1
    k=0
    d=2
    while d*d <= n:
        if n % d == 0:
            n//=d
            k+=1
            if n % d == 0:
                return 0
            while n % d == 0:
                n//=d
        d+=1
    if n>1:
        k+=1
    return (-1)**k


def divisors(n: int) -> list[int]:
    return [d for d in range(1,n+1) if n%d==0]


def ramanujan(q: int, h: int) -> int:
    return sum(d*mobius(q//d) for d in divisors(gcd(q,h)))


def bernoulli_even(m: int, x: Fraction) -> Fraction:
    if m==1:
        return x*x-x+Fraction(1,6)
    if m==2:
        return x**4-2*x**3+x*x-Fraction(1,30)
    if m==3:
        return x**6-3*x**5+Fraction(5,2)*x**4-Fraction(1,2)*x*x+Fraction(1,42)
    raise ValueError("audit covers m=1..3")


def negative_odd_residue(primes: tuple[int,...], m: int) -> Fraction:
    validate_primes(primes)
    q=prod(primes)
    assert q>=1
    return -Fraction(q**(2*m-1),2*m)*sum(
        (bernoulli_even(m,Fraction(a,q)) for a in range(1,q+1) if gcd(a,q)==1),
        Fraction(0))


def negative_odd_factor(primes: tuple[int,...], m: int) -> Fraction:
    zeta={1:Fraction(-1,12),2:Fraction(1,120),3:Fraction(-1,252)}[m]
    return zeta*prod(1-p**(2*m-1) for p in primes)


def finite_euler_minus_one(primes: tuple[int,...]) -> Fraction:
    validate_primes(primes)
    return Fraction(1,prod(1-p for p in primes))


def is_new_prime(n: int) -> bool:
    if n<2:
        return False
    return bool(sieve(primes_through(int(n**0.5)),n))


def full_demo():
    for primes in [(),(2,),(2,3),(2,3,5),(2,3,5,7)]:
        q=prod(primes)
        for n in range(1,max(50,2*q)+1):
            assert sieve(primes,n)==signed_faces(primes,n)==1-simplex_euler_char(primes,n)
            assert sieve(primes,n)==int(gcd(n,q)==1)
        for m in (1,2,3):
            assert negative_odd_residue(primes,m)==negative_odd_factor(primes,m)
        assert negative_odd_residue(primes,1)*finite_euler_minus_one(primes)==Fraction(-1,12)
        for h in range(q):
            expected=prod((p-1 if h%p==0 else -1) for p in primes)
            assert ramanujan(q,h)==expected
    for n in range(2,1000):
        assert is_new_prime(n)==(n in primes_through(n))
    # Fake six is not a prime place: its sieve is redundant after 2 and 3,
    # but its Euler factor would corrupt any purported authentic product.
    for n in range(1,100):
        assert sieve((2,3),n)==(sieve((2,3),n)*(1-int(n%6==0)))
    return 'exact certificates passed'

if __name__ == '__main__':
    print(full_demo())
