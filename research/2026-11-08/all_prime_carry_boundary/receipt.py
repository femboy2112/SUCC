"""Deterministic all-prime BBP carry ledger and finite boundary certificate.

Uses canonical imported source. Outputs exact integers and rational strings only.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from hashlib import sha256
import json

from observational_succ.adelic_additive_gluing import orbit_states
from observational_succ.all_prime_carry_boundary import (
    original_carry_ledger, original_digit_at_carry,
    carry_ledger, carry_at_address, crt_phase_address,
    partial_prime_carry_count, consecutive_carry_counts,
    cross_place_integer_carry, two_adic_integral_residue,
)
from observational_succ.duck_bbp import forcing


def snapshot() -> dict:
    states=orbit_states(32)
    items=[]
    for n in range(17,33):
        r=original_carry_ledger(n,states=states)
        digit,literal,hotspot=original_digit_at_carry(n,depth=12,states=states)
        p2=cross_place_integer_carry(r.previous,r.forcing,bits=8)
        items.append({
            'n': n,
            'forcing':str(r.forcing),
            'common_conductor':str(r.conductor),
            'literal_carry':literal,
            'certified_hex_digit':digit,
            'analytical_hotspot':hotspot,
            'prime_count':len(r.rows),
            'inherited_no_forcing':[q.prime for q in r.rows if q.inherited_without_forcing],
            'new_forcing_only':[q.prime for q in r.rows if q.source_only],
            'source_integer_offset':r.source_integer_offset,
            'local_winding_sum':r.local_winding_sum,
            'global_winding_correction':r.next_global_winding-16*r.prior_global_winding,
            'p2_integral_before_bits8':two_adic_integral_residue(r.previous,8),
            'p2_integral_next_bits8':p2[1],
            'p2_carry_reconstruction':p2[0],
            'local_prime_power_rows':[{
                'p':q.prime,'p_power':q.power,'time_mod_power':q.time_mod_prime_power,
                'prior':str(q.prior),'source':str(q.forcing),'next':str(q.next),
                'local_winding':q.local_winding} for q in r.rows],
        })
    n2=original_carry_ledger(2,states=states)
    counterfactual=[]
    for j in range(5):
        previous=(Fraction(1,3)+Fraction(j,5))%1
        counterfactual.append(carry_ledger(previous,forcing(2),13).literal_carry)
    Q=4095; R=forcing(2)
    calibrated={}
    for selected in ((9,),(9,5)):
        M=1
        for p in selected:M*=p
        L=Q//M
        counts=[partial_prime_carry_count(Q,R,selected,c,k)[0]
                for c in range(M) for k in range(1,16)]
        calibrated[str(selected)]={'M':M,'L':L,'minimum':min(counts),'maximum':max(counts)}
    matrix=[[int(carry_at_address(15,R,crt_phase_address(15,{3:a,5:b}))>=8)
             for b in range(5)] for a in range(3)]
    return {
        'schema':'SUCC_ALL_PRIME_CARRY_BOUNDARY_EXACT_V1',
        'authentic_source':'4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)',
        'literal_zero_seed':True,
        'source_scope':'finite exact rational recurrence, not a pi-normality proof',
        'holdout':{'first':17,'last':32,'events':items},
        'time2':{
            'old_prime5_without_source_injection':True,
            'literal':n2.literal_carry,
            'source_integer_offset':n2.source_integer_offset,
            'local_winding_sum':n2.local_winding_sum,
            'global_winding':n2.next_global_winding-16*n2.prior_global_winding,
            'varying_5_adic_at_fixed_3_adic':counterfactual,
            'complete_carry_alphabet_reference_Q4095':consecutive_carry_counts(Q,R),
            'partial_prime_fibers':calibrated,
            'mixed_3x5_threshold_8_matrix':matrix,
        },
    }


def serialized() -> str:
    return json.dumps(snapshot(),sort_keys=True,ensure_ascii=False,indent=2)+'\n'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    path=Path(__file__).with_name('ALL_PRIME_HOLDOUT_EXACT.json')
    payload=serialized()
    if args.write:
        path.write_text(payload,encoding='utf-8')
    if args.verify:
        if not path.is_file() or path.read_text(encoding='utf-8')!=payload:
            raise SystemExit('FAIL: source-facing all-prime receipt mismatch')
    print(f'PASS: {len(snapshot()["holdout"]["events"])} source times; SHA256 {sha256(payload.encode()).hexdigest()}')

if __name__=='__main__':main()
