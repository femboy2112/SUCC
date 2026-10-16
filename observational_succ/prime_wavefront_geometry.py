"""Exact isolated hinge geometry; authenticated prime-only source enclosures.

On I=(-a,a), T_b u(x)=c int_I (|x-y|-b)_+ u(y)dy. Rational kernels
are integrated exactly. Source logarithms remain intervals, never rational
surrogates. No Gamma/pole/contact completion or positivity is inferred.

Polynomial primitives are reused from suzuki_legendre_source. Real rational
form matrices use the supplied basis without implicit normalization. The
paper identities extend sesquilinearly to complex L2; this API is rational.
"""
from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass
from fractions import Fraction as Q

from . import suzuki_legendre_source as poly


class WavefrontGeometryError(ValueError):
    """Invalid exact geometry, projection, or arithmetic source contract."""


def _q(value):
    if type(value) not in (int, Q):
        raise WavefrontGeometryError("integer or Fraction required")
    return Q(value)


def _radius(value):
    value = _q(value)
    if value <= 0:
        raise WavefrontGeometryError("positive radius required")
    return value


def _polynomial(values):
    values = tuple(_q(v) for v in values)
    if not values:
        raise WavefrontGeometryError("empty polynomial")
    return poly.poly_add(values, (Q(),))


def _modes(modes):
    modes = tuple(modes)
    if any(type(n) is not int or not 0 <= n <= 40 for n in modes):
        raise WavefrontGeometryError("Legendre modes must be integers in 0..40")
    if len(set(modes)) != len(modes):
        raise WavefrontGeometryError("duplicate projection mode")
    return modes


def _shift(p, offset):
    """p(x+offset), using the shared polynomial algebra."""
    result = (Q(),)
    for coefficient in reversed(p):
        result = poly.poly_add(poly.poly_mul(result, (offset, Q(1))),
                               (coefficient,))
    return result


@dataclass(frozen=True)
class Hinge:
    threshold: Q
    weight: Q = Q(1)

    def __post_init__(self):
        object.__setattr__(self, "threshold", _q(self.threshold))
        object.__setattr__(self, "weight", _q(self.weight))
        if self.threshold < 0:
            raise WavefrontGeometryError("nonnegative hinge threshold required")


@dataclass(frozen=True)
class PiecewisePolynomial:
    """Rational polynomials on an ordered finite interval partition.

    Values at interior knots use the right trace. Integration ignores single
    points; weak_derivative refuses jumps instead of discarding Dirac masses.
    """
    breaks: tuple[Q, ...]
    pieces: tuple[tuple[Q, ...], ...]

    def __post_init__(self):
        breaks = tuple(_q(v) for v in self.breaks)
        pieces = tuple(_polynomial(p) for p in self.pieces)
        if len(breaks) < 2 or len(pieces) != len(breaks) - 1:
            raise WavefrontGeometryError("partition/polynomial count mismatch")
        if any(l >= r for l, r in zip(breaks, breaks[1:])):
            raise WavefrontGeometryError("strictly increasing partition required")
        object.__setattr__(self, "breaks", breaks)
        object.__setattr__(self, "pieces", pieces)

    def polynomial_at(self, x):
        x = _q(x)
        if not self.breaks[0] <= x <= self.breaks[-1]:
            raise WavefrontGeometryError("point outside the carrier")
        return self.pieces[min(bisect_right(self.breaks, x) - 1,
                               len(self.pieces) - 1)]

    def value(self, x):
        return poly.poly_eval(self.polynomial_at(x), _q(x))

    def weak_derivative(self):
        for i, x in enumerate(self.breaks[1:-1]):
            if poly.poly_eval(self.pieces[i], x) != poly.poly_eval(self.pieces[i+1], x):
                raise WavefrontGeometryError("jump: weak derivative has a Dirac mass")
        return PiecewisePolynomial(self.breaks,
                                   tuple(poly.poly_derivative(p) for p in self.pieces))

    def integral(self):
        return sum((poly.poly_integral(p, l, r) for p, l, r in
                    zip(self.pieces, self.breaks, self.breaks[1:])), Q())

    def inner(self, other):
        breaks = _common_partition(self, other)
        return sum((poly.poly_integral(poly.poly_mul(self.polynomial_at((l+r)/2),
                                                    other.polynomial_at((l+r)/2)), l, r)
                    for l, r in zip(breaks, breaks[1:])), Q())

    def add(self, other, scale=Q(1)):
        breaks = _common_partition(self, other)
        scale = _q(scale)
        return PiecewisePolynomial(breaks, tuple(
            poly.poly_add(self.polynomial_at((l+r)/2), other.polynomial_at((l+r)/2), scale)
            for l, r in zip(breaks, breaks[1:])))


