"""Exact source-relative p-adic delta gates and factorial Poisson SUCC controls.

Deterministic SUCC words are CRT-compatible only under genuine prime-power
constraints. Poisson time ordering is a stochastic model, not a prime law.
All source equality decisions are exact; no numerical complex phasors.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, gcd, isqrt

MAX_MODULUS = 10**12
MAX_PRIME = 100_000
MAX_EXPONENT = 30
MAX_DISPLACEMENT = 100_000


class ContactError(ValueError):
    pass


def typed(x: int, name: str, low: int, high: int) -> int:
    if type(x) is not int or not low <= x <= high:
        raise ContactError(f"{name}: integer in {low}..{high} required")
    return x


def prime_power(p: int, exponent: int) -> int:
    if (type(p) is not int or not 2 <= p <= MAX_PRIME
            or any(p % d == 0 for d in range(2, isqrt(p)+1))):
        raise ContactError("genuine bounded prime required")
    typed(exponent, "depth", 1, MAX_EXPONENT)
    return typed(p**exponent, "prime-power modulus", 2, MAX_MODULUS)


@dataclass(frozen=True)
class PhaseContact:
    a: int
    b: int
    c: int
    prime: int
    depth: int
    modulus: int
    valuation: int
    relative_phase: int | None
    locked: bool


def abc_prime_power_contact(a: int, b: int, p: int, e: int) -> PhaseContact:
    """Given primitive a+b=c, check -a*b^(-1) == 1 modulo p^e.

    When p|b, b has no inverse, but primitivity makes p∤a and the
    output-cancellation gate automatically fails. The source is NOT guessed.
    """
    typed(a, "a", 1, MAX_MODULUS//2)
    typed(b, "b", 1, MAX_MODULUS//2)
    if gcd(a,b)!=1:
        raise ContactError("primitive gcd(a,b)=1 required")
    modulus=prime_power(p,e)
    c=a+b
    typed(c,"c",2,MAX_MODULUS)
    n, v = c, 0
    while n % p == 0:
        n//=p
        v+=1
    phase = (-a*pow(b,-1,modulus))%modulus if b%p else None
    locked = (c % modulus == 0)
    if locked != (phase==1):
        raise AssertionError("relative source phase != actual sum condition")
    return PhaseContact(a,b,c,p,e,modulus,v,phase,locked)


@dataclass(frozen=True)
class TimedPrimeGate:
    prime: int
    depth: int
    target: int
    succ: int

    def __post_init__(self) -> None:
        m=prime_power(self.prime,self.depth)
        typed(self.target,"residue target",0,m-1)
        typed(self.succ,"SUCC displacement",0,MAX_DISPLACEMENT)


@dataclass(frozen=True)
class ClockWordCRT:
    compatible: bool
    initial_residue: int | None
    combined_period: int
    cumulative_displacement: int


def deterministic_succ_gate_crt(word: tuple[TimedPrimeGate, ...]) -> ClockWordCRT:
    """A prime-clock delta sandwich corresponds to a single CRT source class.

    The j-th projector checks n0 + sum_{i<=j}succ_i mod p_j^e_j.
    A repeated prime can make the gate word EXACTLY ZERO. A reported
    period for incompatible words describes the first failed prefix.
    """
    if type(word) is not tuple or not word or any(type(g) is not TimedPrimeGate for g in word):
        raise ContactError("nonempty tuple of genuine prime-power gates required")
    x,mod,offset=0,1,0
    for gate in word:
        q=prime_power(gate.prime,gate.depth)
        offset+=gate.succ
        wanted=(gate.target-offset)%q
        g=gcd(mod,q)
        new_mod=mod*(q//g)
        if new_mod>MAX_MODULUS:
            raise ContactError("CRT product exceeds exact budget")
        if (wanted-x)%g:
            return ClockWordCRT(False,None,new_mod,offset)
        t=(((wanted-x)//g)*pow(mod//g,-1,q//g))%(q//g) if q//g>1 else 0
        x=(x+mod*t)%new_mod
        mod=new_mod
    return ClockWordCRT(True,x,mod,offset)


def poisson_gate_coefficients(q: int, N: int) -> tuple[tuple[int,...],tuple[int,...]]:
    """Deterministic +1 SUCC, start at phase 1, q is prime.

    Terminal gate: q|number_of_jumps.
    Gate after EVERY jump: only zero jumps survive.
    """
    prime_power(q,1)
    typed(N,"jump cutoff",0,MAX_DISPLACEMENT)
    return (tuple(int(n%q==0) for n in range(N+1)),
            tuple(int(n==0) for n in range(N+1)))


def poisson_polynomial(t: Q, coefficients: tuple[int,...]) -> Q:
    """Unscaled sum c_n t^n/n!. Actual probability needs factor exp(-t)."""
    if (type(t) is not Q or t<0 or type(coefficients) is not tuple
            or not coefficients or any(type(c) is not int or c not in (0,1)
                                        for c in coefficients)):
        raise ContactError("nonnegative rational time and 0/1 coefficients")
    return sum((Q(c)*t**n/factorial(n)
                for n,c in enumerate(coefficients)),Q())


def poisson_tail_bound(t: Q, cutoff: int) -> Q:
    """Certified Poisson-normalized remainder <=t^(N+1)/(N+1)!."""
    if type(t) is not Q or t<0:
        raise ContactError("nonnegative rational time required")
    typed(cutoff,"Poisson cutoff",0,100)
    return t**(cutoff+1)/factorial(cutoff+1)
