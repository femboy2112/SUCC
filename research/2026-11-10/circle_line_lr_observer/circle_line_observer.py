#!/usr/bin/env python3
"""An exact Euclidean-circle -> rational source -> Stern--Brocot observer.

Runtime arithmetic is integral/rational. The construction contains no pi value,
digit table, BBP source, floating point, or trigonometric evaluation. See the
accompanying proofs for the semantic meaning of its geometric source.

    python circle_line_observer.py --steps 512 --digits 64 --output trace.json
    python circle_line_observer.py --source rotations --steps 512
    python circle_line_observer.py --forever

The last mode emits one certified arrow per JSON line. A finite program with
growing integer state is intended; bounded space or a finished infinity is not.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import groupby
import json
from math import gcd
from pathlib import Path
import sys
from typing import Protocol


@dataclass(frozen=True)
class Matrix2:
    """Standard action on t is (a*t+b)/(c*t+d); matrix products compose it."""

    a: int | Q
    b: int | Q
    c: int | Q
    d: int | Q

    def __matmul__(self, other: Matrix2) -> Matrix2:
        a, b, c, d = self.a, self.b, self.c, self.d
        e, f, g, h = other.a, other.b, other.c, other.d
        return Matrix2(a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)

    @property
    def determinant(self) -> int | Q:
        return self.a*self.d-self.b*self.c

    def at(self, t: Q | int) -> Q:
        return Q(self.a*t+self.b, self.c*t+self.d)

    def primitive(self) -> Matrix2:
        """Remove a common integer scalar without changing the projective map."""
        entries = (self.a, self.b, self.c, self.d)
        if not all(isinstance(x, int) for x in entries):
            raise TypeError("primitive() requires integer entries")
        divisor = gcd(*entries)
        if divisor == 0:
            raise ValueError("The zero matrix is not a projective map")
        return Matrix2(*(x//divisor for x in entries))

    def inverse(self) -> Matrix2:
        z = self.determinant
        if not z:
            raise ValueError("Singular matrix")
        return Matrix2(Q(self.d, z), Q(-self.b, z),
                       Q(-self.c, z), Q(self.a, z))


IDENTITY = Matrix2(1, 0, 0, 1)
L = Matrix2(1, 1, 0, 1)
R = Matrix2(1, 0, 1, 1)


def rational_text(value: Q) -> str:
    """Exact decimal fraction text without depending on Python's digit cap.

    The fallback converts internally generated integers in bounded chunks;
    imported API calls therefore need not change a process-wide setting.
    """
    def integer_text(number: int) -> str:
        try:
            return str(number)
        except ValueError:
            sign = "-" if number < 0 else ""
            number = abs(number)
            chunks = []
            while number:
                number, remainder = divmod(number, 10**9)
                chunks.append(remainder)
            return sign+str(chunks[-1])+"".join(f"{x:09d}" for x in reversed(chunks[:-1]))
    value = Q(value)
    numerator = integer_text(value.numerator)
    return numerator if value.denominator == 1 else numerator+"/"+integer_text(value.denominator)


class EuclideanCircleLine:
    """Finite equations, incidence maps and metric data for the named shapes."""

    circle_equation = "x*x + y*y = 1"
    secant_equation = "y = t*(x + 1)"
    metric_equation = "ds*ds = dx*dx + dy*dy"
    diameter = Q(2)

    @staticmethod
    def point(t: Q) -> tuple[Q, Q]:
        t = Q(t)
        return (1-t*t)/(1+t*t), 2*t/(1+t*t)

    @staticmethod
    def tangent(t: Q) -> tuple[Q, Q]:
        t = Q(t)
        return -4*t/(1+t*t)**2, 2*(1-t*t)/(1+t*t)**2

    @staticmethod
    def arc_speed(t: Q) -> Q:
        t = Q(t)
        return 2/(1+t*t)

    @staticmethod
    def multiply(p: tuple[Q, Q], q: tuple[Q, Q]) -> tuple[Q, Q]:
        x, y = p
        u, v = q
        return x*u-y*v, x*v+y*u

    @staticmethod
    def metric_jacobian(matrix: Matrix2, t: Q) -> Q:
        """Pullback factor for Euclidean arclength under the parameter map.

        Valid on an affine chart where c*t+d is nonzero. The projective circle
        extends across chart poles; callers needing that extension use charts.
        """
        t = Q(t)
        if not matrix.determinant or matrix.c*t+matrix.d == 0:
            raise ValueError("Require an invertible map and a finite chart")
        return abs(matrix.determinant)*(1+t*t)/(
            (matrix.a*t+matrix.b)**2+(matrix.c*t+matrix.d)**2)

    @staticmethod
    def conic_lift(matrix: Matrix2) -> tuple[tuple[Q, Q, Q], ...]:
        """Symmetric-square action in (X,Y,Z)=(V²-U²,2UV,V²+U²)."""
        a, b, c, d = matrix.a, matrix.b, matrix.c, matrix.d
        return (
            (Q(a*a-c*c+d*d-b*b, 2), c*d-a*b,
             Q(c*c-a*a+d*d-b*b, 2)),
            (b*d-a*c, a*d+b*c, a*c+b*d),
            (Q(b*b+d*d-a*a-c*c, 2), a*b+c*d,
             Q(a*a+b*b+c*c+d*d, 2)),
        )


class RationalSource(Protocol):
    name: str
    stage: int
    lower: Q
    upper: Q

    def refine(self) -> None: ...


def source_factor(k: int) -> Matrix2:
    """Circle integral's kth positive source factor; k starts at one."""
    if k < 1:
        raise ValueError("k must be positive")
    return Matrix2(k, 4*k+2, 0, 2*k+1)


