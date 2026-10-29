#!/usr/bin/env python3
"""Replay exact observer counts, signed boundary identities and source controls.

Run from any working directory.  The receipt is finite evidence, not a
replacement for the quantified paper proofs or the separately run Lean core.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.divisor_observer_spectrum import (  # noqa: E402
    boundary_multiplicities, divisor_summatory, exact_shell_residuals,
    formal_boundary_minus_weyl, formal_commutator_numerator, gauge_cycle_turn,
    hyperbolic_shell_receipt, original_bbp_turns, sharp_commutator_bound,
)


def encode(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


def phase_fingerprint(turns):
    return hashlib.sha256("\n".join(map(str, turns)).encode()).hexdigest()


def build_receipt():
    # Independent literal pair-space count, separate from floor-grouping code.
    for limit in range(1, 65):
        pairs = {(a, b) for a in range(1, limit + 1)
                 for b in range(1, limit + 1) if a*b <= limit}
        count = len(pairs)
        internal = sum((a+1, b) in pairs for a, b in pairs)
        assert count == divisor_summatory(limit)
        assert internal == count - limit
        weights = boundary_multiplicities(limit)
        assert sum(weights) == limit
        assert sum(abs(c-1) for c in weights) == 2*(limit//2)

    horizons = []
    for limit in (1, 2, 16, 64, 1000, 10000, 100000):
        row = hyperbolic_shell_receipt(limit)
        # Ungrouped quotient oracle, independent of optimized summatory loop.
        assert row["squared_unnormalized_norm"] == sum(limit//b for b in range(1, limit+1))
        row["sharp_signed_scalar_bound"] = sharp_commutator_bound(limit)
        if limit <= 64:
            row["direct_residuals"] = exact_shell_residuals(limit)
            assert row["direct_residuals"]["L_squared_norm"] <= row["residual_squared_upper"]
        horizons.append(row)

    limit = 48
    authentic = original_bbp_turns(limit)
    torsion = original_bbp_turns(limit, seed=Q(1, 15))
    altered, literal, state, mutant = [], [], Q(), Q()
    for n in range(1, limit+1):
        forcing = Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)
        state = (16*state + forcing) % 1
        mutant = (16*mutant + forcing + Q(1, 8*n-7)) % 1
        literal.append(state)
        altered.append(mutant)
    assert tuple(literal) == authentic
    assert all((t-a) % 1 == Q(1, 15) for a, t in zip(authentic, torsion))
    assert tuple(altered) != authentic
    phase_rows = []
    for name, turns in (("authentic_zero_seed", authentic),
                        ("same_forcing_torsion_seed_1_over_15", torsion),
                        ("altered_first_pole_4_to_5", altered),
                        ("constant_nonnormal_control", (Q(),)*limit)):
        direct = formal_commutator_numerator(turns)
        assert direct == formal_boundary_minus_weyl(turns)
        assert gauge_cycle_turn(turns, (2, 3, 4, 2)) == 0
        phase_rows.append({
            "source": name,
            "phase_fingerprint_sha256": phase_fingerprint(turns),
            "formal_signed_boundary_identity": True,
            "cycle_holonomy_turn": "0",
            "nonzero_formal_coefficients": len(direct),
            "authentic_source_member": name == "authentic_zero_seed",
        })

    source_paths = (
        "observational_succ/bbp_natural_carrier.py",
        "observational_succ/origin_fiber_arithmetic_observer.py",
        "research/2026-10-21/DUCK_BBP_SOURCE_IDENTITY.md",
        "research/2026-10-28/OILY_ZETA_CAUSAL_GROWTH_AND_SOURCE_DEFECT.md",
    )
    return {
        "schema": "SUCC-divisor-observer-exact-receipt-v1",
        "base_commit": "fec9b7a72dd6b8c7550d7915070ee8094f2b94a2",
        "authority": "EXACT FINITE TEST; infinite statements are paper proofs",
        "source_sha256": {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
                          for path in source_paths},
        "literal_pair_oracle_horizons": [1, 64],
        "hyperbolic_horizons": horizons,
        "hard_pin_examples": [hyperbolic_shell_receipt(128, 16),
                              hyperbolic_shell_receipt(128, 64)],
        "phase_controls_horizon": limit,
        "phase_controls": phase_rows,
        "alternating_phase_controls": [
            {"limit": n,
             "boundary_sum": sum((-1)**(b*(n//b)) for b in range(1, n+1)),
             "weyl_sum": sum((-1)**j for j in range(1, n+1)),
             "paper_boundary_mean_limit": "1-log(2)"}
            for n in (64, 4096)
        ],
        "coherent_seed_control": {
            "seed": "-pi/16 (irrational; not encoded as a rational seed)",
            "paper_bound": "|U_n| <= 1/[15(n+1)^2] for n>=1",
            "signed_mean_limit": "1 by the paper tail argument; not numerically certified here",
        },
        "pi_normality": "OPEN",
        "RH": "OPEN",
        "academic_novelty": "UNVERIFIED; classical gauge/Weyl ingredients",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.dumps(build_receipt(), indent=2, sort_keys=True, default=encode) + "\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
