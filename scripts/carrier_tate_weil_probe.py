#!/usr/bin/env python3
"""Replay exact carrier/Tate/Weil interfaces, with no zero-coordinate input."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.tate_idelic_zeta import (
    RationalChartIdele, StandardTateSource, TateZeroModes,
    euler_exhaustion_bound, log_derivative_tail_bound,
)
from observational_succ.tate_chi4 import (
    Chi4TateSource, diagonal_hecke_receipt, ramified_fourier,
    source_fourier_multiplier, validate_coefficient_tape,
)
from observational_succ.source_character_interaction import character_four
from observational_succ.tate_weil_distribution import (
    TateWeilSource, pointwise_negative_bump_certificate,
)
from observational_succ.tate_positivity_obstruction import (
    positivity_obstruction_certificate,
)


def receipt():
    zeta = StandardTateSource("carrier-tate-weil-zeta", 1)
    chi4 = Chi4TateSource("carrier-tate-weil-chi4", 1)
    x = RationalChartIdele(Q(-7, 3), Q(5, 2),
                          ((2, Q(8, 3)), (5, Q(1, 25))), zeta.source_id, 1)
    q = x.quotient()
    sources = [TateWeilSource.from_tate(s) for s in (zeta, chi4)]
    source_receipts = []
    for s in sources:
        tape = s.atoms(3)
        s.verify_tape(3, tape)
        rejected = []
        for label, mutant in (("omitted_first", tape[1:]),
                              ("fake6", tape+((6, 6, 1),))):
            try:
                s.verify_tape(3, mutant)
            except ValueError:
                rejected.append(label)
        source_receipts.append({
            "character": s.character, "source_id": s.source_id, "epoch": s.epoch,
            "conductor": s.conductor, "parity": s.parity,
            "pole_multiplicity": s.pole_multiplicity, "atoms_R3": tape,
            "rejected_mutations": rejected,
            "C1_error_R3_delta_1e6": s.continuity_budget(3, delta0=Q(1, 10**6),
                                                        delta1=Q(1, 10**6)),
            "gamma_tail_J16_M0_1_M1_2": s.gamma_tail(16, M0=1, M1=2),
            "accelerated_tail_J16_M0_1_M2_4": s.accelerated_gamma_tail(16, M0=1, M2=4),
        })
    tape = tuple(character_four(n) for n in range(1, 21))
    mutant = tape[:8]+(-1,)+tape[9:]
    obstruction = positivity_obstruction_certificate()
    return {
        "schema": "SUCC_CARRIER_TATE_WEIL_1",
        "parent_commit": "d239c27d3759de71de316180f48dfc097be6aff5",
        "idele": {"norm": x.norm, "q": q.rational_multiplier,
                  "normalized_real": q.representative.real,
                  "reconstructs": q.reconstruct() == x,
                  "diagonal_norm_invariant": x.diagonal_action(Q(-11, 7)).norm == x.norm,
                  "unit_residue_2_depth5": q.unit_residue(2, 5)},
        "standard_zero_mode_residues": TateZeroModes().residues,
        "zeta_euler_exhaustion": euler_exhaustion_bound(31, 2),
        "logarithmic_tail_N31_sigma2": log_derivative_tail_bound(31, 2),
        "chi4_diagonal": diagonal_hecke_receipt(Q(-45, 28)),
        "chi4_ramified_fourier_at_quarter": ramified_fourier(Q(1, 4)),
        "fourier_phase_multiplier": source_fourier_multiplier(),
        "wrong_finite_phase_multiplier": source_fourier_multiplier(1, 1),
        "chi4_true_tape": validate_coefficient_tape(tape),
        "chi4_nonEuler_tape": validate_coefficient_tape(mutant),
        "weil_sources": source_receipts,
        "authentic_pointwise_negative_bump": pointwise_negative_bump_certificate(),
        "modified_signed_source_obstruction": obstruction,
        "boundaries": {"actual_zeta_zero_positions_used": False,
                       "finite_samples_prove_analytic_theorems": False,
                       "source_ids_are_physical_attestation": False,
                       "floating_quadrature_is_certified": False,
                       "canonical_Weil_PSD_proved": False,
                       "RH_proved": False},
    }


if __name__ == "__main__":
    print(json.dumps(receipt(), default=lambda x: str(x), sort_keys=True, indent=2))
