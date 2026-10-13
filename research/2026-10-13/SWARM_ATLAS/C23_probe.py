"""C23: bounded exact controls for conditional, source-calibrated evidence.

Run from the repository root with PYTHONPATH=. and no bytecode writes.
This is a mathematical model probe; no empirical law is authenticated.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

from observational_succ.contextual_heuristics import ModelProbe, HeuristicError
from observational_succ.heuristic_evidence_martingales import (
    adaptive_crossing_probability, lr_step,
)
from observational_succ.heuristic_joint_noise import FiniteJointNoise
from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument


def support_factor(p, q, index):
    """Ratio only on null support; never divide by a null-zero probability."""
    assert sum(p, Q(0)) == sum(q, Q(0)) == 1
    assert all(x >= 0 for x in p + q)
    if not p[index]:
        raise ValueError("NULL_IMPOSSIBLE: no numerical likelihood update")
    return q[index] / p[index]


def null_mean_factor(p, q):
    return sum((p[i] * support_factor(p, q, i)
                for i in range(len(p)) if p[i]), Q(0))


def main():
    p0, p1 = (Q(1, 2), Q(1, 2)), (Q(3, 4), Q(1, 4))
    probe = ModelProbe("fresh", "C23", ("yes", "no"), {"H0": p0, "H1": p1})
    alpha = Q(1, 5)
    fresh = adaptive_crossing_probability(lambda _: probe, 5,
        null="H0", alternative="H1", alpha=alpha)
    assert fresh["null_cross_probability"] == Q(1, 16)
    alternate = ModelProbe("alternate", "C23", ("yes", "no"),
        {"H0": (Q(1, 4), Q(3, 4)), "H1": (Q(1, 2), Q(1, 2))})
    adaptive = adaptive_crossing_probability(
        lambda h: probe if not h or h[-1][1] == "yes" else alternate,
        5, null="H0", alternative="H1", alpha=alpha)
    assert adaptive["null_cross_probability"] <= alpha

    duplicate = FiniteJointNoise(
        {"H0": p0, "H1": p1},
        {m: {"first": ("yes", "no"), "copy": ("yes", "no")}
         for m in ("H0", "H1")})
    conditional = tuple(duplicate.conditioned_distribution(m, "copy", ("yes", "no"),
        (("first", "yes"),)) for m in ("H0", "H1"))
    assert conditional == ((Q(1), Q(0)), (Q(1), Q(0)))
    good_second_factor = support_factor(*conditional, 0)
    assert good_second_factor == 1
    correct_wealths = []
    for i, outcome in enumerate(("yes", "no")):
        wealth = support_factor(p0, p1, i)
        history = (("first", outcome),)
        for _ in range(4):
            laws = tuple(duplicate.conditioned_distribution(m, "copy", ("yes", "no"),
                         history) for m in ("H0", "H1"))
            assert null_mean_factor(*laws) == 1
            wealth *= support_factor(*laws, i)
            history += (("copy", outcome),)
        correct_wealths.append(wealth)
    correct_crossing = sum((p0[i] for i, w in enumerate(correct_wealths)
                            if w >= 1 / alpha), Q(0))
    assert tuple(correct_wealths) == (Q(3, 2), Q(1, 2))
    assert correct_crossing == 0
    naive_yes = Q(3, 2) ** 5
    naive_no = Q(1, 2) ** 5
    false_crossing = sum((p0[i] for i, w in enumerate((naive_yes, naive_no))
                          if w >= 1 / alpha), Q(0))
    assert naive_yes == Q(243, 32)
    assert false_crossing == Q(1, 2) > alpha
    naive_mean = (naive_yes + naive_no) / 2
    assert naive_mean == Q(61, 16)

    correlated = FiniteJointNoise(
        {"H0": (Q(3, 8), Q(1, 8), Q(1, 8), Q(3, 8)),
         "H1": (Q(5, 8), Q(1, 8), Q(1, 8), Q(1, 8))},
        {m: {"A": ("yes", "yes", "no", "no"),
             "B": ("yes", "no", "yes", "no")}
         for m in ("H0", "H1")})
    cp, cq = (correlated.conditioned_distribution(m, "B", ("yes", "no"),
        (("A", "yes"),)) for m in ("H0", "H1"))
    assert null_mean_factor(cp, cq) == 1
    assert support_factor(cp, cq, 0) == Q(10, 9)
    wrong_conditional_mean = sum((cp[i] * support_factor(p0, p1, i)
                                 for i in range(2)), Q(0))
    assert wrong_conditional_mean == Q(5, 4) > 1

    zero_probe = ModelProbe("deterministic", "C23", ("yes", "no"),
        {"H0": (1, 0), "H1": (1, 0)})
    try:
        lr_step(1, zero_probe, "yes", null="H0", alternative="H1")
    except HeuristicError as exc:
        native_zero_rejection = str(exc)
    else:
        raise AssertionError("Native full-support boundary changed")
    assert "full null support" in native_zero_rejection
    assert null_mean_factor((Q(1), Q(0)), (Q(1), Q(0))) == 1
    assert null_mean_factor((Q(1), Q(0)), (Q(1, 2), Q(1, 2))) == Q(1, 2)
    try:
        support_factor((Q(1), Q(0)), (Q(1, 2), Q(1, 2)), 1)
    except ValueError as exc:
        impossible_outcome = str(exc)
    else:
        raise AssertionError("A null-zero outcome was divided")

    carrier = FiniteCarrier(2, (
        Instrument("read_reset", (0, 1), (0, 0), (True, True)),
        Instrument("read", (0, 1), (0, 1), (True, True)),
        Instrument("read_invert", (1, 0), (0, 1), (True, True))),
        "C23-declared-source", "binary")
    first_traces = tuple(carrier.run(s, ("read_reset",)) for s in (0, 1))
    # The policy uses only the previous public outcome; the source is audited separately.
    traces = tuple(carrier.run(s, ("read_reset",
        "read" if first_traces[s].observed_values[-1] == 0 else "read_invert"))
        for s in (0, 1))
    assert tuple(t.observed_values for t in traces) == ((0, 0), (1, 1))
    assert all(t.terminal_state == 0 for t in traces)
    after_reset_factors, stale_means = [], []
    for first_y in (0, 1):
        laws = []
        for weights in (p0, p1):
            compatible = tuple(i for i, t in enumerate(traces)
                               if t.observed_values[0] == first_y)
            mass = sum((weights[i] for i in compatible), Q(0))
            laws.append(tuple(sum((weights[i] for i in compatible
                if traces[i].observed_values[1] == y), Q(0)) / mass for y in (0, 1)))
        assert null_mean_factor(*laws) == 1
        after_reset_factors.append(support_factor(*laws, first_y))
        action = "read" if first_y == 0 else "read_invert"
        stale_laws = tuple(tuple(sum((weights[i] for i in (0, 1)
            if carrier.action(action).outputs[i] == y), Q(0)) for y in (0, 1))
            for weights in (p0, p1))
        stale_means.append(support_factor(*stale_laws, first_y))
    assert after_reset_factors == [Q(1), Q(1)]
    assert stale_means == [Q(3, 2), Q(3, 2)]

    fine_lr = tuple(support_factor(p0, p1, i) for i in range(2))
    forgotten_lr = sum((p0[i] * fine_lr[i] for i in range(2)), Q(0))
    assert forgotten_lr == 1 > fine_lr[1]
    fine_second_moment = sum((p0[i] * fine_lr[i] ** 2 for i in range(2)), Q(0))
    assert fine_second_moment == Q(5, 4) >= forgotten_lr ** 2

    root = Path(__file__).resolve().parents[3]
    paths = ("observational_succ/heuristic_evidence_martingales.py",
             "observational_succ/heuristic_joint_noise.py",
             "observational_succ/contextual_heuristics.py",
             "observational_succ/noncommuting_proof_transport.py")
    result = {
        "candidate": "C23", "source_parent": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "command": "PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. python research/2026-10-13/SWARM_ATLAS/C23_probe.py",
        "execution_exit_code": 0,
        "prior_execution_failure": {"exit_code": 1,
            "finding": "Initial probe had an unclosed action tuple; syntax repaired before successful rerun."},
        "arithmetic": "exact fractions; no random sampling", "all_assertions_passed": True,
        "fresh_iid_crossing_probability": fresh["null_cross_probability"], "alpha": alpha,
        "public_adaptive_crossing_probability": adaptive["null_cross_probability"],
        "public_adaptive_tree_nodes": adaptive["tree_nodes"],
        "duplicate_naive_yes_wealth": naive_yes, "duplicate_naive_null_mean": naive_mean,
        "duplicate_false_crossing_probability": false_crossing,
        "duplicate_correct_terminal_wealths": correct_wealths,
        "duplicate_correct_crossing_probability": correct_crossing,
        "correlated_correct_second_yes_factor": Q(10, 9),
        "correlated_wrong_conditional_factor_mean": wrong_conditional_mean,
        "native_zero_support_rejection": native_zero_rejection,
        "deterministic_supported_factor": Q(1), "singular_supported_mean": Q(1, 2),
        "null_zero_observation_gate": impossible_outcome,
        "destructive_public_traces": tuple(t.public_signature for t in traces),
        "destructive_after_reset_factors_by_public_branch": after_reset_factors,
        "destructive_stale_after_reset_means_by_public_branch": stale_means,
        "fine_lr": fine_lr, "forgetful_lr": forgotten_lr,
        "fine_second_moment": fine_second_moment, "coarse_second_moment": Q(1),
        "source_sha256": {p: sha256((root / p).read_bytes()).hexdigest() for p in paths},
        "dossier_sha256": sha256(Path(__file__).with_name("C23.md").read_bytes()).hexdigest(),
        "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "physical_source_authenticated": False, "universal_mathematical_proof_claimed": False,
        "full_suite_run": False, "theorem_status": "CLASSICAL; transparent local derivation",
        "finite_control_status": "TESTED MODEL", "blind_product_status": "REFUTED",
    }
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
