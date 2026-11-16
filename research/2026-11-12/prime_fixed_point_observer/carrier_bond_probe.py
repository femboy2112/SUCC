"""Exact controls for encoded carrier bonds and shared-observable boundaries.

The scalar implementation is the dossier's existing Gaussian-rational helper.
Contractions are independently calculated as exterior tensors and compressed
logical traces.  Actual arithmetic route columns use the unchanged fresh-flag
implementation, compared with literal integer branch execution.  No physical
wormhole, communication channel, or collapse law is simulated.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path
from random import Random

from twin_correlation_probe import (
    Q, Z, ONE, IM, add, adjoint, apply, channel, conjugate, density, diag,
    eye, inner, matrix, multiply, norm2, random_matrix, scaled, tensor,
    trace, transpose, twin,
)
from twin_transport import CenteredReturn, fresh_flags


def minus(a, b):
    return add(a, scaled(b, -1))


def compression(j, x):
    return multiply(multiply(adjoint(j), x), j)


def lift(j, a):
    return multiply(multiply(j, a), adjoint(j))


def embedding(d, padding=1):
    n = d + padding
    rows = [[F(0) for _ in range(d)] for _ in range(n)]
    rows[0][0], rows[-1][0] = F(3, 5), F(4, 5)
    for k in range(1, d):
        rows[k][k] = F(1)
    return matrix(rows)


def unit(d, row, column):
    return matrix([[int(i == row and j == column) for j in range(d)]
                   for i in range(d)])


def expectation(v, a):
    return inner(v, apply(a, v)) / norm2(v)


def vector_tensor(u, v):
    return tuple(x*y for x in u for y in v)


def reduced_left_vector(v, left, right):
    n = norm2(v)
    return matrix([[sum((v[i*right+k] * v[j*right+k].conj()
                         for k in range(right)), Z) / n
                    for j in range(left)] for i in range(left)])


def reduced_right_vector(v, left, right):
    n = norm2(v)
    return matrix([[sum((v[k*right+i] * v[k*right+j].conj()
                         for k in range(left)), Z) / n
                    for j in range(right)] for i in range(right)])


def reduced_right_matrix(rho, left, right):
    return matrix([[sum((rho[k*right+i][k*right+j] for k in range(left)), Z)
                    for j in range(right)] for i in range(right)])


def rational_determinant(rows):
    """Exact row elimination, separate from the Gaussian matrix routines."""
    a = [[F(x) for x in row] for row in rows]
    result = F(1)
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            result = -result
        value = a[col][col]
        result *= value
        for row in range(col + 1, len(a)):
            factor = a[row][col] / value
            for j in range(col, len(a)):
                a[row][j] -= factor * a[col][j]
    return result


def run():
    counts = Counter()

    def check(group, condition, context=None):
        counts[group] += 1
        if not condition:
            raise AssertionError((group, counts[group], context))

    rng = Random(2026111227)
    dimensions = (1, 2, 3, 4, 5, 7)
    for d in dimensions:
        ja, jb = embedding(d), embedding(d, 2)
        na, nb = len(ja), len(jb)
        omega = twin(d)  # Unnormalized vector; norm squared is exactly d.
        exterior = apply(tensor(ja, jb), omega)
        check("endpoint_isometries", multiply(adjoint(ja), ja) == eye(d))
        check("endpoint_isometries", multiply(adjoint(jb), jb) == eye(d))
        check("bond_normalization", norm2(omega) == d)
        check("encoded_bond_normalization", norm2(exterior) == d)
        # Literal cup/cap index contraction, with both normalized factors.
        snake = matrix([[sum((int(i == k and k == j) for k in range(d)), 0)
                         for j in range(d)] for i in range(d)])
        check("unnormalized_snake", snake == eye(d))
        check("normalized_snake_factor", scaled(snake, F(1, d)) == scaled(eye(d), F(1, d)))
        cases = 8 if d <= 4 else 3
        for case in range(cases):
            x, y = random_matrix(rng, na), random_matrix(rng, nb)
            a, b = compression(ja, x), compression(jb, y)
            exterior_expectation = expectation(exterior, tensor(x, y))
            compressed_trace = trace(multiply(a, transpose(b))) / d
            check("exterior_vs_internal_contraction", exterior_expectation == compressed_trace,
                  (d, case))
            # Hermitian current observables retain the same contraction identity.
            hx, hy = add(x, adjoint(x)), add(y, adjoint(y))
            ha, hb = compression(ja, hx), compression(jb, hy)
            observed = expectation(exterior, tensor(hx, hy))
            check("hermitian_current_contraction", observed == trace(multiply(ha, transpose(hb))) / d)
            check("hermitian_expectation_real", observed.im == 0)
            logical_a, logical_b = random_matrix(rng, d), random_matrix(rng, d)
            check("source_corner_products", multiply(lift(ja, logical_a), lift(ja, logical_b)) ==
                  lift(ja, multiply(logical_a, logical_b)))
            check("source_corner_adjoints", adjoint(lift(ja, logical_a)) == lift(ja, adjoint(logical_a)))
            check("source_corner_intertwining", multiply(lift(ja, logical_a), ja) ==
                  multiply(ja, logical_a))
            pa = multiply(ja, adjoint(ja))
            second = random_matrix(rng, na)
            lhs = minus(compression(ja, multiply(x, second)),
                        multiply(compression(ja, x), compression(ja, second)))
            rhs = multiply(multiply(multiply(adjoint(ja), x),
                                    multiply(minus(eye(na), pa), second)), ja)
            check("source_compression_excursion_identity", lhs == rhs)

        phases = [ONE, IM, Q(F(3, 5), F(4, 5)), -ONE, -IM]
        u = diag([phases[i % len(phases)] for i in range(d)])
        check("declared_conjugate_frame", apply(tensor(u, conjugate(u)), omega) == omega)
        reencoded = apply(tensor(multiply(ja, u), multiply(jb, conjugate(u))), omega)
        check("outside_bond_frame_invariance", reencoded == exterior)
        if d >= 2:
            bad = apply(tensor(multiply(ja, u), multiply(jb, u)), omega)
            check("same_frame_mutation_detected", bad != exterior)

    # One-step arithmetic endpoint maps and their concrete outside bond.
    ja = matrix([[F(3, 5) if k == 3 else F(4, 5) if k == 2 else F(0),
                  F(3, 5) if k == 6 else F(4, 5) if k == 4 else F(0)]
                 for k in range(7)])
    va = matrix([[int(k == 2), int(k == 4)] for k in range(7)])
    eta = (Q(F(3, 5)), Q(F(4, 5)))
    eta_column = matrix([[x] for x in eta])
    route_matrix = [[0 for _ in range(7)] for _ in range(14)]
    for source in range(7):
        # Literal source labels, before imposing any finite matrix boundary.
        output, record = (2 * (source // 3), 0) if source % 3 == 0 else (source, 1)
        route_matrix[2*output + record][source] = 1
        actual = fresh_flags((CenteredReturn(3, 2),), {source: F(1)})
        check("literal_arithmetic_route", actual == {((record,), output): F(1)})
    w = matrix(route_matrix)
    check("arithmetic_route_isometry", multiply(adjoint(w), w) == eye(7))
    check("arithmetic_code_isometry", multiply(adjoint(ja), ja) == eye(2))
    check("arithmetic_code_factorization", multiply(w, ja) == tensor(va, eta_column))
    exterior = apply(tensor(ja, ja), twin(2))
    joint = apply(tensor(w, w), exterior)
    # Reorder (A, E_A, B, E_B) to (A, B, E_A, E_B), explicitly.
    ordered = [Z for _ in joint]
    for a in range(7):
        for ha in range(2):
            for b in range(7):
                for hb in range(2):
                    old = (2*a + ha) * 14 + (2*b + hb)
                    new = (7*a + b) * 4 + (2*ha + hb)
                    ordered[new] = joint[old]
    ordered = tuple(ordered)
    present_bond = apply(tensor(va, va), twin(2))
    record_pair = vector_tensor(eta, eta)
    check("two_arithmetic_endpoint_bond", ordered == vector_tensor(present_bond, record_pair))
    check("record_discard_preserves_entire_bond", reduced_left_vector(ordered, 49, 4) == density(present_bond))
    check("outside_record_pair_constant", reduced_right_vector(ordered, 49, 4) == density(record_pair))
    before_a = reduced_left_vector(exterior, 7, 7)
    after_a = reduced_left_vector(present_bond, 7, 7)
    check("before_endpoint_schmidt_purity", trace(multiply(before_a, before_a)) == Q(F(1, 2)))
    check("after_endpoint_schmidt_purity", trace(multiply(after_a, after_a)) == Q(F(1, 2)))
    for i in range(2):
        for j in range(2):
            logical = unit(2, i, j)
            before, after = lift(ja, logical), lift(va, logical)
            check("arithmetic_code_observable_transport",
                  multiply(w, multiply(before, ja)) == multiply(tensor(after, eye(2)), multiply(w, ja)))

    px = matrix([[0, 1], [1, 0]])
    pz = diag((1, -1))
    py = matrix([[0, -IM], [IM, 0]])
    physical_x, physical_z = lift(va, px), lift(va, pz)
    output_projection = multiply(va, adjoint(va))
    check("arithmetic_output_corner_x", multiply(physical_x, physical_x) == output_projection)
    check("arithmetic_output_corner_z", multiply(physical_z, physical_z) == output_projection)
    check("arithmetic_output_noncommuting", multiply(physical_x, physical_z) ==
          scaled(multiply(physical_z, physical_x), -1))
    check("present_bond_xx", expectation(present_bond, tensor(physical_x, physical_x)) == ONE)
    check("present_bond_zz", expectation(present_bond, tensor(physical_z, physical_z)) == ONE)

    # Distinct route lengths and source scales, one common present output bond.
    route_a = (CenteredReturn(3, 2),)
    route_b = (CenteredReturn(2, 1), CenteredReturn(3, 2))
    asymmetric_joint = {}
    for source_a, source_b in ((3, 6), (6, 12)):
        left = fresh_flags(route_a, {source_a: F(1)})
        right = fresh_flags(route_b, {source_b: F(1)})
        for (ha, a), coefficient_a in left.items():
            for (hb, b), coefficient_b in right.items():
                asymmetric_joint[ha, hb, a, b] = coefficient_a * coefficient_b
    check("different_routes_same_present_bond", asymmetric_joint ==
          {((0,), (0, 0), 2, 2): F(1), ((0,), (0, 0), 4, 4): F(1)})
    check("different_internal_records_not_compared", all(ha != hb for ha, hb, _, _ in asymmetric_joint))

    # Shared classical algebra, and the failure of duplicated full algebra.
    repeat = matrix([[1, 0], [0, 0], [0, 0], [0, 1]])
    za, zb = tensor(pz, eye(2)), tensor(eye(2), pz)
    xa, xb = tensor(px, eye(2)), tensor(eye(2), px)
    check("disjoint_physical_commutation", multiply(xa, zb) == multiply(zb, xa))
    check("shared_diagonal_A", multiply(za, repeat) == multiply(repeat, pz))
    check("shared_diagonal_B", multiply(zb, repeat) == multiply(repeat, pz))
    check("duplicated_x_A_refuted", multiply(xa, repeat) != multiply(repeat, px))
    check("duplicated_x_B_refuted", multiply(xb, repeat) != multiply(repeat, px))
    check("joint_x_survives", multiply(tensor(px, px), repeat) == multiply(repeat, px))
    for a in (px, py, pz):
        check("single_bond_mirror", apply(tensor(a, eye(2)), twin(2)) ==
              apply(tensor(eye(2), transpose(a)), twin(2)))
    xz, zx = multiply(px, pz), multiply(pz, px)
    check("mirror_reverses_product", transpose(xz) == multiply(transpose(pz), transpose(px)))
    check("mirror_not_same_algebra_representation", transpose(xz) != multiply(transpose(px), transpose(pz)))
    check("mirror_wrong_order_state_detected", apply(tensor(xz, eye(2)), twin(2)) !=
          apply(tensor(eye(2), xz), twin(2)))

    # A precise counterexample to replacing whole-code preservation by compression.
    j_bad = matrix([[F(3, 5), F(12, 25)], [F(4, 5), F(-9, 25)],
                    [0, F(4, 5)], [0, 0]])
    check("compression_control_code_isometry", multiply(adjoint(j_bad), j_bad) == eye(2))
    a, b = compression(j_bad, za), compression(j_bad, zb)
    check("compression_control_a", a == diag((1, F(-7, 25))))
    check("compression_control_b", b == matrix([[F(-7, 25), F(72, 125)],
                                                [F(72, 125), F(463, 625)]]))
    comm = minus(multiply(a, b), multiply(b, a))
    check("compression_can_create_noncommutation", comm[0][1] == Q(F(2304, 3125)))
    check("physical_parent_commutes", multiply(za, zb) == multiply(zb, za))
    check("compression_missing_preservation_A", multiply(za, j_bad) != multiply(j_bad, a))
    check("compression_missing_preservation_B", multiply(zb, j_bad) != multiply(j_bad, b))
    v = apply(j_bad, (Z, ONE))
    image_error = tuple(x-y for x, y in zip(apply(za, v), apply(j_bad, apply(a, (Z, ONE)))))
    check("compression_explicit_leakage", norm2(image_error) == F(576, 625))
    pauli = (eye(2), px, py, pz)
    compressed_maps = []
    for side in (0, 1):
        columns = []
        for logical_basis in pauli:
            physical = tensor(logical_basis, eye(2)) if side == 0 else tensor(eye(2), logical_basis)
            compressed = compression(j_bad, physical)
            coefficients = [trace(multiply(basis, compressed)) / 2 for basis in pauli]
            check("compression_map_real_pauli_coordinates", all(x.im == 0 for x in coefficients))
            columns.append([x.re for x in coefficients])
        rows = list(zip(*columns))
        compressed_maps.append(rows)
    check("both_endpoint_compression_maps_surjective",
          rational_determinant(compressed_maps[0]) == F(2304, 15625))
    check("both_endpoint_compression_maps_surjective",
          rational_determinant(compressed_maps[1]) == F(4329, 15625))
    not_positive = diag((1, F(-9, 16)))
    check("compressed_representative_not_positive",
          compression(j_bad, tensor(not_positive, eye(2))) == diag((1, 0)))
    check("compressed_representative_not_positive", not_positive[1][1].re < 0)

    # Weighted bond: exact vector mirror, but not a Hermitian observable mirror.
    amplitudes = (Q(F(3, 5)), Q(F(4, 5)))
    omega_weighted = twin(2, amplitudes)
    dmat, dinv = diag(amplitudes), diag((F(5, 3), F(5, 4)))
    mirror = multiply(multiply(dmat, transpose(px)), dinv)
    check("weighted_bond_norm", norm2(omega_weighted) == 1)
    check("weighted_mirror_values", mirror == matrix([[0, F(3, 4)], [F(4, 3), 0]]))
    check("weighted_mirror_identity", apply(tensor(px, eye(2)), omega_weighted) ==
          apply(tensor(eye(2), mirror), omega_weighted))
    check("weighted_mirror_not_hermitian", mirror != adjoint(mirror))
    check("weighted_conjugate_swap_not_invariant", apply(tensor(px, conjugate(px)), omega_weighted) !=
          omega_weighted)
    phase = diag((ONE, IM))
    check("weighted_commuting_frame_invariant", apply(tensor(phase, conjugate(phase)), omega_weighted) ==
          omega_weighted)
    for _ in range(16):
        a, b = random_matrix(rng, 2), random_matrix(rng, 2)
        rhs = trace(multiply(multiply(multiply(dmat, a), dmat), transpose(b)))
        check("weighted_bond_contraction", expectation(omega_weighted, tensor(a, b)) == rhs)

    # Local trace-preserving operations do not update the remote marginal.
    amplitude_damping = (diag((1, F(3, 5))), matrix([[0, F(4, 5)], [0, 0]]))
    dephasing = (diag((1, 0)), diag((0, 1)))
    local_channels = ((px,), (phase,), amplitude_damping, dephasing)
    for local in local_channels:
        kraus_gram = matrix([[0, 0], [0, 0]])
        for k in local:
            kraus_gram = add(kraus_gram, multiply(adjoint(k), k))
        check("local_channel_trace_preserving", kraus_gram == eye(2))
        for vector in (twin(2), omega_weighted):
            rho = density(vector)
            evolved = matrix([[0 for _ in range(4)] for _ in range(4)])
            for k in local:
                evolved = add(evolved, channel(tensor(k, eye(2)), rho))
            check("no_signal_trace", trace(evolved) == ONE)
            check("remote_marginal_unchanged", reduced_right_matrix(evolved, 2, 2) ==
                  reduced_right_matrix(rho, 2, 2))
    selected = channel(tensor(diag((1, 0)), eye(2)), density(twin(2)))
    check("selected_outcome_probability", trace(selected) == Q(F(1, 2)))
    check("selected_remote_state_needs_flag", reduced_right_matrix(scaled(selected, 2), 2, 2) ==
          diag((1, 0)))

    return {
        "status": "PASS", "exact_checks": sum(counts.values()),
        "groups": dict(sorted(counts.items())),
        "finite_scope": {
            "logical_dimensions": list(dimensions), "holdout_dimensions": [5, 7],
            "complex_scalar_field": "Q(i)", "random_seed": 2026111227,
            "arithmetic_matrix_source_window": [0, 6],
            "asymmetric_route_source_labels": [3, 6, 12],
            "protected_logical_dimension": 2,
            "local_channel_controls": 4,
        },
        "explicit_witnesses": {
            "encoded_arithmetic_bond": {
                "code_vectors": [{"3": "3/5", "2": "4/5"},
                                 {"6": "3/5", "4": "4/5"}],
                "logical_bond_normalization": "1/sqrt(2)",
                "output_bond_labels": [[2, 2], [4, 4]],
                "fixed_record_vector_each_end": ["3/5", "4/5"],
                "local_purity_before_and_after": "1/2", "XX": "1", "ZZ": "1",
            },
            "compression_only_counterexample": {
                "code_u": ["3/5", "4/5", "0", "0"],
                "code_v": ["12/25", "-9/25", "4/5", "0"],
                "compressed_commutator_01": "2304/3125",
                "code_leakage_squared_norm": "576/625",
                "endpoint_compression_determinants": ["2304/15625", "4329/15625"],
                "inverse_A_of_positive_logical_projector": [["1", "0"], ["0", "-9/16"]],
            },
            "weighted_observable_boundary": {
                "schmidt_amplitudes": ["3/5", "4/5"],
                "pauli_x_mirror": [["0", "3/4"], ["4/3", "0"]],
                "mirror_hermitian": False,
            },
            "normalized_cup_cap": "identity/d, not identity",
            "different_route_bond": {
                "A_route": [[3, 2]], "B_route": [[2, 1], [3, 2]],
                "source_bond_labels": [[3, 6], [6, 12]],
                "present_bond_labels": [[2, 2], [4, 4]],
                "fixed_records": [[0], [0, 0]],
            },
        },
        "scope": "Exact finite state/code/tensor-contraction controls; no freely shared changing memory, quantum communication channel, gravitational dual, traversable wormhole, or objective collapse law is established.",
        "current_output_contract": "Only declared present observables in calibrated endpoint frames. Whole-code source algebra reconstruction requires actual intertwining and code preservation, not single-state mirrors or compressed expectations.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
    print(rendered, end="")
