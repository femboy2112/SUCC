#!/usr/bin/env python3
"""Reproduce the X03 finite-gluing/CEGIS receipt without external solvers."""

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.swarm_gluing_cegis import (  # noqa: E402
    FiniteTable, LocalRelation, TypedGrammar, global_sections, monotone_cegis,
    triangle_problem,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    tests = unittest.defaultTestLoader.discover(str(ROOT / "tests"),
                                               pattern="test_swarm_gluing_cegis.py")
    result = unittest.TextTestRunner(verbosity=1).run(tests)
    if not result.wasSuccessful():
        return 1
    source, constraints = triangle_problem()
    pairs = tuple(product((0, 1), repeat=2))
    tables = tuple(tuple(pair for j, pair in enumerate(pairs) if mask & (1 << j))
                   for mask in range(16))
    scopes = (("x", "y"), ("y", "z"), ("x", "z"))
    counts = {"families": 0, "satisfiable": 0, "unsatisfiable": 0,
              "nonempty_pairwise_compatible_families": 0,
              "nonempty_pairwise_compatible_but_unsatisfiable": 0,
              "maximum_cegis_rejections": 0}
    for local in product(tables, repeat=3):
        relations = tuple(LocalRelation(str(j), scope, table)
                          for j, (scope, table) in enumerate(zip(scopes, local)))
        run = monotone_cegis(TypedGrammar(source, source), relations)
        counts["families"] += 1
        counts["satisfiable" if run["status"] == "SAT_SOURCE" else "unsatisfiable"] += 1
        counts["maximum_cegis_rejections"] = max(counts["maximum_cegis_rejections"],
                                                  len(run["rejections"]))
        compatible = all(local)
        for i, left in enumerate(relations):
            for right in relations[i + 1:]:
                overlap = tuple(v for v in left.scope if v in right.scope)
                left_projection = {tuple(row[left.scope.index(v)] for v in overlap)
                                   for row in left.allowed}
                right_projection = {tuple(row[right.scope.index(v)] for v in overlap)
                                    for row in right.allowed}
                compatible = compatible and left_projection == right_projection
        if compatible:
            counts["nonempty_pairwise_compatible_families"] += 1
            counts["nonempty_pairwise_compatible_but_unsatisfiable"] += (
                run["status"] == "UNSAT_SOURCE")
    hidden = FiniteTable(source.variables + ("hidden",), source.domains + ((0, 1),),
                         tuple(row + (h,) for row in source.rows for h in (0, 1)))
    bit = FiniteTable.cartesian(("x",), ((0, 1),))
    truncated = FiniteTable(("x",), ((0, 1),), ((0,),))
    wanted_one = (LocalRelation("one", ("x",), ((1,),)),)
    files = ("observational_succ/swarm_gluing_cegis.py", "tests/test_swarm_gluing_cegis.py",
             "scripts/swarm_x03_probe.py")
    receipt = {
        "schema": "SUCC-SWM-X03/1",
        "frozen_parent": "71eaf11e48ca3ccb349858bba64abf36b59ee6f5",
        "status": "CLASSICAL ingredients; PROVED LOCAL bridge with paper proof",
        "formal_kernel_checked": False,
        "external_source_authenticated": False,
        "unit_tests": {"run": result.testsRun, "failures": len(result.failures),
                       "errors": len(result.errors), "passed": result.wasSuccessful()},
        "exhaustive_binary_triangle_counts": counts,
        "inconsistent_triangle": monotone_cegis(TypedGrammar(source, source), constraints),
        "hidden_variable_extension": monotone_cegis(TypedGrammar(source, hidden), constraints),
        "incomplete_grammar": monotone_cegis(TypedGrammar(bit, truncated), wanted_one),
        "incomplete_grammar_original_solutions": global_sections(bit, wanted_one),
        "file_sha256": {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
                        for path in files},
        "boundary": "Finite declared source tables, finite grammar denotations, exact verification. "
                    "No empirical source authentication, infinite grammar completeness, "
                    "physical branch gluing, or RH consequence.",
    }
    output = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
