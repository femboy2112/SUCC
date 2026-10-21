"""Reproducible exact finite pi polygon / path-defect probe.

Run: python scripts/pi_polygon_normality_probe.py
Or:  python scripts/pi_polygon_normality_probe.py --output research/2026-10-20/PI_POLYGON_NORMALITY_FINITE_RECEIPT.json

No nonzero Fourier-decay theorem or normality of pi is claimed.
"""

import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.pi_polygon_normality import (
    certified_fractional_pi_digits, digit_block_total_variation,
    finite_digit_path, orbit_lipschitz_error_bound, polygon_pi_bracket,
    polygon_quantize, uniform_grid_pushforward_counts,
)


def run_probe():
    levels = []
    for n in (0, 1, 2, 4, 8, 12, 16, 20):
        word, bracket = certified_fractional_pi_digits(n, 10, 16, 256)
        assert bracket.lower < bracket.upper
        assert bracket.upper - bracket.lower < Q(64, bracket.sides**2)
        levels.append({
            'doublings': n, 'vertices': bracket.sides,
            'lower_rational': str(bracket.lower),
            'upper_rational': str(bracket.upper),
            'gap_rational': str(bracket.upper - bracket.lower),
            'certified_decimal_prefix': word,
            'prefix_length': len(word),
        })
    normality_control = tuple(0 if i % 2 == 0 else 1 for i in range(200))
    from math import isqrt
    sparse = tuple(1 if isqrt(i)**2 == i else 0 for i in range(1, 401))
    binary_champernowne = tuple(int(ch) for ch in
        "".join(format(n, "b") for n in range(1, 1500))[:8000])
    x = Q(1, 7)
    q0, q1 = polygon_quantize(x, 4), polygon_quantize(x, 8)
    assert (2 * q1) % 1 != q0
    receipt = {
        'title': 'PI_POLYGON_NORMALITY_FINITE_RECEIPT',
        'parent_main': 'b5f9591033db2022bda6a2f16a935c06466f9eff',
        'date': '2026-10-20',
        'arithmetic': 'exact rational + outward dyadic sqrt; no float pi inputs',
        'pi_polygon_brackets': levels,
        'two_distinct_grid_pushforwards': {
            'start_sides': 4, 'base': 3, 'level': 2,
            'fine_vertex_count': 4*3**3,
            'both_maps_have_every_fiber_size_three': all(
                set(uniform_grid_pushforward_counts(4, 3, 2, op)) == {3}
                for op in ('prefix', 'rotation')),
            'noncommuting_point': {'source': str(x),
                'coarse_prefix': str(q0), 'fine_prefix': str(q1),
                'rotation_of_fine': str((2*q1) % 1)},
        },
        'hostile_symbolic_paths': {
            'all_zero_TV_k2': str(digit_block_total_variation((0,)*200, 2, 2)),
            'alternating_TV_k1': str(digit_block_total_variation(normality_control, 2, 1)),
            'alternating_TV_k2': str(digit_block_total_variation(normality_control, 2, 2)),
            'sparse_squares_TV_k1': str(digit_block_total_variation(sparse, 2, 1)),
            'champernowne_8000_TV_k1': str(digit_block_total_variation(binary_champernowne, 2, 1)),
            'champernowne_8000_TV_k4': str(digit_block_total_variation(binary_champernowne, 2, 4)),
            'terminating_prefix_9_steps': ''.join(map(str, finite_digit_path((1,0,1,1), 2, 9))),
            'limit_of_finite_truncations_claimed_normal': False,
        },
        'orbit_transport': {
            'base': 2, 'horizon': 5, 'source_error': str(Q(1,56)),
            'lipschitz_mean_error_bound': str(orbit_lipschitz_error_bound(2,5,Q(1,56))),
            'nonuniform_in_horizon': True,
        },
        'claim_firewalls': {
            'pi_normality_proved': False,
            'pi_nonnormality_proved': False,
            'pi_digit_frequency_limit_measured': False,
            'finite_polygon_symmetry_forces_all_paths_generic': False,
            'circle_curvature_defect_forced_by_path_bias': False,
            'limit_order_obstruction_proved_on_known_normal_numbers': True,
            'independent_pi_digits_used_to_produce_source_bounds': False,
            'source_specific_fourier_cancellation_obtained': False,
        },
    }
    return receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    options = parser.parse_args()
    rendered = json.dumps(run_probe(), sort_keys=True, indent=2) + '\n'
    if options.output is not None:
        options.output.parent.mkdir(parents=True, exist_ok=True)
        options.output.write_text(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
