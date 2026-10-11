"""Two mathematical observer languages for ONE unit circle.

A (polynomial) uses the rational coordinate ring
    Q[x,y]/(x^2+y^2-1) = {a(x)+y*b(x)}
and B (angular) uses real trigonometric polynomials
    c_0 + sum_{n>=1}(c_n*cos(n theta)+s_n*sin(n theta)),
internally as conjugate-symmetric Gaussian-rational Laurent coefficients.

The two descriptions are algebraically isomorphic; they are NOT the same
as the path space, an unwrapped angle, a physical measurement instrument,
or a source-authenticated continuation transcript.

All finite calculations here use exact Fraction arithmetic. Winding results
for gamma_k(t)=exp(2*pi*i*k*t) are mathematical facts justified in the
research note; no numerical integration pretends to certify topology.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import lcm


class CircleTranslationError(ValueError):
    """An invalid coefficient, non-circle point, or overclaimed probe."""


def _q(value) -> Fraction:
    if type(value) is int or isinstance(value, Fraction):
        return Fraction(value)
    raise CircleTranslationError("Require exact integer/Fraction data")


def _trim(values) -> tuple[Fraction, ...]:
    if type(values) is not tuple or len(values) > 257:
        raise CircleTranslationError("Bounded immutable polynomial coefficients required")
    a = [_q(v) for v in values]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def _add(a, b):
    return _trim(tuple((a[k] if k < len(a) else Fraction()) +
                       (b[k] if k < len(b) else Fraction())
                       for k in range(max(len(a), len(b)))))


def _neg(a):
    return tuple(-x for x in a)


def _derivative(a):
    """Exact ordinary derivative of a rational polynomial in x."""
    return _trim(tuple((k+1)*a[k+1] for k in range(len(a)-1)))


def _mul(a, b):
    if not a or not b:
        return ()
    result = [Fraction() for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return _trim(tuple(result))


@dataclass(frozen=True)
class CirclePolynomial:
    """Canonical polynomial a(x)+y*b(x) on x^2+y^2=1."""

    a: tuple[Fraction, ...] = ()
    b: tuple[Fraction, ...] = ()

    def __post_init__(self):
        object.__setattr__(self, "a", _trim(self.a))
        object.__setattr__(self, "b", _trim(self.b))

    @classmethod
    def scalar(cls, x):
        v = _q(x)
        return cls((v,) if v else ())

    @classmethod
    def x(cls):
        return cls((0, 1))

    @classmethod
    def y(cls):
        return cls((), (1,))

    def __add__(self, other):
        if not isinstance(other, CirclePolynomial):
            return NotImplemented
        return CirclePolynomial(_add(self.a, other.a), _add(self.b, other.b))

    def __neg__(self):
        return CirclePolynomial(_neg(self.a), _neg(self.b))

    def __sub__(self, other):
        return self + (-other)

    def scale(self, factor):
        q = _q(factor)
        return CirclePolynomial(_trim(tuple(q*c for c in self.a)),
                                _trim(tuple(q*c for c in self.b)))

    def __mul__(self, other):
        if not isinstance(other, CirclePolynomial):
            return NotImplemented
        # y^2=1-x^2, so (a+yb)(c+yd)=(ac+(1-x^2)bd)+y(ad+bc).
        ac = _mul(self.a, other.a)
        bd = _mul(self.b, other.b)
        ad = _mul(self.a, other.b)
        bc = _mul(self.b, other.a)
        return CirclePolynomial(
            _add(ac, _mul((Fraction(1), Fraction(0), Fraction(-1)), bd)),
            _add(ad, bc),
        )

    def power(self, n: int):
        if type(n) is not int or not 0 <= n <= 64:
            raise CircleTranslationError("Finite nonnegative polynomial power required")
        result = CirclePolynomial.scalar(1)
        base = self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result

    def at_circle(self, x, y) -> Fraction:
        x, y = _q(x), _q(y)
        if x*x+y*y != 1:
            raise CircleTranslationError("Algebraic circle evaluation requires x²+y²=1")
        return (sum((c*x**k for k, c in enumerate(self.a)), Fraction())
                + y*sum((c*x**k for k, c in enumerate(self.b)), Fraction()))

    def angular_derivative(self):
        """Tangential rotation D=-y*d/dx+x*d/dy, well-defined on quotient.

        D(a(x)+yb(x))=xb-(1-x²)b'+y*(-a').
        Differentiating x²+y²-1 gives 0, so D descends to the ring.
        """
        a_prime = _derivative(self.a)
        b_prime = _derivative(self.b)
        return CirclePolynomial(
            _add(_mul((Fraction(0), Fraction(1)), self.b),
                 _neg(_mul((Fraction(1), Fraction(0), Fraction(-1)), b_prime))),
            _neg(a_prime),
        )

    @classmethod
    def from_monomials(cls, terms: dict[tuple[int, int], object]):
        if not isinstance(terms, dict) or len(terms) > 128:
            raise CircleTranslationError("Require finite polynomial monomial dictionary")
        result = cls()
        for powers, coeff in terms.items():
            if (type(powers) is not tuple or len(powers) != 2 or
                    any(type(n) is not int or not 0 <= n <= 32 for n in powers)):
                raise CircleTranslationError("Nonnegative bounded monomial exponents required")
            term = cls.x().power(powers[0]) * cls.y().power(powers[1])
            result = result + term.scale(coeff)
        return result


@dataclass(frozen=True)
class GaussianRational:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, "real", _q(self.real))
        object.__setattr__(self, "imag", _q(self.imag))

    def __add__(self, other):
        return GaussianRational(self.real+other.real, self.imag+other.imag)

    def __neg__(self):
        return GaussianRational(-self.real, -self.imag)

    def __mul__(self, other):
        return GaussianRational(self.real*other.real-self.imag*other.imag,
                                self.real*other.imag+self.imag*other.real)

    def scale(self, scalar):
        scalar = _q(scalar)
        return GaussianRational(self.real*scalar, self.imag*scalar)

    def conjugate(self):
        return GaussianRational(self.real, -self.imag)

    def is_zero(self):
        return self.real == 0 and self.imag == 0


@dataclass(frozen=True)
class TrigFourierPolynomial:
    """A real trig polynomial as conjugate-symmetric Laurent coefficients."""

    coefficients: tuple[tuple[int, GaussianRational], ...] = ()

    def __post_init__(self):
        if type(self.coefficients) is not tuple or len(self.coefficients) > 257:
            raise CircleTranslationError("Finite Fourier terms required")
        d = {}
        for item in self.coefficients:
            if type(item) is not tuple or len(item) != 2:
                raise CircleTranslationError("Each Fourier term is (integer frequency, coefficient)")
            n, q = item
            if type(n) is not int or not -128 <= n <= 128 or not isinstance(q, GaussianRational):
                raise CircleTranslationError("Invalid Fourier frequency or coefficient")
            if n in d:
                raise CircleTranslationError("Duplicated Laurent frequency")
            if not q.is_zero():
                d[n] = q
        if any(d.get(-n, GaussianRational()) != q.conjugate()
               for n, q in d.items()):
            raise CircleTranslationError("Fourier coefficients must define a real-valued function")
        object.__setattr__(self, "coefficients", tuple(sorted(d.items())))

    @classmethod
    def from_dict(cls, d):
        return cls(tuple(d.items()))

    @classmethod
    def scalar(cls, value):
        v = _q(value)
        return cls(((0, GaussianRational(v)),)) if v else cls()

    @classmethod
    def cos(cls):
        half = GaussianRational(Fraction(1, 2))
        return cls(((-1, half), (1, half)))

    @classmethod
    def sin(cls):
        return cls(((-1, GaussianRational(0, Fraction(1, 2))),
                    (1, GaussianRational(0, Fraction(-1, 2)))))

    def __add__(self, other):
        if not isinstance(other, TrigFourierPolynomial):
            return NotImplemented
        d = dict(self.coefficients)
        for n, v in other.coefficients:
            d[n] = d.get(n, GaussianRational()) + v
        return TrigFourierPolynomial.from_dict(d)

    def __neg__(self):
        return TrigFourierPolynomial(tuple((n, -v) for n, v in self.coefficients))

    def __sub__(self, other):
        return self+(-other)

    def scale(self, scalar):
        return TrigFourierPolynomial(tuple(
            (n, v.scale(scalar)) for n, v in self.coefficients))

    def __mul__(self, other):
        if not isinstance(other, TrigFourierPolynomial):
            return NotImplemented
        d = {}
        for n, v in self.coefficients:
            for m, w in other.coefficients:
                if abs(n+m) > 128:
                    raise CircleTranslationError("Fourier frequency budget exceeded")
                d[n+m] = d.get(n+m, GaussianRational()) + v*w
        return TrigFourierPolynomial.from_dict(d)

    def angular_derivative(self):
        """Exact d/dtheta: Laurent coefficient a_n -> i*n*a_n."""
        return TrigFourierPolynomial(tuple(
            (n, GaussianRational(0, n)*value)
            for n, value in self.coefficients
        ))

    @classmethod
    def from_circle(cls, polynomial: CirclePolynomial, orientation: int = 1):
        if not isinstance(polynomial, CirclePolynomial):
            raise CircleTranslationError("Translate only canonical circle polynomials")
        if type(orientation) is not int or orientation not in (-1,1):
            raise CircleTranslationError("Orientation calibration must be +1 or -1")
        x, y = cls.cos(), cls.sin().scale(orientation)
        xpower = cls.scalar(1)
        total = cls()
        for k in range(max(len(polynomial.a), len(polynomial.b))):
            if k < len(polynomial.a):
                total = total + xpower.scale(polynomial.a[k])
            if k < len(polynomial.b):
                total = total + (xpower*y).scale(polynomial.b[k])
            xpower = xpower*x
        return total

    @staticmethod
    def _cos_multiple(n):
        if n == 0:
            return CirclePolynomial.scalar(1)
        if n == 1:
            return CirclePolynomial.x()
        a, b, x = CirclePolynomial.scalar(1), CirclePolynomial.x(), CirclePolynomial.x()
        for _ in range(2, n+1):
            a, b = b, (x*b).scale(2)-a
        return b

    @staticmethod
    def _sin_multiple(n):
        if n == 0:
            return CirclePolynomial()
        if n == 1:
            return CirclePolynomial.y()
        a, b, x = CirclePolynomial(), CirclePolynomial.y(), CirclePolynomial.x()
        for _ in range(2, n+1):
            a, b = b, (x*b).scale(2)-a
        return b

    def to_circle(self, orientation: int = 1):
        if type(orientation) is not int or orientation not in (-1,1):
            raise CircleTranslationError("Orientation calibration must be +1 or -1")
        d = dict(self.coefficients)
        constant = d.get(0, GaussianRational()).real
        total = CirclePolynomial.scalar(constant)
        for n, c in self.coefficients:
            if n > 0:
                total = (total
                         + self._cos_multiple(n).scale(2*c.real)
                         + self._sin_multiple(n).scale(-2*c.imag))
        return (total if orientation == 1
                else CirclePolynomial(total.a, tuple(-q for q in total.b)))


def cardinal_point(quarter_turns: int, orientation: int = 1):
    """Exact trig-frame calibration at multiples of a quarter turn.

    Algebraic x/y basis holds fixed; orientation flips clockwise versus
    counterclockwise angle labels. A shared set of circle points does not
    choose either convention, and their winding signs are opposite.
    """
    if type(quarter_turns) is not int:
        raise CircleTranslationError("Exact quarter-turn integer required")
    if type(orientation) is not int or orientation not in (-1,1):
        raise CircleTranslationError("Only two calibrated orientations")
    k = quarter_turns % 4
    cardinal = ((Fraction(1), Fraction(0)),
                (Fraction(0), Fraction(1)),
                (Fraction(-1), Fraction(0)),
                (Fraction(0), Fraction(-1)))
    x,y = cardinal[k]
    return (x,orientation*y)


def oriented_winding(turns: int, orientation: int = 1):
    """Sign convention under circle reflection y→-y."""
    if type(turns) is not int or type(orientation) is not int or orientation not in (-1,1):
        raise CircleTranslationError("Calibrated integer winding required")
    return turns*orientation



def circle_angular_one_form_on_generator():
    """Algebraic contraction (x dy - y dx)(-y ∂x+x ∂y)=1.

    Its trig translation is the coefficient of dθ in the pullback.
    The global one-form is NOT d of a globally single-valued angle;
    see nonzero period / winding argument in the research note.
    """
    x, y = CirclePolynomial.x(), CirclePolynomial.y()
    return x*y.angular_derivative() - y*x.angular_derivative()



def rational_stereographic_chart(t):
    """The rational point map R -> circle, omitting the point (-1, 0)."""
    t = _q(t)
    d = 1 + t*t
    return ((1-t*t)/d, (2*t)/d)


def stereographic_inverse(x, y):
    x, y = _q(x), _q(y)
    if x*x+y*y != 1:
        raise CircleTranslationError("Inverse chart needs a point on the circle")
    if x == -1:
        return None  # The missing point, represented by t=infinity.
    return y/(1+x)


def multiply_circle_points(a, b):
    """Geometric rotation composition = algebraic complex multiplication."""
    x, y = (_q(a[0]), _q(a[1]))
    u, v = (_q(b[0]), _q(b[1]))
    if x*x+y*y != 1 or u*u+v*v != 1:
        raise CircleTranslationError("Composition requires two unit-circle points")
    return (x*u-y*v, x*v+y*u)


def _rational_samples(samples):
    if type(samples) is not tuple or len(samples) > 64:
        raise CircleTranslationError("Bounded immutable finite rational sample list required")
    return tuple(_q(t) for t in samples)


def periodic_point_signature(turns: int, samples):
    """Ideal sampled points gamma_k(t)=exp(2*pi*i*k*t), via phase mod 1.

    Fractional turns in [0,1) identify EXACT circle points in a fixed
    orientation and frame, without numeric floating trigonometric calls.
    """
    if type(turns) is not int or abs(turns) > 1000000:
        raise CircleTranslationError("Integer winding source required")
    times = _rational_samples(samples)
    return tuple((turns*t) % 1 for t in times)


@dataclass(frozen=True)
class WindingAliasingWitness:
    sample_times: tuple[Fraction, ...]
    original_turns: int
    aliased_turns: int
    original_points: tuple[Fraction, ...]
    aliased_points: tuple[Fraction, ...]
    finite_samples_equal: bool
    winding_numbers_equal: bool
    exact_winding_difference: int
    physical_infinity_observed: bool = False


def winding_alias_for_rational_samples(turns: int, samples):
    """Construct a path with different winding yet EXACT same finite samples.

    Let L = lcm(denominators of the rational sample times).
    Then exp(2*pi*i*(k+L)*t) = exp(2*pi*i*k*t) at each sample.
    Their genuine smooth closed paths have winding k+L and k, respectively.
    """
    times = _rational_samples(samples)
    if type(turns) is not int or abs(turns) > 1000000:
        raise CircleTranslationError("Bounded integer winding required")
    shift = lcm(*(t.denominator for t in times)) if times else 1
    if abs(turns+shift) > 1000000:
        raise CircleTranslationError("Result exceeds bounded executable winding family")
    a = periodic_point_signature(turns, times)
    b = periodic_point_signature(turns+shift, times)
    if a != b or shift == 0:
        raise ArithmeticError("Exact rational sample alias theorem contradicted")
    return WindingAliasingWitness(times, turns, turns+shift, a, b,
                                 a == b, turns == turns+shift, shift)


def cross_language_circle_demo():
    x, y = CirclePolynomial.x(), CirclePolynomial.y()
    algebraic = x*x+y*y-CirclePolynomial.scalar(1)
    trig = TrigFourierPolynomial.from_circle(algebraic)
    omega_coeff = circle_angular_one_form_on_generator()
    angular_intertwining = (
        TrigFourierPolynomial.from_circle(y.angular_derivative())
        == TrigFourierPolynomial.from_circle(y).angular_derivative()
    )
    assert omega_coeff == CirclePolynomial.scalar(1) and angular_intertwining
    point_a = rational_stereographic_chart(Fraction(1, 2))
    point_b = rational_stereographic_chart(Fraction(1, 3))
    rotated = multiply_circle_points(point_a, point_b)
    sample_times = (Fraction(0), Fraction(1, 4), Fraction(1, 2),
                    Fraction(3, 4), Fraction(1))
    witness = winding_alias_for_rational_samples(1, sample_times)
    assert (algebraic == CirclePolynomial() and trig == TrigFourierPolynomial()
            and rotated == (Fraction(0), Fraction(1))
            and witness.original_turns == 1 and witness.aliased_turns == 5
            and witness.finite_samples_equal and not witness.winding_numbers_equal)
    return {
        "status": "EXACT_CIRCLE_POLYNOMIAL_TRIG_TRANSLATOR",
        "coordinate_ring_identity_zero": algebraic == CirclePolynomial(),
        "trigonometric_polynomial_identity_zero": trig == TrigFourierPolynomial(),
        "angular_derivations_intertwine": angular_intertwining,
        "global_angular_one_form_coefficient_one": omega_coeff == CirclePolynomial.scalar(1),
        "global_single_valued_real_angle_claimed": False,
        "group_law_preserved": rotated == (Fraction(0), Fraction(1)),
        "orientation_requires_explicit_calibration": cardinal_point(1,1) != cardinal_point(1,-1),
        "reflected_winding_sign_inverted": oriented_winding(1,-1) == -1,
        "stereographic_chart_missing_point": [-1, 0],
        "finite_sample_times": [str(t) for t in sample_times],
        "matching_sampled_windings": [witness.original_turns, witness.aliased_turns],
        "identical_finite_phase_samples": witness.finite_samples_equal,
        "different_true_winding_numbers": not witness.winding_numbers_equal,
        "full_path_observability_proved_by_samples": False,
        "general_two_theory_translation_proved": False,
        "RH_claimed": False,
    }
