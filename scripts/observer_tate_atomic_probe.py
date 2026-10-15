"""Reproducible ATOM: exact model->model duality, Tate local Fourier, Weil sign boundary."""
from __future__ import annotations
import json
from fractions import Fraction as F

from observational_succ.tate_observer_completion import (
    integer_source_prefix, profinite_ghost_prefix,
    normal_fourier_naturality, PadicBruhatChart,
    tate_local_inversion_and_parseval, refine_local_precision,
    refine_local_support,local_padic_real_boundary_no_go,
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
    report={
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
