"""APOLLO original source prime-active DOMAIN certification, exact-only receipt.

The proof uses authentic SHA-pinned Weil/Suzuki source and inherited real
Gamma/Brownian Hilbert features. This executable certificate verifies exact
rational source inequalities, not an exhaustive test of all smooth functions.
"""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.apollo_prime_domain import (
    first_prime_sparse_domain, prime_two_pair_packet_domain,
    full_five_source_a_one_sparse_domain,
    any_five_prime_activation_pair, isolated_prime_sixteen_packet,
    source_support_union_gate, prime_packet_low_moment_rank,
    true_prime2_coupled_thirty_moment_witness,
    original_first_legendre_prime2_cross_witness,
    dyadic_gamma_4096_lower, exact_packet_overlap_bump, synthetic_sparse_budget,
)


def main():
    base=first_prime_sparse_domain()
    p2=prime_two_pair_packet_domain()
    five=full_five_source_a_one_sparse_domain()
    packets=[any_five_prime_activation_pair(n) for n in (2,3,4,5,7)]
    witness=exact_packet_overlap_bump(F(1,32768))
    negative=synthetic_sparse_budget(16,F(1,32),F(43,8),F(2),F(1,128))
    assert base.strict_rational_lower>F(1,10)
    assert p2["all_test_Q_over_L2_strict_rational_lower"]>F(3,5)
    assert five.strict_rational_lower>F(1,2)
    assert all(p["strict_exact_margin"]>5 for p in packets)
    assert witness["relative_prime_overlap"]==F(1,2)
    assert not negative["candidate_positive"] and not negative["original_source_authenticated"]
    packets16=[isolated_prime_sixteen_packet(n) for n in (2,3,4,5,7)]
    union=source_support_union_gate(F(1,2),(F(1,64),F(1,64)))
    low=prime_packet_low_moment_rank(2,30)
    assert all(p["strict_rational_margin"]>F(1,2) for p in packets16)
    assert union["all_cross_terms_covered_by_source_budget"]
    assert low["Legendre_1_to_rank_projection_of_u_i_fprime_surjective"]
    assert not low["original_Legendre_low_Schur_sign_proved"]
    high=true_prime2_coupled_thirty_moment_witness(34)
    assert high["vanishing_moments_0_to_29"]
    assert high["original_low_Legendre_1_to_30_zero"]
    assert high["genuine_prime2_translation_overlap"]>0
    low_cross=original_first_legendre_prime2_cross_witness(4)
    assert low_cross["low_cross_prime_component_exact_rational_positive_lower"]>0
    assert not low_cross["completed_signed_Weil_cross_sign_proved"]
    receipt={
      "PR107_first_low_prime_ONLY_cross_strictly_nonzero":True,
      "PR107_first_low_prime_ONLY_cross_rational_lower":str(low_cross["low_cross_prime_component_exact_rational_positive_lower"]),
      "PR107_first_low_completed_total_cross_sign_proved":False,
      "PR107_original_30_high_true_p2_interaction_nonzero":True,
      "PR107_exact_30_high_moment_null":True,
      "PR107_exact_high_packet_one_norm":str(high["one_packet_L2_squared"]),
      "PR107_exact_high_packet_prime_overlap_ratio":"1/2",
      "all_five_isolated_prime_packets_16_Gamma_modes":True,
      "all_five_isolated_prime_packet_measure_upper":"1/64",
      "all_five_isolated_prime_packet_strict_margins":[str(p["strict_rational_margin"]) for p in packets16],
      "all_five_isolated_prime_packet_L2_floor":"1/2",
      "first_prime_support_union_budget_pass":str(union["union_bound"]),
      "PR107_all_30_Legendre_low_moments_reachable_from_one_sparse_packet":True,
      "PR107_sparse_low_projection_has_bounded_inverse_certified":False,
      "operation":"APOLLO_PRIME_ACTIVE_SOURCE_DOMAINS",
      "parent_apollo_head":"cb7b804d8624dcf5247eac34cf59e969577c6ccb",
      "actual_source":"SHA_PINNED_ORIGINAL_ZETA_WEIL_GAMMA_PLUS_PRIME_JETS",
      "first_prime_halfwidth":"1/2",
      "first_prime_active":["2"],
      "first_prime_sparse_support_measure_at_most":"1/32",
      "first_prime_sparse_all_test_L2_floor":"1/10",
      "first_prime_exact_rational_lower":str(base.strict_rational_lower),
      "p2_two_translated_packet_L2_floor":"3/5",
      "p2_true_pair_lower":str(p2["all_test_Q_over_L2_strict_rational_lower"]),
      "p2_nonzero_source_transfer_possible":p2["nonzero_prime_transfer_possible"],
      "a_at_most_one_active_real_jets":[2,3,4,5,7],
      "all_five_sparse_support_measure_at_most":"1/16384",
      "all_five_sparse_L2_floor":"1/2",
      "all_five_exact_rational_margin_lower":str(five.strict_rational_lower),
      "source_4096_gamma_dyadic_rational_lower":str(dyadic_gamma_4096_lower()),
      "each_original_prime_packet_strict_L2_margin_greater_than_5":True,
      "each_original_prime_packet_labels":[p["active_prime_power"] for p in packets],
      "paired_exact_beta_overlap_ratio":str(witness["relative_prime_overlap"]),
      "PR107_interface":"u=i*fprime in L2_zero, <G u,u>=Q(f), <K u,u>=||f||2; K=Neumann inverse",
      "PR107_full_low_30x30_short_sign_proved":False,
      "all_original_source_G_a_positive_on_entire_L2_zero":False,
      "source_defined_Hilbert_contraction_on_each_fixed_small_measure_E":True,
      "unrestricted_suzuki_contraction_proved":False,
      "RH_PROVED":False,
    }
    print(json.dumps(receipt,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
