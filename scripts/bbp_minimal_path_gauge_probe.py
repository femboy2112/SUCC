"""Deterministic exact-receipt printer for the BBP minimal-path experiment.

The rational hash is authoritative for *finite replay*; machine-complex
spectral values are labeled APPROXIMATE and excluded from the exact digest.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import isqrt
from observational_succ.bbp_minimal_path_gauge import single_missing_prime_counterfeit
from observational_succ.bbp_source_memory import forcing
from observational_succ.bbp_cyclotomic_spectral import single_prime_spectral_ledger


def finite_receipt() -> dict:
    trial=single_missing_prime_counterfeit(100,period=30,missing_prime=3,
                                           precision=Q(1,10**6),frozen_prefix=6)
    records=trial['records']
    lines=[f"{r['n']}|{r['authentic_phase']}|{r['counterfeit_phase']}|{r['source']}|{r['forcing_error']}"
           for r in records]
    frozen=sum(int(r['forcing_error']==0) for r in records[:6])
    assert frozen==6
    assert all(r['counterfeit_phase'].denominator%2==1 for r in records)
    assert all(r['forcing_error']<=Q(1,10**6)/16**r['n'] for r in records)
    assert all(r['source']>0 for r in records)
    exact={
      'status':'finite-exact-only-not-normality',
      'parent':'femboy2112/SUCC PR #256 head 0683f8f166b9106ab8405a2d6538415b5ac84ba3',
      'q_missing':3,'period':30,'frozen_prefix':6,'horizon':len(records),
      'all_odd_denominators':True,
      'exponential_source_error_verified':True,
      'positive_forcing_verified':True,
      'first_mutated_n':next(r['n'] for r in records if r['forcing_error']>0),
      'exact_frozen_count':frozen,
      'max_forcing_error':str(max(r['forcing_error'] for r in records)),
      'initial_contact_bound':str(trial['initial_contact_bound']),
      'selected_periodic_z0':str(trial['z0']),
      'rational_rows_sha256':hashlib.sha256(('\n'.join(lines)+'\n').encode()).hexdigest(),
    }
    spectral=[]
    for p in (17,41,73,97,113,193,257,313,401):
        r=single_prime_spectral_ledger(p)
        spectral.append({
            'p':p,'L':r['L'],'B':r['blocks'],
            'abs_full_complex_approx':f'{abs(r["full"]):.6f}',
            'abs_local_zero_mode_approx':f'{abs(r["local_mean"]):.6f}',
            'abs_signed_mixed_approx':f'{abs(r["mixed"]):.6f}',
            'absolute_gauss_bound_approx':f'{r["gauss_upper_nonzero"]:.6f}',
        })
    return {'exact_fraction':exact,'approx_complex_diagnostic_not_proof':spectral}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', default=None)
    args=parser.parse_args()
    out=json.dumps(finite_receipt(),sort_keys=True,indent=2)+'\n'
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(out)
    else:print(out,end='')

if __name__=='__main__':main()
