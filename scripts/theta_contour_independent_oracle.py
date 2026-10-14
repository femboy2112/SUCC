"""Optional numeric holdout, not certificate; no nontrivial-zero coordinates.

Compare entirely independent theta quadrature with direct standard gamma*zeta
values only AFTER mathematical contour certificate was built from true theta.
"""
from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction as Q
import mpmath as mp

mp.mp.dps=65


def verify():
    y=mp.mpf(141347)/10000
    pi=mp.pi
    def psi(t):
        return mp.fsum([mp.exp(-pi*n*n*t) for n in (1,2,3,4)])
    def B_integrand(t):
        return psi(t)*t**(-mp.mpf(3)/4)*mp.cos(y*mp.log(t)/2)
    def S_integrand(t):
        return psi(t)*t**(-mp.mpf(3)/4)*(mp.log(t)/2)*mp.sin(y*mp.log(t)/2)
    bounds=[1,mp.mpf('1.25'),mp.mpf('1.5'),2,3,4,6,8,10,mp.inf]
    B=mp.quad(B_integrand,bounds)
    S=mp.quad(S_integrand,bounds)
    f0=mp.mpf('.5')-(y*y+mp.mpf('.25'))*B
    d=2*y*B-(y*y+mp.mpf('.25'))*S
    s=mp.mpf('.5')+1j*y
    xi=lambda v:mp.mpf('.5')*v*(v-1)*mp.power(mp.pi,-v/2)*mp.gamma(v/2)*mp.zeta(v)
    ref=xi(s)
    deriv=mp.diff(xi,s)
    errF=abs(f0-ref)
    errD=abs(1j*d-deriv)
    assert errF<mp.mpf('1e-28') and errD<mp.mpf('1e-28')
    return {
      'role':'NUMERICAL_HOLDOUT_NOT_RIGOROUS_INTERVAL',
      'precision_digits':65,
      'analytic_theta_B':mp.nstr(B,50),
      'analytic_theta_sine_moment':mp.nstr(S,50),
      'original_theta_F_real':mp.nstr(f0,50),
      'original_theta_derivative_imaginary':mp.nstr(d,50),
      'independent_completed_xi_value':mp.nstr(ref,50),
      'independent_completed_xi_derivative':mp.nstr(deriv,50),
      'value_residual':mp.nstr(errF,12),
      'derivative_residual':mp.nstr(errD,12),
      'contour_center_source':'source-search at rational ordinate 141347/10000',
      'nontrivial_zero_locations_used':False,
      'RH_proved':False,
    }

if __name__=='__main__':print(json.dumps(verify(),indent=2,sort_keys=True))
