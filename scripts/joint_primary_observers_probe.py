"""Exact joint-primary observer calibration; no asymptotic normality inference."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from math import isqrt
from pathlib import Path
import json

from observational_succ.joint_primary_observers import (
    bbp_joint_primary_certificate, circle_distance, escaping_prime_history,
    independent_marginal_phase_law, joint_primary_fiber, joint_primary_phases,
    primary_fiber_points, prime_support, short_arc_crt_control,
    source_matching_prime_escape, temporal_mixed_phase_law,
)


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def main():
    fiber_cases = []
    points_checked = 0
    for D in (6, 15, 21, 45, 105):
        ps = prime_support(D)
        for k in range(len(ps)+1):
            for chosen in combinations(ps, k):
                groups = defaultdict(list)
                for a in range(D):
                    x = Q(a, D)
                    groups[joint_primary_phases(x, chosen)].append(x)
                for observed, expected in groups.items():
                    pairs = tuple(zip(chosen, observed))
                    data = joint_primary_fiber(D, pairs)
                    assert primary_fiber_points(D, pairs) == tuple(expected)
                    R = data["residual_modulus"]
                    anchor = expected[0]
                    radius = min(max(circle_distance(x-anchor-Q(j, 2*R)) for x in expected)
                                 for j in range(2*R))
                    assert radius == data["optimal_real_radius"]
                    points_checked += len(expected)
                fiber_cases.append({"D": D, "observed_primes": chosen,
                                    "fiber_count": len(groups),
                                    "fiber_size": data["residual_modulus"],
                                    "optimal_radius": data["optimal_real_radius"]})

    crt_rows = []
    for moduli in ((5, 7, 11), (17, 19, 23), (47, 53, 59)):
        D = 1
        for q in moduli:
            D *= q
        L = D//isqrt(min(moduli))
        control = short_arc_crt_control(moduli, L)
        for row in control["proper_marginals"]:
            q = row["modulus"]
            counts = Counter(a % q for a in range(L))
            direct = sum((abs(Q(counts[a], L)-Q(1, q)) for a in range(q)), Q())/2
            assert direct == row["TV"]
        crt_rows.append(control)

    escape_rows = []
    for constant in (Q(1), Q(1, 3)):
        data = escaping_prime_history(constant, 80)
        rows = data["rows"]
        chosen = tuple(row["prime"] for row in rows[:5])
        for row in rows:
            n = row["n"]
            assert row["state"].denominator == row["denominator"]
            assert 32**n <= row["denominator"] < 2*64**n
            assert 2*row["numerator_multiple"] <= 2**n
            assert row["tail_lower"] <= row["tail"] < row["tail_upper"]
            assert row["tail_upper"] <= row["uniform_tail_upper"]
            assert row["forcing"] > 0
            if n > 5:
                assert joint_primary_phases(row["state"], chosen) == (Q(),)*5
            if n >= 32:
                for p, power in ((2, 3), (3, 1), (5, 1)):
                    assert row["state"].denominator % p != 0
                    assert row["state"].numerator % p**power == 0
                    assert row["forcing"].denominator % p != 0
                    assert row["forcing"].numerator % p**power == 0
        escape_rows.append({"constant": constant, "base": 16, "horizon": 80,
                            "fixed_primary_observers": chosen,
                            "all_after_index_5_primary_phases_zero": True,
                            "after_index_31_absolute_precision": {"2": 3, "3": 1, "5": 1},
                            "last_real_distance_to_constant": circle_distance(rows[-1]["phase"]-constant),
                            "last_tail_upper": rows[-1]["uniform_tail_upper"],
                            "changed_forcing": True})

    authentic_rows = []
    comparisons = 0
    for n in (3, 7, 17, 43):
        data = bbp_joint_primary_certificate(n)
        state = Q()
        for j in range(1, n+1):
            r = Q(4, 8*j-7)-Q(2, 8*j-4)-Q(1, 8*j-3)-Q(1, 8*j-2)
            state = 16*state+r
            assert state % 1 == data["reconstructed_phases"][j-1]
            assert state.denominator == data["individual_denominators_d_n"][j-1]
            comparisons += 1
        authentic_rows.append({"horizon": n, "common_carrier_D_N": data["common_carrier_D_N"],
                               "last_individual_denominator_d_N": data["individual_denominators_d_n"][-1],
                               "prime_support_size": len(data["prime_support"]),
                               "sampling_obstruction": data["sampling_obstruction"]})

    matching_rows = []
    matching_comparisons = 0
    for constant in (Q(1), Q(1, 3)):
        rows = source_matching_prime_escape(constant, 65)["rows"]
        for row in rows:
            n = row["n"]
            assert row["state"].denominator == row["original_denominator"]*row["new_prime_denominator"]
            assert row["tail_lower"] <= row["tail"] < row["tail_upper"] <= row["uniform_tail_upper"]
            assert 16*n < row["prime"] < 32*n
            assert row["forcing"] > 0
            # Every prime in the full authenticated real conductor bound.
            for p in range(2, 8*n+1):
                if all(p % d for d in range(2, isqrt(p)+1)):
                    for left, right in (("state", "original_state"), ("forcing", "original_forcing")):
                        assert joint_primary_phases(row[left], (p,)) == joint_primary_phases(row[right], (p,))
                        matching_comparisons += 1
        last = rows[-1]
        matching_rows.append({"constant": constant, "horizon": 65,
                              "all_primes_at_most_8n_match_at_every_checked_time": True,
                              "extra_prime_at_last_time": last["prime"],
                              "original_denominator_at_last_time": last["original_denominator"],
                              "extra_prime_power_denominator_at_last_time": last["new_prime_denominator"],
                              "tail_upper_at_last_time": last["uniform_tail_upper"],
                              "last_circle_distance_to_constant": circle_distance(last["phase"]-constant),
                              "preserved_logarithmic_height": "same leading-order bounds; added log(q_n)=o(n), by paper proof",
                              "authentic_conductor_preserved": False,
                              "authentic_four_pole_forcing_preserved": False})

    mixed_rows = tuple(joint_primary_phases(x, (3, 5)) for x in (Q(), Q(1, 15)))
    mixed = temporal_mixed_phase_law(mixed_rows)
    independent = independent_marginal_phase_law(mixed_rows)
    assert mixed != independent
    root = Path(__file__).resolve().parents[1]
    paths = ("observational_succ/joint_primary_observers.py",
             "tests/test_joint_primary_observers.py", "scripts/joint_primary_observers_probe.py",
             "observational_succ/source_path_projector.py", "observational_succ/bbp_source_memory.py")
    output = {"status": "exact finite calibration; paper proofs supply stated infinite claims",
              "preregistered_controls": "primary fibers, marginal substitution, moving primes, authentic rational source",
              "post_discovery_strengthening": "factorial numerator gives all fixed p-adic state/forcing limits zero",
              "fiber_cases": len(fiber_cases), "fiber_points_checked": points_checked,
              "fiber_rows": fiber_cases, "proper_CRT_marginal_controls": crt_rows,
              "escaping_prime_controls": escape_rows, "authentic_source_comparisons": comparisons,
              "source_matching_escape_controls": matching_rows,
              "source_matching_primary_comparisons": matching_comparisons,
              "authentic_carrier_rows": authentic_rows,
              "genuine_coprime_temporal_law": mixed, "counterfactual_independent_law": independent,
              "source_sha256": {path: sha256((root/path).read_bytes()).hexdigest() for path in paths},
              "pi_normality": "OPEN", "new_Lean_authority": False}
    print(json.dumps(serial(output), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
