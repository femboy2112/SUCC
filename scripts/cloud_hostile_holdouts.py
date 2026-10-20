#!/usr/bin/env python3
"""Read-only adversarial fixtures against a separately checked-out SUCC target.

This is an audit runner, not a proof authority or a repair of the target.  An
``exposed`` result records a counterexample; it is deliberately not a passing
positivity certificate.  Run each target in a fresh Python process.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.metadata
import json
from math import gcd
from pathlib import Path
import subprocess
import sys


def shallow_negative_family(n: int, denominator: int):
    """Return exact M=nI-(1+1/denominator)J and v=(1,...,1).

    For n>=3 and denominator>2, q(v)=-n^2/denominator<0, whereas
    every coordinate direction and every e_i +/- e_j has nonnegative q.
    """
    if type(n) is not int or n < 3 or type(denominator) is not int or denominator <= 2:
        raise ValueError("require n>=3 and integer denominator>2")
    eps = Fraction(1, denominator)
    matrix = [[Fraction(n if i == j else 0) - (1 + eps)
               for j in range(n)] for i in range(n)]
    return matrix, [Fraction(1)] * n


def rational_quad(matrix, vector):
    return sum((vector[i] * matrix[i][j] * vector[j]
                for i in range(len(vector)) for j in range(len(vector))), Fraction())


def primitive_slope_audit(max_x: int = 40, max_divisor: int = 12):
    """Independent integer-enumeration check of the proposed divisor spacing lemma.

    No arithmetic function, CRT implementation, or lane B counting code is used.
    This finite receipt supports calibration, not the universal proof.
    """
    checks = 0
    for x in range(2, max_x + 1):
        primitive = [(a, c) for c in range(2, x + 1)
                     for a in range(1, c) if gcd(a, c) == 1]
        for d in range(1, max_divisor + 1):
            for e in range(1, max_divisor + 1):
                for f in range(1, max_divisor + 1):
                    if gcd(d, e) * gcd(d, f) * gcd(e, f) != 1:
                        continue
                    points = [(a, c) for a, c in primitive
                              if a % d == 0 and (c - a) % e == 0 and c % f == 0]
                    product = d * e * f
                    if len(points) > 1 + Fraction(x * x, product):
                        raise AssertionError((x, d, e, f, points))
                    for (a, c), (aa, cc) in zip(points, points[1:]):
                        if (a * cc - aa * c) % product:
                            raise AssertionError("determinant divisibility failed")
                    checks += 1
    # Primitive slope injectivity is necessary: two multiples share one slope.
    x, d, e, f = 34, 8, 9, 17
    nonprimitive = [(a, c) for c in range(2, x + 1) for a in range(1, c)
                    if a % d == 0 and (c - a) % e == 0 and c % f == 0]
    bound = 1 + Fraction(x * x, d * e * f)
    assert len(nonprimitive) > bound
    return {"cases": checks, "max_x": max_x, "max_divisor": max_divisor,
            "primitive_failures": 0,
            "nonprimitive_mutation": {"x": x, "d": d, "e": e, "f": f,
                                      "points_a_c": nonprimitive,
                                      "count": len(nonprimitive), "bound": str(bound)}}


def target_audit(target: Path):
    target = target.resolve()
    sys.path.insert(0, str(target))
    from observational_succ import proof_contracts as pc
    from observational_succ import quantitative_rigidity as qr
    from observational_succ import abc_decomposition as abc
    from observational_succ import goldbach_circle as gc
    import sympy as sp

    def contract(**overrides):
        fields = dict(name="cloud hostile fixture", statement="0 = 1", prefix=[],
                      hypotheses=[], constant_dependencies={}, finite_to_infinite="none",
                      source_authentic=False, method="adversarial fixture", status="UNVERIFIED")
        fields.update(overrides)
        return pc.ProofContract(**fields)

    records = []

    def attempt(identifier, expected, fn, exposed):
        try:
            observed = fn()
            state = "exposed" if exposed(observed) else "not_exposed"
            records.append({"id": identifier, "expected": expected,
                            "state": state, "observed": observed})
        except Exception as exc:
            records.append({"id": identifier, "expected": expected,
                            "state": "rejected_or_exception",
                            "exception": type(exc).__name__, "message": str(exc)})

    attempt("F01_SOURCE_FLAG_MISMATCH", "reject authentic claim with synthetic witness",
            lambda: pc.CarryingContract(
                contract(source_authentic=True),
                source_witness=pc.SourceRealizationWitness("unrelated synthetic object", False)
            ).verify(), lambda r: r.get("source_authentic") is True)

    def status_mutation():
        c = contract()
        carrying = pc.CarryingContract(c)
        c.status = "PROVED LOCAL"
        return carrying.verify()
    attempt("F02_MUTABLE_STATUS", "reject proof status with no backing at verification time",
            status_mutation,
            lambda r: r.get("status") == "PROVED LOCAL" and not r.get("certificates_verified")
                      and not r.get("theorem_refs"))

    def dependency_contradiction():
        c = contract(prefix=[pc.Quantifier("exists", "C", "positive reals"),
                             pc.Quantifier("forall", "N", "positive integers")],
                     constant_dependencies={"C": ["N"]})
        return {"uniform": c.is_uniform_in("C", "N"), "record": c.as_record()}
    attempt("F03_CONTRADICTORY_DEPENDENCIES", "reject later dependency in constant metadata",
            dependency_contradiction, lambda r: r["uniform"] is True)

    attempt("F04_UNCHECKED_THEOREM_REFERENCE", "do not grant proof authority to nonexistent theorem",
            lambda: pc.CarryingContract(
                contract(status="PROVED LOCAL"),
                theorem_refs=[pc.TheoremReference("NoSuchTheorem", "NoSuchKernel")]
            ).verify(), lambda r: r.get("status") == "PROVED LOCAL")

    matrix, vector = shallow_negative_family(3, 10**14)
    exact_value = rational_quad(matrix, vector)
    assert exact_value == Fraction(-9, 10**14)
    smatrix = sp.Matrix(matrix)
    witness_record = {"id": "F05_SHALLOW_NEGATIVE_CONE",
                      "expected": "produce rational negative vector for non-PSD rational matrix",
                      "matrix": [[str(x) for x in row] for row in matrix],
                      "known_vector": [str(x) for x in vector],
                      "known_value": str(exact_value),
                      "target_psd": bool(qr.is_positive_semidefinite(smatrix))}
    try:
        witness = qr.negative_witness(smatrix)
        valid = witness is not None and (witness.T * smatrix * witness)[0] < 0
        witness_record.update(state="not_exposed" if valid else "exposed",
                              returned_vector=None if witness is None else str(witness))
    except Exception as exc:
        witness_record.update(state="exposed", exception=type(exc).__name__, message=str(exc))
    records.append(witness_record)

    # A lower cutoff bound must reject noninteger P rather than silently omitting all primes.
    attempt("F06_NONINTEGER_CUTOFF", "reject noninteger prime cutoff",
            lambda: [str(x) for x in gc.singular_series_enclosure(2, Fraction(5, 2))],
            lambda r: r == ["1/3", "1"])
    records[-1]["independent_true_lower_bound"] = "135/128"
    records[-1]["lower_bound_derivation"] = "2*(1-1/4)*(1-1/16)*(1-1/4)"

    # Not a bug in the exact anatomy identity: this falsifies the displayed
    # interpretation that the whole high-exponent tail is the BBLT small n0.
    n, d = 2**8, 4
    anatomy = abc.bblt_anatomy(n, d)
    tail_doc = abc.bblt_anatomy.__doc__ or ""
    records.append({"id": "F07_BBLT_TAIL_ATTRIBUTION",
                    "state": "exposed" if "BBLT make n0" in tail_doc else "source_review_required",
                    "expected": "do not identify whole exponent tail with small BBLT remainder",
                    "n": n, "d": d, "eps": "1/4", "actual_n0": anatomy["n0"],
                    "claimed_small_remainder_upper": 4,
                    "scope": "documentation/proof attribution; exact identity itself remains true"})

    # Finite local factors give the exact quotient, independently of tail bounds.
    ratio = gc.singular_series_local_factor(5, 10) / gc.singular_series_local_factor(5, 2)
    twin_doc = gc.twin_prime_constant_enclosure.__doc__ or ""
    records.append({"id": "F08_TWIN_CONSTANT_NORMALIZATION",
                    "state": "exposed" if "2*C_2 is S(N)" in twin_doc else "source_review_required",
                    "expected": "S(10)=(4/3)*(2*C2), not 2*C2",
                    "p": 5, "P": 3, "exact_ratio_S10_over_S2": str(ratio),
                    "scope": "false docstring identity; twin constant enclosure computation is separate"})

    h = 10**30
    shifted = sp.Matrix([[h + 2, 1], [1, h + 2]])
    reported_minimum = qr.min_eigenvalue_exact(shifted)
    test_vector = sp.Matrix([1, -1])
    bound_defect = (test_vector.T * (shifted - reported_minimum * sp.eye(2)) * test_vector)[0]
    records.append({"id": "F09_FLOAT_ORDERED_EXACT_EIGENVALUE",
                    "state": "exposed" if reported_minimum != h + 1 else "not_exposed",
                    "expected": str(h + 1), "observed": str(reported_minimum),
                    "matrix": [[h+2, 1], [1, h+2]], "test_vector": [1, -1],
                    "quadratic_form_after_subtracting_reported_minimum": str(bound_defect)})

    paths = ["observational_succ/" + name + ".py" for name in
             ("proof_contracts", "quantitative_rigidity", "abc_decomposition", "goldbach_circle")]
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=target, text=True).strip()
    dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=target, text=True)
    return {"target_sha": sha, "target_worktree_dirty": bool(dirty),
            "python": sys.version, "dependencies": {name: importlib.metadata.version(name)
                for name in ("sympy", "numpy")},
            "target_source_sha256": {p: hashlib.sha256((target / p).read_bytes()).hexdigest()
                                     for p in paths}, "findings": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-repo", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--slope-audit", action="store_true")
    args = parser.parse_args()
    report = target_audit(args.target_repo)
    if args.slope_audit:
        report["independent_abc_slope_calibration"] = primitive_slope_audit()
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
    print(serialized)


if __name__ == "__main__":
    main()
