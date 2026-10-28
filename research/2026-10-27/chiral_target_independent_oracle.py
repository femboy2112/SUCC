"""Independent symbolic derivation; optional SymPy, not runtime dependency."""
from fractions import Fraction
import sympy as s

t,n=s.symbols('t n')
fplus=(2-t)/(4*(t*t-2*t+2));fminus=-t/(4*(2-t*t))
rplus=t*(1-t)/(4*(t*t-2*t+2));rminus=(1-t)*(t+2)/(4*(2-t*t))
assert s.cancel(fplus-s.Rational(1,4)-rplus)==0
assert s.cancel(fminus+s.Rational(1,4)-rminus)==0
assert s.cancel(rplus+rminus-(1-t)/((2-t*t)*(t*t-2*t+2)))==0
assert fplus.subs(t,1)==s.Rational(1,4)
assert fminus.subs(t,1)==-s.Rational(1,4)
# Independent formal series at the endpoint, not a finite numerical fit.
y=s.symbols('y')
assert s.series(rplus.subs(t,1-y),y,0,2).removeO()==y/4
assert s.series(rminus.subs(t,1-y),y,0,2).removeO()==3*y/4
# Native rational source in a direct pole decomposition.
a=4/(8*n-7)+1/(4*n-3)-1/(4*(2*n-1))-1/(8*n-3)-1/(4*(4*n-1))+1/(32*n)
b=-1/(4*n-3)-1/(4*(2*n-1))-1/(4*(4*n-1))-1/(32*n)
original=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
assert s.cancel(a+b-original)==0
assert s.limit(n*a,n,0)==s.Rational(1,32)
assert s.limit(n*b,n,0)==-s.Rational(1,32)
assert s.limit(n*a,n,s.oo)==s.Rational(15,32)
assert s.limit(n*b,n,s.oo)==-s.Rational(15,32)
X=s.symbols('X')
assert s.expand((X-1)*(X-16))==X**2-17*X+16
print('INDEPENDENT SYMBOLIC GAUGE, ENDPOINT, POLE, SOURCE AND TWO-CLOCK IDENTITIES PASS')
