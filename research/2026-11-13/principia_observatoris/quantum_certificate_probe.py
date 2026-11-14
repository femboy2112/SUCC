#!/usr/bin/env python3
"""Exact real-qubit certificate for Principia PO-C2a; declared finite models.

No external physical source, general complex-Hermitian implementation, numerical
sampling theorem, or universal classical ontology is certified. The finite sign
family is exhausted. Rational weighted Kraus maps avoid square-root arithmetic.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from typing import Sequence

Matrix = tuple[tuple[Q, Q], tuple[Q, Q]]
ZERO: Matrix = ((Q(0), Q(0)), (Q(0), Q(0)))
IDENTITY: Matrix = ((Q(1), Q(0)), (Q(0), Q(1)))
P0: Matrix = ((Q(1), Q(0)), (Q(0), Q(0)))
P1: Matrix = ((Q(0), Q(0)), (Q(0), Q(1)))
X: Matrix = ((Q(0), Q(1)), (Q(1), Q(0)))
PROJECTORS = (P0, P1)
WeightedKraus = tuple[Q, Matrix]
Instrument = tuple[tuple[WeightedKraus, ...], ...]
Kernels = tuple[Matrix, ...]


def scalar(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise TypeError("Exact int or Fraction required")
    return Q(value)


def matrix(rows: Sequence[Sequence[int | Q]]) -> Matrix:
    if len(rows) != 2 or any(len(row) != 2 for row in rows):
        raise ValueError("This certificate is restricted to real 2x2 matrices")
    return tuple(tuple(scalar(v) for v in row) for row in rows)  # type: ignore[return-value]


def add(a: Matrix, b: Matrix) -> Matrix:
    return matrix([[a[i][j] + b[i][j] for j in range(2)] for i in range(2)])


def scale(c: Q, a: Matrix) -> Matrix:
    return matrix([[c * x for x in row] for row in a])


def mul(a: Matrix, b: Matrix) -> Matrix:
    return matrix([[sum((a[i][k] * b[k][j] for k in range(2)), Q(0))
                    for j in range(2)] for i in range(2)])


def transpose(a: Matrix) -> Matrix:
    return matrix([[a[j][i] for j in range(2)] for i in range(2)])


def dual(branch: tuple[WeightedKraus, ...], effect: Matrix) -> Matrix:
    out = ZERO
    for weight, kraus in branch:
        out = add(out, scale(weight, mul(mul(transpose(kraus), effect), kraus)))
    return out


def apply(branch: tuple[WeightedKraus, ...], rho: Matrix) -> Matrix:
    out = ZERO
    for weight, kraus in branch:
        out = add(out, scale(weight, mul(mul(kraus, rho), transpose(kraus))))
    return out


def trace(a: Matrix) -> Q:
    return a[0][0] + a[1][1]


def principal_minors(a: Matrix) -> tuple[Q, Q, Q]:
    if a != transpose(a):
        raise ValueError("PSD order requires a symmetric real matrix")
    return (a[0][0], a[1][1], a[0][0] * a[1][1] - a[0][1] * a[1][0])


def validate(instrument: Instrument, kernels: Kernels) -> None:
    if not instrument or len(instrument) != len(kernels):
        raise ValueError("Need one coarse kernel per outcome")
    normalization = ZERO
    for branch, kernel in zip(instrument, kernels):
        for weight, kraus in branch:
            scalar(weight)
            matrix(kraus)
            if weight < 0:
                raise ValueError("Negative Kraus weights do not certify CP")
        normalization = add(normalization, dual(branch, IDENTITY))
        matrix(kernel)
        if any(v < 0 for row in kernel for v in row):
            raise ValueError("Coarse kernels must be nonnegative")
    if normalization != IDENTITY:
        raise ValueError("Instrument sum is not trace preserving")
    if any(sum((kernel[i][j] for kernel in kernels for j in range(2)), Q(0)) != 1
           for i in range(2)):
        raise ValueError("Joint coarse outcome/state kernel is not normalized")


def encode_matrix(a: Matrix) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def certificate(instrument: Instrument, kernels: Kernels, epsilon: Q) -> dict:
    """Check all PO-C2a signs, retaining every matrix/minor and all failures."""
    epsilon = scalar(epsilon)
    if epsilon < 0:
        raise ValueError("Error tolerance cannot be negative")
    validate(instrument, kernels)
    defects = []
    for branch, kernel in zip(instrument, kernels):
        for j, projection in enumerate(PROJECTORS):
            effective = add(scale(kernel[0][j], P0), scale(kernel[1][j], P1))
            defects.append(add(dual(branch, projection), scale(Q(-1), effective)))
    checks = []
    failures = []
    for signs in product((-1, 1), repeat=len(defects)):
        signed = ZERO
        for sign, defect in zip(signs, defects):
            signed = add(signed, scale(Q(sign), defect))
        bound = add(scale(2 * epsilon, IDENTITY), scale(Q(-1), signed))
        minors = principal_minors(bound)
        check = {
            "signs": list(signs),
            "bound_matrix": encode_matrix(bound),
            "principal_minors": [str(x) for x in minors],
            "psd": all(x >= 0 for x in minors),
        }
        checks.append(check)
        if not check["psd"]:
            failures.append(len(checks) - 1)
    assert len(checks) == 2 ** len(defects)
    return {
        "epsilon": str(epsilon),
        "certified": not failures,
        "defect_order": [[o, j] for o in range(len(instrument)) for j in range(2)],
        "defects": [encode_matrix(d) for d in defects],
        "all_signs_checked": len(checks),
        "failed_sign_indices": failures,
        "checks": checks,
    }


def run() -> dict:
    z: Instrument = (((Q(1), P0),), ((Q(1), P1),))
    z_kernel: Kernels = (P0, P1)
    noise_z: Instrument = tuple(
        ((Q(2, 3), projection), (Q(1, 3), mul(projection, X)))
        for projection in PROJECTORS
    )
    noise_kernel: Kernels = (
        matrix(((Q(2, 3), 0), (Q(1, 3), 0))),
        matrix(((0, Q(1, 3)), (0, Q(2, 3)))),
    )
    reset_x: Instrument = (
        ((Q(1, 2), matrix(((1, 1), (0, 0)))),),
        ((Q(1, 2), matrix(((1, -1), (0, 0)))),),
    )
    reset_kernel: Kernels = (matrix(((Q(1, 2), 0), (Q(1, 2), 0))),) * 2
    results = {
        "z_exact": certificate(z, z_kernel, Q(0)),
        "bitflip_z_exact": certificate(noise_z, noise_kernel, Q(0)),
        "reset_x_half_error": certificate(reset_x, reset_kernel, Q(1, 2)),
        "reset_x_false_third_error": certificate(reset_x, reset_kernel, Q(1, 3)),
    }
    assert results["z_exact"]["certified"]
    assert results["bitflip_z_exact"]["certified"]
    assert results["reset_x_half_error"]["certified"]
    rejected = results["reset_x_false_third_error"]
    assert not rejected["certified"]
    assert any("-5/9" in c["principal_minors"] for c in rejected["checks"])

    # Saturating states prove the optimal error is exactly 1/2 for this K.
    qplus = scale(Q(1, 2), matrix(((1, 1), (1, 1))))
    qminus = scale(Q(1, 2), matrix(((1, -1), (-1, 1))))
    actual_plus = [trace(apply(branch, qplus)) for branch in reset_x]
    actual_minus = [trace(apply(branch, qminus)) for branch in reset_x]
    assert actual_plus == [Q(1), Q(0)]
    assert actual_minus == [Q(0), Q(1)]
    assert qplus[0][0] == qminus[0][0] == Q(1, 2)
    saturation = sum(abs(x - Q(1, 2)) for x in actual_plus) / 2
    assert saturation == Q(1, 2)

    rejected_invalid = []
    invalid_cases = (
        ("incomplete_instrument", (z[0],), (IDENTITY,)),
        ("negative_kraus_weight", (((Q(-1), IDENTITY),),), (IDENTITY,)),
        ("unnormalized_kernel", z, (ZERO, ZERO)),
    )
    for name, inst, kernel in invalid_cases:
        try:
            certificate(inst, kernel, Q(0))
        except ValueError:
            rejected_invalid.append(name)
        else:
            raise AssertionError("Invalid certificate input was accepted: " + name)

    return {
        "status": "EXACT_REAL_QUBIT_FINITE_CERTIFICATES",
        "theorem": "PO-C2a",
        "source_semantics": "Declared weighted rational Kraus maps, not external measurements",
        "scalar_arithmetic": "fractions.Fraction",
        "matrix_scope": "Real symmetric 2x2; diagonal algebra with two minimal projections",
        "results": results,
        "total_sign_matrices_checked": sum(r["all_signs_checked"] for r in results.values()),
        "reset_x_optimal_error_for_declared_kernel": str(saturation),
        "saturating_plus_outcome_law": [str(x) for x in actual_plus],
        "saturating_minus_outcome_law": [str(x) for x in actual_minus],
        "invalid_inputs_rejected": rejected_invalid,
        "physical_experiment_claimed": False,
        "general_complex_certificate_claimed": False,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = run()
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(json.dumps({
        "status": receipt["status"],
        "sign_matrices": receipt["total_sign_matrices_checked"],
        "certified_positive_controls": 3,
        "false_epsilon_rejected": True,
        "invalid_inputs_rejected": len(receipt["invalid_inputs_rejected"]),
        "reset_x_optimal_epsilon": receipt["reset_x_optimal_error_for_declared_kernel"],
        "receipt": str(args.output) if args.output else None,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
