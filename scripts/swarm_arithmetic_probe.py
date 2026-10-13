#!/usr/bin/env python3
"""Freeze exact source/action controls for SWM-E33--E40; no zero oracle."""
import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.arithmetic import source_at, factorization
from observational_succ.core import Scalar, ONE
from observational_succ.swarm_arithmetic import (
    AffineAction, cyclic_frame_offsets, factor_square, factorial_valuation,
    mahler_prefix_ambiguity, dirichlet_log, euler_audit, valuation_covariance,
    gamma_cutoff_recurrence, gaussian_component, verify_gaussian_closed,
    projected_resolvent_numerator,
)


def encode(x):
    if isinstance(x, Scalar):
        return x.data()
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): encode(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [encode(v) for v in x]
    return x


def receipt():
    zeta = {n: ONE for n in range(1, 65)}
    fake6 = dict(zeta)
    fake6[6] = Scalar(2)
    sign6 = dict(zeta)
    sign6[6] = -ONE
    chi5 = {n: source_at(n, 'chi5') for n in range(1, 65)}
    mixture = {n: source_at(n, 'mixture5') for n in range(1, 65)}
    phase = {n: chi5[n]*((-ONE)**dict(factorization(n)).get(2, 0)) for n in chi5}
    nonunit = {n: Scalar(2**dict(factorization(n)).get(2, 0)) for n in zeta}
    covariance = valuation_covariance(zeta, 64, (2, 3))
    components = {b: gaussian_component((1, 1), b) for b in (1, 2, 4)}
    return encode({
        'parent_sha': '5eb09e7cba36ec01b8f9d6834b78b5766fd93935',
        'scope': 'exact finite supplied mathematical sources; no physical attestation',
        'E33': {'affine_order': [AffineAction(6).compose(AffineAction(1, 1))(3),
                                 AffineAction(1, 1).compose(AffineAction(6))(3)],
                'odd_prime_clock_12_offsets': cyclic_frame_offsets(12, (3, 5, 7)),
                'with_prime_two_offsets': cyclic_frame_offsets(12, (2, 3, 5, 7))},
        'E34': {'factor_square_36': factor_square(36), 'v2_factorial100': factorial_valuation(100, 2)},
        'E35': mahler_prefix_ambiguity(31, 3),
        'E36': {'zeta': euler_audit(zeta, 64, conductor=1),
                'chi5': euler_audit(chi5, 64, conductor=5),
                'fake6': euler_audit(fake6, 64), 'mixture5': euler_audit(mixture, 64),
                'nonunit2': euler_audit(nonunit, 64),
                'phase2': euler_audit(phase, 64, conductor=5),
                'b6_fake': dirichlet_log(fake6, 64)[6]},
        'E37': gamma_cutoff_recurrence(17, 2),
        'E38': {'covariance_zeta': covariance,
                'covariance_sign6': valuation_covariance(sign6, 64, (2, 3)),
                'b6_zeta': dirichlet_log(zeta, 64)[6], 'b6_sign6': dirichlet_log(sign6, 64)[6],
                'same_covariance': covariance == valuation_covariance(sign6, 64, (2, 3)),
                'determinant': covariance[0][0]*covariance[1][1]-covariance[0][1]*covariance[1][0]},
        'E39': {b: {'vertices': len(c), 'closed': verify_gaussian_closed(c, b),
                   'coordinate_extrema': [min(x for x, _ in c), max(x for x, _ in c),
                                         min(y for _, y in c), max(y for _, y in c)]}
                for b, c in components.items()},
        'E40': [projected_resolvent_numerator(a) for a in (Q(1, 5), Q(1, 2), Q(4, 5))],
        'nontrivial_zeros_input': False, 'completed_Weil_positivity_claim': False,
        'analytic_continuation_constructed': False,
    })


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps(receipt(), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
        print(f'Saved exact arithmetic receipt: {args.output}')
    else:
        print(data, end='')
