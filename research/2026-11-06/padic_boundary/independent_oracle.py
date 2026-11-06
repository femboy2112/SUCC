"""Different implementation: SymPy polynomial/partial fraction verification."""
import sympy as sp
x,z,y=sp.symbols('x z y')
A=120*z*z-89*z+16
D=(2*z-1)*(4*z-1)*(8*z-7)*(8*z-3)
assert sp.cancel(4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)-A/D)==0
P=-4*x**6+2*x**3+x*x+x
Q=1-2*x+2*x*x
G=sp.cancel(P/(1-16*x**8))
assert sp.cancel(G-x/(2*Q)-x/(2*(1-2*x*x)))==0
assert sp.factor(1-16*x**8) == -(2*x*x-1)*(2*x*x+1)*(4*x**4+1) or sp.cancel((1-16*x**8)-(1-2*x*x)*(1+2*x*x)*(1+4*x**4))==0
I=sp.I
a=1+I;b=1-I
assert sp.expand((1-a*x)*(1-b*x)-Q)==0
# Derivative of the formal 2-adic logarithmic primitive, no analytic branch assumptions.
L=sp.log(1-a*x)/8 + sp.log(1-b*x)/8 +(sp.log(1-b*x)-sp.log(1-a*x))/(8*I)-sp.log(1-2*x*x)/8
assert sp.simplify(sp.diff(L,x)-G)==0
assert sp.simplify((1-a)+I)==0 and sp.simplify((1-b)-I)==0
assert (-I)**4==1 and I**4==1 and (-1)**2==1
# Odd-denominator divided difference of r is an odd 2-adic unit:
N=sp.cancel((A*D.subs(z,y)-A.subs(z,y)*D)/(z-y))
assert sp.denom(N)==1
Npoly=sp.Poly(sp.expand(N),z,y)
assert {m: int(c)%2 for m,c in Npoly.terms() if int(c)%2} == {(0,0): 1}
# Mod 2 certificate polynomial: D(z)==1, A(z)==z, D divided diff even, A divided diff odd.
assert all(int(c)%2==0 for m,c in sp.Poly(sp.cancel((D-D.subs(z,y))/(z-y)),z,y).terms())
assert sp.Poly(sp.cancel((A-A.subs(z,y))/(z-y)),z,y).eval({z:0,y:0})%2==1
print('SYMPY_ORACLE_PASS: four-pole compactification; exact formal primitive; Q2(i) torsion endpoints; odd derivative quotient')
