"""Independent arc-sweep oracle using mpmath; diagnostics, not interval certificates.

Never imports golden_aperture.py. Source uses combined A(n)/D(n) rational formula.
"""
from __future__ import annotations
from fractions import Fraction as F
from mpmath import mp
import json


def raw_states(N:int):
    x=F(0); result=[x]
    for n in range(1,N+1):
        r=F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        x=(16*x+r)%1
        result.append(x)
    return result


def arc_sweep_energy(points, dps:int=70):
    with mp.workdps(dps):
        a=(mp.sqrt(5)-1)/2
        half=a/2
        n=len(points);ev=[];current=0
        for x in points:
            z=mp.mpf(x.numerator)/x.denominator
            st=(z-half)%1;en=(z+half)%1
            if st>en:current+=1
            ev.extend([(st,+1),(en,-1)])
        ev.sort(key=lambda z:z[0]);left=mp.mpf(0);en=mp.mpf(0)
        for loc, delta in ev:
            en+=(loc-left)*(mp.mpf(current)/(n*a)-1)**2
            current+=delta;left=loc
        en+=(1-left)*(mp.mpf(current)/(n*a)-1)**2
        return mp.nstr(en,dps-8)


def main():
    samples=[]
    states=raw_states(2*128-1)
    for A in [8,16,32,64,128]:
        val=arc_sweep_energy(states[A:2*A])
        samples.append({'A':A,'independent_arc_sweep_E':val})
    for q in [4,8,16,32,64]:
        val=arc_sweep_energy([F(i,q) for i in range(q)])
        samples.append({'uniform_grid_q':q,'independent_arc_sweep_E':val})
    print(json.dumps(samples,indent=2))

if __name__=='__main__': main()
