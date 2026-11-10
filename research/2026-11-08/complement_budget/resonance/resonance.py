"""Source-cocycle constraints on a single unit polynomial phase model.

All certified numerical bounds use outward integer intervals. This module
neither certifies the imported Weil theorem nor estimates a global decay rate.
"""
from math import isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'research/2026-11-08/covariance_forge'))
sys.path.insert(0, str(ROOT / 'research/2026-11-08/signal_frontier/prime_resonance'))
from intervals import Box, Interval, ONE, ZERO, SCALE, phase, pi_box, mean
from pr_resonance import reduce_on_clock, order16, source_xi, evaluate
from observational_succ.duck_bbp import forcing


def sqrt_interval(value):
    """Outward square root; require a provably nonnegative interval."""
    if value.lo < 0:
        raise ValueError('nonnegative interval required')
    lo = isqrt(value.lo * SCALE)
    hi = isqrt(value.hi * SCALE)
    if hi * hi < value.hi * SCALE:
        hi += 1
    return Interval(lo, hi)


def nonnegative(value):
    return Interval(max(0, value.lo), max(0, value.hi))


def bounded_one(value):
    return Interval(min(SCALE, value.lo), min(SCALE, value.hi))


def modulus(box):
    return sqrt_interval(box.norm_squared())


def nonlinear_floor(p, h, polynomial):
    """Enclose CR3's universal L1 floor, after source-coset reduction."""
    if type(h) is not int:
        raise ValueError('integer h required')
    xi = source_xi(p)
    reduced = reduce_on_clock(polynomial, p, xi)
    d, m, L = len(reduced) - 1, order16(p), (p - 1) // 4
    if not 2 <= d < m:
        raise ValueError('nonlinear reduced degree 2<=d<m required')
    delta = bounded_one(sqrt_interval(Interval.ratio(p)) * Interval.ratio(d, m))
    defect = nonnegative(Interval.ratio(2) - delta * Interval.ratio(2) - Interval.ratio(4, L))
    r = forcing(L + 2)
    f = pi_box() * Interval.ratio(2 * abs(h) * r.numerator, r.denominator)
    residual = nonnegative(sqrt_interval(defect) - f)
    return {'floor': residual.square().divide(578), 'delta': delta,
            'forcing_error': f, 'degree': d, 'm': m, 'L': L,
            'reduced': reduced}


def folded(complement, m):
    if type(m) is not int or m <= 0 or not complement or len(complement) % m:
        raise ValueError('nonempty complete repetitions required')
    return [mean(complement[r::m]) for r in range(m)]


def unit_model(p, h, polynomial, anchor_numerator=0, anchor_denominator=1):
    """The h parameter labels the source observation; P is the complement."""
    if type(h) is not int:
        raise ValueError('integer h required')
    xi, m = source_xi(p), order16(p)
    reduced = reduce_on_clock(polynomial, p, xi)
    return [phase(anchor_numerator * p + anchor_denominator * evaluate(reduced, xi * pow(16, r, p) % p, p),
                  anchor_denominator * p) for r in range(m)]


def error_record(complement, model):
    m = len(model)
    B = folded(complement, m)
    rho = sum((modulus(B[r] - model[r]) for r in range(m)), ZERO).divide(m)
    direct = sum(((z - model[n % m]).norm_squared() for n, z in enumerate(complement)), ZERO).divide(len(complement))
    lifted = Interval.ratio(2) - mean(B[r] * model[r].conjugate() for r in range(m)).re * Interval.ratio(2)
    if not direct.overlaps(lifted):
        raise AssertionError('unit-model lift identity did not enclose a common value')
    if direct.hi > (rho * Interval.ratio(2)).lo:
        # A finite assertion needs strict interval separation. Tiny exact-zero
        # cases may overlap; return inconclusive rather than treating them false.
        certified = False
    else:
        certified = True
    return {'rho': rho, 'full_l2_squared': direct, 'lifted_squared': lifted,
            'lift_bound_strictly_certified': certified}
