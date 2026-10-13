"""Bounded independent exact witnesses; no SUCC runtime imports or float gates."""
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"


def orbit(f, x, n):
    values = [x]
    for _ in range(n):
        values.append(f(values[-1]))
    return values


def circle_distance(x, y):
    gap = abs(x - y)
    return min(gap, 1 - gap)


def exact_horizon(a, delta, epsilon):
    assert a > 1 and 0 < delta <= epsilon
    n, error = 0, delta
    while a * error <= epsilon:
        n, error = n + 1, a * error
    return n


def main():
    checks = []
    linear = []
    for a in (Q(3, 2), Q(2), Q(3)):
        for delta in (Q(1, 64), Q(1, 256)):
            epsilon = Q(1, 8)
            horizon = exact_horizon(a, delta, epsilon)
            values = orbit(lambda x: a*x, delta, horizon + 1)
            assert values[horizon] <= epsilon < values[horizon + 1]
            assert all(x == a**i * delta for i, x in enumerate(values))
            linear.append({"a": str(a), "delta": str(delta), "epsilon": str(epsilon),
                           "last_acceptable_step": horizon,
                           "boundary_error": str(values[horizon]),
                           "next_error": str(values[horizon + 1])})
    checks.append("six exact sharp linear horizons")

    lips = (Q(2), Q(3, 2), Q(3))
    defects = (Q(1, 64), Q(1, 128), Q(0))
    initial = Q(1, 256)
    errors = [initial]
    for a, eta in zip(lips, defects):
        errors.append(a*errors[-1] + eta)
    for n in range(4):
        product = Q(1)
        for a in lips[:n]:
            product *= a
        formula = initial * product
        for j in range(n):
            tail = Q(1)
            for a in lips[j+1:n]:
                tail *= a
            formula += defects[j] * tail
        assert errors[n] == formula
    checks.append("step-defect product-sum bound attained by affine errors")

    doubling = lambda x: (2*x) % 1
    left = orbit(doubling, Q(0), 8)
    right = orbit(doubling, Q(1, 32), 8)
    distances = [circle_distance(x, y) for x, y in zip(left, right)]
    assert distances[:6] == [Q(1, 32), Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 2), Q(0)]
    assert all(x == y for x, y in zip(left[5:], right[5:]))
    constant_observer = lambda _: Q(0)
    report_pairs = [(constant_observer(x), constant_observer(y))
                    for x, y in zip(left, right)]
    assert all(a == b for a, b in report_pairs)
    assert any(x != y for x, y in zip(left, right))
    checks.append("doubling pair coalesces while constant reports never disagree")

    tent = lambda x: 2*x if x <= Q(1, 2) else 2*(1-x)
    logistic = lambda x: 4*x*(1-x)
    pair = (Q(1, 8), Q(7, 8))
    tent_image = tuple(tent(x) for x in pair)
    logistic_image = tuple(logistic(x) for x in pair)
    slopes = tuple(4-8*x for x in pair)
    assert tent_image == (Q(1, 4), Q(1, 4))
    assert logistic_image == (Q(7, 16), Q(7, 16)) and slopes == (Q(3), Q(-3))
    terminal_fibers = {logistic_image[0]: pair}
    side_target = {x: int(x > Q(1, 2)) for x in pair}
    assert len({side_target[x] for x in terminal_fibers[Q(7, 16)]}) == 2
    joined = {(side_target[x], logistic(x)): x for x in pair}
    assert len(joined) == 2
    checks.append("folded states alias terminal; source-side receipt resolves them")

    bin_pair = (Q(255, 1024), Q(257, 1024))
    bins = tuple(x // Q(1, 4) for x in bin_pair)
    assert abs(bin_pair[0]-bin_pair[1]) == Q(1, 512) < Q(1, 4)
    assert bins == (0, 1)
    assert orbit(lambda _: Q(0), initial, 10)[1:] == [Q(0)] * 10
    checks.append("bin-boundary instability and loose-upper-bound necessary-horizon controls")

    inputs = ["observational_succ/chaos_source_quotient.py",
              "observational_succ/logistic_observer_tree.py",
              "observational_succ/precision_transport.py", "observational_succ/entropy_transport.py"]
    manifest = json.loads((ROOT / "provenance/IMPORT_MANIFEST.json").read_text())
    assert not any(e["destination_path"] in inputs for e in manifest["entries"])
    return {"schema": "D28-exact-v1", "source_parent": PARENT,
            "python": sys.version.split()[0],
            "command": "PYTHONDONTWRITEBYTECODE=1 python research/2026-10-13/SWARM_ATLAS/D28_probe.py",
            "expected_exit": 0, "status": "TESTED MODEL; analytic proofs in D28.md",
            "all_assertions_passed": True, "checks": checks, "linear": linear,
            "defect_errors": list(map(str, errors)), "doubling_distances": list(map(str, distances)),
            "constant_report_pair_count": len(report_pairs),
            "tent_image": list(map(str, tent_image)), "logistic_image": list(map(str, logistic_image)),
            "logistic_derivatives": list(map(str, slopes)), "bin_reports": list(bins),
            "native_paths_absent_from_import_manifest": inputs,
            "input_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "physical_source_authenticated": False, "full_repository_suite_run": False,
            "claims_physical_precision_or_information_creation": False}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
