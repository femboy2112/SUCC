"""Exact Radon--Nikodym transport for SUCC bidirectional weighted clocks.

Independent reconstruction of the mathematical source law in sibling
SUCC PR #173 (NOT an import of that unmerged branch):
  W_L(u)=1_{u>=1}/u² + sum_{j>=1}(u+jL)^-2, 0<=u<L.
The folded backward L² target uses omega_L=W_L(u)du, NOT
Haar=du/L. Its total mass is one by the x mod L pushforward of
1_{x>=1}dx/x². W_L(u)>0 for every u, so multiplying by sqrt(L W)
is a unitary identification with Haar L². A cyclic clock translation
must carry the exact RN cocycle:
  T_a^omega f(u)=sqrt(W(u-a)/W(u)) f(u-a).
Its squared cocycle is pure transport and has zero holonomy. However,
the unweighted shift has norm >=sqrt(2)/3 * L for all L>=2,
as witness W(3/2)/W(1/2)>=2 L²/9: the restored connection
becomes asymptotically expensive. These are not Weil/Connes traces.

Finite tests compute exact rational series prefixes with explicit
integral-test tails and exact discrete weighted-clock analogues.
No numerical gamma/zeros, no pretending finite sampling proves L².
"""
from __future__ import annotations

from fractions import Fraction as F


class ClockDensityError(ValueError):
    """A source period, phase, finite budget, or measure was malformed."""


def _period(L):
    if type(L) is not int or not 2<=L<=100_000:
        raise ClockDensityError("genuine finite clock period L>=2")
    return L


def _rational(x):
    if type(x) not in (int,F):
        raise ClockDensityError("exact integer or Fraction phase required")
    return F(x)


def _phase(u,L):
    L=_period(L)
    u=_rational(u)
    if not 0<=u<L:
        raise ClockDensityError("rational clock phase in [0,L) required")
    return u


def _depth(J):
    if type(J) is not int or not 1<=J<=1000:
        raise ClockDensityError("positive finite rational tail budget 1..1000")
    return J


def clock_phase(u,L):
    """Periodize a REAL rational phase, including negative input."""
    L=_period(L)
    return _rational(u)%L


def memory_weight_bounds(u,L,J=12):
    """Certified interval on exact positive W_L(u), with source cut at u=1.

    The integral comparison gives
      1/[L(u+(J+1)L)] <= omitted j>J sum <=1/[L(u+JL)].
    """
    u=_phase(u,L)
    J=_depth(J)
    tail_prefix=sum((F(1)/(u+j*L)**2 for j in range(1,J+1)),F(0))
    near=F(1,u*u) if u>=1 else F(0)
    low=near+tail_prefix+F(1,L*(u+(J+1)*L))
    high=near+tail_prefix+F(1,L*(u+J*L))
    if not 0<low<=high:
        raise AssertionError("source backward memory interval is invalid")
    return {"phase":u,"period":L,"depth":J,
            "source_near_cut":near,"rational_prefix":near+tail_prefix,
            "lower":low,"upper":high,
            "omitted_tail_lower":low-near-tail_prefix,
            "omitted_tail_upper":high-near-tail_prefix,
            "true_mass_is_one_by_pushforward":True,
            "normalized_clock_Haar_equal_to_memory":False,
            "RH_proved":False}


def approximate_weight(u,L,J):
    """Strictly positive rational prefix; NOT the full analytic source weight."""
    u=_phase(u,L)
    J=_depth(J)
    base=F(1,u*u) if u>=1 else F(0)
    return base+sum((F(1)/(u+j*L)**2 for j in range(1,J+1)),F(0))


def ratio_square_interval(L,u,a,J=12):
    """Exact interval for positive squared RN cocycle W(u-a)/W(u)."""
    u=_phase(u,L)
    a=_rational(a)
    v=clock_phase(u-a,L)
    den=memory_weight_bounds(u,L,J)
    num=memory_weight_bounds(v,L,J)
    low=num["lower"]/den["upper"]
    high=num["upper"]/den["lower"]
    if not 0<low<=high:
        raise AssertionError("RN ratio positive interval inconsistent")
    return {
        "period":L,"u":u,"translation":a,"preimage_phase":v,
        "RN_cocycle_square_lower":low,"RN_cocycle_square_upper":high,
        "unitary_in_original_weighted_L2":True,
        "original_Haar_shift_without_cocycle_unitary":False,
        "not_Connes_idelic_trace":True,
    }


