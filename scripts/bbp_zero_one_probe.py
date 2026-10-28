"""Finite rational reproducibility receipt for BBP q=0/q=1 character probes."""
from __future__ import annotations
import json,sys
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.bbp_zero_one_characters import (
    BETA,authentic_r,canceled_r,source_moment,mutant_multiplier,
    mutant_source,mutant_state,polynomial_evaluate,one_jet_of_polynomial,
    zero_jet_of_polynomial,jet_character_phase,discontinuity_witness,
    mutant_rational_extension,two_adic_unit,regularized_slope_rational_certificate,
    rational_eval_tail_bound)

def main():
    source=0
    for n in range(1,257):
        assert authentic_r(n)==canceled_r(n)==source_moment(n)
        source+=1
    jets=0
    for K in range(1,6):
        for J in range(2,7):
            mult=mutant_multiplier(K,J)
            assert polynomial_evaluate(mult,BETA)==0
            assert one_jet_of_polynomial(mult,J)==(Q(1),)+(Q(0),)*(J-1)
            assert zero_jet_of_polynomial(mult,K)==(Q(1),)+(Q(0),)*(K-1)
            assert abs(mutant_state(150,K,J))<Q(1,100) # selected 0, decays
            jets+=1
    adic=0
    for K,J in ((1,2),(2,3),(3,4)):
        for x in range(2,100):
            lhs=mutant_rational_extension(x+1,K,J)-mutant_rational_extension(x,K,J)
            assert two_adic_unit(lhs)
            adic+=1
    noncontinuity=0
    for at_one in (False,True):
        for k in range(2,13):
            p,v=discontinuity_witness(k,at_one)
            assert v==Q(1,2)
            jet=one_jet_of_polynomial(p,k) if at_one else zero_jet_of_polynomial(p,k)
            assert jet==(Q(0),)*k
            noncontinuity+=1
    slope_center,rad=regularized_slope_rational_certificate(64)
    data={
     'status':'PASS', 'authority':'exact finite rational checks; no pi-normality proof',
     'source_integral_coefficients':source,'mutant_0_1_jet_controls':jets,
     'late_time_2adic_isometry_controls':adic,
     'noncontinuous_interior_evaluation_controls':noncontinuity,
     'renormalized_slope_rational_center':f'{slope_center.numerator}/{slope_center.denominator}',
     'renormalized_slope_error_bound':f'{rad.numerator}/{rad.denominator}',
     'source_selected_beta':'1/16',
     'source_pi_prefix_bound_at_64':str(rational_eval_tail_bound(64)),
    }
    print(json.dumps(data,indent=2,sort_keys=True))
if __name__=='__main__':main()
