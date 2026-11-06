"""Exact finite certificate of the all-radius K=3 real-pair census at fixed N.
No extrapolation to all N. Uses rational fractions from original BBP U0=0.
"""
from __future__ import annotations
from fractions import Fraction
import json
from experiment import original


def radius_census(s:list[Fraction],rad:Fraction)->int:
    N=len(s)
    assert Fraction(0)<rad<=Fraction(1,2)
    yy=s+[x+1 for x in s]
    j=0;count=0
    for i in range(N):
        j=max(j,i+1)
        while j<i+N and yy[j]-yy[i]<=rad:
            j+=1
        count+=j-i-1
    return N+2*count


def certify_N(N:int)->dict:
    s=sorted(original(N))
    rad=Fraction(1,N+1)
    records=[]
    while True:
        A=radius_census(s,rad)
        # At grid radius r, K_sample <= 9/4. Geometric interpolation <=4/3
        # yields K_all_delta<=3, as all intermediate A(delta) are monotone.
        assert (A-N)*4*rad.denominator<=9*N*N*rad.numerator, (N,rad,A)
        records.append({'radius':f'{rad.numerator}/{rad.denominator}',
                        'A':A,'excess_ratio_approx':round(float(Fraction(A-N,N*N*rad)),9)})
        if rad==Fraction(1,2):break
        rad=min(rad*Fraction(4,3),Fraction(1,2))
    return {'N':N,'radii_checked':len(records),
            'max_sampled_ratio':max(r['excess_ratio_approx'] for r in records),
            'certified_K_for_every_delta':'3',
            'delta_interval':f'[1/{N+1},1/2]',
            'records':records}


def one_step_failures(xs:list[Fraction],limit=12):
    out=[]
    for n in range(32,len(xs)):
        d=Fraction(1,n+1)
        x=xs[n]
        v=sum(min(abs(x-y),1-abs(x-y))<=d for y in xs[:n])
        # Uniform step bound B_n <=3n d ~3, needed for naive K=3 induction.
        if Fraction(v)>3*n*d:
            out.append({'n':n,'new_point_neighbours':v,
                        'one_step_threshold':f'{3*n}/{n+1}'})
            if len(out)>=limit:break
    return out


def run():
    rows=[]
    for N in (128,256,512,1024,2048):
        rows.append(certify_N(N))
    return {'scope':'CERTIFIED FINITE: for each listed N, ALL real circle radii delta in [1/(N+1),1/2]; NOT all N',
            'source':'authentic original four-pole, U0=0',
            'pi_normality':'OPEN','rows':rows,
            'naive_one_step_failures':one_step_failures(original(512))}


if __name__=='__main__':print(json.dumps(run(),indent=2))
