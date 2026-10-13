#!/usr/bin/env python3
"""C18 independent, bounded exact finite likelihood/gluing crucible.

No EOS algorithm is imported. The dictionaries below independently implement
finite pushforward, conditioning and conditional product. Current source-bound
and heuristic adapters are exercised separately as interface controls.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.source_coupling_bounds import frechet_bounds
from observational_succ.contextual_heuristics import (
    HeuristicError, HeuristicTower, ModelShape, ModelProbe, ProbeReceipt,
)

EOS = "b2774ca485db4b5b4f7ce92e535220352fb3af2f"


def project(law, indices):
    answer = {}
    for row, value in law.items():
        key = tuple(row[i] for i in indices)
        if value:
            answer[key] = answer.get(key, Q(0)) + value
    return answer


def glue(left, right):
    separator = project(left, (1,))
    if separator != project(right, (0,)):
        raise ValueError("incompatible separator")
    return {(a, y, b): u * v / separator[(y,)]
            for (a, y), u in left.items()
            for (z, b), v in right.items() if y == z and u and v}


def condition(law, likelihood):
    weighted = {x: p * likelihood[x] for x, p in law.items() if p}
    z = sum(weighted.values(), Q(0))
    if not z:
        raise ValueError("impossible evidence")
    return {x: p / z for x, p in weighted.items() if p}, z


def markov_prior(separator, left, right):
    return {(a, y, b): separator[y] * left[y][a] * right[y][b]
            for a, y, b in product(range(2), range(len(separator)), range(2))
            if separator[y] * left[y][a] * right[y][b]}


def rank_one_on_prior_support(prior, likelihood):
    for y in {x[1] for x in prior}:
        aa = sorted({x[0] for x in prior if x[1] == y})
        bb = sorted({x[2] for x in prior if x[1] == y})
        for a, c in combinations(aa, 2):
            for b, d in combinations(bb, 2):
                if (likelihood[a, y, b] * likelihood[c, y, d] !=
                        likelihood[a, y, d] * likelihood[c, y, b]):
                    return False
    return True


def check_square(prior, likelihood):
    posterior, z = condition(prior, likelihood)
    left, right = project(posterior, (0, 1)), project(posterior, (1, 2))
    reconstructed = glue(left, right)
    criterion = rank_one_on_prior_support(prior, likelihood)
    assert (posterior == reconstructed) == criterion
    # Independent conditional-expectation version of the pointwise criterion.
    sy = project(prior, (1,))
    u, v = project(prior, (0, 1)), project(prior, (1, 2))
    for (a, y, b), _ in prior.items():
        lm = sum(weight / sy[(y,)] * likelihood[a, y, k]
                 for (z, k), weight in v.items() if z == y)
        rm = sum(weight / sy[(y,)] * likelihood[k, y, b]
                 for (k, z), weight in u.items() if z == y)
        sm = sum(p * likelihood[x] for x, p in prior.items() if x[1] == y) / sy[(y,)]
        if sm:
            assert reconstructed.get((a, y, b), Q(0)) == prior[a, y, b] * lm * rm / (z * sm)
    return criterion


def heuristic_controls():
    models = tuple(ModelShape(h, "C18", frozenset(), 1, h) for h in ("h0", "h1"))
    kernel = {"h0": (Q(1, 4), Q(3, 4)), "h1": (Q(3, 4), Q(1, 4))}
    first = ModelProbe("read", "C18", ("yes", "no"), kernel, noise_group="one-source")
    def receipt(event, probe):
        return ProbeReceipt(event, "C18", 0, "binary", probe, "yes", "independent-probe")
    tower = HeuristicTower(models, frozenset(), source_id="C18", epoch=0, basis_id="binary",
                           prior={"h0": Q(1, 2), "h1": Q(1, 2)})
    assert tower.observe(first, receipt("e0", "read"))["h1"] == Q(3, 4)
    try:
        tower.observe(first, receipt("e1", "read"))
    except HeuristicError:
        rejected = True
    else:
        raise AssertionError("unconditioned shared-noise replay accepted")
    repeat = ModelProbe("copy", "C18", ("yes", "no"),
                        {h: (Q(1), Q(0)) for h in kernel},
                        noise_group="one-source", conditioned_on=("e0",))
    assert tower.observe(repeat, receipt("e1", "copy"))["h1"] == Q(3, 4)
    fresh = ModelProbe("fresh", "C18", ("yes", "no"), kernel, noise_group="fresh-source")
    assert tower.observe(fresh, receipt("e2", "fresh"))["h1"] == Q(9, 10)
    return {"unconditioned_noise_replay_rejected": rejected,
            "genuine_conditional_copy_posterior": "3/4",
            "fresh_conditionally_independent_posterior": "9/10"}


def main():
    counts = {"examined": 0, "impossible": 0, "commuting": 0, "noncommuting": 0}
    for p, r in product((Q(0), Q(1, 2), Q(1)), repeat=2):
        prior = markov_prior((Q(1),), ((p, 1-p),), ((r, 1-r),))
        for values in product((Q(0), Q(1, 2), Q(1)), repeat=4):
            likelihood = dict(zip(product(range(2), range(1), range(2)), values))
            counts["examined"] += 1
            try:
                good = check_square(prior, likelihood)
            except ValueError as err:
                assert str(err) == "impossible evidence"
                counts["impossible"] += 1
                continue
            counts["commuting" if good else "noncommuting"] += 1
    multi = 0
    for n in range(64):
        sy = (Q(n % 3, 2), 1-Q(n % 3, 2))
        left = tuple((Q((n+y) % 3, 2), 1-Q((n+y) % 3, 2)) for y in range(2))
        right = tuple((Q((n+2*y+1) % 3, 2), 1-Q((n+2*y+1) % 3, 2)) for y in range(2))
        prior = markov_prior(sy, left, right)
        likelihood = {x: Q((n+3*x[0]+x[1]+2*x[2]) % 5+1, 5)
                      for x in product(range(2), repeat=3)}
        check_square(prior, likelihood)
        multi += 1
    # Smallest nontrivial duplicated-evidence witness: two separator states,
    # singleton private coordinates. A one-state separator cannot change odds.
    prior = {(0, 0, 0): Q(1, 2), (0, 1, 0): Q(1, 2)}
    likelihood = {(0, 0, 0): Q(1, 4), (0, 1, 0): Q(3, 4)}
    post, _ = condition(prior, likelihood)
    assert post == glue(project(post, (0, 1)), project(post, (1, 2)))
    old = project(prior, (1,)); updated = project(post, (1,))
    fake = {y: updated[y] ** 2 / old[y] for y in old}
    duplicated = fake[(1,)] / sum(fake.values(), Q(0))
    assert duplicated == Q(9, 10) and updated[(1,)] == Q(3, 4)
    # Selection on A=B induces dependence from a conditionally independent prior.
    fair = markov_prior((Q(1),), ((Q(1, 2), Q(1, 2)),), ((Q(1, 2), Q(1, 2)),))
    collider = {x: Q(int(x[0] == x[2])) for x in fair}
    assert not check_square(fair, collider)
    collider_post, _ = condition(fair, collider)
    assert collider_post[(0, 0, 0)] == Q(1, 2)
    positive = {x: Q(1) if x[0] == x[2] else Q(1, 2) for x in fair}
    assert not check_square(fair, positive)
    positive_post, _ = condition(fair, positive)
    assert positive_post[(0, 0, 0)] == Q(1, 3)
    posterior_determinant = (positive_post[0, 0, 0] * positive_post[1, 0, 1] -
                             positive_post[0, 0, 1] * positive_post[1, 0, 0])
    assert posterior_determinant == Q(1, 12)
    bounds = frechet_bounds(Q(1, 2), Q(1, 2))
    assert (bounds.lower, bounds.upper, bounds.independent) == (0, Q(1, 2), Q(1, 4))
    # Conditioning may eliminate an entire separator fiber; no division by 0.
    killed = {(0, 0, 0): Q(1), (0, 1, 0): Q(0)}
    assert check_square(prior, killed)
    stale_left = {(0, 0): Q(1)}
    stale_right = {(1, 0): Q(1)}
    try:
        glue(stale_left, stale_right)
    except ValueError:
        mismatch_rejected = True
    else:
        raise AssertionError("separator mismatch accepted")
    source = subprocess.run(["git", "show", EOS+":observational_succ/source_aware_amalgamation.py"],
                            cwd=ROOT, check=True, capture_output=True).stdout
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout.strip()
    print(json.dumps({"schema": "SWM-C18-exact-v1", "parent": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "execution_head": head, "eos_source_commit": EOS,
        "eos_source_sha256": hashlib.sha256(source).hexdigest(),
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "current_source_sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in ("observational_succ/source_coupling_bounds.py",
                         "observational_succ/contextual_heuristics.py")},
        "finite_likelihood_scan": counts, "two_separator_controls": multi,
        "shared_evidence": {"correct": "3/4", "old_separator_shortcut": str(duplicated)},
        "collider": {"direct_intersection": "1/2", "reglued_intersection": "1/4",
                     "frechet_interval": [str(bounds.lower), str(bounds.upper)]},
        "strictly_positive_likelihood_counterexample": {
            "direct_intersection": "1/3", "reglued_intersection": "1/4",
            "posterior_determinant": str(posterior_determinant)},
        "separator_mismatch_rejected": mismatch_rejected, "heuristic_controls": heuristic_controls(),
        "zero_separator_and_killed_fiber_controls": "PASS", "exit": 0,
        "execution_history": [
            {"command": "python research/2026-10-13/SWARM_ATLAS/C18_probe.py",
             "exit": 1, "error": "ModuleNotFoundError: observational_succ",
             "repair": "Corrected local probe ROOT from parents[4] to parents[3]"},
            {"command": "python research/2026-10-13/SWARM_ATLAS/C18_probe.py", "exit": 0}],
        "proof_status": "PROVED LOCAL pen-and-paper; finite probes are regression evidence",
        "physical_source_authenticated": False, "lean_kernel_claimed": False}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
