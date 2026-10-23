#!/usr/bin/env python3
"""Reproducible, non-normality-claim circle/Kummer/π finite certificate.

Usage:
  python scripts/circle_collision_probe.py --output /tmp/circle.json
  python scripts/circle_collision_probe.py --check
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

from observational_succ.circle_collision_rigidity import (
    aligned_phase, carry_product, chord_fourier, covering,
    energy_transport_error, fejer_chord, haar_moment,
    outward_decimal, pi_interval, polygon_moment,
    prime_carries, replica_count, vertex_orbits, certified_energy,
    polygon_ensemble_fourier_square, polygon_ensemble_energy,
    wallis_from_circle_moments,
)

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "research/2026-10-23/CIRCLE_CHORD_EXACT_RECEIPT.json"
SOURCE_FILES = (
    "observational_succ/circle_collision_rigidity.py",
    "tests/test_circle_collision_rigidity.py",
    "scripts/circle_collision_probe.py",
)


def git_blob_id(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def frac(x):
    return f"{x.numerator}/{x.denominator}"


def construct():
    pi5 = certified_energy(16, 5, 2, digits=72, pi_level=22, order=26)
    pi8 = certified_energy(16, 8, 3, digits=78, pi_level=23, order=26)
    geo8 = certified_energy(16, 8, 3, geometric=True, lookahead=6,
                            digits=78, pi_level=23, order=26)
    error = energy_transport_error(3, 8, 6)
    assert max(abs(geo8[0]-pi8[1]), abs(geo8[1]-pi8[0])) < error
    assert Q(1234121, 1000000) < pi8[0] < pi8[1] < Q(1234122, 1000000)
    assert Q(1541868, 1000000) < pi5[0] < pi5[1] < Q(1541869, 1000000)
    pi20 = pi_interval(20, 78)
    return {
        "schema_version": 1,
        "parent": "5e2ba04c8b4ab627b6b0add588609c347346a1a2",
        "status": "EXACT_FINITE_TESTED; PAPER_THEOREMS_SEPARATE; PI_NORMALITY_UNVERIFIED",
        "pi_normality_proved": False,
        "RH_proved": False,
        "physical_measurement_performed": False,
        "chord_covering_coefficients": {str(n): list(covering(n)) for n in range(1, 7)},
        "fejer_chord_coefficients": {
            str(n): [frac(z) for z in fejer_chord(n)] for n in range(1, 5)
        },
        "haar_chord_moments": {
            str(n): str(haar_moment(n)) for n in range(1, 13)
        },
        "kummer_carries": {str(n): {str(p): k for p, k in prime_carries(n).items()}
                            for n in (2, 3, 5, 12)},
        "kummer_reconstruction_100": carry_product(100) == haar_moment(100),
        "polygon_moment_stabilization": {
            str(k): polygon_moment(k, k+1) == haar_moment(k)
            for k in range(1, 20)
        },
        "polygon_vertex_orbits_7_2": [list(c) for c in vertex_orbits(7, 2)],
        "selected_vertex_mean_7_2": "7/3",
        "full_polygon_mean_7_2": str(polygon_moment(1, 7)),
        "replica_count_16_1_100_128": replica_count(16, 1, 100, 128),
        "polygon_ensemble_16_N6_M3_m4pow12": str(
            polygon_ensemble_energy(16, 6, 3, 4**12)),
        "polygon_ensemble_fourier_16_N6_h1_m4pow12": str(
            polygon_ensemble_fourier_square(16, 1, 6, 4**12)),
        "selected_fixed_vertex_energy_M3": "4",
        "wallis_circumference_bracket_k5": [
            frac(u) for u in wallis_from_circle_moments(5)],
        "pi_polygon_interval_20_decimal12": list(outward_decimal(*pi20, 12)),
        "actual_pi_fejer_16_N5_M2_decimal12": list(outward_decimal(*pi5, 12)),
        "actual_pi_fejer_16_N8_M3_decimal12": list(outward_decimal(*pi8, 12)),
        "aligned_radical_fejer_16_N8_M3_K6_decimal12": list(
            outward_decimal(*geo8, 12)
        ),
        "rigorous_aligned_energy_error_N8_M3_K6": frac(error),
        "source_git_blobs": {path: git_blob_id(path) for path in SOURCE_FILES},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--output")
    args = ap.parse_args()
    got = construct()
    if args.output:
        Path(args.output).write_text(json.dumps(got, indent=2, sort_keys=True) + "\n")
    if args.check:
        expected = json.loads(RECEIPT.read_text())
        if got != expected:
            raise SystemExit("FAIL: frozen exact receipt/source-blob mismatch")
    print(json.dumps({
        "verified": (args.check or not args.output),
        "actual_pi_energy": got["actual_pi_fejer_16_N8_M3_decimal12"],
        "normality_proved": False,
        "source_blobs": got["source_git_blobs"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
