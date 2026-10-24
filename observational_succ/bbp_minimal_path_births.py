"""Four-pole BBP source -> unbounded prime births, minimal recurrence depth.

No statistical normality is asserted. Source-authority: corrected BBP PR #252,
Green coefficient PR #254 and first-birth source PR #256, all ancestors of
this research stack. The PNT-AP asymptotic and irrationality of pi are
classical external theorems, not assertions checked by these finite oracles.

Finite source complexity != bounded p-primary carrier != Hankel rank !=
radix-16 normality. See BBP_MINIMAL_PATH_GALOIS_SELECTION.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt

from .bbp_cyclotomic_birth import birth_index, p_adic_valuation, forced_states
from .bbp_source_memory import (
    forcing, tail_interval, rational_counterfeit_tail,
    rational_counterfeit_forcing,
)


def _nat(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return n


def _prime(p: int) -> int:
    _nat(p,3)
    if p % 2 == 0 or any(p % j == 0 for j in range(3,isqrt(p)+1,2)):
        raise ValueError("odd rational prime required")
    return p


def primes_at_most(bound: int) -> tuple[int,...]:
    """Tiny, transparent finite oracle; no prime distribution assumption."""
    _nat(bound)
    if bound < 3:
        return ()
    flags=bytearray(b"\x01")*(bound+1)
    flags[:2]=b"\x00\x00"
    for p in range(2,isqrt(bound)+1):
        if flags[p]:
            flags[p*p::p]=b"\x00"*len(flags[p*p::p])
    return tuple(p for p in range(3,bound+1,2) if flags[p])


def prime_births_through(horizon: int) -> tuple[tuple[int,int],...]:
    """(p,first n) for EVERY odd prime born by time horizon.

    Source-first birth_index handles all four residues mod 8 and rejects
    composites. Prime count grows without bound, but simultaneity,
    independent entropy, and normality do not follow.
    """
    _nat(horizon)
    return tuple((p,birth_index(p)) for p in primes_at_most(8*horizon)
                 if birth_index(p)<=horizon)


def prime_birth_count_formula(horizon: int) -> tuple[int,int,int,int]:
    """Exact cumulative counts by p mod8, in order (1,5,3,7).

    Combined total B(N)=pi(8N-7;8,1)+pi(8N-3;8,5)
                        +pi(4N-1;8,3)+pi(4N-1;8,7).
    External PNT-AP gives B(N)~6N/log N; finite code proves no limit.
    """
    _nat(horizon)
    samples=primes_at_most(8*horizon)
    return (
        sum(p%8==1 and p<=8*horizon-7 for p in samples),
        sum(p%8==5 and p<=8*horizon-3 for p in samples),
        sum(p%8==3 and p<=4*horizon-1 for p in samples),
        sum(p%8==7 and p<=4*horizon-1 for p in samples)
    )


def check_first_birth_against_real_state(p: int) -> dict:
    """Exact authentic BBP selected Q/Z state has v_p=-1 at first birth."""
    _prime(p)
    n=birth_index(p)
    states=forced_states(n)
    if n>1 and p_adic_valuation(states[n-2],p)<0:
        raise AssertionError("prime entered before certified first birth")
    if p_adic_valuation(states[n-1],p)!=-1:
        raise AssertionError("source p-primary birth valuation mismatch")
    return {"p":p,"birth":n,"before_integral":n==1 or
            p_adic_valuation(states[n-2],p)>=0,
            "new_valuation":-1}


def counterfeit_selected_state(n: int) -> Q:
    """Finite, rational, positive-Green source with selected orbit ZERO.

    T*_n=1/[(n+1)(n+2)], 16T*_0=8, y*_0=0,
    y*_n=(-T*_n) mod 1 for n>=1; no pi source identification.
    """
    _nat(n)
    return Q() if n==0 else (-rational_counterfeit_tail(n))%1


def counterfeit_birth_step(p: int) -> int:
    """New denominator p at n=p-2, every odd prime, despite zero orbit."""
    _prime(p)
    return p-2


def counterfeit_denominator_witness(p: int) -> dict:
    _prime(p)
    n=p-2
    current=counterfeit_selected_state(n)
    previous=counterfeit_selected_state(n-1)
    if p_adic_valuation(current,p)!=-1:
        raise AssertionError("periodic-orbit counterfeit failed p birth")
    if previous != 0 and p_adic_valuation(previous,p)<0:
        raise AssertionError("counterfeit p already present")
    return {"p":p,"birth":n,"first_valuation":-1,
            "selected_circle_phase":Q()}


def green_homogeneous_second_order(n: int) -> tuple[Q,Q]:
    """T_(n+2)=(16+R_n)T_(n+1)-16R_n T_n (rational coefficients)."""
    _nat(n)
    ratio=forcing(n+2)/forcing(n+1)
    return Q(16)+ratio,Q(16)*ratio


def green_order_two_residual_interval(n: int, terms: int = 12) -> tuple[Q,Q]:
    """Independent full source-tail rational interval for residual=0."""
    _nat(n);_nat(terms,1)
    a,b=green_homogeneous_second_order(n)
    e0,e1=tail_interval(n,terms)
    f0,f1=tail_interval(n+1,terms)
    g0,g1=tail_interval(n+2,terms)
    if a<=0 or b<=0:
        raise AssertionError("positive forcing ratio lost")
    return (g0-a*f1+b*e0,g1-a*f0+b*e1)


def rational_first_order_impossibility(n: int, scalar: Q) -> tuple[Q,Q]:
    """A checkable algebraic premise of the minimality proof.

    For rational c, T_(n+1)=c*T_n would imply
        (16-c)T_n=r(n+1)>0 rational.
    T_n=16^(n-1)*pi - rational is irrational (classical irrational pi).
    If c=16 then LHS=0; otherwise LHS irrational. Both contradictions.
    Returns the two rational obstruction parameters, NOT a numeric
    computation of pi irrationality.
    """
    _nat(n)
    if type(scalar) not in (int,Q):
        raise ValueError("rational recurrence scalar required")
    return Q(16)-Q(scalar),forcing(n+1)


def finite_prime_support_no_go(horizon: int, allowed_primes) -> tuple[int,int]:
    """Smallest missing birth at or before horizon; source cannot use only P.

    A finite forbidden-set proof must examine a requested finite horizon.
    If no such birth exists in that horizon, report ValueError, not a
    universal theorem about future support.
    """
    _nat(horizon)
    allowed=tuple(_prime(p) for p in allowed_primes)
    missing=next(((p,n) for p,n in prime_births_through(horizon)
                  if p not in allowed),None)
    if missing is None:
        raise ValueError("no unseen source mode in the requested horizon")
    return missing


def counterfeit_first_step() -> Q:
    """Independent algebraic source recurrence check."""
    return (Q(16)*counterfeit_selected_state(0)
            +rational_counterfeit_forcing(1))%1



def prime_power_first_birth(p: int, depth: int) -> int:
    """First authentic BBP forcing index containing a p^depth denominator.

    Exact for EVERY odd prime p and depth>=1, not only the filtered
    p²=1 mod8 result of parent PR #256. At this time the full y-state has
    valuation -depth; all earlier full states have valuation >=1-depth.
    """
    _prime(p);_nat(depth,1)
    q=p**depth
    if q%8==1:
        return (q+7)//8
    if q%8==5:
        return (q+3)//8
    return (q+1)//4


def prime_power_birth_test(p: int, depth: int, state_cost_cap: int=350) -> dict:
    """Small exact-rational full-source validation of the all-depth proof.

    The cost cap concerns this instrument, NOT the theorem. Invalid oversized
    requests are rejected rather than falsely certified from sparse samples.
    """
    _prime(p);_nat(depth,1);_nat(state_cost_cap,1)
    n=prime_power_first_birth(p,depth)
    if n>state_cost_cap:
        raise ValueError("exact state witness exceeds declared finite cost cap")
    q=p**depth
    for j in range(1,n):
        if any(denom%q==0 for denom in
               (8*j-7,8*j-4,8*j-3,8*j-2)):
            raise AssertionError("earlier p-power forcing intervention found")
    if not any(denom%q==0 for denom in
               (8*n-7,8*n-4,8*n-3,8*n-2)):
        raise AssertionError("no source event at claimed p-power birth")
    s=forced_states(n)
    before=s[n-2] if n>1 else Q()
    after=s[n-1]
    if (before!=0 and p_adic_valuation(before,p)<1-depth):
        raise AssertionError("full state had premature p-adic depth")
    if p_adic_valuation(after,p)!=-depth:
        raise AssertionError("authentic full state failed new prime-power depth")
    return {"p":p,"depth":depth,"birth":n,"valuation":-depth}


def integer_root_floor(n: int, depth: int) -> int:
    """Exact floor(n^(1/depth)) with integer arithmetic only."""
    _nat(n);_nat(depth,1)
    lo,hi=0,1
    while hi**depth<=n:
        lo=hi;hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**depth<=n:
            lo=mid
        else:
            hi=mid
    return lo


def prime_power_birth_count(horizon: int,depth: int) -> int:
    """Count each new p^depth valuation layer at its first forcing event.

    External PNT-AP: fixed even k -> k*8^(1/k)*N^(1/k)/log N;
    fixed odd k -> k*(8^(1/k)+4^(1/k))/2*N^(1/k)/log N.
    These are event counts, not simultaneously present p-adic ranks.
    """
    _nat(horizon);_nat(depth,1)
    maxp=integer_root_floor(8*horizon,depth)
    return sum(prime_power_first_birth(p,depth)<=horizon
               for p in primes_at_most(maxp))
