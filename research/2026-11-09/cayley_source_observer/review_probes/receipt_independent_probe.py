"""Preserved final-receipt audit, with fresh current-tree execution.

The exact checks and mpmath diagnostic are copied from the executed review.
The separate earlier source-hash command is included at the start. The
mpmath calculation is a numerical diagnostic, not the source of certification.
"""
import hashlib
import json
from pathlib import Path
from fractions import Fraction as Q
from math import floor

import mpmath as mp

from observational_succ import parity_boundary_certificate as p
from observational_succ import cayley_source_observer as c

if not __debug__:
    raise RuntimeError("This review probe must run with assertions enabled")

receipt = json.loads(Path(
    'research/2026-11-09/cayley_source_observer/FINITE_RECEIPT.json').read_text())
for path, digest in receipt['source_hashes'].items():
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, path
print({'source_hashes_matched': len(receipt['source_hashes']), 'status': 'PASS'})


def mpq(q):
    return mp.mpf(q.numerator)/q.denominator


def has_periodic_cut(lo, hi, cut):
    return -floor(-(lo-cut)) <= floor(hi-cut)


for epoch in receipt['epochs']:
    A, H = epoch['A'], epoch['H']
    ivs = p.common_horizon_enclosures(A, 2*A)
    actual_digits = [iv.digit() for iv in ivs]
    assert all(d is not None for d in actual_digits)
    assert Q(sum((-1)**d for d in actual_digits), A) == Q(epoch['exact_parity_mean'])
    budget = p.fejer_error_budget(ivs, H, Q(epoch['delta']))
    for name, value in budget.items():
        expected = epoch['budget'][name]
        assert value == (Q(expected) if isinstance(value, Q) else expected), (A, name)
    ambiguous = 0
    for iv in ivs:
        for j in range(4):
            r = Q(1, 4*16**j)
            for cen in (Q(0), Q(1, 2)):
                if any(has_periodic_cut(8*iv.lo, 8*iv.hi, cen+sgn*r)
                       for sgn in (-1, 1)):
                    ambiguous += 1
    assert ambiguous == 0
    lg = 2*A+12
    lo, hi = c.source_completed_interval(2*A, lg)
    assert hi-lo < Q(1, 131072)
    with mp.workdps(65):
        val = mp.mpf('0')
        for iv in ivs:
            for m in range(8, H+1, 16):
                angle = (m*iv.center) % 1
                val += mp.mpf(32)/m*(1-mp.mpf(m)/(H+1)) \
                    * mp.sin(2*mp.pi*mpq(angle))/mp.pi
        val /= A
        lower, upper = map(Q, epoch['fejer_mean_interval'])
        assert mpq(lower) <= val <= mpq(upper), (A, val, mpq(lower), mpq(upper))
    print({'A': A, 'common_cone_digit_match': True, 'budget_match': True,
           'arc_membership_ambiguities': ambiguous,
           'wrong_seed_endpoint_bound': True,
           'high_precision_fourier_diagnostic': 'inside rational interval'})
