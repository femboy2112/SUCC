"""Independent symbolic and high-precision checks; no production helper imports."""
from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction
import mpmath as mp
import sympy as sp

mp.mp.dps=75
z=sp.symbols('z')
Q=4-2*z**3-z**4-z**5
assert sp.simplify(Q-(1-z)*(z*z+2)*(z*z+2*z+2))==0
checks=0
for j in range(20):
    val=sp.integrate(Q*z**(8*j),(z,0,1))
    expect=4/sp.Integer(8*j+1)-2/sp.Integer(8*j+4)-1/sp.Integer(8*j+5)-1/sp.Integer(8*j+6)
    assert val==sp.cancel(expect)
    checks+=1
for n in range(1,15):
    numerator=(16**n-z**(8*n))*Q
    poly=sp.cancel(numerator/(16-z**8))
    direct=sum(16**(n-1-j)*z**(8*j)*Q for j in range(n))
    assert sp.simplify(poly-direct)==0
    checks+=1

# Original four-pole source and green tail written independently.
def f(n):
    return 4/sp.Integer(8*n-7)-2/sp.Integer(8*n-4)-1/sp.Integer(8*n-3)-1/sp.Integer(8*n-2)

def rf(t):
    return (4-2*t**3-t**4-t**5)/(16-t**8)

def tail(n):
    return mp.quad(lambda t: rf(t)*t**(8*n),[0,mp.mpf('0.6'),mp.mpf('0.92'),mp.mpf('0.99'),1])

def sq(n):
    return mp.quad(lambda t: rf(t)**2*t**(16*n),[0,mp.mpf('0.6'),mp.mpf('0.92'),mp.mpf('0.99'),1])

def dd(n,q,lag):
    return mp.quad(lambda t:rf(t)*t**(8*n)*(1-t**(8*q))*(1-t**(8*lag)),
                    [0,mp.mpf('0.6'),mp.mpf('0.92'),mp.mpf('0.99'),1])

def dd_sq(n,q,lag):
    return mp.quad(lambda t:rf(t)**2*t**(16*n)*(1-t**(8*q))**2*(1-t**(8*lag))**2,
                   [0,mp.mpf('0.6'),mp.mpf('0.92'),mp.mpf('0.99'),1])

x=tail(0)
assert abs(x-mp.pi/16)<mp.mpf('1e-68')
checks+=1

source_data=[]
for n in (1,2,4,8,16,32,64):
    mu=tail(n)
    k_ber=tail(2*n)
    k_rb=sq(n)
    assert k_ber>k_rb>0
    assert abs(mu-sum((mp.mpf(int(sp.numer(f(n+j))))/int(sp.denom(f(n+j))))/(16**j) for j in range(1,21))) < mp.mpf('0.000000000000000001')
    source_data.append({'n':n,'T_n':mp.nstr(mu,22),'bernoulli_EY_n2':mp.nstr(k_ber,22),
                        'rb_EY_n2':mp.nstr(k_rb,22), 'rb_over_bernoulli':mp.nstr(k_rb/k_ber,12)})
    checks+=3

phase_data=[]
for n in (2,4,8,16):
    prefix=sum((16**(n-j)*f(j) for j in range(1,n+1)),sp.Rational(0))
    prefix_mp=mp.mpf(int(sp.numer(prefix)))/int(sp.denom(prefix))
    X=prefix_mp+tail(n)
    direct=16**n*x
    assert abs(X-direct)<mp.mpf('1e-52')
    h=3;c=2*mp.pi*h
    phase=mp.e**(1j*c*X)
    factor=mp.e**(1j*c*prefix_mp)*mp.e**(1j*c*tail(n))
    assert abs(phase-factor)<mp.mpf('1e-55')
    phase_data.append({'n':n,'h':h,'phase_re':mp.nstr(mp.re(phase),16),'phase_im':mp.nstr(mp.im(phase),16)})
    checks+=2

four_data=[]
for n,q,lag in [(1,16,2),(8,16,2),(16,16,2),(32,16,2),(32,256,2)]:
    target=dd(n,q,lag)
    diff=tail(n+q+lag)-tail(n+q)-tail(n+lag)+tail(n)
    assert target>0
    assert abs(diff-target)<mp.mpf('1e-65')
    upper_indep_q=16*lag * (2/mp.fprod([8*n+j for j in range(1,4)]))
    upper_fixed_q=64*q*lag * (6/mp.fprod([8*n+j for j in range(1,5)]))
    assert target<upper_indep_q and target<upper_fixed_q
    k_sq=dd_sq(n,q,lag)
    assert k_sq>0
    four_data.append({'n':n,'q':q,'lag':lag,'signed_green_double_difference':mp.nstr(target,22),
                      'rb_squared_mark':mp.nstr(k_sq,22),'uniform_q_bound':mp.nstr(upper_indep_q,16)})
    checks+=4

# Critical noncommutation: the BBP coin C is integer-valued so exp(2pi i h16^n C)=1 a.s.
# But exp(2pi i h16^n E C) is not 1 for any n and h!=0 by pi irrationality.
assert abs(mp.e**(2j*mp.pi*x)-1)>mp.mpf('1')
checks+=1

# Source-gauge independent telescoping: first 12 exact rational checkpoints.
for n in range(1,13):
    corr=sum((sp.Rational(2*j*j-16*2*(j-1)**2,16**j) for j in range(1,n+1)),sp.Rational(0))
    assert corr==sp.Rational(2*n*n,16**n)
    checks+=1

# Independent rational-function check of the complete Oily frequency law.
h=sp.symbols('h', integer=True, positive=True)
zeta=sp.symbols('zeta')
qfun=(4/(2-zeta)**2-1)/3
assert sp.simplify(qfun.subs(zeta,1)-1)==0
assert sp.simplify(sp.diff(qfun,zeta).subs(zeta,1)-sp.Rational(8,3))==0
assert sp.simplify((sp.diff(qfun,zeta,2)+sp.diff(qfun,zeta)).subs(zeta,1)-sp.Rational(32,3))==0
checks+=3

report={
    'scope':'Independent symbolic / high-precision *finite* oracle, not an all-B theorem',
    'checks':checks,
    'source':'original four signed BBP poles and U_0=0',
    'target_x':mp.nstr(x,64),
    'samples':source_data,
    'phase_source_split':phase_data,
    'four_tap_green':four_data,
    'status':{'full_pi_normality':'OPEN','R0':'OPEN','source_phase_transport':'EXACT PAPER IDENTITY'},
}
path=Path(__file__).parent/'FINITE_REPORT.json'
path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('INDEPENDENT_AUDIT_PASS',checks,'symbolic/high-precision checks')
print('x =',mp.nstr(x,28))
print('RB/coin n64 =',source_data[-1]['rb_over_bernoulli'])
print('four-tap positive n32 q256 =',four_data[-1]['signed_green_double_difference'])
