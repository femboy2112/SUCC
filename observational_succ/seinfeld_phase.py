"""Seinfeld SUCC phase lifts: exact root fibers, Frobenius jets, and source clocks.

All phases are *rational turns*, not sampled complex amplitudes.  For a
turn t, its formal U(1) interpretation is exp(2*pi*i*t).  In particular,
this module never claims that numerical equality forces a phase choice.

All results are classical algebraic facts or finite exact diagnostics.
Pi normality, RH, source-selected character cancellation remain OPEN.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb, isqrt
from typing import Callable


class PhaseSourceError(ValueError):
    """A requested arithmetic object or source transport has the wrong type."""


def _nat(value: int, lower: int = 0) -> int:
    if type(value) is not int or value < lower:
        raise PhaseSourceError(f"integer >= {lower} required")
    return value


def _q(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise PhaseSourceError("exact integers/Fractions only, no floating phases")
    return Q(value)


def _prime(value: int) -> int:
    _nat(value, 2)
    if any(value % k == 0 for k in range(2, isqrt(value) + 1)):
        raise PhaseSourceError("primitive FUCC label must be an actual prime")
    return value


def root_turns(depth: int) -> tuple[Q, ...]:
    """Complex roots of u^(2^depth)=1 represented exactly in R/Z turns.

    This inverse fiber is larger than the anchored relation u=2-1=1.
    """
    _nat(depth)
    if depth > 10:
        raise PhaseSourceError("root enumeration limited to 1024 finite labels")
    m = 1 << depth
    return tuple(Q(j, m) for j in range(m))


def root_power_defect(depth: int) -> tuple[int, ...]:
    """Coefficients of u^(2^depth)-1 in Z[u], low degree first."""
    _nat(depth)
    if depth > 20:
        raise PhaseSourceError("finite polynomial degree capped")
    m = 1 << depth
    return tuple([-1] + [0] * (m - 1) + [1])


def jet_of_unit_relation(power: int, order: int) -> tuple[int, ...]:
    """Coefficients of (1+epsilon)^power-1 modulo epsilon^order over Z.

    The first-order coefficient is `power`.  This is an explicitly declared
    deformation of a presentation of the unit, not of the literal integers.
    """
    _nat(power, 1); _nat(order, 1)
    return tuple(0 if j == 0 else comb(power, j) if j <= power else 0
                 for j in range(order))


def _gf2_mul_truncated(a: int, b: int, width: int) -> int:
    """Carry-free F2 polynomial product modulo epsilon^width, encoded in bits."""
    _nat(a); _nat(b); _nat(width, 1)
    mask = (1 << width) - 1
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result & mask


def gf2_nilpotent_power(base: int, power: int, width: int) -> int:
    """Exact polynomial exponent in F2[eps]/(eps^width)."""
    _nat(power); _nat(base); _nat(width, 1)
    mask = (1 << width) - 1
    base &= mask
    out = 1
    while power:
        if power & 1:
            out = _gf2_mul_truncated(out, base, width)
        base = _gf2_mul_truncated(base, base, width)
        power >>= 1
    return out


def frobenius_thickening(depth: int) -> dict[str, int | bool]:
    """mu_(2^k) over F2: one geometric root but length-2^k local algebra."""
    _nat(depth, 1)
    if depth > 10:
        raise PhaseSourceError("finite polynomial width capped")
    m = 1 << depth
    # 1+eps is the encoding 0b11; eps is 0b10.
    return {
        "rank": m,
        "nilpotency_index": m,
        "geometric_points_over_algebraic_closure": 1,
        "unit_power_one": gf2_nilpotent_power(3, m, m) == 1,
        "top_nonzero": gf2_nilpotent_power(2, m - 1, m) == (1 << (m - 1)),
        "top_zero": gf2_nilpotent_power(2, m, m) == 0,
    }


def primitive_clock_multiplier_phase(n: int, p: int) -> Q:
    """A deliberately chosen phase chi_p(n)=n/p modulo one on Vp edges."""
    _nat(n, 1); _prime(p)
    return Q(n, p) % 1


def primitive_clock_affine_holonomy(n: int, p: int) -> Q:
    """Vp S versus S^p Vp, with all S edges given zero transport phase."""
    _nat(n, 1); _prime(p)
    return (primitive_clock_multiplier_phase(n + 1, p)
            - primitive_clock_multiplier_phase(n, p)) % 1


def naive_cross_prime_defect(n: int, p: int, q: int) -> Q:
    """Failure of independent phase choices chi_p(n)=n/p to commute Vp,Vq.

    Returns phase(Vp Vq) - phase(Vq Vp), modulo one, retaining actual order.
    This is a negative control for an unproved all-prime phase coherence law.
    """
    _nat(n, 1); _prime(p); _prime(q)
    a = primitive_clock_multiplier_phase(n, q) + primitive_clock_multiplier_phase(q*n, p)
    b = primitive_clock_multiplier_phase(n, p) + primitive_clock_multiplier_phase(p*n, q)
    return (a-b) % 1


def flat_prime_potential(horizon: int, character: Callable[[int, int], int | Q]) -> tuple[Q, ...]:
    """Reconstruct f from an all-prime coherent multiplicative edge connection.

    A prime-labelled edge n->p*n has phase character(p,n), in rational
    turns. If all arithmetic prime squares are flat, unique factorization
    makes the potential f well-defined, unique up to f(1). We set f(1)=0.

    This finite solver checks *every* prime edge within 1..horizon and
    rejects incompatible data. Passing finite N does not certify infinity.
    """
    _nat(horizon, 1)
    if horizon > 2048:
        raise PhaseSourceError("bounded exact all-edge phase solver")
    primes = tuple(p for p in range(2, horizon + 1)
                   if all(p % d for d in range(2, isqrt(p) + 1)))
    f = [Q() for _ in range(horizon + 1)]
    for n in range(2, horizon + 1):
        p = next(p for p in primes if n % p == 0)
        f[n] = (f[n // p] + _q(character(p, n // p))) % 1
    for n in range(1, horizon + 1):
        for p in primes:
            if p*n > horizon:
                break
            phase = (f[p*n] - f[n]) % 1
            expected = _q(character(p, n)) % 1
            if phase != expected:
                raise PhaseSourceError(
                    f"incompatible all-prime phase square at edge (n={n},p={p})")
    return tuple(f)


def multiplier_phase_from_source(n: int, a: int, source: Callable[[int], int | Q]) -> Q:
    """Coherent finite multiplier phase sourced from one potential f on N."""
    _nat(n, 1); _nat(a, 1)
    return (_q(source(a*n)) - _q(source(n))) % 1


def multiplier_square_defect(n: int, a: int, b: int,
                             source: Callable[[int], int | Q]) -> Q:
    """Exact full-semigroup commutativity V_a^f V_b^f=V_b^f V_a^f=V_ab^f."""
    _nat(n, 1); _nat(a, 1); _nat(b, 1)
    ab = (multiplier_phase_from_source(n, b, source)
          + multiplier_phase_from_source(b*n, a, source))
    ba = (multiplier_phase_from_source(n, a, source)
          + multiplier_phase_from_source(a*n, b, source))
    direct = multiplier_phase_from_source(n, a*b, source)
    if (ab-direct) % 1 != 0 or (ba-direct) % 1 != 0:
        raise ArithmeticError("a source-labelled prime square did not commute")
    return (ab-ba) % 1


def relative_affine_phase(n: int, p: int,
                          source: Callable[[int], int | Q]) -> Q:
    """Mixed SUCC/FUCC phase, with S edges set to zero as the reference.

    This is a relative comparison, not curvature of the full exact gradient
    df (whose affine-cycle holonomy always vanishes).
    """
    _nat(n, 1); _prime(p)
    return (multiplier_phase_from_source(n+1, p, source)
            - multiplier_phase_from_source(n, p, source)) % 1


def full_gradient_affine_holonomy(n: int, p: int,
                                  source: Callable[[int], int | Q]) -> Q:
    """Both S and Vp edges carry df: exact closed-cycle phase is zero."""
    _nat(n, 1); _prime(p)
    lhs = ((_q(source(n+1)) - _q(source(n)))
           + (_q(source(p*(n+1))) - _q(source(n+1))))
    rhs = ((_q(source(p*n)) - _q(source(n)))
           + sum((_q(source(j+1)) - _q(source(j))
                  for j in range(p*n, p*(n+1))), Q()))
    return (lhs-rhs) % 1


def counterfeit_unit_phase(n: int) -> Q:
    """The nonnormal #294 source's unwrapped state, for hostile comparison."""
    _nat(n)
    return Q(16**n, 3) - Q(1, (8*n+1)*(8*n+3))


