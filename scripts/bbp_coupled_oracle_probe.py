"""Deterministic finite receipt; not a normality proof or a trusted kernel.

Run from SUCC root: python scripts/bbp_coupled_oracle_probe.py --N 10 --k 2
All displayed numeric claims are exact Fraction arithmetic or exact integers.
"""
from __future__ import annotations

import argparse
import json

from observational_succ.bbp_coupled_oracle import (
    certify_root, certify_square, finite_prefix_signal, pure_gauge_holonomy,
    snapshot, verify_green_transport,
)


def f(x):
    return f'{x.numerator}/{x.denominator}'


def run(depth: int, digits: int, N: int, k: int) -> dict:
    root = certify_root(depth, digits)
    square = certify_square(root, N, k)
    s = snapshot(root, N, k)
    return {
        'claim_status': 'CERTIFIED-FINITE (source law and BBP evaluation imported)',
        'normality_status': 'OPEN',
        'source_id': root.source_id,
        'source_depth': depth,
        'root_digits': digits,
        'N': N,
        'k': k,
        'root_prefix_hex': format(root.prefix, f'0{digits}X'),
        'root_enclosure_width': f(root.upper-root.lower),
        'knowledge_signal_digits': finite_prefix_signal(depth, max(digits, 1)).certified_digits,
        'variation': f(s.variation),
        'energy': f(s.energy),
        'finite_support_tv_lower': f(s.coverage_lower),
        'refinement_N_energy': f(square.horizontal_refinement_N),
        'refinement_Nplus1_energy': f(square.horizontal_refinement_N1),
        'clock_N_energy': f(square.temporal_increment_k),
        'clock_N_fine_energy': f(square.temporal_increment_k1),
        'square_energy_commutator': f(square.square_energy_commutator),
        'square_counts_commute': square.exact_word_square_commutes,
        'green_enclosure_transports': [f(x) for x in verify_green_transport(N, k)],
        'phase_holonomy_h1': f(pure_gauge_holonomy(N, 1)),
        'warning': 'Exact finite source consistency does not imply signed cancellation.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--depth', type=int, default=32)
    parser.add_argument('--digits', type=int, default=17)
    parser.add_argument('--N', type=int, default=10)
    parser.add_argument('--k', type=int, default=2)
    a = parser.parse_args()
    print(json.dumps(run(a.depth, a.digits, a.N, a.k), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
