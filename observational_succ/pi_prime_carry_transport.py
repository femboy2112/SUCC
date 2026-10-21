"""Exact Wallis/Gamma -> prime-power carry -> pi digit observation transport.

Research-status finite source interface. No pi normality or RH theorem is claimed.
All arithmetic is exact; no floating-point source inputs are accepted.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial, isqrt


def _positive_integer(value: int, name: str, *, minimum: int = 1) -> None:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def _primes_upto(bound: int) -> tuple[int, ...]:
    if bound < 2:
        return ()
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            sieve[p * p : bound + 1 : p] = b"\x00" * (((bound - p * p) // p) + 1)
    return tuple(i for i in range(2, bound + 1) if sieve[i])


def doubling_carries(n: int) -> dict[int, int]:
    """Kummer carries for n+n in every prime-power clock p^a <= 2n.

    The terms floor(2n/p^a) - 2 floor(n/p^a) are exactly 0 or 1.
    Only nonzero prime occupation entries are returned.
    """
    _positive_integer(n, "n")
    counts: dict[int, int] = {}
    for p in _primes_upto(2 * n):
        power, count = p, 0
        while power <= 2 * n:
            step = 2 * n // power - 2 * (n // power)
            assert step in (0, 1)
            count += step
            power *= p
        if count:
            counts[p] = count
    return counts


def central_binomial_by_carries(n: int) -> int:
    """Exact prime-power reconstruction of binomial(2n,n)."""
    _positive_integer(n, "n")
    value = 1
    for p, carry_count in doubling_carries(n).items():
        value *= p ** carry_count
    return value


def wallis_prime_ratio(n: int) -> Fraction:
    """R_n = 2^(4n+1)/((2n+1) * binomial(2n,n)^2) < pi."""
    _positive_integer(n, "n")
    denominator_carries = central_binomial_by_carries(n)
    return Fraction(1 << (4 * n + 1), (2 * n + 1) * denominator_carries ** 2)


def wallis_direct_ratio(n: int) -> Fraction:
    """Independent Wallis n-factorial expression; used for source cross-checks."""
    _positive_integer(n, "n")
    return Fraction(2 * (16 ** n) * factorial(n) ** 4,
                    factorial(2 * n) * factorial(2 * n + 1))


def wallis_pi_bracket(n: int) -> tuple[Fraction, Fraction]:
    """Strict rational L_n < pi < U_n, width L_n/(4n+1).

    The infinite Wallis tail obeys
      0 < log(pi/L_n) < sum_{k>n}1/(4k^2-1) = 1/(4n+2).
    Since e^t <= 1/(1-t), U_n=L_n*(4n+2)/(4n+1) is valid.
    """
    lower = wallis_prime_ratio(n)
    return lower, lower * Fraction(4 * n + 2, 4 * n + 1)


def euler_prime_square_bracket(cutoff: int) -> tuple[Fraction, Fraction]:
    """Strict rational bracket of pi**2 from zeta(2)'s Euler product.

    For P_Q = 6 prod_{p<=Q}(1-p^-2)^-1, Q>=2,
    P_Q < pi**2 < P_Q*(Q+1)/Q, as the omitted prime tail is
    dominated by the telescoping product over all integers > Q.
    """
    _positive_integer(cutoff, "cutoff", minimum=2)
    lower = Fraction(6)
    for p in _primes_upto(cutoff):
        lower *= Fraction(p * p, p * p - 1)
    return lower, lower * Fraction(cutoff + 1, cutoff)


def rational_digit_prefix(value: Fraction, base: int, length: int) -> tuple[int, ...]:
    """Fractional digits of exact nonnegative rational, without floating-point."""
    if type(value) is not Fraction or value < 0:
        raise ValueError("value must be a nonnegative exact Fraction")
    _positive_integer(base, "base", minimum=2)
    _positive_integer(length, "length", minimum=0)
    residue = value.numerator % value.denominator
    result: list[int] = []
    for _ in range(length):
        residue *= base
        digit, residue = divmod(residue, value.denominator)
        result.append(digit)
    return tuple(result)


def certified_pi_digit_prefix(n: int, base: int, length: int) -> tuple[int, ...] | None:
    """Full fractional digit prefix if exact Wallis bracket does not straddle a cylinder.

    None means insufficient precision, NOT an assertion about pi digits.
    """
    _positive_integer(base, "base", minimum=2)
    _positive_integer(length, "length", minimum=0)
    lower, upper = wallis_pi_bracket(n)
    scale = base ** length
    if (lower.numerator * scale // lower.denominator !=
            upper.numerator * scale // upper.denominator):
        return None
    return rational_digit_prefix(lower, base, length)


def prime_carry_fourier_transport_error(n: int, base: int, h: int, horizon: int) -> Fraction:
    """Strict error bound on finite pi-orbit Fourier means vs Wallis midpoint.

    |A_{b,h,N}(pi) - A_{b,h,N}((L_n+U_n)/2)| < bound,
    A_{b,h,N}(x)=N^-1 sum_{j<N} exp(2*pi*i*h*b^j*x).
    Uses the rational universal constant 2*pi<8 and actual bracket width.
    """
    _positive_integer(n, "n")
    _positive_integer(base, "base", minimum=2)
    if type(h) is not int or h == 0:
        raise ValueError("h must be a nonzero integer")
    _positive_integer(horizon, "horizon")
    lower, upper = wallis_pi_bracket(n)
    return Fraction(4 * abs(h) * (base ** horizon - 1), horizon * (base - 1)) * (upper - lower)


def wallis_midpoint(n: int) -> Fraction:
    lower, upper = wallis_pi_bracket(n)
    return (lower + upper) / 2


def synchronized_pi_brackets(n: int, cutoff: int) -> tuple[Fraction, Fraction]:
    """Two analytically different prime routes intersect into a pi^2 bracket.

    Wallis Kummer square and Basel Euler tail supply strict endpoints; the
    intersection must be nonempty when the mathematical sources are faithful.
    """
    lower, upper = wallis_pi_bracket(n)
    p_lower, p_upper = euler_prime_square_bracket(cutoff)
    lo, hi = max(lower * lower, p_lower), min(upper * upper, p_upper)
    if not lo < hi:
        raise ArithmeticError("inconsistent source brackets")
    return lo, hi


def prime_carry_phase_clock(n: int, base: int, h: int, horizon: int) -> tuple[int, tuple[int, ...]]:
    """Finite rational phase clock: residues e(h*b^j*Wallis_midpoint).

    Returns (denominator, residues) for the exact rational midpoint in lowest
    terms; all successive residues obey r_(j+1)=base*r_j mod denominator.
    This does NOT make the rational midpoint normal.
    """
    _positive_integer(base, "base", minimum=2)
    if type(h) is not int or h == 0:
        raise ValueError("h must be a nonzero integer")
    _positive_integer(horizon, "horizon", minimum=0)
    midpoint = wallis_midpoint(n)
    denominator = midpoint.denominator
    current = (h * midpoint.numerator) % denominator
    residues = []
    for _ in range(horizon):
        residues.append(current)
        current = (base * current) % denominator
    return denominator, tuple(residues)


def certified_pi_digit_prefix_joint(n: int, cutoff: int, base: int, length: int) -> tuple[int, ...] | None:
    """Digit prefix certified by intersection of Wallis and Euler pi^2 sources.

    Uses isqrt on exact scaled rational endpoints, never approximate sqrt.
    """
    _positive_integer(base, "base", minimum=2)
    _positive_integer(length, "length", minimum=0)
    lower, upper = synchronized_pi_brackets(n, cutoff)
    scale = base ** length
    lo = isqrt(lower.numerator * scale * scale // lower.denominator)
    hi = isqrt(upper.numerator * scale * scale // upper.denominator)
    if lo != hi:
        return None
    residue = lo % scale
    digits = []
    for power in reversed(range(length)):
        digit, residue = divmod(residue, base ** power)
        digits.append(digit)
    return tuple(digits)


def uniform_fourier_budget(base: int, h: int, horizon: int) -> Fraction:
    """Provable all-N bound for n=base^N without constructing its huge carries.

    |A_{b,h,N}(pi)-A_{b,h,N}(Wallis_midpoint(base^N))|
        < 4*abs(h)/(N*(base-1)) using Wallis_midpoint width and pi<4.
    The returned rational is a safe strict upper bound, not a Fourier decay
    bound on either of the two individual means.
    """
    _positive_integer(base, "base", minimum=2)
    if type(h) is not int or h == 0:
        raise ValueError("h must be a nonzero integer")
    _positive_integer(horizon, "horizon")
    return Fraction(4 * abs(h), horizon * (base - 1))


def dyadic_midpoint_period_floor(level: int) -> int:
    """For y=Wallis_midpoint(2^level), binary orbit period >= this.

    Its reduced odd denominator contains the coprime factors
    2^(level+1)+1 and 2^(level+2)+1. Their orders of 2 are exactly
    2(level+1) and 2(level+2), respectively. Thus the true purely
    periodic rational binary orbit has period divisible by this bound.
    Computing this symbolic theorem does not enumerate any huge n or primes.
    """
    _positive_integer(level, "level", minimum=0)
    return 2 * (level + 1) * (level + 2)


def long_period_nonmixing_control(horizon: int) -> tuple[int, Fraction]:
    """Negative control: huge exact binary period need not imply mixing.

    For x=1/(2^(N*N)-1), ord_denominator(2)=N*N, while
    |N^-1 sum_{j<N} exp(2*pi*i*2^j*x)-1|
        < 8*(2^N-1)/(N*(2^(N*N)-1)).
    The deviation tends to zero despite period quadratic in N.
    """
    _positive_integer(horizon, "horizon")
    m = horizon * horizon
    q = (1 << m) - 1
    return m, Fraction(8 * ((1 << horizon) - 1), horizon * q)


def prime_power_conductor(n: int, *, max_bits: int = 48) -> tuple[int, ...]:
    """Factor the *observed midpoint denominator* into coprime prime powers.

    This is not the same object as the Kummer valuation vector of the source
    central binomial coefficient. Exact trial division is intentionally bounded
    to small finite probes. Large inputs fail closed; the CRT theorem is general.
    """
    _positive_integer(max_bits, "max_bits")
    midpoint = wallis_midpoint(n)
    d = midpoint.denominator
    if d.bit_length() > max_bits:
        raise ValueError("conductor exceeds finite trial-factorization budget")
    remainder, factor = d, 2
    powers = []
    while factor * factor <= remainder:
        if remainder % factor == 0:
            power = 1
            while remainder % factor == 0:
                power *= factor
                remainder //= factor
            powers.append(power)
        factor = 3 if factor == 2 else factor + 2
    if remainder > 1:
        powers.append(remainder)
    return tuple(powers)


def joint_crt_phase_clocks(
    n: int, base: int, h: int, horizon: int, *, max_bits: int = 48,
) -> tuple[int, tuple[tuple[int, tuple[int, ...]], ...]]:
    """Exact additive-character split into simultaneous coprime prime-power clocks.

    If midpoint=a/D and D=prod(q), with u_q=(D/q)^(-1) mod q,
    e(h*b^j*a/D) = prod_q e((h*b^j*a*u_q mod q)/q).
    Returned local phases are integer residues, *not* rounded complex numbers.
    This encodes joint coherence; individual clock averages do not imply the
    mean of their product cancels.
    """
    d, global_residues = prime_carry_phase_clock(n, base, h, horizon)
    factors = prime_power_conductor(n, max_bits=max_bits)
    local = []
    for q in factors:
        inverse = pow(d // q, -1, q)
        local.append((q, tuple((r * inverse) % q for r in global_residues)))
    return d, tuple(local)
