"""C17 bounded exact oracle; independent of observational_succ runtime modules.

Finite rational model checks corroborate the dossier's algebraic proof, rather
than certifying physical source maps or an infinite-domain theorem.
"""
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path


def exact(value):
    if type(value) not in (int, F):
        raise ValueError("Only exact int/Fraction weights")
    return F(value)


def push(law, f, g):
    result = {}
    for (s, q), weight in law.items():
        key = (f(s), g(q))
        result[key] = result.get(key, F(0)) + weight
    return {k: v for k, v in result.items() if v}


def step(law, history, action, outcome, states, kernel):
    result = {}
    for (s, q), weight in law.items():
        for after in states:
            value = weight * kernel(history, action, s, q, outcome, after)
            if value:
                key = (s, after)
                result[key] = result.get(key, F(0)) + value
    predictive = sum(result.values(), F(0))
    if not predictive:
        raise ValueError("Zero-probability history: posterior undefined")
    return {key: value / predictive for key, value in result.items()}, predictive


def path_oracle(prior, word, states, kernel):
    """Enumerate complete hidden paths, not the filtering recurrence."""
    result = {}
    for (s, initial), weight in prior.items():
        for internal in product(states, repeat=len(word)):
            path = (initial,) + internal
            value = weight
            for i, (action, outcome) in enumerate(word):
                value *= kernel(word[:i], action, s, path[i], outcome, path[i+1])
            if value:
                key = (s, path[-1])
                result[key] = result.get(key, F(0)) + value
    mass = sum(result.values(), F(0))
    return {k: v / mass for k, v in result.items() if v}, mass


def check_rows(sources, states, histories, kernel):
    rows = 0
    for h, a, s, q in product(histories, (0, 1), sources, states):
        row = [exact(kernel(h, a, s, q, o, r))
               for o, r in product((0, 1), states)]
        assert all(v >= 0 for v in row) and sum(row, F(0)) == 1
        rows += 1
    return rows


def square(sources, states, target_states, histories, kernel, other, f, g):
    for h, a, s, q, o, z in product(
            histories, (0, 1), sources, states, (0, 1), target_states):
        left = sum((kernel(h, a, s, q, o, r)
                    for r in states if g(r) == z), F(0))
        right = other(h, a, f(s), g(q), o, z)
        if left != right:
            return {"history": h, "action": a, "source": s,
                    "carrier": q, "outcome": o, "after": z,
                    "left": str(left), "right": str(right)}
    return None


def base(h, a, s, q, o, r):
    # History-dependent, correlated outcome/state law; no source-label access.
    c = q ^ a ^ (sum(outcome for _, outcome in h) % 2)
    return {(c, c): F(1, 2), (c, 1-c): F(1, 4),
            (1-c, c): F(1, 8), (1-c, 1-c): F(1, 8)}[(o, r)]


def fine(h, a, s, q, o, r):
    nuisance = F(1, 3) if (s[1] ^ q[1] ^ a) else F(2, 3)
    return base(h, a, s[0], q[0], o, r[0]) * (
        nuisance if r[1] == 0 else 1-nuisance)


def final(h, a, s, q, o, r):
    return base(h, a, 0, 1-q, o, 1-r)


