"""Preregistered source-certified collision windows; exact integers only."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_collision_intervals import (
    source_intervals, certified_pair_count, certified_cell_counts, canonical_cells,
)
from observational_succ.pi_source_collision import order16


def receipt(primes):
    rows = []
    for p in primes:
        u = (p-1)//8
        length = 3*u
        order = order16(p)  # validates primality independently of selection
        assert p % 8 == 1 and order*order > p
        cells = canonical_cells(p)
        sample = source_intervals(u+1, length)
        pairs = certified_pair_count(sample, cells)
        counts = certified_cell_counts(sample, cells)
        digest = hashlib.sha256()
        for lo, hi in sample.bounds:
            digest.update(f'{lo},{hi}\n'.encode())
        rows.append({
            'prime': p, 'order': order, 'good_prime_certificate': 'order^2 > p, p > e',
            'start': u+1, 'length': length, 'cells': cells,
            'ordered_close_pairs': pairs,
            'selected_scaled_close_pairs': str(Q(cells*pairs, length*length)),
            'cell_counts': {str(k): v for k, v in sorted(counts.items())},
            'cell_collision': str(Q(cells*sum(v*v for v in counts.values()), length*length)),
            'same_local_phase_scaled_upper': str(Q(cells, order)),
            'interval_bits': sample.bits, 'pi_bits': sample.pi_bits,
            'pi_interval_width_units': sample.pi_width_units,
            'max_interval_width_units': max(b-a for a, b in sample.bounds),
            'ordered_interval_sha256': digest.hexdigest(),
            'ambiguous_pair_decisions': 0, 'ambiguous_cell_decisions': 0,
        })
    paths = ['observational_succ/pi_collision_intervals.py',
             'observational_succ/pi_source_collision.py',
             'scripts/pi_lag_interval_probe.py', 'tests/test_pi_collision_intervals.py',
             'research/2026-10-24/PI_LAG_PREREGISTRATION.md']
    return {'schema': 'SUCC-PI-LAG-CERTIFIED-WINDOWS-1',
            'status': 'CERTIFIED_FINITE', 'source': 'authentic BBP y0=0',
            'base': 'ea5f92bbc52468e55b597e52455f24bceedb47b3',
            'scale': 'largest 16-power M with M^5 <= p^2; c=2/5',
            'rows': rows, 'pi_normality': 'OPEN',
            'selected_asymptotic_bound': 'UNPROVED',
            'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                              for p in paths}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--large', action='store_true', help='include preregistered p=1048601')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    primes = (2081, 4129, 1048601) if args.large else (2081, 4129)
    result = receipt(primes)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': result['status'], 'rows': [
        {k: r[k] for k in ('prime', 'cells', 'ordered_close_pairs', 'selected_scaled_close_pairs')}
        for r in result['rows']]}))
