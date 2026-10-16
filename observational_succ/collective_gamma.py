"""Certified finite clocks for the normative Gamma_R(s)=pi**(-s/2) Gamma(s/2).

Stdlib only. Paper proofs and exact source pins: COLLECTIVE_GAMMA_CLOCKS.md.
Integer-grid intervals pay every arithmetic rounding. Decimal.exp is padded
by adjacent representable numbers; pi and trigonometry have rational proofs.
No special-function oracle, old-module import, prime source or positivity claim.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Context, Decimal, ROUND_HALF_EVEN
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, gcd, lcm


SOURCE_COMMIT = "849b241801578542997972eb46f3c8d309b36d0c"
SOURCE_MODULE_SHA256 = "05f8bb74ee202c4c8b8a53b05ddd03a92ba4121e2ccceba0b2474155232d14f5"


class GammaCertificateError(ValueError):
    """An exact input, finite budget, or enclosure precondition failed."""


def _q(x):
    if type(x) is int or isinstance(x, F):
        return F(x)
    raise GammaCertificateError("Only int/Fraction inputs; floats and bools are rejected")


def _integer(x, low, high, name):
    if type(x) is not int or not low <= x <= high:
        raise GammaCertificateError(f"{name} must be an integer in [{low}, {high}]")
    return x


def _ceil(x):
    return -((-x.numerator) // x.denominator)


def rational_gcd(meshes):
    """Positive generator of the additive subgroup spanned by rational meshes."""
    hs = tuple(_q(x) for x in meshes)
    if not hs or any(h <= 0 for h in hs):
        raise GammaCertificateError("A nonempty tuple of positive rational meshes is required")
    denominator = lcm(*(h.denominator for h in hs))
    return F(gcd(*(int(h * denominator) for h in hs)), denominator)


def joint_period_pi(meshes):
    """Least positive imaginary period of the R_h tuple, as a multiple of pi."""
    return 4 / rational_gcd(meshes)


def is_joint_period(meshes, pi_multiplier):
    hs = tuple(meshes)
    rational_gcd(hs)
    c = _q(pi_multiplier)
    return all((c * _q(h) / 4).denominator == 1 for h in hs)


@dataclass(frozen=True)
class Interval:
    """Closed interval [lo/10**digits, hi/10**digits], integer endpoints."""

    lo: int
    hi: int
    digits: int = 40

    def __post_init__(self):
        _integer(self.digits, 16, 100, "decimal grid digits")
        if type(self.lo) is not int or type(self.hi) is not int or self.lo > self.hi:
            raise GammaCertificateError("Ordered integer grid endpoints required")

    @classmethod
    def of(cls, x, digits=40):
        x = _q(x)
        _integer(digits, 16, 100, "decimal grid digits")
        y = x * 10**digits
        return cls(y.numerator // y.denominator, _ceil(y), digits)

    @classmethod
    def hull(cls, lower, upper, digits=40):
        lower, upper = _q(lower), _q(upper)
        if lower > upper:
            raise GammaCertificateError("Reversed interval")
        return cls(cls.of(lower, digits).lo, cls.of(upper, digits).hi, digits)

    @property
    def lower(self):
        return F(self.lo, 10**self.digits)

    @property
    def upper(self):
        return F(self.hi, 10**self.digits)

    @property
    def width(self):
        return self.upper - self.lower

    def contains(self, x):
        return self.lower <= _q(x) <= self.upper

    def _other(self, x):
        if not isinstance(x, Interval):
            x = Interval.of(x, self.digits)
        if x.digits != self.digits:
            raise GammaCertificateError("Mixed interval grids")
        return x

    def __add__(self, x):
        x = self._other(x)
        return Interval(self.lo + x.lo, self.hi + x.hi, self.digits)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo, self.digits)

    def __sub__(self, x):
        return self + -self._other(x)

    def __rsub__(self, x):
        return self._other(x) + -self

    def __mul__(self, x):
        x = self._other(x)
        products = (self.lo*x.lo, self.lo*x.hi, self.hi*x.lo, self.hi*x.hi)
        scale = 10**self.digits
        return Interval(min(products)//scale, -((-max(products))//scale), self.digits)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self._other(x)
        if x.lo <= 0 <= x.hi:
            raise GammaCertificateError("Division interval contains zero")
        scale = 10**self.digits
        ratios = tuple(F(a*scale, b) for a in (self.lo, self.hi) for b in (x.lo, x.hi))
        low, high = min(ratios), max(ratios)
        return Interval(low.numerator//low.denominator, _ceil(high), self.digits)

    def exp(self):
        lower = _exp_endpoint(self.lo, self.digits)[0]
        upper = _exp_endpoint(self.hi, self.digits)[1]
        return Interval(lower, upper, self.digits)

    def expand(self, radius):
        radius = _q(radius)
        if radius < 0:
            raise GammaCertificateError("Negative enclosure radius")
        return self + Interval.hull(-radius, radius, self.digits)

    def as_dict(self):
        return {"lower": str(self.lower), "upper": str(self.upper)}


@lru_cache(maxsize=8192)
def _exp_endpoint(n, digits):
    scale = 10**digits
    if n == 0:
        return scale, scale
    # e^3 > 1+3+9/2+27/6 > 10, so this is a proved absolute bound.
    if n < -3*digits*scale:
        return 0, 1
    if n > 10000*scale:
        raise GammaCertificateError("Positive exponential exceeds finite evaluation budget")
    # Tuple construction is exact and does not consult the ambient context.
    x = Decimal((int(n < 0), tuple(int(c) for c in str(abs(n))), -digits))
    ctx = Context(prec=digits+12, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999)
    y = ctx.exp(x)  # documented correctly rounded ROUND_HALF_EVEN, NOT directed
    a, b = F(ctx.next_minus(y))*scale, F(ctx.next_plus(y))*scale
    return max(0, a.numerator//a.denominator), _ceil(b)


@lru_cache(maxsize=100)
def pi_interval(digits=40):
    """Machin's identity with alternating-series rational remainder bounds."""
    _integer(digits, 16, 100, "decimal grid digits")
    def atan(q):
        total, k, term = F(0), 0, q
        threshold = F(1, 10**(digits+8))
        while True:
            total += term
            k += 1
            term = (-1)**k * q**(2*k+1) / (2*k+1)
            if abs(term) < threshold:
                return min(total, total+term), max(total, total+term)
    a, b = atan(F(1, 5))
    c, d = atan(F(1, 239))
    return Interval.hull(16*a-4*d, 16*b-4*c, digits)


