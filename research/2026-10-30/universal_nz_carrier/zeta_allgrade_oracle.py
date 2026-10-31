"""Separate 100-dps two-route calibration, no imports from test modules."""
from math import comb
import json
import mpmath as mp
mp.mp.dps=110
A2=3*mp.log(3)-4*mp.log(2)
def inner(n):
    return mp.fsum((-1)**k * comb(n,k)*(k+1)*mp.log(k+1) for k in range(n+1))
M=60
pascal=mp.mpf(10)/3*mp.log(2)-4*mp.fsum(inner(n)/mp.power(2,n+1) for n in range(2,M+1))
err=4*A2/mp.power(2,M+1)
prime=-mp.diff(mp.zeta,2)/mp.zeta(2)
reflect=mp.log(2*mp.pi)+mp.euler-1+prime
assert 0 < pascal-reflect < err
f=lambda x:mp.exp(-x)*mp.expm1(-x)**2/(x*x*(1+mp.exp(-x))) if x else mp.mpf('0.5')
I=mp.quad(f,[0,1,6,mp.inf])
assert abs(mp.mpf(10)/3*mp.log(2)-I-reflect)<mp.mpf('1e-100')
print(json.dumps({'status':'PASS','M':M,'zeta_logderivative_pascal_upper':mp.nstr(pascal,75),'prime_reflection':mp.nstr(reflect,75),'rigorous_pascal_tail_bound':mp.nstr(err,25),'positive_integral':mp.nstr(I,70),'mpmath':mp.__version__},indent=2))
