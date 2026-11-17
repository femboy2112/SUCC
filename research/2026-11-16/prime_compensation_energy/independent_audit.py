"""Independent SymPy oracle; does not import prime_compensation or its tests.

Reports exact algebraic checks separately from complex floating-point diagnostics.
No infinite analytic assertion is inferred from finite execution.
"""
import cmath
from math import gcd, isqrt, prod, log, pi
from fractions import Fraction
from itertools import permutations
import sympy as S

num_exact=0
num_numeric=0

def ck(expr):
    global num_exact
    if not bool(expr):
        raise AssertionError(expr)
    num_exact+=1

def near(z,w,eps=2e-11):
    global num_numeric
    if abs(z-w)>=eps:raise AssertionError((z,w,abs(z-w)))
    num_numeric+=1

z,p=S.symbols('z p')
chi=1-z
T=S.diag(1/chi,chi)
J=S.Matrix([[0,S.Rational(1,2)],[S.Rational(1,2),0]])
ck(S.simplify(T.T*J*T-J)==S.zeros(2))
M=S.factor((1/chi-1)*(chi-1))
L=S.factor((1/chi-1)+(chi-1))
ck(S.simplify(M+L)==0)
ck(S.simplify(M+z**2/(1-z))==0)
ck(S.simplify(M.subs(z,p)-p**2/(p-1))==0)
ck(S.simplify(M.subs(z,p**(-2))+1/(p**2*(p**2-1)))==0)

C=S.Matrix([[S.Rational(1,2),S.Rational(1,2)],[S.Rational(1,2),-S.Rational(1,2)]])
Cinv=S.Matrix([[1,1],[1,-1]])
LJ=Cinv.T*J*Cinv
ck(LJ==S.diag(1,-1))

def boost(t):
    return S.Matrix([[S.cosh(t),-S.sinh(t)],[-S.sinh(t),S.cosh(t)]])

for pp in [2,3,5,7,11,13,17,19,23,29,31]:
    a=S.Integer(pp-1)
    actual=S.simplify(C*T.subs(z,pp)*Cinv)
    expected=-boost(S.log(a))
    ck(all(S.simplify(actual[i,j]-expected[i,j])==0 for i in range(2) for j in range(2)))
    ck(S.simplify(M.subs(z,pp)-4*S.cosh(S.log(a)/2)**2)==0)
    ck(S.simplify(actual.T*LJ*actual-LJ)==S.zeros(2))

for ps in [(),(2,),(2,3),(2,3,5),(2,3,5,7),(2,3,5,7,11)]:
    Q=prod(ps)
    bsum=sum((S.bernoulli(2,S.Rational(a,Q)) for a in range(1,Q+1) if gcd(a,Q)==1),S.Integer(0))
    residue=-S.Rational(Q,2)*bsum
    expected=-S.Rational(1,12)*prod((1-pp for pp in ps))
    ck(S.simplify(residue-expected)==0)
    E=prod((S.Rational(1,1-pp) for pp in ps), start=S.Integer(1))
    ck(S.simplify(E*residue+S.Rational(1,12))==0)

for ps in permutations([2,3,5]):
    e=S.Rational(1);r=-S.Rational(1,12)
    de=S.Integer(0);dr=S.Symbol('Zprime')
    for pp in ps:
        c=S.Integer(1-pp); cp=pp*S.Symbol(f'log{pp}')
        olde,oldr=e,r
        de,dr=de/c-olde*cp/c**2,dr*c+oldr*cp
        e,r=olde/c,oldr*c
        ck(S.expand(e*r+S.Rational(1,12))==0)
        ck(S.expand(de*r+e*dr-S.Symbol('Zprime'))==0)
    ck(S.simplify(e+S.Rational(1,8))==0)

