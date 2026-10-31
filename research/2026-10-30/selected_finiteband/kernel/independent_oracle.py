"""Separate implementation: combined source, unrolled prefixes, integral tails.

Does not import kernel_transport. High precision is numerical calibration, not
a sound interval or external proof authority. Large coherent cases use doubles.
"""
from fractions import Fraction as F
from functools import lru_cache
import json
import math
import mpmath as mp
import numpy as np

mp.mp.dps=85


def rat(n):
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def dec(x):
    return mp.mpf(x.numerator)/x.denominator


@lru_cache(None)
def tail_integral(n):
    return mp.quad(lambda x: x**(8*n)*(4-2*x**3-x**4-x**5)/(16-x**8),[0,1])


def states(N,s=F(0)):
    return [dec((16**n*s+sum((16**(n-j)*rat(j) for j in range(1,n+1)),F(0)))%1)
            for n in range(1,N+1)]


def k(t,H):
    if not t: return mp.mpf(H)
    return mp.sin(mp.pi*H*t)**2/(H*mp.sin(mp.pi*t)**2)


def paired(xs,H):
    return sum(k(x-y,H) for x in xs for y in xs)/len(xs)**2


def spectral(xs,H):
    return 1+2*sum(mp.mpf(H-h)/H*abs(sum(mp.exp(2j*mp.pi*h*x) for x in xs)/len(xs))**2
                   for h in range(1,H))


def coherent_double(N,H):
    n=np.arange(1,N+1,dtype=np.float64)
    tails=np.zeros(N)
    for j in range(1,29):
        a=8*(n+j)-7
        tails+=(6/(a*(a+3))+4/(a*(a+4))+5/(a*(a+5)))/16.0**j
    total=0.0
    for start in range(0,N,128):
        t=tails[start:start+128,None]-tails[None,:]
        # np.sinc implements sin(pi*x)/(pi*x), including x=0.
        total+=np.sum(H*(np.sinc(H*t)/np.sinc(t))**2)
    E=total/(N*N)
    gap=math.sqrt(H)-math.sqrt(E)
    mass=np.sum(H*(1-(np.sinc(H*tails)/np.sinc(tails))**2))
    C2=math.pi/(8*math.sqrt(3))
    remainder=mass/(N*math.sqrt(H))-gap
    assert remainder>=-1e-10
    assert remainder<=C2*H**1.5/(2*N*N)+1e-10
    return {'N':N,'H':H,'sqrt_energy_loss':gap,'scaled_loss':N/H*gap,
            'pi_over_15':math.pi/15,'finite_mass_scaled':mass/H**1.5,
            'quadratic_remainder':remainder,
            'quadratic_remainder_bound':C2*H**1.5/(2*N*N),
            'authority':'double calibration; 28 positive tail terms'}


def main():
    rows=[]
    for N,H,seed in ((19,7,F(0)),(41,29,F(2,9)),(73,127,F(-7,13))):
        xs=states(N,seed)
        ts=[tail_integral(n) for n in range(1,N+1)]
        ys=[x+t for x,t in zip(xs,ts)]
        a=paired(xs,H); b=spectral(xs,H)
        assert abs(a-b)<mp.mpf('1e-75')
        gap=abs(mp.sqrt(a)-mp.sqrt(paired(ys,H)))
        point=sum(min(mp.sqrt(2*H),2*mp.pi*mp.sqrt(mp.mpf(H*(H*H-1))/6)*t) for t in ts)/N
        global_bound=mp.sqrt(mp.pi/(8*mp.sqrt(3)))*mp.sqrt(H)*mp.root(H*H-1,4)/N
        assert gap<point<global_bound
        rows.append({'N':N,'H':H,'seed':str(seed),'pair_spectral_gap':mp.nstr(abs(a-b),9),
                     'sqrt_energy_gap':mp.nstr(gap,32),'point_budget':mp.nstr(point,32),
                     'global_budget':mp.nstr(global_bound,32)})
    tails=[]
    for n in (1,2,13,19,73,239):
        lo=sum((rat(n+j)/16**j for j in range(1,30)),F(0))
        hi=lo+rat(n+30)/(15*16**29)
        value=tail_integral(n)
        assert dec(lo)<value<dec(hi)
        tails.append({'n':n,'interval_width':str(hi-lo),'n2_T':mp.nstr(n*n*value,28)})
    # Nonoscillatory Gamma/Laplace verification of the cosine Mellin integral:
    # Tonelli: t^-3/2 = Gamma(3/2)^-1 integral s^1/2 exp(-s*t) ds;
    # integrate (1-cos(a*t)) first to obtain a²/(s(s²+a²)).
    mellin=mp.quad(lambda s: 1/(mp.sqrt(s)*(s*s+1)),[0,1,mp.inf])/mp.gamma(mp.mpf(3)/2)
    assert abs(mellin-mp.sqrt(2*mp.pi))<mp.mpf('1e-40')
    K=mp.sqrt(mp.pi)/16*2*mp.quad(lambda u: (1-u)*mp.sqrt(2*u)*mellin,[0,1])
    assert abs(K-mp.pi/15)<mp.mpf('1e-40')
    coherent=[coherent_double(N,H) for N,H in ((128,128),(512,512),(2048,2048),
                                             (1536,768),(4096,2048))]
    print(json.dumps({'status':'PASS','precision_dps':mp.mp.dps,
        'source_route':'combined rational numerator; unrolled prefixes; Beta-type integral tails',
        'fresh_transport_rows':rows,'independent_tail_intervals':tails,
        'mellin_cosine_integral':mp.nstr(mellin,45),'mellin_K':mp.nstr(K,45),
        'coherent_asymptotic_calibration':coherent},indent=2))


if __name__=='__main__': main()
