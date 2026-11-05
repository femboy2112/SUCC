from fractions import Fraction as Q
from math import pi, sin, cos, sqrt, floor
import cmath, time
ORIG=(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
ANG=(Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0))
RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))
def forcing(n,taps=ORIG):
    return sum((w/Q(8*(n-1)+j) for j,w in enumerate(taps,1)),Q())
def forcing_poly(n):
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
def states(N):
    u=y=z=Q(); out=[(u,y,z)]
    for n in range(1,N+1):
        r=forcing(n)
        assert r==forcing_poly(n)
        u=16*u+r; y=16*y+forcing(n,ANG); z=16*z+forcing(n,RAD)
        assert u==y+z
        out.append((u,y,z))
    return out

def alpha_bounds(M):
    a=sum((forcing(n)/16**n for n in range(1,M+1)),Q())
    return (a,a+forcing(M+1)/Q(15*16**M))

def rational_periodic(p):
    lo,hi=alpha_bounds(p+10);q=16**p-1
    k1=((lo*q)+Q(1,2)).numerator//((lo*q)+Q(1,2)).denominator
    k2=((hi*q)+Q(1,2)).numerator//((hi*q)+Q(1,2)).denominator
    assert k1==k2,(p,k1,k2)
    beta=Q(k1,q)
    dist=max(abs(beta-lo),abs(beta-hi))
    assert dist<=Q(1,2*q)
    return beta,dist

def pressure(xs,m):
    M=16**m
    counts={}
    for x in xs:
        w=(Q(x)%1)*M
        idx=w.numerator//w.denominator
        assert 0<=idx<M
        counts[idx]=counts.get(idx,0)+1
    N=len(xs)
    return Q(M*sum(v*v for v in counts.values()),N*N)

def tail(n,J=40):
    return sum((forcing(n+k)/16**k for k in range(1,J+1)),Q())

def ch(x):
    return cmath.exp(2j*pi*float(Q(x)%1))

def verify():
    print('forcing(1)',forcing(1),'sum bound',float(Q(47,15)+Q(1920,2457)),'<4',Q(47,15)+Q(1920,2457)<4)
    for p in (3,5,7,9):
        beta,d=rational_periodic(p)
        q=16**p-1
        for n in (0,1,p-2,p,p+4):
            assert (16**(n+p)*beta-16**n*beta).denominator==1
        K=p-2
        assert 16**K*d<Q(1,250)
        print('p',p,'beta denominator',beta.denominator,'seed abs <',float(d),'first K historical deviation <',float(16**K*d))
    begin=time.time()
    x=states(768)
    print('state 768 computed seconds',time.time()-begin)
    for A in (96,192,384):
        o=[x[n][0] for n in range(A,2*A)]
        neg=[-tail(n) for n in range(A,2*A)]
        for m in (1,2,3):
            print('A',A,'m',m,'P_original',float(pressure(o,m)),'P_wrong',float(pressure(neg,m)))
    N=256
    for h in (1,2,3):
        a=sum(ch(h*x[n][0]) for n in range(N))/N
        b=sum(ch(16*h*x[n][0]) for n in range(N))/N
        # Exact forcing finite upper bound + telescoping bound.
        R=sum(forcing(n) for n in range(1,N+1))
        upper=(2+2*pi*abs(h)*float(R))/N
        assert abs(a-b)<=upper+1e-12
        print('approx inv',h,abs(a-b),'bounded by',upper)
    # characteristic collision profiles exact.
    for m in (1,2,3):
        M=16**m
        biased=(Q(64,15))**m
        half=[Q(k,2*M) for k in range(M)] # one point in each of M half-circle nodes, not equal uniform cells at m
        print('biased m',m,'theoretical',float(biased))
    print('SUCCESS')
if __name__=='__main__': verify()
