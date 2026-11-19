"""Exact response-table realization for the Causal Generator dossier.

Row convention: word (a, b) updates x to x M_a M_b. A returned finite
candidate does not certify the global rank promise. Integers/Fractions only.
No statistical, quantum, or BBP-normality conclusion is implemented.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from typing import Mapping
import json

Word = tuple[str, ...]
Matrix = tuple[tuple[F, ...], ...]


def exact(value):
    if type(value) is not int and not isinstance(value, F):
        raise TypeError("Exact integers and Fractions required")
    return F(value)


def matrix(rows) -> Matrix:
    a = tuple(tuple(exact(x) for x in row) for row in rows)
    if not a or not a[0] or any(len(row) != len(a[0]) for row in a):
        raise ValueError("Nonempty rectangular matrix required")
    return a


def identity(n):
    if type(n) is not int or n < 1:
        raise ValueError("Positive exact dimension required")
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def multiply(a, b):
    a, b = matrix(a), matrix(b)
    if len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions")
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def inverse(a):
    a = matrix(a)
    n = len(a)
    if len(a[0]) != n:
        raise ValueError("Square matrix required")
    aug = [list(a[i]) + list(identity(n)[i]) for i in range(n)]
    for k in range(n):
        p = next((i for i in range(k, n) if aug[i][k]), None)
        if p is None:
            raise ValueError("Singular observed Hankel block")
        aug[k], aug[p] = aug[p], aug[k]
        scale = aug[k][k]
        aug[k] = [x / scale for x in aug[k]]
        for i in range(n):
            if i != k:
                scale = aug[i][k]
                aug[i] = [x - scale*y for x, y in zip(aug[i], aug[k])]
    return tuple(tuple(row[n:]) for row in aug)


def word(value) -> Word:
    result = tuple(value)
    if any(type(a) is not str or not a for a in result):
        raise ValueError("Word letters must be nonempty strings")
    return result


@dataclass(frozen=True)
class Realization:
    alpha: tuple[F, ...]
    transitions: Mapping[str, Matrix]
    beta: tuple[F, ...]

    def __post_init__(self):
        alpha = tuple(exact(x) for x in self.alpha)
        beta = tuple(exact(x) for x in self.beta)
        n = len(alpha)
        if not n or len(beta) != n or not self.transitions:
            raise ValueError("Positive compatible state dimension and alphabet required")
        transitions = {}
        for a, value in self.transitions.items():
            if type(a) is not str or not a:
                raise ValueError("Nonempty string generator labels required")
            t = matrix(value)
            if (len(t), len(t[0])) != (n, n):
                raise ValueError("Generator has incompatible shape")
            transitions[a] = t
        object.__setattr__(self, "alpha", alpha)
        object.__setattr__(self, "beta", beta)
        object.__setattr__(self, "transitions", transitions)

    @property
    def dimension(self):
        return len(self.alpha)

    def response(self, w):
        state = (self.alpha,)
        for a in word(w):
            state = multiply(state, self.transitions[a])
        return sum((x*y for x, y in zip(state[0], self.beta)), F(0))

    def changed_basis(self, s):
        s = matrix(s)
        if (len(s), len(s[0])) != (self.dimension, self.dimension):
            raise ValueError("Basis change has incompatible shape")
        si = inverse(s)
        alpha = multiply((self.alpha,), s)[0]
        beta = tuple(row[0] for row in multiply(si, tuple((x,) for x in self.beta)))
        transitions = {a: multiply(multiply(si, m), s)
                       for a, m in self.transitions.items()}
        return Realization(alpha, transitions, beta)


def probe_bank(prefixes, suffixes, alphabet):
    p = tuple(word(w) for w in prefixes)
    q = tuple(word(w) for w in suffixes)
    letters = tuple(alphabet)
    if not p or len(p) != len(q) or len(set(p)) != len(p) or len(set(q)) != len(q):
        raise ValueError("Distinct equal-sized nonempty prefix and suffix bases required")
    if not letters or len(set(letters)) != len(letters):
        raise ValueError("Distinct nonempty alphabet required")
    word(letters)
    if any(a not in letters for w in p+q for a in w):
        raise ValueError("Basis contains an undeclared generator")
    bank = set(p) | set(q)
    bank.update(u+v for u in p for v in q)
    bank.update(u+(a,)+v for u in p for a in letters for v in q)
    return tuple(sorted(bank, key=lambda w: (len(w), w)))


@dataclass(frozen=True)
class ReconstructedCandidate:
    model: Realization
    hankel: Matrix
    observed_rank: int
    assumed_global_rank_at_most: int | None
    sampled_words: tuple[Word, ...]

    @property
    def claim(self):
        if self.assumed_global_rank_at_most is None:
            return "FINITE_DATA_CANDIDATE_ONLY"
        return "ALL_WORDS_CONDITIONAL_ON_EXTERNAL_GLOBAL_RANK_PROMISE"


def reconstruct_from_table(readings, prefixes, suffixes, alphabet,
                           *, assumed_global_rank_at_most=None):
    """Reconstruct the canonical row model; never verify a global rank promise.

    All required words must be available. Finite recorded inconsistencies fail.
    The promise, when supplied, must equal the witnessed invertible-block rank.
    """
    p = tuple(word(w) for w in prefixes)
    q = tuple(word(w) for w in suffixes)
    letters = tuple(alphabet)
    bank = probe_bank(p, q, letters)
    table = {word(w): exact(y) for w, y in readings.items()}
    missing = set(bank) - set(table)
    if missing:
        raise ValueError("Required forward response words are unavailable")
    d = len(p)
    if assumed_global_rank_at_most is not None:
        if type(assumed_global_rank_at_most) is not int or assumed_global_rank_at_most != d:
            raise ValueError("The external upper promise must equal the witnessed rank")
    h = matrix([[table[u+v] for v in q] for u in p])
    hi = inverse(h)
    alpha = multiply((tuple(table[v] for v in q),), hi)[0]
    beta = tuple(table[u] for u in p)
    transitions = {
        a: multiply(matrix([[table[u+(a,)+v] for v in q] for u in p]), hi)
        for a in letters
    }
    model = Realization(alpha, transitions, beta)
    if any(model.response(w) != y for w, y in table.items()):
        raise ValueError("Finite records contradict the reconstructed word law")
    return ReconstructedCandidate(model, h, d, assumed_global_rank_at_most,
                                  tuple(sorted(table, key=lambda w: (len(w), w))))


def enumerate_path_response(model, w):
    """Independent finite index-path expansion, for calibrated small examples."""
    w = word(w)
    total = F(0)
    for states in product(range(model.dimension), repeat=len(w)+1):
        weight = model.alpha[states[0]] * model.beta[states[-1]]
        for t, a in enumerate(w):
            weight *= model.transitions[a][states[t]][states[t+1]]
        total += weight
    return total


def missing_from_one_history(bank, history):
    """Words absent from one irreversible transcript with prefix readout only.

    This access model includes no reset, replay, branching preparation, or
    authenticated source-computation oracle. Those would be extra resources.
    """
    history = word(history)
    prefixes = {history[:n] for n in range(len(history)+1)}
    return tuple(sorted({word(w) for w in bank} - prefixes,
                        key=lambda w: (len(w), w)))


def verify_linear_function_closure(source_transitions, features,
                                   reduced_transitions, target, output):
    """Check global function identities for a declared rational row carrier.

    State x evolves x L_a. Features are x C. The checks L_a C=C M_a and
    target=C output are identities on every x, not sampled state comparisons.
    """
    c = matrix(features)
    n, d = len(c), len(c[0])
    if not source_transitions or set(source_transitions) != set(reduced_transitions):
        return False
    target = matrix(tuple((exact(x),) for x in target))
    output = matrix(tuple((exact(x),) for x in output))
    if (len(target), len(output)) != (n, d) or multiply(c, output) != target:
        return False
    for a in source_transitions:
        l, m = matrix(source_transitions[a]), matrix(reduced_transitions[a])
        if (len(l), len(l[0]), len(m), len(m[0])) != (n, n, d, d):
            return False
        if multiply(l, c) != multiply(c, m):
            return False
    return True


def affine_row_lift(linear, offset):
    """(x,1) -> (x L+b,1), retaining the affine anchor in a constant feature."""
    linear = matrix(linear)
    n = len(linear)
    offset = tuple(exact(x) for x in offset)
    if len(linear[0]) != n or len(offset) != n:
        raise ValueError("Compatible square linear part and offset required")
    return tuple(row+(F(0),) for row in linear)+(offset+(F(1),),)


def fibonacci_model():
    return Realization((1, 0), {"a": ((1, 1), (1, 0))}, (1, 0))


def delayed_spike_model(delay):
    if type(delay) is not int or delay < 0:
        raise ValueError("Nonnegative exact delay required")
    n = delay+1
    a = tuple(tuple(int(j == i+1) for j in range(n)) for i in range(n))
    return Realization(tuple(int(i == 0) for i in range(n)), {"a": a},
                       tuple(int(i == delay) for i in range(n)))


def add_models(left, right):
    if set(left.transitions) != set(right.transitions):
        raise ValueError("Common alphabet required")
    n, m = left.dimension, right.dimension
    transitions = {}
    for a in left.transitions:
        l, r = left.transitions[a], right.transitions[a]
        transitions[a] = tuple(
            tuple(l[i][j] if i < n and j < n else
                  r[i-n][j-n] if i >= n and j >= n else F(0)
                  for j in range(n+m)) for i in range(n+m))
    return Realization(left.alpha+right.alpha, transitions, left.beta+right.beta)


def receipt():
    fib = fibonacci_model()
    p = q = ((), ("a",))
    bank = probe_bank(p, q, ("a",))
    candidate = reconstruct_from_table({w: fib.response(w) for w in bank}, p, q,
                                       ("a",), assumed_global_rank_at_most=2)
    delayed = add_models(fib, delayed_spike_model(12))
    diag = Realization((1, 1), {"a": ((1, 0), (0, 2))}, (1, 1))
    tri = diag.changed_basis(((1, -1), (0, 1)))
    return {
        "schema": "causal-generator-realization-v1",
        "arithmetic": "exact Fraction",
        "fibonacci_training_lengths": [len(w) for w in bank],
        "fibonacci_recovered_transition": [[str(x) for x in row]
                                              for row in candidate.model.transitions["a"]],
        "fibonacci_holdout_10_to_29": all(candidate.model.response(("a",)*n) ==
                                           fib.response(("a",)*n) for n in range(10, 30)),
        "candidate_claim": candidate.claim,
        "global_rank_promise_verified_by_table": False,
        "delayed_hidden_model_agrees_through_11": all(fib.response(("a",)*n) ==
                                                      delayed.response(("a",)*n)
                                                      for n in range(12)),
        "delayed_hidden_difference_at_12": str(delayed.response(("a",)*12)-fib.response(("a",)*12)),
        "same_behavior_different_support_through_19": all(diag.response(("a",)*n) ==
                                                           tri.response(("a",)*n)
                                                           for n in range(20)),
        "scope": "Finite implementation observations; all-word claims require the paper hypotheses."
    }


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2, sort_keys=True))
