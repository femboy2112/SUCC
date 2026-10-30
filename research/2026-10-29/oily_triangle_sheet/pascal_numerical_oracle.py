"""Independent numerical Pascal-golden convergence holdout. NOT a proof certificate."""
from __future__ import annotations
from math import comb
from platform import python_version
import mpmath as mp

mp.mp.dps=90
lam=(mp.sqrt(5)-1)/2
p=lam**2
omega=lam-mp.euler
print("Python", python_version(), "mpmath", mp.__version__, "dps", mp.mp.dps)
print("lambda=",mp.nstr(lam,45),"p*=",mp.nstr(p,45))
print("Omega=",mp.nstr(omega,45))
for m in (1,2,4,8,16,32,64,128):
    positive=sum((mp.mpf(comb(m,k))*lam**(m+k)*mp.harmonic(k) for k in range(m+1)),mp.mpf(0))
    harmonic_minus_logtail=mp.harmonic(m)-sum((lam**j/mp.mpf(j) for j in range(1,m+1)),mp.mpf(0))
    assert mp.almosteq(positive,harmonic_minus_logtail,rel_eps=mp.mpf('1e-65'))
    omega_m=lam-positive+mp.log(m*p)
    error=omega-omega_m
    bound=1/(2*mp.mpf(m))+lam**(m+1)/((m+1)*(1-lam))
    assert 0<error<bound
    print(f'm={m:3d} omega_m={mp.nstr(omega_m,23):>27} '
          f'error={mp.nstr(error,14):>17} bound={mp.nstr(bound,14):>17}')
print('PASCAL_NUMERIC_HOLDOUT_PASS: 8 finite ranks; not rigorous enclosures')
