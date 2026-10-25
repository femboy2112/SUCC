#!/usr/bin/env python3
"""Frozen authentic BBP N-carrier proof-failure crucible (exact probes).

No normality claim.  Taylor/Machin Fourier envelopes and empirical Brier
scores are finite source observations.  Numerical approximations are separate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
from math import lcm

from observational_succ.bbp_natural_carrier import exact_forcing
from observational_succ.pi_succ_lag_bridge import (
    source_circle_prefix, exact_lag_phase_defect, lag_source,
    lag_positive_upper, clock_blind_lag, special_clock_valuation,
    gaussian_vdc_certificate, resonance_frequency,
    forcing_upper_remainder, fourier_lag_rational_upper,
)
from observational_succ.pi_succ_character_intervals import (
    machin_pi_interval, fourier_squared_interval,magnitude_decimal_bounds,
)
from observational_succ.pi_succ_observer_ablation import (
    source_observations, complete_factorial, full_four_way_interaction,
    feature_mutation,
)


def run():
    checks=0
    def check(ok,context):
        nonlocal checks
        checks+=1
        if not ok:raise AssertionError(context)

    # Frozen windows predeclared before reading outcomes; latter two are
    # independent future/holdout *data* not independent mathematical proof.
    train_limits=(64,1024)
    first_hold=(1024,2048)
    fresh_hold=(2048,3072)
    observations=source_observations(64,3071)
    groups=[tuple(x for x in observations if left<=x.n<right)
            for left,right in (train_limits,first_hold,fresh_hold)]
    check([len(x) for x in groups]==[960,1024,1024],"disjoint window sizes")
    check(all(tail.tail_terms==0 for tail in observations),"single-bound digit certificate")
    check(len(set(x.n for x in observations))==3008,"no duplicate timelines")

    tables=[]
    for group in groups[1:]:
        table=complete_factorial(groups[0],group)
        check(len(table)==16,"complete 2^4 factorial")
        rows=[]
        for subset in sorted(table,key=lambda s:(len(s),s)):
            risk=table[subset]
            check(risk>=0,"Brier nonnegative")
            rows.append({"families":"+".join(("D","P","L","Q")[i] for i in subset) or "empty",
                         "subset":list(subset),"exact_risk":str(risk),
                         "risk_9dp":str(Q((risk*10**9).numerator//(risk*10**9).denominator,10**9))})
        interaction=full_four_way_interaction(table)
        tables.append({"rows":rows,"interaction_exact":str(interaction),
                       "interaction_9dp":round(float(interaction),9),
                       "full_minus_empty_risk_exact":str(table[(0,1,2,3)]-table[()]),
                       "full_minus_empty_risk_float":float(table[(0,1,2,3)]-table[()])})
    mutated=feature_mutation(groups[1],3,7)
    mutant=complete_factorial(groups[0],mutated)
    check(mutant[(0,1,2,3)]!=complete_factorial(groups[0],groups[1])[(0,1,2,3)],
          "shuffled prime clocks alter full gate risk")

    selected=source_circle_prefix(390)
    spectral=[]
    pi_bounds=machin_pi_interval(12)
    for start,size in ((64,64),(128,128),(256,128)):
        for k in (1,2,3):
            amp_sq=fourier_squared_interval(
                selected[start:start+size],16**k-1,pi_bounds,order=10)
            check(Q()<=amp_sq[0]<amp_sq[1]<Q(1),"nontrivial exact Fourier magnitude")
            ml,mh=magnitude_decimal_bounds(amp_sq,7)
            spectral.append({"start":start,"samples":size,"lag":k,
                             "mode":16**k-1,"certified_modulus_interval_7dp":[ml,mh],
                             "certified_square_width_float_display":float(amp_sq[1]-amp_sq[0])})

    comparison=source_circle_prefix(82)
    for n in range(1,35):
        for k in (1,7):
            check(exact_lag_phase_defect(comparison,n,k)==0,"source anchored lag")
            check(Q()<lag_source(n,k)<lag_positive_upper(n,k),"positive sharp source lag")
    for n in range(2,500):
        check(forcing_upper_remainder(n)>0,"positive source polynomial")
    vdc=[]
    for z in (((1,0),)*12,
              ((1,0),(0,1),(-1,0),(0,-1))*3,
              ((1,0),(-1,0))*6):
        for h in (2,4,6,12):
            a,b=gaussian_vdc_certificate(tuple(z),h)
            check(a<=b,"exact source-independent van der Corput control")
            vdc.append([str(a),str(b)])

    clocks=[]
    for depth in (1,2,3,4):
        k=clock_blind_lag(tuple((p,depth) for p in (3,5,7,13)))
        check(all(pow(16,k,p**depth)==1 for p in (3,5,7,13)),"shared clock annihilation")
        clocks.append({"depth":depth,"minimal_lag":k,"lags_vs_window_512":str(k/512)})
    for k in range(1,129):
        for p in (3,5,7,13):
            v=special_clock_valuation(p,k)
            check((16**k-1)%(p**v)==0,"special valuation lower")
            check((16**k-1)%(p**(v+1))!=0,"special valuation upper")
    resonances=[]
    for N in (4,12,32,64):
        h=resonance_frequency(selected[:N])
        check(all((h*x).denominator==1 for x in selected[:N]),"exact finite frequency resonance")
        resonances.append({"N":N,"h_bit_length":h.bit_length()})

    result={
        "experiment":"SUCC N-carrier one-shot spectral crucible; no normality proof",
        "observed_claim":"Actual BBP Fourier frequency cancellation for all fixed h remains unproved",
        "base_parent":"research/pi-natural-carrier-bbp-internal-2026-10-24@f3498142319919e61e56bfe80c39d5410d8c61bf",
        "source":"original four-pole rational BBP recurrence, origin zero, same natural time axis",
        "samples":{"training":{"start":64,"stop_exclusive":1024,"n":len(groups[0]),"digit_zero_count":sum(x.zero_gate for x in groups[0])},
                   "holdout":{"start":1024,"stop_exclusive":2048,"n":len(groups[1]),"digit_zero_count":sum(x.zero_gate for x in groups[1])},
                   "future":{"start":2048,"stop_exclusive":3072,"n":len(groups[2]),"digit_zero_count":sum(x.zero_gate for x in groups[2])}},
        "digit_certificates":{"all_3008_one_tight_tail_bound":True,
                              "threshold":"T_n<1/((8n+1)(8n+2)) (inherited source theorem)"},
        "families":{"D":"dyadic U_n mod 4",
                    "P":"Pascal backward difference U_n-U_(n-1) mod 8",
                    "L":"Lucas row support 2^popcount(n) modulo 7",
                    "Q":"odd-prime depth residues (v3(den)%3, v5(den)%3)"},
        "factorial_holdout":tables[0],
        "factorial_future":tables[1],
        "wrong_time_odd_prime_full_risk":str(mutant[(0,1,2,3)]),
        "certified_special_fourier_amplitudes":spectral,
        "blind_clock_cost":clocks,
        "finite_frequency_resonances":resonances,
        "gaussian_vdc_controls":vdc,
        "checks_passed":checks,
        "status":{"fourier_selected_saving":"UNVERIFIED",
                  "pi_normality":"OPEN","rational_primary_full_factorial":"VERIFIED FINITE",
                  "cyclotomic_lag_bridge":"PAPER PROVED using classical vdc and original BBP"}
    }
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=None)
    args=parser.parse_args()
    result=run()
    txt=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(txt)
    print(json.dumps({"checks_passed":result['checks_passed'],
                      "samples":result['samples'],
                      "certified_spectral":result['certified_special_fourier_amplitudes'],
                      "risk_contrasts":[x['full_minus_empty_risk_float']
                                       for x in (result['factorial_holdout'],result['factorial_future'])]},indent=2))

if __name__=='__main__':main()
