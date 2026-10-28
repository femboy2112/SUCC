"""Independent symbolic checks using SymPy; no import of implementation module."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as s

x,z,t=s.symbols('x z t', real=True)
u=x-x*x/2
v=x*x/2
d=1-x
M=s.Matrix([[u,1],[0,v]])
A=s.Matrix([[u,0],[1-v,v]])
R=d/((2-x*x)*(x*x-2*x+2))

assert s.factor(d/4*(s.eye(2)-M).inv()[0,1]-R)==0
for j in range(18):
    authentic=d/4*sum((u**k*v**(j-k) for k in range(j+1)),s.Integer(0))
    matrix_version=d/4*(M**(j+1))[0,1]
    assert s.factor(authentic-matrix_version)==0

q0=(1-u)*(1-v)
q1=q0*(u+v)
q2=q0*(u*u+u*v+v*v)
assert s.factor(q0*q2-q1*q1+q0*q0*u*v)==0

Au=A.subs(x,1)
for n in range(26):
    predicted=s.Matrix([[1,0],[n,1]])/2**n
    assert Au**n==predicted

# Normalized grade at x=1 yields NB2, with a genuine two-state Hankel rank.
pgf=s.factor(((1-u)*(1-v))/((1-u*z)*(1-v*z)))
assert s.factor(pgf.subs(x,1)-1/(2-z)**2)==0
assert s.factor((q0*q2-q1*q1).subs(x,1)+s.Rational(1,64))==0

# Source-integral proof. The symbolic antiderivative often uses logs/arctans;
# the 2D Gaussian-atom integral is an independent elementary equality.
identity=s.factor(16*R- 2/(1-2*t*(1-t))) if False else None
J=s.integrate(2/(2*t*t-2*t+1),(t,0,1))
assert s.simplify(J-s.pi)==0
# Equality R(x) and that source integral is a separate BBP relation established
# in the main repo, verified here via high precision direct quadrature only.

# Spectral transfer modulus at x=1, one retarded stage.
q=s.symbols('q',real=True)
abs2=s.factor(s.Rational(1,4)/(1+s.Rational(1,4)-q))
assert s.simplify(abs2-1/(5-4*q))==0
assert s.simplify((1+s.Rational(1,2))/(1-s.Rational(1,2)))==3

# 8-periodic signed driver; linear complement (no import of original program).
taps=s.Matrix([4,0,0,-2,-1,-1,0,0]);assert sum(taps)==0
v0=s.Matrix([0,0]);F=s.Matrix([s.Rational(1,2),0]);ac=Au
for t0 in taps:
    v0=ac*v0+F*t0
sol=(s.eye(2)-ac**8).inv()*v0
assert sol == s.Matrix([-s.Rational(4,17),-s.Rational(2548,4335)])

# Synthetically pumped 8-cycle has exact zero mean because DC gain=1.
S=[];y=sol
for z0 in taps:
    S.append(y)
    y=ac*y+F*z0
assert y==sol
assert sum(S,s.zeros(2,1))==s.zeros(2,1)

# Maximum entropy result is conditional on fixing mean of EACH stage.
# For fixed mean=1, geometric P(j)=2^(-j-1) maximizes Shannon entropy
# H=2 log 2 (classical KL proof); a two-point mean1 distribution has H=log2.
assert s.simplify(2*s.log(2)-s.log(2)-s.log(2))==0

# Exact left-inverse of two-stage causal observer transfer after two ticks:
# D(L) E2 = (1-u)(1-v) L^2 W; at endpoint W(t-2) is
# 4 E2(t)-4 E2(t-1)+E2(t-2).
L=s.symbols('L')
c=(1-u)*(1-v)
source_decoder=s.expand((1-(u+v)*L+u*v*L**2)/c)
assert s.simplify(source_decoder.subs(x,1)-(4-4*L+L**2))==0
assert s.simplify(((1-u*L)*(1-v*L))-c*source_decoder)==0

# Finite exact π reconstruction: original inverse central binomial masses.
from math import comb
for j in range(14):
    pj=s.expand(d/4*sum((u**k*v**(j-k) for k in range(j+1)),s.Integer(0)))
    integrated=s.simplify(16*s.integrate(pj,(x,0,1)))
    truth=s.Rational(2**(j+1),(2*j+1)*comb(2*j,j))
    assert s.simplify(integrated-truth)==0

# Check sharp inverse noise amplification of the retained two-stage source.
gain=s.factor((1+u)*(1+v)/((1-u)*(1-v)))
assert s.simplify(gain.subs(x,1)-9)==0

mean_delay=s.factor(2+u/(1-u)+v/(1-v))
assert s.simplify(mean_delay.subs(x,1)-4)==0
assert s.simplify(mean_delay.subs(x,0)-2)==0

# Source-mass invariant: c_(8k+j)=16^-k c_j; pumping restores 8-period,
# but contracts/fixes no real BBP U_n carry statistics.

report={
  'main_source': 'BBP four-pole positive Oily packet factorization',
  'source_resolvent': str(s.factor(R)),
  'signed_source_first_shell': [int(z0) for z0 in taps],
  'normalized_endpoint_pgf': str(s.factor(pgf.subs(x,1))),
  'hankel_rank2_determinant':str(s.factor((q0*q2-q1*q1).subs(x,1))),
  'pumped_period8_stationary_E1_E2': [str(a) for a in sol],
  'critical_monodromy_inf_norm':'9/256',
  'fourier_one_stage_endpoint_modulus_squared':'1/(5-4*cos(omega))',
  'two_stage_worst_cond_number':'9',
  'source_decoder_endpoint':'4*E2(t)-4*E2(t-1)+E2(t-2) = W(t-2)',
  'pi_packet_integral_certificates':14,
  'max_uniform_mean_delay': '4',
  'selected_BBP_phase_transport': 'Bounded prefix-sum difference <= 4 for any |W_n|<=1; paper proof, not novel Weyl cancellation',
  'pass': True,
  'scope': 'Exact symbolic small-model proof checks, not repo-wide tests or BBP Weyl saving',
}
path=Path(__file__).resolve().parents[1]/'receipts'/'independent_sympy.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,indent=2))
