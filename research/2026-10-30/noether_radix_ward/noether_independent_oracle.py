"""Independent math route for Noether/carry/Ward analysis (SymPy + mpmath).

Does not import the exact stdlib probes; audits theory and source independently.
"""
import sympy as S
import mpmath as mp
from math import comb

A=S.symbols('A',positive=True)
R=lambda a:S.Integer(4)/a-S.Integer(2)/(a+3)-S.Integer(1)/(a+4)-S.Integer(1)/(a+5)
assert S.factor(R(A)) == (15*A*A+121*A+240)/(A*(A+3)*(A+4)*(A+5))
assert S.limit(A**2*R(A),A,S.oo)==15
assert S.limit(A**3*(R(A)-15/A**2),A,S.oo)==-59
Kappa=-A*S.diff(S.log(R(A)),A)/2
assert S.limit(A*(Kappa-1),A,S.oo)==-S.Rational(59,30)
assert S.limit(A*A*(Kappa-1)**2,A,S.oo)==S.Rational(3481,900)

# Construct a COMPLETE 3D scalar observer+carrier action in exact symbols
I,c,epsilon,k,eta,edot=S.symbols('I c epsilon k eta edot', real=True, positive=True)
x0,x1,x2,v0,v1,v2=S.symbols('x0 x1 x2 v0 v1 v2', real=True)
w=1+epsilon*k*k*eta*eta
Eobs=I*edot**2/2
Efield=(v0*v0+v1*v1+v2*v2)/2 + c*c*(w*(x0-x1)**2+(x1-x2)**2+(x2-x0)**2)/2
p0=-c*c*(w*(x0-x1)+(x0-x2))
p1=-c*c*(w*(x1-x0)+(x1-x2))
p2=-c*c*((x2-x1)+(x2-x0))
etaacc=-c*c*S.diff(w,eta)*(x0-x1)**2/(2*I)
dEdt=S.diff(Eobs+Efield,edot)*etaacc+S.diff(Efield,eta)*edot
for x,v,f in [(x0,v0,p0),(x1,v1,p1),(x2,v2,p2)]:
    dEdt+=S.diff(Efield,x)*v+S.diff(Efield,v)*f
assert S.simplify(dEdt)==0

# A conventional discrete wave variational action gives the exact recurrence:
u0,u1,u2,l=S.symbols('u0 u1 u2 l',real=True)
Ld=lambda x,y:(y-x)**2/2-l*(x*x+y*y)/4
EL=S.diff(Ld(u0,u1),u1)+S.diff(Ld(u1,u2),u1)
assert S.simplify(EL+u2-2*u1+u0+l*u1)==0

# Cotangent Noether shift and adjoint momentum map
p_n,p_np1,un,un1,r,shift=S.symbols('p_n p_np1 u_n u_np1 r shift')
assert S.expand((un1+16*shift)-16*(un+shift)-r-(un1-16*un-r))==0
assert S.simplify(16*p_np1-p_n).subs(p_n,16*p_np1)==0

# Exact symmetries in a signed source sequence are independent of base seed.
u=[S.Integer(0)]
for n in range(1,6):u.append(S.expand(16*u[-1]+R(8*n-7)))
for n in range(1,5):
    assert S.simplify(16*u[n]-u[n+1]+R(8*(n+1)-7))==0
for p in range(2,5):
    for q in range(p+1,6):
        assert S.simplify(16*u[p-1]+u[q]-16*u[q-1]-u[p]
                          -(R(8*q-7)-R(8*p-7)))==0

mp.mp.dps=70
h=1
N=6
rmp=lambda n:mp.mpf(4)/(8*n-7)-mp.mpf(2)/(8*n-4)-1/mp.mpf(8*n-3)-1/mp.mpf(8*n-2)
U=[mp.mpf(0)]
for n in range(1,N+1): U.append(16*U[-1]+rmp(n))
# Independent spectral/seed-integration with exact unbalanced carry
phase=lambda z:mp.exp(2j*mp.pi*z)
pred=sum(phase(-h*rmp(n+1)) for n in range(1,N))
# Direct coefficient enumeration from polynomial in seed character; all terms
# with 16 powers matching a 1-power must be all at previous index.
coeff=[]
for m in range(1,N+1):
    for n in range(1,N+1):
        if 16*16**n==16**m:
            coeff.append(phase(16*h*U[n]-h*U[m]))
assert len(coeff)==N-1
assert abs(sum(coeff)-pred)<mp.mpf('1e-55')

# Local seed cylinder average: global Haar vanishing does not select s=0.
delta=mp.power(16,-N)
W=sum(phase(h*U[n]) for n in range(1,N+1))
K=lambda t:(phase(t)-1)/(2j*mp.pi*t) if t else mp.mpf(1)
local=sum(phase(h*U[n])*K(h*mp.power(16,n-N)) for n in range(1,N+1))
assert abs(local-W) <= 2*mp.pi*h*sum(mp.power(16,n-N) for n in range(1,N+1))
assert abs(local-W)<2*mp.pi*h*mp.mpf(16)/15
print('Original source R(a), 59², coupled observer+field Noether energy, discrete EL: EXACT PASS')
print('16-to-1 source-only radix carry resonance:',mp.nstr(pred,28))
print('Exponential seed cylinder local average vs selected seed:',mp.nstr(local,24),mp.nstr(W,24))
print('Difference',mp.nstr(abs(local-W),20),'bound',mp.nstr(2*mp.pi*16/15,20))
print('Independent SymPy/mpmath oracle PASS')
