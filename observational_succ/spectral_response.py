"""Exact finite spectral-response models, never an arithmetic source adapter.

See research/2026-10-16/SPECTRAL_RESPONSE_MEASURE.md for infinite-dimensional
domains and conditional paper proofs. Atoms are rational PSD matrix weights;
from_diagonal accepts a rational nonnegative D and rational rows of b. No
eigenvalue computation, floating certification, or infinite range inference.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import comb

from .recursive_operator_gluing import psd


class SpectralResponseError(ValueError):
    """An exactness, positivity, range, shape, or resource gate failed."""


def _q(value):
    if type(value) not in (int, F):
        raise SpectralResponseError("exact int/Fraction required; no bool/float")
    return F(value)


def _integer(value, lower, upper):
    if type(value) is not int or not lower <= value <= upper:
        raise SpectralResponseError(f"integer budget {lower}..{upper} required")
    return value


def _positive(value):
    value = _q(value)
    if value <= 0:
        raise SpectralResponseError("strictly positive parameter required")
    return value


def _matrix(rows):
    if not isinstance(rows, (tuple, list)) or not 1 <= len(rows) <= 8:
        raise SpectralResponseError("matrix dimension budget 1..8")
    n = len(rows)
    if any(not isinstance(row, (tuple, list)) or len(row) != n for row in rows):
        raise SpectralResponseError("square matrix required")
    out = tuple(tuple(_q(x) for x in row) for row in rows)
    if any(out[i][j] != out[j][i] for i in range(n) for j in range(n)):
        raise SpectralResponseError("symmetric matrix required")
    if not psd(out):
        raise SpectralResponseError("PSD weight required; signs are not repaired")
    return out


def _scale(a, s):
    return tuple(tuple(s*x for x in row) for row in a)


def _subtract(a, b):
    return tuple(tuple(x-y for x, y in zip(r, s)) for r, s in zip(a, b))


def _root(n, degree):
    lo, hi = 0, 1 << ((n.bit_length()+degree-1)//degree)
    while lo <= hi:
        mid = (lo+hi)//2
        power = mid**degree
        if power == n:
            return mid
        if power < n:
            lo = mid+1
        else:
            hi = mid-1
    raise SpectralResponseError("power is not rational; no float substituted")


def rational_power(base, exponent):
    """Exact rational powers only; reject irrational outputs, rather than round."""
    base, exponent = _positive(base), _q(exponent)
    if exponent.denominator > 32 or abs(exponent) > 32:
        raise SpectralResponseError("power budget: denominator and magnitude <=32")
    root = F(_root(base.numerator, exponent.denominator),
             _root(base.denominator, exponent.denominator))
    return root**exponent.numerator


def scalar_filter_maximum(alpha, shift, support, order=1):
    """sup_[0,T] t^alpha (lambda/(t+lambda))^order, alpha>0.

    order=1 controls response bias, order=2 original trial energy excess.
    Fractional constants are returned only when exactly rational.
    """
    alpha, shift, support = _positive(alpha), _positive(shift), _positive(support)
    _integer(order, 1, 2)
    peak = support if alpha >= order else min(support, alpha*shift/(order-alpha))
    return rational_power(peak, alpha)*(shift/(peak+shift))**order


@dataclass(frozen=True)
class SpectralMeasure:
    """Finite real matrix measure Sigma, with 1..128 atoms and low size <=8.

    Repeated eigenvalues are retained as separate provenance rows; all
    cumulative operations sum them. Zero eigenvalues are accepted and their
    coupling is checked, never silently pseudoinverted. This is a declared
    model, with no source-authentication flag.
    """

    atoms: tuple

    def __post_init__(self):
        if not isinstance(self.atoms, (tuple, list)) or not 1 <= len(self.atoms) <= 128:
            raise SpectralResponseError("atom budget 1..128")
        clean = []
        for atom in self.atoms:
            if not isinstance(atom, (tuple, list)) or len(atom) != 2:
                raise SpectralResponseError("atom must be (eigenvalue, PSD weight)")
            t, weight = _q(atom[0]), _matrix(atom[1])
            if t < 0:
                raise SpectralResponseError("D must be nonnegative")
            if clean and len(weight) != len(clean[0][1]):
                raise SpectralResponseError("inconsistent low dimensions")
            clean.append((t, weight))
        object.__setattr__(self, "atoms", tuple(sorted(clean, key=lambda a: a[0])))

    @classmethod
    def from_diagonal(cls, eigenvalues, coupling_rows):
        """Sigma({d_j}) += b_j^T b_j, Euclidean metric; b: low -> high."""
        if (not isinstance(eigenvalues, (tuple, list))
                or not isinstance(coupling_rows, (tuple, list))
                or len(eigenvalues) != len(coupling_rows)
                or not 1 <= len(eigenvalues) <= 128):
            raise SpectralResponseError("aligned diagonal and coupling rows required")
        rows = []
        for row in coupling_rows:
            if not isinstance(row, (tuple, list)) or not 1 <= len(row) <= 8:
                raise SpectralResponseError("low dimension budget 1..8")
            rows.append(tuple(_q(x) for x in row))
        if any(len(row) != len(rows[0]) for row in rows):
            raise SpectralResponseError("ragged coupling")
        return cls(tuple((d, tuple(tuple(x*y for y in row) for x in row))
                         for d, row in zip(eigenvalues, rows)))

    @property
    def dimension(self):
        return len(self.atoms[0][1])

    def _sum(self, multiplier):
        out = [[F() for _ in range(self.dimension)] for _ in range(self.dimension)]
        for t, w in self.atoms:
            f = multiplier(t)
            for i in range(self.dimension):
                for j in range(self.dimension):
                    out[i][j] += f*w[i][j]
        return tuple(tuple(row) for row in out)

    def zero_mass(self):
        return self._sum(lambda t: F(int(t == 0)))

    def _range_gate(self):
        if any(x for row in self.zero_mass() for x in row):
            raise SpectralResponseError("nonzero kernel coupling: zero response is not finite")

    def weak_mass(self, cutoff):
        """F(epsilon)=Sigma((0,epsilon]); the zero atom is reported separately."""
        cutoff = _positive(cutoff)
        return self._sum(lambda t: F(int(0 < t <= cutoff)))

    def moment(self, order):
        _integer(order, 0, 32)
        return self._sum(lambda t: t**order)

    def response(self, shift=0):
        """R_lambda=integral (t+lambda)^-1 dSigma; range-gated at zero."""
        shift = _q(shift)
        if shift < 0:
            raise SpectralResponseError("nonnegative shift required")
        if shift == 0:
            self._range_gate()
        return self._sum(lambda t: 1/(t+shift) if t+shift else F())

    def inverse_tail(self, cutoff):
        cutoff = _positive(cutoff)
        self._range_gate()
        return self._sum(lambda t: 1/t if 0 < t <= cutoff else F())

    def shift_gap(self, shift):
        shift = _positive(shift)
        self._range_gate()
        return self._sum(lambda t: shift/(t*(t+shift)) if t else F())

    def completion_gap(self, shift):
        """R0-L_U for U=(D+lambda)^-1 b, not R0-R_lambda."""
        shift = _positive(shift)
        self._range_gate()
        return self._sum(lambda t: shift**2/(t*(t+shift)**2) if t else F())

    def stieltjes_tail_parts(self, cutoff):
        """Exact F(eps)/eps and integral_0^eps F(t)/t^2 dt, atoms <=eps."""
        cutoff = _positive(cutoff)
        self._range_gate()
        return (_scale(self.weak_mass(cutoff), 1/cutoff),
                self._sum(lambda t: 1/t-1/cutoff if 0 < t <= cutoff else F()))

    def fractional_range_gram(self, alpha):
        """V*V=integral t^(-1-alpha)dSigma for this FINITE model only."""
        alpha = _positive(alpha)
        self._range_gate()
        return self._sum(lambda t: rational_power(t, -1-alpha) if t else F())

    def fractional_bounds(self, alpha, shift, cutoff):
        alpha, shift, cutoff = _positive(alpha), _positive(shift), _positive(cutoff)
        gram = self.fractional_range_gram(alpha)
        support = max(t for t, _ in self.atoms)
        if support == 0:
            return {"range_gram": gram, "tail_upper": gram,
                    "shift_upper": gram, "completion_upper": gram}
        return {"range_gram": gram,
                "tail_upper": _scale(gram, rational_power(min(cutoff, support), alpha)),
                "shift_upper": _scale(gram, scalar_filter_maximum(alpha, shift, support)),
                "completion_upper": _scale(gram, scalar_filter_maximum(alpha, shift, support, 2))}

    def weak_mass_bound(self, alpha, ceiling, cutoff):
        """Verify F(t)<=t^(1+alpha) M for EVERY 0<t<=eps in a finite model.

        Between atoms the left side is constant and the right is increasing;
        checking jumps suffices. Return (1+alpha)/alpha eps^alpha M.
        Arbitrary infinite-source weak-mass hypotheses are not certified here.
        """
        alpha, cutoff, ceiling = _positive(alpha), _positive(cutoff), _matrix(ceiling)
        if len(ceiling) != self.dimension:
            raise SpectralResponseError("ceiling dimension mismatch")
        self._range_gate()
        for t in sorted({t for t, _ in self.atoms if 0 < t <= cutoff}):
            rhs = _scale(ceiling, rational_power(t, 1+alpha))
            if not psd(_subtract(rhs, self.weak_mass(t))):
                raise SpectralResponseError("weak-mass hypothesis fails at a jump")
        return _scale(ceiling, (1+alpha)/alpha*rational_power(cutoff, alpha))


def slow_tail_prefix(terms):
    """Rational prefix of d_j=4^-j, b_j=2^-j/j; not an infinite certificate."""
    _integer(terms, 1, 128)
    return SpectralMeasure.from_diagonal(
        tuple(F(1, 4**j) for j in range(1, terms+1)),
        tuple((F(1, 2**j*j),) for j in range(1, terms+1)))


def slow_tail_enclosure(terms, shift):
    """Infinite sum bounds via the integral test, not floating extrapolation.

    Sum_{j>N} 1/j^2 in [1/(N+1),1/N]. Filters increase as d_j decreases.
    """
    _integer(terms, 1, 128)
    shift = _positive(shift)
    model = slow_tail_prefix(terms)
    tail_lo, tail_hi = F(1, terms+1), F(1, terms)
    first = F(1, 4**(terms+1))
    factor = shift/(first+shift)
    r, gap, trial = (model.response()[0][0], model.shift_gap(shift)[0][0],
                     model.completion_gap(shift)[0][0])
    return {"terms": terms, "shift": shift, "response": (r+tail_lo, r+tail_hi),
            "shift_gap": (gap+factor*tail_lo, gap+tail_hi),
            "completion_gap": (trial+factor**2*tail_lo, trial+tail_hi),
            "omitted_inverse_mass": (tail_lo, tail_hi)}


def matched_moment_measures(order, epsilon):
    """Same fixed moments 0..m, positive rational weights, unbounded inverse.

    Nodes x_i=i/(m+1), base weights 2*C(m+1,i); move unit mass to eps
    using exact Lagrange evaluation weights. Base is independent of eps.
    Scalar measure weights need not be squares of rational couplings.
    """
    _integer(order, 0, 16)
    epsilon = _positive(epsilon)
    n = order+1
    if epsilon >= F(1, n):
        raise SpectralResponseError("epsilon must be below the first fixed node")
    nodes = tuple(F(i, n) for i in range(1, n+1))
    base, perturbed = [], [(epsilon, ((F(1),),))]
    for i, x in enumerate(nodes, 1):
        lagrange = F(1)
        for y in nodes:
            if y != x:
                lagrange *= (epsilon-y)/(x-y)
        weight = F(2*comb(n, i))
        base.append((x, ((weight,),)))
        perturbed.append((x, ((weight-lagrange,),)))
    return SpectralMeasure(tuple(base)), SpectralMeasure(tuple(perturbed))


def tiny_coupling_counterexample(index):
    """One visible atom of fixed infinite D=diag(4^-j), b=2^-n e_n."""
    _integer(index, 1, 1024)
    amplitude = F(1, 2**index)
    d = amplitude**2
    model = SpectralMeasure.from_diagonal((d,), ((amplitude,),))
    high_witness = -1/amplitude
    return {"index": index, "operator_perturbation_norm": amplitude,
            "d": d, "b": amplitude, "A": F(1, 2),
            "R0": model.response()[0][0], "S0": F(1, 2)-model.response()[0][0],
            "limit_R0": F(), "limit_S0": F(1, 2),
            "high_witness": high_witness,
            "original_energy": F(1, 2)+2*amplitude*high_witness+d*high_witness**2,
            "response_at_shift_one": model.response(1)[0][0]}
