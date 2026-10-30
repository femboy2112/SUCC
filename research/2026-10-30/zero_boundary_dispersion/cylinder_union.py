"""Exact bounded-slip inverse-cylinder union, with a separate forward oracle."""
from fractions import Fraction as F
from math import isqrt
import json


def r(n): return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def centered(x): return x-((x+F(1,2)).numerator//(x+F(1,2)).denominator)


def merge(intervals):
    out=[]
    for a,b in sorted(intervals):
        if not out or a>out[-1][1]: out.append([a,b])
        else: out[-1][1]=max(b,out[-1][1])
    return out


def inverse_union(A,L,h,K,delta=F(1,20)):
    if A<1 or L<1 or h==0 or K<0 or not 0<delta<F(1,2):
        raise ValueError('invalid finite cylinder domain')
    active={0:[[-F(1,2),F(1,2)]]}
    scale=1; offset=F()
    counts=[]
    for j in range(L):
        nxt={}
        for cost, intervals in active.items():
            for left,right in intervals:
                yl=scale*left+offset; yr=scale*right+offset
                for m in range(yl.numerator//yl.denominator-1,
                               yr.numerator//yr.denominator+2):
                    for lo,hi,extra in ((m-delta,m+delta,0),
                                         (m+delta,m+1-delta,1)):
                        used=cost+extra
                        if used>K: continue
                        a=max(left,(lo-offset)/scale)
                        b=min(right,(hi-offset)/scale)
                        if a<=b: nxt.setdefault(used,[]).append([a,b])
        active={cost:merge(iv) for cost,iv in nxt.items()}
        counts.append(sum(len(x) for x in active.values()))
        if counts[-1]>200000: raise RuntimeError('declared branch cap exceeded')
        offset=16*offset+h*(r(A+j+2)-r(A+j+1))
        scale*=16
    union=merge([iv for group in active.values() for iv in group])
    return union,counts


def forward_count(x,A,L,h,delta=F(1,20)):
    count=0; boundary=False
    for j in range(L):
        x=centered(x)
        boundary |= abs(x)==delta
        count += abs(x)>delta
        x=16*x+h*(r(A+j+2)-r(A+j+1))
    return count,boundary


def contains(union,x): return any(a<=x<=b for a,b in union)


def run():
    rows=[]; oracle_checks=0
    for p in (1153,1201):
        assert all(p%d for d in range(2,isqrt(p)+1))
        A=(p+7)//8
        u=sum((16**(A-k)*r(k) for k in range(1,A+1)),F())
        for h in (1,5):
            x=centered(h*(15*u+r(A+1)))
            for L in (6,8,10):
                union,counts=inverse_union(A,L,h,1)
                direct,boundary=forward_count(x,A,L,h)
                assert not boundary
                assert not contains(union,x) and direct>1
                for j in range(-64,65):
                    v=F(j,131)
                    cost,touch=forward_count(v,A,L,h)
                    if not touch:
                        assert contains(union,v)==(cost<=1)
                        oracle_checks+=1
                # Truncated original Green lag is a coherent coordinate.
                R=L+16
                d=sum((F(1,16**t)*(r(A+t)-r(A+t+1))
                       for t in range(1,R+1)),F())
                shadow=h*d
                cost,touch=forward_count(shadow,A,L,h)
                assert not touch and cost==0 and contains(union,shadow)
                # Uniform omitted Green-lag error after transport is tiny.
                error=abs(h)*F(16,16**R*(8*(A+R)+1)**3)*16**(L-1)
                assert abs(h)*F(16,(8*A+1)**3)+error<F(1,20)
                rows.append({'p':p,'A':A,'L':L,'h':h,'budget':1,
                    'component_count':len(union),'stage_counts':counts,
                    'union_measure':str(sum((b-a for a,b in union),F())),
                    'authentic_strict_slips':direct,'authentic_outside':True,
                    'coherent_coordinate_inside':True,'coherent_error_bound':str(error)})
    return {'status':'PASS','rows':rows,'forward_grid_checks':oracle_checks,
            'scope':'exact bounded-slip union on short prefixes; no asymptotic inference'}


if __name__=='__main__': print(json.dumps(run(),indent=2))
