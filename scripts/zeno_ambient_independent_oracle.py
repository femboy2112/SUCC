#!/usr/bin/env python3
"""Independent high-precision calibration only (NOT proof authority).

Uses numerical quadrature and elementary ODE expressions rather than the
rational SUCC library. No zeta values, nontrivial zeros or fake source.
"""
from __future__ import annotations
import json
import mpmath as mp


def oracle():
    mp.mp.dps=60
    b=mp.log(2)
    k=lambda x:1/(2*mp.cosh(x/2))
    # Full-source prime shift/Gamma kernel moving-left-collar test.
    response=lambda x:mp.quad(lambda y:k(x+b-y),[0,b])/mp.sqrt(b)
    witness=mp.sqrt(mp.quad(lambda x:response(x)**2,[0,b]))
    proven_bound=2*b/5
    sharp=mp.mpf('0.5')
    g=lambda x:mp.sinh(x/2)
    rie=lambda x:4*(mp.sinh(sharp/2)/sharp*x-mp.sinh(x/2))
    ode_inner=mp.quad(lambda x:g(x)*rie(x),[-sharp,0,sharp])
    algebra=4*(sharp+mp.sinh(sharp))-16*(mp.cosh(sharp)-1)/sharp
    series=sum((4*(n-1)*sharp**(2*n+1)/((n+1)*mp.factorial(2*n+1)) for n in range(2,60)))
    first_null=sharp**9/(4032*(1-sharp*sharp/8)**2)
    if not witness > proven_bound > mp.mpf(11)/40:
        raise ValueError('Continuum source check contradicts rational bound')
    if not mp.almosteq(ode_inner,algebra,rel_eps=mp.mpf('1e-50')):
        raise ValueError('Original odd-pole source ODE calibration failed')
    if not mp.almosteq(series,algebra,rel_eps=mp.mpf('1e-50')):
        raise ValueError('Independently summed odd-pole series mismatch')
    return {"scope":"NUMERICAL_HOLDOUT_NOT_RIGOROUS_INTERVAL",
            "source":"original_prime2_and_Carleman_plus_original_odd_pole",
            "witness_norm_lower_45d":mp.nstr(witness,46),
            "analytic_norm_lower_45d":mp.nstr(proven_bound,46),
            "sharp_odd_pole_halfwidth_point5_45d":mp.nstr(algebra,46),
            "ode_integral_45d":mp.nstr(ode_inner,46),
            "positive_series_45d":mp.nstr(series,46),
            "moment_null_budget_45d":mp.nstr(first_null,46),
            "RH_proved":False}

if __name__=='__main__':
    print(json.dumps(oracle(),sort_keys=True,indent=2))
