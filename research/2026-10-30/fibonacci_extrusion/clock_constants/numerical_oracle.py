"""Separate special-function route; 100dps calibration, NOT interval authority."""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps=100
parent=Path(__file__).resolve().parents[1]
record=json.loads((parent/'receipts/clock-exact.log').read_text())
lam=(mp.sqrt(5)-1)/2
phi=1/lam
q=-lam**2
f=[0,1]
for _ in range(180):f.append(f[-1]+f[-2])
harm=mp.fsum(mp.digamma(m+1)-mp.log(m) for m in f[2:181])
# Integral representation of the geometric logarithm tail, distinct from
# the exact implementation's finite power series.
def tail(m):
    return mp.quad(lambda t:t**m/(1-t),[0,lam])
gold=mp.fsum(tail(m) for m in f[2:16])
lf=mp.log(mp.qp(q,q))
values={'harmonic_budget':harm,'golden_budget':gold,'oily_budget':harm+gold,
        'reciprocal_fibonacci':mp.fsum(1/mp.mpf(m) for m in f[1:181]),
        'fibonacci_square_reciprocal':mp.fsum(1/mp.mpf(m)**2 for m in f[2:181]),
        'log_fibonorial_constant':lf,
        'renormalized_pascal_sum':lf-mp.log(1-q)+harm+gold}
checks=[]
for name,value in values.items():
    item=record['constants'][name]
    lo=mp.mpf(item['lo_numerator'])/mp.mpf(item['denominator'])
    hi=mp.mpf(item['hi_numerator'])/mp.mpf(item['denominator'])
    assert lo<value<hi,(name,mp.nstr(value,70))
    checks.append({'name':name,'value':mp.nstr(value,65),'inside_certificate':True})
for label,item in record['point_controls'].items():
    m=int(label); value=mp.digamma(m+1)-mp.log(m)+tail(m)
    lo=mp.mpf(item['lo_numerator'])/mp.mpf(item['denominator'])
    hi=mp.mpf(item['hi_numerator'])/mp.mpf(item['denominator'])
    assert lo<value<hi,(m,mp.nstr(value,70))
    checks.append({'rank':m,'inside_certificate':True})
# Finite aggregate identity uses direct binomial expectation, a third route.
for n in (5,7,9):
    observed=mp.fsum(mp.fsum(mp.binomial(m,k)*(lam**2)**k*lam**(m-k)*
                           (mp.digamma(k+1)+mp.euler) for k in range(m+1))
                    for m in f[2:n+1])
    b=mp.fsum(mp.digamma(m+1)-mp.log(m)+tail(m) for m in f[2:n+1])
    rhs=(n-1)*(n-2)/2*mp.log(phi)+(n-1)*(mp.euler-mp.log(5)/2)+mp.log(mp.qp(q,q,n)/(1-q))+b
    assert abs(observed-rhs)<mp.mpf('1e-85')
    checks.append({'finite_aggregate_n':n,'residual':mp.nstr(abs(observed-rhs),8)})
wrong=mp.log(mp.qp(lam**2,lam**2))
assert abs(wrong-lf)>mp.mpf('0.1')
print(json.dumps({'status':'PASS','authority':'numerical calibration only; no external referee',
                  'mpmath':mp.__version__,'dps':mp.mp.dps,'checks':checks,
                  'wrong_conjugate_log_product':mp.nstr(wrong,40)},indent=2))
