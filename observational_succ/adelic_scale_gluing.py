"""Authentic BBP all-scale transport, adelic magnitude, and harmonic defect.

Research-only, paper-proved elementary bounds.  This DOES NOT bound the
original zero-selected Weyl mean or prove pi normality. The rational product
formula remembers magnitudes, NOT the selected real-circle character.

Main XXI's observational_succ.duck_bbp.forcing is the ONLY imported source.
No seeds, poles, historical files or repository defaults are modified.
"""
from __future__ import annotations
from fractions import Fraction
from math import isqrt
from observational_succ.duck_bbp import forcing


def _natural(value: int, name: str, lower: int = 0) -> int:
    if type(value) is not int or value < lower:
        raise ValueError(f"{name} must be an integer >= {lower}")
    return value


def source_defect(start: int, steps: int) -> Fraction:
    """F_{start,steps} = sum_{j=1}^steps 16^(steps-j) r(start+j).

    Equals U_{start+steps}(s)-16^steps U_start(s) for EVERY seed s.
    """
    _natural(start, "start")
    _natural(steps, "steps", 1)
    return sum((16**(steps-j)*forcing(start+j) for j in range(1, steps+1)), Fraction(0))


def cocycle(start: int, left_steps: int, right_steps: int) -> tuple[Fraction, Fraction]:
    """Two equal rational readings across a composite reference-frame change."""
    _natural(start, "start")
    _natural(left_steps, "left_steps", 1)
    _natural(right_steps, "right_steps", 1)
    direct = source_defect(start, left_steps+right_steps)
    factored = 16**right_steps*source_defect(start, left_steps) + source_defect(start+left_steps, right_steps)
    return direct, factored


def leading_scale(steps: int) -> Fraction:
    """c_k=(16^k-1)/64, source-anchored leading real-scale coefficient."""
    _natural(steps, "steps", 1)
    return Fraction(16**steps-1,64)


def harmonic_coefficient(steps: int) -> Fraction:
    """beta_k= -7/8 + 2k/(16^k-1), the exact next BBP source jet."""
    _natural(steps, "steps", 1)
    return Fraction(-7,8)+Fraction(2*steps,16**steps-1)


def normalized_defect(start: int, steps: int) -> Fraction:
    """R_{n,k}= n^2 F_{n,k}/c_k > 0, for n>=1."""
    _natural(start, "start", 1)
    _natural(steps, "steps", 1)
    return source_defect(start,steps)*Fraction(64*start*start,16**steps-1)


def rational_second_order_residual(start: int, steps: int) -> Fraction:
    """Exact residual bounded uniformly in steps by 298/(25*n^2)."""
    return normalized_defect(start,steps) - 1 - harmonic_coefficient(steps)/start


def residual_bound(start: int) -> Fraction:
    _natural(start, "start", 1)
    return Fraction(298,25*start*start)


def log_remainder_bound(start: int) -> Fraction:
    """For ALL k>=1, |log R_(n,k) - beta_k/n| <=16/n^2 for n>=16.

    The logarithm is NOT numerically evaluated here. This bound is analytic.
    """
    _natural(start, "start", 16)
    return Fraction(16,start*start)


