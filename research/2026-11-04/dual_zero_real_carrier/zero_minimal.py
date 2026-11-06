"""Source-faithful dual-zero / real projective bridge. Research only.

Original signed four-pole BBP source and literal U0=0 unchanged.
The cyclotomic coordinate is algebraic; no pi digits or Haar samples.
"""
from fractions import Fraction as F
from math import comb

ANG=(F(2),F(2),F(1),F(0),-F(1,2),-F(1,2),-F(1,4),F(0))

def source(n,primal=False):
    if type(n)!=int or n<1:raise ValueError('positive source time')
    if primal:
        return sum((w/F(8*(n-1)+j) for j,w in enumerate(ANG,1)),F(0))
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def phase(n,primal=False):
    if type(n)!=int or n<0:raise ValueError('n>=0')
    x=F(0)
    for j in range(1,n+1):x=(16*x+source(j,primal))%1
    if x.denominator%2==0:raise ArithmeticError('odd source phase expected')
    return x

def cayley(t):
    """Rational projective tangent -> (Re,Im) of exact Gaussian unit."""
    if t is None:return F(-1),F(0)
    x=F(t);a,b=x.numerator,x.denominator;N=a*a+b*b
    return F(b*b-a*a,N),F(2*a*b,N)

def tangent_minpoly(M):
    """Odd-order cyclotomic tangent minimal polynomial, no pi digits."""
    from sympy import Symbol,Poly,I,cyclotomic_poly,expand
    if type(M)!=int or M<1 or M%2==0:raise ValueError('odd conductor')
    t,x=Symbol('T'),Symbol('X')
    if M==1:return Poly(t,t)
    phi=Poly(cyclotomic_poly(M,x),x);d=phi.degree()
    return Poly(expand(sum(int(c)*(1+I*t)**(d-j)*(1-I*t)**j
                           for j,c in enumerate(phi.all_coeffs()))),t)

def degree_for_phase(x):
    from sympy import totient
    x=F(x)%1
    if x.denominator%2==0:raise ValueError('odd source phase')
    return int(totient(x.denominator))

def reciprocal_source_phase(x):
    x=F(x)%1
    if x.denominator%2==0:raise ValueError('odd source phase')
    y=(F(1,2)-x)%1
    if y.denominator!=2*x.denominator:raise ArithmeticError('2-primary gap')
    return y

def zero_projectors(M):
    from sympy import Matrix,Rational
    if type(M)!=int or M<1 or M%2==0 or M>100:raise ValueError('small odd M')
    PF=Matrix(M,M,lambda a,b:Rational(1,M))
    P0=Matrix(M,M,lambda a,b:int(a==0 and b==0))
    return PF,P0

def even_odd_tangent_polys():
    from sympy import Symbol,Poly
    t=Symbol('t')
    A=Poly(sum((-1)**k*comb(16,2*k)*t**(2*k) for k in range(9)),t)
    B=Poly(sum((-1)**k*comb(16,2*k+1)*t**(2*k+1) for k in range(8)),t)
    return A,B

def tangent16(t):
    if t is None:return F(0)
    A,B=even_odd_tangent_polys();x=F(t);a=F(A.eval(x));b=F(B.eval(x))
    return None if a==0 else b/a

def tangent_add(x,y):
    if x is None:return F(0) if y is None else (None if y==0 else -1/F(y))
    if y is None:return None if x==0 else -1/F(x)
    x,y=F(x),F(y)
    return None if x*y==1 else (x+y)/(1-x*y)

def source_real_step(t,forcing_tangent):
    """Exact projective real lift of x->16x+r (source r separately supplied)."""
    return tangent_add(tangent16(t),forcing_tangent)
