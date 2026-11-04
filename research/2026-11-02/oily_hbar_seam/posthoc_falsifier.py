#!/usr/bin/env python3
"""POST-HOC RIGOROUS NEGATIVE certificate: G<2Q/N is NOT universal.

The h values below were selected after an exploratory FLOAT scan at N=4096,
Q=16, h=1..4096. They are NOT preregistered or blind. The strict
FALSIFICATION is separately proved by exact rational source, Machin pi,
dyadic phase grid and outward real/imag intervals. Never promote to
a statement against eventual fixed-h Weyl cancellation.
"""
from fractions import Fraction as F
from pathlib import Path
import json,time
from conditional_interval import source, phase_approx, COMPONENT_ERR, SCALE

N=4096; Q=16; H=[1203,1800,3576]
start=time.monotonic()
u=F(); states=[u]
for n in range(1,N):
    u=16*u+source(n)
    states.append(u)

results=[]
for h in H:
    groups=[[0,0] for _ in range(Q)]
    for n in range(N):
        re,im=phase_approx(states[n],h)
        groups[n%Q][0]+=re; groups[n%Q][1]+=im
    L=N//Q
    # Each true grouped component magnitude is at least the recorded
    # rational polynomial component MINUS L times calibrated component error.
    E_lower=sum((max(F(),F(abs(re),SCALE)-L*COMPONENT_ERR)**2+
                 max(F(),F(abs(im),SCALE)-L*COMPONENT_ERR)**2
                 for re,im in groups),F())
    G_lower=F(Q,N*N)*E_lower
    cutoff=F(2*Q,N)
    result={"N":N,"Q":Q,"h":h,
            "G_lower_floor_1e9":int(G_lower*10**9),
            "strict_threshold_1e9":int(cutoff*10**9),
            "relative_lower_floor_1e9":int(G_lower*F(N,Q)*10**9),
            "threshold_relative":2,
            "strict_counterexample":G_lower>cutoff}
    print(result,flush=True)
    assert result["strict_counterexample"],result
    results.append(result)

receipt={"scope":"POST-HOC NEGATIVE; refutes universal all-N/all-h G<2Q/N",
         "source":"exact original signed four-pole, literal U0=0",
         "provenance":"exploratory float search N4096,Q16,h1..4096 selected h1203/1800/3576; exact Fraction certification AFTER selection",
         "phase_error":"same Machin/Taylor rational enclosure as conditional_interval.py",
         "results":results,"all_strict_counterexamples":True,
         "seconds_for_display_only":round(time.monotonic()-start,3)}
Path(__file__).with_name("POSTHOC_FALSE_BOUND.json").write_text(json.dumps(receipt,indent=2)+"\n")
print("ALL POST-HOC ORIGINAL-SOURCE STRICT COUNTEREXAMPLES CERTIFIED")
