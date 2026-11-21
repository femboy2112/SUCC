"""Exact base-16 digit/remainder seam and four binary routing stages.

Research-only model: it does NOT derive the source-root parity to pi-digit map.
All arithmetic observations below are mathematical, not physical measurements.
"""
from __future__ import annotations

from fractions import Fraction


def digit_remainder(x: Fraction | int, base: int = 16) -> tuple[int, Fraction]:
    """Return the reflected branch index and transmitted residual for x in [0,1).

    base*x = digit + residue, digit in 0,...,base-1, residue in [0,1).
    """
    if type(base) is not int or base < 2:
        raise ValueError("base must be an integer >= 2")
    x = Fraction(x)
    if not 0 <= x < 1:
        raise ValueError("x must be in [0,1)")
    v = base * x
    digit = v.numerator // v.denominator
    return digit, v - digit


def reverse_branch(digit: int, residue: Fraction | int, base: int = 16) -> Fraction:
    """Exact inverse of the joint digit-plus-through-port report."""
    if type(base) is not int or base < 2:
        raise ValueError("base must be an integer >= 2")
    if type(digit) is not int or not 0 <= digit < base:
        raise ValueError("digit must be an integral branch label")
    residue = Fraction(residue)
    if not 0 <= residue < 1:
        raise ValueError("residue must be in [0,1)")
    return (digit + residue) / base


def four_binary_stages(x: Fraction | int) -> tuple[tuple[int, int, int, int], int, Fraction]:
    """Factor base-16 routing into four successive binary digit/remainder seams."""
    residual = Fraction(x)
    bits = []
    for _ in range(4):
        b, residual = digit_remainder(residual, 2)
        bits.append(b)
    digit = 8*bits[0] + 4*bits[1] + 2*bits[2] + bits[3]
    return (bits[0],bits[1],bits[2],bits[3]), digit, residual


def source_forcing(n: int) -> Fraction:
    """Unmodified four signed BBP poles; n>=1."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be positive")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def bbp_x_interval(terms: int) -> tuple[Fraction, Fraction]:
    """Certified enclosure for x=pi/16 using only BBP and positive tail."""
    if type(terms) is not int or terms < 0:
        raise ValueError("terms must be nonnegative")
    partial = sum((source_forcing(j) / (16**j) for j in range(1,terms+1)),Fraction())
    # r(j) is positive decreasing for the canonical source; bound the remaining
    # geometric series by r(terms+1)*16^(-terms)/15.
    return partial, partial + source_forcing(terms+1) / (15*(16**terms))


def certified_prefix(n_digits: int, source_terms: int) -> tuple[int, ...]:
    """Return n hexadecimal digits if the exact rational interval certifies them."""
    if type(n_digits) is not int or n_digits < 0:
        raise ValueError("n_digits must be nonnegative")
    lo, hi = bbp_x_interval(source_terms)
    if lo < 0 or hi >= 1:
        raise ValueError("source interval crosses normalized state boundary")
    low_int = (16**n_digits*lo).__floor__()
    high_int = (16**n_digits*hi).__floor__()
    if low_int != high_int:
        raise ValueError("source terms are insufficient to certify all requested digits")
    result = []
    for j in range(n_digits):
        result.append((low_int // 16**(n_digits-j-1)) % 16)
    return tuple(result)


def step_with_memory(prefix: int, length: int, residue: Fraction) -> tuple[int,int,Fraction]:
    """Append exactly one reflected digit; retain unwrapped prefix and through state."""
    if prefix < 0 or length < 0 or prefix >= 16**length:
        raise ValueError("invalid prefix")
    digit, next_residue = digit_remainder(residue,16)
    return 16*prefix+digit, length+1, next_residue


def original_state(prefix: int,length: int,residue: Fraction) -> Fraction:
    """The invariant seed coordinate reconstructed from all acquired digits and tail."""
    return (Fraction(prefix)+Fraction(residue)) / (16**length)


def walsh_row(k: int, coefficients: tuple[Fraction, ...]) -> Fraction:
    """Unnormalized 16x16 Walsh-Hadamard row acting on exact rational amplitudes."""
    if type(k) is not int or not 0<=k<16 or len(coefficients)!=16:
        raise ValueError("requires one of 16 rows and 16 amplitudes")
    return sum(((-1 if ((k & d).bit_count() & 1) else 1)*Fraction(c)
                for d,c in enumerate(coefficients)),Fraction())


def norm_of_input_piecewise_constant(coefficients: tuple[Fraction, ...]) -> Fraction:
    """L^2 norm squared of f(x)=a_d on each interval [d/16,(d+1)/16)."""
    if len(coefficients)!=16:
        raise ValueError("requires exactly 16 pieces")
    return sum((Fraction(c)**2 for c in coefficients),Fraction())/16


def branch_norm(coefficients: tuple[Fraction, ...]) -> Fraction:
    """Sum of L^2 branch norms after (Uf)_d(t)=f((d+t)/16)/4."""
    if len(coefficients)!=16:
        raise ValueError("requires 16 pieces")
    return sum(((Fraction(c)/4)**2 for c in coefficients),Fraction())


def walsh_norm(coefficients: tuple[Fraction, ...]) -> Fraction:
    """Sum of norms after following the unitary branch split by Walsh-Hadamard."""
    if len(coefficients)!=16:
        raise ValueError("requires 16 pieces")
    return sum(((walsh_row(k,coefficients)/16)**2 for k in range(16)),Fraction())


def original_root_arc_coordinates() -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Angles of four authentic H roots normalized on the left semicircle.

    H(t)=(t^2+2)(t^2+2t+2): t=i√2, -1+i, -1-i, -i√2.
    The coordinates follow their exact angles π/2,3π/4,5π/4,3π/2;
    they do NOT define an authenticated map from the actual π-phase orbit.
    """
    return Fraction(0),Fraction(1,4),Fraction(3,4),Fraction(1)
