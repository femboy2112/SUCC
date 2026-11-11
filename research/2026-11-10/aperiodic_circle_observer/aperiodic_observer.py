#!/usr/bin/env python3
"""Productive circle observers with exact cycle, run and rational-probe certificates.

Examples (run from this directory):
  python aperiodic_observer.py period --start 22 --period 1 --output period.json
  python aperiodic_observer.py period --start 22 --period 1 --plan-only
  python aperiodic_observer.py runs --count 32
  python aperiodic_observer.py pinbed --states 0,6,21,22,100,314
  python aperiodic_observer.py periods --forever

The circle source is imported from the unchanged preceding round. Classical
nonquadraticity proves totality; accepted certificates use finite rational
arithmetic. No pi value, digit table, BBP source or trig evaluator is input.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import importlib.util
import json
from math import gcd
from pathlib import Path
import sys


SOURCE_PATH = Path(__file__).resolve().parent.parent / "circle_line_lr_observer/circle_line_observer.py"
spec = importlib.util.spec_from_file_location("succ_circle_source_v4", SOURCE_PATH)
if spec is None or spec.loader is None:
    raise ImportError(f"Cannot load the preceding circle source: {SOURCE_PATH}")
circle = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = circle
spec.loader.exec_module(circle)
Matrix2, L, R = circle.Matrix2, circle.L, circle.R
qt = circle.rational_text


def new_source(name: str = "matrix"):
    if name == "matrix":
        return circle.MatrixCircleSource()
    if name == "rotations":
        return circle.RotationCircleSource()
    raise ValueError("Choose source 'matrix' or 'rotations'")


def word_matrix(word: str):
    result = circle.IDENTITY
    for letter in word:
        if letter not in ("L", "R"):
            raise ValueError("Words must contain only L and R")
        result = result @ (L if letter == "L" else R)
    return result


def matrix_power(matrix, exponent: int):
    if exponent < 0:
        raise ValueError("Exponent must be nonnegative")
    result = circle.IDENTITY
    while exponent:
        if exponent & 1:
            result = result @ matrix
        matrix = matrix @ matrix
        exponent //= 2
    return result


@dataclass(frozen=True)
class Bracket:
    a: int = 3
    b: int = 1
    c: int = 4
    d: int = 1

    def __post_init__(self):
        if self.b <= 0 or self.d <= 0 or self.b*self.c-self.a*self.d != 1:
            raise ValueError("Require positive Farey denominators and bc-ad=1")

    @property
    def lower(self):
        return Q(self.a, self.b)

    @property
    def upper(self):
        return Q(self.c, self.d)

    @property
    def width(self):
        return Q(1, self.b*self.d)

    @property
    def matrix(self):
        return Matrix2(self.a, self.c, self.b, self.d)

    def values(self):
        return [self.a, self.b, self.c, self.d]

    def apply(self, matrix):
        m = self.matrix @ matrix
        if any(Q(v).denominator != 1 for v in (m.a, m.b, m.c, m.d)):
            raise ValueError("A Farey update must have integral matrix entries")
        return Bracket(int(m.a), int(m.c), int(m.b), int(m.d))

    def advance(self, letter: str, count: int = 1):
        if count < 1:
            raise ValueError("Run length must be positive")
        if letter == "L":
            return Bracket(self.a, self.b, self.c+count*self.a, self.d+count*self.b)
        if letter == "R":
            return Bracket(self.a+count*self.c, self.b+count*self.d, self.c, self.d)
        raise ValueError("Unknown arrow")

    def residual(self, x: Q):
        x = Q(x)
        if not self.lower < x < self.upper:
            raise ValueError("Residual requires a point strictly inside its chart")
        return (self.b*x-self.a)/(self.c-self.d*x)


class ProductiveObserver:
    """Finite rules, growing rational state, no prescribed output horizon."""

    def __init__(self, source: str = "matrix"):
        self.source = new_source(source)
        self.bracket = Bracket()
        self.word: list[str] = []
        self.brackets = [self.bracket]
        self.transitions = 0

    def next_transition(self) -> dict:
        old = self.bracket
        source_width = self.source.upper-self.source.lower
        before = source_width*old.width
        mediant = Q(old.a+old.c, old.b+old.d)
        if self.source.upper <= mediant:
            kind, letter = "arrow", "L"
            factor = Q(old.d, old.b+old.d)
        elif self.source.lower >= mediant:
            kind, letter = "arrow", "R"
            factor = Q(old.b, old.b+old.d)
        else:
            kind, letter = "source", None
            self.source.refine()
            factor = (self.source.upper-self.source.lower)/source_width
        if letter is not None:
            self.bracket = old.advance(letter)
            self.word.append(letter)
            self.brackets.append(self.bracket)
        self.transitions += 1
        after = (self.source.upper-self.source.lower)*self.bracket.width
        assert Q(0) < factor < 1 and after == before*factor
        return {"kind": kind, "arrow": letter, "transition": self.transitions,
                "output_length": len(self.word), "source_stage": self.source.stage,
                "mediant": qt(mediant), "bracket_before": old.values(),
                "bracket_after": self.bracket.values(), "potential_before": qt(before),
                "potential_after": qt(after), "decrease_factor": qt(factor)}

    def next_arrow(self) -> dict:
        while True:
            event = self.next_transition()
            if event["kind"] == "arrow":
                return event

    def ensure(self, count: int):
        if count < 0:
            raise ValueError("Output count must be nonnegative")
        while len(self.word) < count:
            self.next_arrow()


def polynomial_value(coefficients, x):
    a, b, c = coefficients
    return (a*x+b)*x+c


def polynomial_range(coefficients, lower, upper):
    """Exact range of a quadratic on a closed rational interval, including vertex."""
    if lower > upper:
        raise ValueError("Reversed interval")
    a, b, _ = coefficients
    values = [polynomial_value(coefficients, lower), polynomial_value(coefficients, upper)]
    if a:
        vertex = Q(-b, 2*a)
        if lower <= vertex <= upper:
            values.append(polynomial_value(coefficients, vertex))
    return min(values), max(values)


def primitive_polynomial(values):
    if any(Q(v).denominator != 1 for v in values):
        raise ValueError("Fixed polynomial must have integral coefficients")
    values = tuple(int(v) for v in values)
    divisor = gcd(*values)
    if divisor == 0:
        raise ValueError("The zero polynomial is not a separation certificate")
    values = tuple(v//divisor for v in values)
    sign = 1 if next(v for v in values if v) > 0 else -1
    return tuple(sign*v for v in values)


def period_polynomial(bracket: Bracket, word: str):
    if not word:
        raise ValueError("A period must be nonempty")
    w = word_matrix(word)
    if set(word) == {"L"}:
        return primitive_polynomial((0, bracket.b, -bracket.a))
    if set(word) == {"R"}:
        return primitive_polynomial((0, bracket.d, -bracket.c))
    f = bracket.matrix @ w @ bracket.matrix.inverse()
    return primitive_polynomial((f.c, f.d-f.a, -f.b))


def exact_escape_blocks(bracket: Bracket, word: str, gap: Q):
    """Find the first hypothetical repeated cylinder narrower than gap.

    Only matrix powers of the proposed word are used; no future true arrows
    are read. Width is strictly decreasing even for a single-letter period.
    """
    if gap <= 0 or not word:
        raise ValueError("Require a positive gap and a nonempty word")
    w = word_matrix(word)
    def cylinder(r):
        return bracket.apply(matrix_power(w, r))
    high = 1
    while cylinder(high).width >= gap:
        high *= 2
    low = 0
    while high-low > 1:
        middle = (low+high)//2
        if cylinder(middle).width < gap:
            high = middle
        else:
            low = middle
    return high, cylinder(high), cylinder(high-1)


def uniform_budget(coefficients, start: int, period: int, mixed: bool):
    """Explicit classical worst-case budget, kept symbolic when astronomical.

    Waldschmidt 1978 Corollary3.2 implies |P(pi)| > H^(-2^43) for degree<=2
    and H=max(16,height(P)). See UNIFORM_BOUNDS.md. This is a theorem import,
    not a finite runtime proof of a transcendence measure.
    """
    height = max(16, *(abs(v) for v in coefficients))
    exponent = 2**43+1
    bits = height.bit_length()
    source_stage = exponent*bits+4
    result = {"polynomial_height_with_floor": height, "height_bit_length": bits,
              "root_bound_exponent": exponent, "source_sign_stage_sufficient": source_stage,
              "classical_import": "Waldschmidt1978 Corollary3.2; conservative degree2 corollary"}
    if mixed:
        result.update(escape_blocks_sufficient=source_stage,
                      last_output_index_sufficient=start+period*source_stage-1)
    else:
        result["escape_blocks_symbolic"] = {"coefficient": 9, "base": height, "exponent": exponent}
    return result


def _prepare_period(start: int, period: int, extra: int, source: str):
    if start < 0 or period < 1 or extra < 0:
        raise ValueError("Require start>=0, period>=1, extra>=0")
    observer = ProductiveObserver(source)
    observer.ensure(start+period)
    prefix = "".join(observer.word[:start])
    word = "".join(observer.word[start:start+period])
    bracket = observer.brackets[start]
    polynomial = period_polynomial(bracket, word)
    while True:
        image = polynomial_range(polynomial, observer.source.lower, observer.source.upper)
        if image[0] > 0 or image[1] < 0:
            break
        observer.source.refine()
    first_stage = observer.source.stage
    for _ in range(extra):
        observer.source.refine()
    image = polynomial_range(polynomial, observer.source.lower, observer.source.upper)
    epsilon = image[0] if image[0] > 0 else -image[1]
    a, b, _ = polynomial
    derivative = max(abs(2*a*bracket.lower+b), abs(2*a*bracket.upper+b))
    assert epsilon > 0 and derivative > 0
    gap = epsilon/derivative
    blocks, escaped, previous = exact_escape_blocks(bracket, word, gap)
    assert blocks >= 2  # The first observed block really agrees with the target.
    deadline = start+blocks*period-1
    mixed = len(set(word)) == 2
    plan = {
        "schema": "succ.aperiodic-period.v1", "start": start, "period": period,
        "source": observer.source.name, "construction_output_length": len(observer.word),
        "prefix": prefix, "candidate_word": word, "prefix_bracket": bracket.values(),
        "fixed_polynomial": list(polynomial), "first_separation_stage": first_stage,
        "extra_source_refinements": extra, "source_stage": observer.source.stage,
        "source_interval": [qt(observer.source.lower), qt(observer.source.upper)],
        "polynomial_range": [qt(v) for v in image], "polynomial_gap": qt(epsilon),
        "derivative_bound_on_prefix": qt(derivative), "root_distance_lower_bound": qt(gap),
        "escape_blocks": blocks, "escaped_cylinder": escaped.values(),
        "escaped_width": qt(escaped.width), "previous_width": qt(previous.width),
        "last_output_index_to_read": deadline, "period_witness_start_at_most": deadline-period,
        "kind": "mixed_hyperbolic" if mixed else "single_letter_parabolic",
        "uniform_classical_budget": uniform_budget(polynomial, start, period, mixed),
    }
    if mixed:
        plan["rational_mixed_width_bound"] = qt(bracket.width/Q(5**blocks))
    return plan, observer


def prepare_period(start: int, period: int, extra: int = 8, source: str = "matrix"):
    """Construct an escape plan before generating any output past start+period."""
    return _prepare_period(start, period, extra, source)[0]


def reject_period(start: int, period: int, extra: int = 8, source: str = "matrix"):
    plan, observer = _prepare_period(start, period, extra, source)
    for j in range(start+period, plan["last_output_index_to_read"]+1):
        observer.ensure(j+1)
        if observer.word[j] != observer.word[j-period]:
            return {"plan": plan, "witness": {
                "comparison_start": j-period, "different_output_index": j,
                "earlier_letter": observer.word[j-period], "later_letter": observer.word[j],
                "is_first_period_mismatch": True, "output_prefix": "".join(observer.word),
                "output_source_stage": observer.source.stage,
                "output_source_interval": [qt(observer.source.lower), qt(observer.source.upper)],
            }}
    raise AssertionError("A proved escape deadline was violated")


class RunObserver:
    """Emit maximal (letter,natural-number length) blocks without expanding them."""

    def __init__(self, source: str = "matrix"):
        self.source = new_source(source)
        self.bracket = Bracket()
        self.output_length = 0
        self.run_count = 0

    def next_run(self):
        before = self.bracket
        while True:
            lo, hi = self.source.lower, self.source.upper
            if not before.lower < lo < hi < before.upper:
                self.source.refine()
                continue
            zlo, zhi = before.residual(lo), before.residual(hi)
            if zlo >= 1:
                letter, flo, fhi = "R", zlo, zhi
            elif zhi <= 1:
                letter, flo, fhi = "L", 1/zhi, 1/zlo
            else:
                self.source.refine()
                continue
            lower_floor, upper_floor = flo.numerator//flo.denominator, fhi.numerator//fhi.denominator
            if lower_floor == upper_floor and lower_floor >= 1:
                length = lower_floor
                break
            self.source.refine()
        self.bracket = before.advance(letter, length)
        start = self.output_length
        self.output_length += length
        self.run_count += 1
        return {"run": self.run_count, "arrow": letter, "length": length,
                "start": start, "stop": self.output_length,
                "source": self.source.name, "source_stage": self.source.stage,
                "source_interval": [qt(lo), qt(hi)], "residual_interval": [qt(zlo), qt(zhi)],
                "floor_interval": [qt(flo), qt(fhi)], "bracket_before": before.values(),
                "bracket_after": self.bracket.values(),
                "expanded_future_arrows_used": 0}


def rational_pinbed(indices: list[int], source: str = "matrix"):
    if not indices or any(n < 0 for n in indices) or len(set(indices)) != len(indices):
        raise ValueError("Use a nonempty list of distinct nonnegative output indices")
    observer = ProductiveObserver(source)
    observer.ensure(max(indices))
    states = [(n, observer.brackets[n]) for n in indices]
    while True:
        lo, hi = observer.source.lower, observer.source.upper
        if not all(b.lower < lo < hi < b.upper for _, b in states):
            observer.source.refine()
            continue
        intervals = sorted((b.residual(lo), b.residual(hi), n, b) for n, b in states)
        if all(x[1] < y[0] for x, y in zip(intervals, intervals[1:])):
            break
        observer.source.refine()
    thresholds = [(x[1]+y[0])/2 for x, y in zip(intervals, intervals[1:])]
    return {"schema": "succ.rational-residual-pinbed.v1", "source": observer.source.name,
            "source_stage": observer.source.stage, "source_interval": [qt(lo), qt(hi)],
            "output_prefix": "".join(observer.word), "requested_states": indices,
            "thresholds": [qt(q) for q in thresholds],
            "states_in_value_order": [
                {"index": n, "bracket": b.values(), "residual_interval": [qt(l), qt(u)],
                 "lower_cut_signature": [int(q < l) for q in thresholds]}
                for l, u, n, b in intervals],
            "optimality_scope": "m-1 fixed nonadaptive rational threshold probes for m distinct ordered states"}


def period_requests():
    """Fair diagonal enumeration: every (start>=0,period>=1) occurs once."""
    diagonal = 1
    while True:
        for start in range(diagonal):
            yield start, diagonal-start
        diagonal += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("period", "periods", "runs", "pinbed", "transitions"))
    parser.add_argument("--start", type=int, default=22)
    parser.add_argument("--period", type=int, default=1)
    parser.add_argument("--extra", type=int, default=8)
    parser.add_argument("--count", type=int, default=16)
    parser.add_argument("--states", default="0,6,21,22,100,314")
    parser.add_argument("--source", choices=("matrix", "rotations"), default="matrix")
    parser.add_argument("--plan-only", action="store_true")
    parser.add_argument("--forever", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.start < 0 or args.period < 1 or args.extra < 0 or args.count < 0:
        parser.error("Require start>=0, period>=1, extra>=0, count>=0")
    if args.forever and (args.output or args.mode in ("period", "pinbed")):
        parser.error("--forever streams periods, runs or transitions to stdout")
    if args.plan_only and args.mode not in ("period", "periods"):
        parser.error("--plan-only applies to period modes")
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    action = prepare_period if args.plan_only else reject_period
    if args.mode == "period":
        result = action(args.start, args.period, args.extra, args.source)
    elif args.mode == "pinbed":
        try:
            indices = [int(x.strip()) for x in args.states.split(",")]
            result = rational_pinbed(indices, args.source)
        except ValueError as error:
            parser.error(str(error))
    else:
        if args.mode == "periods":
            iterator = (action(n, p, args.extra, args.source) for n, p in period_requests())
        elif args.mode == "runs":
            observer = RunObserver(args.source)
            iterator = iter(observer.next_run, None)
        else:
            observer = ProductiveObserver(args.source)
            iterator = iter(observer.next_transition, None)
        if args.forever:
            try:
                for item in iterator:
                    print(json.dumps(item, sort_keys=True), flush=True)
            except BrokenPipeError:
                try:
                    sys.stdout.close()
                except BrokenPipeError:
                    pass
            return
        result = [next(iterator) for _ in range(args.count)]
    encoded = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(encoded)
        print(json.dumps({"mode": args.mode, "output": str(args.output), "status": "CERTIFIED"}))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
