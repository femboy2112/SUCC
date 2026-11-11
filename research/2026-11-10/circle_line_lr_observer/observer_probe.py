#!/usr/bin/env python3
"""Independent finite certificate checks and hostile controls for the observer.

The production generator never calls this module. BBP is a verification-only
source here. Algebraic checks are finite evidence; universal statements are
proved in the accompanying notes, rather than inferred from this receipt.
"""
from __future__ import annotations

import argparse
import ast
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import platform
import sys

from circle_line_observer import (
    EuclideanCircleLine as Geometry, IDENTITY, L, R, Matrix2,
    MatrixCircleSource, RotationCircleSource, digit_certificates, finite_run, rational_text,
)


def beta_intervals(count: int) -> list[tuple[Q, Q]]:
    """Independent scalar-series implementation, with no matrix multiplication."""
    w, partial = Q(1), Q(0)
    intervals = [(Q(3), Q(4))]
    for k in range(1, count+1):
        partial += 2*w
        w *= Q(k, 2*k+1)
        intervals.append((partial+3*w, partial+4*w))
    return intervals


def rotation_interval(m: int) -> tuple[Q, Q]:
    def partial(inv: int, terms: int) -> Q:
        return sum((Q((-1)**j, (2*j+1)*inv**(2*j+1))
                    for j in range(terms)), Q(0))
    return (4*sum((partial(inv, 2*m) for inv in (2, 3)), Q(0)),
            4*sum((partial(inv, 2*m-1) for inv in (2, 3)), Q(0)))


def bbp_interval(terms: int) -> tuple[Q, Q]:
    """Four-pole source, independent of either geometric implementation.

    Its positive integral form bounds the remaining tail by
    16^(1-N)/((8N+1)(8N+2)); see the preceding round's source proof.
    """
    partial = sum((Q(1, 16**n)*(Q(4, 8*n+1)-Q(2, 8*n+4)
                    -Q(1, 8*n+5)-Q(1, 8*n+6))
                   for n in range(terms)), Q(0))
    return partial, partial+Q(16, 16**terms*(8*terms+1)*(8*terms+2))


def matmul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(zip(*a))


def conic(u, v):
    return ((v*v-u*u,), (2*u*v,), (v*v+u*u,))


def verify_trace(trace: dict, source_intervals: list[tuple[Q, Q]], independent) -> None:
    """Replay certificates without the observer's state-update implementation."""
    a, b, c, d = 3, 1, 4, 1
    stage = 0
    word = []
    for k, certificate in enumerate(trace["arrow_certificates"], 1):
        assert certificate["step"] == k
        level = certificate["source_stage"]
        assert level >= stage
        assert certificate["source_consumed"] == level-stage
        stage = level
        lo, hi = source_intervals[level]
        mediant = Q(a+c, b+d)
        assert Q(certificate["mediant"]) == mediant
        arrow = certificate["arrow"]
        if arrow == "L":
            assert hi <= mediant
            c += a
            d += b
        elif arrow == "R":
            assert lo >= mediant
            a += c
            b += d
        else:
            raise AssertionError("Unknown arrow")
        assert certificate["endpoints"] == [a, b, c, d]
        assert b*c-a*d == 1
        assert Q(a, b) <= lo < hi <= Q(c, d)
        assert Q(a, b) < independent[0] < independent[1] < Q(c, d)
        assert Q(c, d)-Q(a, b) == Q(1, b*d) <= Q(1, k+1)
        word.append(arrow)
    assert trace["word"] == "".join(word)
    assert trace["steps"] == len(word)
    assert trace["endpoints"] == [str(Q(a, b)), str(Q(c, d))]
    assert Q(trace["interval_width"]) == Q(1, b*d)
    assert trace["global_root_prefix"] == "RRRL"


def certified_cf(interval: tuple[Q, Q], count: int) -> list[int]:
    """Continued fractions from an independent BBP interval, without L/R states."""
    lo, hi = interval
    result = []
    for _ in range(count):
        a, b = lo.numerator//lo.denominator, hi.numerator//hi.denominator
        if a != b:
            raise AssertionError("Independent interval needs more precision")
        result.append(a)
        assert lo-a > 0
        lo, hi = 1/(hi-a), 1/(lo-a)
    return result


