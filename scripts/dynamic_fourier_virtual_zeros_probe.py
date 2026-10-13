#!/usr/bin/env python3
"""Emit exact observer Fourier/virtual-zero source receipts, no zero search."""
import json
import sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from observational_succ.dynamic_fourier_tower import (
    exact_spectral_debt, verify_fourier_tower, observational_alias,
    claim_target_debt, disappearing_energy_unbounded_claim, source_update_descent)
from observational_succ.virtual_mellin_zeros import (
    model_completion_receipt, zero_class, positive_gaussian_mixture_mellin2,
    VirtualCompletionObserver, virtual_zero_parameter_threshold_report)


def main():
    fine=(1,0,-1,0)
    alias=observational_alias(fine,(0,)*4,2)
    hidden=exact_spectral_debt(fine,2)
    tower=verify_fourier_tower((1,0,0,0,0,0,0,0),
            (8,4,2),source_id='diagonal-Q-finite-cyclic',source_version=0,place_prime=2)
    candidate=VirtualCompletionObserver(F(0),F(1),'arch-source-unspecified',0)
    canonical=candidate.observe_exact_mellin2(F(1),source_id='arch-source-unspecified',source_version=0)
    nonstandard=candidate.observe_exact_mellin2(F(413,188),source_id='arch-source-unspecified',source_version=0)
    # A genuinely state-changing, invertible intervention can reveal old hidden modes.
    shear=[[F(int(i==j)) for j in range(4)] for i in range(4)]
    shear[0][2]=1
    def shift_matrix():
        return tuple(tuple(F(int(i == (j+1)%4)) for j in range(4)) for i in range(4))
    bad_update=source_update_descent(shear,2)
    good_update=source_update_descent(shift_matrix(),2)
    report={
        'source_update_descent_succ_shift':good_update,
        'source_update_descent_shear_counterexample':bad_update,
        'classification':'finite exact classical transport, conditional source model',
        'canonical_zeta_zeros_used_as_inputs':False,
        'rational_probability_and_algebra_only':True,
        'dft_refinement_square':hidden['exact_quotient_fourier']['all_character_squares_exact'],
        'alias_same_coarse_report':alias['same_coarse_report'],
        'alias_different_full_source':not alias['source_states_identical'],
        'alias_hidden_energy':hidden['unseen_spectral_debt'],
        'finite_tower_step_debts':tower['stage_debts'],
        'finite_tower_total_debt':tower['total_debt'],
        'finite_tower_exact_composition':tower['composition_square'],
        'coarse_observer_knows_debt_from_own_report':hidden['observer_can_know_debt_from_coarse_report_alone'],
        'original_claim_transport':claim_target_debt(fine,(1,0,-1,0),2),
        'small_source_large_claim_countermodel':disappearing_energy_unbounded_claim(100),
        'canonical_completion':model_completion_receipt(F(0)),
        'counterfactual_completion':model_completion_receipt(F(10,11)),
        'zero_regimes':{str(e):zero_class(e) for e in (F(0),F(1,2),F(4,5),F(10,11),F(1),F(2))},
        'strict_strip_no_extra_zero':virtual_zero_parameter_threshold_report(F(1,2))['proves_no_C_zeros_in_closed_strip_by_triangle'],
        'virtual_zeros_initially_possible':candidate.classify()['offcritical_strip_zero_possible_in_a_completion'],
        'virtual_zeros_after_canonical_probe':canonical.classify()['offcritical_strip_zero_possible_in_a_completion'],
        'virtual_zeros_after_noncanonical_probe':nonstandard.classify()['offcritical_strip_zero_forced_in_every_completion'],
        'gaussian_mixture_rigidity':positive_gaussian_mixture_mellin2(((1,1),(4,F(10,11)))),
        'full_adelic_fourier_or_RH_proved':False,
        'analytic_Hurwitz_lemma_proved_in_written_math_not_by_sampling':True,
    }
    assert report['alias_hidden_energy']==2
    assert good_update['coarse_dynamics_exists'] is True
    assert bad_update['coarse_dynamics_exists'] is False
    assert bad_update['obstruction_revealed_report'] == (F(1), F(0))
    assert report['finite_tower_step_debts']==(F(1,2),F(1,4))
    assert report['counterfactual_completion']['quadratic_t_constant_first']==(F(1),F(11,5),F(1))
    assert report['counterfactual_completion']['Mellin_C2']==F(413,188)
    assert report['virtual_zeros_initially_possible']
    assert not report['virtual_zeros_after_canonical_probe']
    assert report['virtual_zeros_after_noncanonical_probe']
    return report


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True,default=str))
