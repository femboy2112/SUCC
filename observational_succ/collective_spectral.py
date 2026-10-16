"""Exact signed polarization, typed enclosures, and spectral witness budgets.

Standard library only. Analytic premises are proved/audited in
research/2026-10-16/COLLECTIVE_SPECTRAL_OBSERVERS.md. Typed metadata is not
source authentication; the separate probe verifies and executes pinned PR137.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, isqrt


class SpectralError(ValueError):
    pass


def rational(value):
    if type(value) not in (int, F):
        raise SpectralError('exact int/Fraction required; floats and bools rejected')
    return F(value)


def positive_integer(value):
    if type(value) is not int or value < 1:
        raise SpectralError('positive integer required')
    return value


@dataclass(frozen=True)
class Gaussian:
    real: F = F()
    imag: F = F()

    def __post_init__(self):
        object.__setattr__(self, 'real', rational(self.real))
        object.__setattr__(self, 'imag', rational(self.imag))

    def __add__(self, other):
        other = gaussian(other)
        return Gaussian(self.real+other.real, self.imag+other.imag)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self+-gaussian(other)

    def __rsub__(self, other):
        return gaussian(other)+-self

    def __mul__(self, other):
        other = gaussian(other)
        return Gaussian(self.real*other.real-self.imag*other.imag,
                        self.real*other.imag+self.imag*other.real)

    __rmul__ = __mul__

    def conjugate(self):
        return Gaussian(self.real, -self.imag)


def gaussian(value):
    return value if type(value) is Gaussian else Gaussian(rational(value))


def vector(values):
    values = tuple(gaussian(v) for v in values)
    if not values:
        raise SpectralError('nonempty vector required')
    return values


def combine(x, y, coefficient=1):
    x, y = vector(x), vector(y)
    if len(x) != len(y):
        raise SpectralError('vector dimensions differ')
    return tuple(a+gaussian(coefficient)*b for a, b in zip(x, y))


@dataclass(frozen=True)
class HermitianForm:
    """h(x,y)=sum x_i G_ij conjugate(y_j), LINEAR IN THE FIRST argument."""
    entries: tuple

    def __post_init__(self):
        a = tuple(vector(row) for row in self.entries)
        n = len(a)
        if not n or any(len(row) != n for row in a):
            raise SpectralError('nonempty square form required')
        if any(a[i][j] != a[j][i].conjugate() for i in range(n) for j in range(n)):
            raise SpectralError('Hermitian form required')
        object.__setattr__(self, 'entries', a)

    def pairing(self, x, y):
        x, y = vector(x), vector(y)
        if len(x) != len(y) or len(x) != len(self.entries):
            raise SpectralError('form dimension mismatch')
        return sum((x[i]*self.entries[i][j]*y[j].conjugate()
                    for i in range(len(x)) for j in range(len(y))), Gaussian())

    def quadratic(self, x):
        value = self.pairing(x, x)
        if value.imag:
            raise ArithmeticError('Hermitian quadratic is not real')
        return value.real


@dataclass(frozen=True)
class QuadraticApparatus:
    """Finite, explicitly available signed quadratic queries; not a positivity oracle."""
    form: HermitianForm
    allowed: tuple

    def __post_init__(self):
        if type(self.form) is not HermitianForm:
            raise SpectralError('exact form required')
        allowed = tuple(vector(x) for x in self.allowed)
        if any(len(x) != len(self.form.entries) for x in allowed):
            raise SpectralError('apparatus dimension mismatch')
        object.__setattr__(self, 'allowed', allowed)

    def measure(self, x):
        x = vector(x)
        if x not in self.allowed:
            raise SpectralError('required superposition absent from apparatus')
        return self.form.quadratic(x)


def real_polarization(measure, x, y):
    """Recovers Re h; equals h only for a real symmetric form and real vectors."""
    return (rational(measure(combine(x, y)))-rational(measure(combine(x, y, -1))))/4


def complex_polarization(measure, x, y):
    return Gaussian(real_polarization(measure, x, y),
                    (rational(measure(combine(x, y, Gaussian(0, 1))))
                     - rational(measure(combine(x, y, Gaussian(0, -1)))))/4)


@dataclass(frozen=True)
class Interval:
    lower: F
    upper: F

    def __post_init__(self):
        lo, hi = rational(self.lower), rational(self.upper)
        if lo > hi:
            raise SpectralError('reversed interval')
        object.__setattr__(self, 'lower', lo)
        object.__setattr__(self, 'upper', hi)

    def scale(self, c):
        a, b = rational(c)*self.lower, rational(c)*self.upper
        return Interval(min(a, b), max(a, b))

    def __add__(self, other):
        if type(other) is not Interval:
            raise SpectralError('interval required')
        return Interval(self.lower+other.lower, self.upper+other.upper)

    def absolute_lower(self):
        return max(F(), self.lower, -self.upper)


@dataclass(frozen=True)
class Coordinates:
    """All mathematical identities that must agree BEFORE interval intersection."""
    source_blob: str
    source_commit: str
    radius: F
    basis: tuple[str, ...]
    channels: tuple[str, ...]
    metric_diagonal: tuple[F, ...]
    target: str
    convention: str = 'linear-first'

    def __post_init__(self):
        if any(type(s) is not str or not s for s in
               (self.source_blob, self.source_commit, self.target, self.convention)):
            raise SpectralError('nonempty source and target identity required')
        r = rational(self.radius)
        metric = tuple(rational(x) for x in self.metric_diagonal)
        if r <= 0 or not metric or any(x <= 0 for x in metric):
            raise SpectralError('positive radius and coordinate metric required')
        for labels in (self.basis, self.channels):
            if type(labels) is not tuple or not labels or any(type(x) is not str or not x for x in labels):
                raise SpectralError('nonempty ordered labels required')
            if len(set(labels)) != len(labels):
                raise SpectralError('duplicate basis/channel label')
        if len(self.basis) != len(metric):
            raise SpectralError('basis/metric mismatch')
        object.__setattr__(self, 'radius', r)
        object.__setattr__(self, 'metric_diagonal', metric)


@dataclass(frozen=True)
class Bound:
    coordinates: Coordinates
    interval: Interval
    route: str
    dependencies: frozenset[str]

    def __post_init__(self):
        if type(self.coordinates) is not Coordinates or type(self.interval) is not Interval:
            raise SpectralError('typed bound required')
        if type(self.route) is not str or not self.route:
            raise SpectralError('named route required')
        if type(self.dependencies) is not frozenset or not self.dependencies or any(
                type(x) is not str or not x for x in self.dependencies):
            raise SpectralError('explicit provenance dependencies required')


def intersect_bounds(bounds):
    """Set intersection, never statistical evidence multiplication or authentication."""
    bounds = tuple(bounds)
    if not bounds or any(type(b) is not Bound for b in bounds):
        raise SpectralError('typed nonempty bound collection required')
    if any(b.coordinates != bounds[0].coordinates for b in bounds):
        raise SpectralError('source/radius/basis/channel/metric/target/convention mismatch')
    if len({b.route for b in bounds}) != len(bounds):
        raise SpectralError('duplicate route identifier')
    lo = max(b.interval.lower for b in bounds)
    hi = min(b.interval.upper for b in bounds)
    if lo > hi:
        raise SpectralError('inconsistent evidence: empty intersection')
    groups = []
    for i, bound in enumerate(bounds):
        connected = [g for g in groups if any(bound.dependencies & bounds[j].dependencies for j in g)]
        merged = {i}.union(*(set(g) for g in connected))
        groups = [g for g in groups if g not in connected]+[sorted(merged)]
    return {'interval': Interval(lo, hi),
            'provenance_components': tuple(tuple(bounds[i].route for i in g) for g in groups),
            'independence_established': False,
            'authority': 'EXACT_INTERSECTION_CONDITIONAL_ON_EACH_INPUT_BOUND'}


def compression_error(degree):
    return F(11, 40*(positive_integer(degree)+1))


def ceil_fraction(q):
    q = rational(q)
    return -(-q.numerator//q.denominator)


def negative_witness_budget(margin, norm_cap=F(11, 40)):
    """Conditional: unit x with <Gx,x><=-margin and CG.2 plus ||G||<=norm_cap.

    Rational grid is in unnormalized Legendre coefficients, real AND imaginary.
    No existence of a negative actual-source direction is asserted.
    """
    delta, m = rational(margin), rational(norm_cap)
    if delta <= 0 or m <= 0 or delta > m:
        raise SpectralError('0 < negative margin <= operator norm cap required')
    n = max(1, ceil_fraction(F(11, 10)/delta)-1)
    e = compression_error(n)
    eta = min(F(1), delta/(16*m))
    # Rounding real and imaginary coefficients to denominator D has L2 error
    # squared <= sum_{j=1}^N [1/(2D^2(2j+1))] <= N/(2D^2).
    denominator = ceil_fraction(F(n)/eta)
    perturbation = m*eta*(2+eta)
    radicand = denominator*denominator*(2*n+1)
    root = isqrt(radicand)
    numerator_bound = root+(root*root < radicand)+1
    grid_side = 2*numerator_bound+1
    return {'degree': n, 'compression_error_upper': e,
            'coefficient_denominator': denominator, 'rounding_L2_error_upper': eta,
            'integer_numerator_absolute_bound': numerator_bound,
            'candidate_count_power': (grid_side, 2*n),
            'candidate_count_log2_strict_upper': 2*n*grid_side.bit_length(),
            'quadratic_rounding_error_upper': perturbation,
            'rational_quadratic_upper': -delta+e+perturbation,
            'certification_error_allowance': delta/4,
            'conditional_on_actual_negative_unit_direction': True,
            'density_rate_assumed': False}


def hidden_soft_mode(depth):
    """Synthetic compact block: fixed short -1/2, first depth modes see +1/2.

    High D_j=4^-j, b=2^-m e_m, m=depth+1. Normalized full negative margin
    of vector (1,-2^m e_m) is 1/[2(1+4^m)], hence collapses with depth.
    """
    depth = positive_integer(depth)
    m = depth+1
    d, b = F(1, 4**m), F(1, 2**m)
    return {'synthetic': True, 'hidden_mode': m, 'D_mm': d, 'b_m': b,
            'visible_short': F(1, 2), 'full_short': -F(1, 2),
            'witness_high_coefficient': -F(2**m),
            'unit_witness_negative_margin': F(1, 2*(1+4**m)),
            'square_root_response_norm_squared': b*b/d}


def sqrt_upper(q, denominator=10**12):
    q = rational(q); positive_integer(denominator)
    if q < 0:
        raise SpectralError('negative radicand')
    n = isqrt(q.numerator*denominator**2//q.denominator)
    return F(n+(F(n*n, denominator**2) < q), denominator)


def legendre_cell_integral(degree, left, right):
    """Exact integrals of P_k(2x), k=0,1,2,3; separate from source polynomial code."""
    if type(degree) is not int or not 0 <= degree <= 3:
        raise SpectralError('projection degree 0..3 required')
    a, b = rational(left), rational(right)
    if not -F(1, 2) <= a < b <= F(1, 2):
        raise SpectralError('cell outside fixed source window')
    coefficients = ((1,), (0, 2), (-F(1, 2), 0, 6), (0, -3, 0, 20))[degree]
    return sum((c*(b**(j+1)-a**(j+1))/(j+1) for j, c in enumerate(coefficients)), F())


def derivative_correlation_polynomial(mode, moment):
    """psi_kj(r)=int [P_k(2(y+r))P_j(2y)-P_j(2(y+r))P_k(2y)]dy.

    Bounds are -1/2<=y<=1/2-r, 0<=r<=1. Then int h_j P_k =
    int_0^1 g'(r) psi_kj(r) dr. This includes moment k=0 and its boundary
    contribution, which a mean-zero-only source pairing API would omit.
    """
    if type(mode) is not int or not 1 <= mode <= 4:
        raise SpectralError('source low mode 1..4 required')
    if type(moment) is not int or not 0 <= moment <= 3:
        raise SpectralError('projection moment 0..3 required')
    polys = ((F(1),), (F(), F(2)), (-F(1, 2), F(), F(6)),
             (F(), -F(3), F(), F(20)), (F(3, 8), F(), -F(15), F(), F(70)))
    out = [F()]*(mode+moment+2)
    for sign, left, right in ((1, polys[moment], polys[mode]),
                               (-1, polys[mode], polys[moment])):
        for p, a in enumerate(left):
            for q, b in enumerate(right):
                for t in range(p+1):
                    # (y+r)^p y^q: r^t times y^(p-t+q).
                    power = p-t+q+1
                    c = sign*a*b*comb(p, t)/power
                    for s in range(power+1):
                        out[t+s] += c*comb(power, s)*F(1, 2)**(power-s)*(-1)**s
                    out[t] -= c*(-F(1, 2))**power
    while len(out) > 1 and not out[-1]:
        out.pop()
    return tuple(out)


def refine_projected_column(column, moment_intervals):
    """Intersect certified exact-integral moments with the cell moment enclosure.

    Input certification remains an external proof obligation. For the actual
    source the probe regenerates these moments from pinned signed channels.
    """
    moments = tuple(moment_intervals)
    if len(moments) != 4 or any(type(z) is not Interval for z in moments):
        raise SpectralError('four exact moment intervals required')
    refined = []
    for coarse, exact in zip(column['projection_moment_intervals'], moments):
        refined.append(Interval(max(coarse[0], exact.lower), min(coarse[1], exact.upper)))
    removed = sum(((2*k+1)*z.absolute_lower()**2 for k, z in enumerate(refined)), F())
    if removed > column['finite_J_energy_upper']:
        raise SpectralError('moment energy contradicts total energy bound')
    return dict(column, projection_moment_intervals=tuple((z.lower, z.upper) for z in refined),
                removed_polynomial_energy_lower=removed,
                projected_energy_upper=column['finite_J_energy_upper']-removed,
                moment_method='EXACT_SIGNED_SOURCE_INTEGRATION_INTERSECTED_WITH_CELL_ENCLOSURE')


def projected_column_bound(mode, samples, grid, lipschitz):
    """Conditional continuum L2 bound from certified positive-half midpoint ranges.

    h has parity (-1)^(mode+1), |h'|<=lipschitz, and the supplied ranges.
    This routine cannot authenticate those analytic/source premises.
    """
    if type(mode) is not int or not 1 <= mode <= 4:
        raise SpectralError('source low mode 1..4 required')
    positive_integer(grid)
    lip = rational(lipschitz)
    if grid % 2 or lip < 0:
        raise SpectralError('even grid and nonnegative Lipschitz bound required')
    samples = tuple(samples)
    if len(samples) != grid//2:
        raise SpectralError('missing cells')
    h = F(1, grid)
    energy = F()
    moments = [Interval(0, 0) for _ in range(4)]
    for i, sample in enumerate(samples):
        if len(sample) != 3:
            raise SpectralError('midpoint, lower, upper required')
        x, lo, hi = map(rational, sample)
        if x != F(2*i+1, 2*grid):
            raise SpectralError('incorrect grid midpoint/order')
        z = Interval(lo, hi)
        m = max(abs(lo), abs(hi))
        energy += 2*h*m*m + m*lip*h*h + lip*lip*h**3/6
        for k in range(4):
            if (mode+1-k) % 2 == 0:
                weight = 2*legendre_cell_integral(k, x-h/2, x+h/2)
                moments[k] = moments[k]+z.scale(weight)
    error = lip/(4*grid)
    for k in range(4):
        if (mode+1-k) % 2 == 0:
            moments[k] = moments[k]+Interval(-error, error)
    removed = sum(((2*k+1)*z.absolute_lower()**2 for k, z in enumerate(moments)), F())
    if removed > energy:
        raise SpectralError('inconsistent analytic/sample premises: removal exceeds energy')
    return {'mode': mode, 'finite_J_energy_upper': energy,
            'projection_moment_intervals': tuple((z.lower, z.upper) for z in moments),
            'moment_quadrature_error_upper': error,
            'removed_polynomial_energy_lower': removed,
            'projected_energy_upper': energy-removed}


def projected_response_caps(columns, derivative_tail, kappa):
    """Source theorem: R0 <= kappa^-1 R_P*R_P; finite-J projection + tail Young."""
    columns = tuple(columns)
    eta, k = rational(derivative_tail), rational(kappa)
    if len(columns) != 4 or tuple(c['mode'] for c in columns) != (1, 2, 3, 4):
        raise SpectralError('four ordered derivative columns required')
    if eta < 0 or k <= 0:
        raise SpectralError('nonnegative tail and positive inherited kappa required')
    answer = {}
    for name, modes in (('odd', (1, 3)), ('even', (2, 4))):
        trace = sum(((2*j+1)*columns[j-1]['projected_energy_upper'] for j in modes), F())
        root = sqrt_upper(trace)
        answer[name] = {'projected_normalized_trace_upper': trace,
                        'trace_sqrt_upper': root, 'derivative_operator_tail': eta,
                        'R0_operator_upper_cap': (root+eta)**2/k}
    return answer