def source_counterseed(epoch: int) -> tuple[Fraction, Fraction]:
    """Source-computed DYADIC seed and a rigorous mean |U_n(s)| upper bound.

    N=2A+10, M=8A+80; seed uses only finite exact r(1)...r(N),
    not pi digits or any pi oracle. The seed varies with epoch A.
    For A>=1, average_{A<=n<2A}|U_n(s)| <= returned bound.
    The fixed 2^-80 error is divided by A before summation; a false
    UNIFORM tending-to-zero bound is intentionally not used.
    """
    _natural(epoch, "epoch", 1)
    A=epoch; N=2*A+10; M=8*A+80
    alpha=sum((forcing(j)/16**j for j in range(1,N+1)), Fraction(0))
    lattice=2**M
    seed=-Fraction((alpha*lattice).numerator//(alpha*lattice).denominator,lattice)
    upper = (Fraction(1,2**80*15*A)
             + Fraction(1,16**10*225*A*(2*A+11)**2)
             + Fraction(1,15*(A+1)**2))
    return seed,upper


def _factor(n: int) -> dict[int,int]:
    """Small-integer trial division, only used for exact finite receipts."""
    _natural(n,"n",1)
    primes={}
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0: n//=p; e+=1
            primes[p]=e
        p=3 if p==2 else p+2
    if n>1: primes[n]=primes.get(n,0)+1
    return primes


def finite_place_valuations(value: Fraction) -> dict[int,int]:
    """Nonzero rational -> finite list v_p(value) for receipt-sized examples.

    This is the complete support, not just a selected p or the 2-primary part.
    Use logarithmic product formula in proofs rather than floating logs.
    """
    if not isinstance(value,Fraction) or value==0:
        raise ValueError("nonzero rational required")
    n=_factor(abs(value.numerator));d=_factor(value.denominator)
    return {p:n.get(p,0)-d.get(p,0) for p in sorted(n.keys()|d.keys()) if n.get(p,0)!=d.get(p,0)}


def finite_place_product(value: Fraction) -> Fraction:
    """Exact product over finite primes of |value|_p; equals 1/|value|_infty."""
    val=finite_place_valuations(value)
    out=Fraction(1)
    for p,v in val.items(): out*=Fraction(1,p**v) if v>=0 else p**(-v)
    return out


def weyl_variation_upper(prime_prefix_bound: float, complement: tuple[complex,...]) -> float:
    """Abel bound B*(|last|+total variation)/A for supplied |partial sums a|<=B.

    Generic analytic inequality. To apply to original p-local a_n one must
    separately establish B from full FOUR-stage prime-character history.
    """
    if not complement or prime_prefix_bound<0: raise ValueError("invalid profile")
    total=abs(complement[-1])+sum(abs(complement[i+1]-complement[i]) for i in range(len(complement)-1))
    return prime_prefix_bound*total/len(complement)


def four_pole_denominator(n: int) -> int:
    """Frozen BBP rational denominator D(n) in the declared degree-two class."""
    _natural(n, "n", 1)
    return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)


def _prime(p: int) -> bool:
    if type(p) is not int or p<2:
        return False
    for d in range(2,isqrt(p)+1):
        if p%d==0: return False
    return True


def source_numerator_from_one_finite_place(
    p: int = 41, digits: int = 2, coefficient_bound: int = 120,
    sampled_values: tuple[Fraction,Fraction,Fraction] | None = None,
) -> tuple[int,int,int]:
    """Recover P(x)=a*x^2+b*x+c from exact p-adic samples at 1,2,3.

    A TYPED finite-to-analytic theorem: assumes exact denominator D,
    integer numerator coefficients of degree <=2 and |a|,|b|,|c|<=B,
    a prime with D(1..3) units and p^digits>2B. It determines the
    continuous rational function P(x)/D(x) inside THIS source class.
    It does NOT determine the selected real orbit or its Fourier limits.
    """
    _natural(digits, "digits", 1)
    _natural(coefficient_bound, "coefficient_bound", 1)
    if not _prime(p) or p==2:
        raise ValueError("an odd prime is required")
    m=p**digits
    if m<=2*coefficient_bound:
        raise ValueError("finite-place precision below the coefficient bound")
    if any(four_pole_denominator(j)%p==0 for j in (1,2,3)):
        raise ValueError("a sampled source denominator is not a p-adic unit")
    samples=(forcing(1),forcing(2),forcing(3)) if sampled_values is None else sampled_values
    if not isinstance(samples,tuple) or len(samples)!=3 or not all(isinstance(q,Fraction) for q in samples):
        raise ValueError("three exact rational source samples required")
    y=[]
    for j,q in enumerate(samples,1):
        if q.denominator%p==0:
            raise ValueError("sample is not p-integral")
        y.append((four_pole_denominator(j)*q.numerator*pow(q.denominator,-1,m))%m)
    a=((y[2]-2*y[1]+y[0])*pow(2,-1,m))%m
    b=(y[1]-y[0]-3*a)%m
    c=(y[0]-a-b)%m
    center=lambda v: v if 2*v<m else v-m
    res=tuple(center(v) for v in (a,b,c))
    if any(abs(v)>coefficient_bound for v in res):
        raise ValueError("samples violate the declared numerator coefficient bound")
    return res
