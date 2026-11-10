"""Signed finite-lag energy in the authenticated phase frame.

Reuses the pinned, separately audited outward integer rectangle instrument.
The identities are deterministic; no probability model is used.
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRIOR = HERE.parent / 'covariance_forge'
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(PRIOR))
from intervals import Box, Interval, ZERO, ONE, SCALE, phase, mean


def aperture(H, A):
    if type(H) is not int or type(A) is not int or not 1 <= H <= A:
        raise ValueError('integer aperture 1 <= H <= A required')


def sliding_energy(values, H):
    """Zero-extended energy, including BOTH incomplete boundary windows."""
    A = len(values)
    aperture(H, A)
    total = ZERO
    window = Box()
    # t=-(H-1),...,A-1; the entering index is t+H-1.
    for t in range(1-H, A):
        entering = t+H-1
        leaving = t-1
        if 0 <= entering < A:
            window = window + values[entering]
        if 0 <= leaving < A:
            window = window - values[leaving]
        total = total + window.norm_squared()
    return total.divide(A*H*H)


def lag_means(values, H):
    A = len(values)
    aperture(H, A)
    return [mean(values[n+l]*values[n].conjugate() for n in range(A-l))
            * Box(Interval.ratio(A-l, A)) for l in range(1, H)]


def energy_from_lags(lags, H, diagonal=ONE):
    """diagonal=E|z|²; ONE is valid only for exact unit phases."""
    if type(H) is not int or H < 1 or len(lags) < H-1:
        raise ValueError('enough lags for positive integer aperture required')
    signed = ZERO
    unsigned = ZERO
    for l in range(1, H):
        weight = Interval.ratio(2*(H-l), H*H)
        value = lags[l-1].re
        signed = signed + weight*value
        absolute = Interval(0 if value.lo <= 0 <= value.hi else min(abs(value.lo), abs(value.hi)),
                            max(abs(value.lo), abs(value.hi)))
        unsigned = unsigned + weight*absolute
    return diagonal.divide(H)+signed, diagonal.divide(H)+unsigned


def signed_transport(local, full_lag):
    """v = full_lag * conjugate(local), requiring exact |local|=1.

    Returns the bilinear covariance and its marginal product. This construct
    retains the exact chronological forcing in full_lag. Its validity is
    checked independently against rational source differences by the runner.
    """
    if not local or len(local) != len(full_lag):
        raise ValueError('equal nonempty arrays required')
    complement = [z*a.conjugate() for a, z in zip(local, full_lag)]
    product = mean(local)*mean(complement)
    return mean(full_lag)-product, product


def verdict(interval, numerator, denominator=1):
    if interval.hi*denominator <= numerator*SCALE:
        return 'PASS_FINITE'
    if interval.lo*denominator > numerator*SCALE:
        return 'REFUTED_FINITE'
    return 'INCONCLUSIVE'
