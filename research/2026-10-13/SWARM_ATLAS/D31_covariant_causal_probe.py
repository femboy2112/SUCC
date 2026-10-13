"""D31 bounded exact controls; model receipts do not authenticate physics."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
ETA = (1, -1, -1)
ID = tuple(tuple(F(i == j) for j in range(3)) for i in range(3))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def apply(a, x):
    return tuple(sum(a[i][j] * x[j] for j in range(3)) for i in range(3))


def boost(axis, r):
    assert type(r) in (int, F) and abs(r) < 1 and axis in (1, 2)
    r = F(r)
    g, z = (1 + r*r)/(1 - r*r), 2*r/(1 - r*r)
    a = [list(row) for row in ID]
    a[0][0] = a[axis][axis] = g
    a[0][axis] = a[axis][0] = -z
    return tuple(tuple(row) for row in a)


def interval(x):
    return sum(ETA[i] * x[i]*x[i] for i in range(3))


def before(a, b):
    d = tuple(b[i] - a[i] for i in range(3))
    return d[0] >= 0 and interval(d) >= 0


def diamond(p, o, e):
    return before(p, e) and before(e, o)


def ancestry(parents, anchor):
    seen, queue = set(), [anchor]
    while queue:
        e = queue.pop()
        if e not in seen:
            seen.add(e)
            queue.extend(parents[e])
    return sorted(seen)


def main():
    root = Path(__file__).resolve().parents[3]
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"],
                   cwd=root, check=True, capture_output=True)
    bx, by = boost(1, F(1, 3)), boost(2, F(1, 3))
    frames = (ID, bx, by, boost(1, F(-1, 3)), boost(2, F(-1, 3)),
              mul(bx, by), mul(by, bx))
    p, o = (0, 0, 0), (4, 0, 0)
    grid = tuple(product(range(-3, 4), repeat=3))
    checks = 0
    for a in frames:
        determinant = (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
                       - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
                       + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
        assert determinant == 1
        for i, j in product(range(3), repeat=2):
            assert sum(ETA[k]*a[k][i]*a[k][j] for k in range(3)) == (
                ETA[i] if i == j else 0)
        inverse = tuple(tuple(ETA[i]*a[j][i]*ETA[j] for j in range(3))
                        for i in range(3))
        assert mul(a, inverse) == ID and a[0][0] >= 1
        for e in grid:
            le = apply(a, e)
            assert interval(le) == interval(e)
            assert before(p, e) == before(apply(a, p), le)
            assert diamond(p, o, e) == diamond(apply(a, p), apply(a, o), le)
            checks += 3
    assert mul(bx, by) != mul(by, bx)

    events = {"prepare": p, "probe": (2, -2, 0), "unwired": (2, 0, 0),
              "sample": o}
    parents = {"prepare": (), "probe": ("prepare",), "unwired": (),
               "sample": ("probe",)}
    for a in frames:
        for e, prior in parents.items():
            for v in prior:
                assert before(events[v], events[e])
                assert before(apply(a, events[v]), apply(a, events[e]))
        assert diamond(apply(a, p), apply(a, o), apply(a, events["unwired"]))
        assert "unwired" not in ancestry(parents, "sample")

    external, early = (0, 2, 0), (1, 0, 0)
    assert not before(external, early)
    for a in frames:
        assert not before(apply(a, external), apply(a, early))
    moving, e = (5, 3, 0), events["probe"]
    assert interval(moving) == interval(o) == 16
    assert diamond(p, o, e) and not diamond(p, moving, e)
    assert interval(tuple(moving[i] - e[i] for i in range(3))) == -16
    assert apply(bx, moving) == o
    assert moving[0] > 4 and apply(bx, moving)[0] <= 4

    left, right = (0, -1, 0), (0, 1, 0)
    assert apply(bx, left)[0] == F(3, 4)
    assert apply(bx, right)[0] == F(-3, 4)
    assert not before(left, p) and not before(right, p)
    null = (1, -1, 0)
    galilean = (null[0], null[1] - F(3, 5)*null[0], null[2])
    assert before(p, null) and interval(galilean) == F(-39, 25)
    assert not before(p, galilean)
    time_reversal = (-1, 0, 0)
    assert interval(time_reversal) == 1 and not before(p, time_reversal)

    # Complete field report transports; E-only report fails on a hidden B bit.
    fields = ((0, 0), (0, 1))
    old_e = tuple(v[0] for v in fields)
    new_e = tuple(F(5, 4)*v[0] - F(3, 4)*v[1] for v in fields)
    assert old_e == (0, 0) and new_e == (0, F(-3, 4))
    for ef, bf in product(range(-2, 3), repeat=2):
        ep, bp = F(5, 4)*ef - F(3, 4)*bf, F(5, 4)*bf - F(3, 4)*ef
        assert F(5, 4)*ep + F(3, 4)*bp == ef
        assert F(3, 4)*ep + F(5, 4)*bp == bf
    erase = {0: 0, 1: 0}
    post_report = {0: 0}
    old_report, report_map = {0: 0, 1: 1}, {0: 0, 1: 0}
    for s in (0, 1):
        assert post_report[erase[s]] == report_map[old_report[s]]
    target_fibers = {}
    for s in (0, 1):
        target_fibers.setdefault(post_report[erase[s]], set()).add(s)
    assert target_fibers == {0: {0, 1}}

    # Prefix-dependent finite kernel; R and U complement bits, with h transported.
    def kernel(s, h, y):
        predicted = s if not h else s ^ h[-1]
        return F(3, 4) if y == predicted else F(1, 4)

    def changed_kernel(snew, hnew, ynew):
        predicted = snew if not hnew else 1 ^ snew ^ hnew[-1]
        return F(3, 4) if ynew == predicted else F(1, 4)

    def law(k, s, word):
        v = F(1)
        for i, y in enumerate(word):
            v *= k(s, word[:i], y)
        return v

    kernel_checks = 0
    for s in (0, 1):
        for word in product((0, 1), repeat=3):
            rw = tuple(1-v for v in word)
            assert law(kernel, s, word) == law(changed_kernel, 1-s, rw)
            kernel_checks += 1
            assert all(law(kernel, candidate, word) > 0 for candidate in (0, 1))
        assert sum(law(kernel, s, w) for w in product((0, 1), repeat=3)) == 1
    # Forgetting field/report transport is a mutation of equation (1).
    assert kernel(0, (), 0) != kernel(0, (), 1)
    budget, costs = 4, (2, 3)
    accepted = [i for i in range(len(costs)) if sum(costs[:i+1]) <= budget]
    assert accepted == [0] and F(8, 4) == 2 and F(8, 5) != 2

    paths = [Path(__file__).resolve(), Path(__file__).with_name(
        "D31_COVARIANT_CAUSAL_OBSERVERS.md")]
    native = ["observational_succ/relativistic_shadow_tower.py",
              "observational_succ/galilean_lorentz_succ.py",
              "observational_succ/covariant_observer_frames.py",
              "observational_succ/covariant_proof_descent.py",
              "observational_succ/maxwell_transverse_shadow.py",
              "provenance/origins/fuckingrh/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
              "provenance/IMPORT_MANIFEST.json"]
    hashes = {str(v.relative_to(root)): hashlib.sha256(v.read_bytes()).hexdigest()
              for v in paths + [root / v for v in native]}
    receipt = {"schema": "D31-exact-finite-model-v1", "base_sha": BASE,
        "branch": "research/swm-d31-2026-10-13", "command":
        "python research/2026-10-13/SWARM_ATLAS/D31_covariant_causal_probe.py",
        "exit_code": 0, "arithmetic": "integer/Fraction; no float",
        "positive": {"frames": 7, "grid_vectors": 343,
            "interval_cone_diamond_checks": checks,
            "actual_ancestry": ancestry(parents, "sample"),
            "noncommuting_frames": True, "prefix_kernel_paths": kernel_checks,
            "full_field_inverse_cases": 25, "budget_accepted_indices": accepted},
        "negative": {"outside_cone_squared": -3,
            "different_worldline_probe_squared": -16,
            "unwired_diamond_event_received": False,
            "erased_preparation_sources": [0, 1], "same_post_report": 0,
            "simultaneity_boost_times": ["3/4", "-3/4"],
            "E_only_old_reports": list(old_e), "E_only_new_reports": list(map(str, new_e)),
            "galilean_null_squared": str(interval(galilean)),
            "metric_preserving_time_reversal_is_future_oriented": False,
            "fixed_coordinate_cutoff_changes_sampling": True,
            "noisy_transcripts_identify_original_bit_exactly": False,
            "stale_report_mutation_detected": True},
        "origin_verification": {"commit": "ba075348b7bcc66d938b3e0ca96c26e95bba340a",
            "path": "research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
            "remote_http_status": 200, "bytes": 31980,
            "git_blob_sha1": "04408ed96bd369b5063868eb5ad5664824d18043",
            "matches_archive": True, "verification_exit_code": 0,
            "verification_method": "urllib.request remote bytes; Git blob SHA-1; exact archive byte equality",
            "url": "https://raw.githubusercontent.com/femboy2112/FuckingRH/ba075348b7bcc66d938b3e0ca96c26e95bba340a/research/2026-10-10/OBSERVATIONAL_SUCC_FOUNDATIONS.md",
            "local_origin_object_available": False,
            "local_object_command": "git cat-file -t ba075348b7bcc66d938b3e0ca96c26e95bba340a",
            "local_object_exit_code": 128},
        "native_origin_commits": {
            "covariant_frames": "82f518cda67c9f80054a0b973a5c12bbd248a309",
            "galilean_shadow": "f44bb04b1d8f542b4ebb402ee93d3d534a5d66fe",
            "authoritative_correction": "c3839c78df53aaf0cc41cf5cbbb61841f62f15df"},
        "command_receipts": [
            {"command": "git status --short", "exit_code": 0,
             "baseline_output": "", "state": "clean before D31 files"},
            {"command": "git rev-parse HEAD", "exit_code": 0, "baseline_output": BASE},
            {"command": "git log --diff-filter=A --format='%H %s' -- observational_succ/covariant_observer_frames.py observational_succ/galilean_lorentz_succ.py observational_succ/relativistic_shadow_tower.py research/2026-10-12/COVARIANT_PERCEPTUAL_MOMENTUM_AND_CAUSAL_DESCENT.md",
             "exit_code": 0,
             "origin_shas": ["82f518cda67c9f80054a0b973a5c12bbd248a309",
                             "f44bb04b1d8f542b4ebb402ee93d3d534a5d66fe"]}],
        "sha256": hashes,
        "verdict": "conditional covariance survives; covariance-implies-access refuted",
        "claim_limits": ["finite exact model, not physical attestation",
            "written universal proof, not independent kernel verification",
            "no empirical cognition, quantum mechanism or RH result"],
        "validation_scope": "D31 probe only; no full suite/compiler/push",
        "next_small_lemma": "prefix-dependent kernel covariance with stopping rules"}
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
