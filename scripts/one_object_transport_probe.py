"""Reproducible exact and calibrated ONE OBJECT receipt; no RH claims."""
from __future__ import annotations

import json
from fractions import Fraction as F
from observational_succ.one_object_kernel_certificates import source_two_point_minor
from observational_succ.one_object_transport import (
    contact_rational_increment,contact_tail_majorant,
    screw_uniform_tail_majorant,original_prime_atoms,
    stage_identity_bump,analytic_shift_no_go,
    connes_trace_stabilization,anchored_kernel
)


def main():
    J=8
    tail=contact_tail_majorant(J)
    bound=screw_uniform_tail_majorant(J,F(2))
    source=original_prime_atoms(2)
    clean=stage_identity_bump(F(2),4,60)
    mutated=stage_identity_bump(F(2),4,60,F(1,3))
    fake=analytic_shift_no_go(F(2),F(1),F(7))
    connes=connes_trace_stabilization(3,10,6)
    assert [n for n,_ in source]==[2,3,4,5,7]
    assert tail>0 and bound>tail
    assert clean["residual_abs"]<__import__("mpmath").mpf("1e-48")
    assert abs(mutated["residual_abs"]-F(1,3))<__import__("mpmath").mpf("1e-44")
    assert fake["gram_diagonal"]==-14
    assert connes["traces"]==(3,9,9,9,9,9)
    g=lambda t:-t*t
    assert anchored_kernel(g,F(2),F(3))==12
    minor=source_two_point_minor(F(1,4),F(1,2),128)
    assert minor["verdict"]=="PROVED_FINITE_SOURCE_POSITIVE"
    low=minor["determinant"][0]
    floor_1e6=F(low.numerator*10**6//low.denominator,10**6)
    result={
      "authentic_Suzuki_2x2_points":["1/4","1/2"],
      "authentic_Suzuki_strict_positive_2x2":True,
      "authentic_Suzuki_determinant_lower_floor_1e6":str(floor_1e6),
      "authentic_Suzuki_provenance":"SHA_PINNED_ORIGINAL_SIGNED_ZETA",
      "kind":"ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES",
      "parent_tate_head":"940f0a47ef25b8b553c2f0b45032b37e68c23b02",
      "source_zeta_genuine_prime_powers":list(source),
      "contact_increment_J8":str(contact_rational_increment(J)),
      "contact_tail_fraction":str(tail),
      "screw_uniform_error_on_minus2_to_2":str(bound),
      "bump_independent_weil_suzuki_residual":clean["residual"],
      "wrong_contact_defect_expected":"1/3",
      "wrong_contact_observed":mutated["residual"],
      "fake_nonEuler_gram_diagonal":str(fake["gram_diagonal"]),
      "connes_p3_u10_clock_traces":list(connes["traces"]),
      "connes_stabilized_local_factor":connes["stabilized_local_factor"],
      "algebraic_positive_rank1_control":True,
      "all_test_positive_kernel_constructed":False,
      "global_connes_distribution_identified":False,
      "RH_PROVED":False,
      "status":{
        "contact_equality":"CLASSICAL_DISTRIBUTION_IDENTITY_SOURCE_MARRIED_FINITE_STAGE",
        "local_clock_trace":"CLASSICAL_PROVED_LOCAL",
        "bump_comparisons":"NUMERICAL_CALIBRATION_NOT_RIGOROUS_INTERVAL",
        "Suzuki_Hilbert_feature":"UNVERIFIED"
      }
    }
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
