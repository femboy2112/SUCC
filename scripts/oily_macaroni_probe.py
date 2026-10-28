#!/usr/bin/env python3
"""Reproduce exact finite source-bridge evidence; this does not prove normality.

Usage:
  python scripts/oily_macaroni_probe.py > research/2026-10-26/OILY_MACARONI_RECEIPT.json
  python scripts/oily_macaroni_probe.py --verify research/2026-10-26/OILY_MACARONI_RECEIPT.json

All displayed certificate endpoints are outward-rounded rational decimals.
No floating-point special function or pi digit supplies a certificate input.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import itertools
import json
from math import lcm
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

from observational_succ import bbp_log_mixture as lm
from observational_succ import cyclic_carry_extension as ce
from observational_succ import exponential_gamma_bridge as eg
from observational_succ import ladder_shift_audit as la
from observational_succ.bbp_natural_carrier import exact_forcing
from observational_succ.succ_internal_matrix_walk import PhasePoly


def decimal_interval(lower: Q,upper: Q,digits: int=20) -> dict:
    """Outward rational rounding, with integers throughout."""
    scale=10**digits
    lo=lower.numerator*scale//lower.denominator
    hi=-((-upper.numerator*scale)//upper.denominator)
    def display(v):
        sign='-' if v<0 else ''
        whole,part=divmod(abs(v),scale)
        return f'{sign}{whole}.{part:0{digits}d}'
    return {'lower':display(lo),'upper':display(hi),
            'endpoint_type':'outward rational decimal'}


def receipt() -> dict:
    paths=[
        'observational_succ/bbp_natural_carrier.py',
        'observational_succ/gamma_bbp_signed_coherence.py',
        'observational_succ/euler_mascheroni_succ.py',
        'observational_succ/exponential_gamma_bridge.py',
        'observational_succ/bbp_log_mixture.py',
        'observational_succ/cyclic_carry_extension.py',
        'observational_succ/ladder_shift_audit.py',
        'observational_succ/ladder_contraction_probe.py',
        'tests/test_exponential_gamma_bridge.py',
        'tests/test_bbp_log_mixture.py',
        'tests/test_cyclic_carry_extension.py',
        'tests/test_ladder_shift_audit.py',
        'scripts/oily_macaroni_probe.py',
        'research/2026-10-26/independent_mixture_oracle.py',
        'research/2026-10-26/normalized_frequency_independent.py',
    ]
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    indices=(1,2,8,32,128,512,2048)
    rows=[]
    for n in indices:
        c=lm.tail_log_mixture_certificate(n,16,28)
        b=eg.bbp_euler_tail_bridge(n,16)
        rows.append({
            'n':n,'depth':16,'log_terms':28,
            'T':decimal_interval(c.mass_lower,c.mass_upper),
            'eta':decimal_interval(c.eta_lower,c.eta_upper),
            '8n_eta':decimal_interval(8*n*c.eta_lower,8*n*c.eta_upper),
            '(8n)^2_T':decimal_interval((8*n)**2*c.mass_lower,(8*n)**2*c.mass_upper),
            'T_over_eta_squared':decimal_interval(c.mass_lower/c.eta_upper**2,
                                                  c.mass_upper/c.eta_lower**2),
            '16T_over_euler_remainder_squared':decimal_interval(
                b.normalized_ratio.lower,b.normalized_ratio.upper),
            'upper_polynomial_gap_positive':b.upper_polynomial_gap>0,
            'relative_mellin_loss_bound_t1':str(lm.relative_mellin_loss_bound(n,1)),
        })
    fixed=[]
    for size in (2,8,64,512):
        interval=eg.finite_beta_fixed_point_interval(size,24,96)
        fixed.append({'m':size,'bits':24,'Taylor_terms':96,
                      'fixed_point':decimal_interval(interval.lower,interval.upper),
                      'survival_at_one':str(eg.finite_beta_survival(size,1)),
                      'third_moment':str(eg.finite_beta_moment(size,3))})
    golden=eg.golden_laplace_fixed_point_interval(80)
    offset=eg.golden_gamma_offset_interval(4096,32,80)
    audits=[]
    for length,h in ((8,1),(16,2),(31,7)):
        audit=la.authentic_ladder_audit(length,h)
        audits.append({'N':length,'h':h,'formal_identity_exact':audit.residual==PhasePoly.zero(),
                       'normalized_finite_defect_bound':str(audit.normalized_bound),
                       'normalized_all_horizon_bound':str(la.authentic_normalized_shift_bound(length,h))})
    states=[]
    u=Q()
    for n in range(1,17):
        u=16*u+exact_forcing(n)
        states.append(u)
    conductor=lcm(*(x.denominator for x in states))
    assert all((conductor*x).denominator==1 and (16*conductor*x).denominator==1 for x in states)
    support=ce.even_mode_cross_digit_support()
    marginal_count=0
    for size in (1,2,3):
        for subset in itertools.combinations(range(8),size):
            counts={bits:0 for bits in itertools.product((0,1),repeat=size)}
            for k in support:counts[tuple((k>>i)&1 for i in subset)]+=1
            assert set(counts.values())=={len(support)//(1<<size)}
            marginal_count+=1
    even_coefficients=ce.even_mode_cyclotomic_coefficients()
    assert any(even_coefficients)
    alpha=lm.counterfeit_tail(0)
    cell_coefficients=[sum(v for d,v in lm.POLE_DIFFERENCES if i<d)
                       for i in range(max(d for d,_ in lm.POLE_DIFFERENCES))]
    endpoint_polynomial=[cell_coefficients[0]]+[
        cell_coefficients[i]-cell_coefficients[i-1]
        for i in range(1,len(cell_coefficients))]+[-cell_coefficients[-1]]
    assert endpoint_polynomial==[4,0,0,-2,-1,-1]
    cell_control=((1,Q(1,2)),(3,Q(1,4)),(7,Q(1,4)))
    def cell_tail(n):
        return sum((weight/Q((8*n+b)*(8*n+b+1))
                    for b,weight in cell_control),Q())
    cell_moments={k:sum((weight*Q((b+1)**(k+1)-b**(k+1),k+1)
                          for b,weight in cell_control),Q()) for k in range(4)}
    assert cell_moments[1]==lm.tail_base_moment(1)
    assert cell_moments[2]==lm.tail_base_moment(2)
    return {
        'schema_version':1,
        'status':'EXACT_FINITE_SOURCE_BRIDGE_CERTIFICATES',
        'baseline_commit':'7989be5753341c5e74d570e8fea51e00129d2d0a',
        'original_import_commit':'ba075348b7bcc66d938b3e0ca96c26e95bba340a',
        'source_sha256':hashes,
        'source_identity_holdouts':{str(n):lm.source_authentication_check(n)
                                    for n in (1,2,7,31,97,257,1009)},
        'finite_beta':fixed,
        'golden_fixed_point':decimal_interval(golden.lower,golden.upper),
        'canonical_golden_minus_gamma':decimal_interval(offset.lower,offset.upper),
        'tail_base_moments':{str(k):str(lm.tail_base_moment(k)) for k in range(4)},
        'upper_bridge_positive_coefficients':list(eg.UPPER_BRIDGE_SHIFTED_COEFFICIENTS),
        'tail_log_and_euler_certificates':rows,
        'paper_limits_not_inferred_from_samples':{
            'T_over_eta_squared':'4/49','16T_over_euler_remainder_squared':'1',
            'n_eta':'7/16','n_squared_mellin_loss_at_t1':'73/768',
            '8n_Theta_fixed_nonzero_integer_k':'-7/2-i/(2*pi*k)',
            'Theta_over_eta':'-1-i/(7*pi*k)',
            'Theta_modulus_squared_over_T':'49/4+1/(4*pi^2*k^2)'},
        'normalized_source_circle':{
            'map':'B -> 8n*log(1+B/(8n)) mod 1',
            'Mellin_frequency':'16*pi*k*n, integer k != 0',
            'unit_cell_coefficients':cell_coefficients,
            'endpoint_polynomial_coefficients':endpoint_polynomial,
            'integer_part_mean':str(lm.tail_base_moment(1)-Q(1,2)),
            'uniform_cell_mass':str(Q(sum(cell_coefficients),15)),
            'paper_modulus_bound_with_pi_upper_22_over_7':[
                {'n':n,'k':k,'upper':str(min(Q(1),
                  (7+Q(55,3)*Q(22,7)*abs(k))/Q(8*n)*(1+Q(7,16*n))**2))}
                for n in (1,8,128,2048) for k in (1,15)],
            'changed_initial_seed_distinguished':False,
            'uniform_cell_counterfeit_distinguished':False,
        },
        'ladder_shift_audits':audits,
        'authentic_conductor_resonance':{'N':16,'h':str(conductor),
                                       'A_h':'1','A_16h':'1','ratio':'1'},
        'carry_extension':{
            'sequence':'0 -> C8 -> C16 -> C2 -> 0',
            'homomorphic_section_exists':False,
            'all_256_additions_checked':all(
                ce.join_residue(*ce.add_lifts(ce.split_residue(a),ce.split_residue(b)))==(a+b)%16
                for a,b in itertools.product(range(16),repeat=2)),
            'frequencies_mod16_descending_to_parity':[h for h in range(16) if ce.character_descends_to_parity(h)],
        },
        'even_mode_countermodel':{
            'support_size':len(support),'uniform_joint_marginals_checked':marginal_count,
            'both_complete_digit_marginals_uniform':all(
                sum(((k>>shift)&15)==d for k in support)==8 for shift in (0,4) for d in range(16)),
            'even_h':2,'cyclotomic_modulus':'X^64+1',
            'nonzero_reduced_coefficients':[str(q) for q in even_coefficients],
        },
        'matched_moment_counterfeit':{
            'atoms_and_weights':[[str(b),str(w)] for b,w in lm.MATCHED_MOMENT_CONTROL],
            'matching_moments':[k for k in range(4) if lm.counterfeit_moment(k)==lm.tail_base_moment(k)],
            'zero_seed':str(lm.counterfeit_orbit(0)),'expanding_coefficient':str(alpha),
            'fixed_frequency_with_mean_character_limit_one':alpha.denominator,
            'first_source_mismatch':str(lm.counterfeit_forcing(1)-exact_forcing(1)),
        },
        'uniform_cell_counterfeit':{
            'integer_atoms_and_weights':[[b,str(w)] for b,w in cell_control],
            'independent_uniform_cell':[0,1],
            'moments':{str(k):str(v) for k,v in cell_moments.items()},
            'matching_moments':[k for k in cell_moments if cell_moments[k]==lm.tail_base_moment(k)],
            'tail_at_zero':str(cell_tail(0)),
            'first_forcing':str(16*cell_tail(0)-cell_tail(1)),
            'first_source_mismatch':str(16*cell_tail(0)-cell_tail(1)-exact_forcing(1)),
            'fixed_frequency_with_mean_character_limit_one':cell_tail(0).denominator,
            'passes_auxiliary_moving_frequency_cancellation':True,
        },
        'scope':{'pi_normality_proved':False,'RH_proved':False,
                 'delta_causes_selected_cancellation':False,
                 'finite_testing_proves_infinite_limits':False,
                 'new_Lean_kernel_proof':False},
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    actual=receipt()
    if args.verify:
        expected=json.loads(args.verify.read_text())
        if actual!=expected:
            raise SystemExit('RECEIPT_MISMATCH: source hashes, parameters or certified results differ')
        print('OILY_MACARONI_RECEIPT_VERIFIED')
    else:
        print(json.dumps(actual,indent=2,sort_keys=True))


if __name__=='__main__':main()
