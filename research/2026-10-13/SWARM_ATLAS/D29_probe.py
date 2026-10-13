#!/usr/bin/env python3
"""Independent exact finite-map crucible; no SUCC runtime imports or floats."""
from itertools import product
import json


def factor(f, p, m):
    g = [None] * m
    for x, label in enumerate(p):
        successor = p[f[x]]
        if g[label] is not None and g[label] != successor:
            return None
        g[label] = successor
    return tuple(g)


def trim_invariant(f, nhood):
    """Two-sided finite graph pruning, distinct from the orbit oracle below."""
    current = set(nhood)
    while True:
        images = {f[x] for x in current}
        nxt = {x for x in current if f[x] in current and x in images}
        if nxt == current:
            return current
        current = nxt


def orbit_invariant(f, nhood):
    answer = set()
    for root in nhood:
        seen = set()
        x = root
        while x in nhood and x not in seen:
            seen.add(x)
            x = f[x]
        if x == root:
            answer.add(root)
    return answer


def eventual_cycle(f, x):
    path = []
    while x not in path:
        path.append(x)
        x = f[x]
    return set(path[path.index(x):])


def all_subsets(m):
    for bits in product((False, True), repeat=m):
        yield {i for i, bit in enumerate(bits) if bit}


def main():
    counts = {"lawful_maps": 0, "nonintertwining_maps": 0,
              "neighborhood_cases": 0, "orbit_image_cases": 0,
              "bijection_pullback_cases": 0,
              "nonbijection_pullback_failures": 0,
              "independent_invariant_oracle_checks": 0}
    for n in range(1, 5):
        for f in product(range(n), repeat=n):
            bijective = len(set(f)) == n
            for m in range(1, min(n, 3) + 1):
                for p in product(range(m), repeat=n):
                    if set(p) != set(range(m)):
                        continue
                    g = factor(f, p, m)
                    if g is None:
                        counts["nonintertwining_maps"] += 1
                        continue
                    counts["lawful_maps"] += 1
                    for x in range(n):
                        assert {p[z] for z in eventual_cycle(f, x)} == eventual_cycle(g, p[x])
                        counts["orbit_image_cases"] += 1
                    for nhood in all_subsets(m):
                        lifted = {x for x in range(n) if p[x] in nhood}
                        source_inv = trim_invariant(f, lifted)
                        target_inv = orbit_invariant(g, nhood)
                        assert source_inv == orbit_invariant(f, lifted)
                        assert target_inv == trim_invariant(g, nhood)
                        counts["independent_invariant_oracle_checks"] += 2
                        assert {p[x] for x in source_inv} == target_inv
                        counts["neighborhood_cases"] += 1
                        full_pullback = {x for x in range(n) if p[x] in target_inv}
                        if bijective:
                            assert source_inv == full_pullback
                            counts["bijection_pullback_cases"] += 1
                        elif source_inv != full_pullback:
                            counts["nonbijection_pullback_failures"] += 1

    f, p, g = (1, 1), (0, 0), (0,)
    assert factor(f, p, 1) == g
    assert trim_invariant(f, {0, 1}) == {1}
    assert {x for x in range(2) if p[x] in orbit_invariant(g, {0})} == {0, 1}
    noninvertible = {"f": f, "projection": p, "g": g,
                    "Inv_source": [1], "pullback_Inv_target": [0, 1]}

    f, p, g = (1, 0), (0, 0), (0,)
    assert factor(f, p, 1) == g
    period_loss = {"f": f, "projection": p, "g": g,
                   "source_period": 2, "observed_period": 1}

    # A state intervention crosses basins without reconstructing the model.
    f, old_report = (0, 1, 1), (0, 1, 0)
    assert eventual_cycle(f, 0) == {0}
    assert eventual_cycle(f, 2) == {1}
    assert factor(f, old_report, 2) is None
    assert old_report[0] == old_report[2]
    assert old_report[f[0]] != old_report[f[2]]
    refined = (0, 1, 2)
    assert factor(f, refined, 3) == f
    # Finite itineraries certify that no pair can be merged compatibly.
    itineraries = []
    for root in range(3):
        x = root
        word = []
        for _ in range(3):
            word.append(old_report[x])
            x = f[x]
        itineraries.append(word)
    assert len({tuple(w) for w in itineraries}) == 3
    reconstruction = {"f": f, "old_report": old_report,
                      "old_autonomous_transition_exists": False,
                      "same_old_report_next_outputs": [0, 1],
                      "refined_report": refined, "refined_transition": f,
                      "forget_refinement": old_report,
                      "three_step_itineraries": itineraries,
                      "intervention_0_to_2_cycles": [[0], [1]],
                      "original_source_law_edited": False}
    # Identity observation plus the wrong target law is a one-edge mutation.
    f, p, wrong_g = (1, 1), (0, 1), (0, 1)
    assert p[f[0]] != wrong_g[p[0]]
    wrong_square = {"f": f, "projection": p, "wrong_g": wrong_g,
                    "witness_state": 0, "pi_f": 1, "g_pi": 0}
    # Different-sized calibration, outside the exhaustive enumeration domain.
    f, p = (1, 2, 3, 4, 5, 0), (0, 1, 2, 0, 1, 2)
    g = factor(f, p, 3)
    assert g == (1, 2, 0)
    for nhood in all_subsets(3):
        lifted = {x for x in range(6) if p[x] in nhood}
        assert trim_invariant(f, lifted) == {
            x for x in range(6) if p[x] in orbit_invariant(g, nhood)}
    outside_domain = {"f": f, "projection": p, "g": g,
                      "source_period": 6, "observed_period": 3,
                      "all_eight_neighborhoods_checked": True}
    print(json.dumps({"domain": "finite deterministic maps; n<=4, m<=3",
                      "arithmetic": "exact integers; no runtime imports",
                      "counts": counts,
                      "controls": {"noninvertible_pullback": noninvertible,
                                   "period_loss": period_loss,
                                   "representation_reconstruction": reconstruction,
                                   "nonintertwining": wrong_square,
                                   "outside_domain_permutation": outside_domain},
                      "index_computed_by_probe": False,
                      "physical_source_authenticated": False}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
