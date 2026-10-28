#!/usr/bin/env python3
"""Exact finite audit of quadratic-fiber Haar/empirical energies.

All phase coordinates are Gaussian integers, and all energies/bounds are
fractions.Fraction values. This corroborates finite identities and inequalities;
it does not execute the normal finite-type carrier existence construction.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
from random import Random


SEED = 708271
PARAMETERS = [(7, 1), (7, 2), (7, 3), (11, 1), (11, 2), (241, 1)]
UNIT_PHASES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def numerator(n: int) -> int:
    return 120 * n * n - 89 * n + 16


def energies(seq, start: int, q: int, multiplicities):
    sums, counts, residue_sums = {}, {}, {}
    for offset, phase in enumerate(seq):
        n = start + offset
        label = numerator(n) % q
        value = sums.setdefault(label, [0, 0])
        value[0] += phase[0]
        value[1] += phase[1]
        counts[label] = counts.get(label, 0) + 1
        value = residue_sums.setdefault(n % q, [0, 0])
        value[0] += phase[0]
        value[1] += phase[1]
    N = len(seq)
    haar = F(q, N * N) * sum(
        (F(v[0] ** 2 + v[1] ** 2, multiplicities[a]) for a, v in sums.items()),
        F(0),
    )
    empirical = F(1, N) * sum(
        (F(v[0] ** 2 + v[1] ** 2, counts[a]) for a, v in sums.items()), F(0)
    )
    fine = F(q, N * N) * sum(v[0] ** 2 + v[1] ** 2 for v in residue_sums.values())
    return haar, empirical, fine, len(counts)


def run():
    rng = Random(SEED)
    cases, check_counts = [], {}

    def checked(name, lhs, rhs):
        if lhs > rhs:
            raise AssertionError(f"{name}: {lhs} > {rhs}")
        check_counts[name] = check_counts.get(name, 0) + 1
        return {"lhs": str(lhs), "rhs": str(rhs), "passed": True}

    for p, L in PARAMETERS:
        q = p**L
        fibers = {}
        for r in range(q):
            fibers.setdefault(numerator(r) % q, []).append(r)
        multiplicities = {a: len(rr) for a, rr in fibers.items()}
        for N in sorted(set([1, 2, 5, q - 1, q, q + 1, 2 * q - 1, 3 * q + 5])):
            for repetition in range(8):
                phases = [rng.choice(UNIT_PHASES) for _ in range(N + 1)]
                H0, Q0, E0, occupied0 = energies(phases[:N], 0, q, multiplicities)
                H1, Q1, E1, occupied1 = energies(phases[1:], 1, q, multiplicities)
                ceil_count = (N + q - 1) // q
                checks = {
                    "projection_window_zero": checked("projection_window_zero", H0, E0),
                    "projection_window_one": checked("projection_window_one", H1, E1),
                    "empirical_lower": checked("empirical_lower", H0 / (1 + F(q, N)), Q0),
                    "haar_endpoint": checked("haar_endpoint", abs(H0 - H1), F(4 * q * ceil_count, N * N)),
                    "empirical_endpoint": checked("empirical_endpoint", abs(Q0 - Q1), F(4, N)),
                }
                if N > q:
                    checks["empirical_upper"] = checked("empirical_upper", Q0, H0 / (1 - F(q, N)))
                changed = list(phases[:N])
                exact_discrepancy = 0
                for i in range(0, N, 3):
                    changed[i] = (-changed[i][0], -changed[i][1])
                    exact_discrepancy += 2
                Hw, Qw, Ew, occupiedw = energies(changed, 0, q, multiplicities)
                checks["haar_phase_stability"] = checked(
                    "haar_phase_stability", abs(Hw - H0), F(2 * q * ceil_count * exact_discrepancy, N * N)
                )
                checks["empirical_phase_stability"] = checked(
                    "empirical_phase_stability", abs(Qw - Q0), F(2 * exact_discrepancy, N)
                )
                cases.append({
                    "p": p, "L": L, "q": q, "N": N, "repetition": repetition,
                    "phase_sha256": sha256(json.dumps(phases, separators=(",", ":")).encode()).hexdigest(),
                    "complete_fiber_count": len(fibers),
                    "occupied_fibers_zero_window": occupied0,
                    "occupied_fibers_one_window": occupied1,
                    "occupied_fibers_changed_window": occupiedw,
                    "energies_zero_window": {"H": str(H0), "Qemp": str(Q0), "E": str(E0)},
                    "energies_one_window": {"H": str(H1), "Qemp": str(Q1), "E": str(E1)},
                    "energies_changed_window": {"H": str(Hw), "Qemp": str(Qw), "E": str(Ew)},
                    "exact_phase_discrepancy": exact_discrepancy,
                    "checks": checks,
                })
    return {
        "status": "all passed",
        "authority": "exact finite Fraction/Gaussian-integer audit; no infinite existence inference",
        "seed": SEED,
        "parameters": PARAMETERS,
        "case_count": len(cases),
        "assertion_count": sum(check_counts.values()),
        "check_counts": check_counts,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": cases,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--log", required=True)
    args = parser.parse_args()
    receipt = run()
    payload = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    Path(args.output).write_text(payload)
    summary = {
        key: value for key, value in receipt.items() if key != "cases"
    }
    summary["receipt_sha256"] = sha256(payload.encode()).hexdigest()
    log = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    Path(args.log).write_text(log)
    print(log, end="")


if __name__ == "__main__":
    main()
