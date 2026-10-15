"""Reproducible ATOM: exact model->model duality, Tate local Fourier, Weil sign boundary."""
from __future__ import annotations
import json
from fractions import Fraction as F

from observational_succ.tate_observer_completion import (
    integer_source_prefix, profinite_ghost_prefix,
    normal_fourier_naturality, PadicBruhatChart,
    tate_local_inversion_and_parseval, refine_local_precision,
    refine_local_support,local_padic_real_boundary_no_go,
    exact_local_biaxial_diamond,exact_crt_product_fourier,
    crt_three_prime_fourier,diagonal_rational_additive_character,
)
from observational_succ.tate_adele_quotient_descent import (
    LocalFractionalAdeleCell, FiniteAdeleCoset, add_cosets,
    adele_solenoid_proof_contract,
)
from observational_succ.observer_global_sign_gate import (
    exact_scalar_schur_source_gate,unseen_sign_mutant,
    true_suzuki_anchored_two_point_source,dense_smooth_source_gate,
)


def main():
    integer=integer_source_prefix(17,4)
    ghost=profinite_ghost_prefix(4)
    assert integer.residues==(1,5,17,17)
    assert ghost.residues==(1,3,9,105)
    assert integer.moduli==ghost.moduli==(2,6,24,120)
    q=normal_fourier_naturality((2,-1,0,3,1,-2),24)
    c=PadicBruhatChart(2,1,1)
    raw=(1,0,-2,3)
    fft=tate_local_inversion_and_parseval(c,raw)
    precision=refine_local_precision(c,raw)
    support=refine_local_support(c,raw)
    bad=exact_scalar_schur_source_gate(1,2,1)
    singular=exact_scalar_schur_source_gate(0,1,1)
    hidden=unseen_sign_mutant(4)
    original=true_suzuki_anchored_two_point_source(F(1,4),F(1,2),128)
    boundary=local_padic_real_boundary_no_go()
    density=dense_smooth_source_gate()
    assert fft["Plancherel_on_original_local_source"]
    assert precision["finite_Fourier_naturality"] and support["finite_Fourier_naturality"]
    assert bad["status"]=="NEGATIVE_SCHUR_CROSS"
    assert singular["status"]=="ZERO_RANGE_CROSS_OBSTRUCTION"
    assert original["certified_finite_sign"]=="POSITIVE"
    assert not boundary["real_is_pure_finite_inverse_limit"]
    margin=original["determinant"][0]
    floor=F((margin.numerator*10**6)//margin.denominator,10**6)
    cube=exact_local_biaxial_diamond(c,raw)
    double=exact_crt_product_fourier(2,1,3,1,(1,-1),(2,0,-1))
    triple=crt_three_prime_fourier((
        (2,(1,-1)),(3,(2,0,-1)),(5,(1,0,2,-2,3))))
    phase=diagonal_rational_additive_character(1,6)
    assert cube["strict_source_diamond_commutes"] and cube["dual_Fourier_diamond_commutes"]
    assert double["naive_frequency_transport_disagreement_count"]>0
    assert triple["all_three_source_Fourier_tensor_square_commutes"]
    assert phase["total_global_phase_integer"]==1
    finite_adele=FiniteAdeleCoset((
        LocalFractionalAdeleCell(2,1,1),
        LocalFractionalAdeleCell(3,1,2),
    ))
    coset=finite_adele.check()
    solenoid=adele_solenoid_proof_contract()
    carry=add_cosets(FiniteAdeleCoset((LocalFractionalAdeleCell(2,1,1),)),
                     FiniteAdeleCoset((LocalFractionalAdeleCell(2,1,1),)))
    assert coset["constructive_diagonal_Q_lift"]=="7/6"
    assert coset["global_discrete_Q_mod_Z_class"]=="1/6"
    assert carry["result_Q_over_Z"]=="0"
    assert solenoid["adelic_quotient_compact"]
    report={
        "finite_adele_original_source_prime_places":[2,3],
        "finite_adele_constructive_rational_lift":coset["constructive_diagonal_Q_lift"],
        "finite_adele_quotient_Q_mod_Z":coset["global_discrete_Q_mod_Z_class"],
        "finite_adele_p2_carry_group_consistent":True,
        "finite_adele_strong_approximation":"CLASSICAL_PROVED",
        "real_profinite_solenoid_identifies_A_Q_mod_Q":"CLASSICAL_PROVED",
        "real_profinite_solenoid_compact":solenoid["adelic_quotient_compact"],
        "real_profinite_solenoid_global_Poisson_established":False,
        "local_support_precision_source_Fourier_cube":True,
        "CRT_two_prime_dual_transport_inverse_phase_detects_naive_error":True,
        "CRT_two_prime_naive_frequency_mismatches":double["naive_frequency_transport_disagreement_count"],
        "CRT_three_prime_global_modulus":triple["joint_observation_modulus"],
        "CRT_three_prime_exact_Fourier_tensor_all_frequencies":True,
        "Tate_rational_1over6_p_fractions":list(phase["prime_place_local_fractions"]),
        "Tate_rational_1over6_real_phase":str(phase["real_phase_exponent"]),
        "Tate_global_additive_character_product_equals_one":True,
        "Tate_diagonal_Poisson_unverified":True,
        "operation":"ATOM_OBSERVER_TATE_FINITE_TO_GLOBAL",
        "source_parent_main":"03db44203147a7b28d445bb9f970fa71360e78c4",
        "profinite_character_bijection":"CLASSICAL_PROVED_ON_COFINAL_ALL_STAGES",
        "finite_observer_algebra_moduli":list(integer.moduli),
        "integer_embedding_prefix":list(integer.residues),
        "noninteger_profinite_model_prefix":list(ghost.residues),
        "finite_model_of_model_source_attested":False,
        "CRT_noninteger_limit_has_finite_integer_prefix_witness":True,
        "Tate_padic_local_chart":[c.p,c.support_depth,c.precision_depth],
        "Tate_local_fourier_exact_involution":fft["Fourier_involution_reflection"],
        "Tate_local_fourier_exact_plancherel":fft["Plancherel_on_original_local_source"],
        "Tate_local_precision_refinement_commutes":precision["finite_Fourier_naturality"],
        "Tate_local_support_refinement_commutes":support["finite_Fourier_naturality"],
        "finite_residue_Fourier_modulus":q["new_modulus"],
        "finite_residue_Fourier_all_24_dual_frequencies":q["all_frequencies_checked"],
        "wrong_cross_term_sign_obstruction":bad["status"],
        "singular_old_stage_range_obstruction":singular["status"],
        "unseen_negative_stage_beyond_prefix":hidden["new_negative_at"],
        "authentic_signed_Suzuki_source_two_point_positive":True,
        "authentic_signed_Suzuki_2x2_determinant_floor_1e6":str(floor),
        "full_Tate_adelic_global_Poisson_constructed":False,
        "Archimedean_real_from_profinite_inverse_limit":False,
        "countable_dense_Weil_sign_test_equivalence":"CONDITIONAL_CLASSICAL_DENSITY",
        "coherent_Fourier_observers_imply_Weil_sign":False,
        "global_original_Weil_source_growth_PSD_proved":False,
        "RH_PROVED":False
    }
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
