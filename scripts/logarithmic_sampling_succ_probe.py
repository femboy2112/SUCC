"""Independent finite rational probe for logarithmic BBP sampling identities.

Run: python scripts/logarithmic_sampling_succ_probe.py
Only exact small rational inputs are measured; infinite results are paper proofs.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.logarithmic_sampling_succ import (
    source_r,states_through,pi_prefix,finite_green_tail,
    exact_weighted_sampling_identity,chiral_source,
    CHIRAL_PLUS,CHIRAL_MINUS,source_log_shift_ratio,
    chiral_harmonic_prefix,chiral_harmonic_remainder_constant_bound,
    asymptotic_weight_equivalence,
    fixed_mellin_alias_upper,fixed_mellin_band_upper)


def independent_polynomial_eval(coeff,x):
    return sum((Q(c)*Q(x)**i for i,c in enumerate(coeff)),Q())


def independent_integral(coeff,start,stop):
    return sum((Q(c)*(stop**(i+1)-start**(i+1))/(i+1)
                for i,c in enumerate(coeff)),Q())


def main():
    source_checks=0
    for n in range(1,201):
        direct=Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        assert direct==source_r(n)
        source_checks+=1

    green_checks=0
    for cutoff in (12,25,48):
        U=Q(0)
        piL=pi_prefix(cutoff)
        for n in range(1,cutoff+1):
            U=16*U+source_r(n)
            independent_tail=sum((source_r(j)/16**(j-n) for j in range(n+1,cutoff+1)),Q())
            assert U==16**(n-1)*piL-independent_tail
            assert independent_tail==finite_green_tail(n,cutoff)
            assert 0<=independent_tail<Q(1,15*(n+1)**2)
            green_checks+=1

    sawtooth_checks=0
    source_pulse_checks=0
    cases=[(Q(1),Q(1,600),Q(1,6000)),
           (Q(1,4),Q(1,10),Q(0)),
           (Q(1,360),Q(1,10**5),Q(1,10**8)),
           (Q(0),Q(0),Q(0))]
    for degree, step, shifts in product(range(5),(Q(1),Q(3,4),Q(11,7)),cases):
        coeff=tuple(Q((-1)**i*(i+1),i+2) for i in range(degree+1))
        N=len(shifts)
        answer=exact_weighted_sampling_identity(coeff,step,shifts)
        independent_sample=sum((independent_polynomial_eval(coeff,j*step-d)
                                for j,d in enumerate(shifts)),Q())
        independent_average=independent_integral(coeff,Q(0),N*step)/step
        assert answer['sample']==independent_sample
        assert answer['continuous']==independent_average
        assert answer['defect_left']==answer['defect_right']
        if any(shifts):
            derivative=tuple(Q(i)*coeff[i] for i in range(1,len(coeff)))
            independent_pulse=sum((independent_integral(derivative,j*step-d,j*step)
                                   for j,d in enumerate(shifts)),Q())
            assert answer['source_pulse']==independent_pulse
            source_pulse_checks+=1
        sawtooth_checks+=1

    ratio_checks=0
    for cutoff in (20,40):
        states=states_through(cutoff)
        piL=pi_prefix(cutoff)
        for n in range(cutoff-1):
            epsilon=source_log_shift_ratio(n,cutoff)
            assert states[n+1]==16**n*piL*(1-epsilon)
            ratio_checks+=1

    chiral_checks=0
    assert sum(CHIRAL_PLUS)+sum(CHIRAL_MINUS)==0
    for n in range(1,201):
        assert chiral_source(n,'+')+chiral_source(n,'-')==source_r(n)
        chiral_checks+=1

    chiral_gamma_checks=0
    for n in (2,7,40,120):
        plus=chiral_harmonic_prefix(n,'+')
        minus=chiral_harmonic_prefix(n,'-')
        assert plus['raw']+minus['raw']==plus['counterterm_sum']+minus['counterterm_sum']
        for sign in ('+','-'):
            assert chiral_harmonic_remainder_constant_bound(sign)>0
        chiral_gamma_checks+=1

    weight_checks=0
    for N in (2,8,32,128):
        base=Q(4,9)
        weights=tuple(base+Q(1,n) for n in range(1,N+1))
        predicted=sum((Q(1,n) for n in range(1,N+1)),Q())/N
        assert asymptotic_weight_equivalence(weights,base)==predicted
        weight_checks+=1

    finite_band_checks=0
    for h,alpha,K in product((1,2,-3),(Q(1),Q(-5,7)),(0,1,5)):
        direct=sum((fixed_mellin_alias_upper(k,h,alpha)
                    for k in range(-K,K+1)),Q())
        assert direct==fixed_mellin_band_upper(K,h,alpha)
        finite_band_checks+=1

    report={'status':'PASS','exact_original_four_pole_checks':source_checks,
            'exact_Green_prefix_checks':green_checks,
            'exact_polynomial_dirac_sawtooth_checks':sawtooth_checks,
            'source_pulse_checks':source_pulse_checks,
            'finite_log_shift_ratio_checks':ratio_checks,
            'exact_chiral_source_checks':chiral_checks,
            'scalar_weight_countermodel_checks':weight_checks,
            'exact_chiral_harmonic_gamma_cancellation_checks':chiral_gamma_checks,
            'fixed_alias_majorant_checks':finite_band_checks,
            'claim':'finite exact rational oracle only: no real signed pi-Weyl cancellation'}
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=='__main__':main()
