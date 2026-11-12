"""Small exact complete-qubit controls for a declared communication bridge.

Gaussian-rational primitives are inherited; the literal circuit expansion,
branch maps, no-message twirl, no-signalling test and reference checks are
implemented here. No physical wormhole or collapse model is simulated.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from twin_correlation_probe import (
    Q, Z, ONE, IM, add, adjoint, apply, density, diag, eye, matrix,
    multiply, norm2, scaled, tensor, trace,
)


def zeros(rows, cols):
    return matrix([[0] * cols for _ in range(rows)])


def matrix_unit(d, i, j):
    return matrix([[int(a == i and b == j) for b in range(d)] for a in range(d)])


def conjugation(a, x):
    return multiply(multiply(a, x), adjoint(a))


def channel(kraus, x):
    y = zeros(len(kraus[0]), len(kraus[0]))
    for k in kraus:
        y = add(y, conjugation(k, x))
    return y


def partial_trace_first(rho, first, second):
    return tuple(tuple(sum((rho[a * second + i][a * second + j]
                            for a in range(first)), Z)
                       for j in range(second)) for i in range(second))


def trace_preserving(kraus):
    d = len(kraus[0][0])
    total = zeros(d, d)
    for k in kraus:
        total = add(total, multiply(adjoint(k), k))
    return total == eye(d)


def literal_teleportation_isometry():
    """Register order S,A,B; combined Bell/H normalization is exactly 1/2."""
    values = [[F(0) for _ in range(2)] for _ in range(8)]
    for source in (0, 1):
        for bell_label in (0, 1):
            # Prepared Bell term is (A,B)=(bell_label,bell_label).
            after_cnot_a = bell_label ^ source
            for hadamard_output in (0, 1):
                sign = -1 if source * hadamard_output else 1
                target = 4 * hadamard_output + 2 * after_cnot_a + bell_label
                values[target][source] += F(sign, 2)
    return matrix(values)


def main():
    counts = Counter()

    def check(group, condition, label=""):
        counts[group] += 1
        if not condition:
            raise AssertionError((group, counts[group], label))

    ident = eye(2)
    x = matrix([[0, 1], [1, 0]])
    z = diag((1, -1))
    check("scalar_calibration", IM * IM == Q(-1))
    check("scalar_calibration", Q(F(3, 5), F(4, 5)).abs2() == 1)

    # Normalized cup/cap contraction, literal Kronecker-index sum.
    for d in (1, 2, 3, 5):
        contraction = matrix([[sum((F(int(i == a and a == k), d)
                                   for a in range(d)), F(0))
                               for i in range(d)] for k in range(d)])
        check("normalized_snake", contraction == scaled(eye(d), F(1, d)), d)
        vector = tuple(Q(j + 1, j % 2) for j in range(d))
        probability = norm2(apply(contraction, vector)) / norm2(vector)
        check("normalized_snake_probability", probability == F(1, d * d), d)

    t = literal_teleportation_isometry()
    check("literal_circuit_isometry", multiply(adjoint(t), t) == ident)
    branches, corrections = [], []
    for a in (0, 1):
        for b in (0, 1):
            u = multiply(x if b else ident, z if a else ident)
            branch = tuple(t[4 * a + 2 * b + j] for j in (0, 1))
            correction = adjoint(u)
            branches.append(branch)
            corrections.append(correction)
            check("literal_branch_formula", branch == scaled(u, F(1, 2)), (a, b))
            check("branch_probability", multiply(adjoint(branch), branch) == scaled(ident, F(1, 4)), (a, b))
            check("branch_correction", multiply(correction, branch) == scaled(ident, F(1, 2)), (a, b))
    check("complete_instrument", trace_preserving(branches))
    corrected = tuple(multiply(c, e) for c, e in zip(corrections, branches))
    one_bit = tuple(multiply(x if b else ident, branches[2 * a + b])
                    for a in (0, 1) for b in (0, 1))
    for i in (0, 1):
        for j in (0, 1):
            rho = matrix_unit(2, i, j)
            check("all_matrix_units_identity", channel(corrected, rho) == rho, (i, j))
            check("all_matrix_units_twirl", channel(branches, rho) == scaled(ident, F(int(i == j), 2)), (i, j))
            check("one_bit_control", channel(one_bit, rho) == scaled(add(rho, conjugation(z, rho)), F(1, 2)), (i, j))

    # Global phase conventions are exact at the coherent amplitude level.
    c = zeros(8, 8)
    for a in (0, 1):
        for b in (0, 1):
            p = matrix_unit(4, 2 * a + b, 2 * a + b)
            c = add(c, tensor(p, corrections[2 * a + b]))
    check("coherent_control_unitary", multiply(adjoint(c), c) == eye(8))
    corrected_t = multiply(c, t)
    target = matrix([[F(int(b == s), 2) for s in (0, 1)]
                     for _syndrome in range(4) for b in (0, 1)])
    check("coherent_factorization", corrected_t == target)
    check("coherent_factorization", multiply(adjoint(corrected_t), corrected_t) == ident)

    # Complete reference test with a normalized Bell density; no sqrt arithmetic.
    bell = density((ONE, Z, Z, ONE))
    with_reference = conjugation(tensor(corrected_t, ident), bell)
    expected = tensor(density((ONE, ONE, ONE, ONE)), bell)
    check("reference_preservation", with_reference == expected)
    check("reference_preservation", partial_trace_first(with_reference, 4, 4) == bell)
    no_message = conjugation(tensor(t, ident), bell)
    check("reference_no_message", partial_trace_first(no_message, 4, 4) == scaled(eye(4), F(1, 4)))
    check("reference_no_message", partial_trace_first(no_message, 4, 4) != bell)

    # Missing a branch correction fails the channel even if most branches pass.
    mutated = list(corrected)
    mutated[3] = branches[3]
    mutation_output = channel(mutated, matrix_unit(2, 0, 0))
    check("missing_correction_mutation", mutation_output == diag((F(3, 4), F(1, 4))))
    check("missing_correction_mutation", mutation_output != matrix_unit(2, 0, 0))

    # General no-signalling identity tested on all 16 joint matrix units.
    p0, p1 = matrix_unit(2, 0, 0), matrix_unit(2, 1, 1)
    local_maps = {
        "identity": (ident,),
        "X": (x,),
        "Z": (z,),
        "phase": (diag((ONE, IM)),),
        "rotation": (matrix([[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]),),
        "dephase": (p0, p1),
        "reset_zero": (matrix([[1, 0], [0, 0]]), matrix([[0, 1], [0, 0]])),
        "reset_one": (matrix([[0, 0], [1, 0]]), matrix([[0, 0], [0, 1]])),
        "amplitude_damping": (diag((1, F(3, 5))), matrix([[0, F(4, 5)], [0, 0]])),
    }
    for name, kraus in local_maps.items():
        check("local_map_calibration", trace_preserving(kraus), name)
        joint = tuple(tensor(k, ident) for k in kraus)
        for i in range(4):
            for j in range(4):
                rho = matrix_unit(4, i, j)
                before = partial_trace_first(rho, 2, 2)
                after = partial_trace_first(channel(joint, rho), 2, 2)
                check("chosen_message_no_signalling", after == before, (name, i, j))

    # Distinct chosen local unitaries alter the joint state, not Bob's marginal.
    other_bell = conjugation(tensor(x, ident), bell)
    check("message_joint_state_control", other_bell != bell)
    check("message_joint_state_control", partial_trace_first(other_bell, 2, 2) == partial_trace_first(bell, 2, 2))
    # A selected local outcome is a trace-decreasing branch, not a chosen channel.
    selected_zero = conjugation(tensor(p0, ident), bell)
    selected_one = conjugation(tensor(p1, ident), bell)
    check("postselection_scope", trace(selected_zero) == Q(F(1, 2)))
    check("postselection_scope", trace(selected_one) == Q(F(1, 2)))
    check("postselection_scope", partial_trace_first(add(selected_zero, selected_one), 2, 2) == scaled(ident, F(1, 2)))
    check("postselection_scope", not trace_preserving((p0,)))

    this_file = Path(__file__)
    shared = this_file.with_name("twin_correlation_probe.py")
    return {
        "status": "PASS", "exact_checks": sum(counts.values()), "groups": dict(counts),
        "normalization": {"qubit_selected_amplitude": "1/2", "qubit_selected_probability": "1/4",
                          "dimension_d_selected_amplitude": "1/d", "dimension_d_selected_probability": "1/d^2"},
        "protocol": {"syndrome_order": "a=input qubit S, b=Alice Bell half A",
                     "branch": "X^b Z^a / 2", "correction": "Z^a X^b",
                     "before_message": "rho -> Tr(rho) I/2", "after_complete_correction": "identity channel",
                     "coherent_output": "|++>_syndrome tensor |psi>_Bob, including arbitrary reference",
                     "standard_resources": "One Bell pair and two classical bits, plus local circuit/measurement/corrections.",
                     "coherent_resources": "Actual coherent syndrome transmission or supplied joint controlled coupling; not an entangled-state-only implementation."},
        "finite_scope": {"teleportation_matrix_units": 4, "reference_dimensions": [2, 2],
                         "local_maps": list(local_maps), "no_signalling_joint_matrix_units_per_map": 16},
        "script_sha256": hashlib.sha256(this_file.read_bytes()).hexdigest(),
        "shared_scalar_dependency_sha256": hashlib.sha256(shared.read_bytes()).hexdigest(),
        "scope": "Exact finite algebraic controls of proved channel identities. No physical wormhole, objective collapse, free communication, infinite-input certificate, or new arithmetic asymptotic is claimed.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(main(), indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
    print(rendered, end="")
