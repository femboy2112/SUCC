#!/usr/bin/env python3
"""D32 bounded independent exact delay probe; no production/default changes.

All matrix certificates use integer/Fraction arithmetic implemented here.
Native future-probe code is used only for a comparison, never as the rank oracle.
MODEL_ENCOUNTER denotes a simulated chronological encounter, not physical evidence.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
from random import Random
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.nerode_probe_growth import ObserverDynamics, grow_probe_grammar


def mat(rows):
    if not rows or not rows[0] or len(rows) > 8 or len(rows[0]) > 8:
        raise ValueError("nonempty matrix within 8x8 budget")
    if any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("rectangular matrix required")
    if any(type(v) not in (int, Q) for row in rows for v in row):
        raise ValueError("exact integer/Fraction required")
    return tuple(tuple(Q(v) for v in row) for row in rows)


def identity(n):
    return mat(tuple(tuple(int(i == j) for j in range(n)) for i in range(n)))


def mm(a, b):
    if len(a[0]) != len(b):
        raise ValueError("matrix dimensions differ")
    return tuple(tuple(sum((x*y for x, y in zip(row, col)), Q())
                       for col in zip(*b)) for row in a)


def mv(a, x):
    if any(type(v) not in (int, Q) for v in x):
        raise ValueError("exact source vector required")
    return tuple(row[0] for row in mm(a, tuple((Q(v),) for v in x)))


def delays(f, c, k):
    if len(f) != len(f[0]) or len(c[0]) != len(f) or not 1 <= k <= 8:
        raise ValueError("square law, compatible readout, 1..8 reports")
    rows, current = (), c
    for _ in range(k):
        rows += current
        current = mm(current, f)
    return mat(rows)


def rref(a):
    w = [list(row) for row in a]
    pivots = []
    for col in range(len(w[0])):
        p = next((j for j in range(len(pivots), len(w)) if w[j][col]), None)
        if p is None:
            continue
        row = len(pivots)
        w[row], w[p] = w[p], w[row]
        d = w[row][col]
        w[row] = [v/d for v in w[row]]
        for j in range(len(w)):
            if j != row:
                d = w[j][col]
                w[j] = [x-d*y for x, y in zip(w[j], w[row])]
        pivots.append(col)
        if len(pivots) == len(w):
            break
    return tuple(tuple(row) for row in w), tuple(pivots)


def rank(a):
    return len(rref(a)[1])


def determinant(a):
    """Independent Leibniz minor verifier, bounded to n <= 5."""
    n = len(a)
    if n > 5 or any(len(row) != n for row in a):
        raise ValueError("minor budget")
    total = Q()
    for p in permutations(range(n)):
        sign = (-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = Q(sign)
        for i in range(n):
            term *= a[i][p[i]]
        total += term
    return total


def minor_rank(a):
    for k in range(min(len(a), len(a[0])), 0, -1):
        for rs in combinations(range(len(a)), k):
            for cs in combinations(range(len(a[0])), k):
                if determinant(tuple(tuple(a[i][j] for j in cs) for i in rs)):
                    return k
    return 0


def decoder(o, target):
    """Solve L O = target by transposed equations; free coefficients set to zero."""
    if any(len(t) != len(o[0]) for t in target):
        raise ValueError("target dimension mismatch")
    result = []
    for t in target:
        equations = tuple(tuple(o[j][i] for j in range(len(o))) + (t[i],)
                          for i in range(len(o[0])))
        w, pivots = rref(equations)
        if len(o) in pivots:
            raise ValueError("target not constant on delay fibers")
        l = [Q()] * len(o)
        for i, p in enumerate(pivots):
            l[p] = w[i][-1]
        result.append(tuple(l))
    l = tuple(result)
    assert mm(l, o) == target
    return l


def kernel_basis(o):
    w, pivots = rref(o)
    result = []
    for free in range(len(o[0])):
        if free in pivots:
            continue
        v = [Q()] * len(o[0])
        v[free] = Q(1)
        for i, p in enumerate(pivots):
            v[p] = -w[i][free]
        assert mv(o, v) == (Q(),) * len(o)
        result.append(tuple(v))
    return tuple(result)


@dataclass(frozen=True)
class Encounter:
    source: str
    version: int
    epoch: int
    basis: str
    report: tuple[Q, ...]
    arrival_epoch: int
    kind: str = "MODEL_ENCOUNTER"

    def __post_init__(self):
        if (type(self.source) is not str or not self.source or
                type(self.basis) is not str or not self.basis or
                any(type(v) is not int or v < 0
                    for v in (self.version, self.epoch, self.arrival_epoch)) or
                not self.report or any(type(v) not in (int, Q) for v in self.report)):
            raise ValueError("exact source-tagged encounter required")


def chronology(f, c, x, k, *, source="D32-source", basis="passive-C"):
    records = []
    for epoch in range(k):
        records.append(Encounter(source, 0, epoch, basis, mv(c, x), epoch))
        x = mv(f, x)
    return tuple(records)


def retained_delays(records, k, *, source="D32-source", basis="passive-C",
                    checkpoint=None):
    if len(records) != k:
        raise ValueError("missing chronological encounter")
    records = tuple(sorted(records, key=lambda r: r.epoch))
    for epoch, r in enumerate(records):
        if (r.source, r.version, r.epoch, r.basis, r.kind) != (
                source, 0, epoch, basis, "MODEL_ENCOUNTER"):
            raise ValueError("source/version/epoch/basis/evidence-kind mismatch")
        if r.arrival_epoch < r.epoch or (checkpoint is not None and
                                        r.arrival_epoch > checkpoint):
            raise ValueError("receipt not causally available at checkpoint")
    return tuple(v for r in records for v in r.report)


def expect_rejection(call):
    try:
        call()
    except ValueError:
        return True
    raise AssertionError("negative control accepted")


def run():
    f, c = mat(((1, 1), (0, 1))), mat(((1, 0),))
    o = delays(f, c, 2)
    l = decoder(o, identity(2))
    lifted = mm(mm(o, f), l)
    x = (Q(-2), Q(3))
    events = chronology(f, c, x, 3)
    y = retained_delays(events[:2], 2)
    assert mv(l, y) == x
    assert mm(l, o) == identity(2) and mm(mm(o, l), o) == o
    assert mm(lifted, o) == mm(o, f)
    assert mv(lifted, y) == tuple(v for r in events[1:] for v in r.report)
    provenance_mutations = {
        name: expect_rejection(lambda altered=altered: retained_delays(altered, 2))
        for name, altered in {
            "prediction": (replace(events[0], kind="MODEL_PREDICTION"), events[1]),
            "different_source": (events[0], replace(events[1], source="other")),
            "stale_version": (events[0], replace(events[1], version=1)),
            "reset_epoch": (events[0], replace(events[1], epoch=0)),
            "arrival_predates_event": (events[0], replace(events[1], arrival_epoch=0)),
            "different_basis": (events[0], replace(events[1], basis="reset-C")),
        }.items()
    }
    late = (events[1], replace(events[0], arrival_epoch=2))
    assert retained_delays(late, 2, checkpoint=2) == y
    assert expect_rejection(lambda: retained_delays(late, 2, checkpoint=1))

    swap = mat(((0, 1), (1, 0)))
    b = mat(((1, 0), (0, 0)))
    measured = mm(swap, b)
    native = ObserverDynamics("D32-bit-swap", 0, "first-bit",
                             ("00", "01", "10", "11"),
                             ("00", "10", "01", "11"),
                             ("0", "0", "1", "1"))
    grammar = grow_probe_grammar(native, budget_horizon=2)
    predictions = tuple(Q(int(native.probe("01", j))) for j in range(4))
    passive = retained_delays(chronology(swap, c, (0, 1), 4), 4)
    backaction = retained_delays(chronology(measured, c, (0, 1), 4,
                                 basis="declared-reset-C"), 4,
                                 basis="declared-reset-C")
    assert passive == predictions == (Q(0), Q(1), Q(0), Q(1))
    assert backaction == (Q(0),)*4
    hidden = (Q(0), Q(1))
    assert mv(measured, hidden) == (Q(0), Q(0)) and mv(c, hidden) == (Q(0),)

    sharp = []
    for n in range(2, 7):
        cycle = mat(tuple(tuple(int(i == (j-1) % n) for j in range(n))
                          for i in range(n)))
        read = mat((tuple(int(j == 0) for j in range(n)),))
        v = tuple(Q(int(j == n-1)) for j in range(n))
        assert mv(delays(cycle, read, n-1), v) == (Q(0),)*(n-1)
        assert rank(delays(cycle, read, n)) == n
        sharp.append({"dimension": n, "ranks": [rank(delays(cycle, read, k))
                                                   for k in range(1, n+1)]})

    aliases = {}
    for name, law, read, a, z in (
        ("identity_hidden_coordinate", identity(2), c, (0, 0), (0, 1)),
        ("clock_stride_four", identity(2), c, (0, 1), (0, -1)),
        ("reset_backaction", measured, c, (0, 0), (0, 1)),
    ):
        delta = tuple(Q(x-y) for x, y in zip(a, z))
        obs = delays(law, read, 2)
        assert mv(obs, delta) == (Q(),)*len(obs)
        aliases[name] = {"pair": (a, z), "O_n_rank": rank(obs),
                         "kernel_witness": delta, "all_future_via_n_bound": True}
    quarter_clock = mat(((0, -1), (1, 0)))
    fourth = identity(2)
    for _ in range(4):
        fourth = mm(quarter_clock, fourth)
    assert fourth == identity(2)
    assert rank(delays(quarter_clock, c, 2)) == 2

    def logistic(t):
        return 4*t*(1-t)
    a, z = Q(1, 4), Q(3, 4)
    assert logistic(a) == logistic(z) == Q(3, 4)
    aliases["logistic_post_update_readout"] = {
        "original_pair": (a, z), "readout_is_f_not_identity": True,
        "same_first_report": logistic(a), "same_successor": logistic(z),
        "all_future_by_exact_first_merge": True,
        "identity_readout_at_original_epoch_would_separate": a != z,
        "critical_readout_derivative_at_half": 0}

    zero = mat(((0, 0), (0, 0)))
    lost = delays(zero, c, 2)
    current_target = zero  # full state at epoch 1 = F x0
    current_decoder = decoder(lost, current_target)
    assert rank(lost) == 1
    assert expect_rejection(lambda: decoder(lost, identity(2)))
    partial = decoder(delays(identity(2), c, 2), c)

    eps = Q(1, 10**6)
    nearly = delays(mat(((1, eps), (0, 1))), c, 2)
    near_inverse = decoder(nearly, identity(2))
    norm = lambda a: max(sum(abs(v) for v in row) for row in a)
    condition = norm(nearly)*norm(near_inverse)
    assert determinant(nearly) == eps and condition == 2000002
    first_report, second_report = mv(nearly, (0, 0)), mv(nearly, (0, 1))
    ambiguous_report = (Q(), eps/2)
    assert max(abs(a-b) for a, b in zip(ambiguous_report, first_report)) == eps/2
    assert max(abs(a-b) for a, b in zip(ambiguous_report, second_report)) == eps/2
    tiny = Q(1, 10**18)
    assert Q(1)+tiny != Q(1) and float(Q(1)+tiny) == float(Q(1))

    rng = Random(32013)
    fresh = []
    for trial in range(12):
        n = 2 + trial % 3
        law = mat(tuple(tuple(rng.randrange(-2, 3) for _ in range(n))
                        for _ in range(n)))
        read = mat((tuple(rng.randrange(-2, 3) for _ in range(n)),))
        obs = delays(law, read, n)
        r = rank(obs)
        assert r == minor_rank(obs)
        assert rank(delays(law, read, n+1)) == r
        fresh_x = tuple(Q(rng.randrange(-7, 8), rng.randrange(1, 5)) for _ in range(n))
        assert mv(obs, fresh_x) == retained_delays(chronology(law, read, fresh_x, n), n)
        if r == n:
            inverse = decoder(obs, identity(n))
            assert mv(inverse, mv(obs, fresh_x)) == fresh_x
        else:
            witness = kernel_basis(obs)[0]
            assert witness != (Q(),)*n and mv(obs, witness) == (Q(),)*n
            assert expect_rejection(lambda: decoder(obs, identity(n)))
        target_checks = []
        for target in identity(n):
            factors = rank(obs + (target,)) == r
            if factors:
                dec = decoder(obs, (target,))
                assert mv(dec, mv(obs, fresh_x)) == mv((target,), fresh_x)
            else:
                assert expect_rejection(lambda: decoder(obs, (target,)))
            target_checks.append(factors)
        fresh.append({"trial": trial, "dimension": n, "F": law, "C": read,
                      "O_n": obs, "rank": r, "independent_minor_rank": r,
                      "fresh_state": fresh_x, "coordinate_target_factors": target_checks,
                      "full_inverse": inverse if r == n else None,
                      "nonzero_kernel_witness": witness if r < n else None})

    return {
        "dossier": "D32", "parent": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "arithmetic": "exact integer/Fraction; one separately labeled float-alias demonstration",
        "physical_source_authenticated": False,
        "positive": {"F": f, "C": c, "O_2": o, "inverse_on_image": l,
                     "delay_update": lifted, "initial": x, "chronological_reports": events,
                     "maps_commute": True},
        "source_mutations_rejected": provenance_mutations,
        "delayed_arrival": {"sorted_by_event_epoch": True,
                            "same_delay_vector_at_checkpoint_2": True,
                            "unavailable_at_checkpoint_1_rejected": True},
        "generated_versus_encountered": {
            "native_generated_future_probes": predictions,
            "passive_single_trajectory": passive,
            "declared_readout_backaction": b, "actual_update_FB": measured,
            "actual_backaction_trajectory": backaction,
            "native_physical_counterfactual_reset_available":
                grammar.physical_counterfactual_reset_available},
        "sharp_finite_delay_bound": sharp,
        "all_future_aliases": aliases,
        "clock_stride_one_rank": rank(delays(quarter_clock, c, 2)),
        "original_versus_current": {"O_2_rank": rank(lost),
            "original_full_target_rejected": True,
            "current_full_target": current_target, "current_decoder": current_decoder,
            "partial_original_target_decoder": partial},
        "conditioning": {"epsilon": eps, "exact_rank": rank(nearly),
            "exact_determinant": determinant(nearly), "exact_infinity_condition": condition,
            "noise_radius_for_ambiguity": eps/2,
            "distinct_originals": ((0, 0), (0, 1)),
            "exact_report_pair": (first_report, second_report),
            "shared_noisy_report": ambiguous_report,
            "float_alias_epsilon": tiny, "exact_distinct_float_equal": True,
            "float_is_not_proof_certificate": True},
        "fresh_seed": 32013, "fresh_cases": fresh,
        "input_controls": {"float_rejected": expect_rejection(lambda: mat(((0.5,),))),
                           "bool_rejected": expect_rejection(lambda: mat(((True,),))),
                           "float_source_rejected": expect_rejection(
                               lambda: chronology(f, c, (0.5, 1), 2))},
    }


def encode(v):
    if isinstance(v, Q):
        return str(v)
    if isinstance(v, Encounter):
        return {k: encode(x) for k, x in vars(v).items()}
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [encode(x) for x in v]
    return v


if __name__ == "__main__":
    print(json.dumps(encode(run()), indent=2, sort_keys=True))
