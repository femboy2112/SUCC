"""Exact tools for general two-entry Lonely Runner speed bounds.

All universal claims are proved in research/2026-10-28/lonely_runner/GAMMA.md.
The routines below produce rational witnesses, interval gaps and effective
search bounds. They do not classify the remaining tight configurations.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd

from observational_succ.lonely_runner_deletion import exact_deletion_value, sharp_minimum


def _integer(x):
    if type(x) is not int:
        raise TypeError("an integer excluding booleans is required")


def _domain(n, r1, r2):
    for x in (n, r1, r2):
        _integer(x)
    if n < 5 or not (n - 1 < 2 * r1 < 2 * r2 <= 2 * (n - 1)):
        raise ValueError("require n>=5 and (n-1)/2<r1<r2<=n-1")


def _all_domain(n, r1, r2):
    for x in (n, r1, r2):
        _integer(x)
    if n < 5 or not 1 <= r1 < r2 <= n - 1:
        raise ValueError("require n>=5 and 1<=r1<r2<=n-1")


def all_retained(n, r1, r2):
    """Retained baseline for arbitrary two distinct deletions."""
    _all_domain(n, r1, r2)
    return tuple(i for i in range(1, n) if i not in (r1, r2))


def _exact(x):
    if type(x) not in (int, F):
        raise TypeError("an exact integer or Fraction is required")
    return F(x)


def circle_distance(x):
    x = _exact(x) % 1
    return min(x, 1 - x)


def retained(n, r1, r2):
    _domain(n, r1, r2)
    return tuple(i for i in range(1, n) if i not in (r1, r2))


def safe_radius(n, r):
    """Radius about 1/r on which every undeleted baseline speed is safe."""
    for x in (n, r):
        _integer(x)
    if n < 3 or not (n - 1 < 2 * r <= 2 * (n - 1)):
        raise ValueError("the removed speed must lie in the upper half")
    return F(n - r, n * r * (n - 1))


@dataclass(frozen=True)
class SingleInsertHole:
    n: int
    r1: int
    r2: int
    inserted: int
    time: F
    margin: F
    strategy: str

    def verify(self):
        speeds = all_retained(self.n, self.r1, self.r2) + (self.inserted,)
        return (type(self.inserted) is int and self.inserted >= self.n
                and type(self.time) is F and 0 <= self.time <= 1
                and type(self.margin) is F
                and self.margin == min(circle_distance(v * self.time) for v in speeds)
                and self.margin > F(1, self.n))


def single_insert_hole(n, r1, r2, inserted):
    """Construct an exact strict hole after adding ANY single speed >=n.

    This handles the shared-multiple collision, not just distinct assignments
    of replacement speeds to removed centres.
    """
    speeds = retained(n, r1, r2)
    _integer(inserted)
    if inserted < n:
        raise ValueError("inserted speed must be at least n")
    if inserted % r1:
        time, strategy = F(1, r1), "first nonmultiple centre"
    elif inserted % r2:
        time, strategy = F(1, r2), "second nonmultiple centre"
    else:
        left = F(1, n * inserted)
        right = min(safe_radius(n, r1), F(n - 1, n * inserted))
        if not left < right:
            raise ArithmeticError("common-multiple interval contradicted the proved inequality")
        time = F(1, r1) + (left + right) / 2
        strategy = "common-multiple escape"
    margin = min(circle_distance(v * time) for v in speeds + (inserted,))
    return SingleInsertHole(n, r1, r2, inserted, time, margin, strategy)


def periodic_occupancy(n, velocity, left, right):
    """Exact length of {t in [left,right]: ||velocity*t||<=1/n}."""
    for x in (n, velocity):
        _integer(x)
    if n < 3 or velocity < 1:
        raise ValueError("require n>=3 and positive velocity")
    left, right = _exact(left), _exact(right)
    if right < left:
        raise ValueError("interval endpoints are reversed")
    delta = F(1, n)

    def primitive(x):
        whole = x.numerator // x.denominator
        part = x - whole
        return 2 * delta * whole + min(part, delta) + max(F(0), part - (1 - delta))

    return (primitive(velocity * right) - primitive(velocity * left)) / velocity


def occupancy_upper_bound(n, velocity, length):
    """Sharp phase-uniform additive discrepancy bound for one periodic band."""
    for x in (n, velocity):
        _integer(x)
    length = _exact(length)
    if n < 3 or velocity < 1 or length < 0:
        raise ValueError("require n>=3, positive velocity and nonnegative length")
    return 2 * length / n + F(2 * (n - 2), n * n * velocity)


def uncovered_intervals(n, speeds, *, max_intervals=250000):
    """Exact components of the complement of all radius-1/n bad bands.

    A computational budget is explicit and raises rather than manufacturing
    a negative result. Endpoints of returned open intervals are rational.
    """
    _integer(n)
    _integer(max_intervals)
    speeds = tuple(speeds)
    for v in speeds:
        _integer(v)
    if n < 3 or not speeds or min(speeds) < 1 or len(set(speeds)) != len(speeds):
        raise ValueError("require n>=3 and distinct positive speeds")
    if max_intervals < 1 or sum(speeds) + len(speeds) > max_intervals:
        raise ValueError("exact interval enumeration budget exceeded")
    intervals = []
    for v in speeds:
        for k in range(v + 1):
            intervals.append((max(F(0), F(k * n - 1, n * v)),
                              min(F(1), F(k * n + 1, n * v))))
    frontier, gaps = F(0), []
    for left, right in sorted(intervals):
        if left > frontier:
            gaps.append((frontier, left))
        frontier = max(frontier, right)
    if frontier < 1:
        gaps.append((frontier, F(1)))
    return tuple(gaps)


def effective_bounds(n, r1, r2):
    """Necessary integer search bounds for every cover in the stated family.

    If LR(V)<=1/n, then w1<first_strict_bound and
    w2<=2(n-1)*w1. Thus the listed integer upper bounds are rigorous.
    They are not evidence that any pair below them is tight.
    """
    _domain(n, r1, r2)
    bound = F(2 * (n - 2) * r1 * (n - 1), (n - 4) * (n - r1))
    w1_max = (bound.numerator - 1) // bound.denominator
    return {
        "first_strict_bound": bound,
        "w1_max": w1_max,
        "second_multiplier": 2 * (n - 1),
        "w2_max": 2 * (n - 1) * w1_max,
        "universal_strict_bound": 4 * n**3,
    }


def general_effective_bounds(n, r1, r2):
    """Unrestricted two-deletion bound, using Alpha and one-entry classification.

    Use the stronger retained-safe interval obtained from the exact deletion
    margin. The endpoint-only bound is returned separately as an audit route.
    Every all-time 1/n cover has w2<=2(n-1)w1 and w2<4n^3.
    """
    _all_domain(n, r1, r2)
    margin = max(exact_deletion_value(n, r1), exact_deletion_value(n, r2))
    bound = F(2 * (n - 2) * (n - 1), n * (n - 4)) / (margin - F(1, n))
    uniform_margin = sharp_minimum(n)[0]
    uniform_bound = F(2 * (n - 2) * (n - 1), n * (n - 4)) / (uniform_margin - F(1, n))
    w1_max = (bound.numerator - 1) // bound.denominator
    return {
        "deletion_margin": margin,
        "first_strict_bound": bound,
        "uniform_first_strict_bound": uniform_bound,
        "endpoint_first_strict_bound": F(4 * (n - 2) * (n - 1)**2, n - 4),
        "w1_max": w1_max,
        "second_multiplier": 2 * (n - 1),
        "w2_max": 2 * (n - 1) * w1_max,
        "universal_strict_bound": 4 * n**3,
    }


def general_single_insert_hole(n, r1, r2, inserted, *, max_intervals=250000):
    """Find a rational hole for arbitrary deletions by exact interval geometry.

    The universal existence theorem uses Zhang's classification; this finite
    routine independently checks actual bands and has an explicit work budget.
    """
    speeds = all_retained(n, r1, r2)
    _integer(inserted)
    if inserted < n:
        raise ValueError("inserted speed must be at least n")
    gaps = uncovered_intervals(n, speeds + (inserted,), max_intervals=max_intervals)
    if not gaps:
        raise ArithmeticError("source bands contradict the proved one-insertion hole theorem")
    a, b = gaps[0]
    time = (a + b) / 2
    margin = min(circle_distance(v * time) for v in speeds + (inserted,))
    return SingleInsertHole(n, r1, r2, inserted, time, margin, "exact general interval hole")


def centre_divisibility(n, r1, r2, w1, w2):
    """Necessary centre condition, allowing one common-multiple replacement."""
    _domain(n, r1, r2)
    for w in (w1, w2):
        _integer(w)
    if not n <= w1 < w2:
        raise ValueError("require n<=w1<w2")
    return all(w1 % r == 0 or w2 % r == 0 for r in (r1, r2))
