"""Preregistered large original BBP golden aperture energy windows.

After initial exact Fraction cumulative-distance performance barrier, use a
rigorous fixedpoint interval for pair distances (exact rational inputs).

Writes each completed exact certificate immediately so timeouts are visible.
"""
import json,time,sys,argparse
from pathlib import Path
from fractions import Fraction as F
from golden_aperture import selected_states,golden_aperture_interval_fast,golden_energy_tail_transport_upper
from finite_probe import outward_decimal

root=Path(__file__).resolve().parent
path=root/'LARGE_RESULTS.json'
parser=argparse.ArgumentParser()
parser.add_argument('--include-4096',action='store_true',help='attempt unverified timeout-prone largest preregistered case')
args=parser.parse_args()
A_values=[1024,2048]+([4096] if args.include_4096 else [])
results={'status':'PARTIAL','source':'original four signed BBP forcing, literal U_0=0',
         'preregistration':'PREREG_LARGE_EPOCHS.md, committed before measuring these A',
         'scope':'certified finite, not asymptotic', 'samples':[],
         'preregistered_unverified':[4096] if not args.include_4096 else []}
for A in A_values:
    t=time.perf_counter()
    states=selected_states(2*A-1)
    lo,hi,info=golden_aperture_interval_fast(states[A:2*A],digits=30)
    err=golden_energy_tail_transport_upper(A)
    sample={'A':A,'epoch':[A,2*A],
            'source_energy_certified_outward':outward_decimal(lo,hi),
            'completed_pi_energy_certified_outward':outward_decimal(max(F(0),lo-err),hi+err),
            'transport_absolute_upper':outward_decimal(F(0),err),
            'ordered_pairs_within_golden_b':info['near_ordered_pairs'],
            'elapsed_seconds_noncertifying':round(time.perf_counter()-t,3)}
    results['samples'].append(sample)
    results['status']='COMPLETE' if A==4096 else 'PARTIAL_HOLDOUTS'
    path.write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
    print('A',A,'E',sample['source_energy_certified_outward'],
          'count',sample['ordered_pairs_within_golden_b'],
          'seconds',sample['elapsed_seconds_noncertifying'],flush=True)
