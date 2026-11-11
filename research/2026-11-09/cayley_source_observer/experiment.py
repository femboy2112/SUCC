"""Frozen exact finite certificate probe; run from repository root with PYTHONPATH=."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from math import floor
from pathlib import Path

from observational_succ import duck_bbp
from observational_succ import cayley_source_observer as c
from observational_succ import parity_boundary_certificate as p


ROOT = Path(__file__).resolve().parents[3]


def outward(interval, bits=48):
    """Conservative dyadic compression keeps exact certificates readable."""
    a, b = interval
    scale = 2**bits
    return [Q(floor(a*scale), scale), Q(-floor(-b*scale), scale)]


def encode(obj):
    if isinstance(obj, Q):
        return str(obj)
    raise TypeError(type(obj).__name__)


def digest(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def run():
    files = (
        'observational_succ/duck_bbp.py',
        'observational_succ/selected_orbit.py',
        'observational_succ/cayley_source_observer.py',
        'observational_succ/parity_boundary_certificate.py',
        'research/2026-11-09/cayley_source_observer/PROTOCOL.md',
        'research/2026-11-09/cayley_source_observer/experiment.py',
    )
    result = {
        'status': 'CERTIFIED-FINITE',
        'normality_proved': False,
        'parity_asymptotic_proved': False,
        'source_seed': 'literal zero',
        'source_hashes': {path: digest(path) for path in files},
        'epochs': [],
    }
    for A in (257, 509):
        H, delta = 1023, Q(1, 256)
        intervals = p.common_horizon_enclosures(A, 2*A)
        budget = p.fejer_error_budget(intervals, H, delta)
        fm = outward(p.fejer_mean_enclosure((iv.center for iv in intervals), H,
                                            bits=48, terms=16))
        certified = outward((fm[0]-budget['error_bound'], fm[1]+budget['error_bound']))
        # A second source enclosure schedule: local horizon n+12, not a
        # second unrelated pi source or independent proof of the BBP identity.
        local = p.source_phase_enclosures(A, depth=12)
        digits = [iv.digit() for iv in local]
        if any(d is None for d in digits):
            raise ArithmeticError('fixed local certificate did not resolve every digit')
        positive = sum(d % 2 == 0 for d in digits)
        parity = Q(2*positive-A, A)
        if not certified[0] <= parity <= certified[1]:
            raise ArithmeticError('paid Fourier certificate missed exact parity')
        phases = [iv.lo % 1 for iv in intervals]
        phases.append(16*phases[-1] % 1)
        recursion = p.stationary_boundary_recursion(phases, 3)
        if any(row['identity_residual'] for row in recursion['rows']):
            raise ArithmeticError('two-fiber recurrence failed')

        Lghost = 2*A+12
        # With s=-P_L, the finite completed lower endpoint is exactly zero.
        ghost = []
        for n in range(A, 2*A):
            lo, hi = c.source_completed_interval(n, Lghost)
            ghost.append(p.PhaseEnclosure(Q(), hi-lo))
        if any(iv.digit() != 0 for iv in ghost):
            raise ArithmeticError('same-forcing rational wrong seed not certified')
        wrong = p.stationary_boundary_recursion([Q()]*(A+1), 3)
        if wrong['boundary_mass'] != 1:
            raise ArithmeticError('control lost boundary mass')
        result['epochs'].append({
            'A': A, 'H': H, 'common_source_horizon': 2*A,
            'delta': delta, 'even_digits': positive, 'odd_digits': A-positive,
            'exact_parity_mean': parity,
            'fejer_mean_interval': fm,
            'certified_parity_interval': certified,
            'budget': budget,
            'boundary_recursion': recursion,
            'wrong_seed_control': {
                'construction': f's=-P_{Lghost}; rational same forcing, no p-integral claim',
                'all_completed_epoch_digits_zero': True,
                'parity_mean': Q(1),
                'boundary_mass': wrong['boundary_mass'],
                'boundary_recursion': wrong,
            },
        })
    k, bound = c.common_horizon_epoch_log_bound(1024, 16**32)
    result['clock_calibration'] = {
        'resonance_n': 128, 'h_n': c.quadratic_resonance_frequency(128),
        'phase_error_lower_bound': outward((c.resonance_chord_lower_bound(128, 12), Q(2)))[0],
        'common_epoch_A': 1024, 'bandwidth_H': str(16**32),
        'clipping_threshold': k, 'phase_mean_error_upper_bound': bound,
    }
    return result


if __name__ == '__main__':
    print(json.dumps(run(), default=encode, indent=2, sort_keys=True))