def _common_partition(left, right):
    if (left.breaks[0], left.breaks[-1]) != (right.breaks[0], right.breaks[-1]):
        raise WavefrontGeometryError("different carriers")
    return tuple(sorted(set(left.breaks + right.breaks)))


def polynomial_on_interval(p, a):
    a = _radius(a)
    return PiecewisePolynomial((-a, a), (_polynomial(p),))


def hinge_response(a, polynomial, hinge):
    """Exact T_b p on I, including b=0, overlapping strips and b>=2a."""
    a = _radius(a)
    p = _polynomial(polynomial)
    if not isinstance(hinge, Hinge):
        raise WavefrontGeometryError("Hinge required")
    b, c = hinge.threshold, hinge.weight
    breaks = tuple(sorted({-a, a} | {v for v in (b-a, a-b) if -a < v < a}))
    primitive = poly.poly_primitive_zero_at_left(p, a)
    moment = poly.poly_primitive_zero_at_left(poly.poly_mul((Q(), Q(1)), p), a)
    pieces = []
    for left, right in zip(breaks, breaks[1:]):
        x = (left+right)/2
        result = (Q(),)
        if x-b > -a:
            result = poly.poly_add(poly.poly_mul((-b, Q(1)), _shift(primitive, -b)),
                                   _shift(moment, -b), -1)
        if x+b < a:
            tail = poly.poly_add((poly.poly_eval(moment, a),), _shift(moment, b), -1)
            mass = poly.poly_add((poly.poly_eval(primitive, a),), _shift(primitive, b), -1)
            result = poly.poly_add(result, poly.poly_add(
                tail, poly.poly_mul((b, Q(1)), mass), -1))
        pieces.append(poly.poly_scale(result, c))
    return PiecewisePolynomial(breaks, tuple(pieces))


def hinge_sum_response(a, polynomial, hinges):
    result = polynomial_on_interval((0,), a)
    for hinge in hinges:
        result = result.add(hinge_response(a, polynomial, hinge))
    return result


def project_legendre(function, modes):
    """Orthogonal L2 projection; includes mode 0 only when explicitly asked."""
    if function.breaks[0] != -function.breaks[-1]:
        raise WavefrontGeometryError("symmetric interval required")
    a = function.breaks[-1]
    result = (Q(),)
    for n in _modes(modes):
        p = poly.legendre_polynomial(n, a)
        coefficient = function.inner(polynomial_on_interval(p, a)) * Q(2*n+1)/(2*a)
        result = poly.poly_add(result, p, coefficient)
    return polynomial_on_interval(result, a)


def derivative_response(a, polynomial, hinges, *, output_modes=(), derivative_modes=()):
    """(I-P_derivative) D (I-P_output) T p; operation order is deliberate.

    For Round II's quotient map Pi_M D G use output_modes=() and
    derivative_modes=(0,1,2,3). These two projections are not interchangeable.
    """
    response = hinge_sum_response(a, polynomial, hinges)
    response = response.add(project_legendre(response, output_modes), -1)
    derivative = response.weak_derivative()
    return derivative.add(project_legendre(derivative, derivative_modes), -1)


