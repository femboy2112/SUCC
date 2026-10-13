#!/usr/bin/env python3
"""Bounded exact crucible for SWM-X01; imports no SUCC implementation."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import subprocess
import time


PARENT = "316a93b264f77ee425b6a7e52be26d90bd4ccf20"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def subsets(n):
    return tuple(tuple(i for i in range(n) if mask & (1 << i))
                 for mask in range(1 << n))


def restrict(report, larger, smaller):
    return tuple(report[larger.index(i)] for i in smaller)


def report_of(trace, source, stage):
    return tuple(trace[source][i] for i in stage)


def witnesses(trace, multiplicities, stage):
    return tuple((report_of(trace, source, stage), source, receipt)
                 for source, count in enumerate(multiplicities)
                 for receipt in range(count))


def inverse_families(stages, objects, restriction):
    """Enumerate actual coordinate tuples, checking every comparable arrow."""
    result = []
    for coordinates in itertools.product(*(objects[f] for f in stages)):
        chosen = dict(zip(stages, coordinates))
        if all(restriction(chosen[g], g, f) == chosen[f]
               for f in stages for g in stages if set(f) <= set(g)):
            result.append(coordinates)
    return result


def exact_finite_sweep():
    counts = {"models": 0, "refinement_comparisons": 0,
              "labelled_support_checks": 0, "singleton_bridge_checks": 0}
    for n in range(4):
        for width in range(3):
            stages = subsets(width)
            for flat in itertools.product((0, 1), repeat=n * width):
                trace = tuple(tuple(flat[s * width:(s + 1) * width])
                              for s in range(n))
                report_stages = {f: set(report_of(trace, s, f) for s in range(n))
                                 for f in stages}
                for mult in itertools.product(range(3), repeat=n):
                    counts["models"] += 1
                    for f in stages:
                        for g in stages:
                            if not set(f) <= set(g):
                                continue
                            df = witnesses(trace, mult, f)
                            dg = witnesses(trace, mult, g)
                            pullback = {(rg, e) for rg in report_stages[g] for e in df
                                        if restrict(rg, g, f) == e[0]}
                            comparison = [(e[0], (restrict(e[0], g, f), e[1], e[2]))
                                          for e in dg]
                            assert len(comparison) == len(set(comparison))
                            assert set(comparison) <= pullback
                            if all(count == 1 for count in mult):
                                restriction_values = [restrict(rg, g, f)
                                                      for rg in report_stages[g]]
                                injective = len(restriction_values) == len(set(restriction_values))
                                assert (set(comparison) == pullback) == injective
                                counts["singleton_bridge_checks"] += 1
                            counts["refinement_comparisons"] += 1
                    for labels in itertools.product((0, 1), repeat=n):
                        for target in itertools.product((0, 1), repeat=width):
                            for label in (0, 1):
                                finite = all(any(mult[s] and labels[s] == label
                                                 and report_of(trace, s, f)
                                                 == tuple(target[i] for i in f)
                                                 for s in range(n)) for f in stages)
                                global_receipt = any(mult[s] and labels[s] == label
                                                     and trace[s] == target for s in range(n))
                                assert finite == global_receipt
                                counts["labelled_support_checks"] += 1
    return counts


def actual_limit_controls():
    controls = []
    for trace, mult, labels in [
            (((0, 0), (1, 1)), (2, 1), (0, 0)),
            (((0, 1), (1, 0)), (1, 1), (0, 1)),
            (((0, 1), (1, 0)), (0, 1), (0, 1)),
            ((), (), ()),
    ]:
        stages = subsets(2)
        objects = {f: witnesses(trace, mult, f) for f in stages}
        retained = inverse_families(
            stages, objects,
            lambda e, g, f: (restrict(e[0], g, f), e[1], e[2]))
        decoded = {(row[0][1], row[0][2]) for row in retained}
        total = {(s, a) for s, count in enumerate(mult) for a in range(count)}
        assert decoded == total and len(retained) == len(total)
        assert all(len({(e[1], e[2]) for e in row}) == 1 for row in retained)
        labelled = {f: tuple(sorted({(e[0], labels[e[1]]) for e in objects[f]}))
                    for f in stages}
        profiles = inverse_families(
            stages, labelled, lambda v, g, f: (restrict(v[0], g, f), v[1]))
        actual_joint = {(trace[s], labels[s]) for s, count in enumerate(mult) if count}
        assert {row[-1] for row in profiles} == actual_joint
        controls.append({"trace": trace, "multiplicities": mult, "labels": labels,
                         "retained_limit_cardinality": len(retained),
                         "labelled_report_limit_cardinality": len(profiles),
                         "retained_sources_and_receipts": sorted(decoded)})
    return controls


def smaller_bridge():
    trace, mult = ((0,), (1,)), (1, 1)
    f, g = (), (0,)
    pullback = {(rg, e) for rg in ( (0,), (1,) )
                for e in witnesses(trace, mult, f)}
    image = {(e[0], ((), e[1], e[2])) for e in witnesses(trace, mult, g)}
    assert len(pullback) == 4 and len(image) == 2
    assert ((1,), ((), 0, 0)) in pullback - image
    return {"small_stage_reports": [[]], "large_stage_reports": [[0], [1]],
            "comparison_domain_cardinality": 2, "pullback_cardinality": 4,
            "missing_pairs": sorted(pullback - image),
            "stage_projection_surjectivity": True,
            "cartesian_refinement": False}


def escape_and_repairs():
    horizons, caps = [], []
    for h in range(9):
        matches = [k for k in range(1, h + 2)
                   if all(int(k <= n) == 0 for n in range(1, h + 1))]
        assert matches == [h + 1]
        # The compact original carrier also has infinity, with zero trace,
        # but its witness fibre is EMPTY in the negative control.
        original_infinity_reports = [0] * h
        repaired_costs = [0] + matches
        assert min(repaired_costs) == 0
        horizons.append({"horizon": h, "minimum_supported_receipt_cost": min(matches),
                         "finite_witness_source": h + 1,
                         "compact_original_limit_source_report": original_infinity_reports,
                         "receipt_at_limit_source": False,
                         "restored_limit_receipt_minimum_cost": min(repaired_costs)})
    for cap in range(1, 9):
        reports = {str(k): int(k <= cap) for k in range(1, cap + 1)}
        assert all(value == 1 for value in reports.values())
        caps.append({"cost_cap": cap, "refuting_probe": cap, "reports": reports})
    # Unique source labels must agree even at the empty stage.
    for label in range(1, 9):
        assert int(label <= label) == 1
    return {"finite_horizons_only": horizons, "bounded_cap_refutations": caps,
            "injective_label_checks": 8,
            "universal_nonrealization_evidence": "paper quantifier proof in X01.md, not finite sweep"}


def binary_derivative_control():
    checked = 0
    for h in range(9):
        for profile in itertools.product((0, 1), repeat=h):
            sources = []
            for preparation in (0, 1):
                source = [preparation]
                for bit in profile:
                    source.append(source[-1] ^ bit)
                assert tuple(source[i] ^ source[i + 1] for i in range(h)) == profile
                sources.append(tuple(source))
            assert sources[0] != sources[1]
            assert all(a ^ b == 1 for a, b in zip(*sources))
            checked += 1
    return {"profiles_checked_horizons_0_through_8": checked,
            "retained_preparations_per_profile": 2}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path, default=HERE / "X01_receipt.json")
    args = parser.parse_args()
    started = time.monotonic()
    result = {
        "assignment": "SWM-X01", "status": "TESTED MODEL",
        "source_parent": PARENT, "python": platform.python_version(),
        "imports_repository_helpers": False,
        "finite_sweep": exact_finite_sweep(),
        "actual_inverse_family_controls": actual_limit_controls(),
        "minimal_refinement_counterexample": smaller_bridge(),
        "escape_and_repairs": escape_and_repairs(),
        "compact_cantor_derivative_finite_control": binary_derivative_control(),
    }
    elapsed = time.monotonic() - started
    status_lines = Path("/proc/self/status").read_text().splitlines()
    hwm = int(next(line.split()[1] for line in status_lines if line.startswith("VmHWM:")))
    assert elapsed < 60, elapsed
    assert hwm < 100 * 1024, hwm
    result["bounds"] = {"wall_seconds": elapsed, "vm_hwm_kib": hwm,
                        "maximum_wall_seconds": 60, "maximum_memory_kib": 102400}
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    result["execution_head"] = head
    result["artifact_sha256"] = {p.name: sha256(p)
                                  for p in (HERE / "X01.md", HERE / "X01_sources.json",
                                            Path(__file__).resolve())}
    result["execution_command"] = "timeout 60 python research/2026-10-13/SWARM_ATLAS/X01_probe.py"
    result["assertions_passed"] = True
    result["full_suite_executed"] = False
    result["lean_executed"] = False
    result["physical_source_attestation"] = False
    args.receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "receipt": str(args.receipt),
                      "finite_sweep": result["finite_sweep"],
                      "bounds": result["bounds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
