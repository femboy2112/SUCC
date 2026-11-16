#!/usr/bin/env python3
"""Independent finite diagnostics for the rate-tilt resonance hierarchy.
No SUCC module imports. Floating-point outputs are not interval certificates.
"""
from fractions import Fraction as F
from math import comb
import json
import mpmath as mp
import sympy as sp

mp.mp.dps=90
DEPTH=64
PAIRS=((3,2),(4,1),(5,1))


def moment(order):
    q=F(1,16);geom=[F(1)]
    for r in range(1,order+1):
        geom.append(q/(1-q)*sum((comb(r,j)*geom[j] for j in range(r)),F()))
    answer=F()
    for j in range(order+1):
        ell=order-j
        cell=sum((F(v*((1+d)**(ell+1)-1),15*(ell+1)) for d,v in PAIRS),F())
        answer+=comb(order,j)*8**j*geom[j]*cell
    return answer


def qq(x):
    x=F(x);return mp.mpf(x.numerator)/x.denominator


def psi(n,k,beta,detuning):
    a=mp.mpf(8*n);c=2*mp.pi*k;t=a*c+detuning
    exponent=1-beta-1j*t
    num=mp.mpc(0);den=mp.mpf(0)
    for j in range(1,DEPTH+1):
        b=8*j-7
        for length,v in PAIRS:
            left=1+mp.mpf(b)/a;right=1+mp.mpf(b+length)/a
            p=mp.mpf(v)/16**j
            num+=p*a*(right**exponent-left**exponent)/exponent
            if beta==1:
                den+=p*a*mp.log(right/left)
            else:
                den+=p*a*(right**(1-beta)-left**(1-beta))/(1-beta)
    return num/den


def cubic_constant(c,d,moments):
    # Build the exact positive polynomial in B using |c|,|d| numerically;
    # this expression directly evaluates the paper's global remainder.
    x=sp.Symbol('x')
    C,D=sp.symbols('C D',nonnegative=True)
    M=C*x*x/2+D*x
    N=C*x**3/3+D*x*x/2
    R=C*x**4/4+D*x**3/3
    polynomial=sp.Poly(sp.expand(x**3+M*x*x+x*(N+M*M/2)+R+M*N+M**3/6),x)
    total=mp.mpf(0)
    for (degree,),coef in polynomial.terms():
        total+=mp.mpf(str(coef.subs({C:sp.Float(str(abs(c)),90),D:sp.Float(str(abs(d)),90)}).evalf(85)))*qq(moments[degree])
    return total


def complex_record(z):
    return {'real':mp.nstr(z.real,20),'imag':mp.nstr(z.imag,20)}


def symbolic_checks():
    c,d,mu,m2,m3,beta=sp.symbols('c d mu m2 m3 beta',real=True,nonzero=True)
    e1=sp.I/c
    e2=2*mu*sp.I/c+2/c**2
    e3=3*m2*sp.I/c+6*mu/c**2-6*sp.I/c**3
    e4=4*m3*sp.I/c+12*m2/c**2-24*mu*sp.I/c**3-24/c**4
    first=-(beta+sp.I*d)*e1+sp.I*c*e2/2
    assert sp.simplify(first-(d/c-mu+sp.I*(1-beta)/c))==0
    second=(1-d*d/2+3*sp.I*d/2)*e2+(c*d/2-5*sp.I*c/6)*e3-c*c*e4/8
    predicted=m2-mu**2-sp.I*c*(m3-3*mu*m2+2*mu**3)/2
    assert sp.simplify(second.subs(d,mu*c)-predicted)==0
    # Derive E[B^r exp(-icB)] from K+V directly, using integration by parts.
    K=sp.Symbol('K',real=True)
    cell=[0]
    for r in range(1,5):
        cell.append(sp.I/c+sp.Rational(r,1)/(sp.I*c)*cell[r-1])
    km1=mu-sp.Rational(1,2)
    km2=m2-km1-sp.Rational(1,3)
    km3=m3-sp.Rational(3,2)*km2-km1-sp.Rational(1,4)
    km=[1,km1,km2,km3]
    for r,expected in ((1,e1),(2,e2),(3,e3),(4,e4)):
        actual=sum(sp.binomial(r,j)*cell[j]*km[r-j] for j in range(1,r+1))
        assert sp.simplify(actual-expected)==0
    return 6


def main():
    moments=[moment(r) for r in range(7)]
    mu=moments[1];var=moments[2]-mu*mu
    skew=moments[3]-3*mu*moments[2]+2*mu**3
    assert (mu,var,skew)==(F(7,2),F(73,12),F(42))
    exact=symbolic_checks()+1
    controls=((2,F(2,3)),(3,F(1,4)),(11,F(1,12)))
    control_moments=[sum((p*F((b+1)**(r+1)-b**(r+1),r+1)
                         for b,p in controls),F()) for r in range(4)]
    for r in range(4):
        assert control_moments[r]==moments[r]
        exact+=1
    control_x=sum((p*F(1,b*(b+1)) for b,p in controls),F())
    assert control_x==F(35,264)
    exact+=1
    for n in range(1,6):
        assert (33*16**n*control_x).denominator==1
        exact+=1
    grid=(19,113,977,8191,131071,2097143,33554393)
    first_rows=[];second_rows=[];diagnostics=0
    for k in (-2,3,7):
        c=2*mp.pi*k;d=qq(mu)*c
        expected2=qq(var)-1j*c*qq(skew)/2
        C3=cubic_constant(c,d,moments)
        for n in grid:
            a=8*n
            value=psi(n,k,mp.mpf(1),d)
            scaled=a*a*value
            error=abs(scaled-expected2)
            bound=(1+qq(mu)/a)*(C3+qq(mu)*abs(expected2))/a
            assert error<=bound
            diagnostics+=1
            second_rows.append({'n':n,'k':k,'a2_Psi':complex_record(scaled),
                'predicted':complex_record(expected2),'error':mp.nstr(error,12),
                'proved_error_bound':mp.nstr(bound,12)})
        for beta in (mp.mpf(0),mp.mpf('0.5'),mp.mpf('1.5'),mp.mpf(2),mp.mpf(3)):
            n=grid[-1];a=8*n
            scaled=a*psi(n,k,beta,d)
            expected=1j*(1-beta)/c
            assert abs(scaled-expected)<mp.mpf('0.0001')
            diagnostics+=1
            first_rows.append({'n':n,'k':k,'beta':str(beta),
                'a_Psi':complex_record(scaled),'predicted':complex_record(expected)})
    print(json.dumps({'status':'FINITE_DIAGNOSTICS_NOT_PROOF','exact_checks':exact,
        'diagnostic_checks':diagnostics,'mpmath_decimal_digits':mp.mp.dps,
        'depth':DEPTH,'omitted_base_mass':str(F(1,16**DEPTH)),
        'moments':[str(x) for x in moments],
        'matched_cell_control':{'moments':[str(x) for x in control_moments],
             'endpoint':str(control_x),'locked_harmonic':33},
        'first_order_rows':first_rows,'second_order_rows':second_rows},indent=2))

if __name__=='__main__':main()
