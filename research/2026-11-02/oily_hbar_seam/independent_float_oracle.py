#!/usr/bin/env python3
"""Separate combined-rational BBP source and double complex trig: DIAGNOSTIC ONLY."""
from fractions import Fraction as F
from math import pi,cos,sin
from pathlib import Path
import json

def src_combined(n):
    a=120*n*n-89*n+16
    d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return F(a,d)

Ns=(768,1536,3072);hs=(9,11,17);Qs=(16,256)
u=F(0);phases=[]
for n in range(max(Ns)):
    if n:u=16*u+src_combined(n)
    phases.append(u%1)
result=[]
prior=json.loads(Path(__file__).with_name('CONDITIONAL_HOLDOUTS.json').read_text())
upper={(a['N'],a['h'],a['Q']):a['G_upper_1e9']/10**9 for a in prior['results']}
for h in hs:
    z=[complex(cos(2*pi*float((h*x)%1)),sin(2*pi*float((h*x)%1))) for x in phases]
    for N in Ns:
        for Q in Qs:
            s=[0j]*Q
            for n in range(N):s[n%Q]+=z[n]
            G=Q*sum(abs(v)**2 for v in s)/N**2
            assert G<upper[N,h,Q]+2e-10,(N,h,Q,G,upper[N,h,Q])
            result.append({'N':N,'h':h,'Q':Q,'diagnostic_G':G,'certified_upper':upper[N,h,Q]})
            print('independent',N,h,Q,'G=',format(G,'.10g'),'strict interval',format(upper[N,h,Q],'.10g'))
assert len(result)==18
out={'source':'independent exact combined rational BBP numerator/denominator, float trig diagnostic', 'results':result}
Path(__file__).with_name('INDEPENDENT_FLOAT.json').write_text(json.dumps(out,indent=2)+'\n')
print('FLOAT_DIAGNOSTIC_ONLY 18/18 WITHIN RIGOROUS UPPERS')