def hinge_matrix(a, test_polynomials, input_polynomials, hinges):
    """Exact raw form entries <test_i,T input_j>, no positivity assertion."""
    hinges = tuple(hinges)
    tests = tuple(polynomial_on_interval(p, a) for p in test_polynomials)
    responses = tuple(hinge_sum_response(a, p, hinges) for p in input_polynomials)
    return tuple(tuple(p.inner(r) for r in responses) for p in tests)


def derivative_gram(a, polynomials, hinges, *, output_modes=(), derivative_modes=()):
    """Exact continuum Gram of the explicitly ordered derivative responses."""
    hinges, output_modes, derivative_modes = tuple(hinges), _modes(output_modes), _modes(derivative_modes)
    columns = tuple(derivative_response(a, p, hinges, output_modes=output_modes,
                                       derivative_modes=derivative_modes) for p in polynomials)
    return tuple(tuple(f.inner(g) for g in columns) for f in columns)


def hinge_hs_inner(a, left, right, *, derivative=False):
    """Raw kernel HS pairing, or pairing of first derivative kernels."""
    a = _radius(a)
    if not isinstance(left, Hinge) or not isinstance(right, Hinge):
        raise WavefrontGeometryError("Hinge pair required")
    b = max(left.threshold, right.threshold)
    delta = max(Q(), 2*a-b)
    if derivative:
        return left.weight * right.weight * delta**2
    integrand = poly.poly_mul((2*a, Q(-1)), poly.poly_mul(
        (-left.threshold, Q(1)), (-right.threshold, Q(1))))
    return 2*left.weight*right.weight*poly.poly_integral(integrand, b, b+delta)


def projection_hs_audit(a, hinges, modes):
    """Exact HS squares for D T Q, Q D T Q, and D Q T Q (Q=I-P).

    The last value has NO assumed contraction. Derivative kernel k'(x-y)
    is skew-adjoint; this computes the finite-rank correction by exact inner
    products. It is valid for signed rational sums of even hinges.
    """
    a, hinges, modes = _radius(a), tuple(hinges), _modes(modes)
    basis = tuple(poly.legendre_polynomial(n, a) for n in modes)
    norms = tuple(2*a/Q(2*n+1) for n in modes)
    basis_pw = tuple(polynomial_on_interval(p, a) for p in basis)
    basis_d = tuple(p.weak_derivative() for p in basis_pw)
    images = tuple(hinge_sum_response(a, p, hinges) for p in basis)
    high_images = tuple(f.add(project_legendre(f, modes), -1) for f in images)
    images_d = tuple(f.weak_derivative() for f in images)
    raw = sum((hinge_hs_inner(a, h, k, derivative=True) for h in hinges for k in hinges), Q())
    input_high = raw - sum((f.inner(f)/n for f, n in zip(images_d, norms)), Q())
    high_d = tuple(f.add(project_legendre(f, modes), -1) for f in images_d)
    after_derivative = input_high - sum((f.inner(f)/n for f, n in zip(high_d, norms)), Q())
    cross = -sum((s.inner(hinge_sum_response(a, poly.poly_derivative(p), hinges).weak_derivative())/n
                  for s, p, n in zip(high_images, basis, norms)), Q())
    correction = sum((basis_d[i].inner(basis_d[j])*high_images[i].inner(high_images[j])/(norms[i]*norms[j])
                      for i in range(len(modes)) for j in range(len(modes))), Q())
    before_derivative = input_high - 2*cross + correction
    if not 0 <= after_derivative <= input_high <= raw or before_derivative < 0:
        raise ArithmeticError("HS identity or legal projection contraction failed")
    return {"raw_D_T_HS_squared": raw, "D_T_Q_HS_squared": input_high,
            "Q_D_T_Q_HS_squared": after_derivative,
            "D_Q_T_Q_HS_squared": before_derivative,
            "output_projection_before_derivative_contracts_this_instance": before_derivative <= raw}


