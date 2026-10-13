#!/usr/bin/env python3
"""Positive carrier realization: frozen exact receipt.

Reproduces, in exact rational arithmetic, every finite certificate quoted in
research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY.md.  Fractions are
serialized as strings; the JSON is byte-compared in CI.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction as Q

from observational_succ.carrier_realization import (
    availability_square, calibration_matrix, carrier_from_cone,
    carrier_realization_oracle, charpoly, closed_loop_law, cyclotomic_clock,
    distinguishing_experiment, equivalence_certificate, euler_phi,
    fooling_set_lower_bound, hankel_block, is_fooling_set, legality_pattern,
    minimal_realization, orbit_cone_carrier, path_walk_carrier,
    peripheral_spectrum_certificate, promotion_witness, rank, rational_clock,
    reachable_cone_refinement, tensor_fooling_set, verify_cone,
)

TICK = ("clock", "tick")
RESET = ("clock", "reset")
BOK = ("b", "ok")


def s(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, (list, tuple)):
        return [s(y) for y in x]
    if isinstance(x, dict):
        return {str(k): s(v) for k, v in x.items()}
    return x


def report() -> dict:
    out: dict = {"schema": "SUCC-POSITIVE-CARRIER-1",
                 "status": "EXACT_POSITIVE_CARRIER_REALIZATION_BOUNDARY"}

    # 1. calibration
    P = calibration_matrix()
    size, cells = fooling_set_lower_bound(P)
    out["calibration"] = {
        "row_stochastic": all(sum(r, Q(0)) == 1 for r in P),
        "rank": rank(P),
        "row_dependence_r1_minus_r2_minus_r3_plus_r4": s(tuple(
            P[0][j] - P[1][j] - P[2][j] + P[3][j] for j in range(4))),
        "fooling_set": list(cells), "fooling_set_size": size,
        "nonnegative_rank": 4,
        "lean_kernel_checked_core": "formal/EODCS_PositiveCarrier.lean:calibration_fooling_bound",
    }

    # 2. path walk family
    pw = path_walk_carrier(1)
    R = minimal_realization(pw)
    rows = [("u", (("a", z),)) for z in range(4)]
    cols = [(("a", z),) for z in range(4)]
    H = hankel_block(pw, rows, cols)
    rep3 = carrier_realization_oracle(pw, proposed_dimension=3, hankel_rows=rows, hankel_cols=cols)
    rep4 = carrier_realization_oracle(pw, proposed_dimension=4, cone_depth=2)
    pw2 = path_walk_carrier(2)
    R2 = minimal_realization(pw2)
    rows2 = [(("u", "u"), (("a", (z1, z2)),)) for z1 in range(4) for z2 in range(4)]
    cols2 = [(("a", (z1, z2)),) for z1 in range(4) for z2 in range(4)]
    H2 = hankel_block(pw2, rows2, cols2)
    F2 = tensor_fooling_set(cells, (4, 4), cells, (4, 4))
    dep_ok = all(sum((((1, -1, -1, 1)[i]) * pw.probability(f"d{i}", w) for i in range(4)), Q(0)) == 0
                 for n in range(4) for w in itertools.product(
                     [("a", z) for z in range(4)] + [("b", "s")], repeat=n))
    out["path_walk_family"] = {
        "PW1": {"states": 4, "linear_dimension": R.dimension,
                "mass_conserving_minimal": R.mass_conserving(),
                "single_source_block_rows": "p_u(a z . a z')", "block": s(H),
                "block_rank": rank(H), "block_fooling_set_size": fooling_set_lower_bound(H)[0],
                "oracle_proposed_3": rep3["verdict"],
                "oracle_proposed_4": rep4["verdict"], "carrier_found_dimension": rep4["carrier_dimension"],
                "equivalence_certificate": rep4["equivalence"]["equivalent"],
                "silent_swap_preserves_linear_dependence": dep_ok,
                "positive_carrier_dimension": 4},
        "PW2": {"states": 16, "linear_dimension": R2.dimension, "block_rank": rank(H2),
                "tensor_fooling_set_size": len(F2), "tensor_fooling_set_valid": is_fooling_set(H2, F2),
                "positive_carrier_dimension": 16},
        "general_n": {"linear_dimension": "3^n", "positive_carrier_dimension": "4^n",
                      "lower_bound_witness": "product fooling set of size 4^n",
                      "upper_bound_witness": "product carrier"},
    }

    # 3. rational clock
    ck = rational_clock()
    Rc = minimal_realization(ck)
    cert = peripheral_spectrum_certificate(Rc, (TICK,))
    neg = 0
    for n in range(7):
        for w in itertools.product((TICK, RESET, BOK), repeat=n):
            for src in ("s0", "sstar"):
                if ck.probability(src, w) < 0:
                    neg += 1
    search = reachable_cone_refinement(Rc, depth=2, max_generators=12)
    a, b = 1, 0
    gauss = []
    for n in range(1, 8):
        a, b = 3 * a - 4 * b, 4 * a + 3 * b
        gauss.append({"n": n, "re": a, "im": b, "im_mod_5": b % 5})
    out["rational_clock"] = {
        "linear_dimension": Rc.dimension, "mass_conserving": ck.mass_conserving(),
        "charpoly_tick_on_minimal_space": s(charpoly(Rc.operators["clock"]["tick"])),
        "charpoly_factored": "(x - 1/2) (x^2 - (3/5) x + 1/4)",
        "peripheral_witness": s(cert["witness"]), "verdict": cert["verdict"],
        "positive_carrier_dimension": "infinity",
        "words_checked_nonnegative_length_le_6": neg == 0,
        "pure_tick_from_vstar_first_values": s([ck.probability("sstar", (TICK,) * n) for n in range(6)]),
        "gaussian_power_imaginary_parts": gauss,
        "lean_kernel_checked_core": "formal/EODCS_PositiveCarrier.lean:gaussian_rotation_never_real",
        "reset_word_verdict": peripheral_spectrum_certificate(Rc, (TICK, BOK))["verdict"],
        "cone_refinement_verdict": search["verdict"],
    }

    # 4. cyclotomic clocks
    fam = []
    for k in (3, 4, 5, 6, 8, 10, 12, 30):
        sysk = cyclotomic_clock(k)
        Rk = minimal_realization(sysk)
        ck_cert = peripheral_spectrum_certificate(Rk, (TICK,))
        _, cone = orbit_cone_carrier(sysk, "sstar", (TICK,), k)
        car = carrier_from_cone(cone)
        _, cone_short = orbit_cone_carrier(sysk, "sstar", (TICK,), k - 1)
        fam.append({"k": k, "phi": euler_phi(k), "linear_dimension": Rk.dimension,
                    "mass_conserving": Rk.mass_conserving(),
                    "peripheral_lower_bound": ck_cert["lower_bound"],
                    "orbit_cone_valid": cone.valid, "orbit_carrier_dimension": car.dimension,
                    "equivalent": equivalence_certificate(sysk, car)["equivalent"],
                    "k_minus_1_generators_valid": cone_short.valid,
                    "positive_carrier_dimension": k})
    c6 = cyclotomic_clock(6)
    _, cone6 = orbit_cone_carrier(c6, "sstar", (TICK,), 6)
    car6 = carrier_from_cone(cone6)
    H6 = hankel_block(car6, [("sstar", (TICK,) * i) for i in range(6)],
                      [(TICK,) * j + (RESET,) for j in range(6)])
    out["cyclotomic_clocks"] = {
        "family": fam,
        "C6_hankel_block_strictly_positive": all(x > 0 for r in H6 for x in r),
        "C6_fooling_bound_only": fooling_set_lower_bound(H6)[0],
        "C6_six_state_carrier_tick": s(car6.events["clock"]["tick"]),
        "C6_six_state_carrier_preparations": s(car6.preparations),
    }

    # 5. availability square
    fine, coarse = availability_square()
    wit = promotion_witness(fine, coarse, 2)
    dist = distinguishing_experiment(fine, coarse)
    try:
        closed_loop_law(fine, "mixed", lambda u: {"b": Q(1)}, 1)
        illegal_rejected = False
    except Exception:
        illegal_rejected = True
    out["availability_square"] = {
        "fine_menus_mixed": {repr(k): list(v) for k, v in legality_pattern(fine, "mixed", 1).items()},
        "coarse_menus_mixed": {repr(k): list(v) for k, v in legality_pattern(coarse, "mixed", 1).items()},
        "promotion_witness": s(wit),
        "legal_word_probabilities_agree": all(
            fine.probability(src, u) == coarse.probability(src, u)
            for src in ("pure", "mixed") for u in legality_pattern(fine, src, 3)),
        "fine_bottom_completed_linear_dimension": minimal_realization(fine).dimension,
        "coarse_linear_dimension": minimal_realization(coarse).dimension,
        "p_mixed_b_bottom": s(fine.probability("mixed", (("b", "_|_"),))),
        "p_pure_b_bottom": s(fine.probability("pure", (("b", "_|_"),))),
        "illegal_policy_rejected_in_fine": illegal_rejected,
        "illegal_policy_accepted_in_coarse": closed_loop_law(
            coarse, "mixed", lambda u: {"b": Q(1)}, 1) == {(("b", "ok"),): Q(1)},
        "distinguishing_experiment": {"verdict": dist["verdict"], "word": s(dist["word"]),
                                      "legal_in_fine": dist["legal_in_first"]},
        "lawful_positive_dimension": 2,
    }

    # 6. cone theorem round trip on PW1
    gens = [R.vectors[f"d{i}"] for i in range(4)]
    cc = verify_cone(R, gens)
    out["cone_theorem_round_trip_PW1"] = {
        "valid": cc.valid, "generators": 4,
        "column_stochastic": all(
            sum((cc.event_matrices[a][z][j][i] for z in cc.event_matrices[a] for j in range(4)), Q(0)) == 1
            for a in cc.event_matrices for i in range(4)),
        "equivalent": equivalence_certificate(pw, carrier_from_cone(cc))["equivalent"],
    }

    out["scope"] = {
        "empirically_authenticated_source": False,
        "rational_vs_real_positive_dimension_gap_exhibited_here": False,
        "restricted_vs_unrestricted_cone_gap_exhibited_here": False,
        "whole_program_Lean_refinement_proved": False,
        "general_decidability_of_finite_positive_dimension_claimed": False,
        "main_merge_executed": False,
    }
    return out


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
