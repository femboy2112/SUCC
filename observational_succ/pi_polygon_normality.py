"""Exact finite SUCC circle-refinement and normality transport interfaces.

Mathematical boundary: finite rational enclosures and discrepancy witnesses do
NOT establish normality of pi. This module has no pi digits or floating-point
constants as mathematical inputs. Python integers/Fractions are exact.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt


@dataclass(frozen=True)
class PolygonBracket:
    steps: int
    sides: int
    precision_bits: int
    lower: Q
    upper: Q
    chord_sq_lower: Q
    chord_sq_upper: Q


def rational_sqrt_enclosure(value: Q, precision_bits: int = 192) -> tuple[Q, Q]:
    """Outward dyadic bounds on sqrt(value); no machine-float rounding."""
    if value < 0 or not 1 <= precision_bits <= 4096:
        raise ValueError("nonnegative radicand and 1..4096 bits required")
    scale = 1 << precision_bits
    integer = isqrt((value.numerator * scale * scale) // value.denominator)
    lo = Q(integer, scale)
    hi = lo if integer * integer * value.denominator == value.numerator * scale * scale else Q(integer + 1, scale)
    assert lo * lo <= value <= hi * hi
    return lo, hi


def polygon_pi_bracket(steps: int, precision_bits: int = 192) -> PolygonBracket:
    """Rigorous pi enclosure from regular inscribed/circumscribed 4*2**steps-gons.

    For a unit-radius circle, chord-square x_4=2,
      x_(2m) = 2 - sqrt(4-x_m),
      m/2 * sqrt(x_m) < pi < m * sqrt(x_m/(4-x_m)).
    Every sqrt is outward rounded with exact rational bounds. Combining the
    bounds from all previous steps keeps the enclosing interval monotone.
    """
    if not isinstance(steps, int) or not 0 <= steps <= 100:
        raise ValueError("steps must be an integer in [0,100]")
    if not isinstance(precision_bits, int) or not 1 <= precision_bits <= 4096:
        raise ValueError("precision_bits must be in [1,4096]")
    sides, x_lo, x_hi = 4, Q(2), Q(2)
    lower, upper = Q(0), Q(4)
    for i in range(steps + 1):
        if not (Q(0) < x_lo <= x_hi < Q(4)):
            raise ArithmeticError("precision exhausted at polygon refinement step %s" % i)
        candidate_lo = Q(sides, 2) * rational_sqrt_enclosure(x_lo, precision_bits)[0]
        candidate_hi = sides * rational_sqrt_enclosure(x_hi / (4 - x_hi), precision_bits)[1]
        lower, upper = max(lower, candidate_lo), min(upper, candidate_hi)
        if lower >= upper:
            raise ArithmeticError("invalid bracket; insufficient precision")
        if i != steps:
            # f(x)=2-sqrt(4-x) is increasing: enclosure uses opposing sqrt ends.
            x_lo = 2 - rational_sqrt_enclosure(4 - x_lo, precision_bits)[1]
            x_hi = 2 - rational_sqrt_enclosure(4 - x_hi, precision_bits)[0]
            sides *= 2
    return PolygonBracket(steps, sides, precision_bits, lower, upper, x_lo, x_hi)


def certified_fractional_pi_digits(steps: int, base: int = 10, max_digits: int = 20,
                                   precision_bits: int = 192) -> tuple[str, PolygonBracket]:
    """A *certified* common digit prefix; empty if bracket straddles any bin.

    Requires 3<pi<4 to subtract the known integer part. No pi digit oracle.
    """
    if not 2 <= base <= 36 or max_digits < 0 or max_digits > 10000:
        raise ValueError("base 2..36, max_digits 0..10000")
    bracket = polygon_pi_bracket(steps, precision_bits)
    if not (3 < bracket.lower < bracket.upper < 4):
        return "", bracket
    lo, hi = bracket.lower - 3, bracket.upper - 3
    length, encoded = 0, 0
    for k in range(1, max_digits + 1):
        blo = (base**k * lo).numerator // (base**k * lo).denominator
        bhi = (base**k * hi).numerator // (base**k * hi).denominator
        if blo != bhi:
            break
        length, encoded = k, blo
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = []
    for _ in range(length):
        encoded, d = divmod(encoded, base)
        digits.append(alphabet[d])
    return "".join(reversed(digits)), bracket


def uniform_grid_pushforward_counts(start_sides: int, base: int, level: int,
                                     morphism: str) -> tuple[int, ...]:
    """Balanced fibers of two DISTINCT finite maps G_(n+1)->G_n.

    'rotation': T_b(j/M) = (j % (M/b))/(M/b),
    'prefix':    q(j/M) = floor(j/b)/(M/b).
    Both push forward uniform grid measure, but are different maps.
    """
    if start_sides < 3 or base < 2 or not 0 <= level <= 12:
        raise ValueError("invalid grid parameters")
    if morphism not in ("rotation", "prefix"):
        raise ValueError("morphism must be rotation or prefix")
    parent = start_sides * base**level
    counts = [0] * parent
    for j in range(parent * base):
        counts[j % parent if morphism == "rotation" else j // base] += 1
    return tuple(counts)


def polygon_quantize(x: Q, polygon_sides: int) -> Q:
    """Left endpoint of the polygon cell containing x mod 1."""
    if polygon_sides < 3:
        raise ValueError("polygon_sides must be >=3")
    x = x % 1
    y = x * polygon_sides
    return Q(y.numerator // y.denominator, polygon_sides)


def digit_block_total_variation(digits: tuple[int, ...], base: int, k: int) -> Q:
    """Exact finite TV between empirical overlapping k-blocks and b^-k uniform.

    No finite-N numerical test certifies an infinite digit sequence normal.
    """
    if base < 2 or not 1 <= k <= len(digits) or any(not 0 <= d < base for d in digits):
        raise ValueError("invalid digit block")
    sample_size = len(digits) - k + 1
    counts = [0] * base**k
    for i in range(sample_size):
        value = 0
        for d in digits[i:i + k]:
            value = base * value + d
        counts[value] += 1
    return sum((abs(Q(count, sample_size) - Q(1, base**k)) for count in counts), Q(0)) / 2


def orbit_lipschitz_error_bound(base: int, depth: int, source_error: Q,
                                lipschitz_constant: Q = Q(1)) -> Q:
    """Rigorous bound for difference of N-time orbit means of Lipschitz F.

    For d_circle(T_b^j x,T_b^j y)<=b^j |x-y|,
    |average F(T_b^j x)-average F(T_b^j y)| <= L*epsilon*(b^N-1)/(N*(b-1)).
    This bound is generally useless when N grows at fixed finite precision.
    """
    if base < 2 or depth < 1 or source_error < 0 or lipschitz_constant < 0:
        raise ValueError("invalid stability parameters")
    return lipschitz_constant * source_error * Q(base**depth - 1, depth * (base - 1))


def finite_digit_path(word: tuple[int, ...], base: int, n: int) -> tuple[int, ...]:
    """N iterates of the base-b shift of a terminating prefix, as leading digits.

    Returns first digit after each of the first n iterates, by padding zeros;
    for n>len(word), zeros are the eventual periodic tail of the rational path.
    """
    if base < 2 or n < 0 or any(not 0 <= d < base for d in word):
        raise ValueError("invalid path")
    return tuple(word[i] if i < len(word) else 0 for i in range(n))


def polygon_prefix_path(start_sides: int, base: int, initial: int,
                        digits: tuple[int, ...]) -> tuple[int, ...]:
    """A compatible path in the prefix inverse limit of G_(m*b**n).

    Indices obey j_(n+1)=b*j_n+d_(n+1), so P(j_(n+1))=j_n.
    The path-space measure assigns each level-n cylinder mass 1/(m*b**n).
    It does NOT make every path typical for that measure.
    """
    if start_sides < 3 or base < 2 or not 0 <= initial < start_sides:
        raise ValueError("invalid initial polygon label")
    if any(not 0 <= d < base for d in digits):
        raise ValueError("digits must lie in [0,base)")
    indices = [initial]
    for digit in digits:
        indices.append(base * indices[-1] + digit)
    return tuple(indices)


def polygon_cylinder(index: int, start_sides: int, base: int,
                     level: int) -> tuple[Q, Q, Q]:
    """Cell bounds and exact fair-path probability at refinement level.

    The interval is [j/M,(j+1)/M] with mass 1/M where M=m*b**level.
    Closed-endpoint aliases are kept as a separate quotient, not erased.
    """
    if start_sides < 3 or base < 2 or level < 0:
        raise ValueError("invalid cylinder parameters")
    m = start_sides * base**level
    if not 0 <= index < m:
        raise ValueError("invalid cylinder index")
    return Q(index, m), Q(index + 1, m), Q(1, m)
