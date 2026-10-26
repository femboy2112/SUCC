#!/usr/bin/env python3
"""Replay exact selected-phase witnesses; never promote them to normality.

Run from an installed repository environment. --verify regenerates the
entire receipt, including source hashes and authority flags, before comparing.
Analytic implications are paper proofs; no floating Fourier values are used.
"""
from dataclasses import asdict, is_dataclass
from fractions import Fraction as Q
from hashlib import sha256
import argparse
import json
from pathlib import Path

from observational_succ.bbp_clock_transport import (
    clock_transport_budget, congruent_seed_control, rational_valuation,
    root_energy_transport_squared, verify_congruent_seed_control,
    weighted_spectral_excess,
)
from observational_succ.bbp_diophantine_coherence import (
    BLOCK_LOSS, authentic_block_certificate, approximation_coefficient_bound,
    conditional_budget, terminal_control_loss_upper, terminal_zero_control,
)
from observational_succ.bbp_positive_carry_control import (
    positive_carry_control, positive_control_tail_constants,
)
from observational_succ.bbp_sparse_carry_transport import (
    authentic_carry_profiles, birth_carry_budget, carry_kernel_budget,
    finite_carry_profile, truncation_depth, truncation_root_error_squared,
)
from observational_succ.succ_internal_matrix_walk import source_cyclotomic_quotient


ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    "observational_succ/bbp_clock_transport.py",
    "observational_succ/bbp_diophantine_coherence.py",
    "observational_succ/bbp_positive_carry_control.py",
    "observational_succ/bbp_sparse_carry_transport.py",
    "observational_succ/succ_internal_matrix_walk.py",
    "observational_succ/spectral_purity_arithmetic.py",
    "observational_succ/spectral_purity_innovation.py",
    "observational_succ/gamma_bbp_signed_coherence.py",
    "observational_succ/finite_fourier_carrier.py",
    "formal/SelectedPhase.lean",
    "scripts/check_selected_phase_lean.py",
    "scripts/pi_selected_phase_probe.py",
)


