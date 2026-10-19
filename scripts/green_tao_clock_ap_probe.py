#!/usr/bin/env python3
"""Deterministic bounded source receipt for double prime-AP phase grids."""
from __future__ import annotations

import json
from fractions import Fraction

from observational_succ.green_tao_clock_ap import (
    exact_character_label, local_prime_factors, local_step_requirement,
    prime_clock_progression, prime_predecessor_factorization,
    search_first_grid, verify_prime_clock_grid, wheel_arithmetic,
    verify_flat_rad_prime_ladder, search_flat_rad_ladder,
)


def _ratio(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def _grid(q: tuple[int, ...], start: int, step: int, count: int) -> dict:
    g = verify_prime_clock_grid(q, start, step, count)
    return {
        "clock_primes": list(q), "wheel": g.wheel_modulus,
        "clock_difference": g.clock_step,
        "endpoint_primes": list(g.endpoint_primes),
        "endpoint_difference": g.endpoint_step,
        "start_multiplier": g.multiplier_start,
        "multiplier_step": g.multiplier_step,
        "minimal_local_step": g.local_minimum_step,
        "all_phase_1_incidence_count": g.incidence_count,
        "endpoint_predecessor_factorizations": [
            [[p, exponent] for p, exponent in prime_predecessor_factorization(n)]
            for n in g.endpoint_primes],
        "source_validated_primes": True,
    }


def probe() -> dict:
    seven = (2, 3, 5, 7, 11, 13, 29)
    w = wheel_arithmetic(seven)
    q3 = prime_clock_progression(3, 2, 3)
    q4 = prime_clock_progression(5, 6, 4)
    q5 = prime_clock_progression(5, 6, 5)
    first5 = search_first_grid(q5, 5, 630)
    if first5 is None or first5.endpoint_primes[-1] != 392896351:
        raise AssertionError("bounded five-by-five first-endpoint certificate changed")
    forbidden = local_prime_factors(q5, 5, 1, 11)
    allowed = local_prime_factors(q5, 5, 66, 11)
    return {
        "source": "genuine positive primes; n mod q, +1 SUCC, target phase 1",
        "seven_clock_example": {
            "prime": 870871,
            "modulus": w.modulus,
            "phi": w.totient,
            "candidate_enrichment_exact": _ratio(w.wheel_enrichment),
            "fixed_modulus_relative_density": _ratio(w.relative_prime_density),
            "first_return_prime": w.first_return == 870871,
            "exact_fourier_character_h": w.faithful_character_multiplier,
            "prime_phase_label": list(exact_character_label(870871, seven)),
            "distinct_phase_bits_lower": w.minimum_distinguishing_bits,
            "p_minus_one_factors": [
                [q, e] for q, e in prime_predecessor_factorization(870871)
            ],
        },
        "exact_prime_rectangles": {
            "3x3": _grid(q3, 2, 2, 3),
            "4x4": _grid(q4, 46, 6, 4),
            "5x5": _grid(q5, 366, 66, 5),
        },
        "five_by_five_minimum_with_last_multiplier_at_most_630": {
            "source_fixed_clocks": list(q5),
            "bound_last_multiplier": 630,
            "least_greatest_prime_endpoint": first5.endpoint_primes[-1],
            "first_grid": list(first5.endpoint_primes),
            "global_unbounded_minimum_claimed": False,
        },
        "local_admissibility": {
            "wheel": wheel_arithmetic(q5).modulus,
            "length": 5,
            "required_multiplier_divisor": local_step_requirement(q5, 5),
            "d1_has_zero_local_factor": any(v.singular_series_factor == 0 for v in forbidden),
            "d66_all_local_factors_positive_to_11": all(
                v.singular_series_factor > 0 for v in allowed),
            "fixed_difference_prime_tuple_infinitude_claimed": False,
        },
        "flat_rad_prime_ladders": {
            "3": list(verify_flat_rad_prime_ladder(210, 3).prime_endpoints),
            "4": list(verify_flat_rad_prime_ladder(330, 4).prime_endpoints),
            "5": list(verify_flat_rad_prime_ladder(247710, 5).prime_endpoints),
            "5x5_all_clocks_and_flat_RAD": {
                "clocks": [5, 11, 17, 23, 29],
                "radical": 71533328790,
                "primes": list(verify_flat_rad_prime_ladder(71533328790, 5).prime_endpoints),
                "ris_values": list(verify_flat_rad_prime_ladder(71533328790, 5).residual_values),
            },
            "first_R_length_4_with_cap_330": search_flat_rad_ladder(4, 330).radical,
            "first_R_length_5_with_cap_247710": search_flat_rad_ladder(5, 247710).radical,
            "infinitely_many_anchored_ladders_proved": False,
        },
        "Green_Tao_reconstructed_inside_SUCC": False,
        "GT_positive_density_and_PNT_AP_used_as_external_theorems": True,
        "ABC_proved": False,
        "RH_proved": False,
        "signed_Weil_S4_proved": False,
    }


if __name__ == "__main__":
    print(json.dumps(probe(), indent=2, sort_keys=True))