@dataclass(frozen=True)
class DistributionSecondDerivative:
    """Regular part plus (location, delta coefficient, delta-prime coefficient)."""
    regular: PiecewisePolynomial
    atoms: tuple[tuple[Q, Q, Q], ...]

    def pair_polynomial(self, test):
        test = _polynomial(test)
        derivative = poly.poly_derivative(test)
        regular = sum((poly.poly_integral(poly.poly_mul(p, test), l, r)
                       for p, l, r in zip(self.regular.pieces, self.regular.breaks,
                                          self.regular.breaks[1:])), Q())
        return regular + sum((d*poly.poly_eval(test, x)-dp*poly.poly_eval(derivative, x)
                              for x, d, dp in self.atoms), Q())


def zero_extension_second_derivative(function):
    """Distribution D² of the zero extension, retaining all boundary/jump terms."""
    derivatives = tuple(poly.poly_derivative(p) for p in function.pieces)
    regular = PiecewisePolynomial(function.breaks, tuple(poly.poly_derivative(p) for p in derivatives))
    atoms = []
    for i, x in enumerate(function.breaks):
        left = function.pieces[i-1] if i else (Q(),)
        right = function.pieces[i] if i < len(function.pieces) else (Q(),)
        jump = poly.poly_eval(right, x)-poly.poly_eval(left, x)
        slope_jump = poly.poly_eval(poly.poly_derivative(right), x)-poly.poly_eval(poly.poly_derivative(left), x)
        if jump or slope_jump:
            atoms.append((x, slope_jump, jump))
    return DistributionSecondDerivative(regular, tuple(atoms))


def clipped_hinge(window, hinge):
    """h_b on [-window,window]; zero-extension derivatives retain endpoints."""
    window = _radius(window)
    if not isinstance(hinge, Hinge):
        raise WavefrontGeometryError("Hinge required")
    b, c = hinge.threshold, hinge.weight
    breaks = tuple(sorted({-window, window} | {v for v in (-b, b) if -window < v < window}))
    pieces = []
    for l, r in zip(breaks, breaks[1:]):
        midpoint = (l+r)/2
        pieces.append((-c*b, -c) if midpoint < -b else
                      (-c*b, c) if midpoint > b else (Q(),))
    return PiecewisePolynomial(breaks, tuple(pieces))


def source_prime_geometry(a, *, tape=None, half_density=Q(1, 2), clock_scale=Q(1)):
    """Pinned source law + interval HS geometry for each active genuine atom.

    The complete bounded tape is checked even if a fake place is outside I-I.
    Parameter mutations are rejected rather than silently corrected. Returned
    HS squares are for individual raw prime kernels, not their sum or full G.
    """
    a = _radius(a)
    source = poly._pinned_source()
    if a > 1:
        raise WavefrontGeometryError("pinned source adapter supports only a<=1")
    if _q(half_density) != Q(1, 2) or _q(clock_scale) != 1:
        raise WavefrontGeometryError("wrong source half-density or logarithmic clock")
    tape = source.AUTHENTIC_TAPE if tape is None else tuple(tape)
    if any(not isinstance(atom, (tuple, list)) or len(atom) != 2
           or any(type(v) is not int for v in atom) for atom in tape):
        raise WavefrontGeometryError("source tape entries require exact integer pairs")
    source.assert_original_source_tape(tape)
    atoms = []
    for n, p in source.authenticated_prime_wavefront(a):
        if source.real_prime_power(n) != p:
            raise WavefrontGeometryError("non-prime-power source atom")
        b = source.log_iv(n)
        c = source.log_iv(p)*source.sqrt_inverse(n)
        delta = source.I(max(Q(), 2*a-b.hi), max(Q(), 2*a-b.lo))
        d2 = delta*delta
        c2 = c*c
        atoms.append({"n": n, "prime": p, "threshold": b, "weight": c,
                      "raw_HS_squared": c2*d2*d2/6,
                      "raw_derivative_HS_squared": c2*d2})
    return {"source_blob": poly.PARENT_SOURCE_BLOB, "radius": a, "atoms": tuple(atoms),
            "scope": "individual raw prime hinges only",
            "full_signed_source_included": False, "RH_proved": False}


