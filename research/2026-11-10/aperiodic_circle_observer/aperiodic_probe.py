#!/usr/bin/env python3
"""Independent rational certificate replay and hostile controls for Round V.

The checker uses scalar source recurrences and tuple matrices, not the
production Matrix2/Bracket/polynomial helpers. It checks finite certificates;
the all-time theorems and classical imports remain separate proof obligations.
Run: python aperiodic_probe.py --output audit_receipt.json
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path
import subprocess
import sys
from time import perf_counter

import aperiodic_observer as subject


BETA = "circle_beta_matrix"
ROTATION = "circle_345_rotations"
IDENTITY = (1, 0, 0, 1)
INITIAL = (3, 1, 4, 1)
# Declared before the corresponding future outputs are requested in this probe.
HOLDOUTS = ((1601, 11), (2333, 17), (3072, 23))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def natural(value, label, minimum=0):
    require(type(value) is int and value >= minimum, label+" must be an integer in its declared domain")
    return value


def integer_vector(values, label):
    require(all(type(v) is int for v in values), label+" must have integer entries")


class ScalarSource:
    """Independent affine recurrence or paired rational arc-integral sums."""
    def __init__(self, name=BETA):
        self.name, self.stage = name, 0
        self.offset, self.scale = Q(0), Q(1)
        self.partial = Q(0)
        self.lower, self.upper = Q(3), Q(4)
        if name == ROTATION:
            self.refine()
        elif name != BETA:
            raise ValueError("Unknown scalar source")

    def refine(self):
        self.stage += 1
        k = self.stage
        if self.name == BETA:
            self.offset += 2*self.scale
            self.scale *= Q(k, 2*k+1)
            self.lower = self.offset+3*self.scale
            self.upper = self.offset+4*self.scale
        else:
            positive, negative = 4*k-3, 4*k-1
            self.partial += sum((Q(1, positive*q**positive) for q in (2, 3)), Q(0))
            self.upper = 4*self.partial
            self.partial -= sum((Q(1, negative*q**negative) for q in (2, 3)), Q(0))
            self.lower = 4*self.partial


SOURCE_CACHE = {}


def source_interval(name, stage):
    if name not in SOURCE_CACHE:
        s = ScalarSource(name)
        SOURCE_CACHE[name] = (s, {s.stage: (s.lower, s.upper)})
    s, cache = SOURCE_CACHE[name]
    while s.stage < stage:
        s.refine()
        cache[s.stage] = (s.lower, s.upper)
    return cache[stage]


def advance(chart, arrow, count=1):
    a, b, c, d = chart
    if arrow == "L":
        return a, b, c+count*a, d+count*b
    if arrow == "R":
        return a+count*c, b+count*d, c, d
    raise AssertionError("Invalid branch")


class Reference:
    def __init__(self, name=ROTATION):
        self.source = ScalarSource(name)
        self.charts, self.word = [INITIAL], []

    def ensure(self, count):
        while len(self.word) < count:
            a, b, c, d = self.charts[-1]
            threshold = Q(a+c, b+d)
            while self.source.lower < threshold < self.source.upper:
                self.source.refine()
            arrow = "L" if self.source.upper <= threshold else "R"
            self.word.append(arrow)
            self.charts.append(advance(self.charts[-1], arrow))


def mul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h


def power(matrix, n):
    natural(n, "matrix exponent")
    answer = IDENTITY
    while n:
        if n % 2:
            answer = mul(answer, matrix)
        matrix = mul(matrix, matrix)
        n //= 2
    return answer


def word_matrix(word):
    value = IDENTITY
    for arrow in word:
        require(arrow in "LR", "invalid word alphabet")
        value = mul(value, (1, 1, 0, 1) if arrow == "L" else (1, 0, 1, 1))
    return value


def cylinder(chart, word, copies):
    a, b, c, d = chart
    x, y, z, t = mul((a, c, b, d), power(word_matrix(word), copies))
    return x, z, y, t


def width(chart):
    a, b, c, d = chart
    require(b > 0 and d > 0 and b*c-a*d == 1, "invalid Farey chart")
    return Q(1, b*d)


def poly(chart, word):
    a, b, c, d = chart
    if set(word) == {"L"}:
        values = (0, b, -a)
    elif set(word) == {"R"}:
        values = (0, d, -c)
    else:
        A, B, C, D = mul(mul((a, c, b, d), word_matrix(word)), (-d, c, b, -a))
        values = (C, D-A, -B)
    divisor = gcd(*values)
    require(divisor != 0, "zero polynomial")
    sign = 1 if next(v for v in values if v) > 0 else -1
    return tuple(sign*v//divisor for v in values)


def poly_range(coefficients, lo, hi):
    a, b, c = coefficients
    points = [lo, hi]
    if a and lo <= Q(-b, 2*a) <= hi:
        points.append(Q(-b, 2*a))
    values = [a*x*x+b*x+c for x in points]
    return min(values), max(values)


def text_pair(values):
    return tuple(Q(v) for v in values)


def verify_plan(plan, reference=None):
    require(plan["schema"] == "succ.aperiodic-period.v1", "plan schema")
    n, p = natural(plan["start"], "start"), natural(plan["period"], "period", 1)
    for field in ("construction_output_length", "source_stage", "first_separation_stage", "extra_source_refinements",
                  "escape_blocks", "last_output_index_to_read", "period_witness_start_at_most"):
        natural(plan[field], field)
    for field in ("prefix_bracket", "fixed_polynomial", "escaped_cylinder"):
        integer_vector(plan[field], field)
    reference = reference or Reference()
    reference.ensure(n+p)
    require(plan["prefix"] == "".join(reference.word[:n]), "authenticated prefix")
    word = "".join(reference.word[n:n+p])
    require(plan["candidate_word"] == word, "authenticated candidate block")
    require(plan["construction_output_length"] == n+p, "no future output during preparation")
    chart = reference.charts[n]
    require(tuple(plan["prefix_bracket"]) == chart, "prefix chart")
    coefficients = poly(chart, word)
    require(tuple(plan["fixed_polynomial"]) == coefficients, "global fixed polynomial")
    lo, hi = source_interval(plan["source"], plan["source_stage"])
    require(text_pair(plan["source_interval"]) == (lo, hi), "source interval")
    image = poly_range(coefficients, lo, hi)
    require(text_pair(plan["polynomial_range"]) == image, "exact polynomial range")
    require(image[0] > 0 or image[1] < 0, "polynomial excludes zero")
    epsilon = min(abs(x) for x in image)
    require(Q(plan["polynomial_gap"]) == epsilon, "polynomial gap")
    a, b, c, d = chart
    u, v, _ = coefficients
    derivative = max(abs(2*u*Q(a, b)+v), abs(2*u*Q(c, d)+v))
    require(derivative > 0 and Q(plan["derivative_bound_on_prefix"]) == derivative, "derivative bound")
    gap = epsilon/derivative
    require(Q(plan["root_distance_lower_bound"]) == gap, "root gap")
    copies = plan["escape_blocks"]
    require(copies >= 2, "observed first block cannot escape")
    escaped, previous = cylinder(chart, word, copies), cylinder(chart, word, copies-1)
    require(tuple(plan["escaped_cylinder"]) == escaped, "hypothetical escaped cylinder")
    require(Q(plan["escaped_width"]) == width(escaped) < gap, "escape width")
    require(Q(plan["previous_width"]) == width(previous) >= gap, "minimal escape block count")
    deadline = n+copies*p-1
    require(plan["last_output_index_to_read"] == deadline, "inclusive deadline index")
    require(plan["period_witness_start_at_most"] == deadline-p, "witness deadline index")
    first, extra = plan["first_separation_stage"], plan["extra_source_refinements"]
    require(extra >= 0 and first+extra == plan["source_stage"], "refinement accounting")
    initial = Reference(plan["source"])
    initial.ensure(n+p)
    require(first >= initial.source.stage, "source clock cannot rewind")
    first_image = poly_range(coefficients, *source_interval(plan["source"], first))
    require(first_image[0] > 0 or first_image[1] < 0, "first searched separation stage")
    if first > initial.source.stage:
        previous_image = poly_range(coefficients, *source_interval(plan["source"], first-1))
        require(previous_image[0] <= 0 <= previous_image[1], "minimal searched source stage")
    mixed = len(set(word)) == 2
    require(plan["kind"] == ("mixed_hyperbolic" if mixed else "single_letter_parabolic"), "period kind")
    uniform = plan["uniform_classical_budget"]
    for field in ("polynomial_height_with_floor", "height_bit_length", "root_bound_exponent", "source_sign_stage_sufficient"):
        natural(uniform[field], field, 1)
    H = max(16, *(abs(v) for v in coefficients))
    exponent, bits = 2**43+1, H.bit_length()
    budget = exponent*bits+4
    require(uniform["classical_import"] == "Waldschmidt1978 Corollary3.2; conservative degree2 corollary", "classical theorem provenance")
    require(uniform["polynomial_height_with_floor"] == H, "uniform height")
    require(uniform["height_bit_length"] == bits and uniform["root_bound_exponent"] == exponent, "uniform exponents")
    require(uniform["source_sign_stage_sufficient"] == budget, "uniform source budget")
    if mixed:
        natural(uniform["escape_blocks_sufficient"], "uniform blocks", 1)
        natural(uniform["last_output_index_sufficient"], "uniform output index")
        require(Q(plan["rational_mixed_width_bound"]) == width(chart)/5**copies, "mixed rational width bound")
        require(width(escaped) < Q(plan["rational_mixed_width_bound"]), "mixed contraction")
        require(uniform["escape_blocks_sufficient"] == budget, "uniform mixed blocks")
        require(uniform["last_output_index_sufficient"] == n+p*budget-1, "uniform mixed index")
    else:
        integer_vector(uniform["escape_blocks_symbolic"].values(), "symbolic pure bound")
        require(uniform["escape_blocks_symbolic"] == {"coefficient": 9, "base": H, "exponent": exponent}, "symbolic pure budget")
    return reference


def verify_period(result, reference=None):
    plan, witness = result["plan"], result["witness"]
    reference = verify_plan(plan, reference)
    n, p = plan["start"], plan["period"]
    for field in ("comparison_start", "different_output_index", "output_source_stage"):
        natural(witness[field], field)
    j = witness["different_output_index"]
    require(n+p <= j <= plan["last_output_index_to_read"], "witness within deadline")
    require(witness["comparison_start"] == j-p >= n, "p-spaced comparison")
    reference.ensure(j+1)
    word = "".join(reference.word[:j+1])
    require(witness["output_prefix"] == word, "independent output replay")
    require(witness["earlier_letter"] == word[j-p] and witness["later_letter"] == word[j], "witness letters")
    require(word[j-p] != word[j], "actual period mismatch")
    require(all(word[k] == word[k-p] for k in range(n+p, j)), "first mismatch minimality")
    require(witness["is_first_period_mismatch"] is True, "witness claim")
    require(witness["output_source_stage"] >= plan["source_stage"], "witness source clock cannot rewind")
    lo, hi = source_interval(plan["source"], witness["output_source_stage"])
    require(text_pair(witness["output_source_interval"]) == (lo, hi), "witness source")
    a, b, c, d = reference.charts[j+1]
    require(Q(a, b) <= lo < hi <= Q(c, d), "witness source authenticates final cylinder")
    return j-p


def residual(chart, x):
    a, b, c, d = chart
    require(Q(a, b) < x < Q(c, d), "residual chart domain")
    return (b*x-a)/(c-d*x)


def verify_run(record, expected_chart, expected_start, expected_run):
    for field in ("run", "length", "start", "stop", "source_stage", "expanded_future_arrows_used"):
        natural(record[field], field)
    integer_vector(record["bracket_before"], "run input chart")
    integer_vector(record["bracket_after"], "run output chart")
    require(tuple(record["bracket_before"]) == expected_chart, "run input chart")
    require(record["run"] == expected_run and record["start"] == expected_start, "run indices")
    require(record["expanded_future_arrows_used"] == 0, "compressed construction scope")
    lo, hi = source_interval(record["source"], record["source_stage"])
    require(text_pair(record["source_interval"]) == (lo, hi), "run source")
    zl, zu = residual(expected_chart, lo), residual(expected_chart, hi)
    require(text_pair(record["residual_interval"]) == (zl, zu), "run residual interval")
    if record["arrow"] == "R":
        flo, fhi = zl, zu
    else:
        require(record["arrow"] == "L", "run branch")
        flo, fhi = 1/zu, 1/zl
    require(text_pair(record["floor_interval"]) == (flo, fhi), "run floor interval")
    count = record["length"]
    require(count >= 1 and flo.numerator//flo.denominator == count == fhi.numerator//fhi.denominator, "exact maximal run length")
    require(record["stop"] == expected_start+count, "run stop")
    chart = advance(expected_chart, record["arrow"], count)
    require(tuple(record["bracket_after"]) == chart, "compressed chart update")
    return chart, record["stop"]


def verify_pinbed(record):
    require(record["schema"] == "succ.rational-residual-pinbed.v1", "pinbed schema")
    require(record["optimality_scope"] == "m-1 fixed nonadaptive rational threshold probes for m distinct ordered states", "threshold optimality scope")
    indices = record["requested_states"]
    for n in indices:
        natural(n, "pinbed state index")
    natural(record["source_stage"], "pinbed source stage")
    require(indices and min(indices) >= 0 and len(set(indices)) == len(indices), "pinbed indices")
    reference = Reference()
    reference.ensure(max(indices))
    require(record["output_prefix"] == "".join(reference.word), "pinbed word")
    lo, hi = source_interval(record["source"], record["source_stage"])
    require(text_pair(record["source_interval"]) == (lo, hi), "pinbed source")
    states = record["states_in_value_order"]
    require(len(states) == len(indices) and {x["index"] for x in states} == set(indices), "pinbed state set")
    thresholds = [Q(q) for q in record["thresholds"]]
    require(len(thresholds) == len(indices)-1, "threshold count")
    intervals = []
    for state in states:
        natural(state["index"], "pinbed record index")
        integer_vector(state["bracket"], "pinbed chart")
        integer_vector(state["lower_cut_signature"], "cut signature")
        chart = reference.charts[state["index"]]
        require(tuple(state["bracket"]) == chart, "pinbed chart")
        interval = residual(chart, lo), residual(chart, hi)
        require(text_pair(state["residual_interval"]) == interval, "pinbed residual range")
        require(state["lower_cut_signature"] == [int(q < interval[0]) for q in thresholds], "cut signature")
        require(all(not interval[0] <= q <= interval[1] for q in thresholds), "decisive threshold")
        intervals.append(interval)
    for k, (left, right) in enumerate(zip(intervals, intervals[1:])):
        require(left[1] < thresholds[k] < right[0], "ordered separating threshold")
        require(thresholds[k] == (left[1]+right[0])/2, "threshold construction")
    require(len({tuple(x["lower_cut_signature"]) for x in states}) == len(states), "distinct rational signatures")


class QuadraticSource:
    name = "quadratic_control"
    def __init__(self):
        self.stage = 0
        self.refine()

    def refine(self):
        self.stage += 1
        scale = 2**self.stage
        root = isqrt(5*scale*scale)
        self.lower = (9-Q(root+1, scale))/2
        self.upper = (9-Q(root, scale))/2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("audit_receipt.json"))
    args = parser.parse_args()
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    began = perf_counter()
    report = {"schema": "succ.aperiodic-audit.v1", "status": "RUNNING",
              "scope": "Finite independent replay; proofs and named classical theorem establish universal claims",
              "source_implementation_sha256": sha256(subject.SOURCE_PATH.read_bytes()).hexdigest(),
              "observer_sha256": sha256(Path(subject.__file__).read_bytes()).hexdigest(),
              "probe_sha256": sha256(Path(__file__).read_bytes()).hexdigest()}

    # Every candidate is prepared before its witness search. The fixed holdouts
    # receive fresh reference observers; their future is not read to set a bound.
    cases = [(n, p) for n in (0, 1, 6, 21, 22, 25, 100, 314) for p in (1, 2, 5, 7, 13)]
    period_rows, certificates = [], []
    for n, p in cases+list(HOLDOUTS):
        plan = subject.prepare_period(n, p)
        plan_digest = sha256(json.dumps(plan, sort_keys=True).encode()).hexdigest()
        reference = Reference()
        verify_plan(plan, reference)
        result = subject.reject_period(n, p)
        require(result["plan"] == plan, "precommitted plan changed during execution")
        witness_start = verify_period(result, reference)
        certificates.append(result)
        period_rows.append({"start": n, "period": p, "candidate_word": plan["candidate_word"],
                            "source_stage": plan["source_stage"], "escape_blocks": plan["escape_blocks"],
                            "read_deadline": plan["last_output_index_to_read"], "witness_start": witness_start,
                            "mismatch_index": result["witness"]["different_output_index"],
                            "declared_holdout": (n, p) in HOLDOUTS, "prepared_plan_sha256": plan_digest})
    for n, p in ((0, 7), (22, 1), (315, 13)):
        verify_period(subject.reject_period(n, p, source="rotations"))
    report["periods"] = {"matrix_candidates": len(period_rows), "rotation_candidates": 3, "rows": period_rows}

    observer = subject.ProductiveObserver()
    previous, event_count, source_events = None, 0, 0
    while len(observer.word) < 1024:
        event = observer.next_transition()
        before, after, factor = (Q(event[k]) for k in ("potential_before", "potential_after", "decrease_factor"))
        require(0 < after < before and after == before*factor, "counter-free strict potential")
        if previous is not None:
            require(previous == before, "potential continuity")
        previous = after
        event_count += 1
        source_events += event["kind"] == "source"
    independent = Reference()
    independent.ensure(1024)
    require(observer.word == independent.word, "productive beta/rotation agreement")
    report["semantic_transitions"] = {"outputs": 1024, "transitions": event_count, "source_refinements": source_events,
                                      "word_sha256": sha256("".join(observer.word).encode()).hexdigest()}

    runner, chart, position = subject.RunObserver(), INITIAL, 0
    runs = []
    for k in range(1, 49):
        record = runner.next_run()
        chart, position = verify_run(record, chart, position, k)
        runs.append(record)
    expanded = "".join(r["arrow"]*r["length"] for r in runs)
    independent.ensure(len(expanded)+1)
    require(expanded == "".join(independent.word[:len(expanded)]), "run expansion agrees with independent source")
    for record in runs:
        require(independent.word[record["stop"]] != record["arrow"], "maximal run has a next-letter change")
    require(runs[3]["arrow"] == "R" and runs[3]["length"] == 292 and runs[3]["source_stage"] == 28, "R292 certificate")
    report["maximal_runs"] = {"runs": len(runs), "expanded_arrows": len(expanded),
                              "word_sha256": sha256(expanded.encode()).hexdigest(),
                              "initial_lengths": [r["length"] for r in runs[:12]],
                              "R292_source_stage": runs[3]["source_stage"],
                              "branch_labels_alternate": all(a["arrow"] != b["arrow"] for a, b in zip(runs, runs[1:]))}

    pins = subject.rational_pinbed([0, 6, 21, 22, 100, 314, 512, 1024])
    verify_pinbed(pins)
    singleton = subject.rational_pinbed([0])
    verify_pinbed(singleton)
    report["rational_probes"] = {"states": len(pins["requested_states"]), "thresholds": len(pins["thresholds"]),
                                  "source_stage": pins["source_stage"], "singleton_zero_probe_case": "PASS"}

    control = subject.ProductiveObserver()
    control.source = QuadraticSource()
    transitions = 0
    while len(control.word) < 200:
        event = control.next_transition()
        require(Q(event["potential_after"]) < Q(event["potential_before"]), "quadratic control potential")
        transitions += 1
    require("".join(control.word) == "LR"*100, "quadratic periodic positive control")
    fixed = poly(INITIAL, "LR")
    require(fixed == (1, -9, 19), "quadratic cycle polynomial")
    quadratic = QuadraticSource()
    for _ in range(80):
        image = poly_range(fixed, quadratic.lower, quadratic.upper)
        require(image[0] <= 0 <= image[1], "valid quadratic cycle must not be rejected")
        quadratic.refine()
    report["quadratic_control"] = {"target": "(9-sqrt(5))/2", "periodic_word": "(LR)^100", "arrows": 200,
                                    "strict_potential_transitions": transitions, "zero_containing_ranges": 80,
                                    "verdict": "Interval-state freshness does not imply output aperiodicity"}

    require(poly_range((16, -112, 195), Q(3), Q(4)) == (Q(-1), Q(3)), "interior vertex negative control")
    require(width(cylinder((17, 5, 24, 7), "LR", 1))/width((17, 5, 24, 7)) == Q(35, 204) > Q(1, 6), "1/6 contraction counterexample")
    mutations = []
    def killed(name, verifier, original, edit):
        changed = deepcopy(original)
        edit(changed)
        try:
            verifier(changed)
        except (AssertionError, ValueError, KeyError):
            mutations.append(name)
        else:
            raise AssertionError("Mutation survived: "+name)
    sample = next(x for x in certificates if x["plan"]["start"] == 22 and x["plan"]["period"] == 1)
    killed("wrong fixed polynomial", verify_period, sample, lambda x: x["plan"]["fixed_polynomial"].__setitem__(2, -354))
    killed("inflated gap", verify_period, sample, lambda x: x["plan"].__setitem__("root_distance_lower_bound", "1"))
    killed("off-by-one deadline", verify_period, sample, lambda x: x["plan"].__setitem__("last_output_index_to_read", x["plan"]["last_output_index_to_read"]-1))
    killed("wrong witness displacement", verify_period, sample, lambda x: x["witness"].__setitem__("comparison_start", x["witness"]["comparison_start"]+1))
    killed("wrong source stage", verify_period, sample, lambda x: x["plan"].__setitem__("source_stage", x["plan"]["source_stage"]+1))
    mixed_sample = next(x for x in certificates if x["plan"]["kind"] == "mixed_hyperbolic")
    killed("wrong uniform height", verify_period, mixed_sample, lambda x: x["plan"]["uniform_classical_budget"].__setitem__("polynomial_height_with_floor", 16))
    run4 = runs[3]
    killed("wrong maximal run length", lambda x: verify_run(x, tuple(run4["bracket_before"]), run4["start"], 4), run4, lambda x: x.__setitem__("length", 293))
    killed("wrong rational cut bit", verify_pinbed, pins, lambda x: x["states_in_value_order"][0]["lower_cut_signature"].__setitem__(0, 1))
    killed("missing rational threshold", verify_pinbed, pins, lambda x: x["thresholds"].pop())
    early = next(x for x in certificates if x["plan"]["start"] == 0 and x["plan"]["period"] == 1)
    def rewind_source(x):
        stage = x["plan"]["source_stage"]-1
        x["witness"]["output_source_stage"] = stage
        x["witness"]["output_source_interval"] = [str(q) for q in source_interval(x["plan"]["source"], stage)]
    killed("genuine source interval with rewound clock", verify_period, early, rewind_source)
    killed("erased classical theorem dependency", verify_period, sample, lambda x: x["plan"]["uniform_classical_budget"].__setitem__("classical_import", "New proof without classical dependencies"))
    killed("false adaptive optimality scope", verify_pinbed, pins, lambda x: x.__setitem__("optimality_scope", "Globally optimal among adaptive tests"))
    killed("fractional escape-block count", verify_period, sample, lambda x: x["plan"].__setitem__("escape_blocks", x["plan"]["escape_blocks"]+0.5))
    report["hostile_controls"] = {"interior_vertex": "PASS", "one_sixth_contraction_refuted": "35/204 > 1/6",
                                  "mutations_rejected": mutations, "erased_run_lengths": "Alternating labels are periodic; counts must be retained"}

    # A real unbounded-mode invocation is observed for a finite prefix, then its
    # pipe is closed. This is a liveness smoke check, not an infinite run claim.
    process = subprocess.Popen([sys.executable, str(Path(subject.__file__)), "runs", "--forever"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        lines = [json.loads(process.stdout.readline()) for _ in range(5)]
        require([x["length"] for x in lines] == [6, 15, 1, 292, 1], "unbounded stream finite observation")
        process.stdout.close()
        return_code = process.wait(timeout=20)
        require(return_code == 0, "closed output pipe handled")
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        process.stdout.close()
        process.stderr.close()
    report["forever_cli"] = {"observed_records": 5, "exit_after_pipe_close": return_code}
    report["elapsed_seconds"] = round(perf_counter()-began, 6)
    report["status"] = "PASS"
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    args.output.with_name("period_certificates.json").write_text(json.dumps(certificates, indent=2, sort_keys=True)+"\n")
    args.output.with_name("run_certificates.json").write_text(json.dumps(runs, indent=2, sort_keys=True)+"\n")
    args.output.with_name("pinbed_certificate.json").write_text(json.dumps(pins, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "PASS", "output": str(args.output), "periods": len(period_rows)+3,
                      "runs": len(runs), "mutations_rejected": len(mutations), "elapsed_seconds": report["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
