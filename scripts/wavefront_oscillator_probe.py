"""Deterministic research receipt for Oily completion and pumped oscillator."""
from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path

from observational_succ.wavefront_oscillator_completion import (
    BBP_TAPS, SourceGeometry, kernel_hankel_determinant,
    stationary_oily_source, stationary_oily_state, packet_matrix_coefficient,
    partial_oily_source, raw_packet_tail, certified_uniform_raw_tail_bound,
    periodic_response, critical_transient_bound, two_stage_high_frequency_condition,
    minimum_registers_oily, normalized_chiral_period_radical2,
    normalized_chiral_periodic_response, sizebiased_emitter_rates,
    maximum_entropy_two_bit_emitter, decode_source_two_steps,
    mean_wavefront_delay, signed_observer_prefix_defect,
    certified_prefix_defect_bound,
)
from observational_succ.wavefront_oracle_two_stage import run_two_stages


def fs(x):return str(x)

def main():
    x=F(1)
    w=tuple(BBP_TAPS*3)
    e1,e2=run_two_stages(w+tuple(F(0) for _ in range(3)),x)
    recovered=decode_source_two_steps(e2,x)
    assert tuple(recovered[:len(w)])==w
    raw_x=F(1,2)
    N=16
    source=stationary_oily_source(raw_x)
    finite=partial_oily_source(raw_x,N)
    rem=raw_packet_tail(raw_x,N)
    assert 0<=rem<=certified_uniform_raw_tail_bound(raw_x,N)
    cycle,seed=periodic_response(x)
    assert critical_transient_bound(8)==F(9,256)
    assert minimum_registers_oily(x)==2
    assert kernel_hankel_determinant(x)==F(-1,64)
    assert sizebiased_emitter_rates(x)==(F(1,2),F(1,2))
    assert maximum_entropy_two_bit_emitter(x)==(F(1,4),)*4
    report={
       'source_baseline':'Main XIII, original four-pole signed BBP source and Oily normalized two loops',
       'scope':'Research-only exact Fraction finite-recurrence and source-preserving positive identity; no physical source/observer optimality or pi-normality',
       'test_x':'1/2', 'source_R':fs(source),'source_R_partial_N16':fs(finite),'tail_actual':fs(rem),'tail_certified_bound':fs(certified_uniform_raw_tail_bound(raw_x,N)),
       'endpoint_hankel_determinant':fs(kernel_hankel_determinant(x)),
       'endpoint_minimal_registers':minimum_registers_oily(x),
       'critical_A8_inf_norm':fs(critical_transient_bound(8)),
       'critical_decoder_noise_gain':fs(two_stage_high_frequency_condition(x)),
       'original_signed_shell':[fs(z) for z in BBP_TAPS],
       'pumped_period8_cycle':[[fs(z) for z in s] for s in cycle],
       'normalized_source_radical2_taps':[[fs(a),fs(b)] for a,b in normalized_chiral_period_radical2()],
       'normalized_source_radical2_cycle':[[[fs(x) for x in component] for component in state] for state in normalized_chiral_periodic_response(x)],
       'full_received_source_reconstruction':True,
       'critical_mean_wavefront_delay':fs(mean_wavefront_delay(1)),
       'source_selected_weyl_observer_prefix_bound_for_unit_modulus':'4 for every N (classical proven inequality)',
       'constant_signal_prefix_defect_n256':fs(signed_observer_prefix_defect([F(1)]*256,1)),
       'constant_signal_prefix_certified_bound':fs(certified_prefix_defect_bound(1,1)),
       'maxent_two_bit_mean1_law':[fs(z) for z in maximum_entropy_two_bit_emitter(x)],
       'maxent_palm_rates':[fs(z) for z in sizebiased_emitter_rates(x)],
       'source_initial_condition':'Original BBP U0=0 is untouched and is NOT inferred from the oscillator.'
    }
    path=Path(__file__).resolve().parents[1]/'receipts'/'wavefront_oscillator_exact.json'
    path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(f'PASS exact-rational oscillator and inverse certificate -> {path}')

if __name__=='__main__':
    main()
