"""Source-selected BBP long-lag near returns, with CERTIFIED rational error.

All coordinates come from exact Fraction state recurrence. Convert each to the
lower cell of a fixed denominator D=10**22, so the counted pair triangle
satisfies |J_true-J_grid|<2*q*q/D. All classification uncertainties are
checked for an empty set (none within 2q integer units of a threshold).
"""
from fractions import Fraction as Q
from math import isqrt
from gaussian_circle_probe import bbp_forcing,bbp_alpha_prefix
D=10**22
EPOCHS=(257,509)

def approximate_source_epoch(A,seed):
    u=Q(seed); out=[]
    for n in range(1,2*A):
        u=(16*u+bbp_forcing(n))%1
        if n>=A:
            digit=(u.numerator*D)//u.denominator
            assert 0<=digit<D
            out.append(digit)
    assert len(out)==A
    return out

def energy_per_lag(xs,q):
    A=len(xs); small=(A.bit_length()-1)//2; medium=isqrt(A)
    count=[0]*3;weights=[0]*3; ambiguous=0
    for i in range(A-1):
        x=xs[i]
        for j in range(i+1,A):
            delta=abs(x-xs[j]); delta=min(delta,D-delta)
            surplus=D-q*delta
            if abs(surplus)<=2*q: ambiguous+=1
            if surplus>0:
                lag=j-i
                cat=0 if lag<=small else (1 if lag<=medium else 2)
                count[cat]+=1; weights[cat]+=surplus
    j_grid=Q(q*(A*D+2*sum(weights)),A*A*D)
    eps=Q(2*q*q,D)
    return {'J':j_grid,'err':eps,'count':count,'weights':weights,
            'ambiguous':ambiguous,'small':small,'medium':medium}

def run():
    for A in EPOCHS:
        q=A.bit_length()-1
        for label,seed in [('zero',Q()),('shadow',-bbp_alpha_prefix(2*A+12))]:
            xs=approximate_source_epoch(A,seed)
            s=energy_per_lag(xs,q)
            assert s['ambiguous']==0, (A,label,s['ambiguous'])
            print({'A':A,'q':q,'seed':label,
                   'J_grid':round(float(s['J']),9),
                   'guaranteed_absolute_J_error_lt':str(s['err']),
                   'count_by_lag':s['count'], 'small_lag_k':s['small'],
                   'medium_lag_k':s['medium'],
                   'energy_contributions':[
                      round(float(Q(2*q*w,A*A*D)),9) for w in s['weights']]},flush=True)
    print('All source values rational/exact. Printed J values are rounded reports with exact 2q²/D enclosures. No pi asymptotic.',flush=True)

if __name__=='__main__':run()