@lru_cache(maxsize=8192)
def sin_cos(x):
    """Rigorous real sin/cos intervals, including argument-reduction debt."""
    if not isinstance(x, Interval):
        raise GammaCertificateError("An interval phase is required")
    p = pi_interval(x.digits)
    midpoint = (x.lower+x.upper)/2
    pi_midpoint = (p.lower+p.upper)/2
    k = (midpoint/(2*pi_midpoint)+F(1, 2)).__floor__()
    r = x - 2*k*p
    if max(abs(r.lower), abs(r.upper)) > 4:
        unit = Interval.hull(-1, 1, x.digits)
        return unit, unit
    n = 2
    while F(4**(2*n+1), factorial(2*n+1)) > F(1, 10**(x.digits+4)):
        n += 1
    sin_term, cos_term = r, Interval.of(1, x.digits)
    sine, cosine = sin_term, cos_term
    minus_square = -(r*r)
    for j in range(1, n+1):
        sin_term = sin_term*minus_square / ((2*j)*(2*j+1))
        cos_term = cos_term*minus_square / ((2*j-1)*(2*j))
        sine, cosine = sine+sin_term, cosine+cos_term
    # Lagrange bounds; both degrees are covered by this common majorant.
    remainder = F(4**(2*n+1), factorial(2*n+1))
    scale = 10**x.digits
    def clip(z):
        z = z.expand(remainder)
        return Interval(max(-scale, z.lo), min(scale, z.hi), x.digits)
    return clip(sine), clip(cosine)


