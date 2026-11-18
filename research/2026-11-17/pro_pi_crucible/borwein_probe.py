"""Exact rational checks for the swept Borwein inverse instrument.

Finite certificates only. No asymptotic assertion about pi is computed here.
The interior-point polynomial-interpolation maximizer is separately implemented
from the parent PR's endpoint/midpoint interpolation. Both share the same
piecewise-quadratic mathematical method.
"""
from collections import defaultdict
from fractions import Fraction as F

C = F(162, 289)
DELTA = F(1, 18)
MEAN = F(256, 7803)


def frac(x):
    x = F(x)
    return x - x.numerator // x.denominator


def signed_wrap(x):
    return frac(x + F(1, 2)) - F(1, 2)


def leak(x):
    return C * max(F(), abs(signed_wrap(x)) - DELTA) ** 2


def leak_derivative(x):
    w = signed_wrap(x)
    if abs(w) == F(1, 2):
        raise ValueError("antipodal derivative is not single valued")
    return 2*C*max(F(), abs(w)-DELTA)*(1 if w >= 0 else -1)


def probability(points, weights=None):
    if not points:
        raise ValueError("nonempty probability required")
    if weights is None:
        weights = [F(1, len(points))] * len(points)
    if len(points) != len(weights):
        raise ValueError("point/weight length mismatch")
    data = defaultdict(F)
    for x, w in zip(points, weights):
        if F(w) < 0:
            raise ValueError("negative probability")
        data[frac(F(x))] += F(w)
    if sum(data.values(), F()) != 1:
        raise ValueError("probability mass must be one")
    return tuple(sorted((x, w) for x, w in data.items() if w))


def response(mu, alpha):
    return sum((w*leak(alpha-x) for x, w in mu), F())


def response_derivative(mu, alpha):
    return sum((w*leak_derivative(alpha-x) for x, w in mu), F())


def exact_sweep(mu):
    """Return (sup discrepancy, extremizing origin, candidate count)."""
    breaks = {F(), F(1)}
    for x, _ in mu:
        breaks.update((frac(x-DELTA), frac(x+DELTA), frac(x+F(1, 2))))
    breaks = sorted(breaks)
    candidates = set(breaks)
    for left, right in zip(breaks, breaks[1:]):
        step = (right-left)/4
        mid = (right+left)/2
        v1, v2, v3 = (response(mu, mid+j*step) for j in (-1, 0, 1))
        a = (v1+v3-2*v2)/(2*step*step)
        b = (v3-v1)/(2*step)
        if a < 0:
            raise AssertionError("kernel is convex between breakpoints")
        if a:
            vertex = mid-b/(2*a)
            if left < vertex < right:
                candidates.add(vertex)
    best, origin = max((abs(response(mu, t)-MEAN), t) for t in candidates)
    return best, origin, len(candidates)


def arc_discrepancy(mu):
    cumulative = F()
    extremes = [F()]
    for x, w in mu:
        extremes.append(cumulative-x)
        cumulative += w
        extremes.append(cumulative-x)
    return max(extremes)-min(extremes)


def interval_discrepancy(mu, left, right):
    if not 0 <= left < right <= 1:
        raise ValueError("use an ordinary interval inside [0,1]")
    if any(x in (left, right) for x, _ in mu):
        raise ValueError("endpoint atom: use a one-sided limit")
    return sum((w for x, w in mu if left < x < right), F())-(right-left)


def p_interval_discrepancy(mu, left, right):
    total = F()
    for x, w in mu:
        center = x+F(1, 2)
        overlap = F()
        for k in range(-2, 3):
            lo, hi = center-DELTA+k, center+DELTA+k
            overlap += max(F(), min(right, hi)-max(left, lo))
        total += w*overlap/(2*DELTA)
    return total-(right-left)


def inverse_interval_sides(mu, left, right):
    lhs = interval_discrepancy(mu, left, right)
    lhs += p_interval_discrepancy(mu, left, right)/8
    rhs = -F(289, 288)*(response_derivative(mu, right-F(1, 2))
                        - response_derivative(mu, left-F(1, 2)))
    return lhs, rhs


def forcing(n):
    if n < 1:
        raise ValueError("source clock begins at one")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def terminal(n):
    u = F()
    for j in range(1, n+1):
        u = 16*u+forcing(j)
    return u


def source_certificate(b):
    u = terminal(2*b)
    mu = probability([u/16**k for k in range(1, b+1)])
    sweep, origin, count = exact_sweep(mu)
    error = F(16, 7225*b)*forcing(2*b+1)
    return {
        "B": b, "source": "literal_four_poles_zero_seed",
        "sweep": str(sweep), "extremizing_origin": str(origin),
        "candidates": count, "tail_error_bound": str(error),
        "completed_arc_discrepancy_squared_upper": str(F(1156, 49)*(sweep+error)),
        "rational_shadow_arc_discrepancy": str(arc_discrepancy(mu)),
        "asymptotic_claim": False,
    }
