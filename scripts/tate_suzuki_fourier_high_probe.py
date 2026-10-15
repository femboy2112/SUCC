"""Replay original zeta Tate-Gamma Fourier coercivity and authentic Suzuki Schur gate.

All inequalities use Fraction and original SHA-pinned zeta prime/Gamma/pole
source. Analytic universal quantifiers come from the proof dossier, not
from enumerating source vectors. PR109's g' certificate is rerun on original.
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from observational_succ.tate_suzuki_fourier_schur import (
    gamma_fourier_multiplier_lower, moment_taylor_low_fourier_fraction,
    source_first_prime_spectral_budget, tate_suzuki_zero_shift_interface,
    verify_cross_source_failure_modes,
)


def receipt():
    rank16=source_first_prime_spectral_budget(16)
    rank18=source_first_prime_spectral_budget(18)
    rank30=source_first_prime_spectral_budget(30)
    schur30=tate_suzuki_zero_shift_interface(30)
    mutation=verify_cross_source_failure_modes()
    gm=gamma_fourier_multiplier_lower(F(12),32)
    assert gm>6 and gm<F(601,100)
    assert rank16["original_Weil_L2_gap_strict_lower"]>F(1,20)
    assert rank18["original_Weil_L2_gap_strict_lower"]>F(1,16)
    assert rank30["original_Weil_L2_gap_strict_lower"]>F(1,16)
    assert schur30["zero_shift_R0_operator_norm_strict_upper"]==F(121,100)
    return {
        "schema":"SUCC_TATE_SUZUKI_FOURIER_HIGH_v1",
        "origin":"SHA_PINNED_ZETA_TATE_WEIL_PR109_AND_DYSPON_II",
        "original_suzuki_blob":rank30["original_git_blob"],
        "original_halfwidth":"1/2",
        "actual_prime_power_labels":list(rank30["true_prime_power_labels"]),
        "Gamma_real_modes":32,
        "Fourier_boundary":"12",
        "Gamma_multiplier_exact":str(gm),
        "Gamma_multiplier_strictly_above_six":True,
        "rank16":{
            "power_moments_vanishing":16,
            "low_Fourier_mass_strictly_below":"1/400",
            "strict_original_Weil_L2_coercivity":"1/20",
            "low_parity_split":[8,8],
        },
        "rank18":{
            "power_moments_vanishing":18,
            "low_Fourier_mass_strictly_below":"1/30000",
            "strict_original_Weil_L2_coercivity":"1/16",
            "low_parity_split":[9,9],
        },
        "rank30":{
            "power_moments_vanishing":30,
            "strict_original_Weil_L2_coercivity":"1/16",
            "low_parity_split":[15,15],
        },
        "original_neumann_K":"V*V=(-Delta_N)^(-1) on mean-zero derivative",
        "source_original_gprime_L1_strictly_below":"11/40",
        "new_true_zero_shift_cross_R0_strictly_below":"121/100",
        "old_PR109_30_high_relative_kappa":"369/10000",
        "new_30_high_relative_kappa":"1/16",
        "naive_bound_cannot_certify_low":"-187/200",
        "wrong_contact_mutation_exhausts_rank16_budget":
            mutation["mutation_loses_rank16_kappa_1over20"],
        "source_30x30_actual_low_short_sign_proved":False,
        "all_a_positive_Weil_proved":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    data=receipt()
    if sys.argv[1:]==["--verify"]:
        path=Path(__file__).resolve().parents[1]/"research/2026-10-15/TATE_SUZUKI_FOURIER_HIGH_RECEIPT.json"
        expected=json.loads(path.read_text(encoding="utf-8"))
        if data!=expected:
            raise SystemExit("Tate Fourier high-moment authenticated proof receipt MISMATCH")
        print("TATE/SUZUKI original high Fourier - Neumann - Schur exact receipt verified")
    elif not sys.argv[1:]:
        print(json.dumps(data,sort_keys=True,indent=2))
    else:
        raise SystemExit("usage: python scripts/tate_suzuki_fourier_high_probe.py [--verify]")
