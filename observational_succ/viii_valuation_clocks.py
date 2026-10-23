"""Exact finite prime-valuation sum cells and CRT box transport.

Classical arithmetic, independently derived for Academic Main VIII.  All
valuation depths are *truncated* at k: depth k means zero modulo p**k,
not the assertion v_p(x) == k.  These utilities supply finite counts, not
proof authority or an automatic infinite-prime independence assumption.
See research/2026-10-21/VIII_VALUATION_CLOCKS.md for proofs and tail bounds.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import comb, isqrt, prod


class ValuationClockError(ValueError):
    """An argument is outside the theorem's exact finite domain."""


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValuationClockError(f"{name} must be an integer >= {minimum}")
    return value


def _prime(p):
    _integer(p, "p", 2)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValuationClockError("p must be a genuine prime")
    return p


def _depth(value, k):
    _integer(value, "depth")
    if value > k:
        raise ValuationClockError("depth exceeds the modulus precision k")
    return value


def truncated_valuation(x, p, k):
    """min(v_p(x), k), with v_p(0)=infinity; x may be negative."""
    _prime(p)
    _integer(k, "k", 1)
    if type(x) is not int:
        raise ValuationClockError("x must be an integer")
    value = x % (p**k)
    result = 0
    while result < k and value % p == 0:
        result += 1
        value //= p
    return result


def unit_sum_count(p, r, phase=0):
    """Number of r-tuples in F_p^* whose sum is phase modulo p.

    The empty tuple (r=0) is included.  This closed integer formula has
    independent character and elementary recurrence proofs.
    """
    _prime(p)
    _integer(r, "r")
    if type(phase) is not int:
        raise ValuationClockError("phase must be an integer")
    correction = (p - 1) if phase % p == 0 else -1
    return ((p - 1) ** r + correction * (-1) ** r) // p


def valuation_class_size(p, k, depth):
    """Number of residues modulo p**k with the given truncated depth."""
    _prime(p)
    _integer(k, "k", 1)
    _depth(depth, k)
    return 1 if depth == k else (p - 1) * p ** (k - depth - 1)


def sum_depth_distribution(p, k, depths):
    """Exact conditional law of v_p(sum x_i), truncated at k.

    The x_i are independent uniform residues in their prescribed valuation
    classes.  Return a tuple of Fractions indexed by total depth 0,...,k.
    Input collections are copied; the returned evidence is immutable.
    """
    _prime(p)
    _integer(k, "k", 1)
    depths = tuple(depths)
    if not depths:
        raise ValuationClockError("at least one summand is required")
    for depth in depths:
        _depth(depth, k)
    h = min(depths)
    law = [Fraction(0)] * (k + 1)
    if h == k:
        law[k] = Fraction(1)
        return tuple(law)
    r = depths.count(h)
    cancel = Fraction(unit_sum_count(p, r), (p - 1) ** r)
    law[h] = 1 - cancel
    for j in range(h + 1, k):
        law[j] = cancel * Fraction(p - 1, p ** (j - h))
    law[k] = cancel / p ** (k - h - 1)
    return tuple(law)


def valuation_sum_count(p, k, depths, total_depth):
    """Number of summand vectors modulo p**k in one valuation sum cell."""
    depths = tuple(depths)
    law = sum_depth_distribution(p, k, depths)
    _depth(total_depth, k)
    size = prod(valuation_class_size(p, k, e) for e in depths)
    result = size * law[total_depth]
    if result.denominator != 1:  # Internal arithmetic invariant, not rounding.
        raise ArithmeticError("valuation cell cardinality was not integral")
    return result.numerator


def sum_residue_count(p, k, depths, total):
    """Number in a valuation cell with sum == total modulo p**k.

    Multiplication of every coordinate by a unit acts transitively on
    residues of fixed truncated depth, so division by that class size is
    exact.  There is no floating-point character evaluation.
    """
    j = truncated_valuation(total, p, k)
    result = Fraction(
        valuation_sum_count(p, k, depths, j), valuation_class_size(p, k, j)
    )
    if result.denominator != 1:
        raise ArithmeticError("sum residue cardinality was not integral")
    return result.numerator


