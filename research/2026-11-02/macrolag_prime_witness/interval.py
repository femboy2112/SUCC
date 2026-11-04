#!/usr/bin/env python3
"""Exact rational-interval certifications for finite ORIGINAL BBP prime windows.

A certificate uses exact rational orbit, rational Machin pi bounds, dyadic
phase quantization, rational Taylor polynomials and a rigorous global error.
Finite only! No extrapolation to normality.
"""
from fractions import Fraction as F
from math import factorial, isqrt
import json
import time
from pathlib import Path

Q=2**19   # phase resolution
SCALE=10**9
DEG=20


def atan_interval_inv(a,terms=13):
    # series sum j=0..terms-1 (-1)^j/(2j+1)a^(2j+1)
    seq=sum((F((-1)**j,(2*j+1)*a**(2*j+1)) for j in range(terms)),F(0))
    rem=F(1,(2*terms+1)*a**(2*terms+1))
    return (seq,seq+rem) if terms%2==0 else (seq-rem,seq)

A,B=atan_interval_inv(5,14)
C,D=atan_interval_inv(239,14)
PI_LO=16*A-4*D
PI_HI=16*B-4*C
PI_MID=(PI_LO+PI_HI)/2
assert PI_LO<PI_MID<PI_HI<F(22,7)
R_TAYLOR=F(22,7)**(DEG+1)/factorial(DEG+1)
E_PHASE=F(44,7)/Q + (PI_HI-PI_LO)
E_COMPONENT=F(1,SCALE)+R_TAYLOR+E_PHASE


def R(n):
    a=8*n-7
    return F(15*a*a+121*a+240,a*(a+3)*(a+4)*(a+5))


def coeffs_sincos(theta):
    term=F(1); re=F(1); im=F(0)
    for j in range(1,DEG+1):
        term*=theta/j
        if j%4==0:re+=term
        elif j%4==1:im+=term
        elif j%4==2:re-=term
        else:im-=term
    return int(re*SCALE),int(im*SCALE)


def candidates(start=4000,amount=4):
    out=[]
    for p in range(start+1,start+3000):
        if p%8==5 and all(p%d for d in range(2,isqrt(p)+1)):
            out.append(p)
            if len(out)>=amount:break
    return out


def produce(p,hlist=(1,3,5,7),threshold=F(1,8)):
    assert p%8==5
    k=(p-5)//8
    lo=k+1; hi=4*k+2;L=hi-lo+1
    U=F(0)
    sums={h:[0,0] for h in hlist}
    t0=time.monotonic()
    for n in range(1,hi+1):
        U=16*U+R(n)
        if n<lo:continue
        for h in hlist:
            pz=(h*U.numerator)%U.denominator
            j=(pz*Q)//U.denominator
            if j>=Q//2:j-=Q
            th=2*PI_MID*F(j,Q)
            x,y=coeffs_sincos(th)
            sums[h][0]+=x; sums[h][1]+=y
    result={"p":p,"start":lo,"end":hi,"L":L,"harmonics":{},"seconds":round(time.monotonic()-t0,3)}
    for h,(re,im) in sums.items():
        upper=F(abs(re)+abs(im),L*SCALE)+2*E_COMPONENT
        result["harmonics"][str(h)]={"upper_num":upper.numerator,"upper_den":upper.denominator,
            "upper_decimal":float(upper),"pass":upper<threshold}
    return result

if __name__=='__main__':
    t=time.monotonic()
    out={"method":"exact Fraction source, Machin pi, dyadic floor, Taylor/Lagrange", "phase_grid":Q,"Taylor_degree":DEG,"Taylor_component_error":str(R_TAYLOR),"pi_width":str(PI_HI-PI_LO),
         "preselected_primes":candidates(4000,3),"preselected_harmonics":[1,3,5,7],"threshold":"1/8","results":[]}
    for p in out['preselected_primes']:
        rr=produce(p)
        out['results'].append(rr)
        print(p, {h:(v['upper_decimal'],v['pass']) for h,v in rr['harmonics'].items()},rr['seconds'],flush=True)
    out['elapsed_seconds']=round(time.monotonic()-t,3)
    with open(Path(__file__).with_name('FINITE_WINDOWS_RAW_4000.json'),'w') as f:json.dump(out,f,indent=2)
    assert all(v['pass'] for r in out['results'] for v in r['harmonics'].values())
