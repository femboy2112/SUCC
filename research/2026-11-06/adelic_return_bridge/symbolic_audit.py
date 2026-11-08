"""Optional independent SymPy algebra check of inherited #527 2-adic log derivation.
This is polynomial/rational algebra only: it does not verify p-adic logarithmic analysis.
"""
import sympy as sp
x=sp.symbols('x'); I=sp.I
original=(-4*x**6+2*x**3+x**2+x)/(1-16*x**8)
pair=x/(2*(1-2*x+2*x*x))+x/(2*(1-2*x*x))
assert sp.cancel(original-pair)==0
p=(sp.log(1-(1+I)*x)+sp.log(1-(1-I)*x))/8
p+=(sp.log(1-(1-I)*x)-sp.log(1-(1+I)*x))/(8*I)
p-=sp.log(1-2*x*x)/8
assert sp.simplify(sp.diff(p,x)-pair)==0
z=sp.symbols('z')
A=120*z*z-89*z+16
D=(2*z-1)*(4*z-1)*(8*z-7)*(8*z-3)
assert sp.Poly(A,z,modulus=2)==sp.Poly(z,z,modulus=2)
assert sp.Poly(D,z,modulus=2)==sp.Poly(1,z,modulus=2)
print('SYMPY_RATIONAL_DB6_EXACT_PASS')
print('SYMPY_DB7_LOG_FORMAL_DERIVATIVE_PASS')
print('SOURCE_A_MOD2_Z_D_MOD2_ONE_PASS')
print('NOTE: symbolic identities are NOT a formal certification of the 2-adic log torsion argument')
