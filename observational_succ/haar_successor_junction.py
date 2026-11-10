"""Exact high-road Haar / low-road signed-successor junction.

The finite inequalities here are valid for any digit path. In particular, they
DO NOT prove that the original BBP/zero-seeded pi path is normal.

High-road: first digit conditioned on its *future* suffix (Yoneda/Q twirl).
Low-road: last digit conditioned on its *past* prefix (16-child Haar details).
The de Bruijn graph provides their common oriented edge basis.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import isqrt

B = 16
ZERO = Fraction(0)


def word_law(digits: list[int], starts: int, depth: int, offset: int = 0):
    """Exact frequencies for `starts` word starts; no cyclic wrap is invented."""
    if starts < 1 or depth < 0 or offset < 0 or offset+starts+depth > len(digits)+1:
        raise ValueError("Insufficient actual future digits or invalid arguments")
    if any(not isinstance(d, int) or not 0 <= d < B for d in digits):
        raise ValueError("Expected real hexadecimal digits 0,...,15")
    counts = Counter(tuple(digits[i:i+depth]) for i in range(offset, offset+starts))
    return {w: Fraction(c, starts) for w, c in counts.items()}


def collision_energy(law, depth: int) -> Fraction:
    return B**depth*sum((x*x for x in law.values()), ZERO)-1


def signed_junction(digits: list[int], starts: int, depth: int):
    """Two Haar currents, de Bruijn gradient, signed successor spectral energy.

    Inputs describe `starts` consecutive *genuine* digit starts; the suffix
    marginal is separately sampled one real step later. Every reported energy
    is a Fraction, not rounded floating-point evidence.
    """
    if depth < 0 or starts < 1 or starts+depth+1 > len(digits):
        raise ValueError("Need starts+depth+1 genuine digits")
    p = word_law(digits, starts, depth)
    q = word_law(digits, starts, depth, offset=1)
    edge = word_law(digits, starts, depth+1)
    es = set(edge)
    for w in p:
        es.update(w+(a,) for a in range(B))
    for w in q:
        es.update((a,)+w for a in range(B))
    high = {e:edge.get(e,ZERO)-q.get(e[1:],ZERO)/B for e in es}
    low  = {e:edge.get(e,ZERO)-p.get(e[:-1],ZERO)/B for e in es}
    scale = B**(depth+1)
    kh = scale*sum((v*v for v in high.values()),ZERO)
    kl = scale*sum((v*v for v in low.values()),ZERO)
    seam = scale*sum(((high[e]-low[e])**2 for e in es),ZERO)
    common = scale*sum((((high[e]+low[e])/2)**2 for e in es),ZERO)
    gradient = seam/4  # half-difference energy; high=common+gradient iff stationary
    cross = scale*sum((((high[e]+low[e])/2)*((high[e]-low[e])/2) for e in es),ZERO)
    js = set(edge)
    js.update(e[:-1]+((e[-1]+1)%B,) for e in edge)
    successor = scale*sum(((edge.get(e,ZERO)-edge.get(e[:-1]+((e[-1]-1)%B,),ZERO))**2 for e in js), ZERO)
    ej = collision_energy(p,depth)
    ej1 = collision_energy(edge,depth+1)
    pmoment = sum((v*v for v in p.values()),ZERO)
    qmoment = sum((v*v for v in q.values()),ZERO)
    stationarity_l1 = sum((abs(p.get(w,ZERO)-q.get(w,ZERO)) for w in set(p)|set(q)),ZERO)
    # Exact, finite, no asymptotic hypotheses:
    assert kl == ej1-ej
    assert kh-kl == B**depth*(pmoment-qmoment)
    assert high.keys() == low.keys()
    assert cross == (kh-kl)/4
    assert common+gradient == (kh+kl)/2
    assert stationarity_l1 <= Fraction(2,starts)
    assert abs(kh-kl) <= Fraction(4*B**depth,starts)
    # Sharp theoretical constant = 2 - sqrt(2+sqrt(2)) > 3/20.
    # Use rational 3/20 for an exact, executable lower-bound certificate.
    assert 20*successor >= 3*kl
    assert successor <= 4*kl
    # At depth=0, these are the same 1-digit distribution; seam=0.
    if depth == 0:
        assert kh == kl and seam == 0
    return {
        "depth":depth,"starts":starts,"E_depth":ej,"E_next":ej1,
        "high_energy":kh,"low_energy":kl,"successor_energy":successor,
        "gradient_seam":seam,"common_energy":common,"half_gradient_energy":gradient,
        "common_gradient_inner":cross,"stationarity_l1":stationarity_l1,
        "high_L1":sum((abs(v) for v in high.values()),ZERO),
        "high":high,"low":low,"prefix":p,"suffix":q,"edges":edge,
    }


def rational_sqrt_upper(v: Fraction, bits: int = 48) -> Fraction:
    """Outward rational sqrt bound. Safe for positivity certificates."""
    if v < 0 or bits < 1:
        raise ValueError("sqrt nonnegative, bits>=1")
    z = 1 << bits
    return Fraction(isqrt(v.numerator*z*z//v.denominator)+1,z)


def haar_w1_upper(stats: dict, sqrt_bits: int = 48) -> Fraction:
    """Rigorous upper bound for interval W1 of an actual T(x)={16x} orbit.

    Only use with exact genuine digits; the formula combines RHY-02 from #565,
    interval-cell coupling, the two Haar energies, and a rational spectral gap.
    This function does not assert convergence for any particular source.
    """
    n,j = stats["starts"],stats["depth"]
    radicand = Fraction(20,3)*stats["successor_energy"] + Fraction(4*B**j,n)
    return Fraction(B,B-1)*(rational_sqrt_upper(radicand,sqrt_bits)/2 + Fraction(1,B**(j+1))) + Fraction(1,(B-1)*n)


def source_certified_digits(first: int, count: int, *, seed=Fraction(0), tail_depth: int = 12):
    """Certified digits of completed BBP path, using main's authenticated core.

    Exact four-pole `duck_bbp.forcing` and proven `tail_interval`; no pi oracle.
    A digit is returned only when the entire outward interval lies in one
    hexadecimal cell. `seed` must be an explicitly supplied rational.
    """
    from observational_succ import duck_bbp
    if first < 1 or count < 1 or tail_depth < 0:
        raise ValueError("bad positive source window")
    seed = Fraction(seed)
    state = seed % 1
    out, mids, radii = [], [], []
    for n in range(1, first+count):
        state=(B*state+duck_bbp.forcing(n)) % 1
        if n < first:
            continue
        lo,hi=duck_bbp.tail_interval(n,tail_depth)
        xlo,xhi=state+lo,state+hi
        low_digit = (B*xlo).numerator//(B*xlo).denominator
        high_digit = (B*xhi).numerator//(B*xhi).denominator
        if low_digit != high_digit:
            raise ValueError(f"Uncertified source digit n={n}; increase tail_depth")
        out.append(low_digit % B)
        mids.append((xlo+xhi)/2 % 1)
        radii.append((xhi-xlo)/2)
    return out,mids,max(radii)


def source_dyadic_shadow(A: int):
    """Dyadic wrong seed whose completed orbit shadows zero on [A,2A].

    The *seed* is NOT the original U0=0. Explicit, no unknown pi digits.
    The derived zero-window guarantee needs an appropriate tail_depth.
    """
    from observational_succ import duck_bbp
    if A < 2: raise ValueError("A>=2")
    N=2*A+16
    M=8*A+96
    alpha_prefix=duck_bbp.tail_interval(0,N)[0]
    scaled=alpha_prefix*2**M
    return -Fraction(scaled.numerator//scaled.denominator,2**M)


def exact_w1_to_haar(points: list[Fraction]) -> Fraction:
    """Quantile formula for interval-W1 of rational atoms against Lebesgue."""
    if not points: raise ValueError("empty")
    pts=sorted(points); n=len(pts);total=ZERO
    for i,x in enumerate(pts):
        if not 0<=x<=1: raise ValueError("points must lie in [0,1]")
        a,b=Fraction(i,n),Fraction(i+1,n)
        if x<=a: total+=(b*b-a*a)/2-x*(b-a)
        elif x>=b: total+=x*(b-a)-(b*b-a*a)/2
        else: total+=((x-a)**2+(b-x)**2)/2
    return total


def exact_w1_to_first_digit_twirl(points: list[Fraction]) -> Fraction:
    """Exact interval-W1 to Qmu=C T_*mu for rational phase representatives."""
    if not points: raise ValueError("empty")
    n=len(points);events=defaultdict(Fraction)
    for x in points:
        if not 0<=x<1: raise ValueError("points must lie in [0,1)")
        events[x]+=Fraction(1,n)
        y=(B*x)%1
        for a in range(B):
            events[(a+y)/B]-=Fraction(1,B*n)
    total=ZERO;last=ZERO;mass=ZERO
    for x in sorted(events):
        total+=(x-last)*abs(mass)
        mass+=events[x];last=x
    total+=(1-last)*abs(mass)
    assert mass==0
    return total


def temporal_succ_coboundary(values) -> Fraction:
    """Exact telescoping time-difference mean (always small, even if nonnormal)."""
    vals=list(values)
    if len(vals)<2: raise ValueError("need at least two values")
    return sum((vals[k]-vals[k+1] for k in range(len(vals)-1)), ZERO)/ (len(vals)-1)
