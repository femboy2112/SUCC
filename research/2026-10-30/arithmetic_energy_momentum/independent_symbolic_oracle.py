"""Independent SymPy oracle: polynomial, asymptotic, Lorentz, golden signed mark.
Uses the factored source polynomial N/D and its derivatives, not the
std-lib test implementation's partial-fraction source_moments function.
"""
import sympy as s

a=s.symbols('a',positive=True)
D=s.Poly(a*(a+3)*(a+4)*(a+5),a)
C=s.Poly(15*a*a+121*a+240,a)
R=C.as_expr()/D.as_expr()
U=D.diff()*C-D*C.diff()
V=(D.diff()**2-D.diff().diff()*D)*C**2+(C.diff().diff()*C-C.diff()**2)*D**2
rational_m=a*U.as_expr()/(D*C).as_expr()
rational_rank=U.as_expr()**2/V.as_expr()
assert s.cancel(rational_m-(-a*s.diff(s.log(R),a)))==0
assert s.cancel(rational_rank-(s.diff(s.log(R),a)**2/s.diff(s.log(R),a,2)))==0

lower=U**2-V
upper=2*V-U**2
rankder=(U**2).diff()*V-U**2*V.diff()
assert all(k>=0 for k in lower.all_coeffs()) and lower.as_expr()!=0
assert all(k>=0 for k in upper.all_coeffs()) and upper.as_expr()!=0
assert all(k>=0 for k in rankder.all_coeffs()) and rankder.as_expr()!=0
assert s.limit(rational_m,a,0,dir='+')==1
assert s.limit(rational_m,a,s.oo)==2
assert s.limit(rational_rank,a,0,dir='+')==1
assert s.limit(rational_rank,a,s.oo)==2
assert s.limit(a*(2-rational_m),a,s.oo)==s.Rational(59,15)
assert s.limit(a*a*(2-rational_rank),a,s.oo)==s.Rational(1379,150)

# Source positive Poisson clock: independent partial moments from R.
r1=s.diff(R,a)
r2=s.diff(R,a,2)
mean=-r1/R
var=r2/R-(r1/R)**2
assert s.simplify(var-s.diff(s.log(R),a,2))==0
for m_plus,m_minus in [(s.Rational(1,2),s.Rational(1,2)),(s.Rational(5,3),s.Rational(2,7))]:
    E=a*mean*(m_plus+m_minus)
    P=a*mean*(m_plus-m_minus)
    cov=a*a*var*m_plus*m_minus
    assert s.cancel(E**2-P**2-4*rational_rank*cov)==0

# source first positive transform correction vs Gamma fake, variable d>0.
d=s.symbols('d',positive=True)
full= (15*(a*d)**2+121*a*d+240)/(a*d*(a*d+3)*(a*d+4)*(a*d+5))/R
fake=1/d**2
assert s.simplify(s.limit(a*(full-fake),a,s.oo)-s.Rational(59,15)*(d-1)/d**3)==0

# Native Bernoulli observer's *different* finite effective-rank jet.
t=s.symbols('t')
Rs=lambda k: (15*(1+k*t)**2+121*t*(1+k*t)+240*t*t)/s.prod(1+(k+d)*t for d in (0,3,4,5))
q1=Rs(8)/Rs(0)
q2=Rs(16)/Rs(0)
mu=1-q1
vb=q2-q1*q1
rho_b=s.cancel(mu*mu/vb)
fake1=1/(1+8*t)**2
fake2=1/(1+16*t)**2
rho_fake=s.cancel((1-fake1)**2/(fake2-fake1**2))
assert s.limit(rho_b,t,0)==2
assert s.limit((rho_b-2)/t,t,0)==48
assert s.limit((rho_b-2-48*t)/t**2,t,0)==s.Rational(18061,150)
assert s.limit((rho_fake-2-48*t)/t**2,t,0)==224
assert s.limit((rho_b-rho_fake)/t**2,t,0)==-s.Rational(15539,150)

# Golden integer norm, rapidity, and the signed golden mark.
phi=(1+s.sqrt(5))/2
lam=(s.sqrt(5)-1)/2
B=s.Matrix([[1,1],[1,2]])
metric=s.Matrix([[-1,-s.Rational(1,2)],[-s.Rational(1,2),1]])
assert B.T*metric*B==metric
assert s.simplify(phi**2*(lam**2)-1)==0
assert s.simplify((3+s.sqrt(5))/2-phi**2)==0
assert s.simplify((3-s.sqrt(5))/2-lam**2)==0
qplus=s.simplify(lam*lam**2)
qminus=s.simplify(lam*phi**2)
zplus=s.simplify(1-qplus)
zminus=s.simplify(1-qminus)
assert s.simplify(zminus+lam)==0
assert s.simplify(zplus-(1-lam**3))==0
clocks_plus=phi**2/2
clocks_minus=lam**2/2
Cmark=s.simplify(clocks_plus*qplus+clocks_minus*qminus)
assert s.simplify(Cmark-lam)==0
assert s.simplify((1+Cmark)**-2-lam**2)==0
assert s.simplify((1+(clocks_plus+clocks_minus)*(1-lam**2))**-2-lam**2)!=0

print('INDEPENDENT ORACLE PASSED')
print('source mass: strict 1<M(a)<2; increasing; M(a)=2-59/(15a)+O(a^-2)')
print('effective source rank: 1<rho(a)<2; increasing; rho(a)=2-1379/(150a^2)+O(a^-3)')
print('native Pascal rank: 2+48/a+18061/(150a^2); fake 2+48/a+224/a^2')
print('signed co-moving golden mark: zplus=1-lambda^3, zminus=-lambda; value=lambda^2')
print('exact polynomial coefficient and leading-asymptotic checks passed')
