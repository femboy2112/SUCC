"""SUCC dual zero / rational real Cayley observer, research only.

All finite arithmetic below is exact. The formal x->tan(pi*x) coordinate is
specified by a cyclotomic polynomial and NEVER numerically constructed as a
source oracle. The missing signed Weyl estimate is explicitly OPEN.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, gcd, lcm

ANG_TAPS = (Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0))
RADIX=16


def authentic_r(n: int) -> Q:
    if type(n) is not int or n<1:raise ValueError('positive source time')
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def primal_r(n:int) -> Q:
    if type(n) is not int or n<1: raise ValueError('positive source time')
    return sum((w/Q(8*(n-1)+j) for j,w in enumerate(ANG_TAPS,1)), Q(0))


def source_phase_stream(nlast:int,primal=False):
    if type(nlast) is not int or nlast<0:raise ValueError('nonnegative horizon')
    x=Q(0)
    yield (0,x)
    for n in range(1,nlast+1):
        x=(RADIX*x+(primal_r(n) if primal else authentic_r(n)))%1
        if x.denominator%2==0:raise ArithmeticError('unexpected even source phase')
        yield (n,x)


def integer_oracle_stream(nlast:int,primal=False):
    """Independent LCM integer recurrence using a full-horizon denominator."""
    if type(nlast) is not int or nlast<0:raise ValueError('nonnegative horizon')
    taps=ANG_TAPS if primal else (Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
    vals=[]
    for n in range(1,nlast+1):
        r=sum((weight / (8*(n-1)+j) for j,weight in enumerate(taps,1)),Q(0))
        vals.append(r)
    M=1
    for r in vals: M=lcm(M,r.denominator)
    if M%2==0:raise ArithmeticError('phase conductor should be odd')
    A=0
    yield 0,Q(0)
    for j,r in enumerate(vals,1):
        A=(16*A+r.numerator*(M//r.denominator))%M
        yield j,Q(A,M)


def minimal_source_conductor(nlast:int,primal=False) -> int:
    q=1
    for _,x in source_phase_stream(nlast,primal):q=lcm(q,x.denominator)
    return q


def cayley_rational(t:Q|None)->tuple[Q,Q]:
    """(Re,Im) of (1+i*t)/(1-i*t), t=None denotes infinity."""
    if t is None:return Q(-1),Q(0)
    x=Q(t)
    a,b=x.numerator,x.denominator
    den=a*a+b*b
    return Q(b*b-a*a,den),Q(2*a*b,den)


def inverse_cayley_rational(z:tuple[Q,Q])->Q|None:
    c,s=map(Q,z)
    if c*c+s*s!=1:raise ValueError('must be rational point on unit circle')
    if c==-1:return None
    return s/(1+c)


def cayley_reciprocal(t:Q)->tuple[Q,Q]:
    t=Q(t)
    if not t: return cayley_rational(None)
    return cayley_rational(1/t)


def projective_chart_quarters(u:Q):
    """Four rational arcs from the SAME unit interval, oriented counterclockwise."""
    u=Q(u)
    if not Q(0)<=u<=Q(1):raise ValueError('unit interval')
    return (cayley_rational(u),
            cayley_rational(1/u) if u else cayley_rational(None),
            cayley_rational(-1/u) if u else cayley_rational(None),
            cayley_rational(-u))


def source_tangent_descriptor(phase:Q)->dict:
    """No pi digits: t is real root of cyclotomic Cayley equation.

    If phase reduced a/M, M odd, t=tan(pi*a/M) is algebraic degree phi(M).
    Sign/sector for identifying the correct real root comes from a/M.
    """
    from sympy import totient
    z=Q(phase)%1
    if z.denominator%2==0:raise ValueError('source odd-conductor phase only')
    M=z.denominator
    return {'phase':z,'numerator':z.numerator,'conductor':M,
            'exact_algebraic_degree':int(totient(M)),
            'description':f'tan(pi*{z.numerator}/{M})= -i*(zeta_{M}^{z.numerator}-1)/(zeta_{M}^{z.numerator}+1)'}


@lru_cache(maxsize=64)
def tangent_minpoly_for_odd_conductor(M:int):
    """Integer polynomial R_M(T), defined WITHOUT pi or evaluating tan.

    (1-iT)^phi(M)*Phi_M((1+iT)/(1-iT))=0 at tangent of any
    primitive Mth root, M odd. For M>1 it has degree phi(M), irreducible.
    """
    from sympy import Poly,Symbol,I,cyclotomic_poly,expand
    if type(M) is not int or M<1 or M%2==0:raise ValueError('positive odd conductor')
    t,z=Symbol('T'),Symbol('Z')
    if M==1:return Poly(t,t)
    phi=Poly(cyclotomic_poly(M,z),z)
    d=phi.degree()
    P=expand(sum(int(a)*(1+I*t)**(d-j)*(1-I*t)**j
                 for j,a in enumerate(phi.all_coeffs())))
    poly=Poly(P,t)
    if any(not c.is_Integer for c in poly.all_coeffs()):raise ArithmeticError('non-integer coeff')
    if poly.degree()!=d:raise ArithmeticError('wrong degree')
    return poly


def angle_16_pair():
    """Real and imaginary integer polynomials of (1+i*t)^16."""
    from sympy import Symbol,Poly
    t=Symbol('t')
    A=sum((-1)**k*comb(16,2*k)*t**(2*k) for k in range(9))
    B=sum((-1)**k*comb(16,2*k+1)*t**(2*k+1) for k in range(8))
    return Poly(A,t),Poly(B,t)


def tangent16_projective(t:Q|None):
    """Rational tangent multiple-angle, infinity allowed; no pi oracle."""
    if t is None:return Q(0) # tan(16*pi/2)=0
    t=Q(t);A,B=angle_16_pair()
    aa=Q(int(A.eval(t).p),int(A.eval(t).q)) if hasattr(A.eval(t),'p') else Q(A.eval(t))
    bb=Q(int(B.eval(t).p),int(B.eval(t).q)) if hasattr(B.eval(t),'p') else Q(B.eval(t))
    return None if not aa else bb/aa


def tangent_add_projective(t:Q|None,s:Q|None):
    """Tangent addition on RP1: full projective formula, no branch drop."""
    if t is None:
        return Q(0) if s is None else -1/Q(s) if s else None
    if s is None:return -1/Q(t) if t else None
    t,s=Q(t),Q(s)
    return None if t*s==1 else (t+s)/(1-t*s)


def tangent_forced_step(t:Q|None,forcing_tan:Q|None):
    return tangent_add_projective(tangent16_projective(t),forcing_tan)


def zero_overlap(M:int)->Q:
    if type(M) is not int or M<1 or M%2==0:raise ValueError('odd cyclic conductor')
    return Q(1,M)


def zero_commutator_hs_square(M:int)->Q:
    if type(M) is not int or M<1 or M%2==0:raise ValueError('odd cyclic conductor')
    return Q(2*(M-1),M*M)


def zero_projectors(M:int):
    """Full EXACT rational matrices for calibrated small carriers only."""
    from sympy import Matrix,Rational
    if type(M) is not int or M<1 or M>100 or M%2==0:raise ValueError('small odd M')
    H=Matrix(M,M,lambda a,b:Rational(1,M))
    P=Matrix(M,M,lambda a,b:int(a==0 and b==0))
    return H,P


def fourier_refinement_factor(M:int,Mprime:int)->Q:
    if type(M) is not int or type(Mprime) is not int or M<1 or Mprime<M or Mprime%M or Mprime%2==0:raise ValueError('nested odd cyclic')
    return Q(M,Mprime) # square of amplitude scaling


def exact_source_circle_character(h:int,phase:Q)->tuple[int,int,int]:
    """An EXACT cyclotomic character, not a floating complex or a tangent guess.
    Return canonical root-of-unity exponent h*a modulo M.
    """
    z=Q(phase)%1
    return (int(h*z.numerator)%z.denominator,z.denominator,int(h))


def rational_cayley_split_denominator(t:Q)->int:
    """LCM of the reduced rational circle coordinate denominators."""
    x,y=cayley_rational(t)
    return lcm(x.denominator,y.denominator)
