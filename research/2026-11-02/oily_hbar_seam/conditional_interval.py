#!/usr/bin/env python3
"""Rigorous finite conditional Fourier-energy intervals for authentic BBP source.

All complex phases are enclosed using exact rational Machin pi bounds,
integer-dyadic real phase binning and rational Taylor/Lagrange inequalities.
NO floating arithmetic enters any pass/fail. Predeclared N/h/Q in
PREREGISTRATION.md. No normality inference from finite success.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,time,sys

N_VALUES=(768,1536,3072)
H_VALUES=(9,11,17)
Q_VALUES=(16,256)
GRID=2**19
SCALE=10**9
DEG=18


def atan_limits(a,terms=14):
    S=sum((F((-1)**j,(2*j+1)*a**(2*j+1)) for j in range(terms)),F(0))
    rem=F(1,(2*terms+1)*a**(2*terms+1))
    return (S,S+rem) if terms%2==0 else (S-rem,S)

lo5,hi5=atan_limits(5)
lo239,hi239=atan_limits(239)
PI_LO=16*lo5-4*hi239
PI_HI=16*hi5-4*lo239
PI_MID=(PI_LO+PI_HI)/2
assert F(3)<PI_LO<PI_HI<F(22,7)
TAYLOR_ERR=F(22,7)**(DEG+1)/factorial(DEG+1)
PHASE_ERR=F(44,7*GRID)+(PI_HI-PI_LO)
COMPONENT_ERR=F(1,SCALE)+TAYLOR_ERR+PHASE_ERR


def source(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def rounded_sincos(theta):
    term=F(1);re=F(1);im=F(0)
    for j in range(1,DEG+1):
        term*=theta/j
        if j%4==0:re+=term
        elif j%4==1:im+=term
        elif j%4==2:re-=term
        else: im-=term
    return int(re*SCALE),int(im*SCALE)


def ceil_fraction(f):
    return -((-f.numerator)//f.denominator)


def phase_approx(fr, h):
    u=(h*fr.numerator)%fr.denominator
    grid_j=(u*GRID)//fr.denominator
    if grid_j>=GRID//2:grid_j-=GRID
    theta=2*PI_MID*F(grid_j,GRID)
    return rounded_sincos(theta)


def calculate(maxN=3072):
    assert maxN in N_VALUES
    start=time.monotonic()
    # Keep one exact ORIGINAL rational source history; independent of h and Q.
    states=[F(0)]
    for n in range(1,maxN):
        states.append(16*states[-1]+source(n))
    all_results=[]
    for h in H_VALUES:
        t=time.monotonic()
        approximate=[phase_approx(states[n],h) for n in range(maxN)]
        print('Prepared signed original source',h,'n',maxN,'secs',round(time.monotonic()-t,3),flush=True)
        for N in N_VALUES:
            if N>maxN:continue
            for Q in Q_VALUES:
                if N%Q:continue
                sums=[[0,0] for _ in range(Q)]
                for n,(re,im) in enumerate(approximate[:N]):
                    acc=sums[n%Q]
                    acc[0]+=re;acc[1]+=im
                L=N//Q
                upper=sum(((F(abs(x),SCALE)+L*COMPONENT_ERR)**2
                           +(F(abs(y),SCALE)+L*COMPONENT_ERR)**2
                           for x,y in sums),F(0))
                G_upper=F(Q,N*N)*upper
                threshold=F(2*Q,N)
                result={'N':N,'h':h,'Q':Q,'threshold':'2*Q/N',
                        'G_upper_1e9':ceil_fraction(G_upper*10**9),
                        'threshold_1e9':ceil_fraction(threshold*10**9),
                        'bound_pass':G_upper<threshold,
                        're_im_sum_abs_max':max(abs(x)+abs(y) for x,y in sums),
                        'component_error_upper':str(COMPONENT_ERR)}
                all_results.append(result)
                print('G_bound',N,h,Q,'upper:',result['G_upper_1e9']/1e9,
                      'threshold:',float(threshold), 'PASS:',result['bound_pass'],flush=True)
    out={'source':'unchanged original four-pole; literal U0=0',
         'method':'Fraction original source, Machin exact pi bracket, 2^19 grid, degree18 Taylor, per-component enclosure',
         'preregistered_harmonics':list(H_VALUES),'preregistered_horizons':list(N_VALUES),
         'preregistered_carriers':list(Q_VALUES),
         'pi_bound_width':str(PI_HI-PI_LO),
         'taylor_component_bound':str(TAYLOR_ERR),
         'angle_bound':str(PHASE_ERR),
         'complex_component_total_bound':str(COMPONENT_ERR),
         'results':all_results,
         'pass_count':sum(x['bound_pass'] for x in all_results),
         'fail_count':sum(not x['bound_pass'] for x in all_results),
         'elapsed_seconds':round(time.monotonic()-start,3)}
    dest=Path(__file__).with_name('CONDITIONAL_HOLDOUTS.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',out['pass_count'],out['fail_count'],'seconds',out['elapsed_seconds'],dest)
    assert len(all_results)==len(H_VALUES)*len(Q_VALUES)*len([n for n in N_VALUES if n<=maxN])
    return out

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 3072
    calculate(n)
