"""Deterministic true zeta-source 30-mode infinite-Gamma enclosure receipt.

The finite-J original mixed derivative matrix is authentically sourced via
the immutable Suzuki source; this receipt does NOT build the missing pure
H1 derivative Gram or positive unshifted 30-low Schur.
"""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.suzuki_mixed30_gamma_tail import (
    gamma_mixed_spectral_tail,true_mixed_legendre_tail_bound,
    authentic_infinite_gamma_mixed_rows,
    completed_mixed_gamma_two_stage_intersection,
)


def main():
    low=authentic_infinite_gamma_mixed_rows(1,30,(1,))
    both=completed_mixed_gamma_two_stage_intersection(1,2,3,(1,))
    assert low.original_infinite_Gamma_integral_enclosed
    assert low.all_original_parity_zero_entries_retained
    assert both["all_true_entries_source_consistent"]
    assert not both["original_low_Schur_sign_proved"]
    assert gamma_mixed_spectral_tail(16)<gamma_mixed_spectral_tail(8)
    first=low.completed_matrix_enclosures[0][0]
    value={
        "operation":"TRUE_SUZUKI_30MODE_MIXED_GAMMA_TAIL",
        "original_source_blob":low.original_source_blob,
        "source":"SHA_PINNED_AUTHENTIC_COMPLETED_ZETA_SUZUKI",
        "original_true_low_mode":1,
        "complete_original_Legendre_dual_rows":30,
        "finite_Gamma_J":low.J,
        "source_first_mixed_completed_interval":[str(first.lo),str(first.hi)],
        "first_mode_J1_tight_error":str(true_mixed_legendre_tail_bound(1,1,1)),
        "all30_last_mode_J16_error":str(true_mixed_legendre_tail_bound(16,30,30)),
        "all30_last_mode_J64_error":str(true_mixed_legendre_tail_bound(64,30,30)),
        "error_decay":"RATIONAL_O(J^-2)_OU_SOURCE_INTEGRATION_BY_PARTS",
        "two_distinct_true_Gamma_source_stages_agree":True,
        "original_parity_zeros_exact":True,
        "true_completed_source_pure_H1_Gram_established":False,
        "original_unshifted_30_low_Schur_positive":False,
        "RH_PROVED":False,
    }
    print(json.dumps(value,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
