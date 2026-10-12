#!/usr/bin/env python3
"""Exact source arithmetic + explicitly nonformal complex diagnostics."""
import json
from fractions import Fraction as F
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.diagonal_adele_zeta import (
    additive_reciprocity,multiplicative_reciprocity,DiagonalCarrier,
    bounded_height_injection,height_limited_source,finite_place_joint_limit_escape,
    local_euler_product,no_height_limit_alias)
from observational_succ.adelic_theta_completion import (
    completed_s2_interval,deleted_euler_factor_asymmetry,
    theta_poisson_diagnostic,lambda_theta_diagnostic)
from observational_succ.finite_fourier_carrier import fourier_covariance_receipt
from observational_succ.dual_place_verifier import DualPlaceProof,RationalClaim


def stringify(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):stringify(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [stringify(v) for v in x]
    return x


def main():
    q=F(1,6)
    dual=DualPlaceProof('diagonal Q','exact ring',1,3,{5:1,7:1})
    original=F(1,2)
    reports=tuple(dual.finite_observation(original,p,'finite climb') for p in (5,7))
    arch=(dual.real_observation(original,F(1,10),'arch circle'),)
    claim=RationalClaim('positive source',{v:'positive' if v>0 else 'nonpositive' for v in dual.sources})
    prod=local_euler_product(19,2)
    escape=finite_place_joint_limit_escape((5,7),4)
    z=completed_s2_interval(19,8)
    out={
        'source':'one diagonal rational Q with standard normalized finite and real places',
        'additive_reciprocity_one_sixth':additive_reciprocity(q),
        'multiplicative_reciprocity_one_sixth':multiplicative_reciprocity(q),
        'succ_fucc_square':DiagonalCarrier(q).commuting_square(1,6,{5:2,7:2}),
        'exact_finite_fourier':fourier_covariance_receipt((1,2,3,4,5),1,2,require_prime=True),
        'dual_observer_fiber_sizes':dual.cross_check(reports,arch),
        'dual_observer_proof':dual.conclude(reports+arch,claim),
        'bounded_height_injection':bounded_height_injection(3,{5:1,7:1}),
        'bounded_height_independent_search':height_limited_source(3,{5:1,7:1}),
        'unbounded_escape':escape,
        'unbounded_fixed_depth_alias':no_height_limit_alias({5:2,7:1},100),
        's2_euler':{k:v for k,v in prod.items() if k!='local_factors'},
        's2_arch_completed_exact_interval':z,
        'missing_true_prime_2_mutation':deleted_euler_factor_asymmetry(2,2),
        'theta_diagnostic_nonproof':theta_poisson_diagnostic('2',12,55),
        'lambda_theta_diagnostic_nonproof':lambda_theta_diagnostic('0.4+2.0j',9,55),
        'all_quantitative_exact_receipts_rational':True,
        'analytic_functional_equation_proved_in_code':False,
        'physical_entanglement_claimed':False,
        'gamma_forced_by_finite_prime_data':False,
        'rh_proved':False,
    }
    assert out['additive_reciprocity_one_sixth']['total_integer']==1
    assert out['multiplicative_reciprocity_one_sixth']['global_product']==1
    assert out['bounded_height_injection']['injective']
    assert out['unbounded_escape']['outside_prime_norm_product']==out['unbounded_escape']['diagonal_rational'].denominator
    assert out['dual_observer_proof']['status']=='PROVED'
    assert not out['rh_proved']
    print(json.dumps(stringify(out),indent=2,sort_keys=True))

if __name__=='__main__':main()
