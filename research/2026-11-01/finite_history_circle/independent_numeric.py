"""Optional independent high-precision finite probe, NOT a proof certificate.

Uses sine(pi/2^k) for geometry, not recursive square-root implementation.
All source phases are calculated from exact rational four-pole recurrence.
"""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as F
from mpmath import mp

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source_proj_numeric',HERE/'finite_history.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
mp.dps=160

def tomp(x):
    x=F(x);return mp.mpf(x.numerator)/x.denominator

def run():
    rows=[]
    for N in [3,7,16,31]:
        k,L,J=f.refinement_plan(N,2)
        geom=2**(k+1)*mp.sin(mp.pi/(2**(k+1)))
        orbit=f.source_orbit(N)
        for h in [1,3,5]:
            actual=mp.mpc(0);pred=mp.mpc(0)
            max_delta=mp.mpf(0)
            for n in range(1,N+1):
                u=tomp(f.frac_mod_one(orbit[n]))
                ut=mp.mpf(16)**(n-1)*geom - tomp(f.finite_wilson_future(n,J))
                # Reduce loss of precision in large angular arguments.
                ut=ut-mp.floor(ut)
                ea=mp.exp(2j*mp.pi*h*u)
                ep=mp.exp(2j*mp.pi*h*ut)
                actual+=ea;pred+=ep
                max_delta=max(max_delta,abs(ea-ep))
            observed=abs(actual-pred)
            budget=tomp(f.absolute_weyl_transport_bound(N,h,2))
            op_budget=tomp(f.controlled_echo_operator_bound(N,h,2))
            assert observed < budget,(N,h,observed,budget)
            assert max_delta<op_budget,(N,h,max_delta,op_budget)
            rows.append(dict(N=N,h=h,k=k,L=L,J=J,
                             observed_absolute_error=mp.nstr(observed,35),
                             certified_bound=mp.nstr(budget,35),
                             observed_max_phase_error=mp.nstr(max_delta,35),
                             certified_operator_bound=mp.nstr(op_budget,35),
                             provenance='mpmath diagnostic, not interval proof'))
    target=HERE/'NUMERICAL_DIAGNOSTICS.json'
    target.write_text(json.dumps({'precision_dps':mp.dps,'probe_horizons':[3,7,16,31],
                                  'harmonics':[1,3,5],'rows':rows},indent=2)+'\n')
    print('independent diagnostic:',len(rows),'PASS',target)
    for row in rows:
        if row['h']==1:print(row['N'],row['k'],row['J'],row['observed_absolute_error'],row['certified_bound'])

if __name__=='__main__':run()