class MatrixCircleSource:
    """Nested enclosures A_k([3,4]), A_k=Z_1 ... Z_k.

    Euclidean geometry derives sum_{n>=0} 2*W_n, where W_0=1 and
    W_n/W_(n-1)=n/(2*n+1). Every shifted tail is strictly between 3 and 4.
    Thus the initial interval and each subsequent enclosure are justified
    by the same source, rather than an externally supplied numerical value.
    """

    name = "circle_beta_matrix"

    def __init__(self) -> None:
        self.stage = 0
        self.matrix = IDENTITY
        self.lower, self.upper = Q(3), Q(4)

    def refine(self) -> None:
        self.stage += 1
        self.matrix = (self.matrix @ source_factor(self.stage)).primitive()
        self.lower, self.upper = self.matrix.at(3), self.matrix.at(4)


class RotationCircleSource:
    """Independent circle arc splitting at rational parameters 1/2 and 1/3.

    P(1/2)*P(1/3)=(0,1). Alternating rational integrals on those two arcs
    yield strict lower/upper bounds. The stage counts pairs of series terms.
    """

    name = "circle_345_rotations"

    def __init__(self) -> None:
        self.stage = 0
        self.partial = [Q(0), Q(0)]
        self.lower, self.upper = Q(0), Q(4)
        self.refine()

    def refine(self) -> None:
        j = 2*self.stage
        for i, inverse in enumerate((2, 3)):
            self.partial[i] += Q(1, (2*j+1)*inverse**(2*j+1))
        self.upper = 4*sum(self.partial, Q(0))
        for i, inverse in enumerate((2, 3)):
            self.partial[i] -= Q(1, (2*j+3)*inverse**(2*j+3))
        self.lower = 4*sum(self.partial, Q(0))
        self.stage += 1


class SternBrocotObserver:
    """E has endpoint columns (a,b), (c,d); E -> E*L or E*R.

    Do not conflate E's endpoint convention with Matrix2.at(t). The residual
    chart is (a+c*t)/(b+d*t). Runtime decisions compare rational certificates.
    """

    def __init__(self, source: RationalSource) -> None:
        if not Q(3) <= source.lower < source.upper <= Q(4):
            raise ValueError("This observer requires a strict source inside [3,4]")
        self.source = source
        self.a, self.b, self.c, self.d = 3, 1, 4, 1
        self.steps = 0

    @property
    def endpoints(self) -> tuple[Q, Q]:
        return Q(self.a, self.b), Q(self.c, self.d)

    @property
    def endpoint_matrix(self) -> Matrix2:
        return Matrix2(self.a, self.c, self.b, self.d)

    @property
    def residual_chart(self) -> Matrix2:
        return Matrix2(self.c, self.a, self.d, self.b)

    def next_arrow(self) -> dict:
        q = Q(self.a+self.c, self.b+self.d)
        consumed = 0
        while True:
            if self.source.upper <= q:
                arrow = "L"
                self.c, self.d = self.a+self.c, self.b+self.d
                break
            if self.source.lower >= q:
                arrow = "R"
                self.a, self.b = self.a+self.c, self.b+self.d
                break
            self.source.refine()
            consumed += 1
        self.steps += 1
        return {"step": self.steps, "arrow": arrow, "mediant": rational_text(q),
                "source_stage": self.source.stage, "source_consumed": consumed,
                "endpoints": [self.a, self.b, self.c, self.d]}


