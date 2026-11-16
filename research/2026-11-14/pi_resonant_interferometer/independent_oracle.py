"""Independent raw/symbolic oracle: no import of the primary detector module."""
from __future__ import annotations
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

m,z=sp.symbols('m z',integer=True)
r=sp.Rational(4,1)/(8*m-7)-sp.Rational(2,1)/(8*m-4)-1/(8*m-3)-1/(8*m-2)
D=(2*m-1)*(4*m-1)*(8*m-7)*(8*m-3)
assert sp.factor(r - (120*m*m-89*m+16)/D)==0
rlead=sp.Rational(15,64)/m**2
low=sp.factor(r-rlead)
up=sp.factor(1/m**3-low)
for expr in (low,up):
    num,den=sp.fraction(expr)
    assert all(k>0 for k in sp.Poly(sp.expand(num.subs(m,z+2)),z).all_coeffs())
    assert sp.factor(den.subs(m,z+2)).subs(z,0)>0

# Rederive the innovation from the rational function directly, not the source recurrence.
def coeff(n):
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
checked=0
for n in range(2,84):
    for ell in range(1,13):
        inn=sum((16**(ell-j)*coeff(n+j) for j in range(1,ell+1)),Q(0))
        lead=Q(16**ell-1,64*n*n)
        assert abs(inn-lead)<=Q(16**ell,10*n**3)
        checked+=1

# Direct phase source evaluation from explicit rational closed-form weights.
def U(n):
    return sum((16**(n-j)*coeff(j) for j in range(1,n+1)),Q(0))
mp.mp.dps=85
pair_cases=0
for n0 in range(1,8):
    phase=[]
    for j in range(n0,n0+6):
        q=U(j)%1
        phase.append(mp.exp(2j*mp.pi*mp.mpf(q.numerator)/q.denominator))
    w=sum(phase)/6
    p=sum((a*mp.conj(b) for a in phase for b in phase))/36
    assert abs(p-abs(w)**2)<mp.mpf('1e-76')
    pair_cases+=1

# Gamma phase after one-sided rotational averaging is not a genuine source click.
gamma=mp.quad(lambda t: t*mp.exp(-t)*mp.exp(-1j*t),[0,1,4,12,mp.inf])
assert abs(gamma+1j/2)<mp.mpf('1e-65')
assert abs((1-mp.re(gamma))/2-mp.mpf('0.5'))<mp.mpf('1e-65')

# Periodic nonnormal source x=1/15: finite positive R0-click probability
# does not establish full normality; pair collision is fully locked.
q=mp.mpf(1)/15
click=mp.sin(mp.pi*q)**2
assert 0<click<1
assert all(pow(16,n,15)==1 for n in range(50))

summary={
 'independent_rational_innovation_comparisons':checked,
 'independent_pair_energy_checks':pair_cases,
 'sympy_lower_polynomial':str(sp.Poly(sp.expand(sp.fraction(low)[0].subs(m,z+2)),z).as_expr()),
 'sympy_upper_polynomial':str(sp.Poly(sp.expand(sp.fraction(up)[0].subs(m,z+2)),z).as_expr()),
 'gamma_depth2_phase_factor':'-i/2',
 'periodic_rational_false_positive':'1/15 yields positive clicks, no normality',
 'conclusion':'PASS; model/sample checks only; pi normality open',
}
print('INDEPENDENT_ORACLE_PASS',json.dumps(summary,sort_keys=True))
Path(__file__).with_name('receipts').mkdir(exist_ok=True)
Path(__file__).with_name('receipts').joinpath('independent_summary.json').write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
