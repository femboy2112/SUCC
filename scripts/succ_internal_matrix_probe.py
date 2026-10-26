#!/usr/bin/env python3
"""Exact SUCC BBP internal Fourier matrix / Pascal / Walsh / band-limit receipt.

JSON reports exact rational expressions as strings or exact symbolic metadata.
Optional complex evaluations are explicit NUMERICAL DIAGNOSTICS, not intervals.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q

from observational_succ.succ_internal_matrix_walk import (
    MatrixWalk,PhasePoly,authentic_r,gram_spectral_certificate,
    geometric_frequency_gram,finite_koopman_phases,phase_plaquette,
    frequency_boundary_witness,temporal_derivative_boundary,
    signed_source_difference,exact_source_digits,walsh_digit_energy,
)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',action='store_true',help='check all exact finite source/Gram/energy identities')
    parser.add_argument('--horizon',type=int,default=12)
    parser.add_argument('--width',type=int,default=4)
    args=parser.parse_args()
    state=MatrixWalk.initial(args.width)
    for _ in range(args.horizon):state=state.succ()
    proof=gram_spectral_certificate(state)
    if args.horizon:
        fejer,next_purity=state.innovation()
        geometric=geometric_frequency_gram(state)
        walsh=walsh_digit_energy(exact_source_digits(state.history))
    else:
        raise ValueError('horizon must be positive')
    phase=finite_koopman_phases(11,1,8)
    band=frequency_boundary_witness(5)
    drift=temporal_derivative_boundary(4)
    if args.verify:
        assert state.validate()
        assert next_purity==state.succ().purity()
        assert proof['spectral_purity']-args.width==proof['offdiagonal_excess']
        assert proof['zero_mode']==PhasePoly.one()
        assert proof['normality_proved'] is False
        assert geometric[0][0]==PhasePoly.monomial(0,args.horizon)
        assert all((a-b)%1==0 for a,b in zip(phase['diagonal_gauge'][1:],
                                             (phase['diagonal_gauge'][k]+phase['phases'][k]
                                              for k in range(len(phase['phases'])))))
        assert walsh['spectral_energy']==walsh['collision_energy']
        assert signed_source_difference(11,1,3)<0
        assert phase_plaquette(11,3)==15*signed_source_difference(11,1,3)
        assert 0<band['positive_error']<band['error_cap']
        assert 0<drift['positive_error']<drift['error_cap']
        for n in range(1,41):
            combined=Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            assert authentic_r(n)==combined
    p=proof['spectral_purity'].evaluation(70)
    q=fejer.evaluation(70)
    print(json.dumps({
        'source':'Q:Coherent-Main-X-four-pole-BBP',
        'local_verification':'passed' if args.verify else 'not_requested',
        'single_external_succ':'n -> n+1',
        'matrix_width':args.width,'observations':args.horizon,
        'source_phase_field':'formal Q[Q/Z], optional cyclotomic quotient',
        'last_rational_state_mod_one':str(state.lifted_state-state.lifted_state.numerator//state.lifted_state.denominator),
        'gram_diagonal_exact':str(proof['N']),
        'purity_equals_weighted_weyl_excess_exact':True,
        'spectral_purity_diagnostic':str(p.real),
        'fejer_innovation_diagnostic':str(q.real),
        'next_step_purity_identity_verified_exact':next_purity==state.succ().purity(),
        'walsh_exact_collision_energy':str(walsh['collision_energy']),
        'walsh_highest_order_four_bit':str(walsh['highest_joint_bit_amplitude']),
        'frequency_time_mixed_phase':str(phase_plaquette(11,3)),
        'source_critical_high_band':{k:str(v) for k,v in band.items()},
        'source_critical_temporal_band':{k:str(v) for k,v in drift.items()},
        'koopman_outgoing_channel_squared_norm':str(phase['finite_compression_boundary_squared_norm']),
        'pi_normality_proved':False,'RH_proved':False,
    },indent=2,sort_keys=True))


if __name__=='__main__':main()
