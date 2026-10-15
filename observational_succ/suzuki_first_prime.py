"""Suzuki (arXiv:2606.09096v3) first arithmetic wavefront; exact rational proofs.

Two different operator topologies are deliberately tracked. The genuine n=2
screw-kernel component becomes Hilbert--Schmidt small at its first onset,
while its twice-differentiated quadratic form has a fixed norm. All arithmetic
bounds use Fraction; no nontrivial zeta zeros are read or assumed.

The global Weil/RH-positive operator is NOT constructed here. Read the
accompanying SUZUKI_FIRST_PRIME_WAVEFRONT.md for mathematical proofs and scope.
"""
from __future__ import annotations

from bisect import bisect_right
from fractions import Fraction as Q
from math import factorial, isqrt


class SuzukiWavefrontError(ValueError):
    pass


def strict_integer(n: int, minimum: int, maximum: int) -> int:
    if type(n) is not int or not minimum <= n <= maximum:
        raise SuzukiWavefrontError("integer outside declared exact source domain")
    return n


def prime_power(n: int) -> tuple[int, int] | None:
    """Authenticate p^k; a composite like 6 is not one prime jet."""
    strict_integer(n, 2, 100_000)
    v = n
    for p in range(2, isqrt(v) + 2):
        if v % p == 0:
            e = 0
            while v % p == 0:
                v //= p
                e += 1
            return (p, e) if v == 1 else None
    return n, 1


def atanh_log_interval(n: int, terms: int = 12) -> tuple[Q, Q]:
    """Certified log(n) interval via log(n)=2 atanh((n-1)/(n+1)).

    Positive tail <= 2*z^(2N+3)/((2N+3)*(1-z^2)); N inclusive.
    """
    strict_integer(n, 2, 1000)
    strict_integer(terms, 1, 80)
    z = Q(n - 1, n + 1)
    lo = 2 * sum((z ** (2 * j + 1) / (2 * j + 1)
                  for j in range(terms + 1)), Q())
    tail = 2 * z ** (2 * terms + 3) / ((2 * terms + 3) * (1 - z*z))
    return lo, lo + tail


def sqrt_interval(n: int, decimal_places: int = 18) -> tuple[Q, Q]:
    strict_integer(n, 2, 100)
    strict_integer(decimal_places, 1, 35)
    scale = 10 ** decimal_places
    lower = isqrt(n * scale * scale)
    return Q(lower, scale), Q(lower + 1, scale)


def genuine_prime_weight_interval(n: int, terms: int = 14) -> tuple[Q, Q]:
    """The authentic (log p)/sqrt(p^k), not log(p^k)/sqrt(p^k)."""
    pk = prime_power(n)
    if pk is None:
        raise SuzukiWavefrontError("von Mangoldt coefficient vanishes: not a prime power")
    p, _ = pk
    lp, up = atanh_log_interval(p, terms)
    sqlo, sqhi = sqrt_interval(n)
    return lp / sqhi, up / sqlo


def first_prime_wavefront(a: Q, terms: int = 14) -> dict:
    """Exact rational enclosures of the first genuine Suzuki n=2 onset.

    Requires log(2) < 2a < log(3), a < log(2); logarithms rigorously
    bracketed, not fed in as floating point constants.
    """
    if type(a) not in (int, Q) or a <= 0:
        raise SuzukiWavefrontError("a must be an exact positive rational")
    a = Q(a)
    c_lo, c_hi = atanh_log_interval(2, terms)
    l3_lo, _ = atanh_log_interval(3, terms)
    if not (c_hi < 2 * a < l3_lo and a < c_lo):
        raise SuzukiWavefrontError("interval is not certified first-prime only")
    b_lo, b_hi = genuine_prime_weight_interval(2, terms)
    w_lo, w_hi = 2 * a - c_hi, 2 * a - c_lo
    s6_lo, s6_hi = sqrt_interval(6)
    return {
        "interval_a": str(a), "first_prime": 2,
        "prime_power_source": "Lambda(2)=log 2; no other active prime powers",
        "log2_lower": str(c_lo), "log2_upper": str(c_hi),
        "half_density_b_lower": str(b_lo), "half_density_b_upper": str(b_hi),
        "boundary_width_lower": str(w_lo), "boundary_width_upper": str(w_hi),
        "kernel_HS_lower": str(b_lo * w_lo*w_lo / s6_hi),
        "kernel_HS_upper": str(b_hi * w_hi*w_hi / s6_lo),
        "differentiated_operator_norm_lower": str(b_lo),
        "differentiated_operator_norm_upper": str(b_hi),
        "first_onset": True,
        "only_zero_independent_source": True, "RH_proved": False,
    }


