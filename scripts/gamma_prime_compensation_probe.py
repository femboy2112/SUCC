"""Deterministic exact rational and optionally pinned original-source probe."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.gamma_edge_compensation import (
    rational_source_constant_control,proof_by_exact_harmonic_arithmetic,
    true_first_edge_packet,gamma_logarithmic_edge_lower,
    buffered_edge_bulk_gluing,countermodel_gluing,source_authenticated_compensation,
)
from observational_succ.gamma_prime_phase_lock import phase_lock,source_verified_phase_lock
from observational_succ.gamma_carleman_gluing import (
    gamma_ou_dirichlet_channel,touching_carleman_moment_witness,
    dyadic_gamma_edge_lower,touching_source_gluing_gate)


def serialize(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):serialize(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [serialize(x) for x in v]
    return v


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--source',action='store_true',help='REQUIRE frozen original source gates, fail without SUCC')
    args=parser.parse_args()
    packet={'status':'PAPER_DERIVED_LOCAL_SOURCE_CONDITIONAL',
            'source_constants_independent_rational':rational_source_constant_control(),
            'gamma_sixteen_mode_exact':proof_by_exact_harmonic_arithmetic(),
            'first_edge_delta_1_32':true_first_edge_packet(Q(1,32)),
            'gamma_growth_sample':gamma_logarithmic_edge_lower(Q(1,128)),
            'phase_lock_prime_2_j_3':phase_lock(2,3),
            'phase_lock_prime_square_4_j_3':phase_lock(4,3),
            'gluing_example_conditional':buffered_edge_bulk_gluing(Q(1,4096),Q(1,16),Q(1,4),Q(1)),
            'Gamma_dirichlet_rung_j3':gamma_ou_dirichlet_channel(3),
            'touching_Carleman_Q4_limiting_witness':touching_carleman_moment_witness(4),
            'dyadic_four_billion_modes_compressed':dyadic_gamma_edge_lower(Q(1,2**36)),
            'zero_gap_gluing_conditional_bulk_example':touching_source_gluing_gate(Q(1,2**36),Q(1,4),Q(1,2)),
            'no_ghost_negative_gluing':countermodel_gluing(),
            'authentic_source_installed':False,
            'whole_operator_positive':False,'first_window_S4_sign':'OPEN','RH_proved':False}
    if args.source:
        packet['original_source_compensation']=source_authenticated_compensation()
        packet['original_source_phase_lock']=source_verified_phase_lock(4,3)
        packet['authentic_source_installed']=True
    if args.verify:
        c=packet['source_constants_independent_rational']
        assert c['combined_upper']<Q(47,8)
        assert packet['gamma_sixteen_mode_exact']['uniform_K_margin_lower']>Q(11,128)
        assert packet['first_edge_delta_1_32']['total_K_relative_lower']>Q(11,128)
        assert packet['no_ghost_negative_gluing']['negative_joint_energy']==-2
        assert packet['phase_lock_prime_square_4_j_3']['resulting_exact_rational_log_p_multiplier']==Q(1,4**7)
        assert packet['zero_gap_gluing_conditional_bulk_example']['strict_gluing_condition'] is True
        assert packet['zero_gap_gluing_conditional_bulk_example']['source_bulk_margin_proved'] is False
        assert packet['touching_Carleman_Q4_limiting_witness']['positive_carlemann_half_limit_greater_than']>0
        if args.source:
            assert packet['original_source_compensation']['source_checked'] is True
            assert packet['original_source_phase_lock']['source_verified'] is True
    print(json.dumps(serialize(packet),sort_keys=True,indent=2))

if __name__=='__main__':main()
