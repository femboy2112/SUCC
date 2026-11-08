"""Lambert W word-coverage clock and rigorous entropy amplification for hex digit paths.

Statements about pi require the authentic U0=0 BBP input from existing certified
sources; generic functions are deterministic finite-alphabet identities.
No normality or arithmetic cancellation theorem is asserted.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import log, sqrt, floor
from typing import Sequence

from .bbp_word_spectroscopy import word_counts_cyclic, word_energy, validate_digits

BASE=16
EULER_GAMMA=0.577215664901532860606512090082402431


def lambert_w_positive_log(logz:float) -> float:
    """Numerical principal W(exp(logz)): solve w+log(w)=logz (stable at huge N).

    A numerical depth scheduler, NOT a finite-number proof certificate.
    """
    if logz != logz:
        raise ValueError("NaN log input")
    w = max(0.1, logz-log(max(1.,logz))) if logz>1 else 1.
    for _ in range(80):
        residual=w+log(w)-logz
        nxt=w-residual/(1+1/w)
        if nxt<=0:
            nxt=w/2
        if abs(nxt-w)<1e-14*max(1,w):
            return nxt
        w=nxt
    raise ArithmeticError("Lambert-W Newton iteration did not converge")


@dataclass(frozen=True)
class LambertClock:
    horizon:int
    continuous_depth:float
    integer_depth:int
    continuous_types:float
    integer_types:int
    w:float


def lambert_clock(n:int) -> LambertClock:
    """Inverts N=B(log B+gamma), rounds depth DOWN to a positive integer."""
    if type(n) is not int or n<1:
        raise ValueError("horizon must be positive integer")
    w=lambert_w_positive_log(log(n)+EULER_GAMMA)
    x=(w-EULER_GAMMA)/log(BASE)
    k=max(1,floor(x+1e-12))
    return LambertClock(n, x, k, n/w, BASE**k, w)


def complete_coverage_reference(word_depth:int) -> dict:
    """Exact iid coupon mean for reasonable finite B; rare-event reference only."""
    if type(word_depth) is not int or not 1<=word_depth<=3:
        raise ValueError("exact coupon reference limited to depths 1..3")
    B=BASE**word_depth
    # H_B computed as floating approximation to avoid giant fraction JSON;
    # rational exact expectation is B*sum(Fraction(1,j), j=1..B).
    harmonic=sum(1/j for j in range(1,B+1))
    n=B*harmonic
    missing=B*(1-1/B)**n
    return {"depth":word_depth,"types":B,"mean_complete_draws":n,
            "mean_missing_at_mean":missing,
            "continuum_expected_missing":__import__('math').exp(-EULER_GAMMA)}


def entropy_diagnostics(digits:Sequence[int], depth:int) -> dict:
    """Exact rational collision energy; Shannon/Renyi entropies numeric diagnostics.

    Normality deductions rest on the exact inequalities in the paper dossier.
    """
    ds=validate_digits(digits)
    if type(depth) is not int or not 1<=depth<=len(ds):
        raise ValueError("invalid depth")
    counts=word_counts_cyclic(ds,depth)
    n=len(ds); B=BASE**depth
    e=word_energy(counts,n,depth)
    D=Fraction(n*n,B)*e
    coll=sum(v*v for v in counts.values())
    assert D==Fraction(coll)-Fraction(n*n,B)
    p2=Fraction(coll,n*n)
    s=sum((c/n)*log(n/c) for c in counts.values())
    maxc=max(counts.values())
    return {"depth":depth,"horizon":n,"types":B,"unique":len(counts),
            "missing":B-len(counts),"max_count":maxc,"energy":e,
            "D":D,"D_div_n":D/n,"collision_sum":coll,
            "renyi_deficit":log(1+float(e)),
            "shannon_deficit":depth*log(BASE)-s,
            "renyi_entropy":-log(float(p2)),
            "shannon_entropy":s,
            "max_count_over_average":maxc/(n/B),
            "signed_collision_term":Fraction(D-n*(1-Fraction(1,B)),2)}


def shannon_block_entropy(digits:Sequence[int], depth:int) -> float:
    ds=validate_digits(digits)
    c=word_counts_cyclic(ds,depth)
    n=len(ds)
    return sum((v/n)*log(n/v) for v in c.values())


def exact_overlap_returns(digits:Sequence[int], depth:int, max_lag:int) -> dict:
    """Noncyclic N= len(digits)-depth+1 chronological windows.

    Counts pair collisions by temporal lag. The signed Gram/Cauchy identity
    holds for every list of words; no positive drift is assumed.
    """
    ds=validate_digits(digits)
    if type(depth) is not int or depth<1 or depth>len(ds):
        raise ValueError("invalid depth")
    N=len(ds)-depth+1
    if type(max_lag) is not int or max_lag<0:
        raise ValueError("max_lag>=0")
    max_lag=min(max_lag,N-1)
    # Integer encoding of all sliding words, O(len(ds)).
    B=BASE**depth; m=B-1
    w=0
    for d in ds[:depth]:w=BASE*w+d
    ids=[w]
    for d in ds[depth:]:
        w=((w*BASE)+d)&m
        ids.append(w)
    c=Counter(ids)
    fullD=Fraction(sum(v*v for v in c.values()))-Fraction(N*N,B)
    pair_total=sum(v*(v-1)//2 for v in c.values())
    assert fullD==Fraction(N)*(1-Fraction(1,B))+2*(Fraction(pair_total)-Fraction(N*(N-1),2*B))
    rows=[]
    for lag in range(1,max_lag+1):
        matching=sum(a==b for a,b in zip(ids, ids[lag:]))
        expected=Fraction(N-lag,B)
        rows.append({"lag":lag,"pairs":N-lag,"matching":matching,
                     "signed_excess":Fraction(matching)-expected})
    return {"windows":N,"total_matches_unordered":pair_total,"D":fullD,
            "computed_lags":rows,
            "computed_lags_signed_total":sum((row['signed_excess'] for row in rows),Fraction()),
            "residual_lags_signed_total":Fraction(pair_total)-Fraction(N*(N-1),2*B)-sum((row['signed_excess'] for row in rows),Fraction())}


def entropy_amplification_bound(digits:Sequence[int], shallow_depth:int, deep_depth:int) -> dict:
    """Numerically checks an exact finite Shannon-subadditivity/Renyi theorem.

    Strict theorem: log(1+E_deep)>= floor(deep/t) *
       (t log16 - H_Shannon(p_t)); no asymptotics and no iid premise.
    """
    ds=validate_digits(digits)
    n=len(ds)
    if (type(shallow_depth) is not int or type(deep_depth) is not int or
        not 1<=shallow_depth<=deep_depth<=n):
        raise ValueError("1<=t<=k<=N")
    k=deep_depth;t=shallow_depth
    entropy_t=shannon_block_entropy(ds,t)
    deficit=max(0.,t*log(BASE)-entropy_t)
    deep=entropy_diagnostics(ds,k)
    lower=(k//t)*deficit
    delta=deep['renyi_deficit']
    if delta+1e-10<lower:
        raise AssertionError("finite entropy amplification theorem violated")
    return {"t":t,"k":k,"shannon_deficit_t":deficit,
            "renyi_deficit_k":delta,"proved_lower_bound":lower,
            "pinsker_l1_upper":sqrt(2*delta/(k//t))}


def sparse_insert_positions(j:int) -> tuple[int,int]:
    """Concrete construction schedule for normal-but-not-W-diffusive control."""
    if type(j) is not int or j<1:
        raise ValueError("j positive")
    origin=2**(2**j)
    length=2 if j==1 else 2**(3*2**(j-2))
    return origin,length


def trimmed_cyclic_entropy_bound(digits:Sequence[int], depth:int,
                                 threshold:int, fixed_depth:int=1) -> dict:
    """SCE-style trimmed *finite cyclic* entropy gate with original full marginals.

    Retain the earliest `threshold` occurrences per depth-k word; all other
    **time indices** are removed. The retained set is not assumed stationary.

    For t<=k, q=floor(k/t):
       q D_KL(p_t(full)||u_t) <= drop_fraction*k*ln16
                                 +(1-drop_fraction)*ln C_ret,
    where C_ret=16^k sum_(word) (retained_count/M)^2.
    Paper theorem is deterministic and applies to any chosen retained set.
    """
    ds=validate_digits(digits)
    n=len(ds)
    if (type(depth) is not int or not 1<=depth<=n or
        type(fixed_depth) is not int or not 1<=fixed_depth<=depth or
        type(threshold) is not int or threshold<1):
        raise ValueError('valid 1<=t<=k<=N and threshold>=1 required')
    B=BASE**depth
    all_counts=Counter()
    retained=[]
    for i in range(n):
        w=tuple(ds[(i+j)%n] for j in range(depth))
        all_counts[w]+=1
        if all_counts[w]<=threshold:
            retained.append(i)
    keep_counts=Counter({w:min(c,threshold) for w,c in all_counts.items()})
    kept=len(retained)
    assert sum(keep_counts.values())==kept
    removed=n-kept
    delta=Fraction(removed,n)
    excess=Fraction(B*sum(v*v for v in keep_counts.values()),kept*kept)
    upper=float(delta)*depth*log(BASE) + (1-float(delta))*log(float(excess))
    q=depth//fixed_depth
    full_entropy=shannon_block_entropy(ds,fixed_depth)
    actual=fixed_depth*log(BASE)-full_entropy
    if q*actual>upper+1e-9:
        raise AssertionError('trimmed source marginal inequality violated')
    return {"depth":depth,"fixed_depth":fixed_depth,"threshold":threshold,
            "retained":kept,"discarded":removed,"discarded_fraction":delta,
            "collision_excess_retained":excess,
            "untrimmed_collision_excess":1+entropy_diagnostics(ds,depth)['energy'],
            "kl_full_fixed_depth":actual,"max_allowed_kl":upper/q,
            "retained_time_indices":tuple(retained)}
