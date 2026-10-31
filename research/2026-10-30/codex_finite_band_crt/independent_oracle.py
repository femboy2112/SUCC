"""Independent finite arithmetic oracle: combined BBP fraction + mpmath phases.

Unlike finite_band.py it does not import that module, and it explicitly tests
that two different mathematical expressions for the same Fejer statistic agree.
Numerical precision supports calibration, not a universal proof.
"""
from fractions import Fraction
import json
import mpmath as mp

mp.mp.dps=75


def authentic_r(n):
    return Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def prefix(N):
    u=Fraction(0); out=[]
    for n in range(1,N+1):
        u=(16*u+authentic_r(n))%1
        out.append(u)
    return out

def fejer_direct(x,H):
    # positive square, no sin-ratio or Fourier kernel implementation used
    z=sum(mp.e**(2j*mp.pi*j*x) for j in range(H))
    return abs(z)**2/H

def mpfraction(f):
    return mp.mpf(f.numerator)/f.denominator

def pair_direct(xs,H):
    n=len(xs)
    return sum(fejer_direct(mpfraction(x-y),H) for x in xs for y in xs)/(n*n)

def pair_frequency(xs,H):
    n=len(xs); total=mp.mpf(1)
    for h in range(1,H):
        a=sum(mp.e**(2j*mp.pi*h*mpfraction(x)) for x in xs)/n
        total += 2*mp.mpf(H-h)/H*abs(a)**2
    return total

def main():
    rows=[]
    for N,H in ((7,8),(14,16),(24,32)):
        xs=prefix(N)
        a=pair_direct(xs,H)
        b=pair_frequency(xs,H)
        assert abs(a-b)<mp.mpf('1e-65')
        # exact rational circle bins source FID
        q=2*H
        bins={}
        for x in xs:
            ix=int(q*x)
            bins[ix]=bins.get(ix,0)+1
        Q=Fraction(q*sum(n*n for n in bins.values()),N*N)
        assert mpfraction(Q)<=mp.pi**2/2*a+mp.mpf('1e-60')
        rows.append({'N':N,'H':H,'Q':str(Q),'Fejer':mp.nstr(a,32),'Fourier_agreement':mp.nstr(abs(a-b),9),'hard_over_bound':mp.nstr(mpfraction(Q)/(mp.pi**2*a/2),9)})
    print(json.dumps({'status':'PASS','precision_dps':mp.mp.dps,'rows':rows},indent=2))

if __name__=='__main__':main()