@dataclass(frozen=True)
class Rectangle:
    real: Interval
    imag: Interval

    def __post_init__(self):
        if self.real.digits != self.imag.digits:
            raise GammaCertificateError("Mixed rectangle grids")

    def __add__(self, other):
        return Rectangle(self.real+other.real, self.imag+other.imag)

    def scale(self, coefficient):
        return Rectangle(self.real*coefficient, self.imag*coefficient)

    def expand(self, radius):
        return Rectangle(self.real.expand(radius), self.imag.expand(radius))

    def as_dict(self):
        return {"real": self.real.as_dict(), "imag": self.imag.as_dict()}


@dataclass(frozen=True)
class Strip:
    sigma_min: F
    sigma_max: F
    height: F

    def __post_init__(self):
        for field in ("sigma_min", "sigma_max", "height"):
            object.__setattr__(self, field, _q(getattr(self, field)))
        if not 0 < self.sigma_min <= self.sigma_max <= 64 or self.height < 0:
            raise GammaCertificateError("Require 0 < sigma_min <= sigma_max <= 64 and height >= 0")

    @property
    def contour_constant(self):
        # Gamma(a) <= 1/a_min + M!, a <= M+1, pi*cos(1)>1.
        return 2/self.sigma_min + factorial(_ceil(self.sigma_max/2)-1)


@dataclass(frozen=True)
class ErrorBudget:
    alias: F
    left_tail: F
    right_tail: F

    @property
    def total(self):
        return self.alias+self.left_tail+self.right_tail

    def as_dict(self):
        return {key: str(getattr(self, key)) for key in ("alias", "left_tail", "right_tail", "total")}


def alias_bound(mesh, strip, digits=40):
    """Uniform Poisson-replica majorant on the entire declared finite strip."""
    h = _q(mesh)
    if h <= 0 or not isinstance(strip, Strip):
        raise GammaCertificateError("Positive mesh and explicit Strip required")
    q = (-2*pi_interval(digits)/h).exp()
    return (2*strip.contour_constant*Interval.of(strip.height/2, digits).exp()*q/(1-q)).upper


def _cutoffs(h, left, right):
    if h <= 0:
        raise GammaCertificateError("Positive mesh required")
    _integer(left, -20000, 0, "left cutoff")
    _integer(right, 0, 20000, "right cutoff")
    if right-left+1 > 20000 or right*h > 20:
        raise GammaCertificateError("Finite sample budget exceeded (20000 events, u <= 20)")


def uniform_error(mesh, strip, left, right, digits=40):
    """Analytic error of the finite clock; arithmetic width is separate."""
    h = _q(mesh)
    _cutoffs(h, left, right)
    if not isinstance(strip, Strip):
        raise GammaCertificateError("An explicit Strip is required")
    iv = lambda x: Interval.of(x, digits)
    a, b, v = strip.sigma_min/2, strip.sigma_max/2, (right+1)*h
    left_bound = h*iv(a*(left-1)*h).exp()/(1-iv(-a*h).exp())
    pi_ev = pi_interval(digits)*iv(v).exp()
    ratio = (iv(b*h)-pi_ev*(iv(h).exp()-1)).exp()
    if ratio.upper >= 1:
        raise GammaCertificateError("Right cutoff does not certify a contracting tail")
    right_bound = h*(iv(b*v)-pi_ev).exp()/(1-ratio)
    return ErrorBudget(alias_bound(h, strip, digits), left_bound.upper, right_bound.upper)


def _sample(sigma, t, u, digits):
    iv = lambda x: Interval.of(x, digits)
    amplitude = (iv(sigma*u/2)-pi_interval(digits)*iv(u).exp()).exp()
    sine, cosine = sin_cos(iv(t*u/2))
    return Rectangle(amplitude*cosine, amplitude*sine)


