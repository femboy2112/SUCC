"""Reproduce finite SUCC observer duality, finite adelic quotient, Tate phase.

Outputs calibrated exact mathematical claims only. In particular no finite
sample certifies all continuous characters, full adelic Poisson summation,
physical-source access, or RH/Weil positivity.
"""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.edge_carrier_reconstruction import (
    ProfiniteProgram, finite_clock_collision
)
from observational_succ.finite_adele_localization import FiniteAdeleSpan
from observational_succ.pontryagin_source_duality import (
    RationalCircleCharacter, phase_separation,
    finite_character_orthogonality, wrong_dual_arrow_witness
)
from observational_succ.finite_adelic_character_bridge import (
    finite_adele_phase, quotient_receipt, quotient_additive_naturality,
    diagonal_rational_reciprocity, character_adele_pairing,
    annihilator_probe, finite_adelic_extension_non_split
)
from observational_succ.pontryagin_tate_atlas import three_way_tate_duality
from observational_succ.finite_cyclic_poisson import (
    finite_poisson_coset, exact_cyclic_annihilator,
    wrong_coset_phase_witness
)


def main() -> None:
    original=ProfiniteProgram.projector(2).add(ProfiniteProgram.projector(3))
    freq=RationalCircleCharacter(F(1,6))
    paired=character_adele_pairing(freq,original)
    chart=three_way_tate_duality(freq,original,extra_primes=(5,7))
    x=FiniteAdeleSpan(ProfiniteProgram.projector(2),6)
    y=FiniteAdeleSpan(ProfiniteProgram.projector(3),6)
    negative=wrong_coset_phase_witness()
    data=(F(2),F(-3,2),F(0),F(5,3),F(-7),F(4))
    poisson=finite_poisson_coset(data,3,1)
    result={
        "benchmark":"SUCC local-to-global Pontryagin duality, finite adeles, Tate",
        "source_status":"DECLARED_MATHEMATICAL_ORIGINAL_SOURCE_NOT_PHYSICAL",
        "finite_character":{
            "modular_dual":finite_character_orthogonality(6,1),
            "phase_at_source":freq.evaluate(original),
            "stage_bidirection":phase_separation(original,6),
            "wrong_dual_arrow":wrong_dual_arrow_witness(),
            "finite_horizon_collision":finite_clock_collision(9),
        },
        "finite_adele_quotient":{
            "prime2_fraction":quotient_receipt(x),
            "prime3_fraction":quotient_receipt(y),
            "sum":quotient_additive_naturality(x,y),
            "source_diagonal":diagonal_rational_reciprocity(F(1,6)),
            "non_integral_annihilator_witness":annihilator_probe(x),
            "nonsplit":finite_adelic_extension_non_split(6),
        },
        "tate_transport":{
            "finite_adele_character":paired,
            "original_S_atlas":chart,
            "opposite_signs_cancel":(
                (paired["character_phase"]+chart["Tate_finite_negative_phase"])%1==0
            ),
        },
        "finite_poisson":{
            "source_coset":poisson,
            "annihilator":exact_cyclic_annihilator(6,3),
            "wrong_coset_phase":negative,
        },
        "claim_dependencies":{
            "finite_ab_lca_duality":"CLASSICAL_THEOREM_FINITE_PROBES_EXACT",
            "Zhat_dual_QmodZ":"CLASSICAL_TOPOLOGICAL_THEOREM_NOT_COMPUTED_FROM_SAMPLES",
            "finite_adele_quotient":"CLASSICAL_TOPOLOGICAL_THEOREM_EXACT_REPRESENTED_FRAGMENTS",
            "Tate_global_Poisson":"CLASSICAL_EXPLICIT_FORMULA_DEPENDENCY_NOT_REPROVED",
            "completed_Weil_sign":"RH_HARD_UNVERIFIED",
        },
        "Pontryagin_complete_from_finitely_many_samples":False,
        "adelic_Poisson_proved_here":False,
        "source_derived_Weil_PSD_proved":False,
        "RH_proved":False,
    }
    if not (paired["dual_Tate_square_commutes"] and
            chart["three_way_compatibility"] and
            result["tate_transport"]["opposite_signs_cancel"] and
            poisson["finite_poisson_exact"] and
            negative["sign_mutation_detected"] and
            result["finite_adele_quotient"]["nonsplit"]["exact_sequence_splits_as_groups"] is False):
        raise AssertionError("Finite source duality no-ghost gate failed")
    print(json.dumps(result,sort_keys=True,indent=2,default=str))


if __name__=="__main__":
    main()
