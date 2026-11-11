#!/usr/bin/env python3
"""Independent constructive-period audit for the Round-V observer.

Run next to aperiodic_observer.py:
    python cycle_independent_probe.py --output cycle_independent_receipt.json

The guarded period section reproduces the declared-before-observation audit.
The synthetic section includes the corrected orientation of one invalid test
fixture; the original failure and correction are retained in the receipt.
Tuple arithmetic below deliberately avoids the production matrix, polynomial,
and escape helpers when calculating expected results. The source and preceding
observer are shared provenance, not independent proofs of the circle identity.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import reduce
import hashlib
import importlib.util
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys

sys.dont_write_bytecode = True

FRESH = [(2309, 1), (2371, 7), (3001, 19), (4003, 31)]
CONTROLS = [(0, 4), (25, 5), (315, 2), (320, 7)]
EXTRA = 8
CHARTS = [(3, 1, 4, 1), (17, 5, 24, 7),
          (333, 106, 355, 113), (688, 219, 355, 113)]


def mul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h


def word_product(word):
    z = (1, 0, 0, 1)
    for letter in word:
        z = mul(z, (1, 1, 0, 1) if letter == "L" else (1, 0, 1, 1))
    return z


def normalize(coefficients):
    divisor = reduce(gcd, coefficients)
    result = tuple(t//divisor for t in coefficients)
    return result if next(t for t in result if t) > 0 else tuple(-t for t in result)


def expected_polynomial(e, word):
    a, b, c, d = e
    if set(word) == {"L"}:
        return normalize((0, b, -a))
    if set(word) == {"R"}:
        return normalize((0, d, -c))
    A, B, C, D = mul(mul((a, c, b, d), word_product(word)), (-d, c, b, -a))
    return normalize((C, D-A, -B))


def advance(e, word):
    a, b, c, d = e
    for letter in word:
        if letter == "L":
            c, d = a+c, b+d
        else:
            a, b = a+c, b+d
    return a, b, c, d


def width(e):
    return Q(1, e[1]*e[3])


def polynomial_value(coefficients, x):
    a, b, c = coefficients
    return a*x*x+b*x+c


def expected_range(coefficients, lower, upper):
    values = [polynomial_value(coefficients, lower),
              polynomial_value(coefficients, upper)]
    a, b, _ = coefficients
    if a:
        vertex = -Q(b, 2*a)
        if lower <= vertex <= upper:
            values.append(polynomial_value(coefficients, vertex))
    return min(values), max(values)


def verify_plan(plan):
    n, p = plan["start"], plan["period"]
    word = plan["candidate_word"]
    assert len(word) == p and len(plan["prefix"]) == n
    assert plan["construction_output_length"] == n+p
    e = advance((3, 1, 4, 1), plan["prefix"])
    assert list(e) == plan["prefix_bracket"]
    coefficients = expected_polynomial(e, word)
    assert list(coefficients) == plan["fixed_polynomial"]
    lower, upper = map(Q, plan["source_interval"])
    image = expected_range(coefficients, lower, upper)
    assert list(image) == list(map(Q, plan["polynomial_range"]))
    assert image[0] > 0 or image[1] < 0
    epsilon = min(abs(image[0]), abs(image[1]))
    a, b, _ = coefficients
    derivative = max(abs(2*a*Q(e[0], e[1])+b), abs(2*a*Q(e[2], e[3])+b))
    delta = epsilon/derivative
    assert epsilon == Q(plan["polynomial_gap"])
    assert derivative == Q(plan["derivative_bound_on_prefix"])
    assert delta == Q(plan["root_distance_lower_bound"])
    assert 0 < delta <= width(e)
    r, escaped, previous = 0, e, None
    while width(escaped) >= delta:
        previous = escaped
        escaped = advance(escaped, word)
        r += 1
        assert r < 10000
    assert r == plan["escape_blocks"]
    assert list(escaped) == plan["escaped_cylinder"]
    assert width(escaped) == Q(plan["escaped_width"])
    assert width(previous) == Q(plan["previous_width"])
    assert width(escaped) < delta <= width(previous)
    assert plan["last_output_index_to_read"] == n+r*p-1
    assert plan["period_witness_start_at_most"] == n+(r-1)*p-1
    if len(set(word)) == 2:
        assert width(escaped) <= width(e)/5**r
        assert Q(plan["rational_mixed_width_bound"]) == width(e)/5**r
    else:
        _, bb, _, dd = e
        denominator = bb*(dd+r*p*bb) if word[0] == "L" else dd*(bb+r*p*dd)
        assert width(escaped) == Q(1, denominator)


def load_module(path):
    spec = importlib.util.spec_from_file_location("independent_aperiodic_audit", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def audit(module_path):
    before_hash = hashlib.sha256(module_path.read_bytes()).hexdigest()
    m = load_module(module_path)
    original = m.ProductiveObserver

    class Guarded(original):
        limit = None
        instances = []

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.guard = self.limit
            self.instances.append(self)

        def next_arrow(self):
            assert len(self.word) < self.guard, "Preparation requested an arrow beyond N+p"
            return super().next_arrow()

    print(json.dumps({"phase": "declared_cases", "fresh": FRESH, "known": CONTROLS,
                      "extra": EXTRA, "module_sha256": before_hash}), flush=True)
    prepared = []
    for n, p in CONTROLS+FRESH:
        Guarded.limit = n+p
        m.ProductiveObserver = Guarded
        try:
            plan = m.prepare_period(n, p, extra=EXTRA)
        finally:
            m.ProductiveObserver = original
        observer = Guarded.instances[-1]
        assert len(observer.word) == n+p
        verify_plan(plan)
        prepared.append(plan)
        print(json.dumps({"phase": "prepared", "N": n, "p": p,
                          "word": plan["candidate_word"], "stage": plan["source_stage"],
                          "r": plan["escape_blocks"], "B": plan["last_output_index_to_read"],
                          "emitted_arrows": len(observer.word)}), flush=True)

    rows, prefixes = [], []
    for plan in prepared:
        n, p = plan["start"], plan["period"]
        result = m.reject_period(n, p, extra=EXTRA)
        assert result["plan"] == plan
        witness = result["witness"]
        word = witness["output_prefix"]
        j, i = witness["different_output_index"], witness["comparison_start"]
        assert i == j-p and i >= n and n+p <= j <= plan["last_output_index_to_read"]
        assert i <= plan["period_witness_start_at_most"]
        assert len(word) == j+1 and word[i] != word[j]
        assert all(word[k] == word[k-p] for k in range(n+p, j))
        assert all(word[k] == plan["candidate_word"][(k-n) % p] for k in range(n, j))
        assert word[j] != plan["candidate_word"][(j-n) % p]
        assert witness["earlier_letter"] == word[i] and witness["later_letter"] == word[j]
        assert witness["is_first_period_mismatch"] is True
        row = {"start": n, "period": p, "candidate": plan["candidate_word"],
               "fresh_when_declared": (n, p) in FRESH,
               "source_stage": plan["source_stage"],
               "polynomial_degree": 2 if plan["fixed_polynomial"][0] else 1,
               "preparation_output_length": plan["construction_output_length"],
               "minimal_escape_blocks": plan["escape_blocks"],
               "last_output_index_to_read": plan["last_output_index_to_read"],
               "actual_first_mismatch_index": j, "actual_period_witness_start": i}
        rows.append(row)
        prefixes.append(word)
        print(json.dumps({"phase": "rejected", **row}), flush=True)

    baseline = m.circle.SternBrocotObserver(m.circle.MatrixCircleSource())
    baseline_word = "".join(baseline.next_arrow()["arrow"]
                            for _ in range(max(map(len, prefixes))))
    assert all(baseline_word[:len(word)] == word for word in prefixes)

    # This is the accidentally reversed initial fixture, preserved as a control.
    invalid_fixture = (355, 113, 688, 219)
    try:
        m.Bracket(*invalid_fixture)
    except ValueError:
        invalid_fixture_rejected = True
    else:
        raise AssertionError("Invalid Farey orientation was accepted")

    algebra_cases = strict_equality_cases = 0
    for e in CHARTS:
        bracket = m.Bracket(*e)
        for length in range(1, 8):
            for characters in product("LR", repeat=length):
                word = "".join(characters)
                assert tuple(m.period_polynomial(bracket, word)) == expected_polynomial(e, word)
                expected = advance(e, word*3)
                actual = bracket.apply(m.matrix_power(m.word_matrix(word), 3))
                assert actual.values() == list(expected)
                if set(word) == {"L"}:
                    assert width(expected) == Q(1, e[1]*(e[3]+3*length*e[1]))
                elif set(word) == {"R"}:
                    assert width(expected) == Q(1, e[3]*(e[1]+3*length*e[3]))
                else:
                    assert width(advance(e, word)) <= width(e)/5
                algebra_cases += 1
                if length <= 4:
                    gap = width(expected)
                    r, escaped, previous = m.exact_escape_blocks(bracket, word, gap)
                    assert r == 4 and previous.width == gap and escaped.width < gap
                    strict_equality_cases += 1
    assert algebra_cases == 1016 and strict_equality_cases == 120

    assert m.polynomial_range((1, -7, 12), Q(3), Q(4)) == (-Q(1, 4), Q(0))
    assert m.polynomial_range((4, -28, 48), Q(13, 4), Q(15, 4)) == (-Q(1), -Q(3, 4))
    assert m.polynomial_range((16, -112, 195), Q(3), Q(4)) == (-Q(1), Q(3))
    assert m.polynomial_range((0, 2, -7), Q(3), Q(4)) == (-Q(1), Q(1))

    rotation_rows = []
    for n, p in [(0, 4), (315, 2)]:
        result = m.reject_period(n, p, extra=EXTRA, source="rotations")
        plan, witness = result["plan"], result["witness"]
        verify_plan(plan)
        word = witness["output_prefix"]
        j = witness["different_output_index"]
        assert baseline_word[:len(word)] == word
        assert witness["comparison_start"] == j-p
        assert all(word[k] == word[k-p] for k in range(n+p, j))
        assert word[j] != word[j-p]
        rotation_rows.append({"start": n, "period": p, "source_stage": plan["source_stage"],
                              "minimal_escape_blocks": plan["escape_blocks"],
                              "last_output_index_to_read": plan["last_output_index_to_read"],
                              "actual_first_mismatch_index": j,
                              "actual_period_witness_start": j-p})

    for n, p, extra in [(-1, 1, 8), (0, 0, 8), (0, 1, -1)]:
        try:
            m.prepare_period(n, p, extra)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid period request was accepted")

    after_hash = hashlib.sha256(module_path.read_bytes()).hexdigest()
    assert after_hash == before_hash, "Module changed while the audit was running"
    return {
        "schema": "succ.independent-cycle-audit.v1", "status": "PASS",
        "module_sha256": before_hash,
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "preparation_output_guard": "Exactly N+p arrows; any further next_arrow call raises",
        "expectation_method": "Independent integer tuple matrices, exact rational ranges, linear cylinder scan",
        "extra_source_refinements": EXTRA, "matrix_cases": rows,
        "rotation_cases": rotation_rows,
        "baseline_matched_output_count": len(baseline_word),
        "synthetic_word_lengths": [1, 7], "synthetic_charts": CHARTS,
        "synthetic_algebra_cases": algebra_cases,
        "strict_equality_deadline_cases": strict_equality_cases,
        "exact_polynomial_range_controls": 4, "invalid_request_controls": 3,
        "invalid_farey_fixture_rejected": invalid_fixture_rejected,
        "failure_correction_history": [{
            "phase": "Initial exploratory combined invocation, after eight period cases and baseline match",
            "failure": "Fourth synthetic chart was reversed; Bracket correctly raised ValueError",
            "invalid_chart": invalid_fixture, "invalid_bc_minus_ad": -1,
            "corrected_chart": CHARTS[3], "corrected_bc_minus_ad": 1,
            "result": "Corrected synthetic suite passed; no production-code change"}],
        "scope": [
            "Four fresh cases were fixed before their words were observed in this bearing.",
            "Each preparation had its own source and output guard; all plans were fixed before rejection calls.",
            "The two fresh starts 2309 and 2371 unexpectedly share the run ending at 2693.",
            "This finite audit is corroboration of the proof interface, not a proof of universal aperiodicity.",
            "Baseline and staged observer share the circle source; they are separate emission implementations."
        ]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", type=Path, default=Path(__file__).with_name("aperiodic_observer.py"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("cycle_independent_receipt.json"))
    args = parser.parse_args()
    receipt = audit(args.module)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"phase": "complete", "status": receipt["status"],
                      "receipt": str(args.output), "module_sha256": receipt["module_sha256"],
                      "algebra_cases": receipt["synthetic_algebra_cases"],
                      "baseline_matched_outputs": receipt["baseline_matched_output_count"]}), flush=True)


if __name__ == "__main__":
    main()
