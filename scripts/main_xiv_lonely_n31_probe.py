"""Independent exact circular-band enumeration for 2-entry Lonely Runner.

A conditional census: completeness of the w1,w2 search domain depends on
GAMMA-05 and the baseline-gap bound from SUCC PRs #351/#353.

The finite cover test itself is exact integer/rational arithmetic and does not
import any SUCC search code. This script is not a proof of the universal bound.
"""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
from collections import Counter
import json, sys, time

def ceil_fraction(x):
    return -(-x.numerator // x.denominator)

def whole_covered_intervals(vs,n):
    bands=[]
    for v in vs:
        for k in range(v+1):
            lo=max(F(0), F(n*k-1,n*v))
            hi=min(F(1), F(n*k+1,n*v))
            if lo<=hi: bands.append((lo,hi))
    bands.sort()
    if not bands: return [(F(0),F(1))]
    end=F(0); gaps=[]
    for lo,hi in bands:
        if lo>end: gaps.append((end,lo))
        if hi>end: end=hi
    if end<1: gaps.append((end,F(1)))
    return gaps

def after_one(gaps,w,n):
    res=[]
    for a,b in gaps:
        first=max(0,w*a.numerator//a.denominator -1)
        last=min(w-1,w*b.numerator//b.denominator +1)
        for k in range(first,last+1):
            c=F(n*k+1,n*w); d=F(n*(k+1)-1,n*w)
            lo=max(a,c); hi=min(b,d)
            if lo<hi:res.append((lo,hi))
    return res

def test_w2(gaps,w2,n):
    for a,b in gaps:
        # exists integer k with w2*b - 1/n <= k <= w2*a + 1/n
        lo=w2*b-F(1,n); hi=w2*a+F(1,n)
        if ceil_fraction(lo)>hi.numerator//hi.denominator:
            return False
    return True

def scan(n, dual=False):
    start=time.monotonic()
    counters=Counter(); accepted=[]; pair_summary=[]
    for r,s in combinations(range(1,n),2):
        S=tuple(v for v in range(1,n) if v not in (r,s))
        baseline=whole_covered_intervals(S,n)
        assert baseline, (n,r,s)
        ell=max(b-a for a,b in baseline)
        # Universal B_n from GAMMA-05, plus exact length occupancy from #353.
        Bn={5:F(56),6:F(60)}.get(n,F((n-2)**2*(n-1),n-4))
        Brad=F(4*(n-2),n*(n-4))/ell
        B=min(Bn,Brad)
        maxw1=ceil_fraction(B)-1
        ctr=Counter(); centres=[]
        for a in (r,s):
            if not any(v%a==0 for v in S): centres.append(a)
        for w1 in range(n,maxw1+1):
            ctr['w1_rows']+=1
            residual=after_one(baseline,w1,n)
            assert residual, (n,r,s,w1) # follows one-insertion-hole (universal)
            maxgap=max(b-a for a,b in residual)
            cap1=F(2,n)/maxgap
            cap2=2*(n-1)*w1
            maxw2=min(cap1.numerator//cap1.denominator, cap2)
            if maxw2<=w1: continue
            needed=1
            for a in centres:
                if w1%a: needed=lcm(needed,a)
            # Iterate multiples of needed if needed>1
            lo=((w1+needed)//needed)*needed
            for w2 in range(lo, maxw2+1,needed):
                ctr['w2_checked']+=1
                pred=test_w2(residual,w2,n)
                if dual:
                    actual=whole_covered_intervals((*S,w1,w2),n)
                    assert pred == (not actual), (n,r,s,w1,w2,pred,actual)
                    ctr['dual_full_cover_checks']+=1
                if pred:
                    actual=whole_covered_intervals((*S,w1,w2),n)
                    assert not actual, (n,r,s,w1,w2,actual)
                    accepted.append((n,r,s,w1,w2))
        counters.update(ctr)
        pair_summary.append((r,s,ctr['w1_rows'],ctr['w2_checked']))
    return {'n':n, 'accepted':accepted, 'counts':dict(counters),
            'pairs':len(pair_summary),'elapsed_seconds':round(time.monotonic()-start,3),
            'max_w2_trials_pair':max(pair_summary,key=lambda x:x[-1])}
if __name__=='__main__':
    dual='--dual' in sys.argv
    ns=[int(x) for x in sys.argv[1:] if x!='--dual'] or [5,8,31]
    for n in ns:
        result=scan(n,dual=dual)
        print(json.dumps(result, sort_keys=True),flush=True)
