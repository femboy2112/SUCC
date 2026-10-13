#!/usr/bin/env python3
"""F46 exact finite optimal recovery probe; no physical or cognitive claims."""
from __future__ import annotations

import argparse
from dataclasses import replace
from fractions import Fraction as Q
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import random
import resource
import subprocess
import sys
import time

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024,) * 2)
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
ROOT = Path(__file__).resolve().parents[3]
BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
sys.path.insert(0, str(ROOT))
from observational_succ.field_relative_closure import ClosureError, FiniteField
from observational_succ.phenomenology import example as phenomenology_example


def rational_rows(rows):
    values = tuple(tuple(Q(v) for v in row) for row in rows)
    if not values or not values[0] or any(len(row) != len(values[0]) for row in values):
        raise ValueError("Declare nonempty rectangular rational target table")
    return values


def distance(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def radius(report, rows):
    """Attaining midpoint decoder, using coordinate extrema, not pair search."""
    rows = rational_rows(rows)
    if len(report) != len(rows):
        raise ValueError("Report must cover each source")
    fibers = {}
    for i, label in enumerate(report):
        fibers.setdefault(label, []).append(i)
    decoder = {}
    for label, idx in fibers.items():
        decoder[label] = tuple(
            (min(rows[i][j] for i in idx) + max(rows[i][j] for i in idx)) / 2
            for j in range(len(rows[0]))
        )
    loss = max(distance(row, decoder[label]) for label, row in zip(report, rows))
    return loss, decoder


def pair_bound(report, rows):
    """Independent lower-bound route with concrete original-state witness."""
    rows = rational_rows(rows)
    bound, witness = Q(0), None
    for i, j in combinations(range(len(rows)), 2):
        if report[i] == report[j]:
            gap = distance(rows[i], rows[j])
            if gap / 2 > bound:
                coordinate = next(k for k in range(len(rows[0]))
                                  if abs(rows[i][k] - rows[j][k]) == gap)
                bound, witness = gap / 2, (i, j, coordinate, gap)
    return bound, witness


def scalar_decoder_oracle(report, rows):
    """Enumerate all useful half-grid centers; no midpoint formula."""
    vals = tuple(row[0] for row in rows)
    candidates = (Q(0), Q(1, 2), Q(1), Q(3, 2), Q(2))
    return max(min(max(abs(vals[i] - center) for i in range(len(vals))
                       if report[i] == label) for center in candidates)
               for label in set(report))


def partitions(n):
    """Every set partition as a restricted-growth feature map, once."""
    def extend(prefix):
        if len(prefix) == n:
            yield prefix
        else:
            for label in range(max(prefix) + 2):
                yield from extend(prefix + (label,))
    yield from extend((0,))


def conflict_edges(report, rows, epsilon):
    return tuple((i, j) for i, j in combinations(range(len(rows)), 2)
                 if report[i] == report[j]
                 and distance(rows[i], rows[j]) > 2 * epsilon)


def coloring_oracle(n, edges):
    """Enumerate literal colorings, independently from repair partitions."""
    for k in range(1, n + 1):
        for colors in product(range(k), repeat=n):
            if all(colors[i] != colors[j] for i, j in edges):
                return k, colors
    raise AssertionError("Singleton coloring must exist")


def factor_check(report, rows):
    n = len(report)
    field = FiniteField("F46-declared-source", "F46-rational-basis", tuple(range(n)),
                        {"report": tuple(report)},
                        {str(j): tuple(row[j] for row in rows)
                         for j in range(len(rows[0]))})
    certs = tuple(field.factor(("report",), str(j)) for j in range(len(rows[0])))
    for cert in certs:
        assert field.verify(cert)
    return all(cert.proved for cert in certs)


def exhaustive_checks():
    counts = {"source_report_target_tables": 0, "tolerance_tables": 0,
              "feature_partitions_checked": 0, "zero_error_factor_checks": 0}
    tolerances = (Q(0), Q(1, 2), Q(1), Q(3, 2))
    for n in range(1, 5):
        features = tuple(partitions(n))
        for report in product(range(2), repeat=n):
            for vals in product(range(3), repeat=n):
                rows = tuple((Q(value),) for value in vals)
                optimal, _ = radius(report, rows)
                lower, _ = pair_bound(report, rows)
                assert optimal == lower == scalar_decoder_oracle(report, rows)
                assert (optimal == 0) == factor_check(report, rows)
                counts["zero_error_factor_checks"] += 1
                repair_radii = []
                for feature in features:
                    refined = tuple(zip(report, feature))
                    repaired, _ = radius(refined, rows)
                    assert repaired <= optimal
                    repair_radii.append((feature, repaired))
                    counts["feature_partitions_checked"] += 1
                for epsilon in tolerances:
                    edges = conflict_edges(report, rows, epsilon)
                    minimum, colors = coloring_oracle(n, edges)
                    direct_minimum = min(max(feature) + 1 for feature, loss in repair_radii
                                         if loss <= epsilon)
                    assert minimum == direct_minimum
                    assert radius(tuple(zip(report, colors)), rows)[0] <= epsilon
                    for feature, loss in repair_radii:
                        assert (loss <= epsilon) == all(feature[i] != feature[j]
                                                       for i, j in edges)
                    counts["tolerance_tables"] += 1
                counts["source_report_target_tables"] += 1
    return counts


def rational_cases():
    rng = random.Random(460013)
    digest_rows = []
    for case in range(96):
        n = 2 + case % 5
        report = tuple(rng.randrange(3) for _ in range(n))
        rows = tuple(tuple(Q(rng.randrange(-7, 8), rng.randrange(1, 5))
                           for _ in range(2)) for _ in range(n))
        optimal, _ = radius(report, rows)
        assert optimal == pair_bound(report, rows)[0]
        assert (optimal == 0) == factor_check(report, rows)
        relabeled = tuple(("renamed", 17 * label + 2) for label in report)
        assert radius(relabeled, rows)[0] == optimal
        coarse = tuple(0 for _ in report)
        assert radius(coarse, rows)[0] >= optimal
        feature = tuple(rng.randrange(3) for _ in range(n))
        assert radius(tuple(zip(report, feature)), rows)[0] <= optimal
        assert radius(report, tuple(tuple(3 * v for v in row) for row in rows))[0] == 3 * optimal
        epsilon = Q(case % 5, 3)
        edges = conflict_edges(report, rows, epsilon)
        minimum, colors = coloring_oracle(n, edges)
        brute_repairs = min(max(p) + 1 for p in partitions(n)
                            if radius(tuple(zip(report, p)), rows)[0] <= epsilon)
        assert minimum == brute_repairs
        assert radius(tuple(zip(report, colors)), rows)[0] <= epsilon
        digest_rows.append({"case": case, "report": report, "targets": rows,
                            "radius": optimal, "epsilon": epsilon,
                            "repair_alphabet": minimum})
    return {"seed": 460013, "count": len(digest_rows), "cases": digest_rows,
            "scope": "separate generated mathematical cases, not empirical holdout"}


def controls():
    states = tuple(product(range(2), repeat=2))
    a = tuple(x[0] for x in states)
    b = tuple(x[1] for x in states)
    empty = tuple(0 for _ in states)
    joint = tuple(zip(a, b))
    xor = tuple((Q(x ^ y),) for x, y in states)
    additive = tuple((Q(x + y),) for x, y in states)
    target_a = tuple((Q(x),) for x, _ in states)
    factorial = {}
    for name, target, second in (("xor", xor, b), ("additive", additive, b),
                                  ("duplicate_feature", target_a, a)):
        cells = {"00": radius(empty, target)[0], "10": radius(a, target)[0],
                 "01": radius(second, target)[0],
                 "11": radius(tuple(zip(a, second)), target)[0]}
        mixed = cells["11"] - cells["10"] - cells["01"] + cells["00"]
        factorial[name] = {"cells": cells, "risk_mixed_difference": mixed,
                           "gain_mixed_difference": -mixed}
    assert factorial["xor"]["risk_mixed_difference"] == Q(-1, 2)
    assert factorial["additive"]["risk_mixed_difference"] == 0
    assert factorial["duplicate_feature"]["risk_mixed_difference"] == Q(1, 2)

    future_rows = tuple((Q(x), Q(y)) for x, y in states)
    now = radius(a, target_a)[0]
    future = radius(a, future_rows)[0]
    repaired = radius(joint, future_rows)[0]
    assert (now, future, repaired) == (0, Q(1, 2), 0)
    actual_toy_history = ({"word": (), "current": (0, 1), "report": 0},
                          {"word": ("swap",), "current": (1, 0), "report": 1})
    for event in actual_toy_history:
        assert event["report"] == event["current"][0]
    square_defect = ((0, 0), (0, 1))
    assert square_defect[0][0] == square_defect[1][0]
    assert square_defect[0][1] != square_defect[1][1]

    triple_q = (0, 0, 0)
    triple_f = ((Q(0),), (Q(1),), (Q(2),))
    left, right = (0, 0, 1), (0, 1, 1)
    assert radius(tuple(zip(triple_q, left)), triple_f)[0] == Q(1, 2)
    assert radius(tuple(zip(triple_q, right)), triple_f)[0] == Q(1, 2)
    assert radius(triple_q, triple_f)[0] == 1
    coarser_than_both = tuple(p for p in partitions(3)
                             if all((left[i] != left[j] and right[i] != right[j])
                                    or p[i] == p[j] for i, j in combinations(range(3), 2)))
    assert coarser_than_both == ((0, 0, 0),)
    assert conflict_edges(triple_q, triple_f, Q(1, 2)) == ((0, 2),)

    triangle = ((Q(0), Q(0)), (Q(2), Q(0)), (Q(1), Q(2)))
    squared_pairs = tuple(sum((x - y) ** 2 for x, y in zip(triangle[i], triangle[j]))
                          for i, j in combinations(range(3), 2))
    epsilon = Q(6, 5)
    assert all(value <= (2 * epsilon) ** 2 for value in squared_pairs)
    weights = (Q(5, 16), Q(5, 16), Q(6, 16))
    center = tuple(sum(weights[i] * triangle[i][j] for i in range(3)) for j in range(2))
    assert center == (Q(1), Q(3, 4))
    squared_radii = tuple(sum((x - y) ** 2 for x, y in zip(point, center))
                          for point in triangle)
    assert squared_radii == (Q(25, 16),) * 3
    lower_squared = sum(w * r for w, r in zip(weights, squared_radii))
    assert lower_squared > epsilon ** 2
    assert radius(triple_q, triangle)[0] == 1

    restricted_values = (Q(0), Q(2))
    restricted_loss = min(max(abs(value - center) for value in restricted_values)
                          for center in restricted_values)
    free_loss = radius((0, 0), ((0,), (2,)))[0]
    assert (free_loss, restricted_loss) == (1, 2)

    boundary_loss = radius((0, 0), ((0,), (1,)))[0]
    assert boundary_loss == Q(1, 2)
    assert radius((0, 0), ((0,), (0,)))[0] == 0
    field = FiniteField("F46-source", "basis", (0, 1), {"q": (0, 0)}, {"b": (0, 1)})
    failed_cert = field.factor(("q",), "b")
    assert not failed_cert.proved and field.verify(failed_cert)
    try:
        field.verify(replace(failed_cert, source_id="other"))
    except ClosureError:
        metadata_rejected = True
    else:
        raise AssertionError("Wrong source declaration must be rejected")

    smoke = phenomenology_example()
    comparison = smoke["comparison"]
    thin_q = (tuple(comparison["thin_signature_a"]), tuple(comparison["thin_signature_b"]))
    path_q = (tuple(comparison["path_signature_a"]), tuple(comparison["path_signature_b"]))
    shadow_rows = ((Q(6),), (Q(12),))
    thin_loss, path_loss = radius(thin_q, shadow_rows)[0], radius(path_q, shadow_rows)[0]
    assert (thin_loss, path_loss) == (3, 0)
    assert comparison["shadow_a"]["stage"] == comparison["shadow_b"]["stage"] == "shadow"
    return {
        "complete_feature_factorials": factorial,
        "dynamic_feature": {"source_states": states, "action": "swap",
                            "current_radius": now, "next_field_radius": future,
                            "repaired_radius": repaired, "square_defect": square_defect,
                            "executed_toy_history": actual_toy_history,
                            "contact_scope": "recorded computational model events only"},
        "noncanonical_repair": {"candidate_status": "REFUTED", "source_values": triple_f,
                                "epsilon": Q(1, 2), "optimal_repairs": (left, right),
                                "minimum_alphabet": 2, "coarsenings_of_both": coarser_than_both,
                                "common_coarsening_radius": Q(1)},
        "wrong_norm_graph": {"candidate_status": "REFUTED", "points": triangle,
                             "epsilon": epsilon, "squared_pair_distances": squared_pairs,
                             "positive_weights": weights, "barycenter": center,
                             "universal_squared_radius_lower_bound": lower_squared,
                             "allowed_squared_radius": epsilon ** 2, "supnorm_radius": Q(1)},
        "source_realizing_decoder": {"candidate_status": "REFUTED", "source_values": restricted_values,
                                     "free_estimate_radius": free_loss,
                                     "source_realizing_radius": restricted_loss},
        "boundary_alias": {"source_values": (0, 1), "report": (0, 0),
                           "radius": boundary_loss, "existing_checker_counterexample": failed_cert.counterexample,
                           "wrong_source_metadata_rejected": metadata_rejected,
                           "source_authentication": "NOT ESTABLISHED"},
        "phenomenology_current_code_smoke": {"source_horizon": smoke["source_horizon"],
                                             "thin_reports": thin_q, "path_reports": path_q,
                                             "numeric_shadow_radius_thin": thin_loss,
                                             "numeric_shadow_radius_path": path_loss,
                                             "both_target_stages": ("shadow", "shadow"),
                                             "scope": "laboratory two-target source table, no target observation"}
    }


def serializable(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serializable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serializable(v) for v in value]
    return value


def source_binding():
    paths = (
        "AGENTS.md", "README.md", "docs/FOUNDATIONS.md", "docs/METHOD.md",
        "docs/ARCHITECTURE.md", "docs/ROADMAP.md", "docs/CLAIM_LEDGER.md",
        "provenance/IMPORT_MANIFEST.json", "observational_succ/phenomenology.py",
        "observational_succ/field_relative_closure.py",
        "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
        "provenance/origins/fuckingrh/actualization/YONEDA_GUIDE.md",
        "research/2026-10-13/SWARM_ATLAS/F46_MATHEMATICAL_PHENOMENOLOGY.md",
        "research/2026-10-13/SWARM_ATLAS/F46_PROBE.py",
    )
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}
    for path in paths[:-2]:
        frozen = subprocess.check_output(["git", "show", BASE + ":" + path], cwd=ROOT)
        assert hashes[path] == hashlib.sha256(frozen).hexdigest(), "Immutable source changed: " + path
    result = {"immutable_source_parent": BASE, "sha256": hashes,
              "tracked_source_bytes_equal_immutable_parent": True}
    imported = json.loads((ROOT / "provenance/IMPORT_MANIFEST.json").read_text())
    entry = next(e for e in imported["entries"]
                 if e["destination_path"] == "observational_succ/phenomenology.py")
    result["phenomenology_import"] = {"source_repo": imported["source_repo"],
                                      "source_commit": imported["source_commit"], **entry}
    code = (ROOT / entry["destination_path"]).read_bytes()
    git_blob = hashlib.sha1(b"blob " + str(len(code)).encode("ascii") + b"\0" + code).hexdigest()
    assert git_blob == entry["destination_git_blob_sha"], "Imported blob differs from manifest"
    result["native_field_origin_commit"] = "d1e64948f60662601074c1738d355b3456a17dcf"
    return result