@dataclass(frozen=True)
class GammaCertificate:
    sigma: F
    t: F
    mesh: F
    left: int
    right: int
    strip: Strip
    finite_sum: Rectangle
    error: ErrorBudget

    @property
    def enclosure(self):
        return self.finite_sum.expand(self.error.total)

    @property
    def coordinate_radius(self):
        """L-infinity error from the finite rectangle's exact rational midpoint."""
        return self.error.total + max(self.finite_sum.real.width, self.finite_sum.imag.width)/2

    def as_dict(self):
        return {
            "target": "Gamma_R(s)=pi^(-s/2)*Gamma(s/2)",
            "sigma": str(self.sigma), "t": str(self.t), "mesh": str(self.mesh),
            "left": self.left, "right": self.right,
            "strip": {key: str(getattr(self.strip, key)) for key in ("sigma_min", "sigma_max", "height")},
            "finite_sum": self.finite_sum.as_dict(), "error": self.error.as_dict(),
            "enclosure": self.enclosure.as_dict(), "coordinate_radius": str(self.coordinate_radius),
            "arithmetic": "integer rational grid; padded Decimal.exp; Machin pi; Taylor sin/cos",
        }


def certify_gamma(sigma, t, mesh, left, right, *, strip=None, digits=40):
    """Finite evaluation plus certified error for rational sigma>0 and rational t."""
    sigma, t, h = _q(sigma), _q(t), _q(mesh)
    strip = Strip(sigma, sigma, abs(t)) if strip is None else strip
    if not isinstance(strip, Strip) or not strip.sigma_min <= sigma <= strip.sigma_max or abs(t) > strip.height:
        raise GammaCertificateError("Evaluation point is outside the declared strip")
    error = uniform_error(h, strip, left, right, digits)
    zero = Interval.of(0, digits)
    value = Rectangle(zero, zero)
    for n in range(left, right+1):
        value = value + _sample(sigma, t, n*h, digits).scale(h)
    return GammaCertificate(sigma, t, h, left, right, strip, value, error)


def decode_lanes(values):
    """Fixed arithmetic mean, with NO extra s input. Source coverage is upstream."""
    values = tuple(values)
    if not values or any(not isinstance(v, Rectangle) for v in values):
        raise GammaCertificateError("Nonempty tuple of lane rectangles required")
    total = values[0]
    for value in values[1:]:
        total = total+value
    return total.scale(F(1, len(values)))


def cooperative_gamma(sigma, t, base_mesh, lane_count, left, right, *, strip=None, digits=40, lanes=None):
    """Complete shifted lanes reconstruct a refined finite clock with a certificate.

    L..R are FINE-grid indices. Lane r contains precisely n == r (mod m),
    including negative n, with weight base_mesh. The decoder averages lanes.
    This adds translated source samples; it does not synthesize them from R_h.
    """
    m = _integer(lane_count, 1, 64, "lane count")
    order = tuple(range(m)) if lanes is None else tuple(lanes)
    if any(type(r) is not int for r in order) or sorted(order) != list(range(m)):
        raise GammaCertificateError("Each shifted lane must appear exactly once")
    sigma, t, h = _q(sigma), _q(t), _q(base_mesh)
    fine = h/m
    strip = Strip(sigma, sigma, abs(t)) if strip is None else strip
    if not isinstance(strip, Strip) or not strip.sigma_min <= sigma <= strip.sigma_max or abs(t) > strip.height:
        raise GammaCertificateError("Evaluation point is outside the declared strip")
    error = uniform_error(fine, strip, left, right, digits)
    zero = Interval.of(0, digits)
    values = {r: Rectangle(zero, zero) for r in order}
    for n in range(left, right+1):
        r = n % m
        values[r] = values[r]+_sample(sigma, t, n*fine, digits).scale(h)
    decoded = decode_lanes(values[r] for r in order)
    certificate = GammaCertificate(sigma, t, fine, left, right, strip, decoded, error)
    return certificate, tuple((r, values[r]) for r in order)
