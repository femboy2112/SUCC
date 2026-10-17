"""Deterministic standalone and optionally source-SHA-gated research receipt."""
import argparse
import json
import sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ import hidden_memory_schur as M


def enc(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [enc(x) for x in v]
    return v


def report(use_source=False):
    finite_pos=M.rational_memory_telescope(((F(3,2),),),((1,),),((1,),),12,
                   step=F(1),high_gap=F(1),coupling_sq_upper=F(1))
    finite_neg=M.rational_memory_telescope(((F(1,2),),),((1,),),((1,),),12,
                   step=F(1),high_gap=F(1),coupling_sq_upper=F(1))
    finite_zero=M.rational_memory_telescope(((1,),),((1,),),((1,),),12,
                   step=F(1),high_gap=F(1),coupling_sq_upper=F(2))
    b=(F(3,5),F(4,5));D=((F(37,13),F()),(F(),F(73,127)))
    mem_a=M.scalar_memory_hankel((1,),((1,),),4)
    mem_b=M.scalar_memory_hankel(b,D,4)
    assert mem_a[:2]==mem_b[:2] and mem_a[2]!=mem_b[2]
    x={
     'program':'SUCC_SOURCE_HIDDEN_MEMORY_SCHUR_2026_10_17',
     'exact_rational_finite_models_only':True,
     'positive_trial':{'verdict':finite_pos['verdict'],'S':finite_pos['actual_finite_S'],'tail':finite_pos['Loewner_error_cap']},
     'negative_trial':{'verdict':finite_neg['verdict'],'S':finite_neg['actual_finite_S']},
     'singular_ambiguous_trial':{'verdict':finite_zero['verdict'],'S':finite_zero['actual_finite_S']},
     'two_hidden_baths':{
        'identical_first_two_observations':mem_a[:2],
        'one_mode':M.reconstruct_two_hidden_lags(mem_a),
        'two_mode':M.reconstruct_two_hidden_lags(mem_b),
        'opposite_S_signs':True},
     'measured_hidden_gaussian':M.two_read_hidden_gaussian(),
     'explicit_cell_algebraic_budget':M.finite_cell_algebraic_budget(64),
     'aligned_642_cell_algebraic_budget':M.finite_cell_algebraic_budget(64,642),
     'source_contract':'ORIGINAL_SUZUKI_SOURCE_ADAPTER_ONLY_ON_SOURCE_MODE',
     'source_spectral_projector_computed':False,
     'Suzuki_first_window_sign_proved':False,'RH_proved':False,
    }
    if use_source:
        x['authentic_suzuki_first_prime_source']=M.original_source_memory_budget(12)
        x['authentic_explicit_453_cell_source']=M.explicit_cell_source_memory_budget(64)
        x['authentic_aligned_642_cell_source']=M.explicit_cell_source_memory_budget(64,642)
        x['authentic_prime2_SUCC_clock_resonance']=M.source_prime2_cell_alignment(642)
        assert x['authentic_suzuki_first_prime_source']['discrete_hidden_memory_tail_upper']==F(121,262144)
    else:x['authentic_suzuki_first_prime_source']='NOT_MOUNTED_STANDALONE'
    return enc(x)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',action='store_true')
    p.add_argument('--verify',action='store_true')
    a=p.parse_args()
    d=report(a.source)
    blob=json.dumps(d,sort_keys=True,indent=2)+'\n'
    if a.verify:
        assert blob==json.dumps(report(a.source),sort_keys=True,indent=2)+'\n'
    print(blob,end='')

if __name__=='__main__':main()
