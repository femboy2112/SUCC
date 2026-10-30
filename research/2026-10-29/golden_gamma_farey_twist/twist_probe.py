"""Exact-arithmetic primitives for the Farey/Oily/Gamma 45-degree research sheet.

All functions in this file are finite and standard-library only. Infinite
identities belong to the accompanying paper proof. NO pi normality claim.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import comb, gcd, factorial, isqrt

D = ((1, -1), (1, 1))
S = ((0, -1), (1, 0))
A = ((1, 1), (1, 2))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def act(a, v):
    return (a[0][0]*v[0]+a[0][1]*v[1], a[1][0]*v[0]+a[1][1]*v[1])


def primitive(v):
    return gcd(*v)==1


def gcd_twist(v):
    if not primitive(v):
        raise ValueError('primitive vector required')
    w=act(D,v)
    return gcd(*w)


def farey_neighbor(v,w):
    if not (primitive(v) and primitive(w)):
        return False
    return abs(v[0]*w[1]-v[1]*w[0])==1


def farey_mediant(v,w):
    if not farey_neighbor(v,w):
        raise ValueError('unimodular Farey neighbors required')
    u=(v[0]+w[0],v[1]+w[1])
    if not primitive(u):
        raise AssertionError('unimodular mediant not primitive')
    return u


def totient(n):
    if type(n) is not int or n<1:
        raise ValueError('positive denominator required')
    out=n
    p=2
    x=n
    while p*p<=x:
        if x%p==0:
            out=out//p*(p-1)
            while x%p==0: x//=p
        p+=1
    if x>1: out=out//x*(x-1)
    return out


def cototient(n):
    return n-totient(n)


def cusp_denominator(v):
    if not primitive(v) or v[1]<0:
        raise ValueError('canonical primitive cusp required')
    return v[1] or 1


def ranks(v):
    q=cusp_denominator(v)
    return 1+totient(q),1+cototient(q)


def harmonic(n):
    if type(n) is not int or n<0:
        raise ValueError('nonnegative index required')
    return sum((Q(1,j) for j in range(1,n+1)),Q())


def mobius(n):
    if type(n) is not int or n<1:
        raise ValueError('positive index required')
    x=n
    sign=1
    p=2
    while p*p<=x:
        if x%p==0:
            x//=p
            if x%p==0: return 0
            sign=-sign
            while x%p==0:x//=p
        p+=1
    return -sign if x>1 else sign


def deficit_term(d):
    if type(d) is not int or d<1 or d%2==0:
        raise ValueError('odd d >=1 required')
    z=Q(1,4**d)
    return Q(mobius(d),4)*z/(1-z)**2


def deficit_interval(D_cut):
    """Rigorous exact rational bracket for the 45-degree Oily primitive loss.

    Absolute tail of the odd-d sum is bounded by the unrestricted d>D geometric tail.
    """
    if type(D_cut) is not int or D_cut<1 or D_cut>500:
        raise ValueError('cutoff must be 1..500')
    partial=sum((deficit_term(d) for d in range(1,D_cut+1,2)),Q())
    z=Q(1,4**(D_cut+1))
    error=z/(3*(1-z)**2)
    return (partial-error,partial+error)


def twist_totient_coeff(n):
    """Exact coefficient of q^n in 4*L(-log q): phi(n), doubled when n even."""
    if type(n) is not int or n<1:
        raise ValueError('positive heat trace index required')
    return (1+int(n%2==0))*totient(n)


def totient_heat_interval(N):
    """Independent positive rational enclosure for p45 at q=1/4.

    Uses 4L=sum A(n)q^n, 0<A(n)<=2n and a closed geometric tail.
    """
    if type(N) is not int or N<1 or N>500:
        raise ValueError('positive cutoff 1..500 required')
    r=Q(1,4)
    partial=sum((Q(twist_totient_coeff(n),4)*r**n for n in range(1,N+1)),Q())
    bound=Q(1,2)*r**(N+1)*(Q(N+1,1)/(1-r)+r/(1-r)**2)
    return partial,partial+bound


def twist_coeff_by_mobius(n):
    """An independently arranged arithmetic divisor formula for heat coefficient."""
    if type(n) is not int or n<1:
        raise ValueError('positive heat trace index required')
    return sum((mobius(d)*(n//d) for d in range(1,n+1,2) if n%d==0))


def primitive_pair_interval(D_cut):
    """P(gcd(K,L)=1), K,L iid Geom(1/2) over nonnegative integers.

    P(K=L=0)=1/4 is explicitly removed before Mobius inversion.
    """
    if type(D_cut) is not int or D_cut<1 or D_cut>500:
        raise ValueError('cutoff must be 1..500')
    total=Q(0)
    for d in range(1,D_cut+1):
        x=Q(1,2**d)
        total+=Q(mobius(d),4)*((1-x)**(-2)-1)
    # For x<=1/2, ((1-x)^-2-1)/4 <= 2x. Sum_{d>D} 2x =2^(1-D).
    bound=Q(1,2**(D_cut-1))
    return total-bound,total+bound


def rising(x,k):
    z=1
    for j in range(k):z*=x+j
    return z


def beta_edge_moment(alpha,beta,k):
    if min(alpha,beta)<1 or k<0:
        raise ValueError('integer Gamma shapes and nonnegative moment required')
    return Q(rising(alpha,k),rising(alpha+beta,k))


def dirichlet_moment(shapes, powers):
    if len(shapes)!=3 or len(powers)!=3 or min(shapes)<1 or min(powers)<0:
        raise ValueError('three positive integer shapes and nonnegative powers required')
    n=sum(powers)
    res=Q(1)
    for a,k in zip(shapes,powers):res*=rising(a,k)
    return res/rising(sum(shapes),n)


def gamma_rank_harmonic(r):
    """Exact rational component in E[log Gamma(r,1)]=H_(r-1)-gamma."""
    if type(r) is not int or r<1:
        raise ValueError('positive integer Gamma rank required')
    return harmonic(r-1)


def eisenstein_sigma_minus3(h):
    if type(h) is not int or h==0:
        raise ValueError('nonzero integer Fourier mode required')
    h=abs(h)
    return sum((Q(1,d**3) for d in range(1,h+1) if h%d==0),Q())


def fourpole_forcing(n):
    if type(n) is not int or n<1:
        raise ValueError('positive original source time required')
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def zero_seed_orbit(N):
    if type(N) is not int or N<0 or N>200:
        raise ValueError('finite source horizon 0..200 required')
    out=[Q(0)]
    for j in range(1,N+1):out.append(16*out[-1]+fourpole_forcing(j))
    return out


def literal_carry(q):
    return q.numerator//q.denominator


def frl_complement(q):
    return q-literal_carry(q)


def discrete_eisenstein_harness(h, y=1.0):
    """Numeric presentation ONLY; analytic Fourier coefficient theorem is in README."""
    from math import pi,exp
    y=float(y)
    h=abs(h)
    if h==0 or y<=0:raise ValueError('positive y, nonzero h required')
    return 45/(pi**3*y)*(1+2*pi*y*h)*exp(-2*pi*y*h)*float(eisenstein_sigma_minus3(h))
