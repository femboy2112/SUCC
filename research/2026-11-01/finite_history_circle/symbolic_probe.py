"""Optional SymPy independent symbolic check (not a new Lean proof)."""
from __future__ import annotations
from sympy import symbols, Poly, factor, simplify, prod

x=symbols('x')
A=120*x**2-89*x+16
D=(2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
P=2560*x**2+27261099545*x-10222908432
Q=9*(12923803584*x**3-21109033272*x**2+10286815366*x-1497394413)
assert factor(P*D-A*Q)==1310720*prod(x-j for j in range(1,7))
assert simplify(A/D-(4/(8*x-7)-2/(8*x-4)-1/(8*x-3)-1/(8*x-2)))==0
assert Poly(P,x).degree()==2 and Poly(Q,x).degree()==3
assert Poly(D,x).degree()==4
assert all(Poly(P*D-A*Q,x).eval(j)==0 for j in range(1,7))
assert Poly(P*D-A*Q,x).eval(7)!=0
print('Sympy 6 independent source, mutant, bidegree checks PASS')