def hs_squared(a: Q, c: Q, b: Q) -> Q:
    """Exactly b² (2a-c)^4 / 6, when c/2<a<c. Synthetic rational source."""
    if any(type(v) not in (int, Q) for v in (a, c, b)):
        raise SuzukiWavefrontError("exact rational geometry only")
    a, c, b = Q(a), Q(c), Q(b)
    if not (0 < c / 2 < a < c and b > 0):
        raise SuzukiWavefrontError("cross-corner range c/2 < a < c needed")
    return b*b * (2*a - c)**4 / 6


def _knots(points: tuple[tuple[Q, Q], ...]) -> tuple[tuple[Q, Q], ...]:
    if (type(points) is not tuple or len(points) < 2 or
            any(type(x) not in (int, Q) or type(v) not in (int, Q)
                for x, v in points)):
        raise SuzukiWavefrontError("piecewise affine function must have exact knots")
    t = tuple((Q(x), Q(v)) for x, v in points)
    if not all(t[i][0] < t[i + 1][0] for i in range(len(t)-1)):
        raise SuzukiWavefrontError("strictly ordered knots required")
    if t[0][1] or t[-1][1]:
        raise SuzukiWavefrontError("boundary values must vanish")
    return t


def evaluate(points: tuple[tuple[Q, Q], ...], x: Q) -> Q:
    t = _knots(points)
    x = Q(x)
    if x < t[0][0] or x > t[-1][0]:
        return Q()
    if x == t[-1][0]:
        return t[-1][1]
    j = bisect_right([node[0] for node in t], x)-1
    l, vl = t[j]
    r, vr = t[j+1]
    return vl + (vr-vl)*(x-l)/(r-l)


def l2_piecewise(points: tuple[tuple[Q,Q], ...]) -> Q:
    t = _knots(points)
    return sum(((r-l)*(vl*vl + vl*vr + vr*vr)/3
                for (l,vl),(r,vr) in zip(t,t[1:])), Q())



def derivative_norm2_piecewise(points: tuple[tuple[Q,Q],...]) -> Q:
    """Exact H_0^1 weak-derivative squared norm, for piecewise affine probes."""
    t=_knots(points)
    return sum(((vr-vl)**2/(r-l) for (l,vl),(r,vr) in zip(t,t[1:])),Q())


def low_regularization_certificate(points: tuple[tuple[Q,Q],...],
                                   a: Q,c: Q,b: Q) -> dict:
    """Exact test of |<R v',v'>| <= ||R||_HS ||v'||² (square comparison).

    This finite probe bound is NOT a global L²-relative estimate, since
    normalized translated corner modes can require ||v'||/||v|| ~ 1/w.
    """
    t=_knots(points)
    if type(a) not in (int,Q) or t[0][0]!=-Q(a) or t[-1][0]!=Q(a):
        raise SuzukiWavefrontError("original source interval not matched")
    slope2=derivative_norm2_piecewise(t)
    real_form=prime_differential_form(t,c,b)
    hs2=hs_squared(a,c,b)
    if real_form*real_form>hs2*slope2*slope2:
        raise ArithmeticError("source spectral inequality failed")
    return {"derivative_norm_squared":str(slope2),
            "prime_source_quadratic":str(real_form),
            "kernel_HS_squared":str(hs2),
            "proved_cauchy_schwarz_for_test":True,
            "uniform_L2_relative_bound_derived":False,
            "RH_proved":False}

