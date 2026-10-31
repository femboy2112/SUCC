"""Distinct SymPy/mpmath oracle; does not import the carrier_probe implementation.

Numeric checks calibrate paper formulas; not independent peer review or proof.
"""
import json
from fractions import Fraction
from math import comb
from pathlib import Path
import mpmath as mp
import sympy as sp

mp.mp.dps=70
observations=[]
for m in range(16):
    s=sp.Rational(0)
    for n in range(m+1):
        inner=sum((-1)**k*comb(n,k)*(k+1)**m for k in range(n+1))
        s+=sp.Rational(inner,2**(n+1))
    value=sp.factor(s/(1-2**(m+1)))
    expected=sp.zeta(-m)
    assert value == expected, (m,value,expected)
    observations.append({'m':m,'zeta_neg':str(value)})

# Euler reflected logarithmic-derivative equality; analytic, not finite equality of raw divergent sums.
L=-mp.diff(mp.zeta,2)/mp.zeta(2)
left=mp.diff(mp.zeta,-1)/mp.zeta(-1)
right=mp.log(2*mp.pi)+mp.euler-1+L
assert abs(left-right)<mp.mpf('1e-65')

# Independent prime-power sieve and certified tail bound.
N=50000
mangoldt_sum=mp.mpf(0)
primepowers=0
for p in sp.primerange(2,N+1):
    q=int(p)
    while q<=N:
        mangoldt_sum+=mp.log(int(p))/(q*q)
        primepowers+=1
        q*=int(p)
tail=(mp.log(N)+1)/N
assert 0 < L-mangoldt_sum < tail

# Integer lattice theta modularity with analytic geometric tail control.
theta_obs=[]
for t in (mp.mpf('0.23'),mp.mpf('0.37'),mp.mpf('1'),mp.mpf('2.7')):
    M=18
    def approx(v):
        return sum(mp.exp(-mp.pi*v*j*j) for j in range(-M,M+1))
    def tail_bound(v):
        return 2*mp.exp(-mp.pi*v*(M+1)**2)/(1-mp.exp(-mp.pi*v*(2*M+3)))
    residual=abs(approx(t)-approx(1/t)/mp.sqrt(t))
    maxerr=tail_bound(t)+tail_bound(1/t)/mp.sqrt(t)
    assert residual <= maxerr + mp.mpf('1e-60')
    theta_obs.append({'t':str(t),'residual':mp.nstr(residual,12),'analytic_truncation_bound':mp.nstr(maxerr,12)})

# Independent Gamma integral moments (known closed form, not pi digit mechanism).
for rank in (1,2,3,7):
    for k in (0,1,2,4):
        integral=mp.quad(lambda y:y**(rank+k-1)*mp.exp(-y)/mp.gamma(rank),[0,mp.inf])
        assert abs(integral-mp.factorial(k)*mp.binomial(rank+k-1,k))<mp.mpf('1e-54')

# Original 4-pole BBP source independent high-precision numerical calibration.
r=lambda n: 4/mp.mpf(8*n-7)-2/mp.mpf(8*n-4)-1/mp.mpf(8*n-3)-1/mp.mpf(8*n-2)
alpha=sum((r(j)/16**j for j in range(1,150)))
assert abs(alpha-mp.pi/16)<mp.mpf('1e-65')

print(json.dumps({
 'result':'PASS',
 'independent_negative_zeta_cases':len(observations),
 'negative_zeta_values':observations,
 'functional_eq_prime_identity':{
   'log_derivative_zeta_minus1':mp.nstr(left,50),
   'completed_arch_prime_mass':mp.nstr(L,50),
   'prime_power_truncation_N':N,
   'prime_power_count':primepowers,
   'truncated_prime_power_sum':mp.nstr(mangoldt_sum,50),
   'remainder_bound':mp.nstr(tail,30)
 },
 'theta':theta_obs,
 'gamma_moment_numerical_cases':16,
 'pi_BBP_laplace_independent':mp.nstr(alpha,65),
 'mpmath_version':mp.__version__,'sympy_version':sp.__version__
},indent=2))