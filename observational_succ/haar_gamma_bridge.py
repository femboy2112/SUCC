"""Exact finite Haar/Gamma interfaces and original Oily-source enclosures.

The finite transition model is a declared symmetric Markov generator, not an
inferred BBP phase dynamics. The separate Oily functions retain the literal
four-channel source. All certificates use Fractions; no physical energy,
entanglement, infinite empirical verification, or pi normality is inferred.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache

Matrix = tuple[tuple[F, ...], ...]
MAX_SIZE = 16
MAX_DEPTH = 16
MAX_HAAR_LEVEL = 7
MAX_SOURCE_POWER = 8
MAX_TERMS = 64


def _q(x, name="value") -> F:
    if type(x) not in (int, F):
        raise ValueError(f"{name} must be an exact integer or Fraction")
    return F(x)


def _nat(x, name, maximum, minimum=0):
    if type(x) is not int or not minimum <= x <= maximum:
        raise ValueError(f"{name} must be an integer in [{minimum},{maximum}]")
    return x


def _size(n):
    _nat(n, "size", MAX_SIZE, 1)
    if n & (n - 1):
        raise ValueError("size must be a power of two")
    return n


def _matrix(a) -> Matrix:
    if not isinstance(a, (tuple, list)) or not a:
        raise ValueError("nonempty square matrix required")
    n = _size(len(a))
    if any(not isinstance(row, (tuple, list)) or len(row) != n for row in a):
        raise ValueError("square matrix required")
    return tuple(tuple(_q(x, "entry") for x in row) for row in a)


def _eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def _add(a, b, sign=1):
    return tuple(tuple(x + sign*y for x, y in zip(r, s)) for r, s in zip(a, b))


def _mul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(a))), F())
                       for j in range(len(a))) for i in range(len(a)))


def _transpose(a):
    return tuple(zip(*a))


def _inverse(a):
    n = len(a)
    rows = [list(row) + list(unit) for row, unit in zip(a, _eye(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        value = rows[j][j]
        rows[j] = [x/value for x in rows[j]]
        for i in range(n):
            if i != j:
                value = rows[i][j]
                rows[i] = [x-value*y for x, y in zip(rows[i], rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


def _generator(a):
    a = _matrix(a)
    if any(sum(row, F()) != 0 for row in a):
        raise ValueError("generator rows must sum to zero")
    if a != _transpose(a):
        raise ValueError("uniform reversible model requires a symmetric generator")
    if any(a[i][j] < 0 for i in range(len(a)) for j in range(len(a)) if i != j):
        raise ValueError("off-diagonal jump rates must be nonnegative")
    return a


def haar_projection(size: int, level: int) -> Matrix:
    """Uniform conditional expectation onto 2**level consecutive cells."""
    n = _size(size)
    _nat(level, "level", n.bit_length()-1)
    block = n // 2**level
    return tuple(tuple(F(1, block) if i//block == j//block else F()
                       for j in range(n)) for i in range(n))


def gamma_transition(generator, depth: int, rate=F(1)) -> Matrix:
    """E exp(T L), T~Gamma(integer depth,rate); depth zero is identity.

    Positive depth uses (rate*(rate*I-L)^-1)^depth exactly. Symmetry is an
    explicit scope restriction; nonreversible sources are outside this
    positive-Gram certificate, though their Gamma resolvent law still holds.
    """
    a = _generator(generator)
    _nat(depth, "depth", MAX_DEPTH)
    rate = _q(rate, "rate")
    if rate <= 0:
        raise ValueError("rate must be positive")
    unit = _eye(len(a))
    resolvent = _inverse(tuple(tuple(rate*unit[i][j]-a[i][j]
                                    for j in range(len(a))) for i in range(len(a))))
    step = tuple(tuple(rate*x for x in row) for row in resolvent)
    result = unit
    for _ in range(depth):
        result = _mul(result, step)
    return result


@dataclass(frozen=True)
class GammaHaarCertificate:
    transition: Matrix
    projection: Matrix
    compression: Matrix
    leakage: Matrix
    defect: Matrix
    hidden_grams: tuple[Matrix, ...]
    trace_energy: F


def gamma_haar_certificate(generator, depth: int, level: int, rate=F(1)):
    """Equal-depth compression defect = sum of hidden Haar Gram operators.

    The finite implementation supports depth<=8 because the independent
    full transition has depth 2*depth. At depth=0 all leakage is zero and no
    invariant-subspace inference is licensed.
    """
    _nat(depth, "depth", MAX_DEPTH//2)
    g = gamma_transition(generator, depth, rate)
    n = len(g)
    p = haar_projection(n, level)
    q = _add(_eye(n), p, -1)
    compression = _mul(_mul(p, g), p)
    leakage = _mul(_mul(q, g), p)
    full = gamma_transition(generator, 2*depth, rate)
    defect = _add(_mul(_mul(p, full), p), _mul(compression, compression), -1)
    grams = []
    for j in range(level, n.bit_length()-1):
        detail = _add(haar_projection(n, j+1), haar_projection(n, j), -1)
        h = _mul(_mul(detail, g), p)
        grams.append(_mul(_transpose(h), h))
    total = tuple(tuple(F() for _ in range(n)) for _ in range(n))
    for gram in grams:
        total = _add(total, gram)
    if defect != total or defect != _mul(_transpose(leakage), leakage):
        raise ArithmeticError("Haar/Gamma coherence identity failed")
    return GammaHaarCertificate(g, p, compression, leakage, defect,
                               tuple(grams), sum((defect[i][i] for i in range(n)), F()))


@dataclass(frozen=True)
class RationalInterval:
    lower: F
    upper: F

    def __post_init__(self):
        lower, upper = _q(self.lower), _q(self.upper)
        if lower > upper:
            raise ValueError("reversed interval")
        object.__setattr__(self, "lower", lower)
        object.__setattr__(self, "upper", upper)

    @property
    def width(self):
        return self.upper-self.lower

    def contains(self, value):
        return self.lower <= _q(value) <= self.upper


def _cell(left, right):
    left, right = _q(left, "left"), _q(right, "right")
    if not 0 <= left < right <= 1:
        raise ValueError("source interval must satisfy 0<=left<right<=1")
    return left, right


def source_mass_interval(left=F(0), right=F(1), *, terms=16):
    """Certified integral of literal R=(4-2x³-x⁴-x⁵)/(16-x⁸).

    The omitted nonnegative geometric tail is at most
    (right-left)*(4/15)*16**(-terms). No pi or quadrature oracle is used.
    """
    left, right = _cell(left, right)
    _nat(terms, "terms", MAX_TERMS, 1)
    partial = F()
    for n in range(terms):
        row = F()
        for power, coefficient in ((0, 4), (3, -2), (4, -1), (5, -1)):
            degree = 8*n + power + 1
            row += coefficient*(right**degree-left**degree)/degree
        partial += row/16**(n+1)
    return RationalInterval(partial, partial+(right-left)*F(4, 15*16**terms))


@lru_cache(maxsize=32)
def _moment_polynomial(power):
    """a**power R = (1-x)*a**(power-1)/4 for power>=1."""
    a = (F(1), F(-1), F(0), F(1, 2), F(-1, 4))
    result = (F(1, 4), F(-1, 4))
    for _ in range(power-1):
        product = [F()]*(len(result)+len(a)-1)
        for i, x in enumerate(result):
            for j, y in enumerate(a):
                product[i+j] += x*y
        result = tuple(product)
    return result


def source_power_moment(left, right, power: int):
    """Exact unnormalized integral of a(x)**power R(x), power>=1."""
    left, right = _cell(left, right)
    _nat(power, "power", 2*MAX_SOURCE_POWER, 1)
    return sum((c*(right**(j+1)-left**(j+1))/(j+1)
                for j, c in enumerate(_moment_polynomial(power))), F())


def source_haar_level_energy(level: int, *, power=1, terms=16):
    """Certified weighted Haar energy at one level, for f=a**power.

    Haar weights are the authentic source masses mu=R dx/integral R;
    uniform bin weights would be a different observer.
    """
    _nat(level, "level", MAX_HAAR_LEVEL)
    _nat(power, "power", MAX_SOURCE_POWER, 1)
    total = source_mass_interval(terms=terms)
    low = high = F()
    for j in range(2**level):
        left, middle, right = F(j, 2**level), F(2*j+1, 2**(level+1)), F(j+1, 2**level)
        l = source_mass_interval(left, middle, terms=terms)
        r = source_mass_interval(middle, right, terms=terms)
        al = source_power_moment(left, middle, power)
        ar = source_power_moment(middle, right, power)
        # Strictly decreasing a**power proves this signed numerator positive.
        dl, du = max(F(), al*r.lower-ar*l.upper), al*r.upper-ar*l.lower
        denominator_lower = total.lower*(l.lower+r.lower)*l.lower*r.lower
        denominator_upper = total.upper*(l.upper+r.upper)*l.upper*r.upper
        low += dl*dl/denominator_upper
        high += du*du/denominator_lower
    return RationalInterval(low, high)


def source_residual_variance(level: int, *, power=1, terms=16):
    """Certified remaining conditional variance after level refinements."""
    _nat(level, "level", MAX_HAAR_LEVEL)
    _nat(power, "power", MAX_SOURCE_POWER, 1)
    total = source_mass_interval(terms=terms)
    low = high = F()
    for j in range(2**level):
        left, right = F(j, 2**level), F(j+1, 2**level)
        mass = source_mass_interval(left, right, terms=terms)
        first = source_power_moment(left, right, power)
        second = source_power_moment(left, right, 2*power)
        low += max(F(), second-first*first/mass.lower)
        high += max(F(), second-first*first/mass.upper)
    # |(a**power)'|<=power on [0,1]; conditional range-variance bound.
    bound = F(power*power, 4*4**level)
    return RationalInterval(low/total.upper, min(high/total.lower, bound))


@dataclass(frozen=True)
class SourceHaarCertificate:
    power: int
    terms: int
    source_mass: RationalInterval
    total_variance: RationalInterval
    level_energies: tuple[RationalInterval, ...]
    residual_variance: RationalInterval
    analytic_residual_bound: F


def source_haar_certificate(levels: int, *, power=1, terms=16):
    """Finite certified Haar decomposition of the original depth covariance."""
    _nat(levels, "levels", MAX_HAAR_LEVEL)
    _nat(power, "power", MAX_SOURCE_POWER, 1)
    return SourceHaarCertificate(
        power, terms, source_mass_interval(terms=terms),
        source_residual_variance(0, power=power, terms=terms),
        tuple(source_haar_level_energy(j, power=power, terms=terms) for j in range(levels)),
        source_residual_variance(levels, power=power, terms=terms),
        F(power*power, 4*4**levels))
