"""Run with: python -m observational_succ demo | yoneda-demo | local-global-demo | circle-demo | probe-budget | run | shadow | replay | reverse."""
from __future__ import annotations

import argparse
from pathlib import Path
import json
import sys

from . import (ActualizationError, BasisLift, Engine, Frame, I, Limits,
               ONE, Scalar, conductor_growth, run_arithmetic, source_at)
from .phenomenology import example as yoneda_example
from .local_global import prefix_demo
from .circle_transport import conductor_birth_2_to_6, verify_refinement_tower
from .resource_probe import ProbeBudget, ValuationWord, compare_observers, lcm_word


def emit(data, destination=None):
    encoded = json.dumps(data, indent=2, sort_keys=True)+"\n"
    if destination:
        p = Path(destination)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


def demo():
    e = Engine(arithmetic=True, limits=Limits(max_target=64))
    e.predict(6, ONE, "Declared zeta-coefficient hypothesis; not a direct encounter")
    rows = []
    for n in range(1, 13):
        e.step(source_at(n), context="zeta", probe="coefficient")
        observed = e.shadow(n) if n in {6, 8, 12} else None
        e.propagate()
        rows.append({"N": n, "observed_before_propagation": observed,
                     "targets": {str(t): e.shadow(t, witnesses=True) for t in (6, 8, 12)}})
    chi = run_arithmetic(12, kind="chi5")
    fake = run_arithmetic(6, overrides={6: Scalar("8/7")})
    cycle = Engine(Frame("F2", "modular", (1,), 2))
    for _ in range(4):
        cycle.advance(context="same laboratory")
    original = e.dumps()
    echoed = Engine.loads(original)
    echoed.reverse_all()
    return ({"scope": "finite operational framework, not an RH proof or physical wave simulation",
             "arithmetic_wavefront": rows,
             "conductor_growth": [conductor_growth(n) for n in range(1, 10)],
             "chi5_connected6": chi.shadow(6)["source"],
             "fake6_connected": fake.shadow(6)["source"],
             "periodic_field": {"coordinate": cycle.state["coordinate"],
                "tick": cycle.state["tick"], "distinct_event_witnesses": cycle.shadow_inverse()},
             "history_reconstruction": {"verified": Engine.loads(original).verify(),
                "restored_coordinate": echoed.state["coordinate"],
                "forward_records": len(e.records), "records_after_reversal": len(echoed.records),
                "journal_preserved": len(echoed.records) == 2*len(e.records)},
             "lossy_view": e.view(3)}, e)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("demo", help="6/8/12 shadows, observational_succ, F2, mutation and history reconstruction")
    p.add_argument("--output")
    p.add_argument("--trace", help="Save the full exact reconstructible history separately")
    p = sub.add_parser("run", help="Run a field-relative event stream")
    p.add_argument("--domain", choices=["natural", "integer", "rational", "modular"], default="natural")
    p.add_argument("--step", default="1", help="Comma-separated exact rational coordinates")
    p.add_argument("--start", default="0")
    p.add_argument("--modulus", type=int)
    p.add_argument("--steps", type=int, default=12)
    p.add_argument("--source", choices=["zeta", "chi5", "chi5_bar", "mixture5"],
                   help="Enable the natural arithmetic adapter; only N0,+1 at origin0")
    p.add_argument("--max-target", type=int, default=64)
    p.add_argument("--max-depth", type=int, default=8)
    p.add_argument("--output")
    p = sub.add_parser("shadow", help="Inspect a bounded unrealized or actualized target")
    p.add_argument("--horizon", type=int, default=3)
    p.add_argument("--target", type=int, default=6)
    p.add_argument("--max-depth", type=int, default=8)
    p.add_argument("--source", choices=["zeta", "chi5", "chi5_bar", "mixture5"], default="zeta")
    p.add_argument("--output")
    p = sub.add_parser("yoneda-demo", help="Compare thin versus full-path probes at wavefront 3")
    p.add_argument("--output")
    p = sub.add_parser("local-global-demo", help="Restrict a global arithmetic history to local SUCC observations")
    p.add_argument("--output")
    p = sub.add_parser("circle-demo", help="Check exact Z/2->Z/6 dual circle torsion and conductor birth")
    p.add_argument("--output")
    p = sub.add_parser("probe-budget", help="Certify bounded observational equivalence without materializing huge target values")
    p.add_argument("--budget", type=int, default=3)
    p.add_argument("--a", type=int, default=6)
    p.add_argument("--b", type=int, default=12)
    p.add_argument("--lcm-horizon", type=int, help="Use symbolic LCM(N) versus 2*LCM(N)")
    p.add_argument("--output")
    for command in ("replay", "reverse"):
        p = sub.add_parser(command)
        p.add_argument("trace")
        p.add_argument("--expected-head", help="Externally pinned checksum, not a signature")
        p.add_argument("--output")
        if command == "reverse":
            p.add_argument("--conjugate", action="store_true", help="Conjugate exact coefficients/fibers before uncomputation")
    args = parser.parse_args(argv)
    try:
        if args.command == "demo":
            report, e = demo()
            emit(report, args.output)
            if args.trace:
                emit(e.document(), args.trace)
        elif args.command == "run":
            if not 0 <= args.steps <= 1000:
                raise ActualizationError("steps must be in 0..1000")
            frame = Frame(args.domain, args.domain, tuple(args.step.split(",")), args.modulus)
            e = Engine(frame, tuple(args.start.split(",")), arithmetic=bool(args.source),
                       limits=Limits(max_target=args.max_target, max_depth=args.max_depth,
                                     max_records=max(1024, 4*args.steps+8)),
                       conductor=5 if args.source in {"chi5", "chi5_bar", "mixture5"} else 1)
            for n in range(1, args.steps+1):
                e.advance(source_at(n, args.source) if args.source else None,
                          context=args.source or "field observation")
            emit(e.document(), args.output)
        elif args.command == "shadow":
            limits = Limits(max_target=max(64, args.horizon, args.target), max_depth=args.max_depth)
            e = run_arithmetic(args.horizon, kind=args.source, limits=limits)
            emit(e.shadow(args.target, witnesses=True), args.output)
        elif args.command == "yoneda-demo":
            emit(yoneda_example(), args.output)
        elif args.command == "local-global-demo":
            emit(prefix_demo(), args.output)
        elif args.command == "circle-demo":
            emit({"conductor_birth":conductor_birth_2_to_6(),
                  "dual_tower":verify_refinement_tower(2,6,30)}, args.output)
        elif args.command == "probe-budget":
            if args.lcm_horizon is not None:
                a = lcm_word(args.lcm_horizon)
                b = a.multiply_prime(2)
            else:
                a, b = ValuationWord.from_integer(args.a), ValuationWord.from_integer(args.b)
            emit({"a": a.label(), "b": b.label(),
                  "certificate": compare_observers(a, b, ProbeBudget(args.budget)).data()},
                 args.output)
        else:
            path = Path(args.trace)
            if path.stat().st_size > 32_000_000:
                raise ActualizationError("Input exceeds 32 MB trace bound")
            e = Engine.loads(path.read_text(encoding="utf-8"), expected_head=args.expected_head)
            if args.command == "replay":
                emit({"verified": True, "head": e.head, "records": len(e.records), "state": e.state}, args.output)
            else:
                if args.conjugate:
                    e = e.conjugated()
                e.reverse_all()
                emit(e.document(), args.output)
        return 0
    except (ActualizationError, OSError, ValueError, TypeError) as exc:
        print(f"observational_succ: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
