"""Independent exact rational grid for source-typed finite solenoid identities.

Run from a SUCC checkout: python scripts/solenoid_digit_bridge_probe.py
Output is deterministic JSON; finite checks do not prove an infinite claim.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from fractions import Fraction as Q

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.solenoid_digit_bridge import (
    FiniteSolenoidChart, authentic_four_pole, canceled_four_pole,
    rational_character_split, two_adic_residue,
)


def main() -> None:
    count = 0
    for b in range(1, 38, 2):
        for a in range(-50, 51):
            u = Q(a, b)
            chart = FiniteSolenoidChart.from_unwrapped(u, 4)
            for n in range(4):
                actual = Q(16**n) * u
                floor = actual.numerator // actual.denominator
                oracle = (actual - floor, floor % 16**4)
                assert (chart.circle, chart.memory) == oracle
                for k in range(1, 5):
                    q = 16**k
                    h = 5
                    assert chart.character_phase(h, k) == (Q(h)*actual/q) % 1
                    real, adic, complement = rational_character_split(u, k, h)
                    assert real == (Q(h)*u/q) % 1
                    assert real == (adic + complement) % 1
                    residue = (u.numerator*pow(u.denominator,-1,q))%q
                    assert two_adic_residue(u,k) == residue
                    count += 1
                chart, _ = chart.advance()
    for n in range(1, 100):
        assert authentic_four_pole(n) == canceled_four_pole(n)
    native = False
    try:
        from observational_succ.succ_internal_matrix_walk import authentic_r
    except ModuleNotFoundError:
        pass
    else:
        for n in range(1, 100):
            assert authentic_four_pole(n) == authentic_r(n)
        native = True
    print(json.dumps({
        'status':'PASS',
        'exact_cross_checks':count,
        'numerator_range':[-50,50],
        'odd_denominator_range':[1,37],
        'time_range':[0,3],
        'character_depth_range':[1,4],
        'source_checks':99,
        'native_repo_source_checked':native,
        'claim':'finite exact verification only, no pi normality inference'
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
