#!/usr/bin/env python3
"""Bounded exact residue/Fourier/GCD controls; writes no infinite proof status."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.round2_operators import residue_transport, spectral_certificate


def exact_json(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    files = ['observational_succ/round2_operators.py', 'scripts/round2_operators_probe.py',
             'tests/test_round2_operators.py']
    spectra = [spectral_certificate(n, 4) for n in (1, 2, 4, 8, 16, 32, 64)]
    residue = [residue_transport(primes, q, 500) for primes, q in
               (((), 1), ((2,), 3), ((2, 3), 5), ((2, 3, 7), 25), ((3, 5, 7), 8))]
    record = dict(authority='EXACT_FINITE_CONTROLS_AND_SPECTRAL_ENCLOSURES',
                  infinite_claims='PAPER_PROOF_ONLY; no finite sieve certifies divergent prime sums',
                  hashes={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files},
                  spectra=spectra, residue_transport=residue)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(record, default=exact_json, indent=2)+'\n')
    for row in spectra:
        print('N={N}: {lo} <= ||T_N||^2 <= {hi} (decimal display only)'.format(
            N=row['N'], lo=float(row['lower_squared_operator_norm']),
            hi=float(row['upper_squared_operator_norm'])))
    print('All stored bounds and witnesses are exact rational numbers.')


if __name__ == '__main__':
    main()
