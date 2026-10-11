"""SUCC-shadow selection of the canonical gamma realization.

Mathematical setting: positive functions F on (0,infinity) with
F(x+1)=x F(x), F(1)=1. The ambiguity is F=Gamma*exp(q),
q continuous and 1-periodic. Fractional convexity windows translated
by SUCC detect q: Gamma curvature vanishes as n -> infinity while the
periodic component persists. Nonnegative windows select Gamma.

The sine-gauge examples have EXACT rational finite-witness certificates
via a trigamma upper bound. This is Bohr-Mollerup in operational clothing,
NOT a novel RH positivity theorem, nor a selection of complex-log
monodromy branches. Computation never executes the infinite path.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import floor


class WindowError(ValueError):
    pass


class WindowResourceExhausted(WindowError):
    pass


def _rational(x, name="rational"):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise WindowError(f"{name} must be exact int/Fraction, not float")


def _frequency(k):
    if type(k) is not int or not 1 <= k <= 4096:
        raise WindowError("Periodic frequency must be an integer in 1..4096")
    return k


def _mp():
    try:
        import mpmath as mp
    except ImportError as exc:
        raise WindowError("mpmath is required for non-certified numerical inspection") from exc
    return mp


def _mprat(mp, a: Fraction):
    return mp.mpf(a.numerator)/a.denominator


def _quarter_sine(phase: Fraction) -> int:
    """Return sin(2*pi*phase) EXACTLY when phase is a quarter-cycle."""
    phase %= 1
    index = 4*phase
    if index.denominator != 1:
        raise WindowError("This exact control uses only quarter-cycle phases")
    return (0, 1, 0, -1)[index.numerator % 4]


def periodic_quarter_probe(epsilon, frequency=1, *, center=Fraction(1,4)):
    """Log-gauge centered second difference on a FIXED quarter grid.

    Center 1/4, endpoints 0 and 1/2, regardless of gauge frequency.
    In particular a frequency-2 perturbation is fully invisible here.
    """
    e = _rational(epsilon, "gauge strength")
    r = _frequency(frequency)
    c = _rational(center, "quarter grid center")
    if c != Fraction(1,4):
        raise WindowError("The simple fixed probe is centered at 1/4")
    h = Fraction(1,4)
    q = lambda x: e*_quarter_sine(r*x)
    return q(c-h)+q(c+h)-2*q(c)


@dataclass(frozen=True)
class ShadowWindowCertificate:
    """Exact rational proof of one finite negative log-convexity window.

    The certificate does NOT prove that Gamma is a zeta or Weil form.
    Its positivity assumption is the external global convexity rule.
    """
    epsilon: Fraction
    frequency: int
    successor_stage: int
    fractional_center: Fraction
    half_width: Fraction
    gamma_curvature_upper_bound: Fraction
    periodic_curvature: Fraction

    @property
    def total_curvature_strictly_negative(self):
        return self.gamma_curvature_upper_bound+self.periodic_curvature < 0

    def report(self):
        return {
            "epsilon":str(self.epsilon), "frequency":self.frequency,
            "successor_stage":self.successor_stage,
            "fractional_center":str(self.fractional_center),
            "half_width":str(self.half_width),
            "gamma_second_difference_upper_bound":str(self.gamma_curvature_upper_bound),
            "gauge_second_difference_exact":str(self.periodic_curvature),
            "negative_total_certified":self.total_curvature_strictly_negative,
            "scope":"one finite rational sign certificate from a universal trigamma bound",
            "rh_or_weil_claim":False,
        }


def sine_gauge_witness(epsilon, frequency=1, *, max_stage=1_000_000):
    """A finite shadow-SUCC window falsifying log-convexity for every eps != 0.

    q(x)=eps*sin(2*pi*r*x), r=frequency. At center 1/(4r) if
    eps>0, 3/(4r) if eps<0, and h=1/(4r), the q window is
    EXACTLY -2*abs(eps).

    For center at n+theta and its two endpoints >=n,
    0 < Delta_h^2 logGamma <= h^2*(1/n + 1/n^2).
    Taking n > 1/(16*r^2*abs(eps)) guarantees negativity.
    This is conservative, not the least detecting stage.
    """
    e = _rational(epsilon, "gauge strength")
    r = _frequency(frequency)
    if e == 0:
        raise WindowError("The zero gauge IS the canonical Gamma, no negative witness")
    if abs(e).numerator.bit_length()>512 or abs(e).denominator.bit_length()>512:
        raise WindowResourceExhausted("Excessive rational gauge size")
    if type(max_stage) is not int or not 1 <= max_stage <= 1_000_000:
        raise WindowResourceExhausted("The finite stage budget must be 1..1000000")
    h = Fraction(1, 4*r)
    theta = (Fraction(1,4*r) if e>0 else Fraction(3,4*r))
    cap = Fraction(1, 16*r*r*abs(e))
    n = max(1, cap.numerator//cap.denominator+1)
    if n > max_stage:
        raise WindowResourceExhausted(
            "No CERTIFICATE in the declared stage budget; this does not mean no witness exists"
        )
    gamma_bound = h*h*(Fraction(1,n)+Fraction(1,n*n))
    certificate=ShadowWindowCertificate(
        epsilon=e,frequency=r,successor_stage=n,
        fractional_center=theta,half_width=h,
        gamma_curvature_upper_bound=gamma_bound,
        periodic_curvature=-2*abs(e)
    )
    if not certificate.total_curvature_strictly_negative:
        raise ArithmeticError("Internal proof-bound violated")
    return certificate


def certified_window_penalty_lower_bound(certificate: ShadowWindowCertificate, weight):
    """Strict rational lower bound on a weighted negative-curvature penalty.

    For any full-support atomic probe measure mu with this witness window
    assigned positive weight w, action A(F) = sum_j w_j
      * min(1, max(0,-W_j(F))**2)
    obeys A(F) >= this quantity > 0 for the certified nonzero sine
    gauge. Gamma has zero action. Values and weighting are separate.
    """
    if not isinstance(certificate, ShadowWindowCertificate):
        raise WindowError("Use an explicitly constructed certificate")
    w=_rational(weight,"positive atomic probe weight")
    if not 0 < w <= 1:
        raise WindowError("Probe weight must lie in (0,1]")
    margin=-(certificate.gamma_curvature_upper_bound+
             certificate.periodic_curvature)
    if not margin > 0:
        raise WindowError("This window has no rigorously negative margin")
    return w*min(Fraction(1),margin*margin)


def observed_window(certificate: ShadowWindowCertificate, *, dps=60):
    """Non-certified numerical readout, independent of the rational sign proof."""
    if not isinstance(certificate, ShadowWindowCertificate):
        raise WindowError("A previously checked window certificate is required")
    mp = _mp()
    with mp.workdps(dps):
        n = mp.mpf(certificate.successor_stage)
        c = n+_mprat(mp,certificate.fractional_center)
        h = _mprat(mp,certificate.half_width)
        gamma = mp.loggamma(c-h)+mp.loggamma(c+h)-2*mp.loggamma(c)
        gauge = _mprat(mp,certificate.periodic_curvature)
        return {
            "gamma_window":gamma,
            "gauge_window":gauge,
            "total":gamma+gauge,
            "negative":bool(gamma+gauge<0),
            "scope":"mpmath numerical check, NOT interval certification",
        }




def seam_gauge_witness(epsilon, *, max_stage=1_000_000):
    """Cross-integer SUCC seam for a deceptive cellwise-convex periodic gauge.

    q(x)=eps*({x}^2-{x}), eps>0, is continuous and 1-periodic.
    Inside each open cell, q''=2eps>0; EVERY same-cell convexity
    window passes. But at integers the derivative jumps down by
    2eps. For h=1/4 at integer n>=2:
        Delta_h^2 q(n)=-2eps*h*(1-h)=-3eps/8 < 0.
    Gamma's contribution <= h^2[1/(n-1)+1/(n-1)^2].
    Taking n-1>1/(3eps) certifies a finite violation.
    """
    e=_rational(epsilon,"periodic seam gauge strength")
    if e<=0:
        raise WindowError("This seam control requires positive gauge strength")
    if type(max_stage) is not int or not 2 <= max_stage <= 1_000_000:
        raise WindowResourceExhausted("Seam horizon must be in 2..1000000")
    h=Fraction(1,4)
    cutoff=Fraction(1,3*e)
    n=max(2,cutoff.numerator//cutoff.denominator+2)
    if n>max_stage:
        raise WindowResourceExhausted(
            "Seam witness lies beyond declared budget; no global impossibility follows"
        )
    upper=h*h*(Fraction(1,n-1)+Fraction(1,(n-1)**2))
    actual=-2*e*h*(1-h)
    witness=ShadowWindowCertificate(
        epsilon=e,frequency=1,successor_stage=n,fractional_center=Fraction(0),
        half_width=h,gamma_curvature_upper_bound=upper,periodic_curvature=actual
    )
    if not witness.total_curvature_strictly_negative:
        raise ArithmeticError("Internal seam certificate did not establish negativity")
    return witness


def same_cell_quadratic_gauge_curvature(epsilon,half_width):
    """Exact gauge-only curvature of q(x)=eps*(x^2-x) inside ONE unit cell.

    For eps>0 this is always positive. Same-cell-only probes fail to
    select Gamma, no matter how many integer SUCC stages they visit.
    """
    e=_rational(epsilon)
    h=_rational(half_width)
    if not e>0 or not 0<h<Fraction(1,2):
        raise WindowError("Positive gauge and 0<h<1/2 are required")
    return 2*e*h*h

def unseen_within_prefix(epsilon, horizon, frequency=1):
    """A conservative analytical *positive* lower bound for ALL matched windows
    at n in [1,horizon]. A nontrivial gauge may evade that finite probe class.

    Trigamma Psi'(x)>=1/x^2. All sampled endpoints lie <=n+1; hence
    Delta_h^2 logGamma >= h^2/(n+1)^2. If
      2|eps| <= h^2/(N+1)^2
    no matched frequency-r window is negative at any n<=N.
    A priori this says nothing about different probe locations or widths.
    """
    e=_rational(epsilon,"gauge strength")
    r=_frequency(frequency)
    if type(horizon) is not int or not 1 <= horizon <= 1_000_000:
        raise WindowResourceExhausted("Finite observation horizon must be 1..1000000")
    h=Fraction(1,4*r)
    return 2*abs(e) <= h*h/Fraction((horizon+1)**2)


@dataclass(frozen=True)
class WindingHistory:
    """Closed loops in C^*: endpoint exp(2*pi*i*wind)=1, lift remembers wind."""
    steps: tuple[int,...] = ()

    def __post_init__(self):
        steps=tuple(self.steps)
        if len(steps)>4096 or any(type(k) is not int or abs(k)>1_000_000 for k in steps):
            raise WindowResourceExhausted("Finite signed winding word required")
        object.__setattr__(self,"steps",steps)

    @property
    def winding(self):
        return sum(self.steps)

    @property
    def exponentiated_endpoint(self):
        return 1  # exactly exp(2*pi*i*integer), NOT a float

    def compose(self,other):
        if not isinstance(other,WindingHistory):
            raise WindowError("Only closed lifted complex-log paths may compose")
        return WindingHistory(self.steps+other.steps)

    def inverse(self):
        return WindingHistory(tuple(-k for k in reversed(self.steps)))


def quadratic_weight_gluing_defect(k,l,alpha):
    """For W(k)=exp(-alpha*k^2), log[W(k+l)/(W(k)W(l))]=-2alpha*k*l.

    A nonzero positive damped weighting is NOT a 1D character of the
    winding group. It cannot be a strictly composition-preserving
    scalar path weight without adding further gluing data.
    """
    if type(k) is not int or type(l) is not int:
        raise WindowError("Winding numbers must be exact signed integers")
    a=_rational(alpha,"damping strength")
    if a<0:
        raise WindowError("Damping strength must be nonnegative")
    return -2*a*k*l


def symmetric_positive_multiplicative_winding_weight_is_trivial():
    """Elementary no-go: W(k+l)=W(k)W(l), W(k)=W(-k)>0, W(0)=1
    gives W(k)^2=W(k)W(-k)=1, hence W(k)=1. A theorem, not a scan.
    """
    return True
