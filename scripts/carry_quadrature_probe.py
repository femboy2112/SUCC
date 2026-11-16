#!/usr/bin/env python3
"""Reproducible, finite, original-source carry probe; no normality verdict."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.bbp_spatial_haar_lift import complete_source_states
from observational_succ.carry_quadrature import (
    certified_carry_observations, dyadic_residue, nearest_winding,
    selected_event, shell_statistics, source_pulse,
)


def run(horizon: int, output: Path) -> dict:
    prefix, observations = certified_carry_observations(horizon)
    output.mkdir(parents=True, exist_ok=True)
    residues = "".join(str(o.carry_mod4) for o in observations)
    (output / "carry_residues_mod4.txt").write_text(residues+"\n", encoding="ascii")
    (output / "bbp_prefix_hex.txt").write_text(prefix+"\n", encoding="ascii")

    # Separate finite algorithms: outward integer BBP completion plus a tail
    # certificate above; exact unwrapped rational recurrence here.
    direct_horizon = min(512, horizon)
    states = complete_source_states(direct_horizon+12)
    direct_checks = 0
    winding_counts = [[0]*2 for _ in range(4)]
    winding_events = packet_checks = 0
    for n in range(1, direct_horizon+1):
        u = states[n]
        observation = observations[n-1]
        assert observation.carry_mod4 == u.__floor__() % 4
        assert observation.cofactor_mod4 == dyadic_residue(u % 1, 2)
        assert dyadic_residue(u, 2) == n % 4
        direct_checks += 3
        k, before, epsilon = nearest_winding(states[n-1], u)
        negative = int(epsilon < 0)
        winding_counts[k % 4][negative] += 1
        predicted = (k % 4 == 2 or (k % 4 == 1 and not negative)
                     or (k % 4 == 3 and negative))
        assert predicted == selected_event(u.__floor__())
        direct_checks += 1
        if n >= 2 and k:
            winding_events += 1
            assert 16*(before*before+epsilon*epsilon) > F(9, 257)
            packet_checks += 1

    pulse_samples = []
    for n in sorted({4, 5, 15, 16, 17, 63, 64, 65, 255, 256, 257,
                     1024, 4096, 65536, 4**10-1, 4**10, 4**10+1}):
        pulse = source_pulse(n)
        assert F(1, 128) < pulse.response < F(1, 4)
        if n+pulse.delay < len(states):
            assert pulse.response == states[n+pulse.delay]-pulse.harmonic*states[n]
        record = asdict(pulse)
        record["response"] = str(pulse.response)
        record["response_approx"] = float(pulse.response)
        pulse_samples.append(record)

    shells = []
    b = 16
    while 2*b-1 <= horizon:
        shells.append(shell_statistics(observations, b, b))
        b *= 2
    report = {
        "status": "FINITE_SOURCE_CERTIFICATES_ONLY",
        "source": "original four signed BBP poles; U_0=0",
        "endpoint": "alpha=pi/16 by the classical BBP identity",
        "normality_proved": False,
        "R0_proved": False,
        "carry_positive_lower_density_proved": False,
        "horizon": horizon,
        "prefix_hex_length": len(prefix),
        "prefix_sha256": hashlib.sha256(prefix.encode("ascii")).hexdigest(),
        "residues_sha256": hashlib.sha256(residues.encode("ascii")).hexdigest(),
        "borrow_indices": [o.n for o in observations if o.borrow],
        "certificate_counts": dict(Counter(o.certificate for o in observations)),
        "width_counts": dict(Counter(o.phase_width for o in observations)),
        "direct_recurrence_horizon": direct_horizon,
        "exact_cross_checks": direct_checks,
        "implementation_provenance": (
            "Integer-prefix/tail certification and direct rational recurrence are "
            "different algorithms sharing duck_bbp.forcing; cross-checks also "
            "include clock/cofactor and winding/sign identities, not independence."
        ),
        "winding_residue_by_negative_sign_counts": winding_counts,
        "winding_events_tested": winding_events,
        "rational_packet_inequalities": packet_checks,
        "pulse_samples": pulse_samples,
        "shells": shells,
    }
    (output / "finite_probe.json").write_text(json.dumps(report, indent=2)+"\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--horizon", type=int, default=32768)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "research/2026-11-15/carry_quadrature_assault/receipts")
    args = parser.parse_args()
    report = run(args.horizon, args.output)
    print(json.dumps({k: report[k] for k in
                     ("status", "horizon", "borrow_indices", "certificate_counts",
                      "exact_cross_checks", "rational_packet_inequalities",
                      "shells")}, indent=2))


if __name__ == "__main__":
    main()
