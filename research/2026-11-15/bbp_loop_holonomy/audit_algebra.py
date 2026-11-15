"""Independent symbolic audit: original forcing return-jet congruence in Z_2.

Uses SymPy as an optional, separate algebra implementation. The main probe
and its standard-library tests do not import this module.
"""
from sympy import symbols, expand, Poly, factor, diff
from sympy import Rational

t,u=symbols('t u')
P=120*t*t-89*t+16
D=(2*t-1)*(4*t-1)*(8*t-7)*(8*t-3)
L=expand(diff(P,t)*D-P*diff(D,t))
print('numerator P:',P)
print('denominator D:',expand(D))
print('d/dt r(t) numerator:',factor(L))
print('for each residue t=4u+j the polynomial L-cD² has all coefficients divisible by 16')
for j in range(4):
    c=11 if j in (0,1) else 3
    poly=Poly(expand((L-c*D*D).subs(t,4*u+j)),u)
    residues=[int(v)%16 for v in poly.all_coeffs()]
    assert set(residues)=={0},(j,c,residues)
    print('residue class',j,'r\' mod16',c,'polynomial degree',poly.degree(),'mod16 coefficients',residues)
# Cross-check the original four-pole weights are EXACTLY P/D.
original=Rational(4)/(8*t-7)-Rational(2)/(8*t-4)-1/(8*t-3)-1/(8*t-2)
assert factor(original-P/D)==0
print('SOURCE algebra and four modular polynomial certificates PASS')
