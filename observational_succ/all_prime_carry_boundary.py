"""All-prime additive residue ledger at authentic BBP real carry boundaries.

Research-only. Source is imported from duck_bbp, not redefined here.
Every prime-power in lcm(den(previous), den(forcing)) contributes, including
inherited primes with zero incoming source fraction. No digit normality claim.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import lcm

from observational_succ.duck_bbp import forcing
from observational_succ.adelic_additive_gluing import (
    factor_with_bound, local_additive_fraction, orbit_states,
)


def _fraction(value: Fraction) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError("exact Fraction required")
    return value


def _floor(x: Fraction) -> int:
    return x.numerator // x.denominator


def _ceil_div(a: int, b: int) -> int:
    if type(a) is not int or type(b) is not int or b <= 0:
        raise ValueError("ceil_div needs integers and a positive denominator")
    return -((-a) // b)


@dataclass(frozen=True)
class PrimeBoundaryRow:
    prime: int
    power: int
    prior: Fraction
    forcing: Fraction
    next: Fraction
    local_winding: int
    inherited_without_forcing: bool
    source_only: bool
    time_mod_prime_power: int | None


@dataclass(frozen=True)
class CompleteCarryLedger:
    source_time: int | None
    previous: Fraction
    forcing: Fraction
    following: Fraction
    conductor: int
    rows: tuple[PrimeBoundaryRow, ...]
    prior_global_winding: int
    next_global_winding: int
    source_integer_offset: int
    local_winding_sum: int
    literal_carry: int
    reconstructed_carry: int


def carry_ledger(previous: Fraction, driver: Fraction, maximum_prime: int, *, source_time: int | None = None) -> CompleteCarryLedger:
    """Exact full p^v-to-real carry identity with global CRT wrap winds.

    No probabilistic input: previous, driver, following are exact Q rationals.
    The p^v support is that of lcm of reduced denominators; primes absent
    from the driver MUST NOT be suppressed if inherited from previous.
    """
    previous, driver = _fraction(previous), _fraction(driver)
    following = 16 * previous + driver
    conductor = lcm(previous.denominator, driver.denominator)
    factors = factor_with_bound(conductor, maximum_prime)
    rows: list[PrimeBoundaryRow] = []
    for p, exponent in sorted(factors.items()):
        a = local_additive_fraction(previous, p)
        b = local_additive_fraction(driver, p)
        c = local_additive_fraction(following, p)
        winding = _floor(16 * a + b)
        assert (16 * a + b - winding) == c
        rows.append(PrimeBoundaryRow(p, p**exponent, a, b, c, winding,
                                     a != 0 and b == 0, a == 0 and b != 0,
                                     None if source_time is None else source_time%(p**exponent)))
    qprev = _floor(sum((r.prior for r in rows), Fraction()))
    qnext = _floor(sum((r.next for r in rows), Fraction()))
    total_source = sum((r.forcing for r in rows), Fraction())
    m = driver - total_source
    if m.denominator != 1:
        raise ArithmeticError("lost additive product formula, source offset not integer")
    total_winding = sum(r.local_winding for r in rows)
    literal = _floor(16 * (previous % 1) + driver)
    reconstructed = m.numerator + total_winding + qnext - 16 * qprev
    if literal != reconstructed or literal != _floor(following) - 16 * _floor(previous):
        raise ArithmeticError("all-prime carry does not agree with literal integer lift")
    return CompleteCarryLedger(source_time, previous, driver, following, conductor, tuple(rows),
                               qprev, qnext, m.numerator, total_winding, literal, reconstructed)


def original_carry_ledger(source_time: int, *, states: tuple[Fraction, ...] | None = None) -> CompleteCarryLedger:
    if type(source_time) is not int or source_time < 1:
        raise ValueError("source_time must be >=1")
    states = orbit_states(source_time) if states is None else states
    if len(states) <= source_time:
        raise ValueError("states must contain the requested time")
    if states[0] != 0:
        raise ValueError("authentic selected orbit requires U0=0")
    if any(states[j] != 16 * states[j-1] + forcing(j) for j in range(1,source_time+1)):
        raise ValueError("source prefix or transition mismatch")
    return carry_ledger(states[source_time-1], forcing(source_time), 8*source_time-3, source_time=source_time)


def carry_interval(conductor: int, driver: Fraction, carry: int) -> tuple[int, int]:
    """Half-open [lo,hi) of m in [0,Q): floor(16m/Q+r)=carry.

    Works for any rational source, even when its denominator does not divide Q;
    for the full authenticated CRT boundary the chosen Q contains both.
    """
    if type(conductor) is not int or conductor <=0 or type(carry) is not int:
        raise ValueError("integer conductor>0 and carry required")
    _fraction(driver)
    D, P = driver.denominator, driver.numerator
    scale = conductor * D
    t = conductor * P
    lo = max(0, min(conductor, _ceil_div(carry*scale-t,16*D)))
    hi = max(0, min(conductor, _ceil_div((carry+1)*scale-t,16*D)))
    return lo, max(lo, hi)


def carry_at_address(conductor: int, driver: Fraction, address: int) -> int:
    if type(address) is not int or not (0 <= address < conductor):
        raise ValueError("integer address in [0,Q) required")
    return _floor(Fraction(16*address, conductor)+_fraction(driver))


def _slice_count(lo: int, hi: int, modulus: int, residue: int, Q: int) -> int:
    if Q % modulus or not (0 <= residue < modulus):
        raise ValueError("declared modulus must divide Q and residue be valid")
    lo_t = max(0, min(Q//modulus, _ceil_div(lo-residue,modulus)))
    hi_t = max(0, min(Q//modulus, _ceil_div(hi-residue,modulus)))
    return max(0, hi_t-lo_t)


def partial_prime_carry_count(conductor: int, driver: Fraction, selected_prime_powers: tuple[int, ...],
                              selected_address: int, carry: int) -> tuple[int, int]:
    """Carry counts over every complementary CRT completion, NEVER iid claim.

    M product of selected full prime powers, Q/M completions; the selected
    address fixes m mod M, with no assumptions about which completion is real.
    """
    M = 1
    for power in selected_prime_powers:
        if type(power) is not int or power < 2 or conductor % (M*power):
            raise ValueError("selected prime powers must be disjoint factors of Q")
        M *= power
    if type(selected_address) is not int or not (0 <= selected_address < M):
        raise ValueError("selected residue must be in [0,M)")
    left,right = carry_interval(conductor, driver, carry)
    return _slice_count(left,right,M,selected_address,conductor), conductor//M


def crt_phase_address(conductor: int, local_residues: dict[int, int]) -> int:
    """Reconstruct m mod Q from every prime-power *address* m mod p^v.

    These residues are distinct from additive fractions [m/Q]_p.
    The caller supplies the full prime-power factorization, not one prime.
    """
    if type(conductor) is not int or conductor <=0:
        raise ValueError("conductor must be positive")
    Q = 1
    total = 0
    for power, residue in sorted(local_residues.items()):
        if type(power) is not int or power<2 or type(residue) is not int or not (0<=residue<power):
            raise ValueError("invalid prime-power residue")
        if conductor%power:
            raise ValueError("not a divisor of the conductor")
        from math import gcd
        if gcd(Q,power)!=1:
            raise ValueError("prime-power factors must be pairwise coprime")
        step = (residue-total) * pow(Q,-1,power) % power
        total += Q*step
        Q *= power
    if Q != conductor:
        raise ValueError("partial CRT address: all primes required")
    return total % conductor


def consecutive_carry_counts(conductor: int, driver: Fraction) -> dict[int,int]:
    """The COMPLETE carry alphabet, not just a single selected event."""
    lo = _floor(driver)
    hi = _floor(Fraction(16*(conductor-1),conductor)+driver)
    return {k:carry_interval(conductor,driver,k)[1]-carry_interval(conductor,driver,k)[0]
            for k in range(lo,hi+1)}


def completed_digit_from_tail(next_source_phase: Fraction, next_tail_low: Fraction,
                              next_tail_high: Fraction, literal_carry: int) -> tuple[int, int]:
    """Certified source carry -> true completed radix digit, if interval unique.

    With true T_n in [low,high], complete phase is U_n + T_n, and
    floor(16*{U_(n-1)+T_(n-1)}) = floor(16*{U_(n-1)}+r(n)+T_n) mod16.
    May differ from literal source carry by +1 exactly at a boundary hotspot.
    Finite source tail is an ANALYTIC enclosure, not a sampled pi oracle.
    """
    _fraction(next_source_phase); _fraction(next_tail_low); _fraction(next_tail_high)
    if not (0 <= next_tail_low <= next_tail_high < 1):
        raise ValueError("expected a nonnegative source-tail interval below one")
    lo = _floor(next_source_phase + next_tail_low)
    hi = _floor(next_source_phase + next_tail_high)
    if lo != hi:
        raise ArithmeticError("boundary hotspot not resolved at declared tail depth")
    correction = lo-literal_carry
    if correction not in (0,1):
        raise ArithmeticError("analytic source-tail correction outside {0,1}")
    return lo%16, correction


def original_digit_at_carry(source_time: int, depth: int=12, *, states: tuple[Fraction, ...] | None = None) -> tuple[int,int,int]:
    """(completed hexadecimal digit, literal rational carry, 0/1 hotspot).

    Uses original source future-tail interval from the canonical duck_bbp API.
    No direct pi or decimal approximation; not a frequency/asymptotic theorem.
    """
    from observational_succ.duck_bbp import tail_interval
    if type(depth) is not int or depth<0:
        raise ValueError("nonnegative depth required")
    ledger=original_carry_ledger(source_time,states=states)
    low,high=tail_interval(source_time,depth)
    unwrapped_phase=16*(ledger.previous%1)+ledger.forcing
    digit,hotspot=completed_digit_from_tail(unwrapped_phase,low,high,ledger.literal_carry)
    return digit, ledger.literal_carry, hotspot


def two_adic_integral_residue(value: Fraction, bits: int) -> int:
    """Exact 2-adic INTEGER residue of rational with odd denominator.

    Distinct from the fractional additive p=2 character, which is zero.
    The integral 2-adic carrier retains information invisible to that char.
    """
    _fraction(value)
    if type(bits) is not int or bits < 1:
        raise ValueError("positive number of bits required")
    if value.denominator % 2 == 0:
        raise ValueError("not integral in Z_2")
    modulus = 1 << bits
    return (value.numerator * pow(value.denominator, -1, modulus)) % modulus


def cross_place_integer_carry(previous: Fraction, driver: Fraction, bits: int) -> tuple[int, int, int]:
    """Recover 0..16 literal carry using odd-place rational phase and 2-adic integer lift.

    Returns (carry, next_2adic_residue, next_integer_lift_residue).
    Valid for authentic positive BBP source with carry in [0,16], bits>=5.
    Not a seed-blind digit randomness theorem. No 2-adic Haar substitution.
    """
    _fraction(previous); _fraction(driver)
    if type(bits) is not int or bits<5:
        raise ValueError("at least five bits needed to distinguish 0 from 16")
    following = 16*previous+driver
    Q = lcm(previous.denominator,driver.denominator)
    if Q%2==0:
        raise ValueError("odd-source conductor required")
    # Each fractional phase is in Z2 since all reduced denominators are odd.
    phase_prev = previous % 1
    phase_next = following % 1
    modulus=1<<bits
    u_prev = two_adic_integral_residue(previous,bits)
    u_next = two_adic_integral_residue(following,bits)
    c_prev = (u_prev-two_adic_integral_residue(phase_prev,bits)) % modulus
    c_next = (u_next-two_adic_integral_residue(phase_next,bits)) % modulus
    carry = (c_next-16*c_prev)%modulus
    if not (0<=carry<=16):
        raise ArithmeticError("not a BBP source-compatible literal carry")
    if (u_next-16*u_prev-two_adic_integral_residue(driver,bits))%modulus:
        raise ArithmeticError("2-adic source transition failed")
    return carry,u_next,c_next