def source_prime_matrix(a, test_modes, input_modes, **source_contract):
    """Prime-only exact outward intervals, using existing correlation kernels.

    P_n(x/a), n>=1, are unnormalized; entries are forms, not coordinates of
    the operator in an orthonormal basis. No uncertain threshold is rounded.
    """
    geometry = source_prime_geometry(a, **source_contract)
    source = poly._pinned_source()
    test_modes, input_modes = _modes(test_modes), _modes(input_modes)
    if any(not 1 <= n <= 30 for n in test_modes + input_modes):
        raise WavefrontGeometryError("source correlation supports modes 1..30")
    def entry(i, j):
        polynomial = poly.prime_hinge_integral_polynomial(i, j, geometry["radius"])
        result = source.iv(0)
        for atom in geometry["atoms"]:
            result += atom["weight"]*poly.polynomial_interval(polynomial, atom["threshold"])
        return result
    return tuple(tuple(entry(i, j) for j in input_modes) for i in test_modes)


def source_first_prime_projection_bound(*, modes=(1, 2, 3, 4), epsilon=Q(1, 100)):
    """Certified bound for D Q G2 Q at a=1/2, G2=P0_perp T_log2 P0_perp.

    A rational reference hinge is transferred to the true log2 by an explicit
    HS perturbation bound. It is not identified with the source threshold.
    This can establish an INSTANCE-specific contraction; no full-source or
    universal derivative/output-projection contraction is assumed.
    """
    epsilon = _q(epsilon)
    if epsilon <= 0:
        raise WavefrontGeometryError("positive Young parameter required")
    modes = _modes(modes)
    source = poly._pinned_source()
    a = Q(1, 2)
    atom, = source_prime_geometry(a)["atoms"]
    b, c = atom["threshold"], atom["weight"]
    if not a < b.lo <= b.hi < 2*a:
        raise WavefrontGeometryError("disjoint first-prime strips not enclosed")
    reference = Q(b.lo.numerator*10**6//b.lo.denominator, 10**6)
    threshold_error = max(abs(b.lo-reference), abs(b.hi-reference))
    removed = tuple(sorted(set((0,) + modes)))
    proxy = projection_hs_audit(a, (Hinge(reference),), removed)
    # ||DP||op² <= ||DP||HS² = sum ||L_n'||² / ||L_n||².
    derivative_projection_bound = sum((Q(n*(n+1)*(2*n+1))/(2*a*a) for n in removed), Q())
    length = 2*a
    # ||D(T_b-T_ref)||HS² <= 2 L eta; ||T_b-T_ref||HS² <= L² eta².
    # D Q E Q = D E Q - DP E Q, hence the following squared bound.
    error_squared = 4*length*threshold_error + 2*derivative_projection_bound*length**2*threshold_error**2
    unweighted_upper = ((1+epsilon)*proxy["D_Q_T_Q_HS_squared"]
                        + (1+1/epsilon)*error_squared)
    c2 = c*c
    upper = (c2*unweighted_upper).hi
    delta = source.I(length-b.hi, length-b.lo)
    # DT1 has disjoint linear strips: ||DT1||²=2 delta³/3.
    raw_mean_zero = c2*(delta*delta-Q(2, 3)/length*delta*delta*delta)
    return {"source_blob": poly.PARENT_SOURCE_BLOB,
            "source": "true prime 2 only, mean-zero carrier, a=1/2",
            "removed_modes_including_constant": removed,
            "source_threshold_interval": b, "source_weight_interval": c,
            "rational_reference_threshold": reference,
            "threshold_error_upper": threshold_error,
            "unweighted_reference_audit": proxy,
            "DP_operator_squared_upper": derivative_projection_bound,
            "unweighted_derivative_perturbation_squared_upper": error_squared,
            "epsilon": epsilon,
            "D_G2_HS_squared_interval": raw_mean_zero,
            "D_Q_G2_Q_HS_squared_upper": upper,
            "strict_contraction_certified_this_prime_only": upper < raw_mean_zero.lo,
            "full_signed_source_included": False,
            "universal_output_projection_contraction": False}
