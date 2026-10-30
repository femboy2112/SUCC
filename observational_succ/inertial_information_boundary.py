"""Exact pointed preparation, coding and causal-boundary instruments.

Preparation cost, framed code length and probability-law information are
different objects.  No function below identifies them or proves pi normality.
Paper authority: research/2026-10-29/inertial_information_boundary/.
The native four-pole source is imported without modification.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd
from types import MappingProxyType
from typing import Iterable, Mapping

from .oily_macaroni_transfer import authentic_r


def _integer(value, name="integer", *, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError(f"exact {name} required")
    return value


def _rational(value, name="rational", *, nonnegative=False):
    if type(value) not in (int, F):
        raise ValueError(f"exact {name} required")
    value = F(value)
    if nonnegative and value < 0:
        raise ValueError(f"nonnegative {name} required")
    return value


def _base(value):
    return _integer(value, "base >= 2", minimum=2)


def _frequency(value):
    _integer(value, "nonzero integer frequency")
    if not value:
        raise ValueError("nonzero integer frequency required")
    return value


def signed_integer_encode(value: int) -> str:
    """0 -> '0'; nonzero -> '1' + sign + Elias-gamma(abs(value)).

    Sign is 0 for positive and 1 for negative. This is a declared framed
    prefix code, not a universal ranking of descriptions of fixed numerals.
    """
    _integer(value)
    if value == 0:
        return "0"
    binary = format(abs(value), "b")
    return "1" + ("1" if value < 0 else "0") + "0"*(len(binary)-1) + binary


def signed_integer_decode(code: str) -> int:
    """Decode exactly one complete codeword; reject truncation/trailing bits."""
    if not isinstance(code, str) or not code or any(c not in "01" for c in code):
        raise ValueError("nonempty binary codeword required")
    if code[0] == "0":
        if code != "0":
            raise ValueError("trailing bits after zero codeword")
        return 0
    if len(code) < 3:
        raise ValueError("truncated signed gamma codeword")
    body = code[2:]
    zeros = len(body)-len(body.lstrip("0"))
    if len(body) != 2*zeros+1:
        raise ValueError("truncated or trailing gamma payload")
    value = int(body[zeros:], 2)
    return -value if code[1] == "1" else value


def signed_integer_code_length(value: int) -> int:
    _integer(value)
    return 1 if value == 0 else 2*(abs(value).bit_length()-1)+3


def integer_kraft_partial(max_magnitude: int) -> F:
    """Exact Kraft mass for integer symbols -M,...,M, including zero."""
    _integer(max_magnitude, "nonnegative magnitude", minimum=0)
    answer, low, level = F(1, 2), 1, 0
    while low <= max_magnitude:
        count = min(max_magnitude, 2*low-1)-low+1
        answer += F(count, 2**(2*level+2))
        low *= 2
        level += 1
    return answer


def is_prefix_free(words: Iterable[str]) -> bool:
    """Exact prefix test; the empty codeword is allowed only as a lone code."""
    codes = tuple(words)
    if any(not isinstance(w, str) or any(c not in "01" for c in w) for w in codes):
        raise ValueError("binary strings required")
    codes = sorted(codes)
    return all(not right.startswith(left) for left, right in zip(codes, codes[1:]))


@dataclass(frozen=True)
class AffinePreparation:
    """A declared affine instruction with a nonnegative intervention cost.

    A zero-cost instruction MUST fix the distinguished neutral state zero.
    The finite grammar then has a strictly positive cost gap whenever it
    contains paid operations. Cost is not a code length or an entropy.
    """
    multiplier: F
    offset: F
    cost: F

    def __post_init__(self):
        for name in ("multiplier", "offset", "cost"):
            object.__setattr__(self, name, _rational(
                getattr(self, name), name, nonnegative=(name == "cost")))
        if self.cost == 0 and self.offset != 0:
            raise ValueError("a free preparation may not displace neutral zero")


def preparation_grammar(base: int = 16) -> Mapping[str, AffinePreparation]:
    base = _base(base)
    return MappingProxyType({
        "R": AffinePreparation(base, 0, 0),
        "N": AffinePreparation(-1, 0, 0),
        "+": AffinePreparation(1, 1, 1),
        "-": AffinePreparation(1, -1, 1),
    })


def evaluate_preparation(word: Iterable[str], operations=None, *, base: int = 16) -> dict:
    """Evaluate a finite instruction word from neutral zero, retaining costs."""
    _base(base)
    grammar = preparation_grammar(base) if operations is None else operations
    if not isinstance(grammar, Mapping):
        raise ValueError("finite preparation mapping required")
    if any(not isinstance(label, str) or not label or not isinstance(op, AffinePreparation)
           for label, op in grammar.items()):
        raise ValueError("named validated affine preparations required")
    state, cost, history = F(), F(), [F()]
    instructions = tuple(word)
    for label in instructions:
        if not isinstance(label, str) or label not in grammar:
            raise ValueError("unknown preparation instruction")
        op = grammar[label]
        state = op.multiplier*state+op.offset
        cost += op.cost
        history.append(state)
    paid = [op.cost for op in grammar.values() if op.cost > 0]
    return {"seed": state, "cost": cost, "history": tuple(history),
            "steps": len(instructions), "positive_cost_gap": min(paid) if paid else None}


def recurrence_history(forcing: Iterable, seed=0, *, base: int = 16) -> tuple[F, ...]:
    base = _base(base)
    state = _rational(seed, "seed")
    values = [state]
    for value in forcing:
        state = base*state+_rational(value, "forcing")
        values.append(state)
    return tuple(values)


def scaled_history(history: Iterable, *, base: int = 16) -> tuple[F, ...]:
    base = _base(base)
    states = tuple(_rational(x, "state") for x in history)
    if not states:
        raise ValueError("history must include time-zero state")
    return tuple(x/base**n for n, x in enumerate(states))


def homogeneous_charge(forcing: Iterable, state, time: int, *, base: int = 16) -> F:
    """Recover the seed from one exact state and the complete source prefix."""
    base = _base(base)
    _integer(time, "nonnegative time", minimum=0)
    inputs = tuple(_rational(x, "forcing") for x in forcing)
    if len(inputs) < time:
        raise ValueError("complete source prefix through the observed time required")
    return (_rational(state, "state")/base**time
            -sum((inputs[k-1]/base**k for k in range(1, time+1)), F()))


def finite_advanced_seed(forcing: Iterable, *, base: int = 16) -> F:
    """Unique seed making the last state zero; generally anticipates the source."""
    base = _base(base)
    return -sum((_rational(x, "forcing")/base**k
                 for k, x in enumerate(forcing, 1)), F())


def seed_phase_residue(seed_offset, time: int, *, frequency: int = 1,
                       base: int = 16) -> F:
    """Exact argument modulo one of the ratio of same-source seed phases."""
    base, frequency = _base(base), _frequency(frequency)
    _integer(time, "nonnegative time", minimum=0)
    value = frequency*base**time*_rational(seed_offset, "seed offset")
    return F(value.numerator % value.denominator, value.denominator)


def eventual_phase_equivalence_start(seed_offset, *, frequency: int = 1,
                                     base: int = 16) -> int | None:
    """Least n>=0 with equal phases at every later time, or None.

    For rational offset delta this is the least n for which the reduced
    denominator of h*delta divides base**n. A prime outside the base support
    proves no such time exists. This is not a finite-search heuristic.
    """
    base, frequency = _base(base), _frequency(frequency)
    denominator = (frequency*_rational(seed_offset, "seed offset")).denominator
    time = 0
    while denominator > 1:
        common = gcd(denominator, base)
        if common == 1:
            return None
        denominator //= common
        time += 1
    return time


def phase_equivalent_from(seed_offset, start: int, *, frequency: int = 1,
                          base: int = 16) -> bool:
    _integer(start, "nonnegative observation start", minimum=0)
    first = eventual_phase_equivalence_start(seed_offset, frequency=frequency, base=base)
    return first is not None and first <= start


def coherent_laplace(a, d=0) -> F:
    """Positive source control R_d(a), not the authentic signed BBP source."""
    a, d = _rational(a, "Laplace parameter"), _rational(d, "shift", nonnegative=True)
    if a <= 0:
        raise ValueError("positive Laplace parameter required")
    return 16/(a+d)**2-1/(a+d+8)**2


def coherent_source_r(n: int, d=0) -> F:
    _integer(n, "positive source index", minimum=1)
    return coherent_laplace(8*n-7, d)


def coherent_source_history(horizon: int, d=0) -> tuple[F, ...]:
    """Closed-form zero-seeded hostile source, independently of recurrence."""
    _integer(horizon, "nonnegative horizon", minimum=0)
    d = _rational(d, "shift", nonnegative=True)
    return tuple(F(16)**n/(d+1)**2-1/(8*n+d+1)**2
                 for n in range(horizon+1))


def coherent_source_limit_mode(d=0) -> int:
    """A nonzero integer mode whose phases tend to one for rational d>=0."""
    d = _rational(d, "shift", nonnegative=True)
    return (1/(d+1)**2).denominator


def authentic_source_history(horizon: int, seed=0) -> tuple[F, ...]:
    _integer(horizon, "nonnegative horizon", minimum=0)
    return recurrence_history((authentic_r(n) for n in range(1, horizon+1)), seed)
