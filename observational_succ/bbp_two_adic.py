"""Exact finite quotients of the authentic BBP source over the 2-adic integers.

The underlying paper proofs are in the accompanying research report.  In
particular, the source particular solution F is an isometric bijection and
F(0)=0.  No real normality, independent carries, or cross-place continuity
is asserted by these finite computations.

Every evaluator reduces integers modulo its declared power of two.  It
does not construct the exponentially large unwrapped rational source.
"""

from fractions import Fraction


def _integer(value, name):
    if type(value) is not int:
        raise ValueError(f"{name} must be an integer")
    return value


def _bits(bits):
    _integer(bits, "bits")
    if bits < 1:
        raise ValueError("bits must be positive")
    return bits


def rational_mod(value, bits):
    """Reduce an exact 2-integral rational modulo ``2**bits``.

    An even reduced denominator is a type error for this residue map.
    """
    _bits(bits)
    if type(value) not in (int, Fraction):
        raise ValueError("an exact rational is required")
    value = Fraction(value)
    if value.denominator % 2 == 0:
        raise ValueError("the reduced denominator must be odd")
    modulus = 1 << bits
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def forcing_mod(index, bits):
    """The authentic collapsed r(index) modulo 2**bits, at any integer index.

    Unlike its real positive-source interpretation, the rational formula is
    defined at every integer, including zero and negative integers.  All
    four denominator factors are odd.  The formula extends to an isometric
    bijection of Z_2; the finite quotient is a permutation.
    """
    _integer(index, "index")
    _bits(bits)
    modulus = 1 << bits
    index %= modulus
    numerator = (120 * index * index - 89 * index + 16) % modulus
    denominator = ((2 * index - 1) * (4 * index - 1)
                   * (8 * index - 7) * (8 * index - 3)) % modulus
    return numerator * pow(denominator, -1, modulus) % modulus


def particular_mod(index, bits):
    """F(index)=sum_{j>=0}16**j r(index-j) modulo 2**bits.

    Terms with 4*j >= bits vanish exactly.  F(index) is also an isometric
    permutation on every finite quotient.  The analytic theorem F(0)=0
    implies that for integer index>=0 this is the residue of the authentic
    unwrapped zero-initial-state BBP source U_index.
    """
    _integer(index, "index")
    _bits(bits)
    modulus = 1 << bits
    total = 0
    for j in range((bits + 3) // 4):
        total += (1 << (4 * j)) * forcing_mod(index - j, bits - 4 * j)
    return total % modulus


def particular_inverse_mod(value, bits):
    """The unique t mod 2**bits with F(t)=value, by compatible bit lifting.

    The isometry theorem says exactly one of t and t+2**(k-1) lifts a
    solution at precision k-1 to precision k.  A failed invariant raises
    an error instead of returning an unverified inverse.
    """
    _integer(value, "value")
    _bits(bits)
    result = 0
    for precision in range(1, bits + 1):
        modulus = 1 << precision
        target = value % modulus
        if particular_mod(result, precision) != target:
            result += 1 << (precision - 1)
        if particular_mod(result, precision) != target:
            raise ArithmeticError("the particular-solution isometry failed")
    return result


def time_transport_mod(multiplier, index, bits):
    """sigma_q=F^{-1} o (q multiplication) o F at finite 2-adic precision.

    Odd q gives a coherent family of isometric permutations and
    sigma_q o sigma_r = sigma_(q*r).  These are 2-adic time relabelings;
    they do not assert real-circle state transport or preserve a short
    chronological window.  Negative odd multipliers are allowed.
    """
    _integer(multiplier, "multiplier")
    _integer(index, "index")
    _bits(bits)
    if multiplier % 2 == 0:
        raise ValueError("an odd multiplier is required for a permutation")
    target = multiplier * particular_mod(index, bits) % (1 << bits)
    return particular_inverse_mod(target, bits)


def carry_memory_mod(carries, bits):
    """The literal cumulative carry C_n=16*C_(n-1)+c_n mod 2**bits.

    Carries must be integers, but need not be hexadecimal digits: a small
    positive forcing can allow a literal carry of 16.  The formula retains
    that carry instead of silently reducing each carry modulo 16.
    """
    _bits(bits)
    modulus = 1 << bits
    value = 0
    for carry in carries:
        _integer(carry, "carry")
        value = (16 * value + carry) % modulus
    return value


def residue_collision_count(length, bits):
    """Ordered F-residue collisions in any consecutive ``length`` indices.

    Precision zero denotes the single residue class.  The exact isometry
    F(s)=F(t) mod 2**bits iff s=t mod 2**bits gives the formula below.
    Every one-bit refinement is at most P/2+length/2; four-bit refinement
    is at most P/16+15*length/16.  These counts use 2-adic congruence,
    not real-circle near collisions after literal carries are removed.
    """
    _integer(length, "length")
    _integer(bits, "bits")
    if length < 0 or bits < 0:
        raise ValueError("length and bits must be nonnegative")
    modulus = 1 << bits
    quotient, remainder = divmod(length, modulus)
    return (remainder * (quotient + 1) ** 2
            + (modulus - remainder) * quotient ** 2)


def truncation_dyadic_exponent(depth):
    """Exact power of 2 in the reduced denominator of the depth-N BBP sum.

    P_N=16**(1-N) U_N and the source isometry with F(0)=0 gives
    v_2(U_N)=v_2(N).  Hence the denominator exponent is
    max(0, 4*(N-1)-v_2(N)).  This is an arithmetic theorem, not a
    complete-period replacement for the initial real orbit.
    """
    _integer(depth, "depth")
    if depth < 1:
        raise ValueError("depth must be positive")
    valuation = (depth & -depth).bit_length() - 1
    return max(0, 4 * (depth - 1) - valuation)


def truncation_preperiod(depth):
    """Exact base-16 preperiod of the depth-N rational BBP truncation."""
    return (truncation_dyadic_exponent(depth) + 3) // 4
