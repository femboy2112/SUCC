#!/usr/bin/env python3
"""E40 exact finite linear zero-discrimination probe; stdlib only.

The universal statements are proved in DOSSIER.md. This program checks
finite rational instances and preserved hostile witnesses, not RH or a
physical observation. Resource limits are part of the probe contract.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path
import random
import resource

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
ANCHORS = {
    "observational_succ/dynamic_fourier_tower.py": "4e05012124b4aea62e8ddcbc0f5ee6cd202efb389a053cf277a14a102e0419fd",
    "observational_succ/virtual_mellin_zeros.py": "9a8fe4dec3c3900e31f1aacf57442db6b90fd546552d97a9ee3f893f683f7310",
    "provenance/IMPORT_MANIFEST.json": "2eec9a3a730afdca338f92fbaf195e65130cec21efc68062206163f9f6a0d57f",
    "research/2026-10-12/DYNAMIC_FOURIER_VIRTUAL_ZERO_FRONTIER.md": "b31c8eff1faca63f092d9bd33e16544ca17806fe91132ad04691344f92fcb3f3",
}


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F())


def act(a, x):
    return [dot(row, x) for row in a]


def mul(a, b):
    return [[dot(row, col) for col in zip(*b)] for row in a]


def rowact(c, a):
    return [dot(c, col) for col in zip(*a)]


def identity(d):
    return [[F(i == j) for j in range(d)] for i in range(d)]


def rank(a):
    rows = [[F(x) for x in row] for row in a]
    if not rows:
        return 0
    pivot = 0
    for col in range(len(rows[0])):
        idx = next((j for j in range(pivot, len(rows)) if rows[j][col]), None)
        if idx is None:
            continue
        rows[pivot], rows[idx] = rows[idx], rows[pivot]
        v = rows[pivot][col]
        rows[pivot] = [x/v for x in rows[pivot]]
        for j in range(len(rows)):
            if j != pivot:
                v = rows[j][col]
                rows[j] = [x-v*y for x, y in zip(rows[j], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def solve(a, b):
    d = len(a)
    rows = [[F(x) for x in row] + [F(v)] for row, v in zip(a, b)]
    for col in range(d):
        idx = next((j for j in range(col, d) if rows[j][col]), None)
        if idx is None:
            raise ValueError("singular resolvent excluded by theorem")
        rows[col], rows[idx] = rows[idx], rows[col]
        v = rows[col][col]
        rows[col] = [x/v for x in rows[col]]
        for j in range(d):
            if j != col:
                v = rows[j][col]
                rows[j] = [x-v*y for x, y in zip(rows[j], rows[col])]
    return [row[-1] for row in rows]


def inverse(a):
    return [list(row) for row in zip(*(solve(a, col) for col in identity(len(a))))]


def determinant(a):
    # An independent, deliberately small Leibniz oracle for witness minors.
    d = len(a)
    total = F()
    for perm in itertools.permutations(range(d)):
        parity = sum(perm[i] > perm[j] for i in range(d) for j in range(i+1, d))
        term = F((-1)**parity)
        for i in range(d):
            term *= a[i][perm[i]]
        total += term
    return total


def responses(t, b, c, s):
    d = len(t)
    a = [[F(s)*(i == j)-t[i][j] for j in range(d)] for i in range(d)]
    r = solve(a, b)
    assert act(a, r) == list(b)
    rows, values, h = [], [], []
    ck = list(c)
    for _ in range(d):
        rows.append(ck)
        values.append(dot(ck, r))
        h.append(dot(ck, b))
        ck = rowact(ck, t)
    # Distinct representation: finite trace coefficients versus spectral solve.
    assert all(v == 0 for v in values) == all(v == 0 for v in h)
    # Global kernel invariance is checked by row-span containment, not a flag.
    assert rank(rows + [ck]) == rank(rows)
    return {"resolvent_source": r, "delayed_readouts": values,
            "markov_prefix": h, "observability_rank": rank(rows),
            "trace_blackout": all(v == 0 for v in h)}


def nilpotent(d):
    return [[F(i == j+1) for j in range(d)] for i in range(d)]


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pmul(p, q):
    out = [F()]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def prem(p, q):
    p, q = trim(p), trim(q)
    if q == [F()]:
        raise ValueError("zero divisor")
    while p != [F()] and len(p) >= len(q):
        shift, v = len(p)-len(q), p[-1]/q[-1]
        for j, x in enumerate(q):
            p[shift+j] -= v*x
        p = trim(p)
    return p


def pgcd(p, q):
    p, q = trim(p), trim(q)
    while q != [F()]:
        p, q = q, prem(p, q)
    return [x/p[-1] for x in p] if p != [F()] else p


def exact_encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): exact_encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [exact_encode(v) for v in value]
    return value


def run():
    repo = Path(__file__).resolve().parents[4]
    actual = {name: hashlib.sha256((repo/name).read_bytes()).hexdigest()
              for name in ANCHORS}
    assert actual == ANCHORS, "frozen source-anchor mismatch"
    t, b = nilpotent(2), [F(1), F(0)]
    c = [F(1), F(-1)]
    minimal = responses(t, b, c, F(1))
    base_response = responses(t, b, [F(1), F(0)], F(1))["delayed_readouts"][0]
    assert base_response == 1
    assert minimal["resolvent_source"] == [1, 1]
    assert minimal["delayed_readouts"] == [0, -1]
    assert minimal["observability_rank"] == 2
    h = [F(1), F(-1), F(0)]
    hankel = [[h[i+j] for j in range(2)] for i in range(2)]
    assert determinant(hankel) == -1

    sharp = []
    for d in range(2, 7):
        a = F(3, 2)
        ts, bs = nilpotent(d), [F(i == 0) for i in range(d)]
        cs = [F(i == d-2)-a*(i == d-1) for i in range(d)]
        rec = responses(ts, bs, cs, a)
        assert rec["delayed_readouts"] == [F()]*(d-1)+[F(-1)]
        x, moments = bs, []
        for _ in range(2*d-1):
            moments.append(dot(cs, x))
            x = act(ts, x)
        hd = [[moments[i+j] for j in range(d)] for i in range(d)]
        det = determinant(hd)
        assert det == (-1)**(d*(d-1)//2)*(-a)**d
        rec.update({"d": d, "T": ts, "b": bs, "C": cs, "s": a,
                    "hankel_determinant": det})
        sharp.append(rec)

    one_dim_checks = 0
    for tv, bv, cv, sv in itertools.product(range(-2, 3), repeat=4):
        if bv and cv and sv != tv:
            rec = responses([[F(tv)]], [F(bv)], [F(cv)], F(sv))
            assert rec["delayed_readouts"][0] != 0
            one_dim_checks += 1

    rng = random.Random(401310)
    checked, singular, blackouts, similarities = 0, 0, 0, 0
    for d in range(2, 6):
        for _ in range(90):
            ts = [[F(rng.randrange(-2, 3)) for _ in range(d)] for _ in range(d)]
            bs = [F(rng.randrange(-2, 3)) for _ in range(d)]
            cs = [F(rng.randrange(-2, 3)) for _ in range(d)]
            sv = F(rng.choice([-3, -1, 0, 1, 3]))
            try:
                rec = responses(ts, bs, cs, sv)
            except ValueError:
                singular += 1
                continue
            checked += 1
            blackouts += rec["trace_blackout"]
            s = identity(d)
            s[0][1] = F(2)
            si = inverse(s)
            transported = responses(mul(mul(s, ts), si), act(s, bs), rowact(cs, si), sv)
            assert transported["delayed_readouts"] == rec["delayed_readouts"]
            assert transported["resolvent_source"] == act(s, rec["resolvent_source"])
            assert transported["observability_rank"] == rec["observability_rank"]
            similarities += 1

    invisible = responses([[1, 0], [0, 2]], [0, 1], [1, 0], F(3))
    assert invisible["trace_blackout"] and invisible["resolvent_source"] != [0, 0]
    factorial = []
    for dynamics, sensor in itertools.product((0, 1), repeat=2):
        tf = t if dynamics else [[F(0)]*2 for _ in range(2)]
        cf = c if sensor else [F(1), F(0)]
        val = responses(tf, b, cf, F(1))["delayed_readouts"][0]
        factorial.append({"nilpotent_dynamics": dynamics, "difference_sensor": sensor,
                          "scalar_response": val})
    v = [cell["scalar_response"] for cell in factorial]
    interaction = v[3]-v[2]-v[1]+v[0]
    assert v == [1, 1, 1, 0] and interaction == -1

    source_factor = pmul(pmul([-2, 1], [-2, 1]), [1, 1])
    aux1, aux2 = [-3, 1], [-5, 1]
    visible_gcd = pgcd(pmul(source_factor, aux1), pmul(source_factor, aux2))
    forged_gcd = pgcd(pmul(source_factor, aux1), pmul(source_factor, aux1))
    assert visible_gcd == source_factor
    assert forged_gcd == pmul(source_factor, aux1)
    composite_aux_gcd = pgcd([1, 0, 1], [1, 0, 0, 0, 0, 0, 1])
    assert composite_aux_gcd == [1, 0, 1]
    cross_defect = pmul(aux2, pmul(source_factor, aux1))
    wrong_factor = [1, 1]
    other_side = pmul(aux1, pmul(wrong_factor, aux2))
    assert cross_defect != other_side
    tiny = []
    for sv in (10, 100, 1000):
        g = responses(t, b, c, F(sv))["delayed_readouts"]
        tiny.append({"s": sv, "readouts": g, "squared_norm": dot(g, g)})
    assert tiny[0]["squared_norm"] > tiny[1]["squared_norm"] > tiny[2]["squared_norm"]

    def prime(n):
        return n >= 2 and all(n % j for j in range(2, isqrt(n)+1))

    assert prime(2) and prime(3) and not prime(8)
    return exact_encode({
        "schema": "E40-exact-projection-zero-crucible-v1",
        "source_parent": BASE, "anchor_sha256": actual,
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "resource_limits": {"address_space_bytes": 256*1024**2, "cpu_seconds": 20},
        "minimal_mutation": {"T": t, "b": b, "base_C": [1, 0], "mutated_C": c,
                             "s": 1, "base_response": base_response, "mutated": minimal,
                             "hankel": hankel, "hankel_determinant": -1},
        "sharp_delay_family": sharp,
        "one_dimensional_nonzero_checks": one_dim_checks,
        "seeded_controls": {"seed": 401310, "attempts": 360, "regular_checks": checked,
                            "excluded_singular": singular, "trace_blackouts": blackouts,
                            "fully_transported_similarities": similarities},
        "genuine_unobservable_source": invisible,
        "complete_factorial": {"cells": factorial, "mixed_difference": interaction,
                               "mechanism_inferred_from_interaction": False},
        "analytic_polynomial_control": {"constant_first_source_factor": source_factor,
            "auxiliary_gcd": pgcd(aux1, aux2), "recovered_common_divisor": visible_gcd,
            "duplicate_auxiliary_common_divisor": forged_gcd,
            "incompatible_cross_square_rejected": True},
        "prime_and_non_euler_controls": {"true_scales": [2, 3], "composite_scale_rejected": 8,
            "scale2_scale8_auxiliary_polynomial_gcd": composite_aux_gcd,
            "authentic_b6": F(1)-F(1)*F(1), "matched_fake_b6": F(2)-F(1)*F(1),
            "zero_positions_used_as_inputs": False,
            "full_gamma_pole_or_Weil_form_constructed": False},
        "no_uniform_lower_bound_control": tiny,
        "all_exact_assertions_passed": True,
        "claim_boundaries": {"mathematical_model_only": True, "physical_source_attestation": False,
            "basis_change_removes_fixed_target_zero": False,
            "finite_samples_prove_unknown_dimension_bound": False,
            "independent_principal_review_completed": False, "RH_proved": False},
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    payload = run()
    if args.verify:
        assert json.loads(args.verify.read_text()) == payload, "saved receipt mismatch"
        print(json.dumps({"receipt_verified": True, "source_parent": BASE}, sort_keys=True))
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
