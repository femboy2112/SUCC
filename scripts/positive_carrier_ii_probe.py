#!/usr/bin/env python3
"""Positive carrier realization, Part II: frozen exact receipt.

Reproduces every finite certificate quoted in
research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY_II.md in exact
rational (and exact Q(sqrt5)) arithmetic.  Fractions and quadratic numbers
are serialized as strings; the JSON is byte-compared in CI.
"""
from __future__ import annotations

import json
from fractions import Fraction as Q

from observational_succ.carrier_field_of_definition import (
    Quad, fibonacci_cat_system, golden_carrier, golden_rays, quadratic_cone_carrier,
    rational_interval_invariance, rational_interval_search, rational_root_free,
    two_dimensional_contact_certificate,
)
from observational_succ.carrier_lawful_profile import (
    diagonal_contraction_system, ghost_block_certificate, minimal_lawful_phantom,
    operational_profile, phantom_walk_carrier, profile_equivalence_certificate,
    public_menu, simplicial_grid_search, support_uniform_completion,
)
from observational_succ.carrier_realization import (
    availability_square, carrier_from_cone, carrier_realization_oracle, charpoly,
    cone_coordinates, dot, equivalence_certificate, matvec, minimal_realization,
    normalize_ray, path_walk_carrier, reachable_cone_refinement, verify_cone,
)


def s(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, Quad):
        return f"{x.a}+{x.b}*sqrt{x.D}"
    if isinstance(x, frozenset):
        return sorted(s(y) for y in x)
    if isinstance(x, (list, tuple)):
        return [s(y) for y in x]
    if isinstance(x, dict):
        return {str(k): s(v) for k, v in x.items()}
    if hasattr(x, "__dataclass_fields__"):
        return None
    return x


