"""Separate symbolic/calculus implementation; not a blind external referee."""
import json
from fractions import Fraction
import sympy as s
import mpmath as mp

a,u=s.symbols('a u',positive=True)
V=a**4/((a+3)**2*(a+4)*(a+5))
R=4/a-2/(a+3)-1/(a+4)-1/(a+5)
assert s.cancel(s.diff(V,a)/V-R)==0
derivatives={}
for order in range(1,5):
    expression=s.cancel((-1)**order*s.diff(R,a,order))
    num,den=s.fraction(expression)
    assert all(coefficient>0 for coefficient in s.Poly(num,a).all_coeffs())
    # Powers of a produce zero trailing coefficients; nonnegative coefficients
    # with at least one positive term imply strict positivity for a>0.
    assert all(coefficient>=0 for coefficient in s.Poly(den,a).all_coeffs())
    assert any(coefficient>0 for coefficient in s.Poly(den,a).all_coeffs())
    derivatives[str(order)]={"numerator":str(num),"denominator":str(den)}
assert -s.diff(R,a).subs(a,1)==s.Rational(6853,1800)
assert -s.diff(R,a).subs(a,2)==s.Rational(38447,44100)
assert s.diff(R,a,2).subs(a,1)==s.Rational(427261,54000)

symbolic=[]
for n in (1,2):
    B=s.prod(V.subs(a,8*j-7+u)**16**(n-j) for j in range(1,n+1))
    first=s.cancel((s.diff(B,u)/B).subs(u,0))
    actual=sum(16**(n-j)*R.subs(a,8*j-7) for j in range(1,n+1))
    assert first==actual
    symbolic.append({"n":n,"first_jet":str(first)})

mp.mp.dps=90
Rmp=lambda x:4/x-2/(x+3)-1/(x+4)-1/(x+5)
Vmp=lambda x:x**4/((x+3)**2*(x+4)*(x+5))
C=mp.fsum(16**(-mp.mpf(j))*(4/mp.mpf(8*j-7)**2-2/mp.mpf(8*j-4)**2-1/mp.mpf(8*j-3)**2-1/mp.mpf(8*j-2)**2) for j in range(1,65))
samples=[]
for n in (2,11,37):
    for M in (3,257,10**6):
        d=mp.mpf(1)/M
        target=mp.fsum(mp.mpf(16)**(n-j)*Rmp(mp.mpf(8*j-7)) for j in range(1,n+1))
        secant=mp.fsum(M*mp.mpf(16)**(n-j)*mp.log(Vmp(mp.mpf(8*j-7)+d)/Vmp(mp.mpf(8*j-7))) for j in range(1,n+1))
        err=target-secant
        low=mp.mpf(38447)/44100*mp.mpf(16)**(n-1)/(2*M)
        high=mp.mpf(6853)/1800*(mp.mpf(16)**n-1)/(30*M)
        assert low <= err <= high
        scaled=err*M/mp.mpf(16)**n
        Cn=mp.fsum(mp.mpf(16)**(-j)*(4/mp.mpf(8*j-7)**2-2/mp.mpf(8*j-4)**2-1/mp.mpf(8*j-3)**2-1/mp.mpf(8*j-2)**2) for j in range(1,n+1))
        assert 0 <= Cn/2-scaled <= mp.mpf(427261)/54000/(90*M)
        samples.append({"n":n,"M":M,"scaled_error":mp.nstr(scaled,45)})

# Rational (not mpmath) tail enclosure for the sharp constant.
Rf=lambda j:Fraction(4,(8*j-7)**2)-Fraction(2,(8*j-4)**2)-Fraction(1,(8*j-3)**2)-Fraction(1,(8*j-2)**2)
lower=sum((Rf(j)/16**j for j in range(1,25)),Fraction())
upper=lower+Rf(25)/(15*16**24)
assert mp.mpf(lower.numerator)/lower.denominator<C<mp.mpf(upper.numerator)/upper.denominator

result={"status":"PASS","symbolic":symbolic,"alternating_derivative_polynomials":derivatives,"sharp_constant_rational_lower":str(lower),"sharp_constant_rational_upper":str(upper),"sharp_constant_numerical":mp.nstr(C,60),"numerical_holdouts":samples,"boundary":"Symbolic proof and exact rational bounds are authority. mpmath values are separate numerical calibration. No selected Weyl saving or normality result."}
print(json.dumps(result,indent=2))
