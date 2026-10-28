"""Deterministic exact Seinfeld coherence/checkpoint receipt; no pi oracle."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
from observational_succ import seinfeld_coherence_groups as s

ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/'research'/'2026-10-26'/'SEINFELD_COHERENCE_GROUPS_RECEIPT.json'
SOURCE=ROOT/'observational_succ'/'seinfeld_coherence_groups.py'

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    if isinstance(x,dict):return {str(k):encode(v) for k,v in sorted(x.items())}
    return x

def receipt():
    e=[0]*16;o=[0]*16;e[0]=o[1]=1
    v={
     'schema':1,
     'source_module_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
     'parent_commit':'79344c62c39c96755b742700b3d4d22fa60d86da',
     'reference_law':'independent uniform 16-branch histories',
     'prefix_kl_bases':{str(k):s.prefix_information(4,k) for k in (0,2,4)},
     'minimal_phase_quotients':{str(h):s.phase_partition_certificate(h) for h in (1,2,4,8,16)},
     'global_working_parity':s.conditional_parity_checkpoint((e,o)),
     'reference_checkpoint_energy_at_N8':{str(t):s.reference_checkpoint_energy(8,t,1) for t in (0,1,4,8)},
     'all_zero_selected_checkpoint_at_N8':{str(t):s.constant_selected_checkpoint(8,t) for t in (0,1,4,8)},
     'reinforcement_energy':{str(n):s.polya_fourier_second_moment(n) for n in (2,16,256)},
     'nonlumpable_quotient':s.quotient_transition((0,1,2,3),(0,1,0,1),
             ((0,1,0,0),(1,0,0,0),(0,0,1,0),(0,0,1,0))),
     'pi_base16_normality_proved':False,
     'selected_source_fourier_saving_proved':False}
    return encode(v)

def main():
    ap=argparse.ArgumentParser()
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true')
    opt=ap.parse_args()
    data=json.dumps(receipt(),sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    if opt.write:
        RECEIPT.parent.mkdir(exist_ok=True,parents=True)
        RECEIPT.write_text(data,encoding='utf-8')
    else:
        if RECEIPT.read_text(encoding='utf-8')!=data:
            raise SystemExit('MUTATED SEINFELD CHECKPOINT RECEIPT')
    print('CHECKPOINT_'+('WRITTEN' if opt.write else 'VERIFIED'),hashlib.sha256(data.encode()).hexdigest())
if __name__=='__main__':main()
