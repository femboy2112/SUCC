"""Pure Fraction OUTWARD proof for cancellation in genuine Q-zeta Suzuki g'.

Only the authentic a=1/2 first-prime window; NO zeta zero inputs, no fitted
coefficients.  Use the classical (real) Gamma-OU layer and the exact contact.
This is a deterministic mathematical interval proof, not float quadrature.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction as F
from math import factorial, isqrt

class SignedSourceEnclosureError(ValueError):
    pass

ROUND=10**22
def dlo(x):
    x=F(x);return F(x.numerator*ROUND//x.denominator, ROUND)
def dhi(x):return -dlo(-F(x))
def roundbox(z):return (dlo(z[0]),dhi(z[1]))


def q(x):
    if type(x) not in (int,F):raise SignedSourceEnclosureError('exact rational required')
    return F(x)

@lru_cache(maxsize=5000,typed=True)
def exp_interval(x):
    """Exp(x), rational 0<=x<=1/2, positive Taylor, certified omitted tail."""
    x=q(x)
    if not F()<=x<=F(1,2):raise SignedSourceEnclosureError('exp finite source range')
    term=F(1);value=F(1)
    for k in range(1,29):
        term=term*x/k;value+=term
    nxt=term*x/29
    return roundbox((value,value+nxt/(1-x/F(30))))


def invert_interval(a):
    if a[0]<=0:raise SignedSourceEnclosureError('positive reciprocal required')
    return F(1)/a[1],F(1)/a[0]


def exp_neg_interval(x):return invert_interval(exp_interval(x))

@lru_cache(maxsize=5000,typed=True)
def atan_small(x):
    x=q(x)
    if not 0<=x<=F(1,3):raise SignedSourceEnclosureError('atan reduced source range')
    total=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(27)),F())
    rem=x**55/F(55)
    # 55 terms, next j=55 sign negative; alternating sequence monotone.
    return roundbox((total-rem,total))

@lru_cache(maxsize=1,typed=True)
def pi_interval():
    a=atan_small(F(1,5));b=atan_small(F(1,239))
    return roundbox((16*a[0]-4*b[1],16*a[1]-4*b[0]))

@lru_cache(maxsize=5000,typed=True)
def atan_interval(x):
    x=q(x)
    if not 0<=x<=1:raise SignedSourceEnclosureError('atan real scale 0..1')
    if x<=F(1,3):return atan_small(x)
    if x<=F(1,2):
        total=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(80)),F())
        rem=x**161/F(161)
        return roundbox((total,total+rem))
    # x>1/2. y=(1-x)/(1+x) belongs [0,1/3], interval-directed
    # argument reduction atan(x)=pi/4-atan(y). NO midpoint substitution.
    y=(1-x)/(1+x)
    ylo,yhi=dlo(y),dhi(y)
    low=atan_small(yhi)
    high=atan_small(ylo)
    pi=pi_interval()
    return roundbox((pi[0]/4-low[1],pi[1]/4-high[0]))

@lru_cache(maxsize=1,typed=True)
def log2_interval():
    z=F(1,3)
    total=sum((2*z**(2*j+1)/F(2*j+1) for j in range(25)),F())
    return roundbox((total,total+2*z**51/(F(51)*(1-z*z))))

@lru_cache(maxsize=5000,typed=True)
def log_interval(x):
    x=q(x)
    if x<=0:raise SignedSourceEnclosureError('log positive source')
    if x<1:
        z=log_interval(1/x)
        return -z[1],-z[0]
    n=0;u=x
    while u>=2:
        u/=2;n+=1
    z=(u-1)/(u+1)
    value=sum((2*z**(2*j+1)/F(2*j+1) for j in range(25)),F())
    rem=2*z**51/(F(51)*(1-z*z))
    l2=log2_interval()
    return roundbox((value+n*l2[0],value+rem+n*l2[1]))

@lru_cache(maxsize=1,typed=True)
def gamma_constant_interval():
    """Euler-Maclaurin H16 remainder used by authentic PR85 source."""
    n=16
    H=sum((F(1,k) for k in range(1,n+1)),F())
    c=H-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)+F(1,252*n**6)
    l=log_interval(n)
    return roundbox((c-l[1]-F(1,240*n**8),c-l[0]))

@lru_cache(maxsize=1,typed=True)
def original_contact_interval():
    """C_G=gamma+pi/2+3 log2+log pi: genuine real one-Gamma contact."""
    g=gamma_constant_interval();p=pi_interval();l2=log2_interval()
    lp=(log_interval(p[0])[0],log_interval(p[1])[1])
    return roundbox((g[0]+p[0]/2+3*l2[0]+lp[0],g[1]+p[1]/2+3*l2[1]+lp[1]))

@lru_cache(maxsize=1,typed=True)
def inverse_sqrt2_interval():
    s=10**40
    floor=isqrt(2*s*s)
    # floor/s <=sqrt2<(floor+1)/s
    return roundbox((F(s,floor+1),F(s,floor)))

@lru_cache(maxsize=1,typed=True)
def true_prime2_weight_interval():
    l2=log2_interval();q2=inverse_sqrt2_interval()
    return roundbox((l2[0]*q2[0],l2[1]*q2[1]))


def neg_sinh4_interval(r):
    """Original pole derivative -4 sinh(r/2), r>=0."""
    r=q(r)
    pos=exp_interval(r/2);neg=exp_neg_interval(r/2)
    return roundbox((-2*(pos[1]-neg[0]), -2*(pos[0]-neg[1])))


@lru_cache(maxsize=5000,typed=True)
def gamma_derivative_interval(r):
    """Exact -sum_j 2 e^(-(4j+1)r/2)/(4j+1).

    For z=e^-r/2, this equals -atanh(z)-atan(z); first Gamma layer
    and all other rungs, never separate artificial baths.
    """
    r=q(r)
    if not 0<r<=1:raise SignedSourceEnclosureError('nonzero original Gamma argument')
    zlo,zhi=exp_neg_interval(r/2)
    # atanh z = (log(1+z)-log(1-z))/2, increasing on 0<z<1
    def atanh(z):
        if not 0<=z<1:raise SignedSourceEnclosureError('Gamma argument must be <1')
        p=log_interval(1+z);m=log_interval(1-z)
        return roundbox(((p[0]-m[1])/2,(p[1]-m[0])/2))
    a=atanh(zlo);b=atanh(zhi)
    c=atan_interval(zlo);d=atan_interval(zhi)
    return roundbox((-b[1]-d[1], -a[0]-c[0]))


def prime_step_interval(lo,hi):
    """Allow the actual log2 threshold to occupy one ambiguous grid cell."""
    lo=q(lo);hi=q(hi)
    l2=log2_interval();w=true_prime2_weight_interval()
    if hi<=l2[0]:return F(),F()
    if lo>=l2[1]:return w
    return F(),w[1]


def original_derivative_interval(lo,hi):
    """Guaranteed enclosure on rational cell [lo,hi], lo>0.

    Pole decreases with r, Gamma-derivative increases with r, exact
    contact is constant and true prime-2 step monotone (jump allowed).
    """
    lo=q(lo);hi=q(hi)
    if not 0<lo<=hi<=1:raise SignedSourceEnclosureError('window 0<r<=1')
    p_lo=neg_sinh4_interval(hi)[0]
    p_hi=neg_sinh4_interval(lo)[1]
    g_lo=gamma_derivative_interval(lo)[0]
    g_hi=gamma_derivative_interval(hi)[1]
    contact=original_contact_interval()
    prime=prime_step_interval(lo,hi)
    return p_lo+g_lo+contact[0]/2+prime[0],p_hi+g_hi+contact[1]/2+prime[1]


@lru_cache(maxsize=8,typed=True)
def original_first_window_l1_certificate(cells=512):
    """Exact rational upper bound for integral_-1^1 |g'(r)|dr.

    Split (0,1] into (0,1/cells] logarithmic singular majorant and
    closed rational boxes. Bounds hold for every point, not quadrature
    at a few samples. Oddness gives a factor 2.
    """
    if type(cells) is not int or not 16<=cells<=4096:
        raise SignedSourceEnclosureError('Finite proof cell budget 16..4096')
    step=F(1,cells)
    c=original_contact_interval()
    # (0,delta): atanh(e^-r/2)<=.5 log(6/r), atan<1,
    # |pole'|<=4 sinh(delta/2), contact<=C/2; true p2 is absent.
    ps=neg_sinh4_interval(step)
    near=step*(c[1]/2+(-ps[0])+1) + step*(log_interval(6/step)[1]+1)/2
    upper=near
    lower=F()
    bound_const=c[1]/2+(-ps[0])+1+log_interval(6/step)[1]/2
    sq_upper=step*(bound_const*bound_const+bound_const+F(1,2))
    sq_lower=F()
    for j in range(1,cells):
        lo,hi=original_derivative_interval(F(j,cells),F(j+1,cells))
        upper+=step*max(abs(lo),abs(hi))
        minimum=(min(abs(lo),abs(hi)) if lo*hi>0 else F())
        lower+=step*minimum
        sq_upper+=step*max(abs(lo),abs(hi))**2
        sq_lower+=step*minimum**2
    return {"source":"ORIGINAL_ZETA_GAMMA_CONTACT_POLES_PRIME2",
            "cells":cells,"delta":step,"gprime_L1_lower":2*lower,
            "gprime_L1_STRICT_upper":2*upper,
            "gprime_L2_squared_lower":2*sq_lower,
            "gprime_L2_squared_STRICT_upper":2*sq_upper,
            "positive_rational_certificate":True,"nontrivial_zeros_used":False,
            "RH_proved":False}


def original_primitive_interval(radius=F(1,4), cells=512):
    """Independent exact-rational primitive of authenticated original g'.

    Encloses g(radius)=int_0^radius g' for rational 0<radius<=1;
    near-zero first cell is bounded in ABSOLUTE value analytically,
    not point-sampled. This is a cross-representation source audit, not a
    full signed Weil all-test positivity assertion.
    """
    r=q(radius)
    if not 0<r<=1 or type(cells) is not int or not 32<=cells<=4096:
        raise SignedSourceEnclosureError('positive source primitive radius/steps')
    delta=r/cells
    c=original_contact_interval()
    pole=neg_sinh4_interval(delta)
    near=delta*(c[1]/2-pole[0]+1)+delta*(log_interval(6/delta)[1]+1)/2
    lo=-near;hi=near
    for i in range(1,cells):
        a,b=original_derivative_interval(i*delta,(i+1)*delta)
        lo+=delta*a
        hi+=delta*b
    return lo,hi
