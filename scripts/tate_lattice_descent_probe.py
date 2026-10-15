"""Exact source-indexed Tate lattice descent controls (non-RH)."""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.tate_lattice_descent import (
    RationalSChart, character_naturality, finite_depth_alias,
    s_modulus_receipt, successor_history_kernel, prime_extension_obstruction,
)


def main() -> None:
    large = RationalSChart((2, 3, 5), F(13, 17), (F(1, 2), F(-2, 9), F(3, 25)))
    rows = [
        character_naturality(large, S, q)
        for S, q in (((), 1), ((2,), F(1, 8)), ((2, 3), F(1, 18)))
    ]
    if not all(x['commutes'] for x in rows):
        raise AssertionError('Tate character descent failed')
    degree = s_modulus_receipt(30, (2, 3))
    if degree['quotient_cover_degree'] != 5:
        raise AssertionError('Missing-prime defect not caught')
    blind = finite_depth_alias(2, 16)
    history = successor_history_kernel((2, 3), F(1, 6))
    extension = prime_extension_obstruction((2, 3), 5)
    report = {
        'theory': 'Tate finite-S lattice / SUCC local-global',
        'model_scope': 'dense rational stage charts, exact Fraction arithmetic',
        'phase_naturality': rows,
        'missing_prime_defect_5': degree,
        'bounded_probe_alias': blind,
        'causal_event_kernel': history,
        'nonsplit_prime_extension': extension,
        'tate_classical_imports_formally_verified': False,
        'establishes_completed_weil_positivity': False,
        'RH_proved': False,
    }
    print(json.dumps(report, default=str, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
