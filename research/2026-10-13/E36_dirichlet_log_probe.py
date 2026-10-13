#!/usr/bin/env python3
"""Bounded E36 exact witnesses; finite checks supplement the separate proof.

All source coefficients and responses are integers or Fraction values.
No zero ordinates, floating arithmetic, analytic continuation, or full suite.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
import json
from math import factorial, gcd
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from observational_succ.dirichlet_lambert import (  # noqa: E402
    convolve as imported_convolve,
    star_exp as imported_exp,
    star_log_unit as imported_log,
)

PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
ORIGIN = "ba075348b7bcc66d938b3e0ca96c26e95bba340a"
HORIZON = 64


def unit(n):
    return (Q(0), Q(1)) + (Q(0),) * (n - 1)


def impulse(n, at, value=1):
    result = list(unit(n))
    result[1] = Q(0)
    result[at] = Q(value)
    return tuple(result)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def factors(n):
    out = []
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            exponent += 1
            n //= p
        if exponent:
            out.append((p, exponent))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def mixed(n):
    return len(factors(n)) >= 2


@lru_cache(None)
def paths(n):
    """Enumerate ordered nonunit factors, independently of convolution code."""
    if n == 1:
        return ((),)
    return tuple((d,) + rest for d in range(2, n + 1) if n % d == 0
                 for rest in paths(n // d))


def path_product(values, path):
    value = Q(1)
    for d in path:
        value *= values[d]
    return value


def path_log(a):
    if a[0] != 0 or a[1] != 1:
        raise ValueError("Require reserved index zero and normalized a(1)=1")
    out = [Q(0)] * len(a)
    for n in range(2, len(a)):
        out[n] = sum((Q((-1) ** (len(path) + 1), len(path))
                      * path_product(a, path) for path in paths(n)), Q(0))
    return tuple(out)


def path_exp(b):
    if b[0] != 0 or b[1] != 0:
        raise ValueError("Require augmentation input b(1)=0")
    out = list(unit(len(b) - 1))
    for n in range(2, len(b)):
        out[n] = sum((path_product(b, path) / factorial(len(path))
                      for path in paths(n)), Q(0))
    return tuple(out)


def multiplicativity_defects(a):
    return [(m, n, str(a[m * n] - a[m] * a[n]))
            for m in range(2, len(a))
            for n in range(m, (len(a) - 1) // m + 1)
            if gcd(m, n) == 1 and a[m * n] != a[m] * a[n]]


def mixed_log_defects(b):
    return [(n, str(b[n])) for n in range(2, len(b)) if mixed(n) and b[n]]


def check_source(a):
    b = path_log(a)
    assert b == imported_log(a)
    assert path_exp(b) == a == imported_exp(b)
    defects = multiplicativity_defects(a)
    mixed_defects = mixed_log_defects(b)
    assert bool(defects) == bool(mixed_defects)
    return b, defects, mixed_defects


def local_source(nmax, variant):
    values = list(unit(nmax))
    for n in range(2, nmax + 1):
        value = Q(1)
        for p, k in factors(n):
            value *= Q((p + 2 * k + variant) % 7 - 3, k + 1)
        values[n] = value
    return tuple(values)


def witness(a, n):
    return [{"ordered_factors": path,
             "weight": str(Q((-1) ** (len(path) + 1), len(path))),
             "source_product": str(path_product(a, path)),
             "signed_contribution": str(Q((-1) ** (len(path) + 1), len(path))
                                         * path_product(a, path))}
            for path in paths(n)]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    N = HORIZON
    e = unit(N)
    zeta = (Q(0),) + (Q(1),) * N
    bz, _, _ = check_source(zeta)
    assert all(bz[n] == (Q(1, factors(n)[0][1]) if len(factors(n)) == 1 else 0)
               for n in range(2, N + 1))

    # Exact universal finite-ring power bound, sharp for delta_2.
    L = N.bit_length() - 1
    power = e
    d2 = impulse(N, 2)
    for _ in range(L):
        power = imported_convolve(power, d2)
    assert power[2 ** L] == 1
    assert not any(imported_convolve(power, d2))

    source_cases = []
    for variant in range(8):
        a = local_source(N, variant)
        check_source(a)
        source_cases.append(a)
    for variant in range(8):
        a = (Q(0), Q(1)) + tuple(Q((17 * n + 13 * variant) % 11 - 5,
                                  1 + n % 3) for n in range(2, N + 1))
        check_source(a)
        source_cases.append(a)
    log_additivity_cases = 0
    for a, c in zip(source_cases, reversed(source_cases)):
        ac = imported_convolve(a, c)
        assert path_log(ac) == add(path_log(a), path_log(c))
        log_additivity_cases += 1
    for horizon in (8, 16, 32):
        for a in source_cases:
            assert path_log(a[:horizon + 1]) == path_log(a)[:horizon + 1]

    fake6 = list(zeta)
    fake6[6] = Q(2)
    fake6 = tuple(fake6)
    b6, d6, md6 = check_source(fake6)
    assert b6[6] == 1 and d6[0][:2] == (2, 3)

    # A later mixed coefficient can cancel while an earlier defect survives.
    cancellation = list(fake6)
    cancellation[12] = Q(2)
    cancellation = tuple(cancellation)
    bc, _, _ = check_source(cancellation)
    assert bc[6] == 1 and bc[12] == 0

    # Finite support testing at N=6 cannot certify the infinite source.
    late_fake = list(zeta)
    late_fake[10] = Q(2)
    late_fake = tuple(late_fake)
    blate, _, _ = check_source(late_fake)
    assert blate[:7] == bz[:7] and blate[10] == 1

    # A fake primitive composite impulse survives the complete log intact.
    composite_b = impulse(N, 6)
    composite_a = path_exp(composite_b)
    assert check_source(composite_a)[0] == composite_b
    assert composite_a[2] == composite_a[3] == 0 and composite_a[6] == 1

    # Sum of two genuinely different Euler sources is not generally Euler.
    sign23 = (Q(0),) + tuple(Q((-1) ** sum(k for p, k in factors(n)
                                          if p in (2, 3))) for n in range(1, N + 1))
    mixture = tuple((x + y) / 2 for x, y in zip(zeta, sign23))
    bm, dm, _ = check_source(mixture)
    assert mixture[2] == mixture[3] == 0 and mixture[6] == 1 and bm[6] == 1
    check_source(sign23)

    # Exact pi phase on p=2, transported consistently across every integer.
    phase2 = (Q(0),) + tuple(Q((-1) ** sum(k for p, k in factors(n) if p == 2))
                             for n in range(1, N + 1))
    bp, _, mp = check_source(phase2)
    assert not mp and (bp[2], bp[4], bp[8]) == (Q(-1), Q(1, 2), Q(-1, 3))
    assert bp == tuple(x * chi for x, chi in zip(bz, phase2))
    for a in source_cases[:2]:
        transported = tuple(x * chi for x, chi in zip(a, phase2))
        assert path_log(transported) == tuple(x * chi for x, chi in zip(path_log(a), phase2))
    phase_once = list(zeta)
    phase_once[2] = Q(-1)
    bo, _, _ = check_source(tuple(phase_once))
    assert bo[6] == 2

    # Complete two-factor design: superposition versus convolution composition.
    factorial_cells = {"additive": {}, "convolution": {}}
    for on2 in (0, 1):
        for on3 in (0, 1):
            u = impulse(N, 2, on2)
            v = impulse(N, 3, on3)
            aa = add(e, add(u, v))
            ac = imported_convolve(add(e, u), add(e, v))
            factorial_cells["additive"][f"{on2}{on3}"] = str(path_log(aa)[6])
            factorial_cells["convolution"][f"{on2}{on3}"] = str(path_log(ac)[6])
    factorial_interactions = {}
    for kind, cells in factorial_cells.items():
        interaction = Q(cells["11"]) - Q(cells["10"]) - Q(cells["01"]) + Q(cells["00"])
        factorial_interactions[kind] = str(interaction)
    assert factorial_interactions == {"additive": "-1", "convolution": "0"}
    assert path_log(add(e, d2))[4] == Q(-1, 2)  # Within-prime term remains.
    pointwise_square = tuple(x * x for x in add(e, d2))
    assert path_log(pointwise_square)[2] == 1 != 2 * path_log(add(e, d2))[2]

    # Full log preserves source; projection to prime powers loses mixed defects.
    projected = tuple(b6[n] if len(factors(n)) == 1 else Q(0) for n in range(N + 1))
    reconstructed = path_exp(projected)
    residual = tuple(x - y for x, y in zip(b6, projected))
    assert reconstructed == zeta != fake6
    assert imported_convolve(reconstructed, path_exp(residual)) == fake6

    # Mutation receipt: omit one actual factorization path in the zeta log.
    omitted_path = (3, 2)
    omitted = sum((Q((-1) ** (len(p) + 1), len(p)) * path_product(zeta, p)
                   for p in paths(6) if p != omitted_path), Q(0))
    assert omitted == Q(1, 2)
    mutated_b = list(bz)
    mutated_b[6] = omitted
    mutated_a = path_exp(tuple(mutated_b))
    assert mutated_a[6] == Q(3, 2) != zeta[6]

    # Denominator and analytic boundaries are explicit, not numerical claims.
    assert path_log(add(e, d2))[4].denominator == 2
    truncated_product = imported_convolve(impulse(5, 2), impulse(5, 3))
    assert not any(truncated_product)
    evaluated_product_at_s1 = Q(1, 2) * Q(1, 3)
    assert evaluated_product_at_s1 == Q(1, 6) != 0
    factorial_local = (Q(0),) + tuple(Q(factorial(factors(n)[0][1]))
                                    if len(factors(n)) == 1 and factors(n)[0][0] == 2
                                    else (Q(1) if n == 1 else Q(0))
                                    for n in range(1, N + 1))
    check_source(factorial_local)

    manifest = json.loads((ROOT / "provenance/IMPORT_MANIFEST.json").read_text())
    imported_paths = ["observational_succ/dirichlet_lambert.py",
                      "provenance/origins/fuckingrh/research/2026-10-10/DIRICHLET_LAMBERT_SOURCE_LIFT.md",
                      "provenance/origins/fuckingrh/research/2026-10-10/CERTIFIED_FINITE_PRIME_TRANSPORT.md"]
    provenance = []
    for path in imported_paths:
        entry = next(e for e in manifest["entries"] if e["destination_path"] == path)
        blob = git("hash-object", path)
        assert blob == entry["destination_git_blob_sha"]
        provenance.append({"path": path, "git_blob": blob, "sha256": digest(ROOT / path),
                           "original_path": entry["original_path"],
                           "original_git_blob": entry["original_git_blob_sha"]})

    return {
        "schema": "SUCC-E36-exact-receipt-1", "status": "TESTED MODEL",
        "scope": "Exact rational finite horizon 64; universal theorem proved separately in dossier",
        "parent_commit": PARENT, "execution_head": git("rev-parse", "HEAD"),
        "branch": git("branch", "--show-current"), "source_origin_commit": ORIGIN,
        "origin_manifest_matches": manifest["source_commit"] == ORIGIN,
        "python_version": sys.version.split()[0], "horizon": N,
        "probe_sha256": digest(Path(__file__)),
        "command": "python research/2026-10-13/E36_dirichlet_log_probe.py --receipt research/2026-10-13/E36_DIRICHLET_LOG_RECEIPT.json",
        "exit_code": 0, "imported_provenance": provenance,
        "checks": {"generalized_multiplicative_sources": 8, "arbitrary_sources": 8,
                   "log_convolution_additivity_pairs": log_additivity_cases,
                   "restriction_comparisons": 48, "nilpotence_exponent": L + 1,
                   "nilpotence_sharp_nonzero_index": 2 ** L},
        "zeta_path_witnesses": {"6": witness(zeta, 6), "12": witness(zeta, 12)},
        "controls": {
            "fake_source_a6_2": {"b6": str(b6[6]), "first_multiplicativity_defect": d6[0],
                                 "all_mixed_log_defects": md6},
            "cancellation_a6_a12_2": {"b6": str(bc[6]), "b12": str(bc[12]),
                                       "not_multiplicative": True},
            "late_mutation_a10_2": {"agrees_through_6": True, "b10": str(blate[10])},
            "fake_composite_log_impulse_6": {"a2": "0", "a3": "0", "a6": "1", "b6": "1"},
            "matched_nonEuler_mixture": {"a2": "0", "a3": "0", "a6": "1", "b6": str(bm[6]),
                                         "first_multiplicativity_defect": dm[0]},
            "consistent_prime_phase_pi": {"b2": str(bp[2]), "b4": str(bp[4]),
                                           "b8": str(bp[8]), "mixed_log_defects": []},
            "single_prime_coefficient_phase": {"b6": str(bo[6])},
            "complete_factorial_cells_b6": factorial_cells,
            "complete_factorial_interactions": factorial_interactions,
            "prime_power_projection": {"projects_fake6_to_zeta": True,
                                        "full_log_exp_inverse": True, "residual_split_inverse": True},
            "omitted_ordered_path": {"omitted": omitted_path, "mutated_b6": str(omitted),
                                      "reconstructed_a6": str(mutated_a[6])},
            "integer_ring_not_closed": {"a": "delta_1+delta_2", "b4": "-1/2"},
            "truncated_evaluation_not_a_ring_map": {
                "horizon": 5, "truncated_delta2_star_delta3": "0",
                "product_of_evaluations_at_s1": str(evaluated_product_at_s1)},
            "formal_nonanalytic_source": {"a(2^k)": "k!", "other_prime_local_coefficients": "0",
                                           "finite_prefix_multiplicative": True,
                                           "universal_divergence": "Proved by ratio (k+1)*2^(-sigma), not a finite test"},
        },
        "nonclaims": ["No kernel proof or independently adjudicated theorem promotion",
                      "No analytic continuation, global source authenticity, positivity, RH, or zero inputs",
                      "Imported comparisons share arithmetic provenance; factor-path implementation is separate",
                      "No full suite run under investigator protocol"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    receipt = run()
    payload = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        args.receipt.write_text(payload)
        print(json.dumps({"receipt": str(args.receipt), "sha256": digest(args.receipt),
                          "status": receipt["status"], "horizon": HORIZON,
                          "checks": receipt["checks"], "exit_code": 0}, sort_keys=True))
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