# Source-authenticated BBP rational forcing from the four-pole Gamma quotient.
t=S.symbols('t',positive=True)
ratio=(t+S.Rational(1,8))**4/((t+S.Rational(1,2))**2*(t+S.Rational(5,8))*(t+S.Rational(3,4)))
r_from_gamma=S.diff(S.log(ratio),t)/8
n=S.symbols('n',integer=True,positive=True)
original=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
ck(S.simplify(r_from_gamma.subs(t,n-1)-original)==0)
for k in range(1,33):
    ck(S.simplify(r_from_gamma.subs(t,k-1)-original.subs(n,k))==0)

# Genuine Fourier projector vs source-divisor nerve, with sampled complex phases.
Q=30
for n in range(1,61):
    a=1.0 if gcd(n,Q)==1 else 0.0
    ram=lambda h: sum(cmath.exp(2j*pi*h*j/Q) for j in range(Q) if gcd(j,Q)==1)
    b=sum(ram(h)*cmath.exp(-2j*pi*h*n/Q) for h in range(Q))/Q
    near(b,a,3e-12)

# Finite reflection defect is unitary on the critical line, but not RH.
for t in [0.0,.1,.3,1.0,3.0]:
    s=.5+1j*t
    for pp in [2,3,5,7]:
        a=1-pp**(-s)
        b=1-pp**(-(1-s))
        near(abs(a/b),1,2e-14)

# Analytic derivative of phase anchored at t=0 through finite difference.
for pp in [2,3,5,7,11]:
    dt=1e-6
    f=lambda t:(1-pp**(-(.5+1j*t)))/(1-pp**(-(.5-1j*t)))
    theta=(cmath.phase(f(dt))-cmath.phase(f(-dt)))/(2*dt)
    near(theta,2*log(pp)/(pp**.5-1),2e-8)

# PCE-11 independent signed-boost and coarse-compression calibration.
K=S.Matrix([[0,-1],[-1,0]])
eta=S.diag(1,-1)
P=S.Matrix([[1,0]])
J0=S.Matrix([[1],[0]])
ck(K**2==S.eye(2))
ck(P*J0==S.eye(1))
t=S.symbols('tau',real=True)
Bt=S.Matrix([[S.cosh(t),-S.sinh(t)],[-S.sinh(t),S.cosh(t)]])
ck(S.simplify(Bt.diff(t)-K*Bt)==S.zeros(2))
ck(S.simplify(Bt.subs(t,-t)*Bt-S.eye(2))==S.zeros(2))
ck(S.simplify(Bt.T*eta*Bt-eta)==S.zeros(2))
for pp,qq in [(2,3),(3,5),(3,7),(5,11),(7,13)]:
    a,b=S.Rational(pp-1),S.Rational(qq-1)
    cp,sp=(a+1/a)/2,(a-1/a)/2
    cq,sq=(b+1/b)/2,(b-1/b)/2
    Tp=S.Matrix([[-cp,sp],[sp,-cp]])
    Tq=S.Matrix([[-cq,sq],[sq,-cq]])
    ck(Tp.T*eta*Tp==eta)
    ck(Tp*Tq==Tq*Tp)
    ck(P*Tq*Tp*J0-S.Matrix([[cp*cq+sp*sq]])==S.zeros(1))
    ck(P*Tq*J0*P*Tp*J0-S.Matrix([[cp*cq]])==S.zeros(1))
    gap=P*Tq*(S.eye(2)-J0*P)*Tp*J0
    ck(gap==S.Matrix([[sp*sq]]))
    ck(gap==P*Tq*Tp*J0-P*Tq*J0*P*Tp*J0)
a=S.Rational(3-1); b=S.Rational(5-1)
ck((a-1/a)*(b-1/b)/4==S.Rational(45,32))
print(f'INDEPENDENT AUDIT OK: {num_exact} exact symbolic/coprime/jet checks, {num_numeric} Fourier/phase numerical checks')
print('No RH/π normality inference; independent arithmetic source and scalar completion are separate.')
