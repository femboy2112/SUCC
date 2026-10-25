"""Exact source enclosures, selection memory, and finite mixing budgets.

The statistical limit of the selected pi orbit is not asserted. The measured
observable x(1-x) is continuous and 1-Lipschitz on the circle, so its rational
integrals give an independent finite check of the Wasserstein paper bounds.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .pi_source_collision import bbp_forcing, tail_upper


def _integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError("integer outside the declared domain")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


@dataclass(frozen=True)
class RationalInterval:
    left: Q
    right: Q

    def __post_init__(self):
        object.__setattr__(self, "left", _rational(self.left))
        object.__setattr__(self, "right", _rational(self.right))
        if self.left >= self.right:
            raise ValueError("positive interval length required")

    @property
    def length(self):
        return self.right-self.left


def cylinder_interval(base, depth, point):
    """The canonical half-open base cylinder containing an exact point."""
    _integer(base, 2)
    _integer(depth)
    x = _rational(point) % 1
    scale = base**depth
    cell = (scale*x)//1
    return RationalInterval(Q(cell, scale), Q(cell+1, scale))


def bbp_selector_interval(depth):
    """Nested rational enclosure of alpha=pi/16 from the original forcing.

    These are uncertainty enclosures of one selected source. They are not
    ensembles of different exact BBP solutions with the same initial zero.
    """
    _integer(depth)
    left = sum((bbp_forcing(j)/16**j for j in range(1, depth+1)), Q())
    return RationalInterval(left, left+tail_upper(depth)/16**depth)


def periodic_parabola(point):
    x = _rational(point) % 1
    return x*(1-x)


def _periodic_primitive(point):
    point = _rational(point)
    integer = point//1
    x = point-integer
    return Q(integer, 6)+x*x/2-x*x*x/3


def interval_observable_mean(interval, base, time):
    """Integrate x(1-x) after multiplication, including every wrap exactly."""
    if not isinstance(interval, RationalInterval):
        raise ValueError("RationalInterval required")
    _integer(base, 2)
    _integer(time)
    scale = base**time
    a, b = scale*interval.left, scale*interval.right
    return (_periodic_primitive(b)-_periodic_primitive(a))/(b-a)


def interval_time_average(interval, base, horizon):
    _integer(horizon, 1)
    return sum((interval_observable_mean(interval, base, t)
                for t in range(horizon)), Q())/horizon


def orbit_observable_mean(point, base, horizon):
    _integer(base, 2)
    _integer(horizon, 1)
    x = _rational(point) % 1
    total = Q()
    for _ in range(horizon):
        total += x*(1-x)
        x = (base*x) % 1
    return total/horizon


def interval_haar_tv(interval, base, time):
    """Exact TV distance (half L1) of a wrapped uniform interval from Haar."""
    if not isinstance(interval, RationalInterval):
        raise ValueError("RationalInterval required")
    _integer(base, 2)
    _integer(time)
    length = base**time*interval.length
    remainder = length % 1
    return remainder*(1-remainder)/length


def cylinder_mixture_report(base, depth, point, horizon):
    """Finite observation of the proved selected-prefix/Haar mixture law."""
    _integer(horizon, 1)
    interval = cylinder_interval(base, depth, point)
    selected = min(depth, horizon)
    actual = interval_time_average(interval, base, horizon)
    mixture = Q(horizon-selected, 6*horizon)
    if selected:
        mixture += Q(selected, horizon)*orbit_observable_mean(
            point, base, selected)
    bound = Q(base**selected-1,
              2*horizon*(base-1)*base**depth)
    return dict(base=base, depth=depth, horizon=horizon,
                selected_steps=selected, selected_fraction=Q(selected, horizon),
                interval_mean=actual, mixture_mean=mixture,
                absolute_error=abs(actual-mixture), wasserstein_budget=bound,
                selection_mass=Q(1, base**depth),
                normalized_density_l2_squared=base**depth)


def _ceil_log(base, integer):
    _integer(base, 2)
    _integer(integer, 1)
    power, depth = 1, 0
    while power < integer:
        power *= base
        depth += 1
    return depth


def bbp_selection_budget(depth, horizon):
    """Uniform O(1/N) mixture budget at the effective BBP selection depth.

    L=min(N,K+ceil(log_16((8K+1)(8K+2)))). The mixture has weight
    L/N on the first L points of the genuine alpha=pi/16 orbit, and the
    remaining weight on Haar. The selected orbit's law is still unknown.
    """
    _integer(depth)
    _integer(horizon, 1)
    interval = bbp_selector_interval(depth)
    denominator = (8*depth+1)*(8*depth+2)
    extra = _ceil_log(16, denominator)
    effective = depth+extra
    selected = min(horizon, effective)
    early = interval.length*Q(16**selected-1, 30*horizon)
    late = sum((interval_haar_tv(interval, 16, t)
                for t in range(selected, horizon)), Q())/(2*horizon)
    late_geometric = Q(2, 15*horizon) if horizon > effective else Q()
    return dict(source_depth=depth, horizon=horizon,
                extra_selected_steps=extra, effective_depth=effective,
                selected_steps=selected, selected_fraction=Q(selected, horizon),
                interval=interval, early_budget=early,
                exact_late_tv_budget=late,
                geometric_late_budget=late_geometric,
                total_budget=early+late,
                uniform_budget=Q(2, 3*horizon),
                normalized_density_l2_squared=1/interval.length,
                interval_mean=interval_time_average(interval, 16, horizon))


def parabola_range(interval):
    """Exact range on a real interval of the periodic calibration observable."""
    if not isinstance(interval, RationalInterval):
        raise ValueError("RationalInterval required")
    if interval.length >= 1:
        return Q(), Q(1, 4)
    values = [periodic_parabola(interval.left), periodic_parabola(interval.right)]
    first = (2*interval.left)//1
    last = (2*interval.right)//1
    for k in range(first, last+2):
        x = Q(k, 2)
        if interval.left <= x <= interval.right:
            values.append(periodic_parabola(x))
    return min(values), max(values)


def orbit_observable_enclosure(point_interval, base, horizon):
    """Independent rigorous observable enclosure from an interval for a point."""
    if not isinstance(point_interval, RationalInterval):
        raise ValueError("RationalInterval required")
    _integer(base, 2)
    _integer(horizon, 1)
    low = high = Q()
    for t in range(horizon):
        scale = base**t
        a, b = parabola_range(RationalInterval(
            scale*point_interval.left, scale*point_interval.right))
        low += a
        high += b
    return low/horizon, high/horizon


def signed_product_variation(weights, depth):
    """Finite coherent product weights; bounded variation is a separate gate."""
    _integer(depth)
    if not isinstance(weights, (tuple, list)):
        raise ValueError("explicit tuple or list of weights required")
    weights = tuple(_rational(x) for x in weights)
    if not weights or sum(weights, Q()) != 1:
        raise ValueError("nonempty normalized exact weight vector required")
    return sum((abs(x) for x in weights), Q())**depth