def digit_certificates(source: RationalSource, count: int, base: int = 16) -> list[dict]:
    """Units digit then count fractional digits, all certified by floors.

    The `floor` field retains the whole scaled integer. In bases 2 and 3,
    the exponent-zero `digit` alone is not the whole integer part of the ratio.
    """
    if count < 0 or not 2 <= base <= 36:
        raise ValueError("Require count >= 0 and 2 <= base <= 36")
    result = []
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for exponent in range(count+1):
        scale = base**exponent
        while True:
            lo, hi = source.lower*scale, source.upper*scale
            a, b = lo.numerator//lo.denominator, hi.numerator//hi.denominator
            if a == b:
                result.append({"exponent": exponent, "digit": alphabet[a % base],
                               "floor": a, "source_stage": source.stage})
                break
            source.refine()
    return result


def runs(word: str) -> list[dict]:
    return [{"arrow": a, "count": sum(1 for _ in group)} for a, group in groupby(word)]


def finite_run(steps: int, digits: int, source_name: str = "matrix") -> dict:
    if steps < 0 or digits < 0:
        raise ValueError("Counts must be nonnegative")
    if source_name not in ("matrix", "rotations"):
        raise ValueError("Unknown source; choose 'matrix' or 'rotations'")
    source = MatrixCircleSource() if source_name == "matrix" else RotationCircleSource()
    observer = SternBrocotObserver(source)
    trace = [observer.next_arrow() for _ in range(steps)]
    arrow_stage = source.stage
    word = "".join(item["arrow"] for item in trace)
    dc = digit_certificates(source, digits)
    lo, hi = observer.endpoints
    return {
        "schema": "succ.circle-line-lr.v1", "source": source.name,
        "semantics": {"circle": EuclideanCircleLine.circle_equation,
                      "line": EuclideanCircleLine.secant_equation,
                      "metric": EuclideanCircleLine.metric_equation,
                      "ratio": "Euclidean circumference / diameter",
                      "runtime": "exact integers and rational numbers"},
        "root_interval": ["3", "4"], "global_root_prefix": "RRRL",
        "steps": steps, "word": word, "runs": runs(word),
        "last_run_may_be_incomplete": bool(word),
        "endpoints": [rational_text(lo), rational_text(hi)], "interval_width": rational_text(hi-lo),
        "arrow_source_stage": arrow_stage, "final_source_stage": source.stage,
        "final_source_interval": [rational_text(source.lower), rational_text(source.upper)],
        "hexadecimal": dc[0]["digit"]+"."+"".join(x["digit"] for x in dc[1:]),
        "digit_certificates": dc, "arrow_certificates": trace,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=128)
    parser.add_argument("--digits", type=int, default=32)
    parser.add_argument("--source", choices=("matrix", "rotations"), default="matrix")
    parser.add_argument("--forever", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.steps < 0 or args.digits < 0:
        parser.error("--steps and --digits must be nonnegative")
    if args.forever and args.output:
        parser.error("--forever streams to stdout; omit --output")
    # These integers are generated internally. Remove the decimal display cap
    # so an otherwise productive long run cannot fail merely while serializing.
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    try:
        if args.forever:
            source = MatrixCircleSource() if args.source == "matrix" else RotationCircleSource()
            observer = SternBrocotObserver(source)
            while True:
                print(json.dumps(observer.next_arrow(), sort_keys=True), flush=True)
        else:
            result = finite_run(args.steps, args.digits, args.source)
            if args.output:
                args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
                print(json.dumps({k: result[k] for k in (
                    "source", "steps", "runs", "arrow_source_stage",
                    "final_source_stage", "hexadecimal", "endpoints")}, indent=2))
            else:
                print(json.dumps(result, indent=2, sort_keys=True))
    except BrokenPipeError:
        # A finite consumer is allowed to stop reading the infinite stream.
        try:
            sys.stdout.close()
        except BrokenPipeError:
            pass


if __name__ == "__main__":
    main()
