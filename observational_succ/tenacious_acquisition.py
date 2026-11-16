"""Exact worst-case recovery of a scalar initial target from centered interval sensors.

The source prior is a rational box centered at zero. Each paid action transforms
the present source and then reads one linear functional. See Tenacious D, TD6.
Vertex enumeration is intended for short finite certificates.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

from .principia_observatoris import ContractError, inverse, matrix, rational


def _row(values):
    return tuple(rational(value) for value in values)


def _dot(row, point):
    return sum(a * b for a, b in zip(row, point))


def _pullback(row, transition):
    return tuple(_dot(row, column) for column in zip(*transition))


@dataclass(frozen=True)
class IntervalAction:
    """Update x to A x, then report a calibrated cell for the scalar sensor s A x."""

    transition: tuple
    sensor: tuple
    half_width: Fraction
    cost: int

    def __post_init__(self):
        transition = matrix(self.transition)
        sensor = _row(self.sensor)
        width = rational(self.half_width)
        if len(transition) != len(transition[0]) or len(sensor) != len(transition):
            raise ContractError("sensor and square transition must share a dimension")
        if width < 0 or type(self.cost) is not int or self.cost <= 0:
            raise ContractError("nonnegative half-width and positive integer cost required")
        object.__setattr__(self, "transition", transition)
        object.__setattr__(self, "sensor", sensor)
        object.__setattr__(self, "half_width", width)


def central_radius(box, target, slabs=()):
    """Return the exact scalar radius and a maximizing hidden input.

    Each slab is (row, width) in initial coordinates. The source box is compact,
    so an active full-rank vertex attains the maximum even for zero widths.
    """
    box, target = _row(box), _row(target)
    size = len(box)
    if size == 0 or len(target) != size or any(bound < 0 for bound in box):
        raise ContractError("nonempty aligned box and target with nonnegative bounds required")
    constraints = [(tuple(Fraction(i == j) for j in range(size)), b)
                   for i, b in enumerate(box)]
    for coefficients, width in slabs:
        row, width = _row(coefficients), rational(width)
        if len(row) != size or width < 0:
            raise ContractError("invalid hidden slab")
        constraints.append((row, width))
    faces = [(tuple(sign * a for a in row), width)
             for row, width in constraints for sign in (1, -1)]
    best = Fraction(0)
    witness = (Fraction(0),) * size
    for selected in combinations(faces, size):
        rows, bounds = zip(*selected)
        try:
            solver = inverse(rows)
        except ContractError:
            continue  # A singular set of active faces does not define a vertex.
        candidate = tuple(_dot(row, bounds) for row in solver)
        if all(abs(_dot(row, candidate)) <= width for row, width in constraints):
            score = _dot(target, candidate)
            if score > best:
                best, witness = score, candidate
    return best, witness


def best_interval_schedule(box, target, actions, budget):
    """Return (radius, fixed action-index word, hidden witness for that word).

    Computes the adaptive deterministic minimax value under TD6's sensor
    contract. A zero half-width models an exact readout and may use an infinite
    alphabet. Positive widths admit finite centered grids on bounded ranges.
    """
    box, target, actions = _row(box), _row(target), tuple(actions)
    if type(budget) is not int or budget < 0:
        raise ContractError("nonnegative integer budget required")
    if any(not isinstance(a, IntervalAction) or len(a.sensor) != len(box) for a in actions):
        raise ContractError("action dimension does not match source")
    radius, witness = central_radius(box, target)
    best = (radius, (), witness)
    size = len(box)
    identity = tuple(tuple(Fraction(i == j) for j in range(size)) for i in range(size))
    pending = [((), budget, identity, ())]
    while pending:
        word, remaining, transform, slabs = pending.pop()
        for index, action in enumerate(actions):
            if action.cost > remaining:
                continue
            updated = tuple(_pullback(row, transform) for row in action.transition)
            row = _pullback(action.sensor, updated)
            more = slabs + ((row, action.half_width),)
            schedule = word + (index,)
            score, hidden = central_radius(box, target, more)
            if (score, len(schedule), schedule) < (best[0], len(best[1]), best[1]):
                best = (score, schedule, hidden)
            if score:
                pending.append((schedule, remaining - action.cost, updated, more))
    return best
