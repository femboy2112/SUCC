"""BBP carrier-return / circle-excitation instrument (research, 2026-11-15).

No pi digit fixture. Original exact four-pole forcing and literal U_0=0.
Finite circle certificates use rational BBP Green-tail brackets. This module
proves no asymptotic real equidistribution estimate.
"""
from __future__ import annotations

from fractions import Fraction
from math import sin, pi
from typing import NamedTuple


def forcing(n: int, leading: int = 4) -> Fraction:
    if not isinstance(n, int):
        raise TypeError("integer source index required")
    return (Fraction(leading, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def frac(x: Fraction) -> Fraction:
    return x - x.numerator // x.denominator


def source_states(count: int, leading: int = 4) -> list[Fraction]:
    if count < 0:
        raise ValueError("count must be nonnegative")
    states = [Fraction(0)]
    for n in range(1, count + 1):
        states.append(frac(16 * states[-1] + forcing(n, leading)))
    return states


def lifted_source_states(count: int, leading: int = 4) -> list[Fraction]:
    """Unreduced rational states; integer winding is deliberately retained."""
    if count < 0:
        raise ValueError("count must be nonnegative")
    states = [Fraction(0)]
    for n in range(1,count+1):
        states.append(16*states[-1]+forcing(n,leading))
    return states


def modular_source_states(count: int, modulus: int, leading: int = 4) -> list[int]:
    if modulus <= 0 or modulus & (modulus - 1):
        raise ValueError("positive power-of-two modulus expected")
    states = [0]
    for n in range(1, count + 1):
        rat = forcing(n, leading)
        assert rat.denominator % 2 == 1
        states.append((16*states[-1] + rat.numerator*pow(rat.denominator,-1,modulus)) % modulus)
    return states


def green_tail_interval(n: int, depth: int = 12) -> tuple[Fraction, Fraction]:
    """Inherited original-source strict enclosure; no mutated source permitted."""
    if n < 0 or depth < 0:
        raise ValueError("nonnegative n and depth required")
    partial = Fraction(0)
    for j in range(depth,0,-1):
        partial=(forcing(n+j)+partial)/16
    remainder = forcing(n+depth+1) / (15 * 16**depth)
    return partial, partial+remainder


def distance_to_nearest_integer(x: Fraction) -> Fraction:
    y=frac(x)
    return min(y,1-y)


def distance_interval_lower(lo: Fraction, hi: Fraction) -> Fraction:
    """Guaranteed min ||t|| over t in rational interval [lo,hi]."""
    if lo > hi:
        raise ValueError("reversed interval")
    left=lo.numerator//lo.denominator
    right=hi.numerator//hi.denominator
    if left != right or lo == left:
        return Fraction(0)
    return min(lo-left, 1-(hi-left))


class PulseCertificate(NamedTuple):
    q: int
    n: int
    distance_lower: Fraction
    distance_upper_bound: Fraction
    interval_width: Fraction
    passed: bool


def circle_pulse_certificate(states: list[Fraction], q: int, n: int,
                             depth: int = 16) -> PulseCertificate:
    """A strictly rational certificate of the pi-circle loop separation.

    z_m={U_m+T_m}; delta=(U_{n+q}-U_n)+(T_{n+q}-T_n) (mod 1).
    Bounds are valid because the original four-pole future tail decreases.
    """
    if q < 1 or n < 0 or n+q >= len(states):
        raise ValueError("insufficient source states")
    lo1,hi1=green_tail_interval(n,depth)
    lo2,hi2=green_tail_interval(n+q,depth)
    ratdiff=states[n+q]-states[n]
    lo=ratdiff+lo2-hi1
    hi=ratdiff+hi2-lo1
    floor_lb=distance_interval_lower(lo,hi)
    # Upper bound for distance is merely 1/2; use centered-midpoint for diagnostics.
    return PulseCertificate(q,n,floor_lb,Fraction(1,2),hi-lo,
                            floor_lb >= Fraction(1,17))


def clock_jet(states: list[int], k: int, n: int) -> int:
    q=16**k
    if n+q >= len(states):
        raise ValueError("states must cover n+q")
    # states are already reduced modulo 16*q, so their difference is 0 mod q.
    step=(states[n+q]-states[n])%(16*q)
    if step % q:
        raise AssertionError("source clock did not close at q")
    return (step//q)%16


def predicted_jet(n: int) -> int:
    return 11 if n%4 in (0,1) else 3


def first_certified_pulse(q: int, start: int, count: int = 20,
                          depth: int = 16) -> PulseCertificate | None:
    states=source_states(q+start+count)
    for n in range(start,start+count):
        c=circle_pulse_certificate(states,q,n,depth)
        if c.passed:
            return c
    return None


def pulse_energy_threshold() -> float:
    """Illustrative numerical energy floor; theorem uses symbolic sine."""
    return 4*sin(pi/17)**2


def return_jet_table(q: int, indices: int = 12, leading: int = 4) -> list[int]:
    v=modular_source_states(q+indices, 16*q, leading)
    return [clock_jet(v,k_from_q(q),n) for n in range(indices)]


def k_from_q(q: int) -> int:
    k=0
    value=1
    while value < q:
        value*=16
        k+=1
    if value!=q or k<1:
        raise ValueError("q=16^k for k>=1 required")
    return k


def source_denominator_factorization(d: int, n: int) -> dict[int,int]:
    """Factor d using the actual BBP source conductor restriction p<=8*n.

    d must be the reduced denominator of U_n with n>=1. This is NOT a
    general-purpose arbitrary-integer factorization: source provenance bounds
    each possible prime since each r(j) has factors <=8j and 16 is integral.
    """
    if n<1 or d<1 or d%2==0:
        raise ValueError("original odd source denominator required")
    rem=d
    out={}
    for p in range(3,8*n+1,2):
        if rem%p:
            continue
        # We may encounter composite p; earlier trial factors exhaust their
        # prime divisors, hence a new divisor of rem is necessarily prime.
        count=0
        while rem%p==0:
            rem//=p
            count+=1
        out[p]=count
        if rem==1:
            break
    if rem!=1:
        raise AssertionError("denominator requires an unauthorized prime >8n")
    return out


def source_crt_passport(n: int, unwrapped: Fraction) -> dict:
    """Exact real / all odd-prime CRT source phase passport.

    Sum of component fractions equals fractional part of source rational
    modulo one. The full integer winding is separately preserved.
    """
    if n<1:
        raise ValueError("n>=1")
    m=unwrapped.numerator//unwrapped.denominator
    d=unwrapped.denominator
    b=unwrapped.numerator-m*d
    factors=source_denominator_factorization(d,n)
    local=[]
    reconstructed=Fraction(0)
    for p,v in sorted(factors.items()):
        power=p**v
        cofactor=d//power
        k=(b*pow(cofactor,-1,power))%power
        reconstructed+=Fraction(k,power)
        local.append((p,v,k))
    winding=reconstructed-Fraction(b,d)
    if winding.denominator !=1:
        raise AssertionError("CRT real-phase decomposition failed")
    return {"n":n,"integer_winding":m,"numerator_remainder":b,
            "odd_denominator":d,"local_characters":local,
            "crt_reconstruction_integer":int(winding)}
