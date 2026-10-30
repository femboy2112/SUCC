"""Exact rational operations for two opposing BBP-source observers.

The source is the original signed FOUR-pole rational BBP forcing represented
as a strictly positive Laplace density. All numerical validation is separate.
The two observers sample independently, with laws mu_(a+t), mu_(a-t).
There is no random sampling theorem for the deterministic digits of pi.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, factorial

POLES = ((0,4),(3,-2),(4,-1),(5,-1))

def exact(x, name='value') -> F:
    if type(x) not in (F,int): raise ValueError(f'exact rational {name} required')
    return F(x)

def R(a) -> F:
    a=exact(a,'a')
    if a<=0: raise ValueError('a must be positive')
    return sum((F(c,a+d) for d,c in POLES),F())

def R_prime(a) -> F:
    a=exact(a,'a')
    if a<=0: raise ValueError('a must be positive')
    return sum((-F(c,(a+d)**2) for d,c in POLES),F())

def validate(a,t):
    a,t=exact(a,'a'),exact(t,'t')
    if a<=0 or not 0<=t<a: raise ValueError('require a>t>=0')
    return a,t

def base_coefficients(a):
    """G_a(z)=sum_d c_d R(2a+d) exp(-(a+d)z), z>=0."""
    a=exact(a,'a')
    if a<=0: raise ValueError('a>0 required')
    return tuple((a+d,F(c)*R(2*a+d)) for d,c in POLES)

def product_normalizer(a,t):
    """Product of posterior tilt normalizers relative to base mu_a."""
    a,t=validate(a,t)
    return R(a+t)*R(a-t)/R(a)**2

def hellinger_squared(a,t):
    a,t=validate(a,t)
    return R(a)**2/(R(a+t)*R(a-t))

def overlap_bounds_squared(a,t):
    """Strict lower/upper bounds on affinity squared when 0<t<a."""
    a,t=validate(a,t)
    rho2=(t/a)**2
    lower=(1-rho2)**2
    upper=(1-rho2)*(1-(t/(a+5))**2)
    return lower, upper

def disagreement_moment(a,t,m):
    """Exact m-th moment of Delta=X_+-X_-, including normalization m=0."""
    a,t=validate(a,t)
    if type(m) is not int or m<0: raise ValueError('m nonnegative integer')
    denom=R(a+t)*R(a-t)
    return factorial(m)*sum((c*(1/(rate+t)**(m+1)+(-1)**m/(rate-t)**(m+1))
         for rate,c in base_coefficients(a)),F())/denom

def source_mean(a): return -R_prime(a)/R(a)

def grade_probabilities(n,carrier_a):
    """Exact finite Pascal experiment; n trials, p_failure(X)=1-exp(-8X)."""
    if type(n) is not int or n<0:raise ValueError('n>=0 required')
    carrier_a=exact(carrier_a,'carrier_a')
    if carrier_a<=0:raise ValueError('positive source parameter required')
    normalizer=R(carrier_a)
    return tuple(F(comb(n,j))*sum((F((-1)**k*comb(j,k))*R(carrier_a+8*(n-j+k))
               for k in range(j+1)),F())/normalizer for j in range(n+1))

def grade_mean(n,carrier_a):
    if type(n) is not int or n<0:raise ValueError('n>=0 required')
    a=exact(carrier_a,'carrier_a')
    if a<=0:raise ValueError('positive source parameter required')
    return n*(1-R(a+8)/R(a))

def grade_derivative(n,carrier_a):
    """Exact source-clock derivative d/dc of q_(n,c)(j)."""
    if type(n) is not int or n<0:raise ValueError('n>=0 required')
    c=exact(carrier_a,'carrier_a')
    if c<=0:raise ValueError('positive source parameter required')
    Z=R(c); Zp=R_prime(c)
    answer=[]
    for j in range(n+1):
        u=sum((F((-1)**k*comb(j,k))*R(c+8*(n-j+k)) for k in range(j+1)),F())
        up=sum((F((-1)**k*comb(j,k))*R_prime(c+8*(n-j+k)) for k in range(j+1)),F())
        answer.append(comb(n,j)*(up/Z-u*Zp/Z**2))
    return tuple(answer)


def directional_phase_score_formal(n,carrier_a,seed=F(0),frequency=1):
    """Opposing-tilt derivative at t=0: 2 sum_j q'_j(a) e(h U_(n+j))."""
    if type(frequency) is not int or frequency==0:raise ValueError('nonzero integer frequency')
    qprime=grade_derivative(n,carrier_a)
    states=bbp_history(2*n,seed)
    coefficients={}
    for j,w in enumerate(qprime):
        theta=(frequency*states[n+j])%1
        coefficients[theta]=coefficients.get(theta,F())+2*w
    return {key:value for key,value in coefficients.items() if value}


def bbp_forcing(n):
    if type(n) is not int or n<1:raise ValueError('source index >=1 required')
    return R(8*n-7)

def bbp_history(n,seed=F(0)):
    if type(n) is not int or n<0:raise ValueError('history index >=0 required')
    x=exact(seed,'seed')
    result=[x]
    for i in range(1,n+1):
        x=16*x+bbp_forcing(i)
        result.append(x)
    return tuple(result)

def signed_phase_readout_formal(n,carrier_a,seed=F(0),frequency=1):
    """Exact formal Fourier group algebra readout, map exponent mod 1 -> weight.

    Unrecognized algebraic cancellations can occur among different roots of
    unity, so this is a formal source-preserving representation, not a sign bound.
    """
    if type(frequency) is not int or frequency==0:raise ValueError('nonzero integer frequency')
    q=grade_probabilities(n,carrier_a)
    states=bbp_history(2*n,seed)
    coeff={}
    for j,weight in enumerate(q):
        theta=(frequency*states[n+j])%1
        coeff[theta]=coeff.get(theta,F())+weight
    return {k:v for k,v in coeff.items() if v}

if __name__ == '__main__':
    for a,t in [(F(1),F(1,3)),(F(9),F(3)),(F(73),F(19))]:
        assert disagreement_moment(a,t,0)==1
        assert disagreement_moment(a,t,1)==source_mean(a+t)-source_mean(a-t)
        l,u=overlap_bounds_squared(a,t)
        assert l<hellinger_squared(a,t)<u
    print('OPPOSING_BBP_EXACT_CORE_PASS')
