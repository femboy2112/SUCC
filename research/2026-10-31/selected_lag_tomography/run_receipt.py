"""Produce source-checked finite signed-lag intervals with exact outward rounding.

Run directly for finite horizons. No extrapolation into normality or RH.
"""
import sys, json, hashlib, time
from fractions import Fraction as F
from pathlib import Path
from selected_lag import (
    selected_signed_lag_interval, vdc_certificate_from_signed_lag_interval,
    vdc_lag_error_bound_rational, signed_lag_mass)


def one(N,K,h=1):
    t=time.monotonic()
    low,high=selected_signed_lag_interval(N,K,h)
    assert low<=high
    error=vdc_lag_error_bound_rational(K,N,h)
    coherent_lower=signed_lag_mass(K,N)-error['weighted_rational_upper']
    square_upper=vdc_certificate_from_signed_lag_interval(N,K,h,(low,high))
    assert high<coherent_lower, 'selected and coherent comparison failed at finite horizon'
    return {
       'N':N,'K':K,'h':h,
       'selected_interval_rational':[str(low),str(high)],
       'selected_interval_display':[f'{float(low):.12f}',f'{float(high):.12f}'],
       'actual_selected_weyl_squared_normalized_upper':str(square_upper),
       'coherent_same_forcing_seed_lag_lower':str(coherent_lower),
       'coherent_lower_display':f'{float(coherent_lower):.12f}',
       'source_lag_transport_error_upper':str(error['weighted_rational_upper']),
       'source_lag_transport_coarse_upper':str(error['coarse_upper']),
       'instrument':'source-exact rational states, Machin pi bracket, Taylor/cos Lipschitz, 10^-12 outward grid',
       'horizon_class':'fresh holdout' if N>=1024 else 'calibration',
       'pi_normality_status':'OPEN',
       'independent_global_theorem':False,
       'runtime_seconds':round(time.monotonic()-t,2)
    }


def main():
    if len(sys.argv)!=3:
        raise SystemExit('usage: python run_receipt.py N K')
    N=int(sys.argv[1]);K=int(sys.argv[2])
    row=one(N,K)
    print(json.dumps(row,sort_keys=True))

if __name__=='__main__':main()
