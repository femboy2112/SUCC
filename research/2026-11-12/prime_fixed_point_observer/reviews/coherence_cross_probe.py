"""Independent literal integer and Fraction audit; no project imports.

This preserves the 107,153-assertion path/reference audit and the separately
executed three-assertion authentic-primality control. It is not a new search
campaign or a proof of an unbounded arithmetic assertion.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path


def walk(seq, k):
    x, flags, ok = k, [], True
    for q, r in seq:
        if x % q:
            flags.append(1)
            ok = False
        else:
            flags.append(0)
            x = x // q * r
    return tuple(flags), x, ok


def cell(seq, h):
    a = b = 1
    yes, no = [], []
    for (q, r), bit in zip(seq, h):
        s = b * q // gcd(a, q)
        if bit:
            no.append(s)
        else:
            yes.append(s)
            a, b = a * r, b * q
            g = gcd(a, b)
            a, b = a // g, b // g
    return lcm(*yes) if yes else 1, no


def main():
    counts = Counter()

    def check(group, condition):
        counts[group] += 1
        if not condition:
            raise AssertionError((group, counts[group]))

    pairs = ((2, 1), (3, 2), (5, 2), (7, 5))
    seqs = [seq for n in range(4) for seq in product(pairs, repeat=n)]
    seqs += [((11, 7), (13, 5), (17, 3), (19, 11)),
             ((101, 97), (97, 89), (89, 83)),
             ((29, 17), (43, 31), (17, 3), (31, 2))]
    for seq in seqs:
        a = b = L = 1
        for q, r in seq:
            a, b = a * r, b * q
            g = gcd(a, b)
            a, b = a // g, b // g
            L = lcm(L, b)
        M = F(a, b) * L
        check("prefix_integer", M.denominator == 1)
        check("prefix_descent", L - M >= len(seq))
        for k in list(range(129)) + [L, 2 * L, 3 * L, 997, 1009, 104729]:
            h, f, ok = walk(seq, k)
            check("prefix_admission", ok == (k % L == 0))
            if ok:
                check("prefix_output", f == M * (k // L))
            check("joint_inverse", len(h) == len(seq))
            x = f
            for (q, r), bit in reversed(tuple(zip(seq, h))):
                if not bit:
                    check("reverse_integrality", x % r == 0)
                    x = x // r * q
            check("joint_inverse", x == k)
        for h in product((0, 1), repeat=len(seq)):
            A, no = cell(seq, h)
            empty = any(A % s == 0 for s in no)
            check("sector_emptiness", (walk(seq, A)[0] != h) == empty)
            for k in range(97):
                membership = k % A == 0 and all(k % s for s in no)
                check("sector_membership", membership == (walk(seq, k)[0] == h))

    c1 = {3: F(3, 5), 2: F(4, 5)}
    c2 = {6: F(3, 5), 4: F(4, 5)}
    check("code_orthonormal", sum(x * x for x in c1.values()) == 1)
    check("code_orthonormal", sum(x * x for x in c2.values()) == 1)
    check("code_orthonormal", set(c1).isdisjoint(c2))

    # A maximally entangled input is handled without irrational amplitudes:
    # the vector has norm squared two, and its density is divided by two.
    state = {(n, j): v for j, c in enumerate((c1, c2)) for n, v in c.items()}
    out = {}
    for (n, j), v in state.items():
        bit = int(n % 3 != 0)
        m = n if bit else 2 * (n // 3)
        out[(m, j, bit)] = v
    eta = (F(3, 5), F(4, 5))
    expected = {(m, j, bit): eta[bit]
                for m, j in ((2, 0), (4, 1)) for bit in (0, 1)}
    check("reference_factorization", out == expected)
    rho = defaultdict(F)
    for (m, j, h), a in out.items():
        for (n, k, g), b in out.items():
            if h == g:
                rho[((m, j), (n, k))] += a * b / 2
    ideal = {((m, j), (n, k)): F(1, 2)
             for m, j in ((2, 0), (4, 1)) for n, k in ((2, 0), (4, 1))}
    check("reference_current_density", dict(rho) == ideal)
    check("reference_current_purity",
          sum(rho.get((i, j), 0) * rho.get((j, i), 0) for i, j in rho) == 1)

    erase = {(2, 0): F(1), (3, 1): F(1)}
    erased = {}
    for (n, j), v in erase.items():
        h = int(n % 3 != 0)
        m = n if h else 2 * (n // 3)
        erased[(m, j, h)] = v
    r = defaultdict(F)
    for (m, j, h), a in erased.items():
        for (n, k, g), b in erased.items():
            if h == g:
                r[((m, j), (n, k))] += a * b / 2
    r = {key: v for key, v in r.items() if v}
    check("pure_erasure_reference", r == {
        ((2, 0), (2, 0)): F(1, 2), ((2, 1), (2, 1)): F(1, 2)})
    check("pure_erasure_reference",
          sum(r.get((i, j), 0) * r.get((j, i), 0) for i, j in r) == F(1, 2))

    def prime(n):
        return n >= 2 and all(n % d for d in range(2, n))

    def source_prime_mass(c):
        return sum(v * v for k, v in c.items() if prime(k + 1))

    source_diagonal = (source_prime_mass(c1), source_prime_mass(c2))
    output_diagonal = (F(prime(2 + 1)), F(prime(4 + 1)))
    check("source_prime_semantics", source_diagonal == (F(16, 25), F(1)))
    check("source_prime_semantics", output_diagonal == (F(1), F(1)))
    check("source_prime_semantics", output_diagonal[0] - source_diagonal[0] == F(9, 25))

    this_file = Path(__file__)
    dossier = this_file.parent.parent
    source_paths = ["ARITHMETIC_COHERENCE.md", "COMMON_ROOT_AND_LIMITS.md", "twin_transport.py"]
    return {
        "status": "PASS", "exact_checks": sum(counts.values()), "groups": dict(counts),
        "path_and_reference_checks": sum(v for k, v in counts.items() if k != "source_prime_semantics"),
        "source_semantic_checks": counts["source_prime_semantics"],
        "schedules": len(seqs),
        "reference_case": "Maximally entangled code/reference, normalized at density level by 1/2.",
        "prime_countercontrol": {"source_prime_diagonal": list(map(str, source_diagonal)),
                                 "output_prime_diagonal": list(map(str, output_diagonal)),
                                 "first_diagonal_defect": "9/25",
                                 "source_convention": "epsilon_k corresponds to original positive label k+1"},
        "script_sha256": hashlib.sha256(this_file.read_bytes()).hexdigest(),
        "inspected_source_hashes": {p: hashlib.sha256((dossier / p).read_bytes()).hexdigest()
                                    for p in source_paths},
        "scope": "Finite independent literal integer/Fraction audit; no project implementation imported. Same-model review is not external peer review. Universal results use written proofs.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(main(), indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
    print(rendered, end="")
