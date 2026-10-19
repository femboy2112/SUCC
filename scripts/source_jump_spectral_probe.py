"""Deterministic finite spectral/polar certificates; --source authentic source replay."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from observational_succ.source_jump_spectral import (
    effective_gamma_rank_budget, canonical_cycle_control,
    source_fourier_band_certificate_budget, exact_feature_gram_decision,
    authenticate_original_jump_rank_budget, authentic_primitive_ritz_packet,
)


def serial(v):
    if isinstance(v,F):
        return str(v)
    if isinstance(v,dict):
        return {str(k):serial(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):
        return [serial(x) for x in v]
    return v


def report(authenticated=False):
    positive=canonical_cycle_control()
    negative=canonical_cycle_control(3)
    mixed=canonical_cycle_control(pole_mutation=True)
    band=source_fourier_band_certificate_budget()
    toy=exact_feature_gram_decision(1,((1,F(1,2)),(F(1,2),1)),(-F(1,4),-F(1,4)))
    out={
       'operation':'SOURCE_JUMP_SPECTRAL_POLAR_FOURIER_2026_10_17',
       'rank_gap_paper':effective_gamma_rank_budget(),
       'positive_rational_cycle':{
            'verdict':positive['positive_certified_in_finite_model'],
            'low_rank':positive['low_spectral_rank'],
            'cosh_alpha':positive['cosh_high_resolvent'],
            'cosh_strength':positive['cosh_effective_strength'],
            'sinh_strength':positive['sinh_effective_strength'],
            'RH_proved':False},
       'negative_rational_cycle':{'verdict':negative['positive_certified_in_finite_model'],
                                  'negative_witness':negative['negative_witness']},
       'false_polar_mutant':{'verdict':mixed['positive_certified_in_finite_model']},
       'effective_frequency_lower_budget':{
            'R':band['R'], 'nodes':band['two_sided_midpoint_frequency_nodes'],
            'rank':band['worst_case_real_feature_rank'],
            'error_upper':band['absolute_operator_quadrature_error_certified_upper'],
            'coefficients_actually_sampled':False},
       'finite_feature_gram_control':{'positive':toy['positive_certified_in_finite_feature_model'],
                                      'source_authenticated':False},
       'source_jump_projector_computed':False,
       'original_signed_Weil_positivity_proved':False,
       'RH_proved':False,
    }
    if authenticated:
        out['original_source_rank_gap']=authenticate_original_jump_rank_budget()
        out['original_source_primitive_Ritz']=[authentic_primitive_ritz_packet(k,12) for k in (1,2)]
        assert out['original_source_rank_gap']['actual_source_identified_by_archival_sha']
    return serial(out)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',action='store_true')
    p.add_argument('--verify',action='store_true')
    args=p.parse_args()
    data=report(args.source)
    if args.verify:
        assert data==report(args.source)
        assert data['source_jump_projector_computed'] is False
        assert data['original_signed_Weil_positivity_proved'] is False
        assert data['RH_proved'] is False
    print(json.dumps(data,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
