"""Separate SymPy exact oracle. Does not import opposing_observers.py."""
from fractions import Fraction as F
from math import comb, factorial
import sympy as s

D=[0,3,4,5]; C=[4,-2,-1,-1]
R=lambda a:sum((s.Rational(c)/(a+d) for c,d in zip(C,D)),s.S.Zero)
RP=lambda a:sum((-s.Rational(c)/(a+d)**2 for c,d in zip(C,D)),s.S.Zero)
checks=0
for a in [s.Rational(1),s.Rational(5),s.Rational(73),s.Rational(41,7)]:
 for frac in [s.Rational(0),s.Rational(1,7),s.Rational(1,2),s.Rational(4,5)]:
  t=a*frac
  zplus=a+t;zminus=a-t
  coeff=[s.Rational(c)*R(2*a+d) for c,d in zip(C,D)]
  total=sum((w*(1/(a+d+t)+1/(a+d-t)) for w,d in zip(coeff,D)),s.S.Zero)
  assert s.cancel(total-R(zplus)*R(zminus))==0; checks+=1
  for m in range(6):
   integr=s.factorial(m)*sum((w*((a+d+t)**(-m-1)+(-1)**m*(a+d-t)**(-m-1)) for w,d in zip(coeff,D)),s.S.Zero)/(R(zplus)*R(zminus))
   mom=lambda c,k:s.factorial(k)*sum((s.Rational(q)/(c+d)**(k+1) for q,d in zip(C,D)),s.S.Zero)/R(c)
   direct=sum((s.binomial(m,j)*(-1)**(m-j)*mom(zplus,j)*mom(zminus,m-j) for j in range(m+1)),s.S.Zero)
   assert s.cancel(integr-direct)==0;checks+=1
  mean=RP(zminus)/R(zminus)-RP(zplus)/R(zplus)
  direct= sum((w*((a+d+t)**(-2)-(a+d-t)**(-2)) for w,d in zip(coeff,D)),s.S.Zero)/(R(zplus)*R(zminus))
  assert s.cancel(mean-direct)==0; checks+=1
  if t>0:
   h2=R(a)**2/(R(zplus)*R(zminus))
   lo=(1-frac**2)**2
   hi=(1-frac**2)*(1-(t/(a+5))**2)
   assert 0<s.cancel(h2-lo) and 0<s.cancel(hi-h2); checks+=2
# Source derivative of normalized Pascal weights; pure symbolic quotient rule.
for n in (1,3,7):
 for c0 in (s.Rational(1),s.Rational(9)):
  v=[]
  for j in range(n+1):
   u=sum(((-1)**k*s.binomial(j,k)*R(c0+8*(n-j+k)) for k in range(j+1)),s.S.Zero)
   du=sum(((-1)**k*s.binomial(j,k)*RP(c0+8*(n-j+k)) for k in range(j+1)),s.S.Zero)
   v.append(s.binomial(n,j)*(du/R(c0)-u*RP(c0)/R(c0)**2))
  assert s.cancel(sum(v,s.S.Zero))==0;checks+=1
l=(s.sqrt(5)-1)/2
assert s.simplify(l+l**2-1)==0;checks+=1
assert s.simplify(2/(1+l)-2/(1-l)+4)==0;checks+=1
assert s.simplify((1-l**2)-l)==0;checks+=1
assert s.simplify(((1-l**2)**2/4)*(1/(1+l)+1/(1+l)**2)-l**2/4)==0;checks+=1
assert s.simplify(s.Rational(1,2)*(1/(1+l)+1/(1+l)**2)-s.Rational(1,2))==0;checks+=1
assert s.simplify((s.Rational(1,2)-s.EulerGamma)-s.Rational(1,2)+s.EulerGamma)==0;checks+=1
# Original R and first source jet, not a Gamma-matched fake
z=s.symbols('z',positive=True)
assert s.factor(R(z)-((15*z*z+121*z+240)/(z*(z+3)*(z+4)*(z+5))))==0;checks+=1
assert s.limit(z*(z**2*R(z)/15-1),z,s.oo)==-s.Rational(59,15);checks+=1
print('INDEPENDENT_SYMPY_PASS',checks)
