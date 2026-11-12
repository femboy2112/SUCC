"""Exact controls for calibrated current twin outputs and deferred readout.

Only the Python standard library is used. Gaussian rationals make transpose,
conjugation, phase and density-matrix checks exact. The unnormalized diagonal
twin is used internally; its squared norms are divided by the dimension.
This is a mathematical probe, not a quantum-device measurement or simulator
of physical collapse. It does not compare untransported observer histories.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path
import random


@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    def __add__(self, other):
        other = scalar(other)
        return Q(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-scalar(other))

    def __mul__(self, other):
        other = scalar(other)
        return Q(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = F(other)
        return Q(self.re / other, self.im / other)

    def conj(self):
        return Q(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im


def scalar(value):
    return value if isinstance(value, Q) else Q(value)


Z, ONE, IM = Q(), Q(1), Q(0, 1)


def matrix(rows):
    return tuple(tuple(scalar(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def transpose(a):
    return tuple(zip(*a))


def conjugate(a):
    return tuple(tuple(x.conj() for x in row) for row in a)


def adjoint(a):
    return transpose(conjugate(a))


def multiply(a, b):
    assert len(a[0]) == len(b)
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), Z)
                       for col in transpose(b)) for row in a)


def tensor(a, b):
    return tuple(tuple(x * y for x in row_a for y in row_b)
                 for row_a in a for row_b in b)


def scaled(a, c):
    return tuple(tuple(x * c for x in row) for row in a)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ra, rb))
                 for ra, rb in zip(a, b))


def apply(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), Z) for row in a)


def inner(u, v):
    return sum((x.conj() * y for x, y in zip(u, v)), Z)


def norm2(v):
    return sum(x.abs2() for x in v)


def difference(u, v):
    return tuple(x - y for x, y in zip(u, v))


def twin(d, amplitudes=None):
    amplitudes = tuple(ONE for _ in range(d)) if amplitudes is None else amplitudes
    return tuple(amplitudes[i] if i == j else Z
                 for i in range(d) for j in range(d))


def density(v):
    n = norm2(v)
    assert n > 0
    return tuple(tuple(x * y.conj() / n for y in v) for x in v)


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Z)


def reduced_first(rho, first, second):
    return tuple(tuple(sum((rho[i * second + k][j * second + k]
                            for k in range(second)), Z)
                       for j in range(first)) for i in range(first))


def channel(a, rho):
    return multiply(multiply(a, rho), adjoint(a))


def diag(values):
    return matrix([[values[i] if i == j else 0 for j in range(len(values))]
                   for i in range(len(values))])


def random_matrix(rng, d):
    return matrix([[Q(F(rng.randrange(-5, 6), rng.randrange(1, 8)),
                      F(rng.randrange(-4, 5), rng.randrange(1, 8)))
                    for _ in range(d)] for _ in range(d)])


def run():
    counts = Counter()

    def check(group, condition):
        counts[group] += 1
        if not condition:
            raise AssertionError(f"{group}: check {counts[group]} failed")

    check("arithmetic_calibration", IM * IM == Q(-1))
    check("arithmetic_calibration", Q(F(3, 5), F(4, 5)).abs2() == 1)
    check("arithmetic_calibration", Q(2, 3).conj() == Q(2, -3))
    check("arithmetic_calibration", inner((IM,), (IM,)) == ONE)
    rng = random.Random(2026111207)

    # The tensor implementation is compared with direct column differences.
    # Holdout dimensions 7 and 9 are outside the main small-matrix range.
    for d, cases in [(1, 8), (2, 16), (3, 12), (4, 8), (5, 5), (7, 2), (9, 2)]:
        ident, omega = eye(d), twin(d)
        for _ in range(cases):
            a, b = random_matrix(rng, d), random_matrix(rng, d)
            left = apply(tensor(a, ident), omega)
            right_a = apply(tensor(ident, transpose(a)), omega)
            right_b = apply(tensor(ident, transpose(b)), omega)
            check("vectorization", left == right_a)
            direct = sum((a[i][j] - b[i][j]).abs2()
                         for i in range(d) for j in range(d)) / d
            check("vectorization", norm2(difference(left, right_b)) / d == direct)
            check("vectorization", norm2(difference(left, right_b)) > 0)

    phases = (ONE, -ONE, IM, -IM, Q(F(3, 5), F(4, 5)))
    rotations = ((F(1), F(0)), (F(3, 5), F(4, 5)),
                 (F(5, 13), F(12, 13)), (F(7, 25), F(24, 25)))
    omega2 = twin(2)
    for c, s in rotations:
        rotation = matrix([[c, -s], [s, c]])
        for p in phases:
            u = multiply(rotation, diag((ONE, p)))
            check("conjugate_transport", multiply(adjoint(u), u) == eye(2))
            check("conjugate_transport",
                  apply(tensor(u, conjugate(u)), omega2) == omega2)
    phase_gate = diag((ONE, IM))
    both_same = apply(tensor(phase_gate, phase_gate), omega2)
    check("phase_mutation", both_same == (ONE, Z, Z, -ONE))
    check("phase_mutation", inner(omega2, both_same) == Z)
    # Transpose is not adjoint, and same-coordinate matrices are not frames.
    check("phase_mutation",
          apply(tensor(phase_gate, eye(2)), omega2) !=
          apply(tensor(eye(2), adjoint(phase_gate)), omega2))
    check("phase_mutation", density(omega2) == density(tuple(-x for x in omega2)))
    check("phase_mutation", norm2(difference(omega2, tuple(-x for x in omega2))) / 2 == 4)

    # Bell Z/Z has correlated outcomes; Bell Z/X has four equally likely ones.
    rho_bell = density(omega2)
    z_projectors = (diag((1, 0)), diag((0, 1)))
    x_projectors = (scaled(matrix([[1, 1], [1, 1]]), F(1, 2)),
                    scaled(matrix([[1, -1], [-1, 1]]), F(1, 2)))
    zz, zx = [], []
    for i in range(2):
        for j in range(2):
            pzz = trace(multiply(tensor(z_projectors[i], z_projectors[j]), rho_bell))
            pzx = trace(multiply(tensor(z_projectors[i], x_projectors[j]), rho_bell))
            check("basis_outcomes", pzz == Q(F(1, 2) if i == j else 0))
            check("basis_outcomes", pzx == Q(F(1, 4)))
            zz.append(str(pzz.re))
            zx.append(str(pzx.re))

    # Global coherence can be retained while the declared local current
    # output changes. Undoing the SAME joint unitary restores that output.
    cnot = matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                   [0, 0, 0, 1], [0, 0, 1, 0]])
    input_state = (Q(F(3, 5)), Z, Q(F(4, 5)), Z)
    entangled = apply(cnot, input_state)
    initial_local = reduced_first(density(input_state), 2, 2)
    recorded_local = reduced_first(density(entangled), 2, 2)
    check("environment_record", multiply(adjoint(cnot), cnot) == eye(4))
    check("environment_record", initial_local[0][1] == Q(F(12, 25)))
    check("environment_record", recorded_local == diag((F(9, 25), F(16, 25))))
    check("environment_record", apply(cnot, entangled) == input_state)
    check("environment_record", multiply(density(entangled), density(entangled)) == density(entangled))
    check("environment_record", multiply(recorded_local, recorded_local) != recorded_local)
    for c, s in rotations:
        # Environment overlap c multiplies the current local off-diagonal.
        v = (Q(F(3, 5)), Z, Q(F(4, 5) * c), Q(F(4, 5) * s))
        reduced = reduced_first(density(v), 2, 2)
        check("environment_overlap", reduced[0][1] == Q(F(12, 25) * c))
        check("environment_overlap", trace(reduced) == ONE)

    # Deferred measurement: retain the coherent record and use the same
    # projectors/controlled gates. Final reported record densities agree.
    proj = tuple(tensor(p, eye(2)) for p in z_projectors)
    for c, s in rotations:
        controlled = matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                             [0, 0, c, -s], [0, 0, s, c]])
        for _ in range(12):
            v = tuple(Q(rng.randrange(-3, 4), rng.randrange(-3, 4)) for _ in range(4))
            if norm2(v) == 0:
                v = (ONE, Z, Z, Z)
            rho = density(v)
            measured_first = channel(controlled, add(channel(proj[0], rho), channel(proj[1], rho)))
            advanced = channel(controlled, rho)
            measured_last = add(channel(proj[0], advanced), channel(proj[1], advanced))
            check("deferred_readout", measured_first == measured_last)
            check("deferred_readout", trace(measured_last) == ONE)

    # The symmetric-projector measurement can accept unequal pure states.
    u, v = (ONE, Z), (Q(F(3, 5)), Q(F(4, 5)))
    uv = tuple(x * y for x in u for y in v)
    swap = matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                   [0, 1, 0, 0], [0, 0, 0, 1]])
    symmetric = scaled(add(eye(4), swap), F(1, 2))
    accept = inner(uv, apply(symmetric, uv))
    check("physical_comparison", accept == Q(F(17, 25)))
    check("physical_comparison", accept == Q((1 + inner(u, v).abs2()) / 2))
    check("physical_comparison", F(0) < accept.re < 1)

    finite_blindspots = []
    for d in (2, 3, 5, 8, 13):
        full = d + 1
        amplitudes = tuple(ONE if i < d else Z for i in range(full))
        finite_twin = twin(full, amplitudes)
        flipped = diag(tuple(ONE if i < d else -ONE for i in range(full)))
        check("finite_support", apply(tensor(flipped, eye(full)), finite_twin) == finite_twin)
        check("finite_support", flipped[d][d] != ONE)
        finite_blindspots.append({"observed_dimension": d, "missed_index": d})

    weighted_rows = []
    for d in (2, 3, 5, 7, 9):
        amplitudes = tuple(Q(F(1, 2 ** (j * j))) for j in range(d))
        omega = twin(d, amplitudes)
        total = norm2(omega)
        for n in range(d):
            a = eye(d)
            b = diag(tuple(ONE if j != n else -ONE for j in range(d)))
            delta = difference(apply(tensor(a, eye(d)), omega),
                               apply(tensor(b, eye(d)), omega))
            expected = 4 * amplitudes[n].abs2() / total
            check("weighted_diagnostic", norm2(delta) / total == expected)
            check("weighted_diagnostic", expected > 0)
        # Weighted transpose partner for a finite successor. Its interior
        # coefficients grow as 2^(2j−1), independently of normalization.
        successor = matrix([[int(i == j + 1) for j in range(d)] for i in range(d)])
        mirror = matrix([[Q(F(2 ** (2 * j - 1))) if j == i + 1 else Z
                          for j in range(d)] for i in range(d)])
        check("weighted_mirror", apply(tensor(successor, eye(d)), omega) ==
              apply(tensor(eye(d), mirror), omega))
        weighted_rows.append({"dimension": d, "last_mirror_weight": str(2 ** (2 * d - 3))})

    return {
        "schema": "succ.twin-correlation.v1",
        "status": "PASS",
        "arithmetic": "exact Gaussian rationals; no floating point",
        "checks": sum(counts.values()),
        "checks_by_group": dict(sorted(counts.items())),
        "failures": [],
        "current_output_contract": "Only the declared present diagnostic in an explicitly calibrated common basis is compared; raw histories are not compared.",
        "witnesses": {
            "same_phase_twins": "diag(1,i) tensor diag(1,i) sends Phi+ to the orthogonal Phi-",
            "bell_ZZ_probabilities": zz,
            "bell_ZX_probabilities": zx,
            "local_off_diagonal_before_record": "12/25",
            "local_off_diagonal_after_record": "0",
            "unitary_undo_restores_input": True,
            "swap_accepts_distinct_states_probability": str(accept.re),
            "finite_support_blindspots": finite_blindspots,
            "weighted_mirror_growth": weighted_rows,
        },
        "boundaries": [
            "Finite exact controls accompany proofs; they do not prove infinite statements by enumeration.",
            "Vector norm zero is a mathematical diagnostic, not a single-shot physical equality oracle.",
            "Partial maps need an instrument/dilation before being interpreted as physical operations.",
            "A readout schedule does not determine a physical collapse mechanism.",
            "No arithmetic theorem, source authentication, quantum speedup or physical implementation is claimed.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