def report() -> dict:
    out: dict = {"schema": "SUCC-POSITIVE-CARRIER-2",
                 "status": "EXACT_POSITIVE_CARRIER_FIELD_OF_DEFINITION_AND_GHOST_FREEDOM",
                 "part_i_receipt": "research/2026-10-13/POSITIVE_CARRIER_RECEIPT.json"}

    # ---------------- 1. Fibonacci cat system: Q/R separation at r = 2 ----------------
    fib = fibonacci_cat_system()
    R = minimal_realization(fib)
    letters = [(a, z) for a in fib.actions for z in fib.outcomes(a)]
    frontier = [fib.preparations["s"]]
    checked = 0
    negative = 0
    for _ in range(7):
        nxt = []
        for v in frontier:
            for a, z in letters:
                u = matvec(fib.event(a, z), v)
                checked += 1
                if dot(fib.mass, u) < 0:
                    negative += 1
                if any(x != 0 for x in u):
                    nxt.append(u)
        frontier = nxt
    orbit_a, orbit_b = [], []
    v = fib.preparations["s"]
    for _ in range(7):
        orbit_a.append(v[1] / v[0])
        v = matvec(fib.events["a"]["tick"], v)
    v = fib.preparations["s"]
    for _ in range(7):
        orbit_b.append(v[1] / v[0])
        v = matvec(fib.events["b"]["tock"], v)
    gc = golden_carrier()
    cert = two_dimensional_contact_certificate(fib, (("a", "tick"),), (("b", "tock"),))
    e, ep = golden_rays()
    out["fibonacci_cat_system"] = {
        "events": s({a: {z: fib.events[a][z] for z in fib.outcomes(a)} for a in fib.actions}),
        "mass": s(fib.mass), "source": s(fib.preparations["s"]),
        "mass_conserving": fib.mass_conserving(),
        "linear_dimension": R.dimension,
        "words_checked_nonnegative": {"lengths": "1..7", "checked": checked, "negative": negative},
        "charpoly_tick": s(charpoly(fib.events["a"]["tick"])),
        "charpoly_tock": s(charpoly(fib.events["b"]["tock"])),
        "orbit_slopes_tick": s(orbit_a), "orbit_slopes_tock": s(orbit_b),
        "golden_rays_tau_normalized": {"e": s(e), "e_prime": s(ep)},
        "real_two_state_carrier_over_Q_sqrt5": {
            "intertwining_exact": gc.intertwining_exact, "nonnegative": gc.nonnegative,
            "column_stochastic": gc.column_stochastic, "preparation_convex": gc.preparations_convex,
            "all_entries_rational": gc.all_entries_rational,
            "event_matrices": s(gc.event_matrices), "preparation": s(gc.preparations),
        },
        "irrational_contact_certificate": s({k: v for k, v in cert.items()}),
        "golden_polynomial_rational_root_check": s(rational_root_free([Q(1), Q(1), Q(-1)])),
        "rational_interval_controls": s([
            {"interval": (p, q), "invariant_sandwiched":
             rational_interval_invariance(R, p, q)["invariant_sandwiched"]}
            for (p, q) in [(Q(-2), Q(1)), (Q(-17, 10), Q(7, 10)), (Q(-55, 34), Q(55, 89))]]),
        "rational_interval_grid_search": s({k: v for k, v in rational_interval_search(
            R, denominators=(1, 2, 3, 4, 5, 6), bound=3).items() if k != "certificate"}),
        "reachable_cone_refinement": s({k: v for k, v in reachable_cone_refinement(
            R, depth=4, max_generators=12, max_rounds=12).items() if k not in ("certificate", "generators")}),
        "positive_dimension_over_R": 2, "positive_dimension_over_Q": "infinity",
        "lean_kernel_checked_core": "formal/EODCS_PositiveCarrierII.lean:golden_slope_irrational",
    }

    # positive control for Theorem II.4: a rational r = 2 behavior with a rational interval
    fine, coarse = availability_square()
    Rf = minimal_realization(fine)
    search = rational_interval_search(Rf)
    ctrl = {"linear_dimension": Rf.dimension, "verdict": search["verdict"],
            "interval": s(search.get("interval")), "tried": search.get("tried")}
    if search["verdict"] == "LAWFUL_REALIZATION":
        car = carrier_from_cone(search["certificate"])
        ctrl["carrier_dimension"] = car.dimension
        ctrl["equivalence"] = s(equivalence_certificate(fine, car))
    out["dimension_two_dichotomy_positive_control"] = ctrl

    # ---------------- 2. ghost freedom: phantom walks ----------------
    ghost = {}
    for copies, legal in ((1, False), (1, True), (2, False)):
        ph = phantom_walk_carrier(copies, legal_source=legal)
        mini = minimal_lawful_phantom(copies, legal_source=legal)
        prof = operational_profile(ph, 2)
        eq = profile_equivalence_certificate(ph, mini)
        gcert = ghost_block_certificate(ph, "sigma", "a")
        entry = {
            "copies": copies, "legal_source": legal,
            "carrier_states": ph.dimension,
            "menus_in_profile_depth_2": sorted(s(m) for m in prof.menus()),
            "profile_entries_depth_2": len(prof.entries),
            "minimal_lawful_states": mini.dimension,
            "same_operational_profile": eq["same_operational_profile"],
            "refusal_completion_sizes": eq["refusal_completion_sizes"],
            "linear_dimension_bottom_completion": minimal_realization(ph).dimension,
            "linear_dimension_minimal_lawful_completion": minimal_realization(mini).dimension,
            "ghost_block_rank": gcert["block_rank"], "ghost_fooling_size": gcert["fooling_size"],
            "ghost_fooling_cells": s(gcert["fooling_set"]),
            "refusal_mass_at_sigma": s(gcert["refusal_mass"]),
            "a_available_at_sigma": gcert["action_available_at_source"],
            "bottom_completion_lower_bound": gcert["bottom_completion_lower_bound"],
        }
        if legal:
            entry["public_menu_prior_half_half"] = {
                "empty_history": s(public_menu(ph, {"sigma": Q(1, 2), "eta": Q(1, 2)}, ())),
                "after_a_report_0": s(public_menu(ph, {"sigma": Q(1, 2), "eta": Q(1, 2)}, (("a", (0,)),))),
            }
        ghost[f"PH{copies}{'_legal_source' if legal else ''}"] = entry
    sq = profile_equivalence_certificate(fine, coarse)
    pw = path_walk_carrier(1)
    rep = carrier_realization_oracle(pw, proposed_dimension=4)
    ghost["negative_control_availability_square"] = s(sq)
    ghost["positive_control_PW1_vs_cone_carrier"] = profile_equivalence_certificate(pw, rep["carrier"])["same_operational_profile"]
    ghost["support_uniform_completion_sizes"] = {
        "PW1": support_uniform_completion(pw).dimension,
        "FINE": support_uniform_completion(fine).dimension,
        "COARSE": support_uniform_completion(coarse).dimension,
    }
    out["ghost_freedom"] = ghost

    # ---------------- 3. blind spot: diagonal contraction ----------------
    ds = diagonal_contraction_system()
    Rd = minimal_realization(ds)
    refine = reachable_cone_refinement(Rd, depth=3, max_generators=14)
    grid = simplicial_grid_search(Rd, system=ds, denominators=(1, 2), bound=2, max_candidates=50000)
    # finite extremality evidence: orbit rays g_0..g_7 from s_* are pairwise non-redundant
    rays = []
    v = Rd.vectors["sstar"]
    for _ in range(8):
        rays.append(normalize_ray(Rd, v))
        v = matvec(Rd.operators["clock"]["tick"], v)
    axis = normalize_ray(Rd, Rd.vectors["s0"])
    extreme = []
    for i, g in enumerate(rays):
        others = [axis] + [h for j, h in enumerate(rays) if j != i]
        extreme.append(cone_coordinates(others, g) is None)
    entry = {
        "linear_dimension": Rd.dimension,
        "mass_conserving": ds.mass_conserving(),
        "reachable_ray_refinement": s({k: v for k, v in refine.items() if k not in ("certificate", "generators")}),
        "orbit_rays_extreme_in_cone_of_others_and_axis": extreme,
        "grid_search_verdict": grid["verdict"], "grid_candidates_tried": grid.get("tried"),
        "grid_denominator": grid.get("denominator"),
    }
    if grid["verdict"] == "LAWFUL_REALIZATION":
        car = carrier_from_cone(grid["certificate"])
        entry["carrier_dimension"] = car.dimension
        entry["generators_in_realization_coordinates"] = s(grid["generators"])
        entry["equivalence"] = s(equivalence_certificate(ds, car))
        entry["event_matrices"] = s({a: {z: car.events[a][z] for z in car.outcomes(a)} for a in car.actions})
        entry["preparations"] = s(car.preparations)
    out["blind_spot_diagonal_contraction"] = entry

    out["scope"] = {
        "empirically_authenticated_source": False,
        "rational_vs_real_positive_dimension_gap_exhibited_here": True,
        "rational_vs_real_gap_is_infinite_at_linear_dimension_two": True,
        "ghost_gap_d_law_strictly_below_d_bottom_exhibited_here": True,
        "bottom_completion_is_weakest_repair": False,
        "reachable_ray_refinement_complete": False,
        "general_decidability_of_finite_positive_dimension_claimed": False,
        "general_decidability_of_rational_positive_dimension_claimed": False,
        "cone_theorem_identities_lean_formalized_over_commutative_semiring": True,
        "cone_theorem_lean_formalized_over_Q": False,
        "main_merge_executed": False,
    }
    return out


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
