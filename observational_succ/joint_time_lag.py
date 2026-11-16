"""Finite signed time–lag instruments, with exact BBP completion budgets.

The all-scale statistical estimate is OPEN. Certificates here concern only
their finite input; character authority is the existing rational Machin/Taylor
enclosure. No floating pi value or distribution assumption is used.
"""
from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache

from .duck_bbp import forcing
from .oily_signed_certificate import Interval, ZERO, character_enclosure


def _int(value, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError("ordinary integer outside the declared domain")
    return value


def _frequency(h):
    if type(h) is not int or h == 0:
        raise ValueError("nonzero ordinary integer frequency required")
    return h


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact rational required")
    return Q(value)


def _units(values):
    values = tuple((_rational(a), _rational(b)) for a, b in values)
    if not values or any(a*a+b*b != 1 for a, b in values):
        raise ValueError("nonempty exact Gaussian unit sequence required")
    return values


def gaussian_correlations(values, upto):
    """c_l=N^-1 sum_(n<N-l) z_(n+l) conj(z_n), zero padded.

    Both signed coordinates survive. Lags >= N have empty sums.
    """
    values = _units(values)
    _int(upto)
    n = len(values)
    result = []
    for lag in range(upto):
        real = imag = Q()
        for j in range(max(0, n-lag)):
            a, b = values[j+lag]
            c, d = values[j]
            real += a*c+b*d
            imag += b*c-a*d
        result.append((real/n, imag/n))
    return tuple(result)


def signed_fejer(values, length):
    """Exact signed normalized padded-window energy F_(N,H)."""
    _int(length)
    corr = gaussian_correlations(values, length)
    return Q(1, length) + sum(
        (Q(2*(length-lag), length**2)*corr[lag][0]
         for lag in range(1, length)), Q())


def schur_fejer(values, length):
    """Fejer response of the positive-definite sequence |c_l|^2."""
    _int(length)
    corr = gaussian_correlations(values, length)
    return Q(1, length) + sum(
        (Q(2*(length-lag), length**2)*(a*a+b*b)
         for lag, (a, b) in enumerate(corr[1:], 1)), Q())


def squared_mean(values):
    values = _units(values)
    a = sum((v[0] for v in values), Q())
    b = sum((v[1] for v in values), Q())
    return (a*a+b*b)/len(values)**2


def centered(value):
    value = _rational(value)
    return value - (value+Q(1, 2)).__floor__()


def inverse_lag_certificate(delta, count, epsilon):
    """Authenticate a finite rational instance of inverse lag stability.

    delta is the difference of two completed starting phases. The records
    compare their adjacent-lag phases. This does not infer that either phase
    is the authentic zero-selected BBP point.
    """
    delta = _rational(delta)
    _int(count)
    epsilon = _rational(epsilon)
    if not 0 <= epsilon < Q(1, 17):
        raise ValueError("requires 0 <= epsilon < 1/17")
    u = tuple(centered(15*16**n*delta) for n in range(count))
    if any(abs(v) > epsilon for v in u):
        raise ValueError("lag observations exceed the prescribed tolerance")
    if any(u[n+1] != 16*u[n] for n in range(count-1)):
        raise ArithmeticError("expansivity contradiction")
    k = (15*delta-u[0])
    if k.denominator != 1:
        raise ArithmeticError("nonintegral alias")
    k = int(k) % 15
    budgets = tuple(epsilon/(15*16**(count-1-n)) for n in range(count))
    residuals = tuple(centered(16**n*delta-Q(k, 15)) for n in range(count))
    if any(abs(v) > b for v, b in zip(residuals, budgets)):
        raise ArithmeticError("target inverse-stability inequality failed")
    anchored = abs(centered(delta)) <= Q(1, 30)
    if anchored and k != 0:
        raise ArithmeticError("coarse anchor did not separate aliases")
    return {"alias": k, "anchored": anchored, "residuals": residuals,
            "budgets": budgets,
            "mean_character_error_upper": Q(32*22, 7*225*count)*epsilon,
            "original_zero_authenticated": False}


def source_fejer_transport_upper(start, length, h=1):
    """π<22/7 upper for |F_U-F_Y|, a finite all-lag source budget.

    Endpoint telescoping gives sum_(B<=n<2B-l)(T_n-T_(n+l))
    <= 3l/(256 B^2). The Fejer triangular sum is exact.
    """
    _int(start)
    _int(length)
    h = _frequency(h)
    if length > start:
        raise ValueError("requires length <= shell size")
    return Q(22*abs(h)*(length**2-1), 7*128*length*start**3)


def source_mean_transport_upper(start, h=1):
    _int(start)
    h = _frequency(h)
    return Q(22*abs(h), 7*32*start**2)


@lru_cache(maxsize=8, typed=True)
def authentic_circle_path(horizon):
    """Exact original-zero four-pole rational orbit, reduced after each step."""
    _int(horizon, 0)
    values = [Q()]
    for n in range(1, horizon+1):
        values.append((16*values[-1]+forcing(n)) % 1)
    return tuple(values)


@lru_cache(maxsize=32, typed=True)
def source_character_shell(start, h=1, bits=48, order=16):
    _int(start)
    _frequency(h)
    _int(bits, 8)
    _int(order)
    path = authentic_circle_path(2*start-1)
    return tuple(character_enclosure(h*v, bits, order)
                 for v in path[start:2*start])


def padded_window_energy(rectangles, length):
    """O(N+H) rectangle enclosure of sum_m |sum_(j<H) z_(m+j)|²/(NH²).

    Prefix sums of endpoint arrays avoid treating a removed observation as
    independent noise. Squaring takes place AFTER the signed window sum.
    """
    rectangles = tuple(rectangles)
    n = len(rectangles)
    _int(length)
    if not n:
        raise ValueError("nonempty observation sequence required")
    endpoints = [[Q()] for _ in range(4)]
    for real, imag in rectangles:
        if not isinstance(real, Interval) or not isinstance(imag, Interval):
            raise ValueError("certified rectangular intervals required")
        for row, value in zip(endpoints, (real.lower, real.upper,
                                         imag.lower, imag.upper)):
            row.append(row[-1]+value)
    result = ZERO
    for m in range(1-length, n):
        a, b = max(0, m), min(n, m+length)
        real = Interval(endpoints[0][b]-endpoints[0][a],
                        endpoints[1][b]-endpoints[1][a])
        imag = Interval(endpoints[2][b]-endpoints[2][a],
                        endpoints[3][b]-endpoints[3][a])
        result = result + real.square() + imag.square()
    return result.scale(Q(1, n*length**2))


def _expand(interval, radius):
    return Interval(interval.lower-radius, interval.upper+radius)


def source_shell_certificate(start, length, h=1, bits=48, order=16):
    """Actual finite shell: signed Fejer and mean enclosures, paid completion.

    The mean-modulus result is an upper bound for its SQUARE. The source
    budget is an analytic inequality, not a numerical estimate of a tail.
    """
    debt = source_fejer_transport_upper(start, length, h)
    rects = source_character_shell(start, h, bits, order)
    raw = padded_window_energy(rects, length)
    completed = Interval(max(Q(), raw.lower-debt), raw.upper+debt)
    factor = Q(start+length-1, start)
    mean_raw = tuple(sum((r[k] for r in rects), ZERO).scale(Q(1, start))
                     for k in range(2))
    mean_debt = source_mean_transport_upper(start, h)
    mean_completed = tuple(_expand(v, mean_debt) for v in mean_raw)
    return {"start": start, "length": length, "frequency": h,
            "bits": bits, "order": order,
            "rational_fejer": raw, "completed_fejer": completed,
            "fejer_transport_upper": debt,
            "rational_mean": mean_raw, "completed_mean": mean_completed,
            "completed_mean_modulus_squared_upper":
                min(Q(1), factor*completed.upper),
            "original_zero_authenticated": True,
            "infinite_cancellation_proved": False}
