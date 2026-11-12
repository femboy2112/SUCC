"""Reproducible exact finite controls for the prime-wave carrier addendum."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path

from cylinder import omega
import prime_observer as po
import prime_waves as pw

PARENT_COMMIT = "b3ddf81c4e893866aac04903f682fb5aa01830e2"


def run_probe() -> dict:
    checks = Counter()

    def require(condition: bool, group: str) -> None:
        checks[group] += 1
        if not condition:
            raise AssertionError(f"prime-wave probe failed: {group}")

    # Trial-divisor producer versus multiples-marking reference.
    bound = 10000
    reference = po.sieve_mask(bound)
    produced = pw.corrected_prime_mask(bound)
    for n in range(bound + 1):
        require(produced[n] == reference[n], "corrected_sieve_vs_marking")
    for n in range(1, 257):
        value = sum(pw.valuation_from_pulses(p, n)
                    for p in pw.primes_through(n))
        require(value == omega(n), "prime_power_degree_reconstruction")
    require(pw.corrected_prime_mask(49, 5)[49] == 1 and
            pw.corrected_prime_mask(49, 7)[49] == 0, "fixed_cutoff_alias")
    require(all(pw.divisor_pulse(p, 2) == pw.divisor_pulse(p, 4)
                for p in pw.primes_through(100)), "multiplicity_blindness")

    for p in pw.primes_through(47):
        require(sum(pw.survivor_wave(p, n) for n in range(p)) == p,
                "mean_one_packet")
        for target in range(2 * p):
            direct = sum(pw.survivor_wave(p, n) * pw.survivor_wave(p, target - n)
                         for n in range(p)) / p
            require(direct == pw.local_pair_factor(p, target), "local_interference")
    for primes in ((), (2,), (3,), (2, 3), (2, 3, 5), (2, 3, 5, 7)):
        for target in range(4, 258):
            row = pw.periodic_pair_receipt(primes, target)
            require(row["count"] == row["crt_count"], "crt_pair_count")
            require(row["normalized_correlation"] == row["factor_product"],
                    "crt_wave_product")

    for target in tuple(range(4, 513)) + (514, 582, 997, 1024, 4096):
        cutoff = isqrt(target - 2)
        row = pw.endpoint_decomposition(target, cutoff)
        require(row["total"] == pw.pair_count(reference, target),
                "endpoint_corrected_pair_count")
    require(pw.endpoint_decomposition(4, 2)["total"] == 1, "prime2_diagonal")
    require(pw.endpoint_decomposition(7, 2)["total"] == 2 and
            pw.local_pair_factor(2, 7) == 0, "odd_target_endpoint")
    interval_control = pw.periodic_pair_receipt((2, 3, 5), 16)
    require(interval_control["normalized_correlation"] == Fraction(45, 32) and
            pw.endpoint_decomposition(16, 5)["bulk_pairs"] == 0 and
            pw.endpoint_decomposition(16, 5)["mixed_pairs"] == 4,
            "positive_period_empty_interval")

    a, b = pw.HOMOMETRIC_A, pw.HOMOMETRIC_B
    differences = pw.difference_histogram(a)
    require(differences == pw.difference_histogram(b), "full_intensity_countermodel")
    require(pw.sum_histogram(a).get(8, 0) == 2 and
            pw.sum_histogram(b).get(8, 0) == 0, "coherent_sum_discriminates")
    require(a != b and tuple(sorted(21 - x for x in a)) != b,
            "noncongruent_homometry")

    for n in range(1, 2501):
        require(pw.mod30_relabel(pw.mod30_relabel(n)) == n, "transport_involution")
        require(pw.mod30_relabel(n) % 30 == n % 30, "transport_residue")
        for p in (2, 3, 5):
            require(pw.divisor_pulse(p, pw.mod30_relabel(n)) ==
                    pw.divisor_pulse(p, n), "transport_preserves_small_projectors")
    for window in (713, 1024, 2048):
        require(pw.residue_degree_histogram(window, 30) ==
                pw.residue_degree_histogram(window, 30, transported=True),
                "whole_finite_phase_bank")
    fake = (0, 0) + tuple(int(omega(pw.mod30_relabel(n)) == 1)
                         for n in range(2, 29))
    require((pw.pair_count(reference, 30), pw.pair_count(fake, 30)) == (6, 0),
            "ordinary_sum_fiber_changed")
    require(pw.mod30_product(2, 1) == 2 and pw.mod30_product(2, 7) == 434 and
            pw.mod30_product(2, 6) + 2 == 14, "anchor_survives_braid_fails")

    labels = (2, 3, 5, 7)
    sums = pw.sum_histogram(labels)
    for modulus in (15, 17, 31):
        cyclic = pw.cyclic_product({p: Fraction(1) for p in labels},
                                  {p: Fraction(1) for p in labels}, modulus)
        for target in range(15):
            require(cyclic.get(target, 0) == sums.get(target, 0),
                    "safe_fourier_sampling")
    undersampled = pw.cyclic_product({p: Fraction(1) for p in labels},
                                    {p: Fraction(1) for p in labels}, 5)
    require(undersampled[4] == 4 and sums[4] == 1, "finite_phase_alias")
    for real, imag in ((0, 0), (1, 0), (0, 1), (3, -7), (-5, 2)):
        re = Fraction((real + 1)**2 - (real - 1)**2, 4)
        im = Fraction((imag + 1)**2 - (imag - 1)**2, 4)
        require((re, im) == (real, imag), "coherent_reference_recovery")

    root = Path(__file__).resolve().parent
    report = {
        "status": "PASS", "failures": 0, "parent_commit": PARENT_COMMIT,
        "explicit_checks": sum(checks.values()), "checks_by_group": dict(checks),
        "prime_classification_max": bound,
        "pair_targets": {"all_integers_inclusive": [4, 512],
                         "holdouts": [514, 582, 997, 1024, 4096]},
        "local_interference_primes_through": 47,
        "largest_complete_CRT_period": 210,
        "homometric_control": {"A": a, "B": b, "same_full_intensity": True,
                               "target": 8, "pair_counts": [2, 0]},
        "mod30_counterfeit": {"swaps": [[p, 31*p] for p in pw.MOD30_SWAPPED_PRIMES],
                              "histogram_windows": [713, 1024, 2048],
                              "target": 30, "pair_counts": [6, 0],
                              "braid_basis_index": 6, "braid_outputs": [434, 14]},
        "finite_interval_control": {"modulus": 30, "target": 16,
                                    "residues": interval_control["residues"],
                                    "normalized_period_correlation": "45/32",
                                    "bulk_pairs_in_target_interval": 0,
                                    "endpoint_corrected_pairs": 4},
        "finite_sampling_control": {"source": labels, "target": 4,
                                    "clock": 5, "aliased": 4, "actual": 1},
        "limits": ["Finite controls, not a universal prime-pair theorem.",
                   "Cyclotomic symbolic wave checks are in test_prime_waves.py.",
                   "No physical propagation law or speedup is certified."],
        "source_sha256": {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                          for name in ("prime_waves.py", "wave_probe.py",
                                       "prime_observer.py", "cylinder.py")},
    }
    return report


if __name__ == "__main__":
    report = run_probe()
    path = Path(__file__).resolve().parent / "receipts/WAVE_REPORT.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: report[key] for key in
                      ("status", "explicit_checks", "failures", "checks_by_group")},
                     indent=2, sort_keys=True))
