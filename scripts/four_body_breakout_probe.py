"""Probe: Four-Body Breakout (Moonshots A–E & Wave II Agents G–L).

Reproduces:
1. Moonshot A: Complete 4-moment quotient E^T P^{-1} E = L^T diag(1,3,5,7) L
   from authenticated interior channels c_1, c_2 and boundary-flux rows M_3, M_4.
2. Moonshot B: Certified derivative energy H'_{ij} = <h_i', h_j'> via real-space
   midpoint-Lipschitz integration (B1) + sharpened O(J^{-3/2}) polynomial-IBP
   Gamma tail (B3).
3. Moonshot C: Parity-split weighted Bessel high-sector coercivity
   kappa_odd = 63/500 = 0.126 (6.3x over 1/50),
   kappa_even = 153/500 = 0.306 (15.3x over 1/50).
4. Moonshot D: Exact negative-definiteness obstruction on the 30-mode middle block
   L_{30}|_{5..30} <= -(26191/14760) W_{L^2,5..30} < 0.
5. Moonshot E: Integrated CertifiedTrial and CertifiedDerivativeEnergyTrial
   showing 43.2x (odd) and 49.9x (even) S_4 lower-bracket tightening.
6. Wave II (Agents G–L): FUCC braid cocycle, off-line zero quadruplet signature (2,2)
   and kappa_4 = -4 Delta^2 gamma^2 aliasing, division-free LDL^T rational Schur
   capsule, observer interior/boundary synergy & cross-contact-gauge countermodel,
   Tate/Connes single-moment Neumann contact rigidity, and Hodge–Legendre cochain
   isomorphism.

Run:  PYTHONPATH=. python3 scripts/four_body_breakout_probe.py
"""
from __future__ import annotations

import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(50000)

from observational_succ.certified_four_schur_trial import (
    A_RADIUS,
    CertifiedDerivativeEnergyTrial,
    CertifiedTrial,
)
from observational_succ.four_schur_dual_quotient import (
    cross_contact_gauge_no_ghost_countermodel,
    hodge_legendre_endpoint_free_gram,
    observer_interior_boundary_synergy_certificate,
)
from observational_succ.four_thirty_schur_transport import (
    source_30mode_middle_block_obstruction_certificate,
)
from observational_succ.fucc_braid_resonance_capsules import (
    build_rational_ldlt_schur_capsule,
    delayed_detection_aliasing_countermodels,
    even_sector_small_window_submersion_certificate,
    fucc_fractional_gamma_braid_certificate,
    fucc_self_carry_braid_certificate,
    fucc_succ_functoriality_obstructions,
    odd_bubble_offline_pair_certificate,
    single_moment_contact_rigidity_certificate,
    verify_rational_ldlt_schur_capsule,
)
from observational_succ.tate_weighted_bessel_four_schur import (
    KAPPA_EVEN_LOWER,
    KAPPA_ODD_LOWER,
    source_parity_split_four_moment_coercivity_certificate,
)


def _dec12(val) -> str:
    """Deterministic 12-significant-digit decimal string from an exact Fraction or string."""
    getcontext().prec = 50
    q = F(val)
    d = Decimal(q.numerator) / Decimal(q.denominator)
    return f"{d:.12g}"


