from collections import Counter
from fractions import Fraction
import sympy as S
x,t=S.symbols('x t')
A=120*x*x-89*x+16
D=(2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
W=S.expand(S.diff(A,x)*D-A*S.diff(D,x));Wp=S.diff(W,x)
print('W:',W)
print('W mod7 factor:',S.factor(W, modulus=7))

def ev(f,n,p):return int(f.subs(x,n))%p

def canon(n,q,p):
    a=(120*n*n-89*n+16)%q
    d=((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))%q
    # Opposite chart priority from constructor: use A whenever possible.
    return (1,d*pow(a,-1,q)%q) if a%p else (a*pow(d,-1,q)%q,1)

def deriv(n,p,recip=False):
    a=ev(A,n,p);d=ev(D,n,p);w=ev(W,n,p)
    return -w*pow(a*a,-1,p)%p if recip else w*pow(d*d,-1,p)%p

for p,maxL in [(7,5),(11,3),(241,2)]:
    crit=[n for n in range(p) if ev(W,n,p)==0]
    # Cross-product comparisons avoid using any projective chart for the base certificate.
    cp=[(i,j) for i in range(p) for j in range(p) if (ev(A,i,p)*ev(D,j,p)-ev(A,j,p)*ev(D,i,p))%p==0]
    assert len(cp)=={7:19,11:27,241:497}[p]
    assert all(ev(Wp,c,p)!=0 for c in crit)
    assert all(sum(i==c for i,j in cp)==1 for c in crit)
    assert all(ev(W,n,p) or ev(W,n+1,p) for n in range(p))
    off2=[(i,j) for i,j in cp if i<j and (ev(A,i+1,p)*ev(D,j+1,p)-ev(A,j+1,p)*ev(D,i+1,p))%p==0]
    assert off2=={7:[(2,3)],11:[(2,4)],241:[]}[p]
    print('base',p,'critical',crit,'Wprime',[ev(Wp,c,p) for c in crit], 'C1',len(cp),'off2',off2)
    for a,b in off2:
        # These residues and their successors have A units at both small primes.
        det=(-deriv(a,p,True)*deriv(b+1,p,True)+deriv(b,p,True)*deriv(a+1,p,True))%p
        print('reciprocal two-delay determinant',p,det)
        assert det
    for L in range(1,maxL+1):
        q=p**L
        vals=[canon(n,q,p)for n in range(q)]
        counts=[]
        for d in [1,2,3]:
            freq=Counter(tuple(vals[(n+j)%q]for j in range(d))for n in range(q))
            counts.append(sum(c*c for c in freq.values()))
        expected=[(len(cp)+len(crit)*(p-1)*(L-1))*p**(L-1),q+(2 if p in (7,11)else 0),q]
        assert counts==expected
        print('full count',p,L,counts)
# Real source bound is independently polynomial-certified.
assert S.factor(A-47*x*x)==(x-1)*(73*x-16)
up=S.Poly(S.expand((D-x*x*A).subs(x,t+2)),t)
assert all(c>0 for c in up.all_coeffs())
print('upper bound positivity coefficients:',up.all_coeffs())
for H in range(1,10001):
    # ceil sqrt(4H), using exact integer arithmetic.
    from math import isqrt
    a=isqrt(4*H)
    if a*a<4*H:a+=1
    assert 4*H<=a*a<=9*H
    r=Fraction(120*a*a-89*a+16,(2*a-1)*(4*a-1)*(8*a-7)*(8*a-3))
    assert Fraction(47,4608)<H*r<Fraction(1,4)
print('uniform-in-h arithmetic witness passed H=1..10000; analytic proof is separate')