def _product_linear_integral(l: Q,r: Q,fl: Q,fr: Q,gl: Q,gr: Q) -> Q:
    return (r-l)*(2*fl*gl + fl*gr + fr*gl + 2*fr*gr)/6


def translated_overlap(points: tuple[tuple[Q,Q], ...], c: Q) -> Q:
    """Exact integral of v(x)v(x+c) dx for rational piecewise linear v."""
    t = _knots(points)
    if type(c) not in (int,Q) or c <= 0:
        raise SuzukiWavefrontError("positive rational shift required")
    c = Q(c)
    lo,hi=t[0][0],t[-1][0]-c
    if hi <= lo:
        return Q()
    cuts = sorted(set([lo,hi] + [x for x,_ in t if lo < x < hi] +
                      [x-c for x,_ in t if lo < x-c < hi]))
    integral = Q()
    for left,right in zip(cuts,cuts[1:]):
        integral += _product_linear_integral(
            left,right,evaluate(t,left),evaluate(t,right),
            evaluate(t,left+c),evaluate(t,right+c))
    return integral


def prime_differential_form(points: tuple[tuple[Q,Q], ...], c: Q, b: Q) -> Q:
    """Integration by parts twice gives -2*b*int v(x)v(x+c) dx."""
    if type(b) not in (int,Q) or b <= 0:
        raise SuzukiWavefrontError("positive rational source weight required")
    return -2 * Q(b) * translated_overlap(points, c)



def _ramp_rect(l: Q, r: Q, s: Q, t: Q, c: Q) -> Q:
    """Exact double integral of (x-y-c)_+ over a rational rectangle."""
    z = lambda x: max(Q(0), x) ** 3
    return (z(r-s-c) - z(l-s-c) - z(r-t-c) + z(l-t-c)) / 6


def prime_kernel_form_piecewise(points: tuple[tuple[Q,Q],...],
                                c: Q, b: Q) -> Q:
    """Independent exact double-integral oracle for b(|x-y|-c)_+ v'(x)v'(y).

    Deliberately does NOT call translated_overlap or the integration-by-parts
    representation. Uses 2D piecewise-polynomial antiderivatives on rectangles.
    """
    t = _knots(points)
    if type(c) not in (int,Q) or type(b) not in (int,Q) or c <= 0 or b <= 0:
        raise SuzukiWavefrontError("exact positive source scale required")
    c,b=Q(c),Q(b)
    segments=[(l,r,(vr-vl)/(r-l)) for (l,vl),(r,vr) in zip(t,t[1:])]
    total=Q()
    for l,r,du in segments:
        for s,t,dv in segments:
            integrand = _ramp_rect(l,r,s,t,c) + _ramp_rect(s,t,l,r,c)
            total += b*du*dv*integrand
    return total

def _abs_distance_rectangle(l:Q,r:Q,s:Q,t:Q)->Q:
    return (abs(r-s)**3-abs(l-s)**3-abs(r-t)**3+abs(l-t)**3)/6


