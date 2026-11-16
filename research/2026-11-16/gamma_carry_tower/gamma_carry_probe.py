"""Independent finite calibrations for a proposed Gamma-on-carry-extension observer.

No pi oracle. The source forcing is the four original rational BBP poles.
The abstract cyclic Gamma observer is NOT the actual BBP transition.
"""
from __future__ import annotations
import cmath
from fractions import Fraction
from math import cos, exp, floor, log, pi, sqrt


def forcing(n: int) -> Fraction:
    if n < 1:
        raise ValueError("n>=1")
    a = 8*n-7
    return 4*Fraction(1,a)-2*Fraction(1,a+3)-Fraction(1,a+4)-Fraction(1,a+5)


def sigma(c: int) -> int:
    return 1 if c % 4 in (0,3) else -1


def bit_carry_add(a:int,b:int, ap:int,bp:int):
    return (a^ap, b^bp^(a&ap))


def negbin_mod4(alpha: int):
    """Exact residues modulo four for integer shape alpha via convolution."""
    if alpha<0: raise ValueError('nonnegative integer shape')
    residue = [Fraction(int(j==0)) for j in range(4)]
    single = [Fraction(8,15), Fraction(4,15), Fraction(2,15), Fraction(1,15)]
    for _ in range(alpha):
        residue = [sum(residue[j]*single[(k-j)%4] for j in range(4)) for k in range(4)]
    return residue


def gamma_on_sigma(c:int,alpha:int)->Fraction:
    return sum(w*sigma(c+k) for k,w in enumerate(negbin_mod4(alpha)))


def spectral_sigma(c:int,alpha:float)->float:
    return ((1+1j)*(2-1j)**(-alpha)*(1j)**c).real


def metric_sq(m:int,alpha:float,x:int,y:int)->float:
    """Standard l2 cyclic spectral metric squared, no numpy dependency."""
    N=2**m
    if x%N==y%N: return 0.0
    ans=0.0
    for k in range(N):
        lam=cmath.exp(2j*pi*k/N)
        ans+=abs(2-lam)**(-2*alpha)*abs(lam**x-lam**y)**2
    return ans/N


def tower_metric_sq(M:int,alpha:float,x:int,y:int)->float:
    return sum(2**(-m)*metric_sq(m,alpha,x,y) for m in range(1,M+1))


def lowmode_norm(m:int,alpha:float)->float:
    z=cmath.exp(2j*pi/(2**m))
    return abs(2-z)**(-alpha)


def branch_step(n:int,c:int,u:Fraction):
    """One literal BBP source update, integer winding plus fractional state."""
    if n < 1: raise ValueError("n >= 1")
    rr=forcing(n+1)
    v=16*u
    j=int(v)
    z=v-j+rr
    eps=int(z>=1)
    next_u=z-eps
    return 16*c+j+eps,next_u,j,eps


def exact_orbit(N:int):
    state=Fraction(0)
    out={0:state}
    for n in range(1,N+1):
        state=16*state+forcing(n)
        out[n]=state
    return out


def refractory_length(B:int)->int:
    """Largest conservative integer m with 16^(m+1) <= 64 B^2; no float."""
    if B<1:raise ValueError
    return refractory_length_reference(B)


def refractory_length_reference(B:int)->int:
    cap=64*B*B
    power=1
    k=0
    while power*16<=cap:
        power*=16;k+=1
    return max(0,k-1)


def refractory_experiment(n:int,lowcell:int=3):
    """Force an event by selecting a fractional input in last sliver of a cell."""
    rr=forcing(n+1)
    u=Fraction(lowcell,16)+(1-rr/2)/16
    c=0
    c,u,j,e=branch_step(n,c,u)
    if e!=1:raise AssertionError('positive seam control failed')
    events=[]
    for i in range(1,refractory_length_reference(n)+1):
        c,u,j,e=branch_step(n+i,c,u)
        events.append((i,j,e))
    return events


def main():
    for alpha in range(0,6):
        for c in range(4):
            s=gamma_on_sigma(c,alpha)
            assert abs(float(s)-spectral_sigma(c,alpha))<1.e-12,(c,alpha,s)
    for a, b, ap, bp in ((a,b,ap,bp) for a in range(2) for b in range(2) for ap in range(2) for bp in range(2)):
        c=a+2*b;d=ap+2*bp
        left=(c+d)%4
        x,y=bit_carry_add(a,b,ap,bp)
        assert left==x+2*y
        assert sigma(left)==sigma(c)*sigma(d)*(-1)**(a*ap)
    for m in range(1,8):
        for x in (0,1,3,7,23):
            for y in (0,1,2,7,31):
                if x==y:continue
                for alpha in (0.0,0.5,1.0,2.0):
                    q=metric_sq(m,alpha,x,y)
                    if x%(2**m)==y%(2**m):assert q<1.e-12
                    else:
                        assert 2*(3**(-2*alpha))-1.e-10 <= q<=2+1.e-10,(m,x,y,alpha,q)
    for a in (0,1,2,3):
        for b in (0,1,2,3):
            if a==b:continue
            d=metric_sq(2,1.0,a,b)
            expect=2/5 if (a-b)%4==2 else 1/5+1/9
            assert abs(d-expect)<1.e-12
    for M in (1,2,3,5,8):
        for x,y in ((0,1),(1,3),(2,6),(10,18)):
            v=0;diff=x-y
            while diff%2==0 and diff!=0:v+=1;diff//=2
            if v>=M:expected=0.0
            else:expected=2*(2**(-v)-2**(-M))
            got=tower_metric_sq(M,0.0,x,y)
            assert abs(got-expected)<1.e-9,(M,x,y,got,expected)
    o=exact_orbit(128)
    seams=[]
    for n in range(1,128):
        c=int(o[n]);u=o[n]-c
        cc,uu,j,eps=branch_step(n,c,u)
        assert cc==int(o[n+1])
        assert uu==o[n+1]-int(o[n+1])
        assert eps==int(uu<forcing(n+1))
        if eps: seams.append(n)
    for n in (2,8,24,64,128,1024):
        assert all(j==0 and eps==0 for _,j,eps in refractory_experiment(n)),n
    for m in (3,4,6,8,10,12):
        alpha=1.5
        theta=2*pi/(2**m)
        exact=lowmode_norm(m,alpha)
        asym=exp(-alpha*theta*theta)
        print('spectral small mode',m,'exact',exact,'asym',asym,'relative',abs(exact-asym)/exact)
    print('PASS: carry law, gamma spectrum, gamma metric, 2-adic snowflake, source-step, refractory controls')
    print('original source internal seam events n=1..127',seams)


if __name__=='__main__':main()
