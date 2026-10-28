"""Finite deterministic, source-hashed atomic BBP regression instrument.

`python scripts/bbp_quadratic_atoms_probe.py --write` records an exact source
receipt; --verify compares against committed JSON and exits nonzero on changes.
No analytic or normality theorem is inferred from this finite receipt.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from observational_succ import bbp_quadratic_atoms as atom

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT/'research/2026-10-26/BBP_ATOMS_EXACT_RECEIPT.json'


def fingerprint(name):
    return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()


def build_receipt():
    p = atom.source_polynomial_certificate()
    m = atom.matrix_atoms_certificate()
    q = atom.signed_channel_certificate()
    return {
        'source_module_sha256': fingerprint('observational_succ/bbp_quadratic_atoms.py'),
        'tests_sha256': fingerprint('tests/test_bbp_quadratic_atoms.py'),
        'dossier_sha256': fingerprint('research/2026-10-26/BBP_TWO_QUADRATIC_ATOMS.md'),
        'polynomial_identities': {k: p[k] for k in ('P_equals_boundary_times_cancelled',
                                'octic_factorizes','reduced_identity','numerator_endpoint_zero',
                                'first_endpoint_jet')},
        'matrix_identities': {k: m[k] for k in ('G2_quarter_turn','H2_half_identity',
                             'G4_negative','H4_positive','G8_H8_equal')},
        'minimal_shared_scalar_return': m['least_common_positive_scalar_return'],
        'minimal_reduced_rational_state_dimension': m['minimal_real_state_dimension_for_this_reduced_transfer'],
        'signed_source_channels': {k: q[k] for k in ('taps_sum_to_original',
                                   'angular_equals_4_over_angle',
                                   'radial_equals_logarithmic_derivative')},
        'impulse_first_eight': [str(x) for x in atom.filter_coefficients(8)],
        'rational_radial_cutoffs': {str(n): str(atom.rational_radial_completion(n))
                                    for n in (0,1,2,3,4)},
        'green_tail_bounds': {str(n): [str(z) for z in atom.green_tail_bounds(n)]
                              for n in (1,2,4,8)},
        'pi_normality_proved': False,
        'signed_weyl_saving_proved': False,
        'scholarly_priority_claimed': False,
    }


def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',action='store_true')
    group.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    current=build_receipt()
    if args.write:
        RECEIPT.parent.mkdir(parents=True,exist_ok=True)
        RECEIPT.write_text(json.dumps(current,indent=2,sort_keys=True)+'\n')
        print('BBP_ATOMS_RECEIPT_WRITTEN')
    else:
        if current != json.loads(RECEIPT.read_text()):
            raise SystemExit('BBP_ATOMS_RECEIPT_MISMATCH')
        print('BBP_ATOMS_RECEIPT_VERIFIED')

if __name__=='__main__':
    main()