def build_breakout_receipt() -> dict:
    ct = CertifiedTrial(U=(), J=64, rank=6)
    cdet = CertifiedDerivativeEnergyTrial(
        U=(), J_deriv=20, grid=256, J_galerkin=64, rank=6
    )
    coerc = source_parity_split_four_moment_coercivity_certificate()
    mid30 = source_30mode_middle_block_obstruction_certificate(J=16)
    hl5 = hodge_legendre_endpoint_free_gram(m=5, radius=F(1, 2))
    obs_syn = observer_interior_boundary_synergy_certificate()
    obs_ghost = cross_contact_gauge_no_ghost_countermodel()
    fucc_gamma = fucc_fractional_gamma_braid_certificate(p=3, n_max=4)
    fucc_carry = fucc_self_carry_braid_certificate(p=3, n_max=9, k_max=2)
    fucc_obs = fucc_succ_functoriality_obstructions()
    odd_bub = odd_bubble_offline_pair_certificate(
        Delta=F(1, 10), gamma=F(14, 1), a=F(1, 2)
    )
    even_sub = even_sector_small_window_submersion_certificate(
        Delta=F(1, 10), gamma=F(14, 1), a=F(1, 2), T=F(20, 1)
    )
    alias = delayed_detection_aliasing_countermodels(
        Delta=F(1, 10), gamma=F(14, 1), kappa=F(1, 2)
    )
    contact_rig = single_moment_contact_rigidity_certificate(
        c_perturbation=F(7, 5), a=F(1, 2), rank=6
    )
    M_test = (
        (F(4), F(1), F(1), F(0)),
        (F(1), F(3), F(0), F(1)),
        (F(1), F(0), F(2), F(0)),
        (F(0), F(1), F(0), F(2)),
    )
    capsule = build_rational_ldlt_schur_capsule(
        M_test,
        claim_fqid="PDQ-13",
        mode="SCHUR_COMPLEMENT",
        low_rank=2,
    )
    capsule_ver = verify_rational_ldlt_schur_capsule(capsule)

    return {
        "operation": "OPERATION SUCC x FUCC MEGASWARM: THE FOUR-BODY BREAKOUT",
        "date": "2026-10-16",
        "parent_pr": 150,
        "parent_head": "6a067c1c40e644f589d170a4eaaa1923a25fc200",
        "research_branch": "research/deepseek-pdq-megaswarm-2026-10-16",
        "a": str(A_RADIUS),
        "result_status": "PROVED FINITE/SOURCE-CERTIFIED ENCLOSURES; S_4 SIGN OPEN; RH OPEN",
        "moonshot_A_complete_four_moment_quotient": {
            "claim_ids": ["PDQ-04", "PDQ-07"],
            "identity": "E^T P^{-1} E = 30 c_1^T c_1 + 210 c_2^T c_2 + (1/24) M_3^T M_3 + (1/40) M_4^T M_4 = L^T diag(1,3,5,7) L",
            "U0_J64_two_moment_lower_diag_dec": [
                _dec12(ct["source_dual_boundary_moment_lower"][i][i]) for i in range(4)
            ],
            "U0_J64_four_moment_lower_diag_dec": [
                _dec12(ct["source_full_four_moment_lower"][i][i]) for i in range(4)
            ],
            "U0_J64_two_moment_lower_bracket_diag_dec": [
                _dec12(ct["source_dual_boundary_lower_bracket"][i][i]) for i in range(4)
            ],
            "U0_J64_four_moment_lower_bracket_diag_dec": [
                _dec12(ct["source_dual_four_moment_lower_bracket"][i][i])
                for i in range(4)
            ],
        },
        "moonshot_B_certified_derivative_energy": {
            "claim_ids": ["PDQ-09"],
            "routes": [
                "B1: exact real-space midpoint-Lipschitz quadrature of authentic_suzuki_mode_derivative_point",
                "B3: sharpened O(J^{-3/2}) polynomial integration-by-parts infinite Gamma tail",
            ],
            "J_deriv": cdet["J_deriv"],
            "grid": cdet["grid"],
            "J_galerkin": cdet["J_galerkin"],
            "H_prime_J_midpoint_diag_dec": [
                _dec12(cdet["H_prime_J_midpoint"][i][i]) for i in range(4)
            ],
            "H_prime_loewner_upper_diag_dec": [
                _dec12(cdet["H_prime_loewner_upper"][i][i]) for i in range(4)
            ],
            "gamma_tail_ibp_O_J_minus_3_2_dec": [
                _dec12(x) for x in cdet["gamma_tail_ibp_O_J_minus_3_2"]
            ],
            "gamma_tail_young_O_J_minus_1_dec": [
                _dec12(x) for x in cdet["gamma_tail_young_O_J_minus_1"]
            ],
        },
        "moonshot_C_parity_split_bessel_coercivity": {
            "claim_ids": ["PDQ-08"],
            "kappa_baseline": "1/50",
            "kappa_odd_lower": str(KAPPA_ODD_LOWER),
            "kappa_even_lower": str(KAPPA_EVEN_LOWER),
            "odd_improvement_factor": str(
                coerc["odd_sector"]["improvement_factor_over_1_over_50"]
            ),
            "even_improvement_factor": str(
                coerc["even_sector"]["improvement_factor_over_1_over_50"]
            ),
            "odd_weighted_Bessel_leakage_upper_dec": _dec12(
                coerc["odd_sector"]["weighted_Bessel_leakage_upper"]
            ),
            "even_weighted_Bessel_leakage_upper_dec": _dec12(
                coerc["even_sector"]["weighted_Bessel_leakage_upper"]
            ),
            "kappa_odd_exact_lower_dec": _dec12(
                coerc["odd_sector"]["kappa_odd_exact_lower"]
            ),
            "kappa_even_exact_lower_dec": _dec12(
                coerc["even_sector"]["kappa_even_exact_lower"]
            ),
            "U0_J64_young_parity_kappa_min_eig_by_parity_dec": {
                k: _dec12(v)
                for k, v in ct[
                    "source_dual_parity_kappa_min_eig_lower_by_parity"
                ].items()
            },
            "U0_J64_young_parity_kappa_min_eig_lower_dec": _dec12(
                ct["source_dual_parity_kappa_min_eig_lower"]
            ),
        },
        "moonshot_D_nested_30_to_4_obstruction": {
            "claim_ids": ["PDQ-10"],
            "middle_block_5_to_30_strictly_negative_definite": mid30[
                "middle_block_5_to_30_strictly_negative_definite"
            ],
            "universal_middle_loewner_upper_factor_moment30": str(
                mid30["universal_middle_loewner_upper_factor_moment30"]
            ),
            "universal_middle_loewner_upper_factor_fourier30": str(
                mid30["universal_middle_loewner_upper_factor_fourier30"]
            ),
            "monotone_nested_short_hypothesis_satisfied": mid30[
                "monotone_nested_short_hypothesis_satisfied"
            ],
        },
        "moonshot_E_integrated_S4_brackets": {
            "U0_baseline_young_kappa50_min_eig_by_parity_dec": {
                k: _dec12(v)
                for k, v in ct["lower_bracket_min_eig_lower_by_parity"].items()
            },
            "U0_baseline_young_kappa50_min_eig_dec": _dec12(
                ct["lower_bracket_min_eig_lower"]
            ),
            "U0_young_4moment_parity_kappa_min_eig_by_parity_dec": {
                k: _dec12(v)
                for k, v in ct[
                    "source_dual_parity_kappa_min_eig_lower_by_parity"
                ].items()
            },
            "U0_young_4moment_parity_kappa_min_eig_dec": _dec12(
                ct["source_dual_parity_kappa_min_eig_lower"]
            ),
            "U0_Hprime_4moment_kappa50_min_eig_by_parity_dec": {
                k: _dec12(v)
                for k, v in cdet[
                    "certified_Hprime_kappa50_min_eig_lower_by_parity"
                ].items()
            },
            "U0_Hprime_4moment_kappa50_min_eig_dec": _dec12(
                cdet["certified_Hprime_kappa50_min_eig_lower"]
            ),
            "U0_Hprime_4moment_parity_kappa_min_eig_by_parity_dec": {
                k: _dec12(v)
                for k, v in cdet[
                    "certified_Hprime_parity_kappa_min_eig_lower_by_parity"
                ].items()
            },
            "U0_Hprime_4moment_parity_kappa_min_eig_dec": _dec12(
                cdet["certified_Hprime_parity_kappa_min_eig_lower"]
            ),
            "S4_verdict": cdet["verdict"],
        },
        "wave_II_discoveries": {
            "agent_G_fucc_braid": {
                "all_gauss_legendre_factorizations_exact": fucc_gamma[
                    "all_gauss_legendre_factorizations_exact"
                ],
                "all_kummer_valuations_equal_digit_sum": fucc_gamma[
                    "all_kummer_valuations_equal_digit_sum"
                ],
                "frobenius_scale_invariance_verified": fucc_carry[
                    "frobenius_scale_invariance_verified"
                ],
                "successor_step_valuation_law_verified": fucc_carry[
                    "successor_step_valuation_law_verified"
                ],
                "G_O1_strict_additive_homomorphism_refuted": fucc_obs[
                    "G_O1_strict_additive_homomorphism_refuted"
                ],
            },
            "agent_H_spectral_resonance": {
                "signature_on_4D_quadruplet_span": list(
                    odd_bub["signature_on_4D_quadruplet_span"]
                ),
                "window_scaling_exponent_a": even_sub["window_scaling_exponent_a"],
                "submerged_below_tail_at_T20": even_sub["submerged_below_tail_at_T"],
                "H_C3_fourth_cumulant_discrepancy": str(
                    alias["H_C3_fourth_cumulant_discrepancy"]
                ),
            },
            "agent_I_rational_ldlt_capsule": {
                "claim_id": "PDQ-13",
                "capsule_schema": capsule["capsule_schema"],
                "finite_algebra_verified": capsule_ver["finite_algebra_verified"],
                "division_free_ring_check": capsule_ver["division_free_ring_check"],
            },
            "agent_J_observer_synergy_and_no_ghost": {
                "claim_id": "PDQ-14",
                "strict_synergy_over_sum_of_parts": obs_syn[
                    "strict_synergy_over_sum_of_parts"
                ],
                "residual_under_interior_only": str(
                    obs_syn["residual_under_interior_only"]
                ),
                "residual_under_joined_observer": str(
                    obs_syn["residual_under_joined_observer"]
                ),
                "stitched_ghost_projection_energy": str(
                    obs_ghost["stitched_ghost_projection_energy"]
                ),
                "violates_bessel_inequality": obs_ghost["violates_bessel_inequality"],
            },
            "agent_K_contact_rigidity": {
                "claim_id": "PDQ-12",
                "exact_single_moment_recovery": contact_rig[
                    "exact_single_moment_recovery"
                ],
                "M_Ka_is_strictly_diagonal": contact_rig["M_Ka_is_strictly_diagonal"],
                "boundary_moments_M31_M42_contact_invariant": contact_rig[
                    "boundary_moments_M31_M42_contact_invariant"
                ],
            },
            "agent_L_hodge_legendre_isomorphism": {
                "claim_id": "PDQ-11",
                "m5_K_inverse_00": str(hl5["K_inverse"][0][0]),
                "m5_K_inverse_02": str(hl5["K_inverse"][0][2]),
                "m5_K_inverse_11": str(hl5["K_inverse"][1][1]),
                "m5_K_inverse_22": str(hl5["K_inverse"][2][2]),
            },
        },
        "original_source_weil_sign_certified": False,
        "RH_PROVED": "NO",
    }


def main():
    receipt = build_breakout_receipt()
    root = Path(__file__).resolve().parents[1]
    out_path = root / "research/2026-10-16/FOUR_BODY_BREAKOUT_RECEIPT.json"
    out_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
