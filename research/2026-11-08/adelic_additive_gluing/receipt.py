#!/usr/bin/env python3
"""Preregistered cold-clock BBP source × adelic phase diagnostics.

Run: PYTHONPATH=. python research/2026-11-08/adelic_additive_gluing/receipt.py
This is not a pi oracle, mathematical certificate of Fourier cancellation,
or proof of an asymptotic source-selected estimate. Uses canonical BBP source.
"""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp
from observational_succ.duck_bbp import forcing
from observational_succ.adelic_additive_gluing import (
    source_p_history, orbit_states, original_phase_parts,
    critical_steps, holonomy_exponent, holonomy_center,
    holonomy_error_bound, coboundary_defect_delta,
    coboundary_delta_center, coboundary_delta_error,
)

PRECISION=70
HOLDOUTS=((192,457,(1,3)),(320,769,(1,3)))
CALIBRATION=((32,73,(1,3)),(80,193,(1,3)),(100,233,(1,3)))


def _phase(q: Fraction, h: int=1):
    t=(h*q)%1
    return mp.exp(2j*mp.pi*(mp.mpf(t.numerator)/t.denominator))


def _round(z):
    return [float(mp.re(z)),float(mp.im(z))]


def _counterseed(A:int)->Fraction:
    N=2*A+10; M=8*A+80
    alpha=sum((forcing(j)/16**j for j in range(1,N+1)),Fraction(0))
    quant=2**M
    return -Fraction((quant*alpha).numerator//(quant*alpha).denominator,quant)


def analyze(A:int,p:int,hs=(1,3)):
    states=orbit_states(2*A-1)
    C=source_p_history(p,2*A-1)
    k=(p-1)//8
    births=[k+1,4*k+1,5*k+1,6*k+1]
    # The all-prime phase product is checked exactly against the original rational
    # phase at EACH sample, not by comparing two floating routines.
    for n in range(A,2*A):
        u=states[n]
        parts=original_phase_parts(n,states=states)
        assert sum(parts.values(),Fraction())%1 == u%1
        assert parts.get(p,Fraction(0))==Fraction(C[n],p)
    wrong_seed=_counterseed(A)
    kcrit=critical_steps(A)
    theta=holonomy_exponent(A,kcrit)
    delta=coboundary_defect_delta(A,kcrit)
    assert abs(theta-holonomy_center(A,kcrit))<=holonomy_error_bound(A,kcrit)
    assert abs(delta-coboundary_delta_center(A,kcrit))<=coboundary_delta_error(A,kcrit)
    data={"A":A,"p":p,"p_births":births,"h":{},"all_prime_crt_checks":A,
          "source_critical_k":kcrit,
          "source_holonomy":str(theta),"source_holonomy_center":str(holonomy_center(A,kcrit)),
          "same_pi_coboundary_delta":str(delta),
          "same_pi_coboundary_center":str(coboundary_delta_center(A,kcrit)),
          "counterseed_dyadic_numerator_digits":len(str(abs(wrong_seed.numerator))),
          "counterseed_dyadic_denominator_digits":len(str(wrong_seed.denominator))}
    for h in hs:
        phase=[];local=[];complement=[];wrong=[]
        for n in range(A,2*A):
            u=states[n];c=Fraction(C[n],p)
            phase.append(_phase(u,h));local.append(_phase(c,h));complement.append(_phase(u-c,h))
            wrong.append(_phase(u+16**n*wrong_seed,h))
        assert max(abs(phase[j]-local[j]*complement[j]) for j in range(A))<mp.mpf('1e-50')
        w=sum(phase)/A;am=sum(local)/A;bm=sum(complement)/A; ww=sum(wrong)/A
        tv=sum(abs(complement[j+1]-complement[j]) for j in range(A-1))
        data['h'][str(h)]={"zero_weyl":_round(w),"prime_marginal":_round(am),
            "real_complement_marginal":_round(bm),"signed_dependence":_round(w-am*bm),
            "dyadic_coherent_counterseed_weyl":_round(ww),
            "complement_total_variation":float(tv),"variation_per_sample":float(tv/A),
            "prime_abelform_bound_if_E=1":float(1+tv)}
    return data


def main():
    mp.mp.dps=PRECISION
    out={"status":"FINITE DIAGNOSTIC ONLY; PI NORMALITY OPEN",
         "preregistration":"PREREGISTRATION.md at commit b71d766d464a4c45a53e2748db38f874a639faac",
         "precision_dps":PRECISION,"run_inputs":"exact original four-pole rational source; no pi oracle",
         "calibration":[analyze(*case) for case in CALIBRATION],
         "holdouts":[analyze(*case) for case in HOLDOUTS]}
    payload=json.dumps(out,indent=2,sort_keys=True)+'\n'
    out_path=Path(__file__).with_name('FINITE_DIAGNOSTICS.json')
    out_path.write_text(payload)
    print('wrote',out_path,'sha256',hashlib.sha256(payload.encode()).hexdigest())
    for x in out['holdouts']:
        print('A',x['A'],'p',x['p'],'births',x['p_births'])
        for h,y in x['h'].items():
            z=y['zero_weyl'];ww=y['dyadic_coherent_counterseed_weyl'];p=y['prime_marginal'];
            print(' h',h,'W',z,'wrong',ww,'pmean',p,'TV/A',y['variation_per_sample'])


if __name__=='__main__':
    main()
