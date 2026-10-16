#!/usr/bin/env python3
"""Replay authentic cross-radius low forms, without a transported high theorem."""
from pathlib import Path
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.cross_prime_wavefront import (
    transported_low_bracket, product_formula_observation, radius_continuity_bound,
)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    result = {
        'status': 'EXACT_SOURCE_INTERVAL_LOW_COMPRESSIONS',
        'radii': [transported_low_bracket(a, 64) for a in (F(1, 2), F(9, 16), F(11, 16), F(7, 10))],
        'continuity_budget_example': radius_continuity_bound(F(1, 2), F(9, 16)),
        'partial_product_control': product_formula_observation(F(7, 12), (2, 3)),
        'source_sha256': hashlib.sha256((ROOT/'observational_succ/source_weil_hierarchy.py').read_bytes()).hexdigest(),
        'Schur_sign_proved': False, 'RH_proved': False,
    }
    data = json.dumps(result, default=str, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
        print('Cross-prime source intervals saved:', args.output)
    else:
        print(data)


if __name__ == '__main__':
    main()
