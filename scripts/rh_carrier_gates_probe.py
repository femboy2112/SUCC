"""One reproducible three-carrier RH frontier receipt, no zero-position inputs."""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.rh_arithmetic_carrier import low_carrier_prefix_receipt
from observational_succ.adelic_schwartz_source import DiagonalGaussianTensor
from observational_succ.tate_schwartz_functor import (
    local_euler_logjet, finite_source_logjets
)
from observational_succ.tate_weil_window import CompactWeilSourceWindow
from observational_succ.weil_gns_gate import calibration_pair


def main() -> None:
    low = low_carrier_prefix_receipt(12)
    obj = DiagonalGaussianTensor(F(6),F(1,5),F(9,4),"RH-triple-carrier",0)
    mid = obj.fourier_at_rational(F(1,6))
    jets = finite_source_logjets(27,2)
    source_window = CompactWeilSourceWindow(F(3,2)).certificate()
    signed = calibration_pair()
    if not (low["all_checked_finite_inequalities_certified"]
            and mid["global_phase"]==0 and mid["global_Haar_affine_scaling"]==1
            and jets["exact_original_von_Mangoldt_cross_oracle"]
            and source_window["strict_integer_cutoff"]==27
            and not signed["positivity_of_auxiliary_implies_original_Weil"]):
        raise AssertionError("RH carrier positive/negative baseline failed")

    print(json.dumps({
        "source": "AUTHENTIC_Q_DECLARED_NOT_PHYSICAL",
        "low_lagarias": low,
        "middle_tate_adeles": {
            "Gaussian_Fourier_lattice": mid,
            "local_Tate_logjet": local_euler_logjet(3,2,5),
            "source_identical_Weil_prime_powers": jets,
            "Weil_test_support": source_window,
        },
        "high_signed_Weil": signed,
        "low_to_middle_equivalence": "CLASSICAL_IMPORTED_RH_CRITERIA_NOT_A_DIRECT_FUNCTOR",
        "middle_to_high_identification": "CLASSICAL_WEIL_EXPLICIT_FORMULA_IMPORTED; SUCC_FUNCTOR_NOT_BUILT",
        "source_derived_all_test_positivity": "UNVERIFIED_RH_HARD",
        "minimum_carrier_unique": False,
        "maximum_carrier_unrestricted_exists": False,
        "conditional_Weil_GNS_exists_unconditionally": False,
        "RH_field_class": "UNRESOLVED_NOT_IDEALHARD_OR_FUCKED_PROVED",
        "RH_proved": False,
    },indent=2,sort_keys=True,default=str))


if __name__=="__main__":
    main()
