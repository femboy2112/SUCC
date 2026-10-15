#!/usr/bin/env python3
"""Exact source-conditioned contour receipt, and separate authenticated-parent gate."""
import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.certified_contour_weil import (
    shadow_interval_model, original_xi_model, centered_xi_model,
    verify_shadow_against_original, certify_rectangle, reflected_fake_non_euler,
    fake_reflected_odd_negative_bound, zeta_zero_side_tail_constant,
    derivative_scaling_obstruction, contour_weil_identity_note, THETA_RECEIPT_BLOB
)
SHADOW=ROOT/'tests/fixtures/XI_PARENT_SOURCE_OUTER_INTERVALS.json'

def rounded_lower(x, scale=10**6):
    x=Q(x)
    return str(Q(x.numerator*scale//x.denominator,scale))

def rounded_upper(x, scale=10**6):
    x=Q(x)
    return str(-Q((-x).numerator*scale//(-x).denominator,scale))

def example(name,model,hw,hh,n):
    r=certify_rectangle(model,0,0,hw,hh,n)
    return {'name':name,'zero_count':r['count'],
            'bound_abs_error_ceiling':rounded_upper(model.error),
            'contour_nonzero_margin_floor':rounded_lower(r['min_nonzero_margin']),
            'vertices':r['vertices'],
            'inputs_are_zero_list':False}

def receipt():
    original=shadow_interval_model(SHADOW,3,13)
    wide=shadow_interval_model(SHADOW,Q(107,10),20)
    shifted=shadow_interval_model(SHADOW,Q(3,2),13,centered=True)
    fake=reflected_fake_non_euler(shadow_interval_model(SHADOW,Q(3,2),13))
    v=zeta_zero_side_tail_constant(Q(1,4),16)
    return {'status':'SOURCE_CONDITIONAL_EXACT_POLYGON_WINDING',
      'parent_theta_blob':THETA_RECEIPT_BLOB,
      'separate_immutable_parent_authentication_required':True,
      'authenticated_external_physical_source':False,
      'certificates':[
        example('xi small rectangle',original,Q(2),Q(1),32),
        example('xi square radius 7.5',wide,Q(15,2),Q(15,2),2048),
        example('xi centered difference double zero',shifted,Q(1),Q(1),32),
        example('reflection-symmetric nonEuler xi mutant',fake,Q(1),Q(1),32)],
      'fake_local_weil_strict_negative':fake_reflected_odd_negative_bound(Q(1)),
      'zero_tail_external_count_contract':{
          'test_a':v['a'],'cutoff_T':v['T'],
          'upper_A':v['A_upper'],
          'upper_tail':v['full_zero_side_tail_upper'],
          'source':v['external_zero_count_assumption']},
      'non_uniform_H1_scaling':{k:str(v) if isinstance(v,Q) else v for k,v in derivative_scaling_obstruction(4).items()},
      'actual_completed_weil_comparison':contour_weil_identity_note(),
      'complete_Weil_positivity_certified':False,
      'RH_proved':False}

def authenticate():
    x=verify_shadow_against_original(ROOT,SHADOW)
    xi=original_xi_model(ROOT,Q(107,10),20)
    a=certify_rectangle(xi,0,0,Q(15,2),Q(15,2),2048)
    if a['count']!=0 or Q(a['min_nonzero_margin'])<=0:
        raise RuntimeError('authentic xi wide-contour did not verify')
    shift=centered_xi_model(ROOT,Q(3,2),13)
    b=certify_rectangle(shift,0,0,1,1,32)
    if b['count']!=2:
        raise RuntimeError('authentic xi centered-zero contour did not verify')
    return {'authentic_parent_blob_checked':True,
            'all_21_parent_coefficient_intervals_crosschecked':x['all_21_theta_coefficients_enclosed'],
            'original_xi_zero_count_in_radius_7_5':a['count'],
            'centered_difference_zero_count':b['count'],
            'RH_proved':False}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--verify',type=Path)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--authenticate-parent',action='store_true')
    args=ap.parse_args()
    if args.authenticate_parent:
        print(json.dumps(authenticate(),sort_keys=True,indent=2))
        print('AUTHENTIC_THETA_CONTOUR_PROVENANCE_VERIFIED')
        return
    data=receipt()
    if args.verify:
        if json.loads(args.verify.read_text())!=data:
            raise SystemExit('CONTOUR_WEIL_RECEIPT_MISMATCH')
        print('CONTOUR_WEIL_RECEIPT_REPLAY_VERIFIED')
    elif args.output:
        args.output.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    else:
        print(json.dumps(data,sort_keys=True,indent=2))

if __name__=='__main__':main()
