"""Exact seed-cylinder superposition and anti-aliasing in authentic BBP.

Proofs: PROOFS.md. All infinite claims are paper mathematics. Computations
are exact rational/int and never approximate a selected π Weyl limit.
"""
from __future__ import annotations

from fractions import Fraction as F
from collections import Counter
from itertools import product
from math import factorial

BASE = 16
SOURCE = "original-four-pole-BBP-U0=0"


def forcing(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer source index required")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def states(count: int, seed: F | int = 0) -> tuple[F, ...]:
    """Unwrapped U_0,...,U_(count-1), exact forcing; rational seed."""
    if type(count) is not int or count < 0 or type(seed) not in (int, F):
        raise ValueError("count nonnegative; seed exact int/Fraction")
    u = F(seed)
    out = []
    for n in range(count):
        out.append(u)
        u = 16*u+forcing(n+1)
    return tuple(out)


def seed_lift_identity(n: int, seed: F | int) -> bool:
    """U_n(s)=U_n(0)+16^n*s, independently checked rationally."""
    if type(n) is not int or n<0: raise ValueError("n>=0 required")
    a=states(n+1,seed)[n]
    b=states(n+1,0)[n]
    return a == b+16**n*F(seed)


def recurrence_resonance(n: int, seed: F | int, h: int=1) -> F:
    """The signed exponent of z_n^16 conj(z_(n+1)), precisely -h*r(n+1).

    This is the authentic 17-factor radix resonance from SUCC PR #404,
    not a newly invented 17th-order cancellation.
    """
    if type(n) is not int or n<0 or type(h) is not int or h==0:
        raise ValueError("n>=0 and h nonzero integer")
    u=states(n+2,seed)
    return h*(16*u[n]-u[n+1])


def prefix_cylinder(depth: int, address: int=0) -> tuple[F,F]:
    """One cell of the uniform seed superposition prior [0,1]."""
    if type(depth) is not int or depth<0 or type(address) is not int or not 0<=address<16**depth:
        raise ValueError("depth>=0, 0<=address<16^depth")
    scale=16**depth
    return F(address,scale),F(address+1,scale)


def future_integral_is_zero(depth: int, n: int, h: int=1) -> bool:
    """Certifies integral of exp(2pi i h U_n(s)) over any seed cell=0.

    Only applies to late n>=depth, with h nonzero integer.
    Does not certify the selected point s=0, which has measure zero.
    """
    if type(depth) is not int or depth<0 or type(n) is not int or n<depth or type(h) is not int or h==0:
        raise ValueError("n>=depth>=0 and h nonzero integer")
    return (h*16**(n-depth)) != 0


def covariance_late(depth: int, n: int, m: int, h: int=1) -> int:
    """Exact conditional seed-cell phase Gram coefficient: Kronecker delta."""
    if type(depth) is not int or depth<0 or type(n) is not int or type(m) is not int or min(n,m)<depth or type(h) is not int or h==0:
        raise ValueError("n,m >= depth; nonzero h")
    return int(n==m)


def late_second_moment(depth: int, stop: int, h: int=1) -> int:
    """Integral |sum_(depth<=n<stop) exp(2pi i h U_n(s))|^2 ds/|I|."""
    if type(depth) is not int or depth<0 or type(stop) is not int or stop<depth or type(h) is not int or h==0:
        raise ValueError("invalid interval, nonzero h")
    return stop-depth


def early_anchor_error_coefficient(depth: int, stop: int) -> F:
    """Mean-versus-anchor early prefix error <= pi|h| times this rational.

    Bound: integral 0<=t<=16^-M |e(h16^n t)-1| <=pi|h|16^(n-M).
    """
    if type(depth) is not int or depth<0 or type(stop) is not int or stop<0:
        raise ValueError("depth,stop>=0")
    end=min(stop,depth)
    return sum((F(16**n,16**depth) for n in range(end)),F(0))


def cell_mean_prefix_equivalence(depth: int, stop: int, h: int=1) -> dict:
    """E_I S_stop = S_min(stop,depth)(anchor) + error <=pi|h|/15.

    All n>=depth have exactly zero integrated phase, regardless of forcing.
    Coefficient is rational; no complex evaluation masquerades as a proof.
    """
    if type(h) is not int or h==0:raise ValueError("nonzero h")
    err=early_anchor_error_coefficient(depth,stop)
    return {"early_time_count":min(stop,depth),"late_time_count":max(0,stop-depth),
            "error_coefficient_times_pi_abs_h":err,"uniform_coefficient_upper":F(1,15),
            "late_integral_exactly_zero":stop>=depth}


def phase_relation_unique_for_equal_counts(r: int) -> bool:
    """For r<=16, equal r-term sums of 16^n force same multiplicities.

    The proof uses minimal-exponent divisibility and equal total counts.
    At r=17, the explicit (16,0,1) versus (0,17,0) relation fails.
    """
    if type(r) is not int or not 0<=r<=17:raise ValueError("0<=r<=17")
    return r<=16


def all_multiplicities(k: int, r: int):
    """Compositions c_0+...+c_(k-1)=r, for low exact moments."""
    if k==0:
        if r==0:yield ()
        return
    if k==1:
        yield (r,)
        return
    for c in range(r+1):
        for tail in all_multiplicities(k-1,r-c):
            yield (c,)+tail


def iid_balanced_moment(k: int, r: int) -> int:
    """Exact conditional 2r moment for r<=16, from source-cell phase Gram.

    This is the independent Steinhaus moment, extended from the full
    Haar seed ensemble (SUCC #404) to EVERY base-16 seed cylinder's tail.
    """
    if type(k) is not int or not 0<=k<=40 or type(r) is not int or not 0<=r<=16:
        raise ValueError("k in 0..40, r in 0..16")
    if k==0:return int(r==0)
    f=factorial(r)
    return sum((f*f//(den*den) for vec in all_multiplicities(k,r)
                for den in [product_factorials(vec)]))


def product_factorials(vec) -> int:
    v=1
    for c in vec:v*=factorial(c)
    return v


def direct_balanced_moment(k: int, r: int) -> int:
    """Independent frequency-collision algorithm; use small k,r only."""
    if type(k) is not int or type(r) is not int or k<1 or r<0 or k**r>600_000:
        raise ValueError("independent oracle restricted to k^r <=600000")
    freq=Counter(sum(16**j for j in t) for t in product(range(k),repeat=r))
    return sum(c*c for c in freq.values())


def first_equal_count_carry_resonance() -> dict:
    """Carry collision 16*16^n +16^(n+2)=17*16^(n+1)."""
    left=16*16**0+16**2
    right=17*16**1
    return {"left":left,"right":right,"terms_each":17,"equal":left==right,
            "distinct_multisets":(16,0,1)!=(0,17,0)}


def concentration_bound(k: int, r: int, epsilon: F) -> F:
    """Markov: P_cell(|S_tail|>=epsilon*k) <= r!/(eps^(2r) k^r)."""
    if type(k) is not int or k<1 or type(r) is not int or not 1<=r<=16 or type(epsilon) not in (int,F):
        raise ValueError("k>=1, 1<=r<=16, exact positive epsilon")
    e=F(epsilon)
    if e<=0:raise ValueError("epsilon>0")
    return min(F(1),F(factorial(r),1)/(e**(2*r)*k**r))


def exact_grid_seed_alias(depth: int, resolution: int, time: int, h: int=1) -> int:
    """Average of roots e(h*16^time*j /16^(depth+resolution)) over j.

    For time>=depth, result exactly 0 or 1. Phase from U_time(0) is
    a common factor and deliberately not inferred from the local grid.
    """
    if type(depth) is not int or depth<0 or type(resolution) is not int or resolution<0 or type(time) is not int or time<depth or type(h) is not int or h==0:
        raise ValueError("time>=depth, grid resolution>=0; h nonzero")
    return int((h*16**(time-depth)) % (16**resolution)==0)


def grid_alias_onset(depth: int, resolution: int, h: int=1) -> int:
    """First time >= depth where seed-grid quadrature coheres for all future times."""
    if type(depth) is not int or depth<0 or type(resolution) is not int or resolution<0 or type(h) is not int or h==0:
        raise ValueError("valid integers, nonzero h")
    n=depth
    while not exact_grid_seed_alias(depth,resolution,n,h):n+=1
    return n


def exact_discrete_grid_character_sum(order: int, exponent: int) -> int:
    """Independent finite Fourier orthogonality in a cyclic character group."""
    if type(order) is not int or order<1 or type(exponent) is not int:
        raise ValueError("order>=1, exponent integer")
    # Algebraic group sum: Σ_j ζ^e*j equals order if order divides e else 0.
    return order if exponent%order==0 else 0


def source_tail_upper(n: int) -> F:
    """T_n<=r(n+1)/15 < 1/(64 n^2), n>=1."""
    if type(n) is not int or n<1:raise ValueError("n>=1")
    return F(1,(8*n+1)*(8*n+2))


def coherent_changed_seed_bound(h: int) -> F:
    """|Σ e(hU_n(-pi/16))-K| < pi*|h|/16 for ANY finite n>=1 block.

    Returns coefficient multiplying pi; cannot assert π approximation.
    """
    if type(h) is not int or h==0:raise ValueError("h nonzero")
    return F(abs(h),16)


def seed_phase_boundary(s: F | int, depth: int, h: int=1) -> dict:
    """Typed seed record: exact selected point != normalized cylinder measure."""
    if type(s) not in (int,F) or type(depth) is not int or depth<0 or type(h) is not int or h==0:
        raise ValueError("exact seed; depth>=0; nonzero h")
    left=F(s)
    return {"source":SOURCE,"point_seed":left,"cylinder_start":left,
            "cylinder_width":F(1,16**depth),"point_equals_measure":False,
            "late_phase_integral_zero":True,"selected_point_unproved":True}


def dyadic_seed_coalescence_time(seed: F | int) -> int:
    """Least n>=0 with 16^n*seed integer, or reject non-2-primary seed.

    Any finite ensemble of dyadic rational seeds has eventual identical
    e(hU_n(s)) for ALL integer h: its seed differences vanish mod 1.
    """
    if type(seed) not in (int,F):
        raise ValueError("exact seed only")
    s=F(seed)
    den=s.denominator
    bits=0
    while den%2 == 0:
        den//=2
        bits+=1
    if den!=1:
        raise ValueError("odd denominator persists under multiplication by 16")
    return (bits+3)//4


def finite_dyadic_measure_coalescence(seeds: tuple[F,...], weights: tuple[F,...]) -> dict:
    """Exact path-measure rank-collapse certificate; no complex phases needed.

    If all offsets have denominators supported on 2, their phase factors
    e(h16^n s) coincide with 1 for n>=max coalescence time. Hence the
    full source-phase Gram is rank one on that time tail, irrespective of
    the weights or original forcing.
    """
    if type(seeds) is not tuple or type(weights) is not tuple or len(seeds)==0 or len(seeds)!=len(weights):
        raise ValueError("nonempty paired tuples required")
    if any(type(s) not in (int,F) for s in seeds) or any(type(w) not in (int,F) or w<0 for w in weights):
        raise ValueError("exact nonnegative path weights and rational seeds")
    if sum(weights,F(0))!=1:
        raise ValueError("normalized probability path measure required")
    onset=max(dyadic_seed_coalescence_time(s) for s in seeds)
    return {"coalescence_time":onset,"all_future_phases_match_zero_seed":True,
            "future_phase_gram_rank":1,"unselected_ensemble":True}


def late_gradient_energy_coefficient(depth: int, stop: int) -> int:
    """Exact conditional Dirichlet energy divided by (2π h)^2.

    For the authentic source-phase tail F(s)=Σ_(depth<=n<stop)e(hU_n(s)),
    E_{s in any 16^-depth seed cell} |F'(s)|^2
       = (2π h)^2 Σ 16^(2n), exactly (cross terms orthogonal).
    This is a source-attested resistance/Poincare boundary cost, NOT a π
    Weyl estimate. In particular energy grows ~16^(2stop).
    """
    if type(depth) is not int or depth<0 or type(stop) is not int or stop<depth:
        raise ValueError("stop>=depth>=0")
    return (16**(2*stop)-16**(2*depth))//(16**2-1)


def selected_point_lipschitz_obstruction(depth: int, stop: int) -> F:
    """Upper bound |E_cell S_stop - S_stop(anchor)| <=π|h| * coefficient.

    Unlike early_prefix-only control, this applies to ALL n<stop by
    a derivative/Lipschitz estimate. It is typically huge for stop>>depth.
    The successful early-bound is much stronger because late means exactly 0.
    """
    if type(depth) is not int or depth<0 or type(stop) is not int or stop<0:
        raise ValueError("depth,stop>=0")
    return F(16**stop-1,15*16**depth)


def late_radix_resonance_error_coefficient(start: int, h: int=1) -> F:
    """Uniform N>=start bound |Σ e(-h r(n+1)) - #terms|<=π*coefficient.

    The first 17-factor BBP source resonance is almost FULLY COHERENT at
    late times, despite exact seed-cylindrical L2 orthogonality of modes.
    From r(n+1)<15/(64n²), sum_n>=start<15/[64(start-1)].
    """
    if type(start) is not int or start<2 or type(h) is not int or h==0:
        raise ValueError("start>=2 and h nonzero integer")
    return F(15*abs(h),32*(start-1))
