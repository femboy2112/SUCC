"""Two-sided SUCC Dirac comb -> continuous Gamma and Gamma_R (classical).

Domain: h>0 rational, Re(s)>0 for the actual two-sided integral/sum.
Pole continuation is a separate theorem, never evaluated by the divergent sum.
This does NOT derive the prime source, Weil positivity, or RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial


class DiracGammaError(ValueError):
    """Invalid rational mesh, chart, cutoff or spectral-domain request."""


def _mesh(h):
    if type(h) is int or isinstance(h, Fraction):
        q = Fraction(h)
        if q > 0:
            return q
    raise DiracGammaError("Clock spacing must be a strictly positive exact rational")


def _kind(kind):
    if kind not in ("Gamma", "Gamma_R"):
        raise DiracGammaError("Expected Gamma or Gamma_R (the pi-normalized real place)")
    return kind


def _integer(n, *, minimum, maximum, name):
    if type(n) is not int or not minimum <= n <= maximum:
        raise DiracGammaError(f"{name} must be an integer in {minimum}..{maximum}")
    return n


def _mp():
    try:
        import mpmath
    except ImportError as exc:
        raise DiracGammaError("mpmath required only for analytic readouts") from exc
    return mpmath


@dataclass(frozen=True)
class GammaClock:
    """The mesh, weight and frequency coupling are a declared source chart."""
    spacing: Fraction
    kind: str = "Gamma_R"

    def __post_init__(self):
        object.__setattr__(self, "spacing", _mesh(self.spacing))
        _kind(self.kind)

    @property
    def imaginary_period_pi_multiplier(self):
        """Exact: G_h(s+i*pi*c)=G_h(s) at c=2/h or 4/h."""
        return Fraction(4 if self.kind == "Gamma_R" else 2) / self.spacing

    def pole(self, m, k=0):
        """Exact symbolic pole and residue: residue = q*pi**pi_exponent.

        These are poles of the *meromorphically continued* infinite comb,
        not evaluations of its divergent original series outside Re(s)>0.
        """
        _integer(m, minimum=0, maximum=1000, name="Gamma pole index")
        _integer(k, minimum=-100000, maximum=100000, name="spectral alias index")
        arch = self.kind == "Gamma_R"
        return {
            "real_part": -2*m if arch else -m,
            "imaginary_pi_multiplier": self.imaginary_period_pi_multiplier * k,
            "residue_rational": Fraction((2 if arch else 1)*((-1)**m), factorial(m)),
            "residue_pi_exponent": m if arch else 0,
            "genuine_continuum_pole": k == 0,
            "sampling_alias": k != 0,
        }


def compact_comb_pairing(q):
    """Exact finite Riemann sum against C^1 compact test (1-u^2)^2_+.

    Integral = 16/15, ||f'||_1 = 2; mesh 1/q. A sample at +/-1
    vanishes; all other samples are actual finite rational SUCC events.
    The general W^{1,1} cellwise inequality bounds error by 2/q.
    """
    _integer(q, minimum=1, maximum=4096, name="clock denominator")
    h = Fraction(1, q)
    samples = tuple((Fraction(n,q), (1-Fraction(n*n,q*q))**2)
                    for n in range(-q,q+1))
    observed = h*sum((weight for _,weight in samples), Fraction())
    exact = Fraction(16,15)
    return {
        "events": len(samples),
        "mesh": h,
        "sum": observed,
        "integral": exact,
        "signed_error": observed-exact,
        "absolute_error": abs(observed-exact),
        "proved_error_ceiling": 2*h,
        "raw_unscaled_sum": observed/h,
    }


def direct_comb(s, clock: GammaClock, *, left=-600, right=60, dps=70):
    """Finite two-sided clock; analytically proved absolute tail and mesh bounds.

    Value and numeric bounds are mpmath (NOT outward-rounded intervals).
    The inequalities themselves hold in exact real analysis for Re(s)>0.
    No evaluation of nontrivial zeta zeros or prime-source coefficients.
    """
    if not isinstance(clock, GammaClock):
        raise DiracGammaError("Expected an explicit GammaClock")
    _integer(left, minimum=-20000, maximum=0, name="left cutoff")
    _integer(right, minimum=0, maximum=20000, name="right cutoff")
    if right-left > 20000:
        raise DiracGammaError("Finite clock budget exceeded")
    _integer(dps, minimum=25, maximum=250, name="decimal precision")
    mp = _mp()
    with mp.workdps(dps):
        h = mp.mpf(clock.spacing.numerator)/clock.spacing.denominator
        z = mp.mpc(s)
        beta = z/2 if clock.kind == "Gamma_R" else z
        rate = mp.pi if clock.kind == "Gamma_R" else mp.mpf(1)
        sigma = mp.re(beta)
        if sigma <= 0:
            raise DiracGammaError("Absolute two-sided comb requires Re(s)>0")
        first_right = (right+1)*h
        ratio = mp.exp(sigma*h-rate*mp.expm1(h)*mp.exp(first_right))
        if ratio >= 1:
            raise DiracGammaError("Right cutoff too early for a geometric tail bound")
        value = h*mp.fsum(mp.exp(beta*(n*h)-rate*mp.exp(n*h))
                         for n in range(left,right+1))
        left_tail = h*mp.exp(sigma*(left-1)*h)/(1-mp.exp(-sigma*h))
        right_tail = h*mp.exp(sigma*first_right-rate*mp.exp(first_right))/(1-ratio)
        continuum = (mp.power(mp.pi,-z/2)*mp.gamma(z/2)
                     if clock.kind == "Gamma_R" else mp.gamma(z))
        # Apply |h sum_n f(nh) - integral f| <= h*integral |f'(u)| du.
        mesh_bound = h*mp.power(rate,-sigma)*(abs(beta)*mp.gamma(sigma)
                                                   +mp.gamma(sigma+1))
        return {
            "clock_sum": +value,
            "continuum": +continuum,
            "observed_absolute_error": +abs(value-continuum),
            "left_tail_upper": +left_tail,
            "right_tail_upper": +right_tail,
            "mesh_error_upper": +mesh_bound,
            "combined_upper": +(left_tail+right_tail+mesh_bound),
            "period_pi_multiplier": clock.imaginary_period_pi_multiplier,
            "exact_domain": "Re(s)>0; mpmath outputs are NOT interval certificates",
            "RH_proved": False,
        }


def alias_sum(s, clock: GammaClock, *, aliases=3, dps=70):
    """Finite central segment of exact Poisson periodization, NOT tail-certified.

    G_h(s) = sum_{k in Z} Gamma(s-2*pi*i*k/h) or
    sum_{k in Z} Gamma_R(s-4*pi*i*k/h), valid Re(s)>0.
    """
    if not isinstance(clock, GammaClock):
        raise DiracGammaError("Expected an explicit GammaClock")
    _integer(aliases, minimum=0, maximum=100, name="alias radius")
    _integer(dps, minimum=25, maximum=250, name="decimal precision")
    mp = _mp()
    with mp.workdps(dps):
        h=mp.mpf(clock.spacing.numerator)/clock.spacing.denominator
        z=mp.mpc(s)
        if mp.re(z)<=0:
            raise DiracGammaError("Poisson periodization requires Re(s)>0")
        period=(4 if clock.kind=="Gamma_R" else 2)*mp.pi/h
        def value_at(w):
            return (mp.power(mp.pi,-w/2)*mp.gamma(w/2)
                    if clock.kind=="Gamma_R" else mp.gamma(w))
        return +mp.fsum(value_at(z-1j*k*period) for k in range(-aliases,aliases+1))


def mutated_continuum(s, *, rate, slope, dps=60):
    """Declared NONAUTHENTIC chart: integral exp(s*slope*u-rate*exp(u)).

    Used to show that changing pi or the half-density changes the
    limiting Gamma. A mutant is never relabelled an actual real place.
    """
    if type(rate) is not int and not isinstance(rate,Fraction):
        raise DiracGammaError("Mutation rate must be a positive rational")
    if type(slope) is not int and not isinstance(slope,Fraction):
        raise DiracGammaError("Mutation slope must be a positive rational")
    r, a = Fraction(rate), Fraction(slope)
    if r<=0 or a<=0:
        raise DiracGammaError("Mutation parameters must be positive")
    _integer(dps,minimum=25,maximum=250,name="decimal precision")
    mp=_mp()
    with mp.workdps(dps):
        z=mp.mpc(s)*mp.mpf(a.numerator)/a.denominator
        if mp.re(z)<=0:
            raise DiracGammaError("Integral requires Re(s)>0")
        rate_mp=mp.mpf(r.numerator)/r.denominator
        return +mp.power(rate_mp,-z)*mp.gamma(z)
