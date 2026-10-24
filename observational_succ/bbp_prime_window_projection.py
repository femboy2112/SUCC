"""Prime-birth SUCC spectral projection and source-controlled clock discrepancy.

Operation PRIME-CLOCK SPECTRAL CRUCIBLE. All proof-relevant finite computations
use exact Fraction/integer operations; no pi digits, floats, or independent
phase assumptions. Paper proof and external BGK hypotheses are explicit in
research/2026-10-24/BBP_PRIME_CLOCK_SPECTRAL_PROJECTION.md.

The external Bourgain--Glibichuk--Konyagin constant/exponent is not
constructed or certified by finite tests. The implemented facts establish
the exact finite algebra to which that theorem applies. PI NORMALITY OPEN.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd

from .bbp_cyclotomic_birth import (
    birth_index, first_phase_residue, full_cycle_count,
    multiplicative_order_16, source_window_split,
)
from .bbp_source_memory import forcing, source_tail_beta_bracket


def _natural(x: int, minimum: int = 0) -> int:
    if type(x) is not int or x < minimum:
        raise ValueError("integer >= %d required" % minimum)
    return x


def _integer(x: int) -> int:
    if type(x) is not int:
        raise ValueError("integer required")
    return x


def window_parameters(p: int) -> tuple[int,int,int,int]:
    """(m,L,Delta,B) for authentic p=8m+1 prime first-birth interval."""
    birth_index(p)  # authenticate rational prime before arithmetic use
    if p % 8 != 1:
        raise ValueError("full first-birth window requires p == 1 mod 8")
    m = (p-1)//8
    L = multiplicative_order_16(p)
    delta = 3*m
    if m % L or delta % L:
        raise AssertionError("quadratic-residue period source law failed")
    return m,L,delta,delta//L


def additive_clock_partition(p: int, d: int, h: int=1) -> dict:
    """Certified complete subgroup periods in every time class t mod d.

    If d|Delta, the class length Delta/d is a multiple of L'=ord_p(16^d)
    = L/gcd(L,d), even when d does not divide L. Each class visits a
    multiplicative coset, with exactly Delta/(d*L') full repetitions.
    """
    _natural(d,1); _integer(h)
    m,L,delta,B = window_parameters(p)
    if delta%d:
        raise ValueError("period d must divide the complete source window")
    g = gcd(d,L)
    suborder = L//g
    repetition = delta//(d*suborder)
    if repetition < 1 or pow(16,d*suborder,p)!=1:
        raise AssertionError("invalid prime-clock subgroup")
    if any(pow(16,d*j,p)==1 for j in range(1,suborder)):
        raise AssertionError("subgroup order was not minimal")
    return {"p":p,"m":m,"d":d,"h":h,"L":L,"delta":delta,"blocks":B,
            "gcd":g,"suborder":suborder,"repetitions":repetition,
            "class_length":delta//d,
            "subgroup_coefficients":tuple(
                tuple((4*h*pow(16,r+d*j,p))%p for j in range(suborder))
                for r in range(d))}


def source_complement_window(p: int) -> tuple[Q,...]:
    """Unique source-authenticated p-unit Q/Z complement in first window."""
    return tuple(q for _,q in source_window_split(p))


def circular_distance(q: Q) -> Q:
    x=Q(q)%1
    return min(x,1-x)


def rational_phase_dispersion_bracket(p: int, d: int, h: int=1) -> tuple[Q,Q]:
    """Certified lower/upper for normalized periodic-subspace L2 defect².

    Set v_t=e(h*w_t), Q_d v = time-residue-class mean (d|Delta).
    D²=(1/Delta)sum_t|v_t-(Q_d v)_t|² = 1-||Q_d v||².
    With K=Delta/d, D²=(1/(d*K²))sum_r sum_(i<j in class r)|v_i-v_j|².
    For circle distance a, 4a<=|e(x)-e(y)|<= (44/7)a.
    Thus all finite witnesses are bounded by exact rational pair sums.
    This is NOT an exact evaluation of D² or a normality certificate.
    """
    _integer(h)
    data=additive_clock_partition(p,d,h)
    delta=data["delta"]; K=delta//d
    if h==0 or K<=1:
        return Q(),Q()
    w=source_complement_window(p)
    sq=Q()
    for r in range(d):
        points=[w[r+d*j] for j in range(K)]
        for i in range(K):
            for j in range(i+1,K):
                sq+=circular_distance(h*(points[i]-points[j]))**2
    factor=Q(1,d*K*K)
    lower=16*factor*sq
    upper=min(Q(1),Q(1936,49)*factor*sq)
    if lower>upper:
        raise AssertionError("incorrect phase-pair inequality")
    return lower,upper


def exact_source_period_defects(p: int, d: int, h: int=1) -> tuple[Q,...]:
    """Phase defects ||h*(w_(t+d)-w_t)|| on actual BBP prime-free source.

    Compute by the SOURCE recurrence rather than a postulated periodic
    approximation; cross-check the independent state-difference route.
    This is a rational, actual-source nonautonomous field measurement.
    """
    _integer(h)
    data=additive_clock_partition(p,d,h)
    w=source_complement_window(p)
    n0=data["m"]+1
    residuals=[]
    for t in range(data["delta"]-d):
        input_sum=sum((16**(d-j)*forcing(n0+t+j)
                       for j in range(1,d+1)),Q())
        source_diff=(16**d-1)*w[t]+input_sum
        actual_diff=w[t+d]-w[t]
        if (source_diff-actual_diff)%1:
            raise AssertionError("complement dynamics did not commute")
        residuals.append(circular_distance(h*source_diff))
    return tuple(residuals)


def source_defect_variance_upper(p: int, d: int, h: int=1) -> Q:
    """Sound rational (possibly vacuous) path-Poincare D² upper.

    K=Delta/d. Crude |v_i - mean(class)|² <=
    (K-1)*sum_of_edges |v_next-v|²; average over all Delta points.
    Use |e(a)-e(b)| <=44/7 * ||a-b||.
    """
    data=additive_clock_partition(p,d,h)
    K=data["class_length"]
    if K<=1 or h==0:
        return Q()
    defects=exact_source_period_defects(p,d,h)
    total_sq=sum((x*x for x in defects),Q())
    result=Q(1936,49)*Q(K*K,data["delta"])*total_sq
    return min(Q(1),result)


def window_pi_source_shadow_budget(p: int, h: int=1) -> Q:
    """Finite rational |W_p(h;y)-W_p(h;pi)| strict upper.

    From x_(n-1)={y_n+T_n}, T_n<B_n and 2*pi<44/7.
    Sum is over actual n=m+1,...,4m and has uniform bound
       < 11*|h|/(112*m).
    Dividing by 3*m gives O_h(m^-2), source-specific, all windows.
    """
    _integer(h)
    m,L,delta,B=window_parameters(p)
    return Q(44*abs(h),7)*sum(
        (source_tail_beta_bracket(n)[1] for n in range(m+1,4*m+1)),Q())


def shadow_uniform_budget(p: int, h: int=1) -> Q:
    """Simple all-p rational majorant on source-to-true-pi window error."""
    _integer(h)
    m,*_=window_parameters(p)
    return Q(11*abs(h),112*m)


def first_resonant_clock_period(p: int, h: int=1) -> int:
    """Exact period L for counterfeit v_t=e(-4h*16^t/p) when p does not divide h.

    Then the full mixed window u_t v_t=1 and W=Delta. This is a
    non-BBP comparator, showing the low-period restriction matters.
    """
    _integer(h)
    m,L,delta,B=window_parameters(p)
    if h%p==0:
        raise ValueError("nontrivial local Fourier frequency required")
    residues=[(4*h*pow(16,t,p))%p for t in range(L)]
    if len(set(residues))!=L:
        raise AssertionError("local character unexpectedly not injective")
    return L


def periodic_profile_orthogonality(p: int, d: int, h: int=1) -> dict:
    """Exact integer profile for local forcing e(4h*16^t/p) by d residues.

    A d-periodic complement is a fixed vector (v_0,...,v_(d-1));
    local phase sum equals weighted subgroup complete coset Gauss sums.
    The analytic bound on the coset sums is imported (BGK/Weil),
    NOT evaluated or silently inferred from this finite identity.
    """
    data=additive_clock_partition(p,d,h)
    residues=data["subgroup_coefficients"]
    # Direct full window counts independently from the coset subgroup:
    counts=[]
    for r in range(d):
        raw=tuple((4*h*pow(16,t,p))%p
                  for t in range(r,data["delta"],d))
        expanded=residues[r]*data["repetitions"]
        if raw!=expanded:
            raise AssertionError("direct time walk disagreed with coset blocks")
        counts.append(len(raw))
    return {"p":p,"period":d,"class_lengths":tuple(counts),
            "subgroup_size":data["suborder"],
            "cycles_per_class":data["repetitions"],
            "exact_cover":True}


def source_periodicity_obstruction(p: int, d: int, h: int=1) -> dict:
    """Finite exact SUCC forcing defect forbids perfect low-period complement.

    For 1<=d<=Delta-2 compare forcing at n0+1 and n0+d+1;
    their signed difference r(n0+1)-r(n0+d+1) is positive and <1
    (n0=m+1>=3). Since w_(t+1)=16w_t+r(n0+t+1) mod1,
        ||h*(r(n0+1)-r(n0+d+1))||
              <= 16||h*(w_d-w_0)|| + ||h*(w_(d+1)-w_1)||.
    Thus at least one phase-period defect >= gap/17, a rational
    finite boundary witness. For h=1 the gap is just its real value;
    for arbitrary h it may be an integer (then the bound is zero).
    """
    _integer(h)
    data=additive_clock_partition(p,d,h)
    delta=data["delta"]
    if d>delta-2:
        raise ValueError("need both initial and successor matched checkpoints")
    n0=data["m"]+1
    r0=forcing(n0+1)
    rd=forcing(n0+d+1)
    gap=r0-rd
    if not (Q() < gap < Q(1)):
        raise AssertionError("strict rational BBP forcing monotonicity failed")
    w=source_complement_window(p)
    first=circular_distance(h*(w[d]-w[0]))
    second=circular_distance(h*(w[d+1]-w[1]))
    effective_gap=circular_distance(h*gap)
    if effective_gap>16*first+second:
        raise AssertionError("source defect violates circle triangle inequality")
    return {"p":p,"d":d,"h":h,
            "forcing_difference":gap,
            "phase_gap":effective_gap,
            "first_defect":first,"successor_defect":second,
            "minimum_maximum_defect":effective_gap/17}
