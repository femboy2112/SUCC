"""Source-faithful mixed BBP lag filters and their prime-birth passports.

Finite differences remove specified old prime clocks, not the entire source
state. New prime births can survive at their newest endpoint. The accompanying
paper proves these assertions and gives mixed Green-tail error bounds; it does
not prove a signed correlation saving or pi normality.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import factorial, prod

from .bbp_cyclotomic_birth import (
    birth_index, next_pole_gap, p_primary_first_digit, unwrapped_bbp,
)
from .bbp_source_memory import forcing


def _nat(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError("exact integer >= %d required" % minimum)
    return value


def _lags(lags: tuple[int, ...]) -> tuple[int, ...]:
    if type(lags) is not tuple or not lags:
        raise ValueError("nonempty tuple of positive integer lags required")
    for lag in lags:
        _nat(lag, 1)
    return lags


def lag_filter(lags: tuple[int, ...]) -> tuple[int, ...]:
    """Integer coefficients of P(X)=product (X**lag-1), low degree first."""
    _lags(lags)
    coefficients = [1]
    for lag in lags:
        result = [0] * (len(coefficients) + lag)
        for index, value in enumerate(coefficients):
            result[index] -= value
            result[index+lag] += value
        coefficients = result
    return tuple(coefficients)


def filter_state_multiplier(lags: tuple[int, ...]) -> int:
    """P(16)>0: mixed ordinary lag differences never erase initial state."""
    return prod(16**lag-1 for lag in _lags(lags))


def source_filter_passport(start: int, lags: tuple[int, ...]) -> dict:
    """Exact P(E)U_start=P(16)U_start+authenticated forcing correction.

    Both routes retain U_0=0 and every signed original forcing term. Integer
    lifts are kept; taking the result mod one subsequently is lawful.
    """
    _nat(start)
    coefficients = lag_filter(lags)
    states = [Q()]
    for n in range(1, start + len(coefficients)):
        states.append(16*states[-1] + forcing(n))
    direct = sum((coefficient*states[start+j]
                  for j, coefficient in enumerate(coefficients)), Q())
    correction = sum((coefficient * sum(
        (16**(j-a)*forcing(start+a) for a in range(1, j+1)), Q())
        for j, coefficient in enumerate(coefficients)), Q())
    multiplier = filter_state_multiplier(lags)
    if direct != multiplier*states[start]+correction:
        raise AssertionError("filtered source recurrence does not commute")
    return {"start": start, "lags": lags, "coefficients": coefficients,
            "state": states[start], "filtered_state": direct,
            "state_multiplier": multiplier, "forcing_correction": correction,
            "source": "BBP original four signed poles; U_0=0"}


def prime_filter_passport(prime: int, start: int,
                          lags: tuple[int, ...]) -> dict:
    """Exact prime-primary output before the prime's second source pole.

    Restriction prime==1 mod8 is intentional. Endpoints before first birth
    contribute zero; endpoints from first birth onward contribute the genuine
    4*16**(index-birth)/prime phase. A prime-square event is outside this gate.
    """
    n0 = birth_index(prime)
    if prime % 8 != 1:
        raise ValueError("first-birth passport requires prime == 1 mod 8")
    _nat(start)
    coefficients = lag_filter(lags)
    last = start + len(coefficients)-1
    if last >= n0+next_pole_gap(prime):
        raise ValueError("filter reaches a second prime pole")
    predicted = sum(coefficient*4*pow(16, start+j-n0, prime)
                    for j, coefficient in enumerate(coefficients)
                    if start+j >= n0) % prime
    direct = sum((coefficient*unwrapped_bbp(start+j)
                  for j, coefficient in enumerate(coefficients)), Q())
    observed = p_primary_first_digit(direct, prime)
    if observed != predicted:
        raise AssertionError("original prime birth and filtered source disagree")
    return {"prime": prime, "start": start, "last": last, "birth": n0,
            "lags": lags, "residue": predicted,
            "fresh_last_endpoint": last == n0,
            "old_clock_only": start >= n0,
            "filtered_phase": direct % 1}


def mixed_forcing_moment(start: int, lags: tuple[int, ...]) -> Q:
    """Positive (-1)**r P(E)r(start+1), for arbitrary positive integer lags."""
    _nat(start)
    coefficients = lag_filter(lags)
    return (-1)**len(lags)*sum(
        (coefficient*forcing(start+j+1)
         for j, coefficient in enumerate(coefficients)), Q())


def mixed_tail_interval(start: int, lags: tuple[int, ...],
                        terms: int = 4) -> tuple[Q, Q]:
    """Strict rational enclosure of R=(-1)**r P(E)T_start > 0.

    Positive geometric expansion of 1/(16-x**8) gives the lower sum and
    monotonicity in start gives the displayed strict remainder bound.
    """
    _nat(start); _lags(lags); _nat(terms, 1)
    lower = sum((mixed_forcing_moment(start+j, lags)/16**(j+1)
                 for j in range(terms)), Q())
    return lower, lower + mixed_forcing_moment(start+terms, lags)/(15*16**terms)


def mixed_tail_beta_bounds(start: int,
                           lags: tuple[int, ...]) -> tuple[Q, Q]:
    """Strict K/4 < R < K for an exactly integrated positive mixed kernel."""
    _nat(start)
    coefficients = lag_filter(lags)
    kernel = (-1)**len(lags)*sum(
        (Q(coefficient, (8*(start+j)+1)*(8*(start+j)+2))
         for j, coefficient in enumerate(coefficients)), Q())
    return kernel/4, kernel


def mixed_tail_simple_upper(start: int, lags: tuple[int, ...]) -> Q:
    """Uniform upper with polynomial lag cost, not 16**sum(lags).

    R < min(B(8n+1,2), 8**r*product(lags)*B(8n+1,r+2)).
    """
    _nat(start); _lags(lags)
    order = len(lags)
    denominator = prod(8*start+j for j in range(1, order+3))
    beta_upper = Q(8**order*prod(lags)*factorial(order+1), denominator)
    return min(Q(1, (8*start+1)*(8*start+2)), beta_upper)


def mixed_character_transport_upper(start: int, length: int,
                                    lags: tuple[int, ...], h: int = 1) -> Q:
    """Upper for sum |e(h P(E)U_n)-e(h P(16)16**n alpha)|, alpha=pi/16.

    This compares with the genuine completed circle orbit, NOT with
    e(h P(16)U_n). The latter comparison has an exponentially larger debt.
    No cancellation of the target growing Fourier frequency is assumed.
    """
    _nat(start); _nat(length); _lags(lags)
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    return min(Q(2*length), Q(44*abs(h), 7)*sum(
        (mixed_tail_simple_upper(n, lags)
         for n in range(start, start+length)), Q()))
