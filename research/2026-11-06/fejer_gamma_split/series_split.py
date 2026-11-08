"""Exact algebra and scoped numerical probe for SUCC dyadic return-fiber energy.

All source states use Fraction; finite character evaluations use complex floating
values only for numerical comparison, never for rigorous infinite estimates.
"""
from __future__ import annotations
import cmath
import math
from fractions import Fraction


def original_forcing(n: int) -> Fraction:
    assert isinstance(n, int) and n >= 1
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def exact_original_states(N: int):
    u = Fraction()
    states = []
    for n in range(N):
        if n:
            u = (16*u + original_forcing(n)) % 1
        states.append(u)
    return states


def shadow_states(N: int):
    return [Fraction(n, (2*n-1)**4) % 1 for n in range(N)]


def phases(states, h=1):
    return [cmath.exp(2j*math.pi*float((h*x) % 1)) for x in states]


def completed_beta_one_fifth(N, h=1):
    x = Fraction(1, 5)
    zz=[]
    for n in range(N):
        zz.append(cmath.exp(2j*math.pi*float((h*x) % 1)))
        x=(16*x)%1
    return zz


def fibers(z, Q):
    N=len(z)
    if Q<1 or N % Q:
        raise ValueError("Q must divide the sample size")
    M=N//Q
    return [sum(z[a+t*Q] for t in range(M))/M for a in range(Q)]


def direct_energy(z, Q):
    aa=fibers(z,Q)
    return sum(abs(v)**2 for v in aa)/Q


def global_mean(z):
    return sum(z)/len(z)


def spectral_energy(z,Q):
    A=fibers(z,Q)
    return sum(abs(sum(A[a]*cmath.exp(-2j*math.pi*r*a/Q) for a in range(Q))/Q)**2
               for r in range(Q))


def independent_split_energy(z,Q):
    """Wrong result from making the two residue labels independent."""
    return abs(global_mean(z))**2


def level_means(z, level):
    q=1<<level
    if len(z)%q:
        raise ValueError('2^level must divide sample length')
    return fibers(z,q)


def martingale_budget(z,k):
    if len(z)%(1<<k):
        raise ValueError('Q must divide N')
    base=abs(global_mean(z))**2
    increments=[]
    levels=[]
    for j in range(k+1):
        f=level_means(z,j)
        levels.append(sum(abs(x)**2 for x in f)/(1<<j))
        if j:
            ell=1<<(j-1)
            increments.append(sum(abs(f[a]-f[a+ell])**2 for a in range(ell)) / (4*ell))
    return base, increments, levels


def triad_budget(z,Q):
    A=fibers(z,Q)
    N=len(z);M=N//Q
    global_sq=abs(global_mean(z))**2
    between=sum(abs(a-b)**2 for a in A for b in A)/(2*Q*Q)
    within=sum(abs(z[a+t*Q]-z[a+s*Q])**2 for a in range(Q)
               for s in range(M) for t in range(M))/(2*Q*M*M)
    return global_sq,between,within


def fejer_energy(z,Q):
    N=len(z);M=N//Q
    result=1/M
    for d in range(1,M):
        cov=sum(z[a+(t+d)*Q]*z[a+t*Q].conjugate()
                for a in range(Q) for t in range(M-d))/(Q*(M-d))
        result+=2*(M-d)/M**2*cov.real
    return result


def normalized_lag(z,Q,d):
    N=len(z);M=N//Q
    return sum(z[n+d*Q]*z[n].conjugate() for n in range(Q*(M-d)))/(Q*(M-d))


def source_sum(n:int, L:int):
    out=Fraction()
    for j in range(1,L+1):
        out=16*out+original_forcing(n+j)
    return out


def original_lag_phase(n:int,L:int,h:int):
    x=exact_original_states(n+1)[-1]
    diff=((16**L-1)*x+source_sum(n,L))%1
    return cmath.exp(2j*math.pi*float((h*diff)%1))


def tails(n:int,depth:int):
    # for n>=0 and depth>=1, all terms after depth have source index>=2
    if depth<1 or n<0:
        raise ValueError
    out=sum((original_forcing(n+j)*Fraction(1,16**j) for j in range(1,depth+1)),Fraction())
    remainder=Fraction(1,15*16**depth*(n+depth+1)**2)
    return out,out+remainder


def completed_phases(N:int,h:int,depth:int=120):
    states=exact_original_states(N)
    zz=[]
    for n,x in enumerate(states):
        lo,hi=tails(n,depth)
        y=(x+(lo+hi)/2)%1
        zz.append(cmath.exp(2j*math.pi*float((h*y)%1)))
    return zz


def completed_highfreq_cov(z,Q,d):
    """Completed product regrouped as one Weyl character at H=h(16^(dQ)-1).
    Input z contains the completed phase e(h z_n). This computes the same
    high-frequency phase as a consecutive n-sum by the exact orbit identity.
    """
    M=len(z)//Q
    return normalized_lag(z,Q,d)


def half_gamma_series_partial(Q:int,J:int):
    """Sqrt-inverse telescoping series truncated after J terms."""
    return 1/math.sqrt(Q)-1/math.sqrt(Q+J)


def harmonic_series_partial(M:int,J:int):
    return Fraction(1,M)-Fraction(1,M+J)


def Abel_prefix_coefficient(values,M):
    """[u^(M-1)] (sum_t values[t] u^t)/(1-u), divided by M."""
    return sum(values[:M])/M


def proxy_quadrant_example(Q:int,M:int):
    zz=[cmath.exp(2j*math.pi*(n%Q)/Q) for n in range(Q*M)]
    return direct_energy(zz,Q),abs(global_mean(zz))**2


def gamma_harmonic_truncation_factor(Q:int,M:int,J:int,L:int):
    """Exact positive truncation of BOTH half-density and harmonic amplitudes.

    Relative to R the factor is (alpha_J*sqrt(Q))**2*(beta_L*M)**2.
    Never infer original-source cancellation from this scalar factor.
    """
    if min(Q,M,J,L)<1:
        raise ValueError
    return (1-math.sqrt(Q/(Q+J)))**2*(L/(M+L))**2


def gluing_projector_energy(z,Q):
    """R = Q^-2 sum_{a,b} A_a conj(A_b) sum_r e(r(a-b)/Q)."""
    A=fibers(z,Q)
    return sum(A[a]*A[b].conjugate()*sum(
        cmath.exp(2j*math.pi*r*(a-b)/Q) for r in range(Q))
        for a in range(Q) for b in range(Q)).real/Q**2
