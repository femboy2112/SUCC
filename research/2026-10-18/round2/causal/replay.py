#!/usr/bin/env python3
"""Bounded replay of Round II causal proofs, independent oracles and controls."""
from dataclasses import asdict
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from observational_succ.round2_causal import (
    compare_interfaces, guard_source, output_split_combined, post, safe_menu,
    simulation, split_combined, stochastic_contract, synthesize, verify_certificate,
)
from observational_succ.no_ghost import solve_nonnegative, verify_dual, verify_primal
from observational_succ.no_ghost_policy import (
    compile_public_policy, verify_policy_obstruction, verify_policy_solution,
)


def encode(obj):
    if isinstance(obj, Q):
        return str(obj)
    if isinstance(obj, (set, frozenset)):
        return sorted(obj)
    raise TypeError(type(obj).__name__)


def save(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2, default=encode) + "\n")


def run(name, command):
    started = datetime.now(timezone.utc).isoformat()
    before = time.monotonic()
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=120)
    (HERE / (name + ".stdout")).write_text(proc.stdout)
    (HERE / (name + ".stderr")).write_text(proc.stderr)
    return dict(name=name, command=command, cwd=str(ROOT), started_utc=started,
                elapsed_seconds=time.monotonic() - before, returncode=proc.returncode,
                stdout=name + ".stdout", stderr=name + ".stderr")


def model_data(model):
    return dict(source_id=model.source_id, basis=model.basis, digest=model.digest(),
                states=model.states, actions=model.actions, original=dict(model.original),
                observation=dict(model.observation), transitions=[
                    dict(before=s, action=a, edges=[asdict(e) for e in row])
                    for (s, a), row in model.transitions.items()])


def main():
    checks = [run("python_version", [sys.executable, "--version"]),
              run("focused_tests", [sys.executable, "-m", "unittest", "tests.test_round2_causal", "-v"]),
              run("causal_regression", [sys.executable, "-m", "unittest", "tests.test_round2_causal",
                  "tests.test_institute_causal", "tests.test_no_ghost", "tests.test_no_ghost_policy",
                  "tests.test_no_ghost_coherence", "tests.test_field_history_lift",
                  "tests.test_eodcs_causal_nerode", "-q"]),
              run("provenance", [sys.executable, "scripts/verify_provenance.py"]),
              run("observer", [sys.executable, "scripts/observer_foundations_probe.py"]),
              run("ordinal", [sys.executable, "scripts/ordinal_succ_report_probe.py"]),
              run("kernel", [sys.executable, "scripts/round2/verify_causal_lean.py"])]
    A, B = split_combined()
    initial = frozenset({"root"})
    source_records = []
    for source in (A, B):
        cert = synthesize(source, initial, 2)
        chance = stochastic_contract(source)
        system = compile_public_policy(chance, 2).system
        matrix, rhs = system.equations((), ())
        result = solve_nonnegative(matrix, rhs)
        verified = (verify_policy_solution(chance, system, result.primal, (), ())
                    if result.primal is not None else
                    verify_policy_obstruction(chance, 2, (), (), result.dual))
        source_records.append(dict(source=model_data(source), certificate=asdict(cert),
                                   certificate_verified=verify_certificate(source, initial, 2, cert),
                                   chance_source_id=chance.source_id,
                                   chance_rows=[dict(public_prefix=h, action=a, original=s, state=c,
                                                      atoms=[asdict(e) for e in row])
                                                for (h, a, s, c), row in chance.kernels.items()],
                                   LP=dict(variables=system.variables, matrix=matrix, rhs=rhs,
                                           result=asdict(result), verified=verified)))
    original_paths = []
    for i in range(2):
        states, actions = ("root", "s" + str(i), "end"), ("a", "b" + str(i))
        verified = all(any(e.target == after for e in A.transitions.get((before, action), ()))
                       for before, after, action in zip(states, states[1:], actions))
        original_paths.append(dict(states=states, actions=actions, verified=verified,
                                   original_tags=[A.original[s] for s in states]))
    outA, outB = output_split_combined()
    save("split_counterexample.json", dict(
        sources=source_records, original_possible_histories=original_paths,
        may_trace_comparison=asdict(compare_interfaces(A, initial, B, initial)),
        public_interface_comparison=asdict(compare_interfaces(A, initial, B, initial, public_safe=True)),
        simulation_A_by_B=sorted(simulation(A, B)), simulation_B_by_A=sorted(simulation(B, A)),
        bisimulation=sorted(simulation(A, B, bisimulation=True)),
        output_variant=dict(sources=[model_data(outA), model_data(outB)],
                            public_interface=asdict(compare_interfaces(outA, initial, outB, initial, public_safe=True)),
                            bisimulation=sorted(simulation(outA, outB, bisimulation=True))),
        forced_b_probability="UNDEFINED_ORIGINAL_ACTION_UNAVAILABLE_ON_HIDDEN_BRANCH",
        repaired_failed_proposal="Do not totalize absent row as invented half-probability failure",
        RH_proved=False))
    guards = []
    for n in range(1, 7):
        source = guard_source(n)
        menus = set()
        for bits in range(1, 1 << n):
            belief = frozenset(str(j) for j in range(n) if bits & (1 << j))
            menus.add(safe_menu(source, belief))
        guards.append(dict(n=n, source_digest=source.digest(), distinct_safe_menus=len(menus),
                           expected=(1 << n) - 1))
    save("guard_obstruction.json", dict(instances=guards, theorem_scope="EXACT_MENU_MONITOR_STATE_SIZE",
                                        winning_policy_memory_lower_bound=False,
                                        academic_novelty_established=False))
    paths = ["observational_succ/round2_causal.py", "tests/test_round2_causal.py",
             "formal/round2/PublicBelief.lean", "scripts/round2/verify_causal_lean.py",
             "research/2026-10-18/ROUND2_CAUSAL.md", "research/2026-10-18/round2/causal_axioms.json",
             str(Path(__file__).resolve().relative_to(ROOT))]
    receipt = dict(base_commit=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                   branch=subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip(),
                   checks=checks, passed=all(c["returncode"] == 0 for c in checks),
                   source_sha256={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
                   finite_scope=dict(full_relation_policy_cases=2304, adaptive_policy_cases=192,
                                     guard_beliefs=120),
                   proof_boundary="Kernel: policy and exact quotient core; paper: operational interface and counting",
                   RH_proved=False)
    save("receipt.json", receipt)
    print(json.dumps({"passed": receipt["passed"], "checks": [
        {"name": c["name"], "returncode": c["returncode"]} for c in checks]}, indent=2))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
