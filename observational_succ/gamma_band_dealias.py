"""Certified band-uniform de-aliasing for the original real-place Gamma source.

No zeta zero or positive Weil form is read. Rational bounds are *mathematically*
exact: they use only integer operations and Fraction, plus pi > 3 and the
Taylor lower polynomial for exp. No floating point/interval inference occurs.
Analytic evaluations are optional independent diagnostics (mpmath).

Source: Gaussian Tate real-place kernel f_s(u)=exp(s*u/2-pi*exp(u));
Re(s)>0. Interleaved subclocks cost q times as many source events.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial


class GammaBandError(ValueError):
    """Rejected mesh, source type, unattested norm or spectral budget."""


def _rational(x, name, *, strictly_positive=False, nonnegative=False):
    if type(x) is not int and not isinstance(x, Fraction):
        raise GammaBandError(f"{name} requires an integer or Fraction, not an approximate float")
    q = Fraction(x)
    if strictly_positive and q <= 0:
        raise GammaBandError(f"{name} must be strictly positive")
    if nonnegative and q < 0:
        raise GammaBandError(f"{name} must be nonnegative")
    return q


def _int(x, name, lower, upper):
    if type(x) is not int or not lower <= x <= upper:
        raise GammaBandError(f"{name} must be an integer in {lower}..{upper}")
    return x


def _exp_lower_polynomial(x: Fraction, order: int) -> Fraction:
    """Exact rational P_N(x) <= exp(x), x >= 0."""
    if x < 0:
        raise GammaBandError("An exponential majorant requires nonnegative exponent")
    return sum((x**j / factorial(j) for j in range(order+1)), Fraction(0))


def uniform_phase_filter(interleaves: int, alias_index: int) -> int:
    """Exact DFT coefficient of q equally weighted, equally spaced offsets.

    (1/q) sum_{j=0}^{q-1} exp(2*pi*i*k*j/q) equals 1 iff q divides k.
    No floating point approximation to roots of unity is necessary.
    """
    q = _int(interleaves, "subclock count", 1, 64)
    k = _int(alias_index, "alias index", -1000000, 1000000)
    return int(k % q == 0)


def gamma_r_band_certificate(spacing, sigma_min, sigma_max, imag_radius, *,
                             interleaves=1, left_steps=250, right_steps=24,
                             taylor_order=64):
    """Exact rational, source-conditional *finite sampling* certificate.

    For all s with sigma_min <= Re(s) <= sigma_max and |Im(s)| <= imag_radius:
       | (h/q) sum_{n=-left_steps}^{right_steps} f_s(n h/q) - Gamma_R(s) |
            <= total_upper  (a Fraction).
    This is a proof by the Poisson/contour-shift theorem and two geometric
    tails; not a rounding certificate for any floating evaluation. The genuine
    pi and s/2 in the source are mandatory and are never derived from primes.
    The rational spectral guard T < 12q/h is conservative vs the exact first
    alias height 4*pi*q/h, because pi > 3 is used for rational bounds.
    """
    h = _rational(spacing, "coarse clock spacing", strictly_positive=True)
    a = _rational(sigma_min, "minimum real part", strictly_positive=True)
    b = _rational(sigma_max, "maximum real part", strictly_positive=True)
    t = _rational(imag_radius, "imaginary band radius", nonnegative=True)
    q = _int(interleaves, "subclock count", 1, 64)
    left = _int(left_steps, "left retained steps", 0, 50000)
    right = _int(right_steps, "right retained steps", 0, 50000)
    n = _int(taylor_order, "Taylor order", 1, 256)
    if a > b:
        raise GammaBandError("Minimum real part exceeds maximum")
    if left+right+1 > 50000:
        raise GammaBandError("Finite-event budget exceeded")
    d = h/q
    gap = 6/d - t/2
    if gap <= 0:
        raise GammaBandError("Band meets rational spectral alias guard T < 12q/h")

    # Gamma(z) <= 1/z_min + (ceil(z_max)-1)! from Euler's positive integral,
    # splitting at x=1; (pi*cos(pi/3))^{-z} <= 1 because pi/2 > 1.
    ceil_zmax = -(-(b/2).numerator // (b/2).denominator)
    m = 2/a + factorial(ceil_zmax-1)
    alias = 2*m*(1+d/6) / _exp_lower_polynomial(gap,n)

    # Left negative-time tail is dominated by a geometric exp(a*u/2).
    lx = a*(left+1)*d/2
    ltail = (2/a+d) / _exp_lower_polynomial(lx,n)

    # Right tail: exp(u) >= 1+u+u^2/2, exp(d)-1 >= d and pi > 3.
    u0 = (right+1)*d
    lam = 3*(1+u0)-b/2
    eta = 3*(1+u0+u0*u0/2)-b*u0/2
    if lam <= 0 or eta < 0:
        raise GammaBandError("Right cutoff is not far enough for rational tail majorant")
    rtail = (d+1/lam) / _exp_lower_polynomial(eta,n)

    return {
        "source": "GAUSSIAN_TATE_REAL_PLACE_PI_NORMALIZED_S_HALF",
        "status": "ANALYTIC_THEOREM_EXACT_RATIONAL_BOUND",
        "coarse_spacing": h,
        "effective_spacing": d,
        "interleaves": q,
        "source_event_count": left+right+1,
        "positive_real_strip": (a,b),
        "imaginary_band_radius": t,
        "first_surviving_alias_imaginary_pi_multiplier": Fraction(4*q,1)/h,
        "conservative_rational_band_margin": 12/d-t,
        "gamma_integral_majorant": m,
        "alias_error_upper": alias,
        "left_tail_upper": ltail,
        "right_tail_upper": rtail,
        "total_upper": alias+ltail+rtail,
        "taylor_order": n,
        "actual_prime_source_authenticated": False,
        "Weil_sign_proved": False,
        "RH_proved": False,
    }



def gamma_r_jet_certificate(spacing, sigma_min, sigma_max, imag_radius,
                              *, collar, jet_order=1, interleaves=1,
                              left_steps=250, right_steps=24, taylor_order=64):
    """Exact rational uniform bound on s-derivative *errors* by Cauchy.

    Require an authenticated open complex collar of radius r>0 around every
    point of the target band; it must stay in Re(s)>0. On the expanded strip
    [a-r,b+r] x [-T-r,T+r], the same clock has a rational error bound B.
    Analyticity and the Cauchy estimate give, for each point in the original
    band, |(finite_clock-Gamma_R)^(j)(s)| <= j!*B/r^j.
    This certifies Gamma_R jets only, not digamma log derivatives or the
    completed Suzuki/Weil form.
    """
    a=_rational(sigma_min,"minimum real part",strictly_positive=True)
    b=_rational(sigma_max,"maximum real part",strictly_positive=True)
    T=_rational(imag_radius,"imaginary band radius",nonnegative=True)
    r=_rational(collar,"complex Cauchy collar",strictly_positive=True)
    j=_int(jet_order,"jet order",0,12)
    if r>=a:
        raise GammaBandError("Cauchy collar crosses the Gamma integral domain")
    expanded=gamma_r_band_certificate(
        spacing,a-r,b+r,T+r,interleaves=interleaves,
        left_steps=left_steps,right_steps=right_steps,
        taylor_order=taylor_order)
    return {
        "jet_order":j,
        "collar":r,
        "expanded_band_total_upper":expanded["total_upper"],
        "jet_error_upper":factorial(j)*expanded["total_upper"]/r**j,
        "exact_rational":True,
        "source":expanded["source"],
        "Weil_sign_proved":False,
        "RH_proved":False,
    }


def compact_mellin_band_bound(spacing, imag_radius, derivative_l1_upper,
                              *, derivative_order=2, interleaves=1):
    """Conditional all-frequency band Poisson bound for general compact log tests.

    Let g_sigma(u)=exp(sigma*u/2)*phi(exp(u)). REQUIRE externally PROVED
    sup over the sigma interval of ||g_sigma^(N)||_L1 <= D, and g_sigma in
    W^{N,1}(R) with sufficient decay. The sigma interval and phi are source
    metadata, not authenticated by this function. The actual Mellin test is
    exp(i*t*u/2)*g_sigma(u) and is sampled on mesh d=h/q.

    For |t|<=T<12/d, error <= 2D (d/6)^N
      * [(1-a)^-N + (1-a)^(1-N)/(N-1)], a=d*T/12.
    Exact rational, using pi>3. The theorem includes smooth compact Tate tests
    but does not prove a supplied norm bound or the full adelic interface.
    """
    h = _rational(spacing,"coarse clock spacing",strictly_positive=True)
    t = _rational(imag_radius,"imaginary band radius",nonnegative=True)
    D = _rational(derivative_l1_upper,"independently proved derivative L1 bound",nonnegative=True)
    N = _int(derivative_order,"derivative order",2,50)
    q = _int(interleaves,"subclock count",1,64)
    d = h/q
    a = d*t/12
    if a >= 1:
        raise GammaBandError("Band outside rational compact Mellin alias guard")
    b=1-a
    bound=2*D*(d/6)**N*(b**(-N)+b**(1-N)/(N-1))
    return {
        "bound":bound,
        "spacing":d,
        "source_derivative_norm_required":D,
        "conditional_on_verified_L1_bound":True,
        "source_identity_checked":False,
        "Weil_sign_proved":False,
    }


def sampled_gamma_r(s, spacing, *, left_steps=250, right_steps=24,
                    interleaves=1, dps=75):
    """Numeric diagnostic; no directed rounding or certification of mpmath.

    Independently assembles the *same finite events* as (i) a refined ladder
    and (ii) q staggered SUCC charts grouped by residues. The exact identity
    is arithmetic reindexing, not a claim of independent source evidence.
    """
    h=_rational(spacing,"coarse clock spacing",strictly_positive=True)
    q=_int(interleaves,"subclock count",1,64)
    left=_int(left_steps,"left retained steps",0,50000)
    right=_int(right_steps,"right retained steps",0,50000)
    prec=_int(dps,"working precision",25,200)
    if left+right+1>50000:
        raise GammaBandError("Finite-event budget exceeded")
    try:
        import mpmath as mp
    except ImportError as exc:
        raise GammaBandError("mpmath required for noncertified numerical diagnostics") from exc
    with mp.workdps(prec):
        z=mp.mpc(s)
        if mp.re(z)<=0:
            raise GammaBandError("Euler integral chart requires Re(s)>0")
        H=mp.mpf(h.numerator)/h.denominator
        d=H/q
        f=lambda u: mp.exp(z*u/2-mp.pi*mp.exp(u))
        refined=d*mp.fsum(f(n*d) for n in range(-left,right+1))
        charts=[]
        for j in range(q):
            chart=mp.fsum(f(H*k+j*d)
                for k in range((-left-j)//q, (right-j)//q+1)
                if -left<=q*k+j<=right)
            charts.append(chart)
        interleaved=d*mp.fsum(charts)
        gamma=mp.power(mp.pi,-z/2)*mp.gamma(z/2)
        return {
            "refined":+refined,
            "interleaved":+interleaved,
            "coherent_chart_disagreement":+abs(refined-interleaved),
            "true_gamma_r":+gamma,
            "observed_absolute_error":+abs(refined-gamma),
            "number_of_events":left+right+1,
            "q":q,
            "numeric_only":True,
            "RH_proved":False,
        }
