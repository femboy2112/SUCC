"""Exact present-output/frame controls, independent of twin_transport.py.

This finite oracle uses rational 2x2 matrices and literal coordinate sums.
It does not inspect observer histories. Universal claims are proved in
TWIN_OBSERVERS.md. The random seed selects reproducible rational fixtures;
it does not assign truth probabilities or measure a physical apparatus.
"""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
import json
from pathlib import Path
import random
import hashlib


def mat(rows):
    return tuple(tuple(Q(x) for x in row) for row in rows)


I = mat(((1, 0), (0, 1)))
Z = mat(((0, 0), (0, 0)))
SWAP = mat(((0, 1), (1, 0)))
PHASE = mat(((1, 0), (0, -1)))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def act(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) for row in a)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def sub(a, b):
    return tuple(tuple(x - y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def vecsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def transpose(a):
    return tuple(zip(*a))


def inverse(a):
    aa, b = a[0]
    c, d = a[1]
    determinant = aa * d - b * c
    if not determinant:
        raise ValueError("singular frame")
    return mat(((d / determinant, -b / determinant),
                (-c / determinant, aa / determinant)))


def product(edges):
    result = I
    for edge in edges:
        result = mul(edge, result)
    return result


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm2(v):
    return dot(v, v)


def frobenius2(a):
    return sum(x * x for row in a for x in row)


@dataclass(frozen=True)
class PresentOutput:
    event: str
    frame: str
    unit: str
    values: tuple


def compare_present(left, right):
    """Only two calibrated present outputs are accepted, never histories."""
    if type(left) is not PresentOutput or type(right) is not PresentOutput:
        raise TypeError("two current output records are required")
    if (left.event, left.frame, left.unit, len(left.values)) != (
            right.event, right.frame, right.unit, len(right.values)):
        raise ValueError("event, frame, unit and dimension must agree")
    return vecsub(left.values, right.values)


def change_frame(output, new_frame, transformation, new_unit=None):
    """Re-express the same event; this cannot advance a historical event."""
    return PresentOutput(output.event, new_frame, new_unit or output.unit,
                         act(transformation, output.values))


def run():
    counts = Counter()
    witnesses = {}

    def check(name, condition):
        counts[name] += 1
        if not condition:
            raise AssertionError(name)

    def rejects(name, f):
        try:
            f()
        except (TypeError, ValueError):
            check(name, True)
        else:
            check(name, False)

    left = PresentOutput("meeting", "common", "length", (Q(1), Q(2)))
    right = PresentOutput("meeting", "swapped", "length", (Q(2), Q(1)))
    rejects("raw_frame_comparison_rejected", lambda: compare_present(left, right))
    corrected = change_frame(right, "common", SWAP)
    check("different_coordinates_same_current_output",
          compare_present(left, corrected) == (0, 0))
    equal_numbers = PresentOutput("meeting", "swapped", "length", left.values)
    corrected_equal = change_frame(equal_numbers, "common", SWAP)
    check("equal_coordinates_different_current_output",
          compare_present(left, corrected_equal) == (-1, 1))
    old = PresentOutput("past_patch", "swapped", "length", right.values)
    old_reframed = change_frame(old, "common", SWAP)
    check("reframing_keeps_event", old_reframed.event == "past_patch")
    rejects("different_event_rejected", lambda: compare_present(left, old_reframed))
    speed = PresentOutput("meeting", "common", "length/time", left.values)
    rejects("incompatible_unit_rejected", lambda: compare_present(left, speed))
    rejects("raw_history_rejected", lambda: compare_present([left, old], right))
    wrong_dimension = PresentOutput("meeting", "common", "length", (Q(1),))
    rejects("dimension_mismatch_rejected", lambda: compare_present(left, wrong_dimension))
    # Two distinct routes produce different internal states and the same
    # permitted first-coordinate output. Only those outputs reach comparison.
    prepared_first = act(I, (Q(1), Q(1)))
    prepared_second = act(PHASE, (Q(1), Q(1)))
    check("distinct_internal_preparations", prepared_first != prepared_second)
    output_from_first = PresentOutput("meeting", "common", "root", prepared_first[:1])
    output_from_second = PresentOutput("meeting", "common", "root", prepared_second[:1])
    check("output_agreement_does_not_require_history_identity",
          compare_present(output_from_first, output_from_second) == (0,))

    scale = mat(((2, 0), (0, 1)))
    metric = mul(transpose(inverse(scale)), inverse(scale))
    moved = act(scale, (Q(1), Q(0)))
    check("untransported_norm_mutation", norm2(moved) == 4)
    check("transported_metric_restores_norm", dot(moved, act(metric, moved)) == 1)
    check("holonomy_root_blindspot", act(PHASE, (1, 0)) == (1, 0))
    check("holonomy_nonroot_detection", vecsub(act(I, (0, 1)), act(PHASE, (0, 1))) == (0, 2))
    first_coordinate = mat(((1, 0),))
    check("coarse_current_readout_misses_holonomy",
          mul(first_coordinate, I) == mul(first_coordinate, PHASE))
    witnesses["present_frames"] = {
        "different_local_coordinates": [[1, 2], [2, 1]],
        "calibrated_equal": True,
        "equal_raw_coordinates_calibrated_residual": [-1, 1],
        "scaled_coordinate_squared_norm": 4,
        "transported_metric_squared_norm": 1,
        "historical_event_is_not_advanced_by_reframing": True,
    }

    rng = random.Random(20261112)

    def rational_matrix(invertible=False):
        while True:
            a = mat(tuple(tuple(Q(rng.randint(-7, 7), rng.choice((1, 3, 7, 11, 13)))
                                for _ in range(2)) for _ in range(2)))
            if not invertible or a[0][0] * a[1][1] != a[0][1] * a[1][0]:
                return a

    for length in range(1, 7):
        for _ in range(18):
            edges = [rational_matrix() for _ in range(length)]
            frames = [rational_matrix(True) for _ in range(length + 1)]
            transformed = [mul(mul(frames[j + 1], edges[j]), inverse(frames[j]))
                           for j in range(length)]
            raw_product = product(edges)
            moved_product = product(transformed)
            check("path_frame_covariance",
                  moved_product == mul(mul(frames[-1], raw_product), inverse(frames[0])))
            x = (Q(rng.randint(-9, 9), 7), Q(rng.randint(-9, 9), 11))
            output = mat(((Q(3, 7), Q(-5, 11)),))
            check("present_readout_gauge_invariance",
                  act(output, act(raw_product, x)) ==
                  act(mul(output, inverse(frames[-1])),
                      act(moved_product, act(frames[0], x))))
            delta = act(raw_product, x)
            moved_delta = act(frames[-1], delta)
            moved_metric = mul(transpose(inverse(frames[-1])), inverse(frames[-1]))
            check("metric_covariance",
                  norm2(delta) == dot(moved_delta, act(moved_metric, moved_delta)))
            holonomy = mul(inverse(frames[0]), mul(PHASE, frames[0]))
            check("holonomy_conjugation_keeps_nontriviality", holonomy != I)

            f_edges = edges
            g_edges = [rational_matrix() for _ in range(length)]
            eta = frames
            defects = [sub(mul(eta[j + 1], f_edges[j]), mul(g_edges[j], eta[j]))
                       for j in range(length)]
            direct = sub(mul(eta[-1], product(f_edges)), mul(product(g_edges), eta[0]))
            telescoped = Z
            for j in range(length):
                term = mul(mul(product(g_edges[j + 1:]), defects[j]), product(f_edges[:j]))
                telescoped = add(telescoped, term)
            check("typed_naturality_defect_telescoping", direct == telescoped)

    rotations = [I, SWAP, PHASE, mat(((Q(3, 5), Q(-4, 5)), (Q(4, 5), Q(3, 5)))),
                 mat(((Q(5, 13), Q(-12, 13)), (Q(12, 13), Q(5, 13)))),
                 mat(((Q(8, 17), Q(-15, 17)), (Q(15, 17), Q(8, 17))))]
    for u in rotations:
        check("unitary_fixture", mul(transpose(u), u) == I)
    for length in range(1, 9):
        for offset in range(len(rotations)):
            edges = [rotations[(j + offset) % len(rotations)] for j in range(length)]
            a = (Q(3, 5), Q(4, 5))
            b = (Q(5, 13), Q(12, 13))
            expected = norm2(vecsub(act(product(edges), a), b))
            for cut in range(length + 1):
                ell = act(product(edges[:cut]), a)
                rr = act(transpose(product(edges[cut:])), b)
                check("unitary_current_vector_cut_defect", norm2(vecsub(ell, rr)) == expected)
                check("current_cut_pairing", dot(rr, ell) == dot(b, act(product(edges), a)))
            compatible_b = act(product(edges), a)
            middle = length // 2
            check("compatible_boundary_meets",
                  act(product(edges[:middle]), a) ==
                  act(transpose(product(edges[middle:])), compatible_b))
            opposite_b = tuple(-x for x in compatible_b)
            check("opposite_boundary_never_meets",
                  norm2(vecsub(act(product(edges[:middle]), a),
                              act(transpose(product(edges[middle:])), opposite_b))) == 4)

    projection = mat(((1, 0), (0, 0)))
    check("lossy_false_agreement", act(projection, (0, 1)) == act(projection, (0, 0)))
    check("lossy_disagreement_existed", norm2(vecsub((0, 1), (0, 0))) == 1)
    witnesses["lossy_false_agreement"] = {
        "map": [[1, 0], [0, 0]], "left_before": [0, 1], "right_boundary": [0, 0],
        "before_squared_discrepancy": 1, "after_squared_discrepancy": 0,
    }

    # Arithmetic checks use direct index arithmetic, without importing return APIs.
    def basis_return(q, r, index):
        return (index // q) * r if index % q == 0 else None

    for dimension in (1, 2, 5, 6, 11, 32):
        squared = Q(0)
        for index in range(dimension):
            a = basis_return(5, 1, index)
            b = basis_return(5, 2, index)
            squared += 0 if a == b else (1 if a is None or b is None else 2)
        expected = Q(2 * ((dimension - 1) // 5), dimension)
        check("finite_twin_return_blindspot_and_detection", squared / dimension == expected)
    witnesses["arithmetic_twin"] = {"q": 5, "r_left": 1, "r_right": 2,
                                     "dimension_5_squared_defect": "0",
                                     "dimension_6_squared_defect": "1/3"}

    for label in (1, 2, 5, 13, 31, 67, 127):
        weight = Q(1, 2 ** (label + 1))
        identity_columns = [Q(1) for _ in range(label + 1)]
        mutated_columns = [Q(-1) if k == label else Q(1) for k in range(label + 1)]
        weighted_difference = sum(Q(1, 2 ** (k + 1)) * (a - b) ** 2
                                  for k, (a, b) in enumerate(zip(identity_columns, mutated_columns)))
        check("weighted_large_norm_small_readout", weighted_difference == 4 * weight)
        check("finite_window_tail_blindspot", identity_columns[:label] == mutated_columns[:label])
        check("outside_window_operator_defect", identity_columns[label] - mutated_columns[label] == 2)
    for dimension in (1, 2, 5, 11, 19):
        # Exact finite rectangular columns. The bound applies to the infinite
        # weighted diagnostic as well by dropping nonnegative tail terms.
        columns = [(Q(j + 1, 7), Q((-1) ** j, 11)) for j in range(dimension)]
        weighted2 = sum(Q(1, 2 ** (j + 1)) * norm2(v) for j, v in enumerate(columns))
        column2 = sum(norm2(v) for v in columns)
        check("weighted_prefix_hilbert_schmidt_bound", column2 <= 2 ** dimension * weighted2)
    witnesses["weighted_conditioning"] = {
        "weights": "w_j=2^(-j-1)", "operator_norm_of_tail_sign_defect": 2,
        "squared_weighted_defect": "4*w_N", "prefix_factor_squared": "2^D",
    }

    return {
        "schema": "succ-twin-present-seam-v1", "status": "PASS", "failures": 0,
        "total_checks": sum(counts.values()), "checks": dict(sorted(counts.items())),
        "witnesses": witnesses,
        "finite_scope": {"arithmetic": "exact rational", "gauge_path_lengths": [1, 6],
                         "gauge_fixtures_per_length": 18, "unitary_path_lengths": [1, 8],
                         "fixture_seed": 20261112,
                         "comparator_inputs": "two calibrated current outputs only"},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "boundary": "Finite exact controls; universal and infinite statements require the written proofs. No physical collapse or arithmetic asymptotic claim.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
