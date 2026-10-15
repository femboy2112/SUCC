"""Reproduce Tate Q_p + standard Gaussian adelic and Weil support gates.

This probe reads arithmetic source laws directly, never positions of nontrivial
zeros or a model-fitted positive substitute for the signed Weil functional.
"""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.tate_schwartz_functor import (
    PadicBall, SourceEvent, SourceWord,
    critical_mellin_character, first_missing_prime, local_mellin_shell,
)
from observational_succ.adelic_schwartz_source import DiagonalGaussianTensor
from observational_succ.tate_weil_window import (
    CompactWeilSourceWindow, invisible_prime_window,
    support_cofinality_receipt,
)


def main():
    padic = PadicBall(3, F(1, 3), 0, "SUCC-Tate-source", 2)
    word = SourceWord(padic, (
        SourceEvent(padic.source_id, 2, 0, "SUCC", F(1, 3)),
        SourceEvent(padic.source_id, 2, 1, "PRIME_JET_FUCC", F(3)),
        SourceEvent(padic.source_id, 2, 2, "FUCC", F(1, 3)),
    ))
    fourier = word.fourier_receipt(F(3))
    gaussian = DiagonalGaussianTensor(F(-6, 35), F(1, 22), F(7, 11),
                                     "SUCC-Tate-source", 2)
    paired = gaussian.fourier_at_rational(F(-35, 6))
    source = CompactWeilSourceWindow(F(3, 2)).certificate()
    missing = first_missing_prime(7)
    controls = {
        "Qp_affine_Fourier": fourier,
        "adelic_diagonal_phase_Haar": paired,
        "local_Euler_Mellin": local_mellin_shell(3, 2, 0, 6),
        "critical_halfdensity": critical_mellin_character(F(1, 2)),
        "wrong_halfdensity": critical_mellin_character(F(1, 2), F(1, 3)),
        "compact_source_window": source,
        "unseen_candidate_tape_mutation": missing,
        "certified_outside_window": invisible_prime_window(29, F(3, 2)),
        "cofinality_not_finite_completion": support_cofinality_receipt(5),
    }
    if not (fourier["fourier_naturality"] and
            paired["global_phase"] == 0 and
            paired["global_Haar_affine_scaling"] == 1 and
            source["support_bounded_without_exp_floats"] and
            not missing["mutant_satisfies_complete_actual_von_Mangoldt_source"]):
        raise AssertionError("Tate source interface does not pass controls")
    report = {
        "scope": "Declared original Q source; rational local charts and symbolic Gaussian",
        "claims": controls,
        "full_Schwartz_Bruhat_completion_proved": False,
        "complete_source_Weil_form_identified_by_functor": False,
        "all_Weil_tests_positive": False,
        "RH_proved": False,
    }
    print(json.dumps(report, default=str, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
