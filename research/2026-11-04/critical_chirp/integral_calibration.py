"""Optional noncertifying high-precision finite integral comparison.

Not used in proof or native test requirements. Exact source proof is in PROOFS.md.
"""
from __future__ import annotations
import mpmath as mp

HOLDOUT_MU=(8,32,128) # preregistered before first evaluations

def half_turn(mu:int,dps:int):
    if mu<1 or dps<20: raise ValueError('positive mu, precision>=20')
    with mp.workdps(dps):
        L=mp.mpf(mu)
        a=2/mp.sqrt(1+2/L)
        f=lambda x: mp.exp(-2j*mp.pi*L/(x*x))
        integral=mp.quad(f,[a,2])
        scaled=L*abs(integral)
        return mp.nstr(scaled,30),mp.nstr(scaled-4/mp.pi,30)

if __name__=='__main__':
    for mu in HOLDOUT_MU:
        p60=half_turn(mu,60)
        p90=half_turn(mu,90)
        assert abs(mp.mpf(p60[0])-mp.mpf(p90[0]))<mp.mpf('1e-25')
        print('HALF_TURN',mu,'scaled_60',p60[0], 'scaled_90',p90[0], 'error',p90[1])
    print('QUADRATURE_CALIBRATION_ONLY_NOT_PROOF')