def counterfeit_relative_phase_bound(n: int, p: int) -> Q:
    """Proved positive upper bound on |unwrapped mixed phase| at n>=1.

    The periodic 16^n/3 pieces cancel in the phase modulo one because
    16 is 1 mod 3.  The remaining signed tail contribution is bounded by
    T_(pn+p)+T_(pn)+T_(n+1)+T_n <= 1/(16*n^2).
    """
    _nat(n, 1); _prime(p)
    return Q(1, 16*n*n)


def counterfeit_mixed_phase_lift(n: int, p: int) -> Q:
    """Signed real representative with the periodic integer phase removed."""
    _nat(n, 1); _prime(p)
    def tail(k: int) -> Q:
        return Q(1, (8*k+1)*(8*k+3))
    return -(tail(p*(n+1)) - tail(n+1) - tail(p*n) + tail(n))


def source_mixed_phase_lift(n: int, p: int,
                            states: tuple[Q, ...]) -> Q:
    """Unwrapped mixed first difference, no quotient phase or time aliases."""
    _nat(n, 1); _prime(p)
    if len(states) <= p*(n+1):
        raise PhaseSourceError("not enough source history for the affine diamond")
    return (_q(states[p*(n+1)]) - _q(states[n+1])
            - _q(states[p*n]) + _q(states[n]))