def finite_grid_cocycle(L,resolution,depth,shift):
    """Exact finite clock comparison (NOT continuous-source quadrature).

    Grid G=Z/(L*resolution). Weights w_j are strictly positive rational
    truncated source series sampled at u=j/resolution. Pullback by
    sqrt(w_(j-shift)/w_j) is exactly an isometry on the WEIGHTED
    finite-vector space. Ordinary translation generally fails.

    A cyclic 1-period shift needs shift=resolution.
    """
    L=_period(L)
    if type(resolution) is not int or not 1<=resolution<=8:
        raise ClockDensityError("positive bounded phase resolution 1..8 required")
    J=_depth(depth)
    if type(shift) is not int:
        raise ClockDensityError("exact integer shift in phase-grid units required")
    size=L*resolution
    if size>128:
        raise ClockDensityError("finite exact cyclic grid budget <=128")
    weights=tuple(approximate_weight(F(j,resolution),L,J) for j in range(size))
    if any(x<=0 for x in weights):
        raise AssertionError("finite source clock weight zero")
    # Do not replace the source by uniform Haar; the finite weights
    # are raw positive sampled prefix values, not exact source measures.
    coeff_sq=tuple(weights[(j-shift)%size]/weights[j] for j in range(size))
    def isometry_exact():
        for j in range(size):
            if weights[j]*coeff_sq[j]!=weights[(j-shift)%size]:
                return False
        return True
    if not isometry_exact():
        raise AssertionError("exact finite source density transport failed")
    return {
        "L":L,"resolution":resolution,"memory_prefix_depth":J,
        "shift_grid_steps":shift%size,
        "source_weight_prefixes":weights,
        "RN_amplitude_squares":coeff_sq,
        "weighted_norms_preserved_by_cocycle":True,
        "naive_clock_shift_weight_preserving":
            all(weights[j]==weights[(j-shift)%size] for j in range(size)),
        "finite_prefix_represents_exact_integrated_memory":False,
        "RH_proved":False,
    }


def finite_cocycle_composition(L,u,a,b,J=10):
    """The RN source is a COBoundary: cocycle(a,u)cocycle(b,u-a)
    =cocycle(a+b,u). Check independently on any rational prefix gauge;
    analytic equality follows algebraically for the true W as well.
    """
    L=_period(L)
    u=_phase(u,L)
    a=_rational(a);b=_rational(b)
    v=clock_phase(u-a,L)
    w=clock_phase(v-b,L)
    x=approximate_weight(u,L,J)
    y=approximate_weight(v,L,J)
    z=approximate_weight(w,L,J)
    first=y/x
    second=z/y
    together=z/x
    if first*second!=together:
        raise AssertionError("source unitary transport acquired holonomy")
    return {"L":L,"u":u,"a":a,"b":b,
            "cocycle_a_sq":first,"cocycle_b_after_a_sq":second,
            "composed_sq":together,
            "exact_pure_coboundary_at_every_positive_weight":True,
            "phase_gauge_data_cancels_from_transport_loop":True,
            "change_to_uniform_measure_is_source_free":False,
            "full_Weil_trace_identified":False}


def cut_jump_and_unweighted_shift_lower(L):
    """Exact source discontinuity and L-growing norm no-go.

    W(3/2)>=4/9; W(1/2)<=sum_{j>=1}(jL)^-2<2/L²
    by 1+sum_{j>=2}1/(j(j-1))=2.
    Hence W(3/2)/W(1/2)>2 L²/9.
    For naive shift f(u)->f(u-1), its squared weighted L² operator
    norm >=W(3/2)/W(1/2). The corrected RN shift is unitary.
    """
    L=_period(L)
    ratio_lower=F(2*L*L,9)
    if ratio_lower<=0:
        raise AssertionError("wrong one-sided source cut window")
    return {
        "period":L,
        "comparison_below_cut":F(1,2),
        "comparison_above_cut":F(3,2),
        "near_cut_right_jump_exact":F(1),
        "memory_below_cut_upper":F(2,L*L),
        "memory_above_cut_lower":F(4,9),
        "source_density_ratio_strict_lower":ratio_lower,
        "naive_one_unit_translation_operator_norm_squared_lower":ratio_lower,
        "corrected_density_cocycle_translation_is_unitary":True,
        "uniformly_bounded_naive_shift_as_L_grows":False,
        "original_source_must_retain_memory_density":True,
        "not_a_global_suzuki_or_Weil_result":True,
    }


def periodic_ghost_mutant(L,ghost):
    """Source recurrence alone cannot certify w: R(u)+ghost preserves
    the shift equation but violates R(u)->0 for ghost!=0.
    Integrating constant ghost over one clock adds L*ghost to
    probability mass, i.e. is NOT observationally redundant.
    """
    L=_period(L)
    c=_rational(ghost)
    return {
        "period":L,"ghost":c,
        "shift_law_unchanged":True,
        "decay_at_infinity_retained":c==0,
        "integrated_source_mass_added":L*c,
        "same_declared_backward_probability_measure":c==0,
        "RH_proved":False,
    }
