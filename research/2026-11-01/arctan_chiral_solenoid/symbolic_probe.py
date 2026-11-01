"""Optional independent symbolic certificates; run with sympy, not a Lean kernel."""
import sympy as sp

x,y=sp.symbols('x y')
A=120*x*x-89*x+16
D=(2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
Aa=120*y*y-89*y+16
Dd=(2*y-1)*(4*y-1)*(8*y-7)*(8*y-3)
H=sp.cancel((A*Dd-Aa*D)/(x-y))
assert sp.denom(H)==1
poly=sp.Poly(sp.expand(H),x,y)
assert all(int(c)%2==0 for c in sp.Poly(sp.expand(H-1),x,y).coeffs()),'isometry numerator must be odd polynomial'
# The derivative congruence 11+4x(x-1) is integer-valued because the residual
# difference is 8*x*(x+1), which is divisible by 16 at all integer/2-adic x.
N=sp.expand(sp.diff(A,x)*D-A*sp.diff(D,x))
P=sp.Poly(sp.expand(N-(11+4*x*(x-1))*D**2-8*x*(x+1)),x)
assert all(int(c)%16==0 for c in P.all_coeffs())
# The base-16 formula is proved by evaluating 16 source residues; rational map
# with odd denominator is 16-Lipschitz on congruence classes.
for n in range(16):
    a=int(A.subs(x,n));d=int(D.subs(x,n));assert d%2
    assert (a*pow(d,-1,16)+n-2*(n%2))%16==0
    dn=int(N.subs(x,n))*pow(d*d,-1,16)%16
    assert dn==(11 if n%4 in(0,1) else 3)
# The Gaussian integer Machin factor is exact and geometrically branch-aware.
assert sp.expand((5+sp.I)**4-2*(1+sp.I)*(239+sp.I))==0
# Möbius inversion J(t)=1/t is an SU(2) 180-degree sphere rotation.
M=sp.Matrix([[0,sp.I],[sp.I,0]])
assert sp.simplify(M.det())==1
assert sp.simplify(M.conjugate().T*M)==sp.eye(2)
# Derivative angular form eta=2dt/(1+t^2) is anti-invariant under J.
assert sp.simplify(2/(1+1/x**2)*(-1/x**2)+2/(1+x**2))==0
print('SYMBOLIC PROBE PASSED: 2-adic source isometry, derivative-16, all residues, Gaussian Machin, SU(2) inversion, angular orientation')
print('ISOMETRY BI-ARITHMETIC H(x,y) MOD 2: 1')
print('DERIVATIVE RESIDUES MOD 16: 11,11,3,3')
# Source-specific Mellin completion is a RELATIVE ANGULAR period, not a generic
# sphere rotation. All four original forcing poles enter P(t).
t=sp.symbols('t', real=True)
P=4-2*t**3-t**4-t**5
F=sp.cancel(P/(16-t**8))
reduced=(1-t)/((2-t*t)*(t*t-2*t+2))
assert sp.simplify(F-reduced)==0
angle=sp.Rational(1,4)/(1+(t-1)**2)
Gprime=sp.Rational(1,8)*(-2*t/(2-t*t)-(2*t-2)/(t*t-2*t+2))
assert sp.simplify(reduced-angle-Gprime)==0
Gargument=(2-t*t)/(t*t-2*t+2)
assert Gargument.subs(t,0)==1 and Gargument.subs(t,1)==1
assert sp.simplify(sp.integrate(reduced,(t,0,1))-sp.pi/16)==0
# Four original source-time poles and the completed Mellin integral's four
# different t-plane poles have DISTINCT Möbius invariant j-values.
def crossratio(p):
 return sp.simplify((p[0]-p[2])*(p[1]-p[3])/((p[0]-p[3])*(p[1]-p[2])))
def jcurve(v):return sp.factor(256*(1-v+v*v)**3/(v*v*(1-v)**2))
original_poles=(sp.Rational(7,8),sp.Rational(1,2),sp.Rational(3,8),sp.Rational(1,4))
completed_poles=(sp.sqrt(2),-sp.sqrt(2),1+sp.I,1-sp.I)
lambda_original=crossratio(original_poles)
lambda_completed=crossratio(completed_poles)
assert lambda_original==sp.Rational(8,5)
assert lambda_completed==-1
assert jcurve(lambda_original)==sp.Rational(470596,225)
assert jcurve(lambda_completed)==1728
assert jcurve(lambda_original)!=jcurve(lambda_completed)
print('SOURCE-ANGLE RELATIVE COHOMOLOGY PASSED: complete BBP integrand = angular eighth + exact endpoint-zero log')
print('FOUR-PUNCTURE CROSS-RATIO OBSTRUCTION: lambda_source=8/5, j_source=470596/225; lambda_completed=-1, j_completed=1728')
