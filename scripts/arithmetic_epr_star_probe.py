"""Deterministic source-aware finite arithmetic/analytic/EPR/p-adic-star receipt.

Run at repository root with: python scripts/arithmetic_epr_star_probe.py
No NumPy, floating numerical certificates, or external packages required.
"""
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F

from observational_succ.arithmetic_epr_star import (
    PAIRS, codeword, dirichlet_reconstruct, dirichlet_samples,
    local_bruhat_tits_neighbors, encoded_mirror_images,
    pair_decode, truncation_mirror_residual_beta2, source_chart_braid_defect,
)


def main():
    samples = dirichlet_samples((F(2,7), F(-3,5), F(1,11)))
    coeffs = dirichlet_reconstruct(samples)
    assert coeffs == (F(2,7), F(-3,5), F(1,11))
    assert len(local_bruhat_tits_neighbors()) == 3
    all_pair_results = {}
    for a in PAIRS:
        for b in PAIRS:
            left,right = encoded_mirror_images(a,b)
            fake_left,fake_right = encoded_mirror_images(a,b,weights=(4,2,2))
            assert left == right and fake_left != fake_right
            all_pair_results[f'{a}-{b}'] = {
                'mirror_equal': True,
                'unnormalized_amplitude_support': len(left),
                'mutated_source_mirror_equal': False,
            }
    braid_left, braid_right = source_chart_braid_defect()
    assert braid_left != braid_right
    receipt = {
        'research': 'PRIME_BRIDGE_ONE_SHOT_2026_10_22',
        'scope': 'genuine radius-one p=2 Bruhat-Tits shell; 3-qutrit standard QEC; finite source {1,2,4}',
        'academic_novelty_claimed': False,
        'geometric_gravitational_duality_claimed': False,
        'source_prime': 2,
        'boundary_qutrit_alphabet_size': 3,
        'geometric_neighbors_exact': 3,
        'isometry_codeword_support_sizes': [len(codeword(i)) for i in range(3)],
        'analytic_evaluation_sigma': [1,2,3],
        'analytic_samples': [str(s) for s in samples],
        'analytic_round_trip_coefficients': [str(c) for c in coeffs],
        'all_nine_region_pair_checks': all_pair_results,
        'finite_beta2_tfd_logical_numerator': [4,2,1],
        'finite_beta2_tfd_squared_norm_numerator_denominator': [21,21],
        'bulk_entropy_natural_log_symbolic': 'log(21)-(24/7)*log(2)',
        'two_leg_entropy_natural_log_symbolic': 'log(3)+log(21)-(24/7)*log(2)',
        'truncation_error_squared_N2_p2': str(truncation_mirror_residual_beta2(2)),
        'truncation_error_squared_N3_p2': str(truncation_mirror_residual_beta2(3)),
        'compressed_braid_left_e1': [str(x) for x in braid_left],
        'compressed_braid_right_e1': [str(x) for x in braid_right],
        'no_full_infinite_hilbert_code': True,
        'RH_proved': False,
        'signed_Weil_positivity_proved': False,
    }
    root=Path(__file__).resolve().parents[1]
    receipt['source_module_sha256']=hashlib.sha256(
        (root/'observational_succ/arithmetic_epr_star.py').read_bytes()).hexdigest()
    receipt['test_module_sha256']=hashlib.sha256(
        (root/'tests/test_arithmetic_epr_star.py').read_bytes()).hexdigest()
    print(json.dumps(receipt,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
