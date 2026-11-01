"""Independent Gaussian window telescope + BBP source shifted exact oracle.

Does not import selected_lag; independent algebra and loops.
"""
from fractions import Fraction as F

def window_energy(z,K):
    N=len(z)
    if not 1<=K<=N: raise ValueError('invalid finite width')
    energy=0
    for t in range(N+K-1):
        real=imag=0
        for j in range(K):
            idx=t-j
            if 0<=idx<N:
                real+=z[idx][0];imag+=z[idx][1]
        energy+=real*real+imag*imag
    return energy

def independently_unroll_difference(n,k):
    def r(j):
        x=8*j-7
        return F(4,x)-F(2,x+3)-F(1,x+4)-F(1,x+5)
    u=F(0)
    states=[u]
    for t in range(1,n+k+1):
        u=u*16+r(t)
        states.append(u)
    return states[n+k]-states[n], (16**k-1)*states[n],sum(16**(k-j)*r(n+j) for j in range(1,k+1))


def direct_shifted_character_histogram(a,k,h,seed=0):
    q=2**a
    u=F(seed)
    hist=[0]*q
    for n in range(1,q+1):
        t=8*n-7
        u=16*u+F(4,t)-F(2,t+3)-F(1,t+4)-F(1,t+5)
        v=(u.numerator*pow(u.denominator,-1,q))%q
        hist[(h*(16**k-1)*v)%q]+=1
    return hist
