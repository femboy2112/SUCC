#!/usr/bin/env python3
"""Registered exact finite all-gain measurements; no normality inference."""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.all_gain_observers import (
    gain_average, gain_limit_haar_bound, gain_limit_origin_mass,
    origin_ball_mass, prime_fourier_certificate, prime_stationarity_costs,
    rational_gain_limit, uniform_torsion,
)
from observational_succ.pi_source_collision import bbp_states, tail_upper
from observational_succ.source_history_transport import circle_w1, empirical_law


def rational_json(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


def enclosure(value, places=8):
    scale = 10**places
    lower = value.numerator*scale//value.denominator
    # Both endpoints are certified rationals.  Displayed decimal strings are
    # exact terminating representations, not rounded floating measurements.
    def display(integer):
        return f"{integer//scale}.{integer%scale:0{places}d}"
    return {"lower": display(lower), "upper": display(lower+1),
            "width": str(Q(1, scale))}


def main():
    horizons = (32, 64, 128, 256)
    cutoffs = (2, 4, 8)
    states = bbp_states(max(horizons))
    rows = []
    source_summaries = []
    for horizon in horizons:
        mu = empirical_law(states[1:horizon+1])
        mean_tail = sum((tail_upper(n) for n in range(1, horizon+1)), Q())/horizon
        costs = prime_stationarity_costs(mu, 7)
        source_summaries.append({
            "N": horizon, "support_size": len(mu.atoms),
            "prime_costs": costs,
            "prime_cost_enclosures": {p: enclosure(c) for p, c in costs.items()},
            "origin_mass_radius_1_16": origin_ball_mass(mu, Q(1, 16)),
            "origin_mass_radius_1_64": origin_ball_mass(mu, Q(1, 64)),
            "infinite_gain_origin_mass": gain_limit_origin_mass(mu),
            "infinite_gain_haar_w1_upper": gain_limit_haar_bound(mu),
            "mean_true_orbit_tail_upper": mean_tail,
            "fourier_certificate_Q8_h1_rho1_8":
                prime_fourier_certificate(mu, 8, 1, Q(1, 8)),
        })
        for cutoff in cutoffs:
            average = gain_average(mu, cutoff)
            cost = circle_w1(average, mu)
            rows.append({"N": horizon, "Q": cutoff,
                         "selected_support_size": len(mu.atoms),
                         "averaged_support_size": len(average.atoms),
                         "preservation_W1": cost,
                         "preservation_enclosure": enclosure(cost),
                         "true_orbit_cost_difference_upper":
                             Q(cutoff+3, 2)*mean_tail})
    zero = empirical_law((0,))
    fifth = empirical_law((Q(1, 5),))
    grid = uniform_torsion(5)
    control = {
        "zero_preserved_Q31": gain_average(zero, 31) == zero,
        "zero_origin_mass": origin_ball_mass(zero, 0),
        "one_fifth_Q5_W1": circle_w1(gain_average(fifth, 5), fifth),
        "one_fifth_gain_limit": rational_gain_limit(fifth).atoms,
        "uniform5_not_fixed_by_gain_limit": rational_gain_limit(grid) != grid,
        "uniform5_gain_limit_origin_mass": gain_limit_origin_mass(grid),
        "heldout_uniform101_prime_fourier_certificate":
            prime_fourier_certificate(uniform_torsion(101), 31, 3, Q(1, 8)),
    }
    files = ("observational_succ/all_gain_observers.py",
             "observational_succ/source_history_transport.py",
             "observational_succ/pi_source_collision.py",
             "scripts/all_gain_observers_probe.py",
             "tests/test_all_gain_observers.py")
    result = {
        "schema_version": 1,
        "authority": "EXACT FINITE POST_DISCOVERY CALIBRATION; pi normality OPEN",
        "parent": "d942c4707d750f788f39acb137a04e871a93e0a6",
        "registration": "PI_HYPOTHESIS_A_HOLE_CONTRACT.md",
        "horizons": horizons, "gain_cutoffs": cutoffs,
        "all_registered_rows_retained": len(rows) == len(horizons)*len(cutoffs),
        "source_summaries": source_summaries, "rows": rows, "controls": control,
        "input_sha256": {name: sha256((ROOT/name).read_bytes()).hexdigest()
                         for name in files},
        "asymptotic_claim": False,
    }
    destination = ROOT/'research/2026-10-24/PI_ALL_GAIN_RECEIPT.json'
    destination.write_text(json.dumps(result, default=rational_json,
                                     sort_keys=True, indent=2)+'\n')
    print(json.dumps({"receipt": str(destination.relative_to(ROOT)),
                      "rows": len(rows),
                      "preservation_lower_endpoints": [
                          {"N": row['N'], "Q": row['Q'],
                           "W1_lower": row['preservation_enclosure']['lower']}
                          for row in rows],
                      "pi_normality": "OPEN"}, indent=2))


if __name__ == '__main__':
    main()
