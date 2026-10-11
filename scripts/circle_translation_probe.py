#!/usr/bin/env python3
"""Exact semantic transport report for polynomial A and trigonometric B.

Claims apply to exact finite rational polynomial/angle samples only; global
trig Fourier equivalence and winding statements have separate mathematical
derivations in the research note. Do not claim actual observer experiments.
"""
import json

from observational_succ.circle_translation import cross_language_circle_demo


def main():
    report = cross_language_circle_demo()
    assert report["status"] == "EXACT_CIRCLE_POLYNOMIAL_TRIG_TRANSLATOR"
    assert report["coordinate_ring_identity_zero"] is True
    assert report["trigonometric_polynomial_identity_zero"] is True
    assert report["group_law_preserved"] is True
    assert report["orientation_requires_explicit_calibration"] is True
    assert report["reflected_winding_sign_inverted"] is True
    assert report["identical_finite_phase_samples"] is True
    assert report["different_true_winding_numbers"] is True
    assert report["matching_sampled_windings"] == [1,5]
    assert report["full_path_observability_proved_by_samples"] is False
    assert report["general_two_theory_translation_proved"] is False
    assert report["RH_claimed"] is False
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
