"""Compare distinct direct arc-sweep implementation against exact rational field intervals."""
from __future__ import annotations
from mpmath import mp
from golden_aperture import epoch_energy, selected_states
from independent_oracle import arc_sweep_energy,raw_states
from finite_probe import outward_decimal
import json

def main():
    states=selected_states(2*128-1)
    indep=raw_states(2*128-1)
    assert states==indep, 'four-pole vs combined source differs'
    results=[]
    with mp.workdps(85):
        for A in [8,16,32,64,128]:
            v=mp.mpf(arc_sweep_energy(indep[A:2*A],80))
            lo,hi,_=epoch_energy(A,states)
            L=mp.mpf(lo.numerator)/lo.denominator
            H=mp.mpf(hi.numerator)/hi.denominator
            assert L < v < H, (A,mp.nstr(L,65),mp.nstr(v,65),mp.nstr(H,65))
            results.append({'A':A,'oracle_sweep_decimal':mp.nstr(v,45),'exact_interval':outward_decimal(lo,hi)})
    print(json.dumps({'verdict':'PASS','independence':'separate combined-source recurrence and direct arc sweep; same mathematical definitions, not blind referee','cases':results},indent=2))

if __name__=='__main__':main()
