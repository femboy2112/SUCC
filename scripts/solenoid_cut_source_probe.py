#!/usr/bin/env python3
"""Source-hashed exact replay for pointed-circle solenoid and 2-adic clock.

Usage from repo root:
  python scripts/solenoid_cut_source_probe.py --write
  python scripts/solenoid_cut_source_probe.py --verify
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
from observational_succ import solenoid_cut_source as s

OUT=ROOT/'research/2026-10-27/POINTED_CIRCLE_SOLENOID_RECEIPT.json'
SOURCES=[
 'observational_succ/solenoid_cut_source.py',
 'tests/test_solenoid_cut_source.py',
 'scripts/solenoid_cut_source_probe.py',
]

def normalize(x):
    from fractions import Fraction
    if isinstance(x,Fraction):return f'{x.numerator}/{x.denominator}'
    if isinstance(x,(tuple,list)):return [normalize(z) for z in x]
    if isinstance(x,dict):return {k:normalize(v) for k,v in x.items()}
    if type(x) in (int,bool,str) or x is None:return x
    raise TypeError(f'unsupported receipt value {type(x).__name__}')

def build_receipt():
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in SOURCES}
    cut=s.authentic_cut_history(24,anchor=s.Q(3,7),h=5)
    memories=[s.memory_gap_certificate(u,3) for u in s.source_unwrapped_states(12)]
    v={
        'schema':'SUCC.pointed-circle-solenoid-clock.v1',
        'source':'unaltered-Coherent-Main-X-four-pole-U0=0',
        'source_sha256':hashes,
        'dyadic_circle_seam':[s.cut_seam_receipt(k) for k in (2,4,12)],
        'solenoid_seam_odometer':[{'depth':k,'minus_one_to_zero':s.seam_memory_glue(16**k-1,k)} for k in (1,2,3)],
        'authentic_cut_coboundary':s.seam_coboundary_telescope(cut),
        'authentic_cut_first_six_carries':[(v.original_carry,v.cut_carry) for v in cut[:6]],
        'signed_midpoint_source':s.cut_midpoint_character_certificate(cut[-1],7,31),
        'two_adic_winding_torsion_gap':memories,
        'two_adic_uniformity':[s.time_clock_certificate(k) for k in (1,2,3,4)],
        'two_adic_signed_prefix_bound':s.two_adic_character_prefix_upper(4109,3,1),
        'odd_circle_Haar_nonHaar_solenoid':[s.nonhaar_grid_witness(m) for m in (3,97)],
        'zero_seed_decoy_permutations':[s.decoy_source_control(k) for k in (1,2,3)],
        'normality_proved':False,
        'original_source_witness_kept':True,
        'hostile_control_does_not_change_source':False,
        'proof_authority':'paper; exact finite replay; not Lean-verified infinite math',
    }
    return normalize(v)

def dump(x):return json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+'\n'

def verify(path=OUT):
    expected=build_receipt()
    got=json.loads(Path(path).read_text(encoding='utf-8'))
    if got != expected: raise ArithmeticError('source-hash or mathematical receipt mismatch')
    if got['normality_proved'] is not False:raise ArithmeticError('false normality promotion')
    return expected

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--verify',action='store_true')
    opt=ap.parse_args()
    if opt.write:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(dump(build_receipt()),encoding='utf-8')
        print(f'WRITTEN {OUT.relative_to(ROOT)}')
    else:
        verify()
        print('VERIFIED exact source-hashed pointed-circle solenoid/2-adic-clock receipt')
