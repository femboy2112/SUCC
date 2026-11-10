"""Finite CFS-5 history-fiber certificate: prediction error AND prime leakage."""
from collections import defaultdict
from math import isqrt
from fractions import Fraction as Q
from intervals import SCALE, ZERO, ONE, Interval, Box, mean
from observational_succ.selected_orbit import original_forcing


def authenticate_history(states):
    """Full unwrapped original source verification; no trusted source tag."""
    if not states or any(type(s) is not Q for s in states) or states[0] != 0:
        raise ValueError('literal-zero exact rational history required')
    for n in range(1, len(states)):
        if states[n] != 16*states[n-1]+original_forcing(n):
            raise ValueError(f'original unwrapped source mismatch at time {n}')
    return True


def unit_energy(interval):
    """Intersect with a mathematically proved [0,1] energy constraint."""
    return Interval(max(0, interval.lo), min(SCALE, interval.hi))


def sqrt_box(interval):
    if interval.lo < 0:
        raise ValueError('nonnegative interval required')
    low = isqrt(interval.lo*SCALE)
    high = isqrt(interval.hi*SCALE)
    if high*high < interval.hi*SCALE:
        high += 1
    return Interval(low, high)


def certificate(a, b, labels):
    """Conditional on a,b being unit characters, prove the CFS-5 norm bound.

    Boxes are rigorous enclosures, not exact unit-vector witnesses by themselves.
    Callers must establish unit modulus from their rational phase construction.
    This function does not authenticate a source; authenticate_history does.
    """
    if not a or len(a) != len(b) or len(a) != len(labels):
        raise ValueError('equal nonempty sequence lengths required')
    cells = defaultdict(list)
    for j, label in enumerate(labels):
        cells[label].append(j)
    a0, b0 = mean(a), mean(b)
    ea, eb = ZERO, ZERO
    for indices in cells.values():
        w = Interval.ratio(len(indices), len(a))
        ea = ea+w*mean(a[j] for j in indices).norm_squared()
        eb = eb+w*mean(b[j] for j in indices).norm_squared()
    a0e, b0e = a0.norm_squared(), b0.norm_squared()
    d2 = unit_energy(ea-a0e)
    r2 = unit_energy(ONE-ea)
    t2 = unit_energy(eb-b0e)
    eta2 = unit_energy(ONE-eb)
    retained = sqrt_box(d2*t2)
    residual = sqrt_box(r2*eta2)
    covariance_bound = retained+residual
    mean_product = sqrt_box((a0*b0).norm_squared())
    full_bound = covariance_bound+mean_product
    return {'cells': len(cells), 'samples': len(a),
            'prime_leakage_squared': d2.as_list(), 'prime_residual_squared': r2.as_list(),
            'complement_model_squared': t2.as_list(), 'complement_residual_squared': eta2.as_list(),
            'retained_term': retained.as_list(), 'residual_term': residual.as_list(),
            'covariance_bound_expression': covariance_bound.as_list(),
            'full_bound_expression': full_bound.as_list()}
