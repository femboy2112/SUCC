"""Finite, NON-CERTIFIED Guinand-Weil triangulation using a triangle test.
Do not take numerical zero truncation as RH evidence; this is a sign oracle.
"""
import math
import mpmath as mp
from scipy.integrate import quad
from scipy.special import digamma

mp.mp.dps=17

def gtri(a,L):
    if a < 0: return gtri(-a,L)
    if a >= 2*L: return 0.0
    if a <= L: return 2*L/3-a*a/L+a**3/(2*L*L)
    return (2*L-a)**3/(6*L*L)

def Fourier(t,L):
    if abs(t) < 1e-10: return L
    return L*(math.sin(L*t/2)/(L*t/2))**2

def omega(t):
    return digamma(0.25+0.5j*t).real - math.log(math.pi)

def archt(L):
    f = lambda t: Fourier(t,L)**2*omega(t)/math.pi
    segs=[(0,20),(20,80),(80,250),(250,1000),(1000,5000)]
    vals=[]
    for A,B in segs:
        val,err=quad(f,A,B,epsabs=1e-10,epsrel=1e-9,limit=800)
        vals.append(val)
    return sum(vals),vals

def prime_term(L):
    terms=[]
    for n in range(2,10000):
        a=math.log(n)
        if a>=2*L: break
        for p in range(2,n+1):
            if n % p != 0: continue
            k=0;m=n
            while m%p==0: m//=p;k+=1
            if m==1:
                w=math.log(p)/math.sqrt(n)
                terms.append((p,k,-2*w*gtri(a,L)))
            break
    return sum(x[-1] for x in terms),terms

def zeros_sum(L,N):
    s=mp.mpf('0')
    for j in range(1,N+1):
        z=mp.im(mp.zetazero(j))
        f=L*(mp.sin(L*z/2)/(L*z/2))**2
        s+=2*f*f
    return float(s)

for L in [.4,.6]:
    a,blocks=archt(L)
    pp,pterms=prime_term(L)
    pole=2*(L*(math.sinh(L/4)/(L/4))**2)**2
    rhs=a+pp+pole
    print('L',L,'pole',pole,'arch',a,'prime',pp,'terms',pterms,'RHS',rhs)
    for N in [8,16]:
        zz=zeros_sum(L,N)
        print(' zeros',N,zz,'residual zeros-RHS',zz-rhs)
