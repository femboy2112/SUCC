"""Backward-from-infinity SUCC memory kernel for the LCM clock.

The genuine full Hilbert upper-cut error folds onto one finite clock using
W_L(u) = 1_[u>=1]/u^2 + sum_{j>=1} 1/(u+jL)^2, 0<=u<L.

The infinite memory tail solves R(u)-R(u+L)=1/(u+L)^2 and is uniquely
specified by decay as u->infinity. A merely periodic backward solution may
add a ghost constant. Exact finite rational intervals certify omitted tail.
"""
from fractions import Fraction as F
from .bidirectional_cut import CutSourceError, rat, small_n


def memory_bounds(phase, period, depth=8):
    """Rigorous OUTWARD rational interval for backward clock memory.

    R_L(u)=sum_{j>=1} (u+jL)^(-2) on u>=0.
    For decreasing j sequence, integral comparison bounds omitted j>depth:
      1/[L(u+(depth+1)L)] <= tail <= 1/[L(u+depth L)].
    """
    u=rat(phase)
    small_n(period,maximum=100000)
    if u < 0:
        raise CutSourceError("nonnegative clock phase required")
    if type(depth) is not int or not 1<=depth<=2000:
        raise CutSourceError("positive bounded memory depth required")
    L=F(period)
    prefix=sum((F(1)/(u+j*L)**2 for j in range(1,depth+1)),F(0))
    low=prefix+F(1)/(L*(u+(depth+1)*L))
    high=prefix+F(1)/(L*(u+depth*L))
    if not 0 < low <= high:
        raise AssertionError("bad remainder interval")
    return {"phase":u,"period":period,"depth":depth,
            "lower":low,"upper":high,
            "forgotten_tail_enclosed":True,"global_functional_bounded":False,
            "RH_proved":False}


def upper_cut_weight_bounds(phase, period, depth=8):
    """Weight after folding x>=1 to clock phase u in [0,L)."""
    u=rat(phase)
    small_n(period,maximum=100000)
    if not F(0)<=u<period:
        raise CutSourceError("phase must lie in one fundamental LCM period")
    b=memory_bounds(u,period,depth)
    extra=F(1)/u**2 if u>=1 else F(0)
    return {"lower":extra+b["lower"],"upper":extra+b["upper"],
            "near_cut_term":extra,"periodic_memory":b,
            "RH_proved":False}


def backward_ladder_mutation(phase, period, depth=8, ghost=0):
    """Finite diagnostic of shift equation + invisible L-periodic ghost.

    Both genuine R_L and R_L+ghost solve the same difference equation;
    only genuine solution tends to zero. For nonzero ghost the persistent
    boundary condition is falsified. This is an analytical, not numerical,
    source-status gate.
    """
    u=rat(phase)
    small_n(period,maximum=100000)
    g=rat(ghost)
    b=memory_bounds(u,period,depth)
    shifted=memory_bounds(u+period,period,depth)
    exact_shift=F(1)/(u+period)**2
    # Difference of interval enclosures should cover the exact shift;
    # the *underlying series* has exact termwise telescope.
    difference_lo=b['lower']-shifted['upper']
    difference_hi=b['upper']-shifted['lower']
    if not difference_lo<=exact_shift<=difference_hi:
        raise AssertionError("memory recurrence not enclosed")
    return {'shift_law_exact':str(exact_shift),
            'memory_difference_enclosure':(difference_lo,difference_hi),
            'constant_ghost':g,'shift_law_cannot_discriminate_ghost':True,
            'boundary_decay_certified':g==0,
            'RH_proved':False}


def folded_memory_energy_bounds(coeffs, period, *, J=12, subdivisions=1,
                                 max_clock_states=1200):
    """Exact outward interval for integral_0^L A_c(u)^2 W_L(u)du.

    A_c=1-sum c_n {u/n}. Each unit cell k..k+1 has rational quadratic
    integral; W_L(u) is strictly decreasing on each branch 0..1 and 1..L.
    Subdivision controls the one-step endpoint enclosure width; W_L's
    memory tail uses the rigorous rational integral-test bound above.

    This is a FINITE source clock reconstruction of the full x>1 weighted
    energy. It never claims that a globally optimized coefficient sequence
    has been constructed, nor that Nyman/Weil positivity is proved.
    """
    from .bidirectional_cut import signed_coefficients
    c=signed_coefficients(coeffs)
    small_n(period,maximum=100000)
    if type(subdivisions) is not int or not 1<=subdivisions<=40:
        raise CutSourceError("1..40 exact subcells per clock state")
    if period>max_clock_states:
        raise CutSourceError("materialized phase clock exceeds declared budget")
    if any(period % n for n in range(1,len(c)+1)):
        raise CutSourceError("period must be an observed common multiple of all clock species")
    b=sum((v/n for n,v in enumerate(c,1)),F(0))
    low=high=F(0)
    for k in range(period):
        a=F(1)+sum((v*(k//n) for n,v in enumerate(c,1)),F(0))
        for s in range(subdivisions):
            left=F(k)+F(s,subdivisions)
            right=F(k)+F(s+1,subdivisions)
            midpoint=(left+right)/2
            halfwidth=(right-left)/2
            # A(x)=a-b*x on every original integer cell.
            quadratic=(right-left)*((a-b*midpoint)**2 + b*b*halfwidth**2/3)
            # The 1/u^2 branch is present on the entire integer cell
            # precisely when k>=1. At boundaries u=1 and u=L use the
            # relevant ONE-SIDED value, not a pointwise new branch.
            active = (k >= 1)
            lower_w=memory_bounds(right,period,J)['lower']
            upper_w=memory_bounds(left,period,J)['upper']
            if active:
                lower_w+=F(1)/right**2
                upper_w+=F(1)/left**2
            low+=lower_w*quadratic
            high+=upper_w*quadratic
    if not F(0)<=low<=high:
        raise AssertionError("invalid folded integration bounds")
    return {"lower":low,"upper":high,"period":period,
            "memory_depth":J,"subdivisions":subdivisions,
            "cut_zero_interval_energy":b*b,
            "full_squared_error_lower":low+b*b,
            "full_squared_error_upper":high+b*b,
            "RH_proved":False}


def haar_memory_transport_obstruction(period, window):
    """Source-invariant lower bound separating uniform and inverse-square clocks.

    Uniform Haar on [0,L): H(B)=|B|/L. Backward memory probability:
      omega(B)=integral_B W_L(u)du,
    where omega is the pushforward of x^-2 dx on x>=1 by x mod L.
    For B=[1,R), 1<R<=L:
      omega(B)>=integral_1^R dx/x²=1-1/R,
      H(B)=(R-1)/L.
    Thus TV(omega,H)>=max(0,1-1/R-(R-1)/L).
    On a positive-measure set approaching 1 from the right W_L(u)>=u^-2,
    so the identity L²(H)->L²(omega) has squared norm >=L (L>1).
    No infinite-closure norm bound independent of clock period follows.
    """
    small_n(period,maximum=100000)
    R=rat(window)
    if period<2 or not 1<R<=period:
        raise CutSourceError("nontrivial bounded window 1<R<=L required")
    haar=F(R-1,period)
    mem=F(1)-1/R
    delta=max(F(0),mem-haar)
    return {"period":period,"window":R,
            "haar_window_probability":haar,
            "memory_window_probability_lower":mem,
            "total_variation_distance_lower":delta,
            "L2_norm_transport_squared_lower":F(period),
            "growing_clock_not_uniformly_norm_equivalent":True,
            "RH_proved":False}
