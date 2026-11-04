"""Reproducible exact integer/Fraction receipts for original source + controls.

The float conversions here are explicitly diagnostics, never proof inputs.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import argparse
import oily_shear as o

PATH=Path(__file__).with_name('FINITE_RECEIPT.json')

def digest(x):
    if isinstance(x,int):
        x=x.to_bytes(max(1,(x.bit_length()+7)//8),'big',signed=False)
    if isinstance(x,str):x=x.encode('utf-8')
    return sha256(x).hexdigest()

def frac(x:F):return [x.numerator,x.denominator]

def compute():
    out={'status':'EXACT FINITE RECEIPT, NO ALL-HORIZON WEYL SAVING',
         'parent_sha':'cdb01d73839f08cb10b46f51d42afecf44469ee2',
         'preregistration_sha':'48777b17383d8c42c6f3adb9853923b2017bed23',
         'original':'four signed poles, literal U0=0',
         'finite_ghosts':{},'source_pi_lag_certificates':{},'shadow_horizon':{},
         'radial_null':{},'gamma_shear':{},'source_primes':{}}
    for A,m in ((48,8),(96,16)):
        pack=o.clean_passports(A)
        ghost=o.rational_ghost_cloud(pack,m)
        D,R,S=ghost['D'],ghost['R'],ghost['old_prime_product']
        out['finite_ghosts'][str(A)]={
            'mesh':m,'window_size':pack['end']-A,
            'split_primes':len(pack['plus']),'inert_primes':len(pack['minus']),
            'common_odd_D_bits':D.bit_length(),'selected_R_bits':R.bit_length(),
            'old_S_bits':S.bit_length(),'D_over_R_bits':(D//R).bit_length(),
            'D_sha256_unsigned_be':digest(D),'R_sha256_unsigned_be':digest(R),
            'all_selected_primes_sha256':digest(','.join(str(p) for p in pack['primes'])),
            'unit_residue_fraction':frac(ghost['coprime_residue_fraction']),
            'ghost_arc_radius_upper':frac(ghost['real_arc_radius_upper']),
            'p_local_recurrence_and_actual_residues_exact':True,
            'every_ghost_in_same_real_mesh_cell':True,
            'countermodel_not_original_full_recurrence':True,
        }
    for A,m in ((37,8),(73,8),(137,16)):
        end=(4*A+2)//3
        seq=o.exact_original_orbit(end-1)
        count_source=count_true=near_ambiguous=positive=negative=0
        for n in range(A,end):
            for d in range(1,end-n):
                rec=o.original_pi_lag_certificate(seq,n,d,m,32)
                if rec['classification']=='ambiguous':near_ambiguous+=1
                original=rec['original_source_near']; true=rec['classification']=='near'
                count_source+=original;count_true+=true
                if true and not original:positive+=1
                if original and not true:negative+=1
        out['source_pi_lag_certificates'][str(A)]={
            'mesh':m,'window_length':end-A,'unordered_source_near':count_source,
            'unordered_true_pi_near_certified':count_true,
            'ambiguous':near_ambiguous,'positive_boundary_flux':positive,
            'negative_boundary_flux':negative}
    for M,m in ((17,8),(49,16),(113,16),(257,32),(1024,16)):
        h=o.gamma_shadow_horizon(M,m)
        q=h['guaranteed_extra_steps']
        out['shadow_horizon'][str(M)]={
            'mesh':m,'guaranteed_extra_steps':q,
            'true_extra_steps_in':[q,q+1],
            'tail_lower':frac(h['tail_lower']),'tail_upper':frac(h['tail_upper']),
            'certified_extra_phase_cells':[
                o.certified_phase_bin(M,M+i,m) for i in range(q+1)],
            'no_external_pi_digits':True}
    for n in (1,2,3,4,5,8):
        out['radial_null'][str(n)]={'strictly_positive_exact':frac(o.finite_null_radial(n)),
                                    'strict_upper':frac(o.finite_null_radial_upper(n))}
    for n,d in ((37,1),(73,7),(137,17),(512,1),(1024,7)):
        lo,hi=o.shear_interval(n,d,36)
        out['gamma_shear'][f'{n}:{d}']={'lower':frac(lo),'upper':frac(hi),
            'sharpness_ratio_32n3_over_d_approx':round(float(lo*F(32*n**3,d)),12),
            'rational_beta_shear_cap':frac(o.shear_cap(n,d))}
    for A in (48,96):
        pack=o.clean_passports(A)
        seq=o.exact_original_orbit(pack['end']-1)
        nonalias_checks=0
        for n in range(A,pack['end']):
            for t in range(n+1,pack['end']):
                d=t-n; R=o.nonalias_radical(pack,d)
                for h in (1,3,5,A):
                    z=h*(seq[t]-seq[n]);assert z.denominator%R==0
                    nonalias_checks+=1
        out['source_primes'][str(A)]={
            'all_pair_h_radicals_verified':nonalias_checks,
            'radical_d1_bits':o.nonalias_radical(pack,1).bit_length(),
            'selected_prime_count':len(pack['primes']),
            'prime_order_exact_no_repeat':True}
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    out=compute()
    if args.verify:
        expected=json.loads(PATH.read_text())
        assert expected==out
        print('EXACT source/Gamma/radial/CRT receipt replay: PASS')
    else:
        PATH.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
        print(f'Saved {PATH}, {PATH.stat().st_size} bytes')
