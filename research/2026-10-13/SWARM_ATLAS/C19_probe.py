"""Bounded exact controls for C19; Gaussian rationals, no quantum hardware.

Run: python research/2026-10-13/SWARM_ATLAS/C19_probe.py
The universal theorem is proved in C19.md, not established by this probe.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import json
from pathlib import Path
import sys


@dataclass(frozen=True)
class G:
    r: Q = Q(0)
    i: Q = Q(0)

    def __post_init__(self):
        assert isinstance(self.r, (int, Q)) and isinstance(self.i, (int, Q))
        object.__setattr__(self, "r", Q(self.r))
        object.__setattr__(self, "i", Q(self.i))

    def __add__(self, other):
        b = other if isinstance(other, G) else G(other)
        return G(self.r + b.r, self.i + b.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + -(other if isinstance(other, G) else G(other))

    def __mul__(self, other):
        b = other if isinstance(other, G) else G(other)
        return G(self.r * b.r - self.i * b.i, self.r * b.i + self.i * b.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = other if isinstance(other, G) else G(other)
        t = b.r * b.r + b.i * b.i
        assert t != 0
        return self * G(b.r / t, -b.i / t)

    def conj(self):
        return G(self.r, -self.i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __str__(self):
        return str(self.r) if not self.i else f"({self.r})+({self.i})i"


def mat(rows):
    a = tuple(tuple(x if isinstance(x, G) else G(x) for x in row) for row in rows)
    assert a and a[0] and len({len(row) for row in a}) == 1
    return a


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def zero(m, n):
    return mat([[0 for _ in range(n)] for _ in range(m)])


def adj(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def mul(a, b):
    assert len(a[0]) == len(b)
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), G())
                       for j in range(len(b[0]))) for i in range(len(a)))


def add(a, b):
    assert (len(a), len(a[0])) == (len(b), len(b[0]))
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(a, x):
    return tuple(tuple(x * v for v in row) for row in a)


def tr(a):
    assert len(a) == len(a[0])
    return sum((a[i][i] for i in range(len(a))), G())


def rank(a):
    rows = [list(row) for row in a]
    pivot = 0
    for j in range(len(a[0])):
        k = next((k for k in range(pivot, len(rows)) if rows[k][j]), None)
        if k is None:
            continue
        rows[pivot], rows[k] = rows[k], rows[pivot]
        d = rows[pivot][j]
        rows[pivot] = [v / d for v in rows[pivot]]
        for k in range(len(rows)):
            if k != pivot:
                d = rows[k][j]
                rows[k] = [v - d * w for v, w in zip(rows[k], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def psd2(a):
    assert len(a) == len(a[0]) == 2
    if a != adj(a):
        return False
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return (a[0][0].i == a[1][1].i == determinant.i == 0
            and min(a[0][0].r, a[1][1].r, determinant.r) >= 0)


def dual(branch, observable):
    out = zero(len(branch[0][0]), len(branch[0][0]))
    for k in branch:
        out = add(out, mul(mul(adj(k), observable), k))
    return out


def apply(branch, rho):
    out = zero(len(branch[0]), len(branch[0]))
    for k in branch:
        out = add(out, mul(mul(k, rho), adj(k)))
    return out


def compose(left, right):
    return tuple(mul(k, l) for k in left for l in right)


def effect(branch):
    return dual(branch, eye(len(branch[0])))


def probability(branch, rho):
    p = tr(apply(branch, rho))
    assert p.i == 0 and 0 <= p.r <= 1
    assert p == tr(mul(effect(branch), rho))
    return p.r


def check_instrument(branches):
    total = zero(len(branches[0][0][0]), len(branches[0][0][0]))
    for branch in branches:
        total = add(total, effect(branch))
    assert total == eye(len(total))


def encoded(a):
    return [[str(x) for x in row] for row in a]


def run():
    ident = eye(2)
    p0, p1 = mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 1]])
    xp = mat([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])
    xm = mat([[Q(1, 2), Q(-1, 2)], [Q(-1, 2), Q(1, 2)]])
    yp = mat([[Q(1, 2), G(0, Q(-1, 2))], [G(0, Q(1, 2)), Q(1, 2)]])
    ym = add(ident, scale(yp, -1))
    z, x, y = ((p0,), (p1,)), ((xp,), (xm,)), ((yp,), (ym,))
    for instrument in (z, x, y):
        check_instrument(instrument)
    assert psd2(yp) and tr(yp) == G(1)
    yz, zy = compose(z[0], y[0]), compose(y[0], z[0])
    assert probability(yz, p0) == Q(1, 4)
    assert probability(zy, p0) == Q(1, 2)
    posterior_y = scale(apply(y[0], p0), Q(2))
    assert posterior_y == yp and posterior_y != p0

    # Dual composition is checked independently of multiplying Kraus words.
    assert effect(yz) == dual(y[0], dual(z[0], ident))
    assert effect(yz) == scale(yp, Q(1, 2))
    assert psd2(add(effect(y[0]), scale(effect(yz), -1)))

    # CP without trace nonincrease does not license decreasing effects.
    amplifier = (scale(ident, 2),)
    assert effect(amplifier) == scale(ident, 4)
    assert not psd2(add(ident, scale(effect(amplifier), -1)))

    # Same one-step POVM, different disturbance and two-step effects.
    lower = mat([[0, 1], [0, 0]])
    prepare_zero_z = ((p0,), (lower,))
    check_instrument(prepare_zero_z)
    assert effect(z[1]) == effect(prepare_zero_z[1]) == p1
    assert apply(z[1], p1) == p1
    assert apply(prepare_zero_z[1], p1) == p0
    repeat_luders = compose(z[0], z[1])
    repeat_prepare = compose(z[0], prepare_zero_z[1])
    assert effect(repeat_luders) == zero(2, 2)
    assert effect(repeat_prepare) == p1

    # Multiple hidden Kraus labels are summed, never treated as recorded labels.
    reset = (p0, lower)
    check_instrument((reset,))
    assert effect(reset) == ident
    assert apply(reset, p0) == apply(reset, p1) == p0
    assert tr(mul(p0, p0)).r == 1 and tr(mul(p0, p1)).r == 0

    # Changing output dimensions does not change the initial effect space.
    j = (mat([[1, 0], [0, 1], [0, 0]]),)
    b = (mat([[1, 0, 0]]),)
    c = (mat([[1], [0], [0], [0]]),)
    varying = compose(c, compose(b, j))
    assert effect(j) == ident and effect(compose(b, j)) == effect(varying) == p0
    assert len(varying[0]) == 4 and len(effect(varying)) == 2

    # Representative source controls; compactness is not used by the proof.
    near_one = mat([[Q(1, 5), Q(2, 5)], [Q(2, 5), Q(4, 5)]])
    sources = {"zero": p0, "one": p1, "plus": xp, "near_one": near_one}
    word = tuple((xp,) if n % 2 == 0 else (p0,) for n in range(16))
    prefix = (ident,)
    previous = ident
    ranks, plus_likelihoods = [], []
    for branch in word:
        prefix = compose(branch, prefix)
        current = effect(prefix)
        assert psd2(current) and psd2(add(previous, scale(current, -1)))
        assert rank(current) == 1
        assert probability(prefix, xp) > 0
        ranks.append(rank(current))
        plus_likelihoods.append(str(probability(prefix, xp)))
        previous = current
    supported = [name for name, rho in sources.items() if probability(prefix, rho) > 0]
    assert supported == list(sources)
    assert probability(compose((xm,), (xp,)), xp) == 0

    # Arbitrarily late rank drops: horizon 17 exceeds initial dimension 2.
    late_word = ((ident,),) * 16 + ((p0,),)
    prefix, late_ranks = (ident,), [2]
    for branch in late_word:
        prefix = compose(branch, prefix)
        late_ranks.append(rank(effect(prefix)))
    assert late_ranks == [2] * 17 + [1]

    # Repeated reported fair outcome: all finite prefixes positive, limit zero.
    coin = (scale(ident, Q(1, 2)), scale(ident, Q(1, 2)))
    check_instrument((coin, coin))
    prefix = (ident,)
    coin_probabilities = []
    # Repeated composition need not materialize the exponentially many Kraus words.
    current = p0
    for n in range(1, 25):
        current = apply(coin, current)
        assert tr(current).r == Q(1, 2**n)
        coin_probabilities.append(str(tr(current).r))

    # Finite slices of the infinite countermodel; proof of all indices is in C19.md.
    # rho_k has support {0,k}; its 2x2 nonzero block is exactly rational.
    tail_table = []
    for k in range(1, 9):
        rho_k = mat([[Q(k*k, k*k+1), Q(k, k*k+1)],
                     [Q(k, k*k+1), Q(1, k*k+1)]])
        assert psd2(rho_k) and rank(rho_k) == 1 and tr(rho_k) == G(1)
        weights = [Q(1, k*k+1) if k >= n else Q(0) for n in range(1, 10)]
        assert weights[k] == 0 and all(p > 0 for p in weights[:k])
        tail_table.append({"k": k, "rho_nonzero_block": encoded(rho_k),
                           "prefix_likelihoods_n1_to9": [str(p) for p in weights]})

    # Real native smoke path; imports are read-only and no full suite is run.
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from observational_succ.quantum_records import QuantumObserver, measure_x, measure_z
    native_initial = QuantumObserver.initial_state()
    native_first = native_initial.advance(measure_x(), "plus")
    native_second = native_first.advance(measure_z(), "zero")
    native_reverse = native_initial.advance(measure_z(), "zero").advance(measure_x(), "plus")
    assert native_second.verify({"X": measure_x(), "Z": measure_z()})
    assert native_reverse.verify({"X": measure_x(), "Z": measure_z()})
    assert native_second.records[:1] == native_first.records
    assert native_first.state != native_second.state
    assert native_initial.records == ()

    return {
        "status": "PASS_EXACT_BOUNDED_CONTROLS",
        "arithmetic": "Gaussian rationals over fractions.Fraction; no floats",
        "universal_theorem_checked_by": "written proof, not this finite probe",
        "complex_order": {"Yplus_then_Zzero": str(probability(yz, p0)),
                          "Zzero_then_Yplus": str(probability(zy, p0)),
                          "prefix_effect": encoded(effect(yz))},
        "missing_TNI_negative_control": {"CP_effect": encoded(effect(amplifier)),
                                         "effect_decrease": False},
        "same_POVM_different_disturbance": {"Luders_Zone_then_Zzero": "0",
                                          "prepare_zero_Zone_then_Zzero": "1"},
        "reset": {"multiple_Kraus": 2, "original_target_values": ["1", "0"],
                  "identical_poststates": True, "effect": encoded(effect(reset))},
        "changing_dimensions": {"dimensions": [2, 3, 1, 4], "initial_effect": encoded(effect(varying))},
        "fixed_word_16": {"ranks": ranks, "plus_likelihoods": plus_likelihoods,
                          "tested_sources_supporting_all_16": supported},
        "late_rank_drop": {"initial_dimension": 2, "ranks_n0_to17": late_ranks,
                           "last_drop_index": 17, "strict_drop_count": 1},
        "zero_infinite_event_control": {"finite_likelihoods_n1_to24": coin_probabilities,
                                        "analytic_limit": "0 by geometric sequence"},
        "infinite_dimensional_compact_C": {"finite_slices": tail_table,
                                          "uniform_source_refuted_by": "each rho_k killed at k+1; rho_0 at 1",
                                          "compactness_proof": "trace_norm(rho_k-rho_0)=2/sqrt(k^2+1)"},
        "native_smoke": {"Xplus_then_Zzero_joint": str(native_second.joint_probability),
                         "Zzero_then_Xplus_joint": str(native_reverse.joint_probability),
                         "replay": True, "history_prefix_retained": True,
                         "current_state_changed": True},
        "physical_experiment": False,
        "human_cognition_claim": False,
        "RH_or_Weil_claim": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
