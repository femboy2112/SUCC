"""Exploratory Q-split golden return energies. Not preregistered, not blind."""
import json,time
from pathlib import Path
from golden_aperture import selected_states,golden_return_energy_interval_fast
from finite_probe import outward_decimal

res={'status':'exploratory finite; not blind; no asymptotic bound','samples':[]}
for A,Q_list in [(1024,[8,16,32,64]),(2048,[16,32,64,128])]:
    t=time.perf_counter();states=selected_states(2*A-1);pts=states[A:2*A]
    for Q in Q_list:
        lo,hi,d=golden_return_energy_interval_fast(pts,Q,28)
        rec={'A':A,'Q':Q,'M':A//Q,'golden_return_energy_certified':outward_decimal(lo,hi),
             'near_count':d['ordered_near_pairs'],'ambiguous':d['ambiguous_fallbacks']}
        res['samples'].append(rec)
        print(A,Q,rec['golden_return_energy_certified'],flush=True)
res['duration_seconds_diagnostic']=round(time.perf_counter()-t,3)
Path(__file__).resolve().parent.joinpath('FIBER_PROBE.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
