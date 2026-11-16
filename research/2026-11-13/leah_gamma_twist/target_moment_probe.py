"""Preregistered finite observations, with source certificates retained.

Run from the repository root. This reports finite measurements only.
The canonical four-pole source grid is the authority. No digit file or
floating-point pi constant is read. A receipt includes all grid points and
the integer source enclosure in a deterministic gzip JSON certificate.
"""
from __future__ import annotations

from dataclasses import replace
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import gzip
import json
import subprocess
import time

from target_moments import (
    certified_shell, rational_display, signed_moment_coordinates,
    target_interval, verify_packet_source,
)


HERE = Path(__file__).resolve().parent
SHELLS = (17, 65, 129, 32771, 65537, 131101)
TERMS = (1, 2, 4, 6)


def encode(obj):
    if isinstance(obj, Q):
        return [str(obj.numerator), str(obj.denominator)]
    if isinstance(obj, dict):
        return {str(k): encode(v) for k,v in obj.items()}
    if isinstance(obj, (tuple,list)):
        return [encode(v) for v in obj]
    return obj


def main():
    records = []
    for B in SHELLS:
        clock = time.perf_counter()
        cert, packet, _ = certified_shell(B, terms=6, depth=6)
        if not verify_packet_source(cert, packet):
            raise ArithmeticError("canonical source verification failed")
        certificate = {
            "start": cert.start, "count": cert.count, "depth": cert.depth,
            "guard": cert.guard, "horizon": cert.horizon,
            "integer_lower_hex": hex(cert.integer_lower),
            "integer_upper_hex": hex(cert.integer_upper),
            "points": cert.points,
        }
        raw = json.dumps(certificate, sort_keys=True,separators=(",", ":")).encode()
        path = HERE / f"target_grid_{B}.json.gz"
        path.write_bytes(gzip.compress(raw, mtime=0))
        observations = {}
        for q in TERMS:
            truncated = replace(packet,terms=q,
                                moments_by_digit=tuple(row[:q] for row in packet.moments_by_digit))
            interval = target_interval(truncated,phase_error=Q(1,2*cert.denominator))
            observations[str(q)] = {
                "exact": encode(interval),
                "outward_display": {k:rational_display(interval[k],12)
                                    for k in ("real","imag","anti_lock")},
            }
        record = {
            "shell": [B,2*B], "end_exclusive": True,
            "role": "calibration" if B < 1000 else "held_out",
            "frequency":1, "source":"literal four-pole BBP, seed=0",
            "certificate_file":path.name,
            "certificate_sha256":sha256(path.read_bytes()).hexdigest(),
            "decoded_certificate_sha256":sha256(raw).hexdigest(),
            "grid_denominator":cert.denominator, "source_horizon":cert.horizon,
            "source_verified":True,
            "moments_by_digit":encode(packet.moments_by_digit),
            "signed_moment_field_coordinates":encode(signed_moment_coordinates(packet)),
            "observations":observations,
            "runtime_seconds_observed":round(time.perf_counter()-clock,3),
            "asymptotic_authority":False,
        }
        records.append(record)
        receipt = {"protocol_commit":"17e58672bbd3954a8e72ec9de9ca90c1c2b5de0d",
                   "completion":"complete" if len(records)==len(SHELLS) else "partial",
                   "scope":"finite rational certificates, not an all-scale R0 bound",
                   "shells":records}
        (HERE / "target_moment_results.json").write_text(json.dumps(receipt,indent=2)+"\n")
        print(json.dumps({"B":B,"q6":observations['6']['outward_display'],
                          "seconds":record['runtime_seconds_observed']}),flush=True)


if __name__ == "__main__":
    main()
