"""Deterministic exact Tate conductor probe (declared arithmetic, RH remains open)."""
from __future__ import annotations

import json
from fractions import Fraction as Q

from observational_succ.tate_local_contract import (
    unramified_ball_pair, ramified_mod3_coset_pair, gauss_sum_mod3,
    coarse_ramified_unit_zeta, finite_twisted_log_jets,
    chi3_strip_tail_rational, symmetric_offline_mutant,
)


def main():
    original = unramified_ball_pair(2, 2, 3)
    ramified = ramified_mod3_coset_pair(1, 3)
    bound = chi3_strip_tail_rational(7, 55)
    assert original.zeta == original.forward_over_dual * original.dual_zeta
    assert ramified.zeta == Q(1, 2)
    assert gauss_sum_mod3(1).norm() == 3
    assert coarse_ramified_unit_zeta() == 0
    assert symmetric_offline_mutant(Q(1, 4)) == 0
    assert bound < Q(1, 10**16)
    report = {
        "parent_main": "03db44203147a7b28d445bb9f970fa71360e78c4",
        "source": "declared_Tate_Q_places_not_empirical",
        "unramified_ball_case": {
            "p": 2, "a": 2, "sigma": 3,
            "zeta": str(original.zeta),
            "dual_zeta": str(original.dual_zeta),
        },
        "ramified_conductor": {
            "p": 3, "exponent": 1, "gauss_norm_squared": 3,
            "coarse_unit_observation": str(coarse_ramified_unit_zeta()),
            "fine_coset_observation": str(ramified.zeta),
            "local_ratio_delta_coeff": str(ramified.forward_over_dual.b),
        },
        "twisted_log_jet_coefficients": {
            str(p): str(a) for p, a in
            finite_twisted_log_jets((2, 3, 5, 7), 3, 3, "chi3").items()
        },
        "chi3_strip_tail_bound_N7": str(bound),
        "off_line_mutant_roots": ["1/4", "3/4"],
        "status": "CLASSICAL_Tate_plus_derived_rational_strip_tail",
        "completed_Weil_positivity": "UNVERIFIED",
        "RH_PROVED": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