def exact(value):
    if isinstance(value, Q):
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    if is_dataclass(value):
        return exact(asdict(value))
    if isinstance(value, dict):
        return {k: exact(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [exact(v) for v in value]
    return value


def digest(value):
    return sha256(json.dumps(exact(value), sort_keys=True).encode()).hexdigest()


def rational_evaluation(polynomial):
    value = source_cyclotomic_quotient(polynomial, modulus_cap=256)
    if len(value.polynomial) > 1:
        raise ArithmeticError("expected a rational cyclotomic value")
    return value.polynomial[0]


def build_receipt():
    arcs = []
    for m, h in ((1, 1), (3, -2), (11, 121), (23, -17), (37, -1369)):
        c = authentic_block_certificate(m, h)
        if not (c.authentic_zero_anchor and c.backward_identity_defect == 0
                and c.inverse.outside_arcs and c.inverse.branch_span < 1):
            raise ArithmeticError("authentic inverse witness failed")
        arcs.append({"m": m, "h": h, "block_length": c.inverse.observations,
                     "branch_span": c.inverse.branch_span,
                     "distance_to_centers": c.inverse.distance_to_centers,
                     "arc_radius": c.inverse.arc_radius,
                     "absolute_loss_threshold": c.inverse.absolute_loss_threshold,
                     "full_certificate_sha256": digest(c)})

    wrong_anchors = []
    for m in (3, 7, 19):
        c = terminal_zero_control(m)
        upper = terminal_control_loss_upper(m)
        if (c.authentic_zero_anchor or c.terminal_state != 0
                or c.inverse.distance_to_centers != 0 or upper >= BLOCK_LOSS):
            raise ArithmeticError("wrong-anchor control failed")
        wrong_anchors.append({"m": m, "initial": c.source_initial,
                              "absolute_loss_upper": upper,
                              "authentic_zero_anchor": False,
                              "same_four_pole_forcing": True})

    sharp = []
    for H in (2, 5, 9):
        phases = tuple(Q(j, H) for j in range(H))
        weights = [Q(1, H)]*H
        zero = rational_evaluation(weighted_spectral_excess(phases, tuple(weights), H))
        amount = Q(1, 3*H)
        weights[0] += amount
        weights[1] -= amount
        actual = rational_evaluation(weighted_spectral_excess(phases, tuple(weights), H))
        cap = root_energy_transport_squared(H, 2*amount)
        if zero != 0 or actual != cap:
            raise ArithmeticError("sharp transport equality failed")
        sharp.append({"H": H, "l1_distance": 2*amount, "energy": actual,
                      "sharp_squared_bound": cap,
                      "authority": "EXACT FINITE cyclotomic evaluation"})

    seeds = []
    for N, m, depths in ((8, 3, ((2, 3), (3, 4), (7, 3))),
                          (37, 19, ((2, 8), (3, 5), (5, 5), (17, 3)))):
        c = congruent_seed_control(N, m, depths)
        verify_congruent_seed_control(c)
        slack = min(rational_valuation(v-u, p)-k-(4*n if p == 2 else 0)
                    for n, (u, v) in enumerate(zip(c.authentic_history, c.changed_history), 1)
                    for p, k in depths)
        seeds.append({"N": N, "m": m, "prime_depths": depths,
                      "initial": c.initial, "minimum_valuation_slack": slack,
                      "window_radius": c.window_radius,
                      "all_partition_gain_upper_h1": c.gain_upper_h1,
                      "full_certificate_sha256": digest(c),
                      "authentic_zero_initial": False,
                      "single_infinite_counterexample_claimed": False})

    positive = positive_carry_control(128)
    positive_rows = [positive[n-1] for n in (1, 14, 64, 128)]
    if not all(p.control_forcing > 0 and 0 <= p.control_phase <= p.authentic_lift % 1
               for p in positive):
        raise ArithmeticError("positive carry counterfeit failed")

    budgets = []
    for N in (2**16, 2**64, 2**256):
        budget = birth_carry_budget(N)
        J = truncation_depth(N, budget.width)
        budgets.append({"transport": budget, "future_read_depth": J,
                        "truncation_root_error_squared":
                        truncation_root_error_squared(budget.width, J)})
    profiles = authentic_carry_profiles(32, 11)
    future_example = finite_carry_profile((0,)*16+(8,), 16, 1)
    if future_example != Q(1, 2):
        raise ArithmeticError("future-boundary counterexample failed")

    return exact({
        "schema": "succ-pi-selected-phase-v1",
        "base_commit": "b792caae40dfe777cf7e9d3301b61f1ac0adac41",
        "source": {"initial": 0, "poles": [[4, 8, -7], [-2, 8, -4],
                                              [-1, 8, -3], [-1, 8, -2]],
                   "lift": "U_n=16 U_(n-1)+r(n)"},
        "source_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES},
        "authority": "EXACT FINITE witnesses and rational budgets; analytic claims in linked dossiers",
        "pi_normality_proved": False,
        "numerical_diophantine_threshold_certified": False,
        "classical_irrationality_input": "https://arxiv.org/abs/1912.06345v2",
        "authentic_arc_exclusions": arcs,
        "approximation_coefficient_uniform_upper": approximation_coefficient_bound(1),
        "wrong_anchor_terminal_controls": wrong_anchors,
        "illustrative_conditional_budget_not_a_certified_threshold": conditional_budget(8**12, 65537, 2),
        "sharp_clock_equalities": sharp,
        "actual_clock_budgets": [clock_transport_budget(37, 9, 7),
                                  clock_transport_budget(36, 9, 7)],
        "finite_local_seed_controls": seeds,
        "positive_carry_control": {
            "prefix_length": 128, "prefix_sha256": digest(positive),
            "selected_rows": positive_rows,
            "analytic_tail_constants": positive_control_tail_constants(),
            "authentic_forcing": False, "same_carries_and_common_tower": True},
        "sparse_carry_transport_budgets": budgets,
        "kernel_holdouts": [carry_kernel_budget(h) for h in (1, 73, 74, 1171, 65537)],
        "authentic_carry_profile": {
            "horizon": profiles.horizon, "depth": profiles.depth,
            "prefix_sha256": digest(profiles), "uniform_tail_upper": profiles.uniform_tail_upper,
            "births_in_observed_horizon": sum(p.conductor_birth for p in profiles.source[:32]),
            "purity_proved": False},
        "future_only_mutation": {"N": 16, "changed_observed_carries": 0,
                                 "last_phase_change": future_example,
                                 "boundary_free_estimate_refuted": True},
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", type=Path)
    action.add_argument("--verify", type=Path)
    args = parser.parse_args()
    receipt = build_receipt()
    if args.verify:
        if json.loads(args.verify.read_text()) != receipt:
            raise SystemExit("FAIL: receipt differs from exact replay or current source hashes")
        print("PASS: exact selected-phase receipt replay; normality remains OPEN")
    elif args.write:
        args.write.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
        print(f"WROTE: {args.write}; finite witnesses only")
    else:
        print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
