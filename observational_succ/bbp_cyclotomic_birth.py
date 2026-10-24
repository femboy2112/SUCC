"""Exact first BBP prime births, primitive clock regimes and time-CRT controls.

Research scope: the authentic index forcing and y0=0 from bbp_source_memory;
prime-local signed periods are not the selected global pi Weyl sums.
See research/2026-10-24/BBP_CYCLOTOMIC_BIRTH_AND_LAG.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd, isqrt

from observational_succ.bbp_source_memory import forcing, forced_step


def _prime(p: int) -> int:
    if type(p) is not int or p < 3 or p % 2 == 0 or any(p % j == 0 for j in range(3, isqrt(p)+1, 2)):
        raise ValueError("odd rational prime required")
    return p


def birth_index(p: int) -> int:
    """First index where the authentic BBP source forcing has a p-pole."""
    _prime(p)
    if p % 8 == 1: return (p+7)//8
    if p % 8 == 5: return (p+3)//8
    return (p+1)//4


def first_phase_residue(p: int) -> int:
    """Canonical p-primary phase numerator modulo p, at the first birth."""
    _prime(p)
    if p % 8 == 1: return 4 % p
    if p % 8 == 5: return (p-1) % p
    return (-pow(2,-1,p)) % p


def next_pole_gap(p: int) -> int:
    """Exact number of consecutive indices n>=birth with no later p-pole.

    The interval is birth_index(p) <= n < birth_index(p)+gap;
    p divides exactly one source denominator at the left endpoint and no
    source denominator at the remaining indices.
    """
    _prime(p)
    return {1:(3*p-3)//8, 5:(3*p+1)//8, 3:(p+5)//8, 7:(p+1)//8}[p%8]


def pole_denominators(n: int) -> tuple[int, int, int, int]:
    if type(n) is not int or n < 1: raise ValueError("n>=1 required")
    return 8*n-7, 8*n-4, 8*n-3, 8*n-2


def p_adic_valuation(q: Q, p: int) -> int:
    """v_p(q) for nonzero rational q."""
    _prime(p)
    q=Q(q)
    if q==0:raise ValueError("valuation of 0 is infinite")
    n=abs(q.numerator); d=q.denominator; value=0
    while n%p==0:n//=p;value+=1
    while d%p==0:d//=p;value-=1
    return value


def p_primary_phase(q: Q, p: int) -> int:
    """Numerator in (1/p)Z/Z of a rational whose denominator has p exactly once.

    Q/Z decomposition into p-primary and prime-to-p parts; returns c with
    q = c/p + q_other (mod 1) and denom(q_other) coprime to p.
    """
    _prime(p)
    q=Q(q)
    if p_adic_valuation(q,p)!=-1:
        raise ValueError("exactly one p-primary denominator digit required")
    m=q.denominator//p
    return (q.numerator*pow(m,-1,p)) % p


def forced_states(count: int) -> tuple[Q,...]:
    if type(count) is not int or count<0:raise ValueError("count >=0")
    result=[]; state=Q()
    for n in range(1,count+1):
        state=forced_step(state,n)
        result.append(state)
    return tuple(result)


def multiplicative_order_16(p: int) -> int:
    _prime(p)
    residue=16%p; state=residue; order=1
    while state != 1:
        state=state*residue%p;order+=1
        if order>p-1:raise AssertionError("bad prime residue order")
    return order


def first_window_residues(p: int) -> tuple[int,...]:
    """Exact time sequence of p-primary numerators over the first pole-free window."""
    n=birth_index(p); gap=next_pole_gap(p)
    return tuple(first_phase_residue(p)*pow(16,t,p)%p for t in range(gap))


def full_cycle_count(p: int) -> int | None:
    """For p==1 mod 8 the entire first free window is complete cycles."""
    _prime(p)
    if p%8 != 1:return None
    period=multiplicative_order_16(p)
    gap=next_pole_gap(p)
    if gap%period:raise AssertionError("missing quadratic-residue-of-2 fact")
    return gap//period


def cyclic_autocorrelation_residues(p: int, lag: int) -> tuple[int,...]:
    """Complete-period local lag characters, excluding end-window truncation."""
    _prime(p)
    if type(lag) is not int or lag<0:raise ValueError("lag >=0")
    if p%8!=1:raise ValueError("complete first window requires p==1 mod 8")
    multiplier=(pow(16,lag,p)-1)*first_phase_residue(p)%p
    return tuple((multiplier*z)%p for z in (pow(16,t,p) for t in range(next_pole_gap(p))))


def galois_mean_squared(p: int) -> Q:
    """Exact mean over a in Fp* of abs(sum_{t<Delta} e(a eps16^t/p))^2.

    Only defined for a complete local period window (p==1 mod 8).
    No selected-embedding bound follows from this mean.
    """
    if p%8!=1:raise ValueError("p==1 mod 8 required")
    delta=next_pole_gap(p); L=multiplicative_order_16(p)
    return Q(delta*delta*(p-L),L*(p-1))



def source_window_split(p: int) -> tuple[tuple[int,Q], ...]:
    """Authentic BBP y_n = (p-primary numerator)/p + p-unit complement.

    Requires p=8m+1 prime. Times n=m+1..4m, inclusive. At every step
    the complementary rational denominator is prime to p. All exact.
    """
    _prime(p)
    if p%8!=1: raise ValueError("complete split window needs p==1 mod 8")
    m=(p-1)//8
    states=forced_states(4*m)
    residues=first_window_residues(p)
    parts=tuple((a,(states[m+t]-Q(a,p))%1) for t,a in enumerate(residues))
    if any(q.denominator%p==0 for _,q in parts):
        raise AssertionError("p-free source transport lost its residue carrier")
    return parts


def within_block_complement_variation(p: int) -> Q:
    """Exact total circle-distance variation of the p-free complement,
    excluding bridges between completed L_p-period blocks. This is an
    absolute-value *sufficient bound diagnostic*, not signed cancellation.
    """
    parts=source_window_split(p)
    L=multiplicative_order_16(p)
    return sum((min((parts[j+1][1]-parts[j][1])%1,
                    (parts[j][1]-parts[j+1][1])%1)
                for j in range(len(parts)-1) if (j+1)%L!=0),Q())

def construct_coprime_clock_counterfeit(p: int, horizon: int, padding: int = 2) -> tuple[Q,int]:
    """A second p-coprime clock forces the global phase almost stationary.

    x = eps_p/p + s/Q, gcd(Q,p)=1, |x|<=1/(2Q), Q odd, and
    sum_{t<horizon} e(16^t x) is within < (22/7)*(16^horizon-1)/(15Q)
    of horizon (using pi<22/7). The p-clock is unchanged.
    """
    _prime(p)
    if type(horizon) is not int or horizon < 1:raise ValueError("positive horizon")
    if type(padding) is not int or padding < 0:raise ValueError("padding >=0")
    Qn=16**(horizon+padding)+1
    if Qn%p==0:Qn+=2
    assert Qn%2==1 and gcd(Qn,p)==1
    epsilon=first_phase_residue(p)
    # nearest integer epsilon*Qn/p; no float or round-half-to-even
    s=-((2*epsilon*Qn+p)//(2*p))
    phase=Q(epsilon,p)+Q(s,Qn)
    assert abs(phase)<=Q(1,2*Qn)
    assert p_primary_phase(phase,p)==epsilon
    return phase,Qn


def counterfeit_upper(horizon: int, coprime_denominator: int) -> Q:
    """Strict rational upper bound on |sum e(16^t*x)-horizon|."""
    if type(horizon) is not int or horizon<1:raise ValueError("positive horizon")
    if type(coprime_denominator) is not int or coprime_denominator<1:raise ValueError("positive denominator")
    return Q(22*(16**horizon-1),7*15*coprime_denominator)


def exceptional_prime_count_bound(X: int) -> int:
    """Proof bound for primes p<=X with ord_p(16)<=p^(1/3).

    Each such p divides product_{m<=floor(cuberoot X)}(16^m-1).
    Number distinct prime factors <= log_2(product) < 2M(M+1).
    """
    if type(X) is not int or X<1:raise ValueError("X >=1")
    lo,hi=0,1
    while hi**3<=X:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**3<=X:lo=mid
        else:hi=mid
    M=lo
    return 2*M*(M+1)
