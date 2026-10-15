"""Independent numerical non-proof calibration, explicitly no zero lookup.

All zero density and signed form-tail inequalities are proven algebraically in
research/2026-10-14/SIGNED_WEIL_H1_SPECTRAL_TAIL.md.  The only be evaluations
below are at arbitrary sampling points, not zeros or a zero-hunting oracle.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fractions import Fraction as Q
from observational_succ.signed_weil_h1_tail import (
    source_count, signed_tail_operator_bound, absolute_zero_tail_weight,
    first_pair_receipt,
)
import mpmath as mp
mp.mp.dps=45

def xi(s):
    return s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)/2

def tent_laplace(s,a):
    # v_a(x)=1-x²/a² on [-a,a], otherwise zero; in H_0^1, not C^7.
    z=s-mp.mpf('0.5')
    if abs(z)<mp.mpf('1e-20'):
        return 4*a/3
    return 4*(a*z*mp.cosh(a*z)-mp.sinh(a*z))/(a*a*z*z*z)

def run():
    a=mp.mpf('0.5'); h1sq=mp.mpf(16)*a/15+mp.mpf(8)/(3*a)
    samples=[]
    for beta,gamma in [(mp.mpf(1)/4,30),(mp.mpf(1)/2,48),(mp.mpf(3)/4,90)]:
        s=beta+1j*gamma
        A=tent_laplace(s,a)
        B=tent_laplace(1-mp.conj(s),a)
        absolute=abs(A*mp.conj(B))
        individual=(5*a/2)*mp.exp(a)*h1sq/(gamma*gamma)
        assert absolute < individual
        samples.append({'synthetic_beta':mp.nstr(beta,10),
                        'synthetic_gamma':gamma,
                        'absolute_spectral_product':mp.nstr(absolute,25),
                        'perzero_H1_envelope':mp.nstr(individual,25),
                        'zero_is_authentic':False})
    source_points=[]
    for z in (mp.mpf('2'),mp.mpf('3')+2j,mp.mpf(4)+5j,mp.mpf(5)+7j):
        F=xi(mp.mpf('0.5')+z)
        R=abs(z)
        growth=3*(1+R)**(R/2+2)
        assert abs(F)<growth
        source_points.append({'shifted_z':str(z),'absolute_Xi':mp.nstr(abs(F),25),
                              'theta_Jensen_growth_upper':mp.nstr(growth,25)})
    tail=[]
    for t in (16,100,1000,10**6):
        delta=Q(signed_tail_operator_bound(Q(1,2),t)['signed_remainder_form_norm_upper'])
        exact=mp.mpf(delta.numerator)/delta.denominator
        expected=70*a*mp.exp(a)*mp.log(16*t)/t
        assert exact >= expected and (exact-expected)<mp.mpf('1e-20')
        tail.append({'T':t,'delta':mp.nstr(exact,24),
                     'source_upper_count':source_count(t)['absolute_count_upper']})
    cert=first_pair_receipt()
    return {'status':'INDEPENDENT_NUMERICAL_CALIBRATION_NOT_PROOF',
            'precision_digits':45,'no_zeta_zero_list_or_zero_finding':True,
            'no_RH_assertion':True,'synthetic_offcritical_products':samples,
            'Xi_growth_points_no_zero_lookup':source_points,
            'source_only_H1_tail':tail,
            'source_pair_receipt_sha':cert['receipt_sha']}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
