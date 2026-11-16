#!/usr/bin/env python3
"""Exact finite controls and frozen BBP holdout. Never a normality verdict.

Run from any directory. The source receipt is generated separately by the
existing original-source certifier. The rational controls here reimplement
the four literal poles and do not import the production forcing function.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / "carry_quadrature_assault" / "receipts"
ASSERTIONS = 0


def check(condition: bool, message: str = "audit failure") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def source(n: int) -> F:
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def ell(j: int, c: int) -> int:
    j, c = j % 4, c % 4
    return int(j == 2 and c == 1)+int(j == 3 and c == 2)-int(j == 1 and c == 1)


def gate(c: int) -> int:
    return int(c % 4 in (1, 2))


def q(j: int, k: int) -> int:
    j, k = j % 4, k % 4
    return int(j == 0 and k == 0)+int(k == 1)-int(j < 2 and k < 2)


def frames(j: int, k: int) -> tuple[int, ...]:
    return tuple(q(j-t, k-t) for t in range(4))+tuple(
        q(-j-t, 1-k-t) for t in range(4))


def v2(x: F) -> int:
    if not x:
        return 10**9  # used only in >= checks
    a, b = abs(x.numerator), x.denominator
    return (a & -a).bit_length()-(b & -b).bit_length()


def residue(x: F, bits: int) -> int:
    check(x.denominator % 2 == 1, "dyadic residue outside rational carrier")
    m = 1 << bits
    return x.numerator * pow(x.denominator, -1, m) % m


def periodic_endpoint(digits: tuple[int, ...]) -> F:
    a = 0
    for d in digits:
        a = 16*a+d
    return F(a, 16**len(digits)-1)


def shadow(word: tuple[int, ...], bits: int) -> tuple[F, F]:
    n = len(word)
    beta = periodic_endpoint(tuple(4+c for c in word))
    prefix = sum((source(j)/16**j for j in range(1, n+2)), F(0))
    odd = 2**(bits+4*n+8)+1
    m = ((beta-prefix)*odd/2**bits+F(1, 2)).__floor__()
    return F(2**bits*m, odd), beta


def algebra_controls() -> dict:
    for j, c in product(range(4), repeat=2):
        k = (j-c) % 4
        fs = frames(j, k)
        check(q(j, k) == ell(j, c))
        check(ell(j, c) <= gate(c))
        check(sum(fs[:4]) == int(c == 2))
        check(sum(fs[4:]) == int(c == 1))
        check(sum(fs) == gate(c))
        for value in fs:
            check(value <= gate(c))
        check(ell(j, 0) == ell(j, 3))
        for d in range(4):
            check(abs(ell(j, d)-ell(j, d-1)) <= 1)
    cases = {}
    for name, word in {"haar_cycle_clock_lock": (1, 2, 3, 0),
                       "zero_gate": (0, 0, 0, 0),
                       "positive_clock_cycle": (0, 1, 2, 3)}.items():
        scores = [sum(frames(n % 4, (n-c) % 4)[t]
                      for n, c in enumerate(word, 1)) for t in range(8)]
        d = F(sum(map(gate, word)), 4)
        lb = F(sum(ell(n, c) for n, c in enumerate(word, 1)), 4)
        check(d/8 <= F(max(scores), 4) <= d)
        cases[name] = {"word": list(word), "L": str(lb), "d": str(d),
                       "eight_frame_counts": scores}
    check(cases["haar_cycle_clock_lock"]["L"] == "-1/4")
    check(cases["haar_cycle_clock_lock"]["d"] == "1/2")
    check(sum(ell(j, c) for j, c in product(range(4), repeat=2)) == 1)
    check(sum(gate(c) for j, c in product(range(4), repeat=2)) == 8)
    distribution = Counter()
    for word in product(range(4), repeat=4):
        distribution[sum(ell(n, c) for n, c in enumerate(word, 1))] += 1
    check(distribution == {-1: 36, 0: 132, 1: 76, 2: 12})
    for z in (F(1, 3), F(1, 2), F(1), F(2), F(3)):
        mgf = sum((F(v, 256)*z**k for k, v in distribution.items()), F(0))
        check(mgf == (3+z)**2*(3+1/z)/64)
    z = (math.sqrt(73)-1)/12
    m = (3+z)**2*(3+1/z)/64
    z32 = (1+8*math.sqrt(19))/45
    m32 = (3+z32)**2*(3+1/z32)/64
    i32 = math.log(z32)/32-math.log(m32)/4
    return {"exact_controls": cases,
            "four_slot_score_distribution": dict(distribution),
            "entropy_threshold_approximations_only": {
                "tilt": z, "M_min": m,
                "signed_budget_bits_per_digit": 4+math.log2(m)/4,
                "budget_1_over_32_bits_per_digit": 4-i32/math.log(2),
                "bad_shell_dimension_upper_bound": 1+math.log(m)/(8*math.log(16)),
                "gate_zero_max_bits_per_digit": 3}}


def rational_shadow_controls() -> dict:
    positions = 0
    records = []
    for n, bits, kind in product((1, 2, 4, 8, 16, 32, 64), (2, 17, 80),
                                ("zero", "locked", "mixed")):
        if kind == "zero":
            word = (0,)*n
        elif kind == "locked":
            word = tuple(j % 4 for j in range(1, n+1))
        else:
            word = tuple((j*j+3*j+1) % 4 for j in range(1, n+1))
        s, beta = shadow(word, bits)
        bound = 2**(bits+4*n+8)+1
        check(0 < s < 1)
        check(v2(s) >= bits)
        check(max(abs(s.numerator), s.denominator) <= bound)
        u, us = F(0), s
        for j, c in enumerate(word, 1):
            u, us = 16*u+source(j), 16*us+source(j)
            check(us-u == 16**j*s)
            check(v2(us-u) >= bits+4*j)
            check(us.__floor__() % 4 == c)
            check(residue(u, 2) == residue(us, 2) == j % 4)
            check(residue(us-us.__floor__(), 2) == (j-c) % 4)
            check(us.__floor__() == (16**j*beta).__floor__())
            positions += 1
        records.append({"N": n, "bits": bits, "word_type": kind,
                        "seed_numerator_bits": s.numerator.bit_length(),
                        "seed_denominator_bits": s.denominator.bit_length()})
    return {"status": "FINITE_EXACT_CONTROLS_NOT_CANONICAL_ZERO_SEED",
            "positions": positions, "cases": records,
            "quantifiers": "for every finite N,L,word there exists a rational seed"}


def denominator_grid_control() -> dict:
    b, bits = 8, 48
    odd_grid = math.lcm(*range(1, 8*b, 2))
    check(odd_grid == 18472920064106597929865025)
    check(F(2**bits, odd_grid) < F(1, 16**(b-1)))
    s = F(-117004818048662636658688, 595900647229245094511775)
    check(v2(s) == 16)
    u, us = F(0), s
    rows = []
    for n in range(1, 2*b):
        u, us = 16*u+source(n), 16*us+source(n)
        check(residue(us, 2) == n % 4)
        if n >= b:
            check(math.lcm(*range(1, 8*n, 2)) % us.denominator == 0)
            check(v2(us-u) >= bits+4*(n-b))
            c = us.__floor__() % 4
            rows.append({"n": n, "c": c, "K": residue(us-us.__floor__(), 2),
                         "ell": ell(n, c)})
        if n == b:
            check(us == F(6311125010945226836920984, 2052546673789621992207225))
    check([r["c"] for r in rows] == [3, 1, 3, 3, 3, 1, 3, 3])
    check(sum(r["ell"] for r in rows) == -2)
    return {"status": "CHANGED_SEED_EXACT_CONTROL", "B": b, "state_bits": bits,
            "seed": str(s), "L": "-1/4", "rows": rows}


def borrow_mask_controls() -> dict:
    # Exact synthetic tails are admissible for the GENERAL mask lemma. They
    # are not asserted to be BBP tails or source samples.
    endpoints = (F(0), F(1, 16**8), F(1, 15),
                 periodic_endpoint((1,)+(0,)*7),
                 periodic_endpoint((5, 6, 7, 4)),
                 periodic_endpoint((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)))
    checks = 0
    for beta in endpoints:
        rows = []
        for n in range(1, 257):
            v = 16**n*beta
            completed = v.__floor__()
            raw = (v-F(1, 128*n*n)).__floor__()
            check(raw in (completed, completed-1))
            rows.append((n, completed % 4, raw % 4))
        for b in range(1, 129):
            m = (64*b*b).bit_length()-1
            m //= 4
            count_bound = 1+(b-1)//(m+1)
            masks = [lambda j, c: gate(c), ell]
            masks += [lambda j, c, t=t: frames(j, (j-c) % 4)[t] for t in range(8)]
            for mask in masks:
                affected = [n for n, c, a in rows[b-1:2*b-1]
                            if mask(n, c) != mask(n, a)]
                check(len(affected) <= count_bound)
                check(all(y-x >= m+1 for x, y in zip(affected, affected[1:])))
                checks += 1
    # Remove f(0)=f(3): beta=0 and any positive tail produce a discrepancy
    # at every position, so the claimed vanishing bound must fail.
    b = 16
    m = ((64*b*b).bit_length()-1)//4
    bound = 1+(b-1)//(m+1)
    check(b > bound)
    return {"synthetic_admissible_tail_shell_checks": checks,
            "seam_mutation": {"endpoint": "0", "mask": "1[c=3]",
                              "B": b, "discrepancies": b,
                              "false_unmatched_seam_bound": bound},
            "scope": "controls of the general mask theorem, not BBP evidence"}


def holdout() -> dict:
    fresh = HERE / "receipts" / "fresh_source"
    residues = (fresh / "carry_residues_mod4.txt").read_text().strip()
    prefix = (fresh / "bbp_prefix_hex.txt").read_text().strip()
    report = json.loads((fresh / "finite_probe.json").read_text())
    old = (PARENT / "carry_residues_mod4.txt").read_text().strip()
    check(len(residues) == report["horizon"] == 131072)
    check(len(old) == 32768)
    check(residues[:len(old)] == old)
    check(hashlib.sha256(residues.encode()).hexdigest() == report["residues_sha256"])
    check(hashlib.sha256(prefix.encode()).hexdigest() == report["prefix_sha256"])
    # Independent literal-four-pole Fraction implementation, sharing only
    # the mathematical source formula, cross-checks the first 512 states.
    u = F(0)
    for n in range(1, 513):
        u = 16*u+source(n)
        check(u.__floor__() % 4 == int(residues[n-1]))
        check(residue(u, 2) == n % 4)
    arrays = [[0] for _ in range(5)]
    for n, raw in enumerate(residues, 1):
        c = int(raw)
        j, k = n % 4, (n-c) % 4
        vals = (int(j == k == 0), int(k == 1), int(j < 2 and k < 2),
                ell(j, c), gate(c))
        for a, v in zip(arrays, vals):
            a.append(a[-1]+v)
    def shell(b: int) -> dict:
        a, c, f, l, d = [p[2*b-1]-p[b-1] for p in arrays]
        check(l == a+c-f)
        check(d >= l)
        error = max(F(1, 16)-F(a, b), F(0))
        error += max(F(1, 4)-F(c, b), F(0))
        error += max(F(f, b)-F(1, 4), F(0))
        check(F(l, b) >= F(1, 16)-error)
        return {"B": b, "F1_count": a, "c1_count": c, "F2_count": f,
                "L_count": l, "selected_count": d,
                "L": F(l, b), "d": F(d, b), "one_sided_error": error}
    minima = {"L": None, "d": None}
    min_at = {"L": [], "d": []}
    max_error, max_at = F(-1), []
    failures = []
    for b in range(32769, 65537):
        row = shell(b)
        for name in minima:
            value = row[name]
            if minima[name] is None or value < minima[name]:
                minima[name], min_at[name] = value, [b]
            elif value == minima[name]:
                min_at[name].append(b)
        e = row["one_sided_error"]
        if e > max_error:
            max_error, max_at = e, [b]
        elif e == max_error:
            max_at.append(b)
        if e > F(1, 32):
            failures.append(b)
    selected_rows = {b: shell(b) for b in
                     sorted(set((32769, 65536)+tuple(min_at["L"])+tuple(
                         min_at["d"])+tuple(max_at)))}
    return {"status": "FINITE_PASS" if not failures else "FINITE_FAIL",
            "normality_proved": False, "source_budget_proved": False,
            "fresh_n_start": 32769, "certified_horizon": 131072,
            "all_integer_B_range": [32769, 65536], "shells_tested": 32768,
            "minimum_L": str(minima["L"]), "minimum_L_at_B": min_at["L"],
            "minimum_selected_density": str(minima["d"]),
            "minimum_selected_density_at_B": min_at["d"],
            "maximum_one_sided_error": str(max_error),
            "maximum_one_sided_error_at_B": max_at,
            "predeclared_tolerance": "1/32", "failing_B": failures,
            "extremal_and_endpoint_shells": [
                {k: str(v) if isinstance(v, F) else v for k, v in row.items()}
                for row in selected_rows.values()],
            "overlap_exact_match": True, "independent_fraction_horizon": 512,
            "borrow_indices": report["borrow_indices"],
            "source_hashes": {k: report[k] for k in
                              ("prefix_sha256", "residues_sha256")}}


def main() -> None:
    report = {"status": "EXACT_FINITE_AUDIT_ONLY",
              "normality_proved": False, "authentic_source_budget_proved": False,
              "algebra": algebra_controls(),
              "rational_shadows": rational_shadow_controls(),
              "denominator_grid_control": denominator_grid_control(),
              "borrow_masks": borrow_mask_controls(),
              "fresh_holdout": holdout()}
    report["assertions_passed"] = ASSERTIONS
    output = HERE / "receipts" / "independent_audit.json"
    output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": report["status"], "assertions": ASSERTIONS,
                      "holdout": report["fresh_holdout"],
                      "entropy": report["algebra"]["entropy_threshold_approximations_only"]},
                     indent=2))


if __name__ == "__main__":
    main()
