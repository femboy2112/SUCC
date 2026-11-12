#!/usr/bin/env python3
"""Replay the preregistered finite regions and write an exact JSON receipt."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))

import prime_observer as po
from lambda_observer import prime_prefix, program_sha256


def run() -> dict:
    counts = Counter()
    def require(condition, family):
        counts[family] += 1
        if not condition:
            raise AssertionError(f"failed {family} check {counts[family]}")

    limit = 10000
    flags = po.sieve_mask(limit)
    # Independent divisor-count source: add one for each divisor's multiples.
    divisor_counts = [0] * (limit + 1)
    for d in range(1, limit + 1):
        for n in range(d, limit + 1, d):
            divisor_counts[n] += 1
    for n in range(2, limit + 1):
        energy = po.factor_energy(n)
        require(energy == divisor_counts[n] - 2, "divisor_incidence")
        require((energy == 0) == bool(flags[n]), "prime_fixed_labels")
        require(po.least_divisor(po.least_divisor(n)) == po.least_divisor(n), "retraction")
        for r in (0, 1, 2, 7):
            require(0 <= Q(1, (energy + 1) ** r) - flags[n] <= Q(1, 2 ** r), "filter_error")

    selected = (4, 6, 20, 100, 512, 2048, 2458, 4096, 8192, 16384)
    spectra = []
    targets = tuple(range(4, 2050, 2)) + selected[6:]
    all_flags = po.sieve_mask(max(targets))
    for N in targets:
        receipt = po.pair_spectral_receipt(N)
        mask = all_flags[2:N - 1]
        expected = sum(mask[i] * mask[-i - 1] for i in range(len(mask)))
        stats = po.reflection_statistics(mask)
        require(receipt["floor"] == expected == receipt["zero_modes"], "spectral_floor")
        require(0 <= Q(receipt["trace_error"]) <= Q(receipt["error_upper"]) < 1, "trace_error")
        require(stats["commutator_hs_squared"] == 2 * (sum(mask) - expected), "reflection")
        require(expected % 2 == all_flags[N // 2], "exchange_parity")
        if N in selected:
            spectra.append({"spectral": receipt, "reflection": stats})

    haar = []
    for n in (100, 256, 1024, 4096):
        a, b = po.midpoint_masks(n)
        raw = po.haar_overlap(a, b)
        odd_a = tuple(bit if (n+d) % 2 else 0 for d, bit in enumerate(a))
        odd_b = tuple(bit if (n-d) % 2 else 0 for d, bit in enumerate(b))
        filtered = po.haar_overlap(odd_a, odd_b)
        quotient = po.haar_overlap(*po.midpoint_masks(n, quotient_parity=True))
        for entry in (raw, filtered, quotient):
            require(Q(entry["constant"]) + Q(entry["detail"]) == entry["overlap"], "haar")
        require(raw["overlap"] == quotient["overlap"], "parity_quotient")
        haar.append({"n": n, "raw": raw, "parity_filtered_full_grid": filtered,
                     "parity_quotient": quotient})

    crt = []
    for z in (2, 3, 5, 7):
        previous_lower, previous_upper = 0, 1024
        for width in (128, 64, 32, 16, 8, 4, 2, 1):
            c = po.crt_haar_certificate(1024, z, width)
            require(previous_lower <= c["lower"] <= c["interior_actual"] <= c["upper"] <= previous_upper,
                    "crt_refinement")
            require(po.minimum_overlap_model(c)["overlap"] == c["lower"], "frechet_sharpness")
            require(po.minimum_overlap_model(c, preserve_center=True)["overlap"] == c["coherent_lower"],
                    "coherent_frechet_sharpness")
            crt.append({k: v for k, v in c.items() if k != "rows"})
            previous_lower, previous_upper = c["lower"], c["upper"]

    real100 = po.reflection_statistics(all_flags[2:99])
    fake_mask = tuple(int(po.transported_energy(k) == 0) for k in range(2, 99))
    fake100 = po.reflection_statistics(fake_mask)
    fake_spectrum = po.pair_spectral_receipt(100, transported=True)
    require(real100["prime_sector"] == fake100["prime_sector"] == 25, "hostile_relabel")
    require(real100["ordered_pairs"] == 12 and fake100["ordered_pairs"] == 0, "hostile_relabel")
    require(sum(all_flags[2:99:2]) == sum(fake_mask[::2]) == 1, "hostile_relabel")
    require(fake_spectrum["floor"] == 0 < Q(fake_spectrum["trace"]), "hostile_soft_trace")
    require(po.transported_product(2, 9) == 106 != po.transported_product(2, 8) + 2 == 18,
            "hostile_braid")

    coarse = po.crt_haar_certificate(1024, 2, 128)
    require(po.minimum_overlap_model(coarse)["overlap"] == 0 < coarse["interior_actual"] == 25,
            "hostile_coarse_observer")

    mutation_count = 0
    good = po.pair_spectral_receipt(100)
    for field, wrong in (("r", True), ("floor", 13), ("zero_modes", 0), ("trace", "13"),
                         ("source", "unlabelled"), ("universal_goldbach_proved", True)):
        require(not po.verify_pair_spectral_receipt(dict(good, **{field: wrong})), "mutation_rejection")
        mutation_count += 1
    require(po.verify_pair_spectral_receipt(good), "independent_receipt_replay")

    beta = prime_prefix(30).as_dict()
    expected_prefix = tuple(k for k in range(2, 114) if all_flags[k])
    require(beta["status"] == "COMPLETE" and beta["values"] == expected_prefix, "beta_stream")
    require(beta["beta_steps"] > 0 and beta["delta_steps"] > 0, "beta_stream")
    budget = prime_prefix(30, 0).as_dict()
    require(budget["status"] == "UNKNOWN" and budget["values"] == (), "budget_control")

    code_files = ("prime_observer.py", "lambda_observer.py", "test_prime_observer.py",
                  "test_lambda_observer.py", "cylinder.py", "test_cylinder.py", "probe.py")
    hashes = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in code_files}
    inherited = ROOT / "observational_succ/c_monoid_succ_embedding.py"
    return {
        "schema": "SUCC-prime-fixed-point-finite-v1",
        "base_commit": "071ce1e0ee6ab8f8c07113e901131aa646d6b95d",
        "arithmetic_interval": [2, limit], "all_even_targets": [4, 2048],
        "additional_targets": list(selected[6:]), "checks": dict(sorted(counts.items())),
        "total_checks": sum(counts.values()), "failures": 0,
        "mutation_rejections": mutation_count,
        "spectral_samples": spectra, "haar_samples": haar, "crt_samples": crt,
        "hostile_transport": {"actual": real100, "transported": fake100,
                              "transported_spectral": fake_spectrum,
                              "V2S_at_8": 106, "S2V2_at_8": 18},
        "coarse_counterfeit": {"n": 1024, "z": 2, "width": 128,
                               "A": sum(row["A"] for row in coarse["rows"]),
                               "B": sum(row["B"] for row in coarse["rows"]),
                               "actual_overlap": 25, "fake_overlap": 0},
        "beta_prefix": beta, "zero_budget_control": budget,
        "program_sha256": program_sha256(), "code_sha256": hashes,
        "inherited_beta_kernel_sha256": hashlib.sha256(inherited.read_bytes()).hexdigest(),
        "universal_results_are_proved_by_finite_checks": False,
        "goldbach_proved": False, "pi_normality_proved": False, "RH_proved": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "receipts/FINITE_REPORT.json")
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "total_checks": report["total_checks"],
                      "failures": report["failures"], "beta_prefix": report["beta_prefix"]},
                     indent=2, sort_keys=True))
