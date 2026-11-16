#!/usr/bin/env python3
"""Replay the bounded translator QA of predictive_horizons.

Production functions are exercised, but expected horizon answers come from
direct repeated walks and all equal-report pairs. Expected monoid membership
comes from an independent coin dynamic program. These are finite checks of
declared tables, not a formal proof or independent physical source.

Run with --repo /path/to/SUCC to override the enclosing checkout.
The default receipt is receipts/differential.json beside this script.
"""

from argparse import ArgumentParser
from dataclasses import replace
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys


def partitions(n):
    for labels in product(range(n), repeat=n):
        if labels[0] != 0:
            continue
        highest = 0
        valid = True
        for label in labels[1:]:
            if label > highest + 1:
                valid = False
                break
            highest = max(highest, label)
        if valid:
            yield labels


def walk(table, x, k):
    for _ in range(k):
        x = table[x]
    return x


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent / "receipts" / "differential.json")
    args = parser.parse_args()
    repo = args.repo.resolve()
    sys.path.insert(0, str(repo))
    from observational_succ.predictive_horizons import (
        AdditiveHorizonMonoid, FiniteReportedSource, HorizonCertificate,
        certify_horizon, compose_horizons, horizon_profile,
        realize_horizon_monoid, verify_horizon, verify_profile,
    )

    sources = checks = compositions = 0
    for n in range(1, 5):
        for trans in product(range(n), repeat=n):
            for reports in partitions(n):
                s = FiniteReportedSource(trans, reports)
                p = horizon_profile(s)
                assert verify_profile(s, p)
                flags = []
                for k in range(25):
                    expected = all(
                        reports[walk(trans, x, k)] == reports[walk(trans, z, k)]
                        for x in range(n) for z in range(x)
                        if reports[x] == reports[z]
                    )
                    assert p.contains(k) == expected, (trans, reports, k)
                    cert = certify_horizon(s, k)
                    assert cert.predictable == expected and verify_horizon(s, cert)
                    flags.append(expected)
                    checks += 1
                yes = [k for k in range(5) if flags[k]]
                for a, b in product(yes, repeat=2):
                    assert flags[a + b]
                    assert verify_horizon(
                        s, compose_horizons(s, certify_horizon(s, a), certify_horizon(s, b))
                    )
                    compositions += 1
                if len(set(trans)) == n:
                    d = next(k for k in range(1, 25) if flags[k])
                    assert all(flag == (k % d == 0) for k, flag in enumerate(flags))
                sources += 1

    monoids = 0
    for r in range(5):
        for gens in combinations(range(1, 10), r):
            m = AdditiveHorizonMonoid(gens)
            dp = [True] + [False] * 300
            for k in range(1, 301):
                dp[k] = any(k >= g and dp[k - g] for g in gens)
            assert [m.contains(k) for k in range(301)] == dp
            s = realize_horizon_monoid(m)
            p = horizon_profile(s)
            assert verify_profile(s, p)
            assert [p.contains(k) for k in range(301)] == dp
            monoids += 1

    s = FiniteReportedSource((1, 2, 3, 0), (0, 0, 1, 1))
    c = certify_horizon(s, 2)
    p = horizon_profile(s)
    cases = []
    for h in (True, -1, 1.2, "2", None):
        cases.append(replace(c, horizon=h))
    for val in ([], [1, 0], (1,), (1, 0, 1), (True, 0), (1, -1), (1, 2), "10", 42):
        cases.append(replace(c, induced=val))
    for val in ([], [0, 1], (0,), (0, 1, 2), (True, 1), (-1, 1), (0, 4), "01", 42):
        cases.append(HorizonCertificate(s.fingerprint, 1, collision=val))
    for x in cases:
        assert verify_horizon(s, x) is False, x
    pcases = []
    for key, vals in [
        ("preperiod", (True, -1, 1.2, "0", None)),
        ("period", (True, 0, -1, 1.2, "4", None)),
        ("admitted", ([True, False, True, False], (1, 0, 1, 0), (), (True,), None, 42)),
    ]:
        for v in vals:
            pcases.append(replace(p, **{key: v}))
    for x in pcases:
        assert verify_profile(s, x) is False, x

    paths = (
        "observational_succ/predictive_horizons.py",
        "tests/test_predictive_horizons.py",
        "research/2026-11-14/knowledge_volume/HORIZON_THEOREMS.md",
    )
    receipt = {
        "status": "PASS",
        "scope": "Finite declared-source differential checks; not a formal or empirical source proof.",
        "source_oracle": "Direct repeated walks; all equal-present-report source-state pairs.",
        "monoid_oracle": "Independent Boolean coin dynamic programming.",
        "all_sources_n_le_4": sources,
        "source_horizons_inclusive": [0, 24],
        "pairwise_horizon_checks": checks,
        "decoder_compositions": compositions,
        "composition_input_horizons_inclusive": [0, 4],
        "permutation_classification": "Checked every permutation source among the enumerated tables.",
        "generator_subsets_size_le_4_from_1_to_9": monoids,
        "membership_and_realization_horizons_each": 301,
        "monoid_horizons_inclusive": [0, 300],
        "malformed_horizon_certificates_rejected": len(cases),
        "malformed_profiles_rejected": len(pcases),
        "failures": 0,
        "unexpected_exceptions": 0,
        "sha256": {path: sha256((repo / path).read_bytes()).hexdigest() for path in paths},
        "audit_script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
