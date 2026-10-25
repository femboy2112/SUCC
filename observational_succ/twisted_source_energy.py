"""Signed temporal energy of the authentic BBP source, with exact enclosures.

The elementary zero-extension/van der Corput identity is classical. The
instrument retains signs, time endpoints and the source's Green-tail budget.
No finite result returned here is an asymptotic normality certificate.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .pi_source_collision import prime_window, tail_upper
from .pi_source_genesis import ComplexBox, character_interval


def _integer(value, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("integer outside the declared domain")
    return value


def _exact(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _gaussian(value):
    if not isinstance(value, (tuple, list)) or len(value) != 2:
        raise ValueError("a real/imaginary exact pair is required")
    return _exact(value[0]), _exact(value[1])


def _square(z):
    return z[0]*z[0]+z[1]*z[1]


def _product_conjugate(z, w):
    return z[0]*w[0]+z[1]*w[1], z[1]*w[0]-z[0]*w[1]


def exact_energy_identity(values, width):
    """Two independently arranged exact sides, plus the finite mean bound.

    Values are Gaussian rationals. The identity and inequality allow arbitrary
    values; no unverified unit-modulus premise is accepted or needed.
    """
    z = tuple(_gaussian(x) for x in values)
    n = len(z)
    _integer(width, 1)
    if not n or width > n:
        raise ValueError("requires 1 <= width <= nonempty sample length")
    diagonal = sum((_square(x) for x in z), Q())
    correlations = []
    for lag in range(1, width):
        terms = [_product_conjugate(z[t+lag], z[t]) for t in range(n-lag)]
        correlations.append((sum((x[0] for x in terms), Q()),
                             sum((x[1] for x in terms), Q())))
    lag_side = width*diagonal+2*sum(
        ((width-d)*correlations[d-1][0] for d in range(1, width)), Q())
    block_side = Q()
    for start in range(1-width, n):
        block = z[max(0, start):min(n, start+width)]
        block_side += _square((sum((x[0] for x in block), Q()),
                               sum((x[1] for x in block), Q())))
    mean_sq = _square((sum((x[0] for x in z), Q())/n,
                       sum((x[1] for x in z), Q())/n))
    energy = block_side/(n*width**2)
    upper = Q(n+width-1, n)*energy
    return {"lag_side": lag_side, "block_side": block_side,
            "correlations": tuple(correlations), "energy": energy,
            "mean_squared": mean_sq, "mean_squared_upper": upper}


def _interval_square(low, high):
    lower = Q() if low <= 0 <= high else min(low*low, high*high)
    return lower, max(low*low, high*high)


def _box_square(box):
    a, b = _interval_square(box.real_low, box.real_high)
    c, d = _interval_square(box.imag_low, box.imag_high)
    return a+c, b+d


def _scale_box(box, value):
    if value < 0:
        raise ValueError("nonnegative scaling required")
    return ComplexBox(box.real_low*value, box.real_high*value,
                      box.imag_low*value, box.imag_high*value)


def phase_boxes(phases, frequency=1, *, order=16, bits=90):
    """Outward phase boxes; true pi comes from inherited Machin intervals.

    Quantizing the input outward prevents large source denominators from
    growing through Taylor powers. The quantization error is charged by the
    inherited interval routine, and each final box is rounded outward again.
    """
    _integer(frequency)
    _integer(order, 1)
    _integer(bits, 1)
    values = tuple(_exact(x) for x in phases)
    if not values:
        raise ValueError("nonempty sample required")
    return tuple(character_interval(frequency*x, frequency*x,
                                    order=order, bits=bits).outward(bits)
                 for x in values)


def energy_intervals(boxes, widths):
    """Certified zero-extended block energies and direct mean square.

    Every input box must enclose a unit complex phase. This premise is paid by
    phase_boxes in the source entry point, not asserted from arbitrary boxes.
    The returned global inequality uses the exact finite endpoint factor.
    """
    boxes = tuple(boxes)
    n = len(boxes)
    if not n or any(not isinstance(x, ComplexBox) for x in boxes):
        raise ValueError("nonempty ComplexBox sequence required")
    widths = tuple(widths)
    if not widths:
        raise ValueError("at least one width required")
    for width in widths:
        _integer(width, 1)
        if width > n:
            raise ValueError("width exceeds sample length")
    zero = ComplexBox(Q(), Q(), Q(), Q())
    prefix = [zero]
    for box in boxes:
        for bound in (box.real_low, box.real_high, box.imag_low, box.imag_high):
            _exact(bound)
        if box.real_low > box.real_high or box.imag_low > box.imag_high:
            raise ValueError("reversed box")
        prefix.append(prefix[-1]+box)
    mean = _scale_box(prefix[-1], Q(1, n))
    direct_lo, direct_hi = _box_square(mean)
    rows = []
    for width in widths:
        lower = upper = Q()
        # Prefix subtraction is outward even though overlapping errors are
        # correlated. We deliberately pay the harmless extra interval width.
        for start in range(1-width, n):
            box = prefix[min(n, start+width)]-prefix[max(0, start)]
            lo, hi = _box_square(box)
            lower += lo
            upper += hi
        lower /= n*width**2
        upper /= n*width**2
        factor = Q(n+width-1, n)
        rows.append({"width": width, "energy_low": lower,
                     "energy_high": upper,
                     "mean_squared_upper": factor*upper})
    return {"length": n, "direct_mean_squared_low": direct_lo,
            "direct_mean_squared_high": direct_hi, "rows": rows}


def green_energy_budget(start, length, frequency=1):
    """All-width |E(source)-E(pi shadow)| bound, independent of lag.

    |e(h*x)-e(h*y)| <= (44/7)|h| T_n. Each sample enters width
    blocks and each block has norm <= width, giving (2/N)*sum errors.
    """
    _integer(start, 1)
    _integer(length, 1)
    _integer(frequency)
    return Q(88*abs(frequency), 7*length)*sum(
        (tail_upper(n) for n in range(start, start+length)), Q())


def source_energy_report(prime, frequency=1, widths=(2, 4, 8, 16)):
    """Full authentic first-prime window; prescribed finite probe only."""
    _integer(frequency)
    window = prime_window(prime)
    widths = tuple(widths)
    for width in widths:
        _integer(width, 1)
    selected = tuple(width for width in widths if width <= window.length)
    result = energy_intervals(phase_boxes(window.states, frequency), selected)
    result.update({"prime": prime, "frequency": frequency,
                   "start_state": window.start+1, "period": window.period,
                   "green_energy_budget": green_energy_budget(
                       window.start+1, window.length, frequency)})
    return result
