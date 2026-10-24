"""Exact circle-origin covariance, cyclotomic torsion and source-gauge probes.

All executable claims are rational/integer identities. Analytic Haar/L2,
Wasserstein and asymptotic proofs are scoped in CIRCLE_CYCLOTOMIC_ORIGIN_GAUGE.md.
The source selected by pi is not assumed normal. No physical inertial frame,
source measurement, RH or signed Weil consequence is asserted.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from math import gcd


def _i(n, lo=0):
    if type(n) is not int or n < lo:
        raise ValueError(f"integer >= {lo} required")
    return n


def mod1(x):
    return Q(x) % 1


def covering(x, base, steps=1):
    _i(base,2);_i(steps)
    return mod1(base**steps * Q(x))


def rotate(x, origin):
    return mod1(Q(x)+Q(origin))


def frame_covering(x, base, origin, steps=1):
    """R_-a T_b^steps R_a, NOT the unmodified map T_b."""
    _i(base,2);_i(steps)
    return mod1(base**steps*Q(x)+(base**steps-1)*Q(origin))


def origin_defect(base, steps, origin):
    """H_d(a)=(b^d-1)a: failure of naive rotation commutation."""
    _i(base,2);_i(steps)
    return mod1((base**steps-1)*Q(origin))


def moving_frame_forcing(base, origin_now, origin_next):
    _i(base,2)
    return base*Q(origin_now)-Q(origin_next)


def commuting_origins(base):
    """All rotations that actually commute with the FIXED T_b law."""
    _i(base,2)
    return tuple(Q(k,base-1) for k in range(base-1))


def commutes_with_fixed_covering(base, origin):
    _i(base,2)
    return mod1((base-1)*Q(origin)) == 0


def fixed_frame_character_average(base, harmonic):
    """Average of e(h a) over the (b-1) legal commuting rotations."""
    _i(base,2)
    if type(harmonic) is not int or harmonic == 0:
        raise ValueError("nonzero integer Fourier frequency")
    return 1 if harmonic % (base-1) == 0 else 0


def projective_chord_sq(s, t):
    """Intrinsic squared chord in s=tan(pi*x) chart; poles excluded."""
    s,t=Q(s),Q(t)
    return 4*(s-t)**2/((1+s*s)*(1+t*t))


def projective_rotate(s,tau):
    """Möbius circle rotation in the tan chart, away from chart poles."""
    s,tau=Q(s),Q(tau)
    if 1-s*tau == 0:
        raise ValueError("transformed origin reaches the projective pole")
    return (s+tau)/(1-s*tau)


def _divisors(n):
    _i(n,1)
    return tuple(i for i in range(1,n+1) if n % i == 0)


@lru_cache(None)
def cyclotomic_at_base(base, period):
    """Phi_period(base), via exact b^d-1 product-factor recurrence."""
    _i(base,2);_i(period,1)
    denominator=1
    for d in _divisors(period):
        if d<period:
            denominator*=cyclotomic_at_base(base,d)
    numerator=base**period-1
    if numerator % denominator:
        raise ArithmeticError("cyclotomic divisor/source mismatch")
    return numerator//denominator


@lru_cache(None)
def exact_periodic_points(base, period):
    """Points of exact T_b-period d, not Phi_d(b)!"""
    _i(base,2);_i(period,1)
    out=base**period-1-sum(
        exact_periodic_points(base,d)
        for d in _divisors(period) if d<period)
    if out<=0 or out % period:
        raise ArithmeticError("primitive periodic orbit source corrupt")
    return out


def periodic_orbit_count(base,period):
    return exact_periodic_points(base,period)//period


def frame_frequency_residues(base,harmonic,horizon,modulus,
                             *, holonomy=False):
    """Finite origin-grid character labels for time or defect measurements."""
    _i(base,2);_i(horizon,1);_i(modulus,2)
    if type(harmonic) is not int or harmonic==0:
        raise ValueError("h != 0")
    start=1 if holonomy else 0
    return tuple((harmonic*(base**j-(1 if holonomy else 0)))%modulus
                 for j in range(start,start+horizon))


def frame_nonaliased(base,harmonic,horizon,modulus,*,holonomy=False):
    v=frame_frequency_residues(base,harmonic,horizon,modulus,
                               holonomy=holonomy)
    return len(set(v)) == horizon


def frame_origin_energy_at_zero(base,harmonic,horizon,modulus,
                                *,holonomy=False):
    """Exact full grid mean of |mean_j e(frequency_j * r/m)|².

    Root-of-unity orthogonality: sum_class count(class)^2 / N^2.
    This is a SPATIAL ENSEMBLE measurement, not a pointwise orbit bound.
    """
    v=frame_frequency_residues(base,harmonic,horizon,modulus,
                               holonomy=holonomy)
    freq={}
    for x in v:
        freq[x]=freq.get(x,0)+1
    return Q(sum(c*c for c in freq.values()),horizon*horizon)


def order_mod(base,modulus):
    """Multiplicative order; only when b is a unit modulo modulus."""
    _i(base,2);_i(modulus,2)
    if gcd(base,modulus)!=1:
        raise ValueError("base must be a unit modulo the finite origin clock")
    x=1
    for j in range(1,modulus+1):
        x=x*base%modulus
        if x==1:
            return j
    raise ArithmeticError("finite multiplicative order not reached")


def order_suffices_for_frame(base,harmonic,horizon,modulus):
    _i(base,2);_i(modulus,2);_i(horizon,1)
    if type(harmonic) is not int or harmonic==0:
        raise ValueError("nonzero harmonic required")
    return (gcd(base*harmonic,modulus)==1
            and order_mod(base,modulus)>=horizon)


def cyclotomic_source_orbit(base,period):
    """Selected x_d=1/(b^d-1), one genuine full period d (d>=2)."""
    _i(base,2);_i(period,2)
    modulus=base**period-1
    return tuple(Q(base**j,modulus) for j in range(period))


def cyclotomic_selected_linear_mean(base,period):
    """Exact source orbit average of points in [0,1); also W1 to delta0 if b>=3."""
    _i(base,2);_i(period,2)
    v=cyclotomic_source_orbit(base,period)
    answer=sum(v,Q())/period
    if answer!=Q(1,period*(base-1)):
        raise ArithmeticError("geometric selected orbit sum mismatch")
    return answer


def periodic_origin_grid_w1(base,period):
    """Exact Haar W1 to the whole (b^d-1)-torsion grid on circle geodesic."""
    _i(base,2);_i(period,2)
    return Q(1,4*(base**period-1))


def selected_orbit_w1_zero(base,period):
    """EXACT W1(selected orbit, delta0) for b>=3."""
    _i(base,3);_i(period,2)
    return cyclotomic_selected_linear_mean(base,period)


def selected_orbit_weyl_deviation_bound(base,period,harmonic=1):
    """|A_h,d(1/(b^d-1))-1| <= 2*pi*|h|/[d(b-1)].

    Return rational coefficient of 2*pi; this is a bound, not its value.
    """
    _i(base,2);_i(period,2)
    if type(harmonic) is not int or harmonic==0:
        raise ValueError("nonzero Fourier frequency required")
    return Q(abs(harmonic),period*(base-1))


def certified_cyclotomic_pi_shadow(pi_lo,pi_hi,base,period):
    """Select periodic rational orbit from independent π interval.

    Requires both interval endpoints (3,4) and one uniquely rounded
    numerator. Output: (numerator,denominator,certified circle error).
    An arbitrarily close PERIODIC fake does not certify π normality.
    """
    _i(base,2);_i(period,2)
    lo,hi=Q(pi_lo),Q(pi_hi)
    if not (Q(3)<lo<=hi<Q(4)):
        raise ValueError("independent source interval strictly inside (3,4)")
    m=base**period-1
    low,high=lo-3,hi-3
    def nearest(x):
        return (m*x+Q(1,2)).numerator//(m*x+Q(1,2)).denominator
    k_lo,k_hi=nearest(low),nearest(high)
    if k_lo!=k_hi or not(0<k_lo<m):
        raise ValueError("π interval insufficient to certify unique source grid point")
    k=k_lo
    error=max(abs(Q(k,m)-low),abs(Q(k,m)-high))
    if error>Q(1,2*m)+(hi-lo):
        raise ArithmeticError("periodic source selection error invalid")
    return k,m,error


def truncated_bbp_connection(n,depth):
    """Exact finite-BBP gauge cocycle residual in Q, no pi digits."""
    _i(n);_i(depth,1)
    from observational_succ.bbp_source_memory import forcing
    def partial(k):
        return sum((forcing(k+j)/16**j for j in range(1,depth+1)),Q())
    t0,t1=partial(n),partial(n+1)
    observed=16*t0-t1-forcing(n+1)
    expected=-forcing(n+depth+1)/16**depth
    if observed!=expected:
        raise ArithmeticError("source gauge / BBP origin residual mismatch")
    return observed


def exact_relative_rms_thirds(horizon):
    """For base16 and relative displacement 1/3 (h=1):
    integral_|a| |A_N(a)-A_N(a+1/3)|² da = 3/N.
    """
    _i(horizon,1)
    return Q(3,horizon)


def bbp_lag_boundary_interval(lag, window, terms=8):
    """Certified finite source boundary for sum_(j=1)^window (t_j-t_(j+lag)).

    Exact telescoping leaves only q=min(lag,window) early terms and
    q late terms starting at max(lag,window)+1. Uses genuine BBP tails.
    Output is (nonnegative rational lower, rational upper) and is
    independent of pointwise character approximations.
    """
    _i(lag,1);_i(window,1);_i(terms,1)
    from observational_succ.bbp_source_memory import tail_interval
    q=min(lag,window)
    last=max(lag,window)
    early=[tail_interval(j,terms) for j in range(1,q+1)]
    late=[tail_interval(j,terms) for j in range(last+1,last+q+1)]
    lower=max(Q(),sum((a for a,b in early),Q())-
                      sum((b for a,b in late),Q()))
    upper=sum((b for a,b in early),Q())-sum((a for a,b in late),Q())
    if upper<=0 or lower>upper:
        raise ArithmeticError("positive monotone source boundary failed")
    return lower,upper


def bbp_lag_signed_error_upper(lag,window,harmonic=1,terms=8):
    """Rational upper for |C_d(pi)-C_d(authentic forced BBP)|.

    Every phase difference is bounded by 2*pi*|h|*(t_j-t_(j+d)).
    Uses pi < 22/7. No signed-sum cancellation or normality is claimed.
    """
    if type(harmonic) is not int or harmonic==0:
        raise ValueError("nonzero Fourier harmonic required")
    _,upper=bbp_lag_boundary_interval(lag,window,terms)
    return Q(44,7)*abs(harmonic)*upper


def haar_frame_fourth_moment(horizon):
    """Exact Haar-origin E|A_h,N(x+a)|^4=(2N²-N)/N^4, b>=2,h!=0."""
    _i(horizon,1)
    return Q(2*horizon*horizon-horizon,horizon**4)


def frame_fourth_no_alias(base,harmonic,horizon,modulus):
    """Distinct UNORDERED pair sums of hb^j modulo the origin clock."""
    values=frame_frequency_residues(base,harmonic,horizon,modulus)
    sums=[(values[j]+values[k])%modulus
          for j in range(horizon) for k in range(j,horizon)]
    return len(set(sums))==len(sums)


def frame_fourth_energy_at_zero(base,harmonic,horizon,modulus):
    """Exact spatial-grid fourth moment at a selected source x=0.

    Frequency pair-sum convolution; roots-of-unity orthogonality.
    For any selected x, the same value follows if frame_fourth_no_alias
    is true; aliasing otherwise may preserve phases and cannot be erased.
    """
    v=frame_frequency_residues(base,harmonic,horizon,modulus)
    classes={}
    for j in range(horizon):
        for k in range(horizon):
            residue=(v[j]+v[k])%modulus
            classes[residue]=classes.get(residue,0)+1
    return Q(sum(c*c for c in classes.values()),horizon**4)


def frame_fourth_bad_origin_measure_upper(horizon,epsilon):
    """Exact fourth-moment/Markov bound <= (2N²-N)/(N^4 epsilon^4)."""
    _i(horizon,1)
    e=Q(epsilon)
    if e<=0:
        raise ValueError("positive deviation threshold required")
    return haar_frame_fourth_moment(horizon)/e**4


def inverse_source_tree(base,depth,source):
    """Complete b^k preimage ensemble of x under T_b^k, not one trajectory."""
    _i(base,2);_i(depth)
    m=base**depth
    x=mod1(source)
    return tuple(mod1((x+r)/m) for r in range(m))


def inverse_tree_w1_haar(base,depth):
    """Exact W1 of uniform preimage coset and Haar in geodesic metric."""
    _i(base,2);_i(depth)
    return Q(1,4*base**depth)


def inverse_tree_fourier_survives(base,depth,harmonic):
    """Character e(hx) mean is 0 unless b^depth divides h."""
    _i(base,2);_i(depth)
    if type(harmonic) is not int:
        raise ValueError("integer character required")
    return harmonic%(base**depth)==0


def inverse_tree_pushforward_multiplicity(base,depth,source):
    """Exact counted multiset after one forward SUCC from full inverse FUCC tree.

    Each of b^(depth-1) preimages occurs exactly b times. Does not
    authenticate any particular selected branch or pi normality.
    """
    _i(base,2);_i(depth,1)
    from collections import Counter
    points=inverse_source_tree(base,depth,source)
    actual=Counter(covering(v,base,1) for v in points)
    expected=Counter({v:base for v in inverse_source_tree(base,depth-1,source)})
    if actual!=expected:
        raise ArithmeticError("inverse/forward source tree projectivity broken")
    return tuple(sorted(actual.items()))
