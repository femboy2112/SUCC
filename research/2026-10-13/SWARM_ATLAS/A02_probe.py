#!/usr/bin/env python3
"""Tiny exact A02 controls; finite tests calibrate, not prove the universal theorem.

The independent oracle uses tuple arrows and a literal naturality enumerator.
No imported module or historical receipt is modified. At most 3 DAG vertices,
2 parallel generators per endpoint, and 8 probe families in the sweep.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))


class TinyCategory:
    def __init__(self, objects, homs, composites):
        self.objects = tuple(objects)
        self.homs = homs
        self.composites = composites

    def hom(self, x, y):
        return self.homs.get((x, y), ())

    def compose(self, left, right):
        assert right[1] == left[0]
        return self.composites[(left, right)]

    def verify(self):
        arrows = [f for x in self.objects for y in self.objects for f in self.hom(x, y)]
        for x in self.objects:
            identity = (x, x, ())
            assert identity in self.hom(x, x)
        for f in arrows:
            assert self.compose((f[1], f[1], ()), f) == f
            assert self.compose(f, (f[0], f[0], ())) == f
        triples = 0
        for f, g, h in itertools.product(arrows, repeat=3):
            if f[1] == g[0] and g[1] == h[0]:
                assert self.compose(h, self.compose(g, f)) == self.compose(self.compose(h, g), f)
                triples += 1
        return {"objects": len(self.objects), "arrows": len(arrows), "associative_triples": triples}


def free_dag(n, generators):
    assert 1 <= n <= 3 and len(generators) <= 6
    assert all(0 <= x < y < n for x, y in generators)
    homs = {(x, y): [] for x in range(n) for y in range(n)}
    for x in range(n):
        def walk(y, word):
            homs[x, y].append((x, y, word))
            for token, (source, target) in enumerate(generators, 1):
                if source == y:
                    walk(target, word + (token,))
        walk(x, ())
    homs = {k: tuple(v) for k, v in homs.items()}
    arrows = [f for fs in homs.values() for f in fs]
    composites = {(g, f): (f[0], g[1], f[2] + g[2])
                  for f in arrows for g in arrows if f[1] == g[0]}
    return TinyCategory(range(n), homs, composites)


def transformations(category, a, b, probes):
    options = []
    candidate_count = 1
    for j in probes:
        domain, codomain = category.hom(j, a), category.hom(j, b)
        candidate_count *= len(codomain) ** len(domain)
        assert candidate_count <= 64, "Only the tiny controls enumerate natural transformations"
        options.append([dict(zip(domain, values))
                        for values in itertools.product(codomain, repeat=len(domain))])
    answer = []
    for components in itertools.product(*options):
        eta = dict(zip(probes, components))
        if all(eta[j][category.compose(v, u)] == category.compose(eta[k][v], u)
               for j in probes for k in probes for u in category.hom(j, k)
               for v in category.hom(k, a)):
            answer.append(eta)
    return answer


def represented(category, f, probes):
    return {j: {u: category.compose(f, u) for u in category.hom(j, f[0])} for j in probes}


def faithful(category, probes):
    return all(any(category.compose(f, u) != category.compose(g, u)
                   for j in probes for u in category.hom(j, x))
               for x in category.objects for y in category.objects
               for f, g in itertools.combinations(category.hom(x, y), 2))


def full(category, probes):
    return all(all(eta in [represented(category, f, probes) for f in category.hom(x, y)]
                   for eta in transformations(category, x, y, probes))
               for x in category.objects for y in category.objects)


def restricted_isomorphic(category, x, y, probes):
    return any(all(len(component) == len(set(component.values())) == len(category.hom(j, y))
                   for j, component in eta.items())
               for eta in transformations(category, x, y, probes))


def separates_objects(category, probes):
    # Every control here is skeletal. The idempotent e is not invertible.
    return all(not restricted_isomorphic(category, x, y, probes)
               for x, y in itertools.combinations(category.objects, 2))


def criterion(category, probes):
    branching = [x for x in category.objects
                 if any(len(category.hom(x, y)) >= 2 for y in category.objects)]
    return all(any(category.hom(j, x) for j in probes) for x in branching)


def control(category, probes):
    return {"probes": list(probes), "object_separating": separates_objects(category, probes),
            "faithful": faithful(category, probes), "full": full(category, probes)}


def run():
    parallel = free_dag(2, ((0, 1), (0, 1)))
    linear = free_dag(2, ((0, 1),))
    weak = control(parallel, (1,))
    strong = control(parallel, (0,))
    complete = control(parallel, (0, 1))
    linear_root = control(linear, (0,))
    assert weak == {"probes": [1], "object_separating": True, "faithful": False, "full": True}
    assert strong["faithful"] and strong["object_separating"] and not strong["full"]
    assert all(complete[k] for k in ("faithful", "full", "object_separating"))
    assert linear_root["faithful"] and not linear_root["object_separating"] and not linear_root["full"]

    # Absolute finite-category minimum: isolated two-element idempotent monoid.
    i, e, k = (0, 0, ()), (0, 0, (1,)), (1, 1, ())
    idem = TinyCategory((0, 1), {(0, 0): (i, e), (1, 1): (k,)},
                        {(i, i): i, (i, e): e, (e, i): e, (e, e): e, (k, k): k})
    absolute = control(idem, (1,))
    assert absolute["object_separating"] and not absolute["faithful"]

    # Mutation of the free-path premise: reachable prefix coequalizes f and g.
    a, b, c = (0, 0, ()), (1, 1, ()), (2, 2, ())
    u, f, g, w = (0, 1, (1,)), (1, 2, (2,)), (1, 2, (3,)), (0, 2, (4,))
    arrows = (a, b, c, u, f, g, w)
    composites = {(h, q): (h if q[0] == q[1] else q)
                  for q in arrows for h in arrows
                  if q[1] == h[0] and (q[0] == q[1] or h[0] == h[1])}
    composites[f, u] = w
    composites[g, u] = w
    relation = TinyCategory(range(3), {(0, 0): (a,), (1, 1): (b,), (2, 2): (c,),
                                     (0, 1): (u,), (1, 2): (f, g), (0, 2): (w,)}, composites)
    assert criterion(relation, (0,)) and not faithful(relation, (0,))

    sweep_categories = sweep_families = 0
    for n in (1, 2, 3):
        endpoints = list(itertools.combinations(range(n), 2))
        for multiplicities in itertools.product(range(3), repeat=len(endpoints)):
            generators = tuple(edge for edge, count in zip(endpoints, multiplicities) for _ in range(count))
            cat = free_dag(n, generators)
            cat.verify()
            sweep_categories += 1
            for bits in itertools.product((False, True), repeat=n):
                probes = tuple(x for x, bit in enumerate(bits) if bit)
                assert faithful(cat, probes) == criterion(cat, probes)
                sweep_families += 1

    from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument
    from observational_succ.operational_yoneda_descent import (
        BeliefGame, ObservationPathCategory, forget_observation_history,
        restricted_yoneda_arrow_detection,
    )
    from observational_succ.yoneda import enumerate_natural_transforms, representable_natural_transform
    field = FiniteCarrier(1, (Instrument("A", (0,), (0,), (True,)),
                              Instrument("B", (0,), (0,), (True,))),
                          "A02-declared-source", "A02-one-point-chart")
    game = BeliefGame.build(field, (0,), ("constant",), target_id="A02-constant")
    actual = ObservationPathCategory(game, 1, max_objects=2, max_paths=2)
    root, leaf = 0, 1
    histories = actual.hom(root, leaf)
    assert tuple(actual.pretty_path(h) for h in histories) == ((("A", 0),), (("B", 0),))
    assert representable_natural_transform(actual, histories[0], (leaf,)) == representable_natural_transform(actual, histories[1], (leaf,))
    assert not restricted_yoneda_arrow_detection(actual, root, leaf, (leaf,))["faithful_on_selected_hom"]
    assert restricted_yoneda_arrow_detection(actual, root, leaf, (root,))["faithful_on_selected_hom"]
    quotient = forget_observation_history(actual)
    quotient_check = quotient.verify(max_compositions=16)
    assert quotient.arrow_image(histories[0]) == quotient.arrow_image(histories[1])
    assert not quotient.hom_faithfulness()["faithful"]
    counts = {name: len(enumerate_natural_transforms(actual, root, leaf, probes, max_candidates=16))
              for name, probes in (("leaf", (leaf,)), ("root", (root,)), ("full", (root, leaf)))}
    assert counts == {"leaf": 1, "root": 2, "full": 2}

    paths = ("observational_succ/yoneda.py", "observational_succ/operational_yoneda_descent.py",
             "provenance/IMPORT_MANIFEST.json",
             "provenance/origins/fuckingrh/actualization/YONEDA_GUIDE.md",
             "provenance/origins/fuckingrh/research/2026-10-10/CATEGORICAL_YONEDA_RESOURCE_FRONTIER.md",
             str(Path(__file__).relative_to(ROOT)))
    return {"schema": "succ-swarm-A02-exact-control/v1", "status": "TESTED MODEL",
            "universal_theorem_is_paper_derivation": True, "lean_kernel_checked": False,
            "parent_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935", "python": platform.python_version(),
            "source_hashes_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
            "minimal_free_history_witness": parallel.verify(),
            "absolute_category_witness": idem.verify(), "nonfree_premise_mutation": relation.verify(),
            "controls": {"leaf_probe": weak, "root_probe": strong, "all_probes": complete,
                         "faithful_but_object_nonseparating": linear_root, "absolute_minimum": absolute},
            "nonfree_reachable_but_nonfaithful": True,
            "bounded_free_dag_sweep": {"categories": sweep_categories, "probe_families": sweep_families,
                                       "max_vertices": 3, "max_parallel_generators": 2},
            "actual_SUCC_history_replay": {"contexts": actual.contexts, "histories": [actual.pretty_path(h) for h in histories],
                "restricted_natural_transform_counts": counts, "endpoint_quotient": quotient_check,
                "endpoint_quotient_faithful": False, "source_id_physically_authenticated": False},
            "not_run": ["full unittest suite", "foundations probes", "Lean compiler", "CI"]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
