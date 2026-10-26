#!/usr/bin/env python3
"""Replay source-hashed exact boundary/Gamma certificates.

Run from an installed checkout. This receipt records finite certificates;
the universal analytic statements have separately cited paper proofs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from observational_succ.bbp_gamma_boundary import gamma_boundary_receipt
from observational_succ.bbp_twisted_boundary import (
    solve_affine_seam, generating_identity_certificate,
    reciprocal_reversal_certificate, source_commuting_affine,
)
from observational_succ.bbp_twist_boundary_layer import (
    edge_loss_interval, edge_complex_error, scaled_deficit_budget,
)
from observational_succ.qgamma_seam import (
    antiperiodic_factorization, antiperiodic_product_interval,
    q_euler_constant_interval, shifted_twist_gamma_ratio,
)
from observational_succ.euler_mascheroni_succ import gamma_bounds
from observational_succ.twisted_digamma_boundary import (
    alternating_euler_interval, alternating_reciprocal_interval,
    dyadic_euler_certificate, bbp_digamma_interval, bbp_alternating_interval,
    reciprocal_gamma_word,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'research/2026-10-25/MOBIUS_GAMMA_RECEIPT.json'
MODULES = ('bbp_gamma_boundary', 'bbp_twisted_boundary',
           'bbp_twist_boundary_layer', 'qgamma_seam', 'twisted_digamma_boundary')
INPUTS = [f'observational_succ/{name}.py' for name in MODULES]
INPUTS += [f'tests/test_{name}.py' for name in MODULES]
INPUTS += [
    'observational_succ/bbp_source_memory.py',
    'observational_succ/bbp_resonance_controls.py',
    'observational_succ/bbp_prime_window_signed_intervals.py',
    'observational_succ/euler_mascheroni_succ.py',
    'observational_succ/zero_one_gamma_bridge.py',
    'observational_succ/euler_bbp_regulator.py',
    'scripts/mobius_gamma_boundary_probe.py',
    'research/2026-10-25/MOBIUS_GAMMA_BOUNDARY_REPORT.md',
    'research/2026-10-25/BBP_GAMMA_BOUNDARY.md',
    'research/2026-10-25/BBP_TWISTED_BOUNDARY.md',
    'research/2026-10-25/TWISTED_DIGAMMA_BOUNDARY.md',
    'research/2026-10-25/QGAMMA_SEAM_DETERMINANT.md',
    'research/2026-10-25/MOBIUS_GAMMA_HOSTILE_AUDIT.md',
    'docs/CLAIM_SUPPLEMENT_MOBIUS_GAMMA_BOUNDARY.md',
]


def canonical(value):
    if isinstance(value, Q):
        # Large exact sums of log intervals can exceed Python's decimal
        # conversion cap. Hex preserves every bit without disabling the cap.
        if max(value.numerator.bit_length(),value.denominator.bit_length())>8192:
            return {'exact_rational':{'numerator_base16':hex(value.numerator),
                                      'denominator_base16':hex(value.denominator)}}
        return str(value)
    if hasattr(value, 'lower') and hasattr(value, 'upper') and not isinstance(value,str):
        return {'lower':canonical(value.lower),'upper':canonical(value.upper)}
    if isinstance(value,dict):
        return {str(k):canonical(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):
        return [canonical(v) for v in value]
    return value


def recompute():
    gamma = gamma_bounds(64)
    seams = [solve_affine_seam(n,lam,beta)
             for n in (1,5,13) for lam,beta in ((-1,0),(1,0),(Q(2,3),Q(7,11)))]
    for seam in seams:
        assert not seam['authentic_compatible']
    identities=[generating_identity_certificate(n,c,z)
                for n,c,z in ((0,0,Q(1,16)),(7,Q(2,7),Q(1,16)),(11,0,Q(-1,3)))]
    assert all(v['residual']==0 for v in identities)
    products=[]
    for q in (Q(1,16),Q(1,2),Q(2,3)):
        a,b=antiperiodic_factorization(q,12)
        assert a==b
        direct,ratio=shifted_twist_gamma_ratio(q,7)
        assert direct==ratio
        products.append({'q':q,'product':a,'interval':antiperiodic_product_interval(q,12),
                         'qgamma7_ratio':ratio,'gamma_q':q_euler_constant_interval(q,24)})
    dyadic=dyadic_euler_certificate(8,24,32)
    assert max(gamma[0],dyadic.total.lower)<min(gamma[1],dyadic.total.upper)
    alternate=bbp_alternating_interval(32)
    digamma=bbp_digamma_interval(32)
    assert max(alternate.lower,digamma.lower)<min(alternate.upper,digamma.upper)
    return canonical({
        'schema':'MGB-exact-boundary-gamma-v1',
        'parent':'eca4462ee4d62642b15c4af672136aa5bcacd00b',
        'authority':'finite rational certificates; infinite claims are separate paper proofs',
        'normality_proved':False,'RH_proved':False,'new_lean_authority':False,
        'reference_offsets':[{'offset':c,'gamma_minus_offset':(gamma[0]-c,gamma[1]-c)}
                             for c in (Q(),Q(1,2),Q(1))],
        'gamma_primitive':gamma_boundary_receipt(24,24),
        'twisted_euler':{
            'ordinary_gamma_interval':gamma,
            'alternating_delta_interval':alternating_euler_interval(1,32,32),
            'dyadic_gamma_interval':dyadic.total,
            'dyadic_tail':dyadic.tail,
            'reciprocal_resolvent_at_one':alternating_reciprocal_interval(1,32),
            'two_step_multiplier_at_one':reciprocal_gamma_word(1,2).multiplier,
            'bbp_alternating_direct':alternate,'bbp_alternating_digamma':digamma,
        },
        'finite_seams':seams,'finite_generating_identities':identities,
        'source_fixed_reflection':[source_commuting_affine(n,-1) for n in (0,3,11)],
        'reciprocal_quotient_counterexample':reciprocal_reversal_certificate(2),
        'edge_losses':[{'h':h,'interval':edge_loss_interval(h,depth=8,phase_terms=10),
                        'm37_complex_error':edge_complex_error(37,h),
                        'm37_scaled_error':scaled_deficit_budget(37,h)} for h in (0,1,2)],
        'seam_qproducts':products,
        'source_sha256':{path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
                         for path in INPUTS},
    })


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    choice=parser.add_mutually_exclusive_group(required=True)
    choice.add_argument('--write',nargs='?',const=str(DEFAULT))
    choice.add_argument('--verify',nargs='?',const=str(DEFAULT))
    args=parser.parse_args()
    actual=recompute()
    data=json.dumps(actual,sort_keys=True,indent=2)+'\n'
    path=Path(args.write or args.verify)
    if args.write:
        path.write_text(data)
    else:
        expected=json.loads(path.read_text())
        if expected!=actual:
            raise SystemExit('MGB receipt mismatch: source, claim flag or exact output changed')
    print(json.dumps({'result':'written' if args.write else 'verified',
                      'sha256':hashlib.sha256(data.encode()).hexdigest(),
                      'hashed_inputs':len(INPUTS),'normality_proved':False}))


if __name__=='__main__':
    main()
