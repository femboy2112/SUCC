"""Reproducible exact source receipt for solved-problem SUCC carrier ladder."""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.edge_carrier_reconstruction import (
    NatLoop, IntegerLoop, RayPath, RationalSpan, SLocalization,
    GaussianInteger, GaussianRational, ProfiniteProgram,
    finite_prime_partition, finite_cyclic_yoneda, prime_projector_is_not_integer,
    finite_clock_collision, carrier_interface_contract,
)
from observational_succ.finite_adele_localization import (
    FiniteAdeleSpan, RationalArchimedeanAdeleChart,
    local_idempotent_is_a_nonrational_adele, finite_adele_nonfield_control,
)
from observational_succ.complex_cauchy_edge import (
    GaussianCauchyRoot2, sqrt2_is_not_gaussian_rational,
)


def main() -> None:
    source_nat=NatLoop(3).then(NatLoop(7))
    integers=IntegerLoop(5,12)
    rational=RationalSpan.from_edges(integers,NatLoop(14))
    atlas=SLocalization((2,7))
    gauss=GaussianInteger.from_pair(3,4)
    qi=GaussianRational.from_gaussian(gauss)
    sqrt2=GaussianCauchyRoot2(RationalSpan(1,3))
    idempotent=ProfiniteProgram.projector(2)
    adele=FiniteAdeleSpan(idempotent,2)
    ring=RationalArchimedeanAdeleChart.diagonal_rational(RationalSpan(2,3))

    checks={
        "one_vertex_free_loop_to_Z": {
            "n_successor_composition":source_nat.count,
            "inverted_loop_raw":(integers.forward,integers.backward),
            "signed_Z_winding":integers.winding,
            "cancelled_composition_is_identity":integers.then(integers.inverse()).winding==0,
            "ray_groupoid_aut_at_origin_trivial":
                not RayPath(0,(1,1,-1,-1)).nontrivial_based_loop_after_reduction,
            "finite_yoneda":finite_cyclic_yoneda(5),
        },
        "Z_to_Q_localization": {
            "rational_edge":rational.as_fraction(),
            "S_atlas":atlas.primes,
            "in_selected_S_integers":atlas.contains(rational),
            "outside_one_prime_stage":not SLocalization((7,)).contains(rational),
        },
        "Z_i_and_Q_i": {
            "gaussian_pair":gauss.pair, "gaussian_norm":gauss.norm(),
            "gaussian_in_Qi":qi.as_pair(),
            "complex_irrational_Cauchy":sqrt2.cauchy_receipt(24,8),
            "not_in_Qi":sqrt2_is_not_gaussian_rational(),
        },
        "finite_modular_edges_to_Zhat": {
            "e2_12":idempotent.residue(12),
            "e2_bonding_60_to_12":idempotent.bonding(60,12),
            "CRT_partition_at_60":finite_prime_partition(60),
            "properness":prime_projector_is_not_integer(2),
            "bounded_source_alias":finite_clock_collision(10),
        },
        "Zhat_to_Af_then_real_place": {
            "finite_adele_2_component":adele.local_integral_scaled(2,4),
            "finite_adele_3_component":adele.local_integral_scaled(3,4),
            "projector_outside_diagonal_Q":local_idempotent_is_a_nonrational_adele(2),
            "finite_adele_not_field":finite_adele_nonfield_control(2,3),
            "rational_archimedean_chart":ring.real,
            "complete_R_supplied_by_a_rational_coordinate":False,
        },
        "typed_interfaces":carrier_interface_contract(),
    }
    assert checks["one_vertex_free_loop_to_Z"]["cancelled_composition_is_identity"]
    assert checks["Z_to_Q_localization"]["in_selected_S_integers"]
    assert checks["Z_to_Q_localization"]["outside_one_prime_stage"]
    assert checks["Z_i_and_Q_i"]["gaussian_norm"]==25
    assert checks["finite_modular_edges_to_Zhat"]["e2_12"]==9
    assert checks["finite_modular_edges_to_Zhat"]["CRT_partition_at_60"]["sum_modulus"]==1
    assert not checks["Zhat_to_Af_then_real_place"]["finite_adele_not_field"]["finite_adeles_are_a_field"]
    print(json.dumps({
        "source":"DECLARED_ARITHMETIC_CARRIER",
        "proof_status":"CLASSICAL_THEOREMS_PLUS_EXACT_FINITE_SOURCE_MODELS",
        "checks":checks,
        "all_points_of_C_A_Zhat_executed":False,
        "all_physical_carriers_authenticated":False,
        "source_derived_complete_Weil_positivity":False,
        "RH_proved":False,
    },default=str,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
