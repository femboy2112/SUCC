# CB-1 with the seed as a free parameter: x_n arbitrary in [0,1). Place y=x_{n+d} exactly ON / just off the
# window endpoints eps, sigma, and at 0 and just below 1. Far past the fitting window: n up to 2^61.
import random
from fractions import Fraction as F
random.seed(1)
def r(n): return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
def S(k,n,rr=r):
    t=F(0)
    for j in range(1,k+1): t=16*t+rr(n+j)
    return t
def check(n,d,rr=r,trials=None):
    sig=S(d,n,rr); out=[]
    if not sig<1: return None
    for m in range(1,d):
        k=d-m; eps=S(m,n+k,rr); delta=(16**m*S(k,n,rr))%1
        tiny=F(1,10**60)
        for Y in [eps,sig,eps-tiny,sig-tiny,eps+tiny,F(0),1-tiny,(eps+sig)/2]:
            Y=Y%1
            for j in [0,1,16**d-1,random.randrange(16**d)]:
                x=(((Y-sig)%1)+j)/16**d   # then {16^d x + sig} = Y
                assert (16**d*x+sig)%1==Y
                theta=(16**d*x)%1
                bdef=int(theta+delta>=1); bwin=int(eps<=Y<sig)
                out.append((bdef==bwin and delta==sig-eps,(n,m,k,Y)))
    return out
tot=0;bad=[]
ns=list(range(1,300))+[2**(2*d-3)+e for d in range(2,32) for e in (-2,-1,0,1,2)]+[random.randrange(2,2**61) for _ in range(200)]
for n in ns:
    if n<1: continue
    d=2
    while d<70:
        res=check(n,d)
        if res is None: break
        for ok,info in res:
            tot+=1
            if not ok: bad.append(info)
        d+=1
print("original forcing: checks",tot,"mismatches",len(bad),bad[:3])
# maximal-d near-1 cases: report closest S_d(n) to 1 from below among n=2^(2d-3)+e
best=min(((1-S(d,2**(2*d-3)+e)),d,e) for d in range(2,30) for e in range(-3,4) if S(d,2**(2*d-3)+e)<1)
print("closest 1-S_d(n) (float):",float(best[0]),"at d,e",best[1:])
# mutants: one-pole positive; and a forcing with ONE negative term (outside hypothesis)
one=lambda n:F(4,8*n-7)
tot=0;bad=[]
for n in range(1,200):
    d=2
    while d<20:
        res=check(n,d,one)
        if res is None: break
        for ok,info in res:
            tot+=1; bad+= [] if ok else [info]
        d+=1
print("one-pole positive mutant: checks",tot,"mismatches",len(bad))
neg=lambda n: (F(-1,1000) if n==50 else F(1,100*n*n))
tot=0;bad=[]
for n in range(40,50):
    for d in range(2,6):
        res=check(n,d,neg)
        if res is None: continue
        for ok,info in res:
            tot+=1; bad+= [] if ok else [info]
print("forcing with one negative term (outside CB-1 hypothesis): checks",tot,"mismatches",len(bad),bad[:2])
