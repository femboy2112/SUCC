"""Independent exact rational X11 controls; no author probe or runtime imports."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import random
import resource
import sys

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
Z = (Q(0),) * 4
I = (Q(1), Q(0), Q(0), Q(1))
P0, P1 = (Q(1), Q(0), Q(0), Q(0)), (Q(0), Q(0), Q(0), Q(1))
J = (Q(0), Q(1), Q(0), Q(0))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c * x for x in a)


def transpose(a):
    return (a[0], a[2], a[1], a[3])


def mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def cp(branch, x):
    out = Z
    for k in branch:
        out = add(out, mul(mul(k, x), transpose(k)))
    return out


def dual(branch, x):
    out = Z
    for k in branch:
        out = add(out, mul(mul(transpose(k), x), k))
    return out


def tr(x):
    return x[0] + x[3]


def rank(x):
    if x == Z:
        return 0
    return 2 if x[0]*x[3] != x[1]*x[2] else 1


def psd(x):
    return x[1] == x[2] and x[0] >= 0 and x[3] >= 0 and x[0]*x[3] >= x[1]*x[2]


def tni(branch):
    return psd(add(I, scale(dual(branch, I), Q(-1))))


def dominates(a, b):
    return rank(add(a, b)) == rank(a)


def same_kernel(a, b):
    return rank(a) == rank(b) == rank(add(a, b))


def allowed(sigma):
    return [i for i, x in enumerate(sigma) if tr(x) > 0]


def cycle_bounds():
    singles = [(tuple(Q(x, 2) for x in a),) for a in product((-1, 0, 1), repeat=4)]
    rng = random.Random(831107)
    pairs = [tuple(tuple(Q(rng.choice((-1, 0, 1)), 3) for _ in range(4))
                   for _ in range(2)) for _ in range(128)]
    for branch in singles + pairs:
        assert tni(branch)
        effects = [I]
        for _ in range(6):
            effects.append(dual(branch, effects[-1]))
        for a, b in zip(effects, effects[1:]):
            assert psd(a) and psd(b)
            assert rank(add(a, b)) == rank(a)  # ker(a) subset ker(b)
        assert all(same_kernel(effects[2], e) for e in effects[3:])
        for k in range(5):
            if same_kernel(effects[k], effects[k+1]):
                assert same_kernel(effects[k+1], effects[k+2])
    shift_effects = [I, dual((J,), I), dual((J,), dual((J,), I))]
    assert [rank(x) for x in shift_effects] == [2, 1, 0]
    return {"maps": len(singles) + len(pairs), "nilpotent_effect_ranks": [2, 1, 0],
            "plateau_checked_through_cycles": 6}


def generator_bounds():
    branches = ((I,), (P0,), (P1,), (J,), (P0, J))
    count = admitted = 0
    for n in (1, 2):
        for successor in product(range(n), repeat=n):
            for output in product(range(len(branches)), repeat=n):
                for initial in range(n):
                    seen, path, current = {}, [], initial
                    while current not in seen:
                        seen[current] = len(path)
                        path.append(current)
                        current = successor[current]
                    mu, lam = seen[current], len(path)-seen[current]
                    assert mu+lam <= n and mu+2*lam <= 2*n
                    sigma = (P0, P1)
                    stages = [allowed(sigma)]
                    current = initial
                    for _ in range(mu+8*lam):
                        sigma = tuple(cp(branches[output[current]], x) for x in sigma)
                        current = successor[current]
                        stages.append(allowed(sigma))
                    assert all(a == stages[mu+2*lam] for a in stages[mu+2*lam:])
                    if stages[-1]:
                        admitted += 1
                        assert all(a == stages[mu+lam] for a in stages[mu+lam:])
                    count += 1
    return {"complete_tables": count, "surviving_tables": admitted,
            "author_deadline_matches_later_prefixes": True,
            "reviewer_promised_one_cycle_deadline_matches": True}


def controls():
    reset = (P0, J)
    sigma = tuple(cp(reset, p) for p in (P0, P1))
    assert sigma == (P0, P0) and allowed(sigma) == [0, 1]
    assert dominates(sigma[0], sigma[1]) and dominates(sigma[1], sigma[0])
    assert not dominates(P0, P1) and not dominates(P1, P0)

    full_branch = (scale(P0, Q(1, 2)), (Q(0), Q(0), Q(1, 2), Q(0)), J)
    assert tni(full_branch)
    a, b = (cp(full_branch, p) for p in (P0, P1))
    assert a == scale(I, Q(1, 4)) and b == P0
    assert dominates(a, b) and not dominates(b, a)
    assert (tr(a), tr(b)) == (Q(1, 2), Q(1))  # not a trace-preserving channel

    # A non-coordinate rational separating projector, independently constructed.
    line = (Q(1, 4), Q(1, 4), Q(1, 4), Q(1, 4))
    separator = (Q(1, 2), Q(-1, 2), Q(-1, 2), Q(1, 2))
    assert mul(separator, separator) == separator
    assert cp((separator,), line) == Z
    assert tr(cp((separator,), scale(I, Q(1, 4)))) == Q(1, 4)
    assert add(dual((separator,), I), dual((add(I, scale(separator, -1)),), I)) == I

    idle = (Q(1), Q(0), Q(0), Q(3, 5))
    kill = scale(P1, Q(4, 5))
    assert add(dual((idle,), I), dual((kill,), I)) == I
    for delay in (0, 3, 19):
        sigma = (P0, P1)
        for _ in range(delay):
            sigma = tuple(cp((idle,), x) for x in sigma)
            assert allowed(sigma) == [0, 1]
        sigma = tuple(cp((kill,), x) for x in sigma)
        assert allowed(sigma) == [1]

    scalar_idle, scalar_other = scale(I, Q(3, 5)), scale(I, Q(4, 5))
    assert add(dual((scalar_idle,), I), dual((scalar_other,), I)) == I
    probability_prefix_12 = Q(9, 25)**12
    assert 0 < probability_prefix_12 < Q(1, 1000)

    # Oracle cylinders and C2 label direction: both surviving sets and exclusions.
    for bit in (0, 1):
        sigma = (P0, P1)
        for _ in range(11):
            sigma = tuple(cp((I,), x) for x in sigma)
        sigma = tuple(cp(((P0, P1)[1-bit],), x) for x in sigma)
        assert allowed(sigma) == [1-bit]
    reductions = []
    for excluded in (None, 0, 1):
        sigma = (P0, P1)
        branch = (I,) if excluded is None else ((P0, P1)[1-excluded],)
        sigma = tuple(cp(branch, x) for x in sigma)
        reductions.append({"excluded": excluded, "survivors": allowed(sigma)})

    # Removing the dimension hypothesis: persistent source plus a 3-step nilpotent path.
    v = (0, 0, 0, 1)
    history = [v]
    for _ in range(3):
        v = (v[0], v[2], v[3], 0)
        history.append(v)
    assert history[2] != (0,)*4 and history[3] == (0,)*4
    return {"reset_safe_choices": [0, 1], "reset_original_bit_identified": False,
            "dominance_branch_traces": ["1/2", "1"], "branch_is_TP_channel": False,
            "restricted_identity_toolkit_has_safe_incomparable_choices": True,
            "two_outcome_stationary_delays": [0, 3, 19],
            "zero_probability_limit_prefix12": str(probability_prefix_12),
            "negative_name_projector_labels": reductions,
            "dimension_four_death_step": 3}


def main():
    result = {"cycle_kernel": cycle_bounds(), "generator": generator_bounds(),
              "countermodels": controls()}
    source = Path('/home/leah/succ_lab/swm-x11/research/2026-10-13/SWARM_ATLAS/X11.md')
    candidate = source.parent/'reviews/C19_EFFECTIVE_SELECTOR_CANDIDATE.md'
    result.update({"status": "INDEPENDENT_EXACT_CONTROLS_PASS", "exit_code": 0,
        "author_commit": "30d630504ee429bfcba8be83f921eb57a2b8eb36",
        "review_parent": "f57d09eb456e49a1ae10f8a614bc2b8cc15993d0",
        "command": "PYTHONDONTWRITEBYTECODE=1 timeout 30s python research/2026-10-13/SWARM_ATLAS/reviews/X11_B11_probe.py",
        "limits": {"address_space_bytes": 256*1024**2, "cpu_seconds": 20},
        "author_probe_or_receipt_read": False, "provider_source_lineage_independent": False,
        "hashes": {"author_dossier_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                   "root_candidate_sha256": hashlib.sha256(candidate.read_bytes()).hexdigest(),
                   "review_probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        "finite_controls_prove_universal_theorems": False})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