def neumann_quadratic(steps:tuple[tuple[Q,Q,Q], ...],a:Q) -> tuple[Q,Q]:
    """K_a inverse-Neumann kernel vs exact norm of Dirichlet primitive.

    steps are complete consecutive segments (left,right,value), u mean zero.
    Both outputs must be equal on the declared mean-zero Neumann domain.
    """
    if type(a) not in (int,Q) or a <= 0 or type(steps) is not tuple or not steps:
        raise SuzukiWavefrontError("invalid Neumann carrier")
    a=Q(a)
    clean=[]
    for l,r,v in steps:
        if any(type(x) not in (int,Q) for x in (l,r,v)) or l>=r:
            raise SuzukiWavefrontError("nonempty exact source segments required")
        clean.append((Q(l),Q(r),Q(v)))
    if clean[0][0]!=-a or clean[-1][1]!=a or any(clean[i][1]!=clean[i+1][0] for i in range(len(clean)-1)):
        raise SuzukiWavefrontError("complete non-overlapping source needed")
    if sum((v*(r-l) for l,r,v in clean),Q()):
        raise SuzukiWavefrontError("Neumann inverse requires mean zero")
    form=Q()
    for l,r,v in clean:
        for s,t,u in clean:
            L1,L2=r-l,t-s
            x2=(r**3-l**3)/3
            y2=(t**3-s**3)/3
            integ=(x2*L2 + L1*y2)/(4*a) - _abs_distance_rectangle(l,r,s,t)/2 + a*L1*L2/6
            form += v*u*integ
    primitive=Q()
    value=Q()
    for l,r,u in clean:
        nxt=value+u*(r-l)
        primitive += (r-l)*(value*value+value*nxt+nxt*nxt)/3
        value=nxt
    if value or form != primitive:
        raise ArithmeticError("Neumann-vs-primitive identity failed")
    return form,primitive


def onset_archimedean_certificate() -> dict:
    """Rational proof certificate for a source-real first-prime boundary theorem.

    If 0 < w=2a-log2 <= log2/65536 and v is smooth supported entirely
    inside the two width-w endpoint strips, Suzuki's FULL Weil form obeys
         Q_W(v) > (8/35)*||v||².

    This uses the exact W formula and its full real-place contribution; it
    DOES NOT certify all of C_c^infinity(-a,a), lambda_a, or RH.
    """
    z=Q(1,3)
    lower_log2=2*sum((z**(2*k+1)/(2*k+1) for k in range(3)),Q())
    harmonic32=sum((Q(1,k) for k in range(1,33)),Q())
    gamma_upper=harmonic32-5*lower_log2
    e_upper=sum((Q(1,factorial(k)) for k in range(7)),Q())+Q(1,4410)
    exp26_lower=sum((Q(13,5)**k/factorial(k) for k in range(6)),Q())
    exp07_lower=sum((Q(7,10)**k/factorial(k) for k in range(4)),Q())
    sinh036_upper=(Q(9,25))/(1-Q(9,25)**2/6)
    checks={
        "log2_below_7_over_10":exp07_lower>2,
        "e_below_68_over_25":e_upper<Q(68,25),
        "exp11_below_65535":Q(68,25)**11<65535,
        "exp_13_over_5_exceeds_4pi_upper":exp26_lower>Q(88,7),
        "gamma_below_3_over_5":gamma_upper<Q(3,5),
        "four_sinh_a_below_3_over_2":4*sinh036_upper<Q(3,2),
        "inverse_sqrt2_above_7_over_10":Q(7,10)**2<Q(1,2),
        "log2_over_sqrt2_below_half":Q(7,10)/Q(7,5)<=Q(1,2),
        "wavefront_a_below_9_over_25":Q(7,20)*(1+Q(1,65536))<Q(9,25),
        "first_wavefront_below_log3":Q(7,10)*(1+Q(1,65536))<Q(1),
    }
    # log 3 > 1 follows because e < 3; source log 3 is certified.
    if not all(checks.values()):
        raise ArithmeticError("failed rigorous rational transcendental guard")
    bad_upper=Q(13,5)+Q(3,5)+Q(7,10)+Q(11,7)+Q(3,2)+Q(1,2)
    good_lower=Q(7,10)*11
    gap=good_lower-bad_upper
    if gap!=Q(8,35):
        raise ArithmeticError("incorrect quantitative positivity margin")
    return {
        "w_over_log2_max":"1/65536",
        "interval_type":"first prime only; two boundary strips",
        "log_shift_energy_lower":str(good_lower),
        "negative_and_prime_upper":str(bad_upper),
        "full_Weil_form_lower_over_L2":str(gap),
        "constant_inequality_checks":checks,
        "all_Cc_infinity_positivity_proved":False,
        "lambda_a_positive_proved":False,
        "uses_complete_real_place":True,
        "nontrivial_zero_positions_used":False,
        "RH_proved":False,
    }