def git_value(args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--write", type=Path)
    choice.add_argument("--verify", type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    evidence = serializable({"exhaustive": exhaustive_checks(),
                             "separate_rational_cases": rational_cases(), "controls": controls()})
    bound = source_binding()
    receipt = {"schema": "SUCC.F46.exact.v1", "source_binding": bound, "evidence": evidence,
               "status": "TESTED MODEL; paper theorems await independent non-deriver review",
               "execution": {"command": "timeout 25s python " + str(Path(__file__).relative_to(ROOT))
                                              + " " + " ".join(sys.argv[1:]),
                             "head_at_execution": git_value(["rev-parse", "HEAD"]),
                             "branch_at_execution": git_value(["branch", "--show-current"]),
                             "python": sys.version.split()[0], "exit_code": 0,
                             "wall_seconds": round(time.monotonic() - started, 6),
                             "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                             "address_space_cap_mib": 256, "cpu_cap_seconds": 20,
                             "empirical_contact": False, "full_suite_run": False, "ci_run": False}}
    if args.write:
        args.write.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        action = "WROTE"
    else:
        saved = json.loads(args.verify.read_text())
        assert saved["schema"] == receipt["schema"]
        assert saved["source_binding"] == bound, "Bound source/script/dossier changed"
        assert saved["evidence"] == evidence, "Exact mathematical evidence changed"
        assert saved["execution"]["exit_code"] == 0
        action = "VERIFIED"
    print(json.dumps({"action": action, "exhaustive": evidence["exhaustive"],
                      "rational_cases": len(evidence["separate_rational_cases"]["cases"]),
                      "preserved_refuted_candidates": 3,
                      "wall_seconds": receipt["execution"]["wall_seconds"],
                      "max_rss_kib": receipt["execution"]["max_rss_kib"]}, sort_keys=True))


if __name__ == "__main__":
    main()
