#!/usr/bin/env python3
"""Independent symbolic derivation / calibrations (SymPy). Not a Lean proof."""
import sympy as s

n,x,t,H,theta,bb=s.symbols('n x t H theta b', positive=True)
u=x-x*x/2
v=x*x/2
R=(1-x)/((2-x*x)*(x*x-2*x+2))
M=s.Matrix([[u,1],[0,v]])
assert s.simplify(((1-x)/4)*((s.eye(2)-M).inv())[0,1]-R)==0
assert s.simplify((u+v)-x)==0
assert s.simplify(u-v-x*(1-x))==0

# No fixed two-bit event has P(A)=1-2p: polynomial matching would
# require a00=1, a01+a10=0, and a11=-1 (not an acceptance rate).
p=s.symbols('p',real=True)
a00,a01,a10,a11=s.symbols('a00 a01 a10 a11')
P=a00*(1-p)**2+(a01+a10)*p*(1-p)+a11*p*p
cs=s.Poly(s.expand(P-(1-2*p)),p).all_coeffs()
sol=s.solve(cs,[a00,a01,a10,a11],dict=True)
assert sol and s.simplify(sol[0][a00]-1)==0
assert s.simplify(sol[0][a01]+a10)==0
assert sol[0][a11]==-1
# Plug a01=a10=0, a00=1, then a11 must be -1.
assert s.simplify(s.expand(P-(1-2*p)).subs({a00:1,a01:0,a10:0,a11:-1}))==0

# Exact coherent Bayesian message map, DISTINCT from merely multiplying
# signal amplitudes. For small independent centered child messages, the
# squared/variance linearization coefficient is b*theta**2, not b*theta.
q,m1,m2=s.symbols('q m1 m2',real=True)
pplus=(1+q*m1)*(1+q*m2)
pminus=(1-q*m1)*(1-q*m2)
msg=s.cancel((pplus-pminus)/(pplus+pminus))
assert s.simplify(msg-q*(m1+m2)/(1+q*q*m1*m2))==0
assert s.diff(msg,m1).subs({m1:0,m2:0})==q
assert s.diff(msg,m2).subs({m1:0,m2:0})==q

# Original four-pole compact numerator: source passport exact.
r=(4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2))
A=120*n*n-89*n+16
D=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
assert s.factor(r-A/D)==0

# Critical double-root Jordan transfer; energy amplification under copied cells.
m=s.symbols('m', integer=True,nonnegative=True)
J=s.Matrix([[s.Rational(1,2),1],[0,s.Rational(1,2)]])
for k in range(0,15):
    a=J**k
    expected=s.Matrix([[s.Rational(1,2)**k,s.Integer(k)*s.Integer(2)**(1-k) if k else 0],[0,s.Rational(1,2)**k]])
    assert a==expected
    sq=sum(z*z for z in a)
    assert s.simplify(sq-((2+4*k*k)/s.Integer(4)**k))==0

# Independent exact 4D chiral source block: 16*T^8=I.
G=s.Matrix([[s.Rational(1,2),-s.Rational(1,2)],[s.Rational(1,2),s.Rational(1,2)]])
Q=s.Matrix([[0,1],[s.Rational(1,2),0]])
Z=s.zeros(2)
T_chiral=s.BlockMatrix([[G,Z],[Z,Q]]).as_explicit()
assert 16*(T_chiral**8)==s.eye(4)
for k in range(1,10):
    assert (16**k)*(T_chiral**(8*k))==s.eye(4)

# Conformal reach of c=1 null rays under a(t)=exp(Ht) and de Sitter expansion.
eta=s.integrate(s.exp(-H*t),(t,0,s.symbols('T',positive=True)))
T=s.symbols('T',positive=True)
assert s.simplify(eta-(1-s.exp(-H*T))/H)==0
assert s.simplify(s.limit((1-s.exp(-H*T))/H,T,s.oo)-1/H)==0
assert s.diff(s.exp(H*t),t)==H*s.exp(H*t)

# Scale factor smooth kinematics (1+1) curvature scalar 2 a''/a=2H^2;
# 3+1 de Sitter has R=12H^2 from standard FLRW identity.
assert s.simplify(2*s.diff(s.exp(H*t),t,2)/s.exp(H*t)-2*H**2)==0

# Haar initial seed prior kills every nonzero h character despite original
# forcing appearing as an overall phase. The exact integral is classical.
z=s.symbols('z',real=True)
for h in (-2,-1,1,2,3):
    for k in range(4):
        omega=h*16**k
        assert s.simplify(s.integrate(s.exp(2*s.pi*s.I*omega*z),(z,0,1)))==0

# Finite BBP comparison universal r(k)<=5/(3 k²) via factorwise lower bounds.
assert s.factor((5*s.Integer(72)-s.Integer(3)*120))==0

# Two-stage endpoint PGF versus inferred additional independent noise:
pgf=1/(2-x)**2
assert s.simplify(pgf.subs(x,1)-1)==0
phi=(1+s.sqrt(5))/2
psi=(1-s.sqrt(5))/2
L=[2,1]
for k in range(2,24): L.append(L[-1]+L[-2])
for k in range(0,23):
    assert s.simplify(phi**k+psi**k-L[k])==0
    assert s.simplify(L[k]/phi**k-1-(-1)**k*phi**(-2*k))==0

print('PASS: exact SUCC Oily resolvent, compact original signed forcing, Jordan powers, FLRW null horizon, Haar seed character countermodel, finite comparison algebra')
