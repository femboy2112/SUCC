"""Quantitative, source-authenticated Borwein sweep certificates.

Everything is rational except standard inequalities invoked in the theorem note.
The returned certificates are finite-B statements, not a proof of convergence.
"""
from fractions import Fraction as F
from functools import lru_cache

DELTA=F(1,18)
C=F(162,289)
HAAR_MEAN=F(256,7803)
FOURIER_FLOOR=F(2205,139876)


def source_r(n):
    if type(n) is not int or n<1: raise ValueError('BBP source clock n>=1')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


@lru_cache(None)
def U(n):
    if type(n) is not int or n<0: raise ValueError('nonnegative clock required')
    u=F(0)
    for j in range(1,n+1): u=16*u+source_r(j)
    return u


def original_phases(B):
    if type(B) is not int or B<1: raise ValueError('positive integer B required')
    terminal=U(2*B)
    return tuple((terminal/F(16**k))%1 for k in range(1,B+1))


def torus(z):
    x=F(z)%1
    return min(x,1-x)


def L(z):
    x=max(torus(z)-DELTA,0)
    return C*x*x


def swept(phases,a):
    return sum((L(x-a) for x in phases),F(0))/len(phases)


def shadow_tail(B):
    if type(B) is not int or B<1: raise ValueError
    return F(16,7225*B)*source_r(2*B+1)


def origin_breakpoints(phases):
    pts={F(0),F(1)}
    for x in phases:
        for e in (F(0),DELTA,F(1,2),1-DELTA):
            pts.add((x-e)%1)
    return sorted(pts)


def polynomial_quadrature(phases):
    """Exact Q_B=integral_0^1 (swept(alpha)-HAAR_MEAN)^2 d alpha.

    Each swept response is piecewise quadratic with rational breakpoints,
    so this performs exact polynomial integration on every interval.
    """
    if not phases: raise ValueError('nonempty sample')
    pp=tuple(F(x)%1 for x in phases)
    pts=origin_breakpoints(pp)
    total=F(0)
    for a,b in zip(pts[:-1],pts[1:]):
        mid=(a+b)/2
        fa=swept(pp,a)-HAAR_MEAN
        fm=swept(pp,mid)-HAAR_MEAN
        fb=swept(pp,b)-HAAR_MEAN
        # Interpolate f(a+t*(b-a))=a0+a1*t+a2*t**2 for t in [0,1]
        a0=fa
        a2=2*(fa+fb-2*fm)
        a1=fb-fa-a2
        total+=(b-a)*(a0*a0+a0*a1+(a1*a1+2*a0*a2)/3 + a1*a2/2 + a2*a2/5)
    return total


def original_energy(B):
    return polynomial_quadrature(original_phases(B))


def certified_weyl_bound_from_energy(B,h):
    """Theorem: |W_B^{pi}(h)| <= this upper bound, valid all h!=0."""
    if type(h) is not int or h==0:raise ValueError('nonzero harmonic integer')
    # Caller retains exact Q_B; avoid float until mathematical reporting.
    return (original_energy(B),shadow_tail(B), F(h*h,1)/FOURIER_FLOOR)


def quantitative_interval_discrepancy(B,H,q=None):
    """Exact rational upper bound assuming q >= sqrt(original_energy(B)).

    q may be any nonnegative rational upper certificate of sqrt(Q_B).
    Does not claim a sharp bound; can be >1 for small B.
    Uses D <= 3/(H+1)+3*sum(|W(h)|/h) (Erdos-Turan theorem).
    """
    if type(H) is not int or H<1:raise ValueError('positive cutoff')
    v=original_energy(B)
    if q is None:
        from math import isqrt
        # Rational ceiling at 1e-8 resolution; remain exact.
        digits=10**8
        up=isqrt((v.numerator*digits*digits+v.denominator-1)//v.denominator)
        q=F(up+1,digits)
    q=F(q)
    if q<0 or q*q<v:raise ValueError('q must certify sqrt(energy)')
    return F(3,H+1) + F(3,2*FOURIER_FLOOR)*H*(H+1)*(q+shadow_tail(B))


def discrete_interval_discrepancy(phases):
    """Exact full circular-interval discrepancy for a finite point multiset.

    For 0<=x_1<=...<=x_N<1, extremal one-sided empirical-CDF
    deviations are D^+=max_i(i/N-x_i) and
    D^-=max_i(x_i-(i-1)/N). The full interval discrepancy is D^++D^-.
    Repeated phases and endpoint conventions are included by limits.
    """
    if not phases:raise ValueError('nonempty sample')
    points=sorted(F(x)%1 for x in phases)
    N=len(points)
    dplus=max(F(i,N)-x for i,x in enumerate(points,1))
    dminus=max(x-F(i-1,N) for i,x in enumerate(points,1))
    return dplus+dminus


def autocorrelation(t):
    """Exact periodic K(t) = integral L(a)L(a-t) da; rational for rational t."""
    shift=F(t)%1
    pts=origin_breakpoints((F(0),shift))
    total=F(0)
    for a,b in zip(pts[:-1],pts[1:]):
        m=(a+b)/2
        def qcoeff(q):
            f0=L(a-q);fm=L(m-q);f1=L(b-q)
            c2=2*(f0+f1-2*fm)
            c1=f1-f0-c2
            return (f0,c1,c2)
        p=qcoeff(F(0))
        q=qcoeff(shift)
        a0=p[0]*q[0]
        a1=p[0]*q[1]+p[1]*q[0]
        a2=p[0]*q[2]+p[1]*q[1]+p[2]*q[0]
        a3=p[1]*q[2]+p[2]*q[1]
        a4=p[2]*q[2]
        total+=(b-a)*(a0+a1/2+a2/3+a3/4+a4/5)
    return total


def autocorrelation_energy(phases):
    """Exact characteristic-kernel MMD^2 against Haar."""
    ps=tuple(F(x)%1 for x in phases)
    N=len(ps)
    if N<1:raise ValueError
    total=sum((autocorrelation(ps[i]-ps[j]) for i in range(N) for j in range(N)),F(0))
    return total/(N*N)-HAAR_MEAN**2


def certified_hex_words(B,k):
    """Authenticated BBP digit words, with exact ambiguities.

    For each shell clock n in [B,2B), the completed phase equals the exact
    rational terminal shadow plus a strictly positive tail, bounded by
    16^(n-2B)*r(2B+1)/15. If the entire interval remains in one base-16^k
    cylinder, return its rigorously certified word. Otherwise mark ambiguous.
    Returns (counts, undecided_clocks); every count is a lower bound, and
    each final actual count <= lower + len(undecided_clocks).
    """
    if type(B) is not int or B<1 or type(k) is not int or k<1:raise ValueError
    N=2*B
    Ulast=U(N)
    bound=source_r(N+1)/15
    base=16**k
    counts={}
    undecided=[]
    for n in range(B,2*B):
        z=Ulast/F(16**(2*B-n))
        error=bound/F(16**(2*B-n))
        lo=(base*z).numerator//(base*z).denominator
        high=base*(z+error)
        hi=high.numerator//high.denominator
        if lo==hi:
            word=lo%base
            counts[word]=counts.get(word,0)+1
        else:
            undecided.append(n)
    return counts,tuple(undecided)
