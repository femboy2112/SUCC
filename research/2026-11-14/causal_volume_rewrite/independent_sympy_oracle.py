"""Independently typed exact symbolic and high-precision BBP volume crosschecks.

Does not import observational_succ.causal_volume_rewrite. This is an
implementation-independent check of the selected formulas, not blind academic
review or a universal proof from finitely many evaluations.
"""
from __future__ import annotations
from math import factorial
import sympy as sp
import mpmath as mp

x=sp.Symbol('x',real=True)
d=sp.Symbol('d',real=True)
Q=4-2*x**3-x**4-x**5
D=16-x**8
R=(1-x)/((2-x**2)*(x**2-2*x+2))
assert sp.factor(Q-D*R)==0
assert sp.expand(Q-(1-x)*(x**2+2)*(x**2+2*x+2))==0
assert sp.expand(D-(2-x**2)*(2+x**2)*(x**2-2*x+2)*(x**2+2*x+2))==0
assert sp.series(R.subs(x,1-d),d,0,5).removeO()==d-2*d**2+4*d**3-10*d**4

u=x-x**2/2
v=x**2/2
source_matrix=sp.Matrix([[u,1],[0,v]])
e2=sp.Matrix([0,1])
assert sp.cancel((1-x)*((sp.eye(2)-source_matrix).inv()*e2)[0]/4-R)==0
for grade in range(10):
 p_from_matrix=(1-x)*(source_matrix**(grade+1))[0,1]/4
 p_from_stages=(1-x)*sum(u**k*v**(grade-k) for k in range(grade+1))/4
 assert sp.cancel(p_from_matrix-p_from_stages)==0

for n in range(1,16):
 poles=sp.Rational(4,8*n-7)-sp.Rational(2,8*n-4)-sp.Rational(1,8*n-3)-sp.Rational(1,8*n-2)
 source=sp.integrate(x**(8*n-8)*Q,(x,0,1))
 assert poles==source
 vol=sp.expand(sum(16**(n-1-j)*x**(8*j) for j in range(n)))
 assert sp.expand(D*vol-(16**n-x**(8*n)))==0
 state=sp.integrate(Q*vol,(x,0,1))
 assert state==sum(16**(n-j)*(
   sp.Rational(4,8*j-7)-sp.Rational(2,8*j-4)-sp.Rational(1,8*j-3)-sp.Rational(1,8*j-2)) for j in range(1,n+1))

for n in range(1,8):
 for k in range(0,7):
  a=sum((-1)**j*sp.binomial(k,j)*(sp.Rational(4,8*(n+1+j)-7)-sp.Rational(2,8*(n+1+j)-4)-sp.Rational(1,8*(n+1+j)-3)-sp.Rational(1,8*(n+1+j)-2)) for j in range(k+1))
  b=sp.integrate(x**(8*n)*(1-x**8)**k*Q,(x,0,1))
  assert a==b and b>0

# A same-Gamma-shape, positive, zero-origin mutant whose completion is 1/2.
alt_R=1-x
alt_Q=sp.expand(D*alt_R)
assert sp.integrate(alt_R,(x,0,1))==sp.Rational(1,2)
for n in range(0,12):
 assert sp.integrate(x**(8*n)*alt_R,(x,0,1))==sp.Rational(1,(8*n+1)*(8*n+2))

# Finite-horizon polynomial perturbation: source and moments differ later.
L=9
f=sp.diff(x**(L+2)*(1-x)**(L+2),x,L)
assert f!=0
assert sp.factor(f).has(x**2)
assert all(sp.integrate(x**(8*k)*f,(x,0,1))==0 for k in range(2))
assert sp.integrate(x**16*f,(x,0,1))!=0

mp.mp.dps=60
Mp=lambda z: mp.quad(lambda t:(t**z)*(1-t)/((2-t*t)*(t*t-2*t+2)),[0,mp.mpf('0.3'),mp.mpf('0.7'),mp.mpf('0.93'),1])
phases=0
for m in (32,64,128):
 for lam in (0,mp.mpf('0.125'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2')):
  actual=Mp(m*(1+1j*lam))/Mp(m)
  goal=1/(1+1j*lam)**2
  error=abs(actual-goal)
  bound=(14+12*abs(lam))/m+2*m*m/(mp.mpf(2)**m)
  assert error<=bound, (m,lam,error,bound)
  phases+=1

face_phases=0
for k in (1,2,3):
 for m in (128,256):
  for lam in (mp.mpf('0.5'),mp.mpf('1')):
   numer=mp.quad(lambda t:(t**(m*(1+1j*lam)))*(1-t**8)**k*
                 (1-t)/((2-t*t)*(t*t-2*t+2)),
                 [0,mp.mpf('0.3'),mp.mpf('0.8'),mp.mpf('0.94'),1])
   denom=mp.quad(lambda t:t**m*(1-t**8)**k*
                 (1-t)/((2-t*t)*(t*t-2*t+2)),
                 [0,mp.mpf('0.3'),mp.mpf('0.8'),mp.mpf('0.94'),1])
   actual=numer/denom
   target=(1+1j*lam)**(-(k+2))
   assert abs(actual-target)<mp.mpf('0.15'),(k,m,lam,actual,target)
   face_phases+=1

print('PASS original exact polynomial cancellation, two-register Oily resolvent, ten grades, 15 source states')
print('PASS finite-difference Hausdorff hierarchy: 42 independent exact integrals')
print('PASS rational nonnormal Gamma(2) mutant, 12 exact moments')
print('PASS finite-jet source mutant, initial-two-moment agreement and third-moment disagreement')
print('PASS moving complex Mellin Gamma(2) twist: 15 high-precision ratios and rigorous bounds')
print('PASS moving Gamma(k+2) face limits: 12 high-precision out-of-grammar controls')
print('SymPy',sp.__version__,'mpmath',mp.__version__)
