"""Independent SymPy symbolic oracle for the rational polynomial echo and M=4 rational quadrature.

Separate implementation from causal_echo_probe.py; supports finite exact controls
only. No normality or asymptotic verification.
"""
import sympy as s
from fractions import Fraction as F
x=s.symbols('x'); a=s.Rational(1,4); b=s.Rational(1,2)

def R(n):
 t=s.Integer(8*n-7)
 return 4/t-2/(t+3)-1/(t+4)-1/(t+5)

for M in (1,2,3,4,5,6):
 g=s.expand((x-a)**(M+1)*(b-x)**(M+1)); psi=s.diff(g,x,M)
 for n in range(1,M+1):
  assert s.integrate(x**(n-1)*psi,(x,a,b))==0,(M,n)
 assert s.integrate(x**M*psi,(x,a,b))!=0

M=4; g=s.expand((x-a)**5*(b-x)**5); psi=s.diff(g,x,4)
B=sum(abs(v) for v in s.Poly(psi,x).all_coeffs()); eps=s.Rational(1,1000)/B
def delta_r(n):return eps*s.integrate(x**(n-1)*psi,(x,a,b))

u=s.Rational(0)
v=s.Rational(0)
for n in range(1,19):
 u=16*u+R(n)
 v=16*v+R(n)+delta_r(n)
 if n<=M:assert u==v
 if n==18:
  d=(v-u)%1; norm=min(d,1-d)
  print('M4 N18 exact circle distance',str(norm),float(norm))
  assert s.Rational(1,4)<norm<s.Rational(2,5)

nodes=[s.Rational(1,80),s.Rational(5,16),s.Rational(1,2),s.Rational(63,80)]
mat=s.Matrix([[node**j for node in nodes] for j in range(4)])
weights=mat.inv()*s.Matrix([R(j+1) for j in range(4)])
assert all(w>0 for w in weights)
q=sum((w/(16-node) for w,node in zip(weights,nodes)),s.Rational(0))
assert q==s.Rational(4062342947075618,20689342837729335)
print('M4 positive rational quadrature',[(str(v),str(w)) for v,w in zip(nodes,weights)])
print('SYMPY_INDEPENDENT_EXACT_PASS')
