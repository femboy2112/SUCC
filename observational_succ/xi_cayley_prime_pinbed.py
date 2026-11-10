"""Source-typed critical-circle / prime Euler / Jensen observation instruments.

This is a finite exact-algebra and numerical *diagnostic* package, not an
RH proof, zero finder or completed Weil-positivity certificate.

Critical shift 1/2 in the deliberately changed prime factor is EXPLICIT and
must never be mistaken for the unshifted zeta Euler factor. No locations of
nontrivial zeta zeros enter any construction or test.

All Fraction routines perform rationally exact arithmetic. Python complex
and float routines are diagnostics only, never rigorous interval certificates.
"""
from __future__ import annotations

from fractions import Fraction
from math import exp, isfinite, log, pi
from typing import Sequence


def _q(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise TypeError("integer or Fraction required; floats cannot certify algebra")
    return Fraction(value)


def real_cayley(s: int | Fraction) -> Fraction:
    """Exact w=(s-1)/s on the real projective line, s != 0."""
    x = _q(s)
    if x == 0:
        raise ValueError("s=0 maps to infinity, not a finite disk point")
    return (x-1)/x


def critical_circle_at_height(t: int | Fraction) -> tuple[Fraction, Fraction]:
    """Exact image w of s=1/2+i*t in Q(i) coordinates.

    w=((4t^2-1)+4it)/(4t^2+1) and |w|^2=1 identically.
    """
    t = _q(t)
    denominator = 4*t*t + 1
    return ((4*t*t-1)/denominator, (4*t)/denominator)


def half_plane_horodisk(sigma: int | Fraction) -> tuple[Fraction, Fraction]:
    """Re s>sigma>0 is |w-c|<radius under s=1/(1-w)."""
    sigma = _q(sigma)
    if sigma <= 0:
        raise ValueError("positive half-plane threshold required")
    radius = 1/(2*sigma)
    return (1-radius, radius)


def exact_horodisk_margin(x: int | Fraction, y: int | Fraction,
                           sigma: int | Fraction = 1) -> Fraction:
    """Positive exactly inside the Euler half-plane's Cayley horodisk."""
    x, y = _q(x), _q(y)
    center, radius = half_plane_horodisk(sigma)
    return radius**2-(x-center)**2-y*y


def critical_line_zero_pair(a: int | Fraction) -> tuple[Fraction, Fraction]:
    """Off-line REAL symmetric fake zeros at s=1/2+-a, 0<a<1/2,
    returned in Cayley coordinates: one inside disk and its reciprocal outside.
    """
    a = _q(a)
    if not 0 < a < Fraction(1, 2):
        raise ValueError("fake off-line displacement in (0,1/2) required")
    inside = -(Fraction(1, 2)-a)/(Fraction(1, 2)+a)
    outside = 1/inside
    return inside, outside


def fake_completed_reflection(s: int | Fraction,
                              a: int | Fraction) -> Fraction:
    """Exact completed-reflection toy Q_a(s)=1+s(s-1)/(1/4-a^2).

    Q_a(0)=Q_a(1)=1, Q_a(1-s)=Q_a(s), and real zeros at 1/2+-a.
    These are *not* zeros of xi and this toy does NOT have the zeta Euler source.
    """
    s, a = _q(s), _q(a)
    critical_line_zero_pair(a)
    return 1+s*(s-1)/(Fraction(1, 4)-a*a)


def fake_disk_reflection(w: int | Fraction,
                         a: int | Fraction) -> Fraction:
    """Exactly Q_a(1/(1-w)), where w is real and !=1."""
    w = _q(w)
    if w == 1:
        raise ValueError("w=1 is the source-infinity point")
    a = _q(a)
    critical_line_zero_pair(a)
    return 1+w/((1-w)**2*(Fraction(1, 4)-a*a))


def fake_li_coefficient(n: int, a: int | Fraction) -> Fraction:
    """Exact nth coefficient of d/dw log Q_a(1/(1-w)) at w=0.

    For the inside zero -r and outside reciprocal zero -1/r, it is
    lambda_n=2+(-1)^(n+1)(r^n+r^(-n)).  In particular lambda_2<0.
    """
    if type(n) is not int or n < 1:
        raise ValueError("positive Li index required")
    inside, _ = critical_line_zero_pair(a)
    r = -inside
    return Fraction(2) + (-1)**(n+1)*(r**n + r**(-n))


def fake_jensen_exp_mean(r: int | Fraction,
                         a: int | Fraction) -> Fraction:
    """Exact exp[J_Qa(r)] for 0<r<1 and r not a zero radius.

    No approximation to log-integrals is needed: Jensen returns r/r_zero
    when the single inside zero has entered the radius, otherwise 1.
    """
    r = _q(r)
    if not 0 < r < 1:
        raise ValueError("strict interior radius required")
    inside, _ = critical_line_zero_pair(a)
    rzero = -inside
    if r == rzero:
        raise ValueError("choose a circle without zeros for Jensen calibration")
    return r/rzero if r > rzero else Fraction(1)


def upper_zero_count_from_jensen(r0: int | Fraction,
                                 r: int | Fraction,
                                 certified_exp_mean_upper: int | Fraction) -> int:
    """Exact Jensen zero-count bound given an EXTERNALLY CERTIFIED mean.

    If E>=exp(J(r)), then (r/r0)^N(r0)<=E.  This function does not
    compute or certify E for xi. The bound is valid only with a real proof
    of E and 0<r0<r<1, F(0)=1, F analytic in |w|<=r.
    """
    r0, r, e = _q(r0), _q(r), _q(certified_exp_mean_upper)
    if not 0 < r0 < r < 1 or e < 1:
        raise ValueError("0<r0<r<1, proven exp-mean bound >=1 required")
    growth = r/r0
    count = 0
    x = Fraction(1)
    while x*growth <= e:
        x *= growth
        count += 1
        if count > 100000:
            raise ValueError("bound too large for finite exact evaluator")
    return count


def prime_sieve(limit: int) -> tuple[int, ...]:
    """Exact elementary sieve, bounded to avoid accidental huge runs."""
    if type(limit) is not int or not 2 <= limit <= 1000000:
        raise ValueError("sieve cutoff integer in [2,1_000_000] required")
    s = bytearray(b'\x01')*(limit+1)
    s[0:2] = b'\x00\x00'
    for p in range(2, int(limit**0.5)+1):
        if s[p]:
            s[p*p:limit+1:p] = b'\x00'*(((limit-p*p)//p)+1)
    return tuple(p for p in range(2, limit+1) if s[p])


def half_density_prime_product_at_boundary(limit: int) -> Fraction:
    """Finite E_P(3/2)=prod_{p<=P}(1-1/p) exactly.

    Every finite E_P(s)=prod(1-p^(1/2-s)) has its zeros on Re(s)=1/2.
    The infinite-prime limit at s=3/2 is 0, NOT a finite-factor zero.
    """
    out = Fraction(1)
    for p in prime_sieve(limit):
        out *= Fraction(p-1, p)
    return out


def mertens_gamma_diagnostic(limit: int) -> float:
    """Numerical log(P)*E_P(3/2), tending to exp(-EulerGamma) classically."""
    return log(limit)*float(half_density_prime_product_at_boundary(limit))


def prime_euler_log_tail_bound(sigma: float, cutoff: int) -> float:
    """Analytically proved absolute log Euler-tail B for Re(s)>=sigma>1.

    Sum_{p>cutoff,k>=1} |p^(-ks)|/k <=
       cutoff^(1-sigma) / ((sigma-1)*(1-2^(-sigma))).
    This does not transport through Re(s)=1 or imply RH.
    """
    if (type(sigma) not in (int, float) or not isfinite(sigma)
            or sigma <= 1 or type(cutoff) is not int or cutoff < 2):
        raise ValueError("sigma>1 finite, prime cutoff>=2 required")
    return cutoff**(1-sigma)/((sigma-1)*(1-2**(-sigma)))


def completed_euler_product_diagnostic(s: complex, cutoff: int) -> complex:
    """Finite original-prime xi approximation in Re(s)>1 only.

    This is NOT the normalized half-density factor, not interval-certified,
    and requires mpmath only for special functions.  Do not use at s=1.
    """
    import mpmath as mp
    if complex(s).real <= 1:
        raise ValueError("original Euler product only certified in Re s>1")
    with mp.workdps(50):
        v = mp.mpc(s)
        eul = mp.mpc(1)
        for p in prime_sieve(cutoff):
            eul /= (1-mp.power(p, -v))
        out = mp.mpf('0.5')*v*(v-1)*mp.power(mp.pi,-v/2)*mp.gamma(v/2)*eul
        return complex(out)


def normalized_prime_pole_location(p: int, k: int,
                                   half_density: bool = False) -> complex:
    """Finite-prime factor zero/pole as a complex diagnostic, k!=0.

    Original factors: s=2pi ik/log(p), Cayley points Re(w)=1 OUTSIDE.
    Changed half-density: s=1/2+2pi ik/log(p), |w|=1 BOUNDARY.
    Values use float approximations; algebraic claims are proved in text.
    """
    if type(p) is not int or p < 2 or type(k) is not int or k == 0:
        raise ValueError("prime>=2 and nonzero integer frequency required")
    if p not in prime_sieve(p):
        raise ValueError("actual prime source only")
    s = (0.5 if half_density else 0) + 2j*pi*k/log(p)
    return (s-1)/s


def sampled_phase_winding_diagnostic(evaluate, radius: float,
                                     samples: int = 512) -> tuple[int, float, float]:
    """Numerical learning-observer path: measured phase winding round a disk.

    Returns (nearest integer winding, maximum measured phase increment,
    minimum sampled |F|). Even a beautiful integer and tiny phase increments
    DO NOT prove absence of unsampled zeros/winding excursions: independent
    analytic derivative/interval error bounds are required for certification.
    """
    import cmath
    if (not callable(evaluate) or type(radius) not in (int,float)
            or not isfinite(radius) or not 0 < radius < 1
            or type(samples) is not int or not 16 <= samples <= 100000):
        raise ValueError("finite callable, 0<r<1 and 16..100000 samples required")
    seq = [complex(evaluate(radius*cmath.exp(2j*pi*k/samples)))
           for k in range(samples)]
    if any(not isfinite(z.real) or not isfinite(z.imag) or abs(z) == 0 for z in seq):
        raise ValueError("sample contains zero or nonfinite source amplitude")
    increments = [cmath.phase(seq[(i+1)%samples]/seq[i])
                  for i in range(samples)]
    winding = round(sum(increments)/(2*pi))
    return winding, max(abs(x) for x in increments), min(abs(x) for x in seq)
