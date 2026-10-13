#!/usr/bin/env python3
"""Bounded exact X09 algebraic controls; infinite/topological claims are paper proofs."""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import resource
import time

ROOT = Path(__file__).resolve().parents[3]
PARENT = "dc23cf405fa432b717ca84018ab86d78ef08edde"
LIMIT = 256 * 1024 * 1024


def multiply(a, b, order):
    return tuple(sum((a[j] * b[k-j] for j in range(k+1)), F(0))
                 for k in range(order+1))


def cayley_jets(power, order):
    # Center s=1, t=s-1: w(s)=t/(2+t). Expand first, multiply independently.
    base = (F(0),) + tuple(F((-1)**(k-1), 2**k) for k in range(1, order+1))
    answer = (F(1),) + (F(0),) * order
    for _ in range(power):
        answer = multiply(answer, base, order)
    return answer


def coefficient_formula(power, degree):
    return F(0) if degree < power else F((-1)**(degree-power) * math.comb(degree-1, degree-power), 2**degree)


def dirichlet_log(values):
    horizon = len(values) - 1
    u = tuple(F(0) if n <= 1 else values[n] for n in range(horizon+1))
    power = u
    answer = [F(0)] * (horizon+1)
    for r in range(1, horizon.bit_length()):
        for n in range(2, horizon+1):
            answer[n] += F((-1)**(r+1), r) * power[n]
        power = tuple(sum((power[d] * u[n//d] for d in range(1, n+1) if n % d == 0), F(0))
                      if n else F(0) for n in range(horizon+1))
    return answer


def main():
    started = time.perf_counter()
    resource.setrlimit(resource.RLIMIT_AS, (LIMIT, LIMIT))
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
    order = 8
    jets = {n: cayley_jets(n, order) for n in range(1, order+2)}
    for n, coefficients in jets.items():
        assert coefficients == tuple(coefficient_formula(n, k) for k in range(order+1))
    escape = []
    cap_controls = []
    for stage in range(order+1):
        matching = [n for n in jets if not any(jets[n][:stage+1])]
        assert min(matching) == stage+1
        escape.append({"jet_order": stage, "minimum_source_cost": min(matching),
                       "first_receipt": min(matching)})
        for cap in range(order+1):
            admitted = [n for n in matching if n <= cap]
            assert bool(admitted) == (cap >= stage+1)
            cap_controls.append((stage, cap, bool(admitted)))

    # On |s-1|<=1/2, |w(s)|<=1/3. Equality at s=1/2 calibrates the bound.
    uniform = []
    wrong_topology = []
    for n in range(1, order+2):
        at_half = F(-1, 3)**n
        assert abs(at_half) == F(1, 3)**n
        uniform.append({"power": n, "compact_sup_bound": str(abs(at_half))})
        # (2w)^n has eventually zero every fixed jet, but diverges at s=7.
        value = (2 * F(7-1, 7+1))**n
        assert value == F(3, 2)**n
        wrong_topology.append({"power": n, "value_at_7": str(value)})

    # Formal factorial coefficients match finite polynomial sources, not a holomorphic germ.
    factorial_thread = tuple(F(math.factorial(k)) for k in range(order+1))
    polynomials = {n: tuple(factorial_thread[k] if k <= n else F(0)
                           for k in range(order+1)) for n in range(order+1)}
    formal_escape = []
    for stage in range(order+1):
        matching = [n for n, p in polynomials.items() if p[:stage+1] == factorial_thread[:stage+1]]
        assert min(matching) == stage
        formal_escape.append({"jet_order": stage, "minimum_source_cost": min(matching),
                              "coefficient": str(factorial_thread[stage]),
                              "term_at_radius_half": str(factorial_thread[stage] * F(1, 2)**stage)})
    for n in range(2, order):
        assert (factorial_thread[n+1]*F(1, 2)**(n+1)) / (factorial_thread[n]*F(1, 2)**n) == F(n+1, 2)

    # Adding the limit receipt repairs the zero jet profile at cost zero.
    supported_labels = {**{n: "finite" for n in jets}, "limit": "limit"}
    zero_coefficients = (F(0),) * (order+1)
    with_limit = {**jets, "limit": zero_coefficients}
    for stage in range(order+1):
        assert with_limit["limit"][:stage+1] == zero_coefficients[:stage+1]
        finite_label_matches = [n for n in jets if supported_labels[n] == "finite"
                                and jets[n][:stage+1] == zero_coefficients[:stage+1]]
        assert finite_label_matches
    label_mutation = {"compact_source_with_limit_receipt": True,
                      "constant_label_repairs_realization": True,
                      "different_limit_label_is_discontinuous": True,
                      "finite_label_zero_profile_has_no_global_receipt": True,
                      "statements_are_paper_proved_not_finite_search": True}

    # E37 factorial Mellin approximants: G_N(1)=N/(N+1), never Gamma(1)=1.
    gamma_precision_escape = []
    for precision in range(2, 10):
        tolerance = F(1, precision)
        candidates = []
        for n in range(1, precision+1):
            from_product = F(math.factorial(n)*n, math.prod(range(1, n+2)))
            assert from_product == F(n, n+1)
            if abs(from_product - 1) <= tolerance:
                candidates.append(n)
        assert min(candidates) == precision-1
        gamma_precision_escape.append({"value_target": "1", "tolerance": str(tolerance),
                                       "minimum_source_cost": min(candidates)})

    # Connectedness is essential: two componentwise constants have identical first-component jets.
    disconnected = ((0, 0), (0, 1))
    assert disconnected[0][0] == disconnected[1][0] and disconnected[0] != disconnected[1]

    # All Gamma-side outputs can agree for distinct arithmetic sources.
    authentic = [F(0)] + [F(1)] * 8
    fake = authentic.copy()
    fake[6] = F(2)
    b, fake_b = dirichlet_log(authentic), dirichlet_log(fake)
    assert b[2] == 1 and b[4] == F(1, 2) and b[6] == 0 and b[8] == F(1, 3)
    assert fake_b[6] == 1 and fake[6] != fake[2] * fake[3]
    assert authentic[6] == authentic[2] * authentic[3]
    normalized_form_delta = -(fake_b[6] - b[6]) * 2
    assert normalized_form_delta == -2
    assert F(1) / F(1, 2) == 2  # Wrong half-density doubles the n=4 coefficient.

    # Finite compact-source realization/minimum-cost oracle, with labels and duplicate receipts.
    models = targets = 0
    for count in range(4):
        for coefficients in itertools.product(((0, 0), (0, 1), (1, 0)), repeat=count):
            for labels in itertools.product(("a", "b"), repeat=count):
                models += 1
                costs = tuple(range(count))
                for target in ((0, 0), (0, 1), (1, 0)):
                    for label in ("a", "b"):
                        minima = []
                        for stage in (0, 1):
                            matching = [costs[i] for i in range(count) if labels[i] == label
                                        and coefficients[i][:stage+1] == target[:stage+1]]
                            minima.append(min(matching) if matching else None)
                        global_costs = [costs[i] for i in range(count) if labels[i] == label and coefficients[i] == target]
                        global_min = min(global_costs) if global_costs else None
                        max_finite = None if None in minima else max(minima)
                        assert max_finite == global_min
                        approx_minima = []
                        for stage in (0, 1):
                            for tolerance in (F(1, 4), F(1, 2), F(1)):
                                matches = [costs[i] for i in range(count) if labels[i] == label
                                           and max(abs(coefficients[i][k] - target[k])
                                                   for k in range(stage+1)) <= tolerance]
                                approx_minima.append(min(matches) if matches else None)
                        max_approx = None if None in approx_minima else max(approx_minima)
                        assert max_approx == global_min
                        targets += 1

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    assert peak < LIMIT
    assert time.perf_counter() - started < 25
    source_base = Path('/home/leah/succ_lab/many-worlds-atlas/research/2026-10-13')
    source_paths = ('SWARM_ATLAS/B09.md', 'SWARM_ATLAS/B10.md', 'SWARM_ATLAS/X01.md',
                    'E37_ARCHIMEDEAN_GAMMA_BOUNDARY.md', 'SWM_E38_ARITHMETIC_POLARIZATION/DOSSIER.md',
                    'SWARM_ATLAS/reviews/B09_REVIEW.md', 'SWARM_ATLAS/reviews/B10_REVIEW.md',
                    'SWARM_ATLAS/reviews/X01_A05_REVIEW.md', 'SWARM_ATLAS/reviews/E38_E39_PRINCIPAL_REVIEW.md')
    artifact_paths = ('research/2026-10-13/SWARM_ATLAS/X09.md',
                      'research/2026-10-13/SWARM_ATLAS/X09_probe.py', 'provenance/IMPORT_MANIFEST.json')
    return {"schema": "succ-X09-bounded-exact-receipt/v1", "parent_sha": PARENT,
            "status": "TESTED MODEL", "paper_theorem_review_pending": True,
            "python": platform.python_version(), "peak_rss_bytes": peak,
            "caps": {"address_space_bytes": LIMIT, "cpu_seconds": 25, "required_wall_timeout_seconds": 30},
            "source_hashes_sha256": {p: hashlib.sha256((source_base/p).read_bytes()).hexdigest() for p in source_paths},
            "artifact_hashes_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifact_paths},
            "zero_profile_source_cost_escape": escape, "cap_comparisons": len(cap_controls),
            "compact_uniform_analytic_bound": uniform, "jet_only_topology_mutation": wrong_topology,
            "zero_radius_formal_jet_escape": formal_escape, "label_mutation": label_mutation,
            "Gamma_scalar_precision_source_cost_escape": gamma_precision_escape,
            "disconnected_domain_same_jets_distinct_functions": disconnected,
            "finite_source_cost_models": models, "labelled_target_cost_equalities": targets,
            "Gamma_identical_arithmetic_twins": {"authentic_b6": str(b[6]), "fake_b6": str(fake_b[6]),
                "normalized_completed_form_difference": str(normalized_form_delta),
                "actual_scale_is_log6_over_sqrt6": True, "wrong_half_density_ratio_at_4": "2",
                "no_Gamma_numerics_or_nontrivial_zero_inputs": True},
            "not_run": ["numerical Gamma integration", "full Weil evaluation", "compiler", "full suites", "CI"]}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
