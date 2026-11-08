"""Predeclared original-source holdouts; integer-only certificate calculations."""
from __future__ import annotations
import json, time
from fractions import Fraction as F
from golden_aperture import selected_states,epoch_energy,golden_return_energy_bounds,golden_b_bounds,transport_bound_approx,completed_energy_bounds_from_original,golden_energy_tail_transport_upper
from pathlib import Path


def outward_decimal(l:F,u:F,digits:int=14)->list[str]:
    if l>u:raise ValueError('not enclosure')
    scale=10**digits
    lv=l.numerator*scale//l.denominator
    uv=-((-u.numerator*scale)//u.denominator) # ceil positive/negative using integer arithmetic
    def fmt(v):
        return f"{'-' if v<0 else ''}{abs(v)//scale}.{abs(v)%scale:0{digits}d}"
    return [fmt(lv),fmt(uv)]


def run():
    t0=time.perf_counter(); As=[79,157,281,389]
    states=selected_states(2*max(As)-1)
    out={'claim':'FINITE ORIGINAL ZERO-SEED GOLDEN APERTURE ENERGY; no asymptotic inference',
         'precision':'Q(sqrt5) intervals using exact Fraction and integer isqrt at 35 decimals',
         'predeclared_epochs':As,'samples':[]}
    for A in As:
        t=time.perf_counter(); l,u,d=epoch_energy(A,states)
        eps=golden_energy_tail_transport_upper(A)
        out['samples'].append({'epoch':[A,2*A],'A':A,'golden_energy_enclosure':outward_decimal(l,u),
                     'near_ordered_pairs':d['near_ordered_pairs'],
                     'completed_pi_energy_enclosure':outward_decimal(max(F(0),l-eps),u+eps),
                     'source_to_pi_energy_upper':outward_decimal(F(0),eps),
                     'relative_analytic_transport_upper_float_diagnostic':transport_bound_approx(A),
                     'elapsed_seconds_float_diagnostic':round(time.perf_counter()-t,3)})
        print('A',A,'E',outward_decimal(l,u),'near',d['near_ordered_pairs'],'sec',round(time.perf_counter()-t,2),flush=True)
    for A in [64,128]:
        pts=states[A:2*A]
        d=[]
        for Q in [1,2,4,8,16]:
            l,u,v=golden_return_energy_bounds(pts,Q)
            d.append({'Q':Q,'M':A//Q,'energy_enclosure':outward_decimal(l,u)})
        out.setdefault('double_triangle',[]).append({'epoch':[A,2*A],'fibers':d})
        print('FIBERS A',A,[(v['Q'],v['energy_enclosure']) for v in d],flush=True)
    out['runtime_seconds_float_diagnostic']=round(time.perf_counter()-t0,3)
    path=Path(__file__).resolve().parent/'FINITE_RESULTS.json'
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    return out

if __name__=='__main__':run()
