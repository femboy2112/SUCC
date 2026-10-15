"""INDEPENDENT NUMERICAL CALIBRATION only; cannot authorize proof statuses.

No nontrivial zero queries. The true theta/Gamma integer source alone constructs
proofs; mpmath's zeta is used here only as a separate HOLDOUT oracle.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.theta_taylor_jets import jets, rouche_center_certificate, certified_midpoint_polynomial
from fractions import Fraction as Q
import mpmath as mp

mp.mp.dps=65

def mpr(q):return mp.mpf(q.numerator)/q.denominator

def xi(s):return (s*(s-1)/2)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)

def theta_b(j):
    summand=mp.mpf(0)
    for n in range(1,6):
        summand += mp.quad(lambda t: mp.exp(-mp.pi*n*n*t)*t**(-mp.mpf(3)/4)*mp.log(t)**(2*j),[1,2,4,8,mp.inf])
    return summand/(4**j*mp.factorial(2*j))

def run():
    data=jets(20,3,8,1536)
    rows=[]
    for j in (0,1,2,3,4,6,8,10,12,16,20):
        actual=theta_b(j)
        l,h=data['b'][j]
        assert mpr(l) <= actual <= mpr(h), f'interval excludes independent theta moment {j}'
        rows.append({'j':j,'b_numeric':mp.nstr(actual,27),'certified_bracket':True,
                     'width':mp.nstr(mpr(h-l),12)})
    obs=certified_midpoint_polynomial(data,Q(11,2),13)
    c=obs['coefficient_midpoints']
    err=mpr(obs['uniform_complex_error'])
    points=[0,1,2,3,mp.mpf('5.5')*1j,mp.mpf('1.5')+mp.mpf('4')*1j,mp.mpf('2.4')+mp.mpf('2')*1j]
    samples=[]
    for z in points:
        poly=sum((mpr(a)*z**(2*j) for j,a in enumerate(c)),mp.mpc(0))
        exact=xi(mp.mpf('0.5')+z)
        resid=abs(exact-poly)
        assert resid <= err+mp.mpf('1e-45'), f'xi holdout outside enclosure: {z}'
        samples.append({'z':mp.nstr(z,20),'actual_xi':mp.nstr(exact,27),
                        'abs_midpoint_error':mp.nstr(resid,15),'certified_uniform_bound':mp.nstr(err,15)})
    return {'evidence':'NUMERICAL_HOLDOUT_NOT_PROOF','theta_moments':rows,
            'xi_samples':samples,'certified_R55':rouche_center_certificate(data,Q(11,2),13)['certified_zero_free'],
            'nontrivial_zero_coordinates_used':False,'RH_proved':False}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