@dataclass(frozen=True)
class PrimeValuationCell:
    """A finite exact condition; not a source-authentication certificate."""

    p: int
    k: int
    depths: tuple
    total_depth: int

    def __post_init__(self):
        object.__setattr__(self, "depths", tuple(self.depths))
        # Validate even an empty or impossible cell at construction time.
        sum_depth_distribution(self.p, self.k, self.depths)
        _depth(self.total_depth, self.k)

    @property
    def cardinality(self):
        return valuation_sum_count(self.p, self.k, self.depths, self.total_depth)


def crt_cell_signature(cells):
    """Return (dimension, modulus, cardinality, density) for distinct primes.

    No explicit enumeration of the combined residue set is necessary.
    Repeated primes are rejected: their constraints are not independent.
    """
    cells = tuple(cells)
    if not cells or any(type(c) is not PrimeValuationCell for c in cells):
        raise ValuationClockError("provide at least one PrimeValuationCell")
    if len({c.p for c in cells}) != len(cells):
        raise ValuationClockError("CRT cells must use distinct genuine primes")
    m = len(cells[0].depths)
    if any(len(c.depths) != m for c in cells):
        raise ValuationClockError("all cells must have the same dimension")
    W = prod(c.p**c.k for c in cells)
    count = prod(c.cardinality for c in cells)
    return m, W, count, Fraction(count, W**m)


def residue_box_enclosure(m, W, count, X):
    """Enclose positive integer points in [1,X]^m in any count residues.

    Return exact (lower, upper, main_term, absolute_error_bound).  For
    X divisible by W this is exact.  Relative error tends uniformly to zero
    when m*W/X -> 0 (nonempty residue set).  Sparse sets cause no hidden
    density-dependent constant.  X is an integer, not a real cutoff.
    """
    _integer(m, "m", 1)
    _integer(W, "W", 1)
    _integer(X, "X")
    _integer(count, "count")
    if count > W**m:
        raise ValuationClockError("count exceeds the entire residue space")
    quotient, remainder = divmod(X, W)
    lower = count * quotient**m
    upper = count * (quotient + bool(remainder)) ** m
    main = count * Fraction(X, W) ** m
    return lower, upper, main, max(main - lower, upper - main)


def local_coprime_density(m, p, *, pairwise=False, include_total=False):
    """Local coprimality density among summands and optionally their total.

    Primitive means not all summands vanish.  Pairwise means at most one
    of the selected coordinates vanishes.  Including the total changes
    pairwise density when m>2; it never changes joint primitivity.
    """
    _integer(m, "m", 2)
    _prime(p)
    if type(pairwise) is not bool or type(include_total) is not bool:
        raise ValuationClockError("pairwise/include_total must be booleans")
    if not pairwise:
        return 1 - Fraction(1, p**m)
    count = (p - 1) ** m + m * (p - 1) ** (m - 1)
    if include_total:
        count -= m * unit_sum_count(p, m - 1)
    return Fraction(count, p**m)


def missed_prime_tail_bound(m, X, P, *, pairwise=False, include_total=False):
    """Absolute box-count error after testing all genuine primes <= P.

    Requires the stated ALL-primes hypothesis in the paper theorem; this
    numeric bound does not authenticate an arbitrary list of primes.
    For joint gcd use X**m/((m-1)*P**(m-1)); for pairwise use the elementary
    union bound [C(m,2)+2m*include_total]*X**m/P.  Any additional residue
    conditions may be imposed: taking a subset only decreases the error.
    """
    _integer(m, "m", 2)
    _integer(X, "X")
    _integer(P, "P", 1)
    if type(pairwise) is not bool or type(include_total) is not bool:
        raise ValuationClockError("pairwise/include_total must be booleans")
    if P >= X:
        return Fraction(0)
    if not pairwise:
        return Fraction(X**m, (m - 1) * P ** (m - 1))
    coefficient = comb(m, 2) + (2 * m if include_total else 0)
    return Fraction(coefficient * X**m, P)
