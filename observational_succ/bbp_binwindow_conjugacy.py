"""Exact coherent bin-window / 2-adic odometer of authentic four-pole BBP.

Original four-pole source is NOT modified.  We extend the *already-canceled*
rational source to Z_2 in a declared analytic continuation.  Main paper proof:
research/2026-10-27/BBP_BINWINDOW_ZERO_BOUNDARY.md.

The 2-adic infinite-past normalization is exactly zero for this source.
Hence n -> U_n extends to an isometric bijection of Z_2, a conjugacy of the
source-induced shift to the 2-adic adding machine.  This does NOT establish
any real-circle Weyl estimate or normality of pi.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd

from .succ_internal_matrix_walk import authentic_r

BASE = 16
SOURCE_TAG = "original-four-pole-BBP-canceled-rational-extension"


def _natural(n, name, lower=0, upper=1_000_000):
    if type(n) is not int or not lower <= n <= upper:
        raise ValueError(f"{name}: ordinary integer between {lower} and {upper}")
    return n


def _signed_index(n, name, bound=1_000_000):
    if type(n) is not int or abs(n) > bound:
        raise ValueError(f"{name}: exact integer of bounded magnitude")
    return n


def canceled_source_extension(n: int) -> Q:
    """Rational extension to negative integers: NOT an original negative-time observation."""
    _signed_index(n, "extended time")
    ans = Q(120*n*n - 89*n + 16,
            (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    if ans.denominator % 2 == 0:
        raise ArithmeticError("source lost odd-denominator authentication")
    return ans


def source_verified(n: int) -> Q:
    """Original positive-time forcing crosschecked against the native source."""
    _natural(n,"positive time",1)
    a = canceled_source_extension(n)
    if a != authentic_r(n):
        raise ArithmeticError("authentic BBP source changed")
    return a


def two_adic_mod(value: Q, hex_depth: int) -> int:
    """2-adic reduction of an odd-denominator rational mod 16**hex_depth."""
    _natural(hex_depth,"hex depth",1,64)
    if type(value) not in (int, Q):
        raise ValueError("exact integer/Fraction required")
    x = Q(value)
    if x.denominator % 2 != 1:
        raise ValueError("2-adic integer needs odd reduced denominator")
    modulus = BASE**hex_depth
    return (x.numerator * pow(x.denominator,-1,modulus)) % modulus


def past_boundary_partial(hex_depth: int) -> Q:
    """First k summands of C = sum_(s>=0) 16**s r(-s) in Q_2.

    The *paper proof*, not finite checks, gives C=0 in Q_2. The remaining
    tail is divisible by 16**k. Thus the returned rational must be zero
    modulo 16**k for every k, and this is checked independently by tests.
    """
    _natural(hex_depth,"hex depth",1,128)
    return sum((Q(BASE**s)*canceled_source_extension(-s)
                for s in range(hex_depth)),Q())


def zero_boundary_certificate(hex_depth:int) -> dict:
    k = _natural(hex_depth,"hex depth",1,128)
    prefix = past_boundary_partial(k)
    residue = two_adic_mod(prefix,k)
    if residue != 0:
        raise ArithmeticError("2-adic BBP zero boundary failed")
    return {"hex_depth":k,"modulus":BASE**k,"partial_sum":prefix,
            "modulus_residue":residue,"analytic_zero_proved_by_code":False,
            "paper_logarithmic_zero_identity":True}


def stationary_window(time:int,hex_depth:int) -> int:
    """The whole infinite 2-adic source clock modulo 16**k.

    n may be 0 or earlier than k; analytic extension to negative source
    indices is required in that case.  The resulting value is the actual
    positive-time U_n mod 16**k, including n=0, by the paper zero lemma.
    """
    n=_natural(time,"time",0,2_000_000)
    k=_natural(hex_depth,"hex depth",1,10)
    mod=BASE**k
    return sum((BASE**s*two_adic_mod(canceled_source_extension(n-s),k)
                for s in range(k)))%mod


def authentic_state(time:int)->Q:
    """Independent original zero-initial exact rational state."""
    n=_natural(time,"time",0,2500)
    u=Q()
    for j in range(1,n+1):
        u=BASE*u+source_verified(j)
    return u


def window_agrees_with_zero_seed(time:int,hex_depth:int)->dict:
    n=_natural(time,"time",0,2500)
    k=_natural(hex_depth,"hex depth",1,10)
    actual=two_adic_mod(authentic_state(n),k)
    stationary=stationary_window(n,k)
    if actual != stationary:
        raise ArithmeticError("window lost original zero seed")
    return {"time":n,"hex_depth":k,"direct_original":actual,
            "infinite_past_window":stationary,"source_selected":True}



def negative_time_ghost_completion(time:int,hex_depth:int)->dict:
    """The out-of-N part of an early finite window is a labelled ZERO witness.

    For n<k, sum_(s=n)^(k-1) 16**s r(n-s) is generally nonzero in Q,
    but vanishes modulo 16**k for this exact source. This result relies
    on the separately paper-proved p-adic zero boundary, NOT generic
    convolution. These negative indices are analytic extensions, not
    physical/observed negative source times.
    """
    n=_natural(time,"time",0)
    k=_natural(hex_depth,"hex depth",1,64)
    ghost=sum((Q(BASE**s)*canceled_source_extension(n-s)
               for s in range(n,k)),Q())
    code=two_adic_mod(ghost,k)
    if code!=0:raise ArithmeticError("the boundary ghost did not evaluate to zero")
    return {"time":n,"depth":k,"formal_negative_terms":max(0,k-n),
            "nonzero_rational_witness":ghost!=0,"ghost_rational":ghost,
            "ghost_residue_mod_16k":code,"source_requires_analytic_extension":n<k}


def causal_diagonal(time:int,hex_depth:int)->tuple[tuple[int,int,int,Q],...]:
    """(a,s,16**s,r(a)) with a=n-s, a+s=n: no independent samples."""
    n=_natural(time,"time",0)
    k=_natural(hex_depth,"window size",1,128)
    return tuple((n-s,s,BASE**s,canceled_source_extension(n-s))
                 for s in range(k))


def bin_reindex_multiplicity(start:int,stop:int,window:int)->dict[int,int]:
    """Count source a across all diagonals start <= a+s < stop.

    Every sufficiently interior source a is counted exactly `window` times.
    This is a deterministic Fubini/reindexing fact, NOT an independence law.
    """
    lo=_natural(start,"start",0)
    hi=_natural(stop,"stop",lo+1)
    w=_natural(window,"window",1,256)
    counts={}
    for n in range(lo,hi):
        for s in range(w):
            a=n-s
            counts[a]=counts.get(a,0)+1
    return dict(sorted(counts.items()))


def isometry_receipt(left:int,right:int,hex_depth:int)->dict:
    """Exact finite congruence iff: F_k(n)=F_k(m) mod16^k <=> n=m mod16^k."""
    a=_natural(left,"left index",0,2_000_000)
    b=_natural(right,"right index",0,2_000_000)
    k=_natural(hex_depth,"hex depth",1,10)
    modulus=BASE**k
    x,y=stationary_window(a,k),stationary_window(b,k)
    if (x==y)!=((a-b)%modulus==0):
        raise ArithmeticError("source-window isometry congruence failed")
    return {"a":a,"b":b,"depth":k,"same_source_bin":(a-b)%modulus==0,
            "same_target_bin":x==y}


@dataclass(frozen=True)
class OdometerCertificate:
    hex_depth:int
    modulus:int
    unique_residues:int
    time_zero_value:int
    one_cycle:bool
    first_hex_residues:tuple[int,...]
    real_circle_pi_normality_proved:bool=False


def odometer_certificate(hex_depth:int, maximum: int=4096)->OdometerCertificate:
    """Exact full finite permutation and conjugated successor; bounded budget.

    At k, time n mod16**k -> Phi(n) mod16**k is a permutation.  Its
    conjugated plus-one map on the output is one cycle, not a mixing
    theorem for the real-circle BBP orbit.
    """
    k=_natural(hex_depth,"hex depth",1,5)
    m=BASE**k
    if m>maximum:raise ValueError("exact permutation enumeration exceeds budget")
    output=tuple(stationary_window(n,k) for n in range(m))
    if len(set(output))!=m or output[0]!=0:
        raise ArithmeticError("time-to-source bins not a zero-marked permutation")
    inverse=[-1]*m
    for n,v in enumerate(output):inverse[v]=n
    successor=tuple(output[(inverse[v]+1)%m] for v in range(m))
    s=0; seen=set()
    for _ in range(m):
        if s in seen:break
        seen.add(s);s=successor[s]
    if len(seen)!=m or s!=0:
        raise ArithmeticError("source-induced successor is not an odometer")
    return OdometerCertificate(k,m,m,output[0],True,output[:16])


def first_hex_bin(time:int) -> int:
    """First digit of 2-adic time code: even n -> -n, odd n -> 2-n mod16.

    Derivation uses the exact canceled r(t) modulo 16, not real fractional
    hex digits. In particular this is an involution of the 16 residue bins.
    """
    n=_natural(time,"time",0)
    expected=(-n+(2 if n%2 else 0))%16
    value=stationary_window(n,1)
    if value!=expected:raise ArithmeticError("first source-bin involution changed")
    return value


def genuine_vs_2adic_Fourier_firewall()->dict:
    """A 2-adic character of an odd-denominator rational is NOT its real character."""
    u=authentic_state(1) # 47/15
    code=two_adic_mod(u,1)
    return {"original_real_fraction":u%1,"hexadic_code":code,
            "hexadic_turn":Q(code,16),"real_and_2adic_turns_distinct":Q(code,16)!=u%1,
            "all_selected_real_Weyl_cancellation_proved":False,
            "global_canonical_2adic_zero_proved_in_dossier":True}


def theorem_authority()->dict:
    return {"original_four_pole_source_unchanged":True,
            "two_adic_boundary_C_zero_paper":True,
            "all_time_2adic_clock_isometry_paper":True,
            "isometric_conjugacy_of_2adic_successor_paper":True,
            "pi_base16_normality_proved":False,
            "new_real_circle_signed_saving_proved":False}
