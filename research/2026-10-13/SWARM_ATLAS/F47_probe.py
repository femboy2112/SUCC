#!/usr/bin/env python3
"""F47: exact bounded calibration/consensus controls, not a physical clock model.

Only stdlib plus two unchanged source modules. Run with Python -B to avoid caches.
Every Fraction is serialized as a string. No floating-point certificates.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import resource
import subprocess
import sys

if not __debug__:
    raise RuntimeError("F47 checks require assertions enabled")
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
resource.setrlimit(resource.RLIMIT_CPU, (29, 29))
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.misiurewicz_phase_quotient import (  # noqa: E402
    actual_source_cells, dual_phase_correlation, f, CubicElement, phase,
)
from observational_succ.dual_boundary_observers import DualFiniteTower  # noqa: E402

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def exact(value: int | Q) -> Q:
    if type(value) is bool or not isinstance(value, (int, Q)):
        raise ValueError("exact integer/Fraction required")
    return Q(value)


@dataclass(frozen=True)
class Affine:
    rate: Q
    origin: Q

    def __post_init__(self):
        object.__setattr__(self, "rate", exact(self.rate))
        object.__setattr__(self, "origin", exact(self.origin))
        if self.rate <= 0:
            raise ValueError("positive invertible orientation required")

    def __call__(self, x):
        return self.rate * exact(x) + self.origin

    def inverse(self):
        return Affine(1 / self.rate, -self.origin / self.rate)

    def after(self, other):
        return Affine(self.rate * other.rate,
                      self.rate * other.origin + self.origin)


@dataclass(frozen=True)
class Record:
    source: str
    epoch: int
    event: int
    time: Q
    local: tuple[Q, ...]


@dataclass(frozen=True)
class Calibration:
    source: str
    epoch: int
    charts: tuple[Affine, ...]

    def decode(self, record):
        if (record.source, record.epoch) != (self.source, self.epoch):
            raise ValueError("source/epoch mismatch")
        if len(record.local) != len(self.charts):
            raise ValueError("all observer coordinates required")
        return tuple(h.inverse()(v) - exact(record.time)
                     for h, v in zip(self.charts, record.local))

    def encode(self, z, event, time):
        if len(z) != len(self.charts):
            raise ValueError("all observer phases required")
        if type(event) is not int or event < 0:
            raise ValueError("nonnegative event index required")
        t = exact(time)
        return Record(self.source, self.epoch, event, t,
                      tuple(h(t + exact(v)) for h, v in zip(self.charts, z)))

    def step(self, record, edge, next_time):
        t = exact(next_time)
        if t < exact(record.time):
            raise ValueError("backwards common event time")
        return self.encode(average(self.decode(record), edge),
                           record.event + 1, t)


def average(z, edge):
    z = tuple(exact(x) for x in z)
    i, j = edge
    if type(i) is not int or type(j) is not int or not 0 <= i < j < len(z):
        raise ValueError("one ordered distinct valid edge required")
    m = (z[i] + z[j]) / 2
    return tuple(m if k in edge else v for k, v in enumerate(z))


def mean(z):
    return sum(z, Q(0)) / len(z)


def energy(z):
    m = mean(z)
    return sum(((v - m) ** 2 for v in z), Q(0))


def width(z):
    return max(z) - min(z)


def connected(n, edges):
    seen = {0}
    while True:
        new = seen | {j for i, j in edges if i in seen} | {
            i for i, j in edges if j in seen}
        if new == seen:
            return len(seen) == n
        seen = new


def independent_product(n, schedule):
    """Separate explicit matrix multiplication; never calls average()."""
    m = [[Q(i == j) for j in range(n)] for i in range(n)]
    for i, j in schedule:
        p = [[Q(a == b) for b in range(n)] for a in range(n)]
        for a in (i, j):
            for b in range(n):
                p[a][b] = Q(1, 2) if b in (i, j) else Q(0)
        m = [[sum((p[a][k] * m[k][b] for k in range(n)), Q(0))
              for b in range(n)] for a in range(n)]
    return tuple(tuple(row) for row in m)


def bounded_controls():
    cases = []
    for n in (2, 3):
        all_edges = tuple(combinations(range(n), 2))
        for mask in range(1, 1 << len(all_edges)):
            edges = tuple(e for k, e in enumerate(all_edges) if mask >> k & 1)
            if connected(n, edges):
                cases.extend((n, s) for s in permutations(edges))
    # Unfitted extra regimes: four nodes, branching/path/dense/slack schedules.
    for edges in (((0, 1), (1, 2), (2, 3)),
                  ((0, 1), (0, 2), (0, 3))):
        cases.extend((4, s) for s in permutations(edges))
    cases += [(4, tuple(combinations(range(4), 2))),
              (4, ((2, 3), (1, 2), (0, 1), (2, 3)))]
    states_checked = 0
    lowest_anchor = Q(1)
    for n, block in cases:
        b = len(block)
        length = (n - 1) * b
        schedule = block * (n - 1)
        m = independent_product(n, schedule)
        alpha = Q(1, 2 ** length)
        assert all(sum(row) == 1 for row in m)
        assert all(sum(m[i][j] for i in range(n)) == 1 for j in range(n))
        assert min(row[0] for row in m) >= alpha
        lowest_anchor = min(lowest_anchor, min(row[0] for row in m))
        for values in product((-1, 0, 2), repeat=n):
            initial = tuple(map(Q, values))
            z = initial
            for edge in schedule:
                after = average(z, edge)
                assert mean(after) == mean(initial)
                assert energy(z) - energy(after) == (z[edge[0]] - z[edge[1]]) ** 2 / 2
                z = after
            direct = tuple(sum((a * x for a, x in zip(row, initial)), Q(0)) for row in m)
            assert z == direct
            assert width(z) <= (1 - alpha) * width(initial)
            states_checked += 1
    # Nonperiodic aligned blocks, variable exact common times and new charts.
    cal = Calibration("F47-declared-clock", 1,
                      (Affine(1, 0), Affine(2, 7), Affine(Q(3, 2), -2), Affine(Q(7, 3), 11)))
    blocks = (((2, 3), (1, 2), (0, 1), (2, 3)),
              ((0, 1), (1, 2), (2, 3), (0, 1)),
              ((1, 2), (0, 1), (0, 1), (2, 3)))
    initial = (Q(-3), Q(1), Q(7), Q(2))
    record = cal.encode(initial, 0, Q(0))
    trace = [record]
    z = initial
    for event, edge in enumerate(sum(blocks, ()), 1):
        z = average(z, edge)
        record = cal.step(record, edge, Q(event * (event + 1), 6))
        assert cal.decode(record) == z
        assert mean(z) == mean(initial)
        trace.append(record)
    assert width(z) <= (1 - Q(1, 2 ** 12)) * width(initial)
    m = independent_product(4, sum(blocks, ()))
    assert min(row[0] for row in m) >= Q(1, 2 ** 12)
    return {"schedule_cases": len(cases), "initial_vectors_checked": states_checked,
            "smallest_observed_anchor_column_entry": lowest_anchor,
            "nonperiodic_common_time_trace": [
                {"event": r.event, "common_time": r.time, "local_values": r.local,
                 "decoded_offsets": cal.decode(r)} for r in trace],
            "conserved_mean": mean(initial), "final_range": width(z)}


def calibration_controls():
    h = (Affine(1, 0), Affine(2, 7), Affine(Q(3, 2), -2))
    transitions = {(i, j): h[j].after(h[i].inverse()) for i in range(3) for j in range(3)}
    assert all(transitions[j, k].after(transitions[i, j]) == transitions[i, k]
               for i, j, k in product(range(3), repeat=3))
    bad_loop = Affine(1, 1).after(Affine(1, 0)).after(Affine(1, 0))
    assert bad_loop != Affine(1, 0) and bad_loop(0) == 1
    cal = Calibration("source", 3, h)
    valid = cal.encode((0, 1, 2), 0, 0)
    rejected = []
    for name, operation in [
        ("float_chart", lambda: Affine(1.0, 0)),
        ("zero_rate", lambda: Affine(0, 0)),
        ("wrong_source", lambda: cal.decode(Record("other", 3, 0, Q(0), valid.local))),
        ("wrong_epoch", lambda: cal.decode(Record("source", 2, 0, Q(0), valid.local))),
        ("backwards_time", lambda: cal.step(valid, (0, 1), -1)),
        ("invalid_edge", lambda: cal.step(valid, (1, 1), 1)),
    ]:
        try:
            operation()
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError("negative control accepted: " + name)
    return {"commuting_triangles_checked": 27,
            "bad_affine_cycle": {"rate": bad_loop.rate, "origin": bad_loop.origin},
            "rejections": rejected}


def phase_adapter():
    covariances = []
    for lag in range(10):
        raw = (0 ^ (lag % 2), 1 ^ (lag % 2))
        aligned = tuple(p ^ (lag % 2) for p in raw)
        cov = sum(((Q(x) - Q(1, 2)) * (Q(y) - Q(1, 2)) / 2
                   for x, y in zip((0, 1), raw)), Q(0))
        assert aligned == (0, 1)
        prior_report = dual_phase_correlation(lag)
        assert cov == Q((-1) ** lag, 4)
        assert prior_report["raw_phase_covariance"] == cov
        covariances.append({"lag": lag, "raw_covariance": cov,
                            "transported_covariance": Q(1, 4)})
    actual = actual_source_cells(Q(2, 5), 4)
    assert tuple(phase(c) ^ (i % 2) for i, c in enumerate(actual)) == (0,) * 5
    assert f(CubicElement.coerce(Q(2, 5))) == f(CubicElement.coerce(Q(3, 5)))
    raw_signs = (1, -1)
    corrected_signs = (raw_signs[0], -raw_signs[1])
    assert sum(raw_signs) == 0 and sum(corrected_signs) == 2
    return {"lag_sweep": covariances, "actual_logistic_cells_2_over_5": actual,
            "raw_signs": raw_signs, "lag_transported_signs": corrected_signs,
            "raw_squared_sum": 0, "incoherent_power": 2, "transported_squared_sum": 4,
            "source_family_count": 1, "independent_evidence_count_claimed": 0}


def hostile_controls():
    # Identical affine report laws, different normalized relative phase.
    world_a = (Affine(1, 0), Affine(1, 0))
    world_b = (Affine(1, 0), Affine(1, -1))
    za, zb = (Q(0), Q(0)), (Q(0), Q(1))
    coefficient_a = tuple((h.rate, h.rate * z + h.origin) for h, z in zip(world_a, za))
    coefficient_b = tuple((h.rate, h.rate * z + h.origin) for h, z in zip(world_b, zb))
    assert coefficient_a == coefficient_b  # all t, not just tested t
    assert width(za) == 0 and width(zb) == 1
    unknown_time_worlds = ([(b ^ c ^ (n % 2)) for n in range(8)]
                          for b, c in ((0, 0), (1, 1)))
    x, y = unknown_time_worlds
    assert x == y
    # Missed connected edge leaves one observer isolated, forever.
    isolated = (Q(0), Q(2), Q(10))
    after = average(isolated, (0, 1))
    assert after == (Q(1), Q(1), Q(10))
    assert average(after, (0, 1)) == after and width(after) == 9
    # Copying instead of averaging can be fair and preserve sum, yet oscillate.
    copied = ((Q(0), Q(1)), (Q(1), Q(0)), (Q(0), Q(1)))
    assert all(width(v) == 1 for v in copied)
    # One-sided delivery destroys the designated invariant.
    partial = (Q(1), Q(2))
    assert mean((Q(0), Q(2))) == 1 and mean(partial) == Q(3, 2)
    # Source identity loss from current consensus state; history still kept.
    states = ((0, 2), (1, 1), (2, 0))
    original_left = tuple(x[0] for x in states)
    old = DualFiniteTower("F47-original", 1, states, (Q(1, 3),) * 3,
                         (tuple(x[0] for x in states),), (tuple(x[1] for x in states),))
    now = DualFiniteTower("F47-original", 1, states, (Q(1, 3),) * 3,
                         ((1, 1, 1),), ((1, 1, 1),))
    assert old.claim_factors(original_left)["factors"]
    alias = now.claim_factors(original_left)
    assert not alias["factors"]
    # At finite time every value is dyadic, whereas invariant mean is 1/3.
    nonfinite = (Q(0), Q(0), Q(1))
    for n in range(20):
        nonfinite = average(nonfinite, ((0, 1), (1, 2))[n % 2])
        assert all(v.denominator & (v.denominator - 1) == 0 for v in nonfinite)
        assert width(nonfinite) > 0 and mean(nonfinite) == Q(1, 3)
    def readout_law(states, report):
        result = {}
        for state in states:
            out = report(state)
            result[out] = result.get(out, Q(0)) + Q(1, len(states))
        return result
    common_states = (("one", 0), ("one", 1))
    paired_states = ((("left", 0), ("right", 0)),
                     (("left", 1), ("right", 1)))
    same_source = readout_law(common_states, lambda s: (s[1], s[1]))
    two_carriers_shared_preparation = readout_law(paired_states,
                                                 lambda s: (s[0][1], s[1][1]))
    assert same_source == two_carriers_shared_preparation
    return {"unknown_chart_report_coefficients_identical": coefficient_a,
            "hidden_normalized_phase_ranges": (width(za), width(zb)),
            "unknown_parity_identical_eight_reports": x,
            "omitted_edge_fixed_state": after, "omitted_edge_range": width(after),
            "fair_copy_cycle": copied, "one_sided_update_means": (Q(1), Q(3, 2)),
            "source_alias_receipt": alias, "preserved_original_history_target": True,
            "finite_dyadic_sync_control_final": nonfinite, "invariant_mean": Q(1, 3),
            "same_vs_two_carrier_report_laws_identical": True,
            "common_carrier_states": common_states,
            "paired_carrier_states": paired_states,
            "common_report_probability_table": [
                {"reports": key, "mass": mass} for key, mass in sorted(same_source.items())],
            "identity_of_physical_carrier_inferred": False}


def provenance():
    paths = (
        "observational_succ/misiurewicz_phase_quotient.py",
        "observational_succ/dual_boundary_observers.py",
        "research/2026-10-12/MISIUREWICZ_PHASE_CHAOTIC_QUOTIENT.md",
        "research/2026-10-12/DUAL_BOUNDARY_OBSERVER_CORRELATION.md",
        "provenance/IMPORT_MANIFEST.json",
    )
    manifest = json.loads((ROOT / paths[-1]).read_text())
    rows = []
    for path in paths:
        origin = subprocess.check_output(
            ["git", "log", "--format=%H", "--diff-filter=A", BASE, "--", path],
            cwd=ROOT, text=True).splitlines()[0]
        original = subprocess.check_output(["git", "show", origin + ":" + path], cwd=ROOT)
        frozen = subprocess.check_output(["git", "show", BASE + ":" + path], cwd=ROOT)
        current = (ROOT / path).read_bytes()
        assert current == frozen
        rows.append({"path": path, "origin_commit": origin,
                     "origin_sha256": hashlib.sha256(original).hexdigest(),
                     "base_current_sha256": hashlib.sha256(current).hexdigest(),
                     "in_import_manifest": any(e["destination_path"] == path
                                               for e in manifest["entries"])})
    return {"immutable_parent": BASE, "source_paths": rows,
            "historic_import_source": manifest["source_commit"],
            "import_entries": len(manifest["entries"]),
            "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    result = serial({"schema": "SUCC-F47-exact-receipt-v1",
                     "status": "TESTED MODEL; derivations require independent principal review",
                     "provenance": provenance(),
                     "calibration": calibration_controls(),
                     "averaging": bounded_controls(),
                     "phase_adapter": phase_adapter(),
                     "crucible": hostile_controls(),
                     "boundaries": {"physical_clock_calibration": False,
                                    "physical_source_authentication": False,
                                    "finite_probe_proves_universal_convergence": False,
                                    "independent_principal_review_complete": False,
                                    "resources": "CPU <=29s; address space <=256MiB"}})
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.verify:
        assert json.loads(args.verify.read_text()) == result, "receipt mismatch"
        print("F47 exact receipt replay passed")
    elif args.write:
        if args.write.resolve().parent != Path(__file__).parent:
            raise ValueError("receipt must stay beside F47 probe")
        args.write.write_text(encoded)
        print("F47 wrote exact receipt; " + str(result["averaging"]["initial_vectors_checked"]) + " vectors checked")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
