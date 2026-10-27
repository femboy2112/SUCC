"""Uniform signed-loss instruments for original BBP mixed lag characters.

The paper theorem controls arbitrary periodic unit templates and positive
integer lag tuples with a prescribed total span. It proves logarithmic
absolute loss only. The universal onset exists but is not numerically known.
All computations here use integers/Fractions; no guessed onset is certified.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import prod

from .bbp_diophantine_coherence import ceil_log, floor_log
from .bbp_resonant_lags import lag_filter, mixed_tail_interval
from .succ_internal_matrix_walk import authentic_r


def _nat(value, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError("ordinary integer outside the declared domain")
    return value


def _frequency(value):
    if type(value) is not int or value == 0:
        raise ValueError("nonzero ordinary integer frequency required")
    return abs(value)


def _lags(values):
    if type(values) is not tuple or not values:
        raise ValueError("a nonempty tuple of positive integer lags is required")
    for value in values:
        _nat(value)
    return values


def lag_multiplier(lags):
    """P(16), retaining every signed factor of P(X)=product(X^ell-1)."""
    return prod(16**ell-1 for ell in _lags(lags))


def scale_requirement(period, total_span, frequency=1):
    """Effective part of the onset; the unknown arithmetic onset is separate."""
    _nat(period)
    _nat(total_span)
    h = _frequency(frequency)
    return max(4096*period, 60*(total_span+ceil_log(h, 16)))


def tail_transport_upper(start, frequency=1):
    """All-order bound on the COMPLETE infinite transport debt for n>start.

    The positive Green kernel gives |P(E)T_n|<=T_n<1/(64*n*n).
    Telescoping sum_{n>start}1/n² <= 1/start and 2*pi<44/7 pay the bound.
    No exponential P(16) factor occurs: the target is the completed orbit.
    """
    _nat(start)
    return Q(11*_frequency(frequency), 112*start)


@dataclass(frozen=True)
class ConditionalMixedLagBudget:
    observations: int
    period: int
    total_span: int
    frequency: int
    threshold_exponent: int
    first_exponent: int
    eligible_blocks: int

    @property
    def first_scale(self):
        return 8**self.first_exponent

    @property
    def transport_debt(self):
        return (tail_transport_upper(self.first_scale, self.frequency)
                if self.eligible_blocks else Q())

    @property
    def modulus_sum_upper(self):
        """Upper for sum of period-residue moduli, conditional on valid onset."""
        return min(Q(self.observations), Q(self.observations)
                   -Q(self.eligible_blocks, 14)+self.transport_debt)

    @property
    def numerical_onset_certified(self):
        return False


def conditional_mixed_lag_budget(observations, period, total_span,
                                 frequency, threshold_exponent):
    """Exact scheduling arithmetic, NOT certification of a numerical pi onset."""
    _nat(observations)
    _nat(threshold_exponent, 4)
    required = scale_requirement(period, total_span, frequency)
    first = max(threshold_exponent, ceil_log(required, 8))
    blocks = max(0, floor_log(observations, 8)-first)
    return ConditionalMixedLagBudget(observations, period, total_span,
                                     frequency, threshold_exponent, first, blocks)


def diophantine_exponent_margin(scale, period, lags, frequency=1):
    """Certify m-15p-15(d+ceil_log16|h|)>=m/2 on the proved schedules.

    Together with C²16^(m/2)>16 this implies the required comparison,
    since |h|P(16)<16^(d+ceil_log16|h|). C is not supplied or certified.
    """
    _nat(scale)
    span = sum(_lags(lags))
    if scale < scale_requirement(period, span, frequency):
        raise ValueError("scale outside the prescribed joint schedule")
    exponent = scale-15*period-15*(span+ceil_log(_frequency(frequency), 16))
    if 2*exponent < scale:
        raise ArithmeticError("joint Diophantine margin failed")
    return exponent


def authentic_mixed_window(start, length, lags):
    """Exact unwrapped P(E)U_n, replayed from U_0=0 and all four poles."""
    _nat(start)
    _nat(length)
    _lags(lags)
    span = sum(lags)
    if start+length+span > 2000:
        raise ValueError("finite source replay budget exceeded")
    coefficients = lag_filter(lags)
    states = [Q()]
    for n in range(1, start+length+span):
        states.append(16*states[-1]+authentic_r(n))
    return tuple(sum((c*states[n+j] for j, c in enumerate(coefficients)), Q())
                 for n in range(start, start+length))


def verify_authentic_mixed_window(values, start, length, lags):
    if (type(values) is not tuple or any(type(x) is not Q for x in values)
            or values != authentic_mixed_window(start, length, lags)):
        raise ValueError("mixed history does not have the original zero selector")


def finite_tail_holdout(start, lags, terms=6):
    """Exact interval for positive signed mixed tail; includes infinite remainder.

    This independently replayable holdout is evidence for a finite instance,
    not a proof of the universal positive-kernel or Diophantine theorem.
    """
    _nat(start)
    _lags(lags)
    _nat(terms)
    if sum(lags)+start+terms > 2000:
        raise ValueError("finite tail replay budget exceeded")
    lower, upper = mixed_tail_interval(start, lags, terms)
    return {"start": start, "lags": lags, "terms": terms,
            "lower": lower, "upper": upper,
            "order_free_upper": Q(1, 64*start**2),
            "finite_interval_inside_bound": 0 < lower < upper < Q(1, 64*start**2),
            "infinite_remainder_included": True}
