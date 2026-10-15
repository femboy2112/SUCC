"""Optional independent high-precision Gaussian wavepacket calibration.

The true theorem is elementary Gaussian integration with exact rational
upper bounds.  This mpmath oracle is NOT a mathematical sign certificate.
"""
from __future__ import annotations
import json
import mpmath as mp
mp.mp.dps=55


def run():
    cases=[]
    for N,t,frequency_gap in ((8,1,mp.mpf(1)/8),
                              (16,2,mp.mpf(1)/16),
                              (32,1,mp.mpf(1)/32)):
        tau=mp.mpf(1)/N**2
        g=lambda x: (2*tau)**mp.mpf('.25')*mp.exp(-mp.pi*tau*x*x)
        norm=mp.quad(lambda x:g(x)**2,[-mp.inf,mp.inf])
        observed_shift=mp.quad(lambda x:(g(x+t)-g(x))**2,[-mp.inf,mp.inf])
        formula_shift=2*(1-mp.exp(-mp.pi*tau*t*t/2))
        overlap=mp.quad(lambda x:g(x)**2*mp.cos(2*mp.pi*frequency_gap*x),
                        [-mp.inf,mp.inf])
        formula_overlap=mp.exp(-mp.pi*frequency_gap**2/(2*tau))
        assert abs(norm-1)<mp.mpf('1e-40')
        assert abs(observed_shift-formula_shift)<mp.mpf('1e-40')
        assert abs(overlap-formula_overlap)<mp.mpf('1e-40')
        cases.append({
            'N':N,'time_shift':t,'source_frequency_gap':mp.nstr(frequency_gap,22),
            'norm_error':mp.nstr(abs(norm-1),9),
            'shift_identity_error':mp.nstr(abs(observed_shift-formula_shift),9),
            'source_Gram_identity_error':mp.nstr(abs(overlap-formula_overlap),9),
            'observed_shift_residual_squared':mp.nstr(observed_shift,20),
            'observed_Gram_overlap':mp.nstr(overlap,20)
        })
    return {'oracle':'NUMERICAL_GAUSSIAN_SOURCE_CALIBRATION_NOT_PROOF',
            'precision_dps':55,'cases':cases,
            'not_a_solenoid_Weil_intertwiner':True,'RH_proved':False}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