def main() -> dict:
    independent = bbp_interval(180)
    primary = finite_run(512, 64, "matrix")
    alternate = finite_run(512, 64, "rotations")
    assert primary["word"] == alternate["word"]
    assert primary["hexadecimal"] == alternate["hexadecimal"]
    source_intervals = beta_intervals(primary["final_source_stage"])
    verify_trace(primary, source_intervals, independent)

    # All stored digit decisions also agree with an independently derived name.
    for entry in primary["digit_certificates"]:
        j, level, integer = entry["exponent"], entry["source_stage"], entry["floor"]
        for endpoint in (*source_intervals[level], *independent):
            scaled = endpoint*16**j
            assert scaled.numerator//scaled.denominator == integer
        assert entry["digit"] == format(integer % 16, "X")

    source = MatrixCircleSource()
    for k, interval in enumerate(source_intervals):
        assert (source.lower, source.upper) == interval
        assert interval[0] < independent[0] < independent[1] < interval[1]
        if k:
            previous = source_intervals[k-1]
            assert previous[0] <= interval[0] < interval[1] < previous[1]
            assert interval[1]-interval[0] < Q(1, 2**k)
        source.refine()

    rotation = RotationCircleSource()
    for m in range(1, 65):
        expected = rotation_interval(m)
        assert (rotation.lower, rotation.upper) == expected
        assert expected[0] < independent[0] < independent[1] < expected[1]
        width = Q(4, 4*m-1)*(Q(1, 2**(4*m-1))+Q(1, 3**(4*m-1)))
        assert expected[1]-expected[0] == width
        rotation.refine()

    # A third geometric construction: monotone rational Riemann sums.
    riemann = []
    for n in (2, 4, 8, 16, 32, 64, 128):
        lower = Q(4, n)*sum((1/(1+Q(k, n)**2) for k in range(1, n+1)), Q(0))
        upper = Q(4, n)*sum((1/(1+Q(k, n)**2) for k in range(n)), Q(0))
        assert upper-lower == Q(2, n)
        assert lower < independent[0] < independent[1] < upper
        riemann.append({"subdivisions": n, "width": str(upper-lower)})

    parameters = sorted({Q(i, j) for i in range(-8, 9) for j in range(1, 9)})
    for t in parameters:
        x, y = Geometry.point(t)
        dx, dy = Geometry.tangent(t)
        assert x*x+y*y == 1
        assert y == t*(x+1)
        assert dx*dx+dy*dy == Geometry.arc_speed(t)**2
        assert y/(1+x) == t
    for t in (-2, 0, 1, 2):
        assert all(isinstance(x, Q) for x in Geometry.point(t)+Geometry.tangent(t))
        assert isinstance(Geometry.arc_speed(t), Q)
        assert isinstance(Geometry.metric_jacobian(L, t), Q)
    assert Geometry.multiply(Geometry.point(Q(1, 2)), Geometry.point(Q(1, 3))) == (0, 1)

    # Actual map/coherence checks for the projective line -> circle/conic functor.
    words = ["".join(p) for n in range(5) for p in product("LR", repeat=n)]
    matrices = []
    for word in words:
        m = IDENTITY
        for letter in word:
            m = m @ (L if letter == "L" else R)
        matrices.append(m)
    matrices.extend((Matrix2(3, 14, 0, 7), Matrix2(1, Q(1, 2), Q(-1, 2), 1)))
    lorentz = ((1, 0, 0), (0, 1, 0), (0, 0, -1))
    for m in matrices:
        cm = Geometry.conic_lift(m)
        lhs = matmul(matmul(transpose(cm), lorentz), cm)
        assert lhs == tuple(tuple(m.determinant**2*x for x in row) for row in lorentz)
        for u, v in ((0, 1), (1, 1), (1, 2), (-3, 4), (2, -1)):
            assert matmul(cm, conic(u, v)) == conic(m.a*u+m.b*v, m.c*u+m.d*v)
        for n in matrices:
            assert Geometry.conic_lift(m @ n) == matmul(cm, Geometry.conic_lift(n))
    for m, n in product(matrices[:8], repeat=2):
        for t in (Q(0), Q(1, 2), Q(1), Q(3, 2)):
            lhs = Geometry.metric_jacobian(m @ n, t)
            rhs = Geometry.metric_jacobian(m, n.at(t))*Geometry.metric_jacobian(n, t)
            assert lhs == rhs
    assert Geometry.metric_jacobian(L, 0) == Q(1, 2)
    assert Geometry.metric_jacobian(R, 1) == Q(2, 5)
    rotation_matrix = matrices[-1]
    for t in (Q(0), Q(1, 3), Q(1)):
        assert Geometry.metric_jacobian(rotation_matrix, t) == 1

    # Check the coordinate swap in source/output commutation and residual maps.
    e = Matrix2(3, 4, 1, 1)
    swap = Matrix2(0, 1, 1, 0)
    b = e @ swap
    z = Matrix2(7, 30, 0, 15)
    a = Matrix2(2, 18, 0, 6)
    residual = b.inverse() @ a
    for g in (L, R):
        h = swap @ g @ swap
        assert (e @ g) @ swap == b @ h
        assert (h.inverse() @ residual) @ z == h.inverse() @ (residual @ z)
    assert R.inverse().at(Q(1, 3)) == Q(1, 2)
    assert L.inverse().at(Q(5, 3)) == Q(2, 3)
    # Exact residual-to-radix identity, without an exponential or a chosen pi value.
    for certificate in primary["arrow_certificates"][::17]:
        aa, bb, cc, dd = certificate["endpoints"]
        for t in (Q(1, 3), Q(5, 2)):
            x = (aa+cc*t)/(bb+dd*t)
            for j in (0, 1, 5):
                integer = (16**j*x).numerator//(16**j*x).denominator
                assert 16**j*x-integer == ((16**j*aa-integer*bb)
                    +(16**j*cc-integer*dd)*t)/(bb+dd*t)

    # Complete output run lengths agree with a different coding algorithm.
    cf = certified_cf(independent, len(primary["runs"])+2)
    global_runs = [3]+[r["count"] for r in primary["runs"]]
    global_runs[1] += 1  # Initial global word RRRL already used one L.
    assert global_runs[:-1] == cf[:len(global_runs)-1]
    assert global_runs[-1] <= cf[len(global_runs)-1]

    mutations = []
    for name, mutate in (
        ("flipped_arrow", lambda x: x["arrow_certificates"][0].__setitem__("arrow", "R")),
        ("corrupted_denominator", lambda x: x["arrow_certificates"][20]["endpoints"].__setitem__(1, 2)),
        ("unearned_precision", lambda x: x["arrow_certificates"][20].__setitem__("source_stage", 0)),
        ("altered_mediant", lambda x: x["arrow_certificates"][0].__setitem__("mediant", "3")),
    ):
        changed = deepcopy(primary)
        mutate(changed)
        try:
            verify_trace(changed, source_intervals, independent)
        except AssertionError:
            mutations.append({"mutation": name, "verdict": "REJECTED"})
        else:
            raise AssertionError("Mutation survived: "+name)
    assert e @ L != L @ e and e @ R != R @ e
    assert [Q((L @ e).a, (L @ e).c), Q((L @ e).b, (L @ e).d)] == [4, 5]
    assert [Q((R @ e).a, (R @ e).c), Q((R @ e).b, (R @ e).d)] == [Q(3, 4), Q(4, 5)]
    mutations.append({"mutation": "left_instead_of_right_endpoint_action", "verdict": "REJECTED"})
    assert Q(4) > independent[1]  # Flattening 4/(1+t^2) to 4 destroys the metric.
    assert 2*independent[0] > independent[1]  # Circumference vs diameter ratio.
    mutations.extend({"mutation": name, "verdict": "REJECTED"} for name in (
        "erased_arclength_density", "missing_diameter_normalization"))

    # Radians/turns mutation: geometric pi radians is half a turn.
    wrong_phases = [(16**j*Q(1, 2)) % 1 for j in range(12)]
    assert wrong_phases == [Q(1, 2)]+[Q(0)]*11
    assert Q(1, 8) < independent[0]-3 < independent[1]-3 < Q(1, 6)
    mutations.append({"mutation": "pi_radians_substituted_for_pi_turns", "verdict": "REJECTED"})

    # Analytic countermodel in HOSTILE_OBSERVER.md; these counts are finite only.
    positions, factorial, k = [], 1, 1
    while factorial <= 1000:
        positions.append(factorial)
        k += 1
        factorial *= k
    assert positions == [1, 2, 6, 24, 120, 720]

    try:
        finite_run(1, 1, "typo")
    except ValueError:
        pass
    else:
        raise AssertionError("Unknown source silently accepted")
    for base in (2, 3, 10, 16, 36):
        for entry in digit_certificates(MatrixCircleSource(), 8, base):
            x = independent[0]*base**entry["exponent"]
            y = independent[1]*base**entry["exponent"]
            assert x.numerator//x.denominator == y.numerator//y.denominator == entry["floor"]

    # Library use must not silently depend on a permissive decimal display cap.
    previous_cap = sys.get_int_max_str_digits()
    try:
        sys.set_int_max_str_digits(640)
        long_result = finite_run(0, 600, "matrix")
        negative_text = rational_text(Q(-10**1000, 3))
        assert len(long_result["hexadecimal"]) == 602
        assert sys.get_int_max_str_digits() == 640
    finally:
        sys.set_int_max_str_digits(previous_cap)
    assert Q(negative_text) == Q(-10**1000, 3)

    # Rational majorant for the proved source-stage -> epoch precision theorem.
    # No trigonometric sampling is used to establish the bound.
    precision_checks = 0
    budgets = beta_intervals(8*32+5)
    for epoch in (1, 2, 4, 8, 16, 32):
        for extra_bits in (0, 1, 5):
            k = 8*epoch+extra_bits
            width = budgets[k][1]-budgets[k][0]
            bound_per_h = Q(4, 15*epoch)*width*(16**(2*epoch-1)-16**(epoch-1))
            assert bound_per_h < Q(1, 60*epoch*2**extra_bits)
            precision_checks += 1

    root = Path(__file__).parent
    production = root / "circle_line_observer.py"
    syntax = ast.parse(production.read_text())
    assert not any(isinstance(node, ast.Constant) and isinstance(node.value, float)
                   for node in ast.walk(syntax))
    imports = sorted({node.module for node in ast.walk(syntax)
                      if isinstance(node, ast.ImportFrom)})
    assert not any(isinstance(node, ast.Attribute) and node.attr in ("pi", "sin", "cos", "tan")
                   for node in ast.walk(syntax))
    source_hashes = {name: sha256((root/name).read_bytes()).hexdigest()
                     for name in ("circle_line_observer.py", "observer_probe.py")}
    return {
        "status": "PASS", "scope": "finite exact checks; universal proofs are in notes",
        "python": platform.python_version(), "source_sha256": source_hashes,
        "arrows_per_source": 512, "hexadecimal_fractional_digits_per_source": 64,
        "two_geometric_sources_agree": True, "independent_bbp_terms": 180,
        "matrix_source_stages": primary["final_source_stage"],
        "matrix_source_stages_for_arrows": primary["arrow_source_stage"],
        "rotation_source_stages": alternate["final_source_stage"],
        "word_sha256": sha256(primary["word"].encode()).hexdigest(),
        "exact_circle_incidence_and_speed_parameters": len(parameters),
        "conic_lift_maps": len(matrices), "conic_composition_pairs": len(matrices)**2,
        "metric_cocycle_checks": 8*8*4, "rotation_enclosures": 64,
        "epoch_precision_majorant_checks": precision_checks,
        "imported_api_decimal_cap_640_control": "PASS; 600 hexadecimal digits returned",
        "riemann_checks": riemann, "mutations": mutations,
        "independent_cf_coefficients": cf,
        "hexadecimal": primary["hexadecimal"], "lr_initial_runs": primary["runs"][:12],
        "countermodel_prefix": {"digits": 1000, "one_positions": positions, "zero_count": 994},
        "production_from_imports": imports,
        "truth_boundary": "No normality, RH, cancellation, or infinite physical run claimed",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = main()
    rendered = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")