def main():
    binary = (0, 1)
    pairs = tuple(product(binary, repeat=2))
    events = tuple(product(binary, repeat=2))
    histories = tuple(w for n in range(3) for w in product(events, repeat=n))
    words = tuple(w for n in range(4) for w in product(events, repeat=n))
    f = g = lambda x: x[0]
    u, v = lambda s: 0, lambda q: 1-q
    row_counts = [check_rows(pairs, pairs, histories, fine),
                  check_rows(binary, binary, histories, base),
                  check_rows((0,), binary, histories, final)]
    assert square(pairs, pairs, binary, histories, fine, base, f, g) is None
    assert square(binary, binary, binary, histories, base, final, u, v) is None
    assert square(pairs, pairs, binary, histories, fine, final,
                  lambda s: u(f(s)), lambda q: v(g(q))) is None
    prior = {key: F(i+1, 136)
             for i, key in enumerate(product(pairs, pairs))}
    coarse = push(prior, f, g)
    terminal = push(coarse, u, v)
    assert terminal == push(prior, lambda s: u(f(s)), lambda q: v(g(q)))
    for word in words:
        laws = [prior, coarse, terminal]
        masses = [F(1)] * 3
        for i, (action, outcome) in enumerate(word):
            for j, (states, kernel) in enumerate(
                    ((pairs, fine), (binary, base), (binary, final))):
                laws[j], z = step(laws[j], word[:i], action, outcome, states, kernel)
                masses[j] *= z
            assert push(laws[0], f, g) == laws[1]
            assert push(laws[1], u, v) == laws[2]
        independently_enumerated, likelihood = path_oracle(prior, word, pairs, fine)
        assert independently_enumerated == laws[0]
        assert likelihood == masses[0] == masses[1] == masses[2]

    # A tiny positive-support mutation changes weights while preserving row mass.
    def mutant(h, a, s, q, o, r):
        weight = fine(h, a, s, q, o, r)
        if (h, a, s, q, r) == ((), 0, (0, 0), (0, 0), (0, 0)):
            weight += F(1, 48) if o == 1 else -F(1, 48)
        return weight
    check_rows(pairs, pairs, histories, mutant)
    mismatch = square(pairs, pairs, binary, histories, mutant, base, f, g)
    assert mismatch is not None
    assert all((fine(h, a, s, q, o, r) > 0) == (mutant(h, a, s, q, o, r) > 0)
               for h, a, s, q, o, r in product(
                   histories, binary, pairs, pairs, binary, pairs))

    # Minimal nontrivial coordinates: original, carrier, and public output binary.
    # Same full support and uniform marginals; read q and overwrite it with zero.
    plus = {(s, q): F(3 if s == q else 1, 8) for s, q in product(binary, repeat=2)}
    minus = {(s, q): F(1 if s == q else 3, 8) for s, q in product(binary, repeat=2)}
    erase = lambda h, a, s, q, o, r: F(int(o == q and r == 0))
    forgotten = lambda q: 0
    assert set(plus) == set(minus)
    assert push(plus, lambda s: s, forgotten) == push(minus, lambda s: s, forgotten)
    for law in (plus, minus):
        assert all(sum(law[(s, q)] for s in binary) == F(1, 2) for q in binary)
        assert all(sum(law[(s, q)] for q in binary) == F(1, 2) for s in binary)
    ppost, pz = step(plus, (), 0, 0, binary, erase)
    mpost, mz = step(minus, (), 0, 0, binary, erase)
    assert pz == mz == F(1, 2)
    assert set(ppost) == set(mpost) == {(0, 0), (1, 0)}
    assert ppost[(0, 0)] == F(3, 4) and mpost[(0, 0)] == F(1, 4)

    policy_prior = {0: F(1, 2), 1: F(1, 2)}
    action0 = {s: policy_prior[s] * F(int(s == 0)) for s in binary}
    action_mass = sum(action0.values(), F(0))
    policy_posterior = action0[0] / action_mass
    assert policy_posterior == 1 and policy_prior[0] == F(1, 2)

    rejected = []
    try:
        exact(0.5)
    except ValueError:
        rejected.append("floating_weight")
    try:
        constant_zero = lambda h, a, s, q, o, r: F(int(o == 0))
        impossible_mass = F(1) * constant_zero((), 0, 0, 0, 1, 0)
        assert impossible_mass == 0
        step({(0, 0): F(1)}, (), 0, 1, (0,), constant_zero)
    except ValueError:
        rejected.append("zero_probability_history")
    assert len(rejected) == 2
    result = {
        "claim_id": "SWM-C17", "parent_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "proof_status": "PROVED LOCAL: dossier algebra; probe is TESTED MODEL",
        "runtime_imports": [], "exact_arithmetic": "fractions.Fraction",
        "bounded_domain": {"fine_source_states": 4, "fine_carrier_states": 4,
                           "actions": 2, "outcomes": 2, "maximum_history_length": 3},
        "normalized_kernel_rows_checked": row_counts,
        "positive_model_history_words_checked": len(words),
        "law_squares": ["fine_to_coarse", "coarse_to_final", "composite"],
        "independent_complete_hidden_path_oracle": "PASS",
        "filter_transport_and_predictive_mass": "PASS",
        "support_preserving_kernel_mutation": {"rejected": True, "witness": mismatch},
        "equal_support_correlated_read_erase": {
            "prior_diagonal_weights": ["3/8", "1/8"],
            "same_prior_marginals": True, "same_joint_coarse_prior": True,
            "same_original_source_posterior_support": True,
            "same_current_endpoint": 0, "same_report_probability": str(pz),
            "original_s0_posteriors_after_report0": [str(ppost[(0, 0)]), str(mpost[(0, 0)])],
            "universal_coarse_kernel_from_forgotten_prior": "REFUTED"},
        "hidden_policy_negative_control": {
            "S0_prior": "1/2", "P_action0_given_S0": "1",
            "P_action0_given_S1": "0", "correct_S0_after_action0": str(policy_posterior),
            "incorrect_ignoring_action_likelihood": str(policy_prior[0])},
        "guard_rejections": rejected,
        "positive_cone_restriction": {
            "formal_edge": "report1 under constant-report0 instrument",
            "pushforward_unnormalized_mass": str(impossible_mass),
            "positive_fiber_has_lift_over_fixed_formal_base": bool(impossible_mass),
            "blanket_actual_history_opfibration": "REFUTED",
        },
        "physical_source_authenticated": False, "scholarly_novelty_claimed": False,
        "formal_kernel_verified": False,
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
