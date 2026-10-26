"""Replay exact spectral-purity instruments; no asymptotic claim from samples."""
from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.spectral_purity_arithmetic import (
    conductor_birth_innovation_budget, conductor_growth_certificate,
    conductor_growth_count_upper, conductor_locked_countermodel,
    prescribed_width, source_trace_certificate,
)
from observational_succ.spectral_purity_certificates import (
    authentic_innovation_interval, selected_trace_counterexample,
)
from observational_succ.spectral_purity_innovation import (
    authentic_sequential_certificate, spectral_green_budget,
)
from observational_succ.spectral_purity_multiscale import prefix_jet_counterfeit
from observational_succ.succ_internal_matrix_walk import walsh_digit_energy


SOURCES = (
    "observational_succ/succ_internal_matrix_walk.py",
    "observational_succ/gamma_bbp_signed_coherence.py",
    "observational_succ/pi_source_genesis.py",
    "observational_succ/pi_joint_prime_carrier.py",
    "observational_succ/finite_fourier_carrier.py",
    "observational_succ/spectral_purity_arithmetic.py",
    "observational_succ/spectral_purity_certificates.py",
    "observational_succ/spectral_purity_innovation.py",
    "observational_succ/spectral_purity_multiscale.py",
    "formal/SpectralPurity.lean",
    "scripts/check_spectral_purity_lean.py",
    "scripts/spectral_purity_probe.py",
)


def serial(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(item) for item in value]
    return value


def digest(data):
    return hashlib.sha256(data).hexdigest()


def report():
    sequential = authentic_sequential_certificate(4, 3)
    traces = []
    for n, width, p in ((2, 3, 3), (14, 4, 109)):
        cert = source_trace_certificate(n, width, p)
        traces.append({
            "arrival": n, "width": width, "prime": p,
            "old_depth": cert.old_depth, "new_depth": cert.new_depth,
            "old_conductor": str(cert.old_conductor),
            "new_conductor": str(cert.new_conductor),
            "trace_identity_checked": cert.traced_innovation == cert.predicted_trace,
            "relative_trace_upper": cert.evaluated_trace_upper,
            "selected_innovation_interval": authentic_innovation_interval(n, width),
            "selected_bound_proved": cert.selected_bound_proved,
        })
    mutants = []
    for prefix, order in ((2, 2), (6, 6)):
        c = prefix_jet_counterfeit(prefix, order)
        density = json.dumps(serial(c.density), separators=(",", ":")).encode()
        mutants.append({
            "prefix": prefix, "jet_order": order, "level": c.approximation_level,
            "seed": c.seed, "even_polynomial_degree": len(c.density)-1,
            "density_sha256": digest(density), "positivity_margin": c.positivity_margin,
            "correction_norm": c.correction_norm,
            "first_changed_forcing": c.forcing(prefix+1),
            "difference_bounds": [c.forcing_difference_bound(n, b)
                                  for n, b in ((31, 0), (257, 1), (65537, 3))],
            "all_time_odd_denominators_authority": "PAPER-PROVED",
            "authentic_global_four_pole_source": False,
        })
    locked = conductor_locked_countermodel(32)
    even = tuple(d for d in range(16) if d.bit_count() % 2 == 0)
    return serial({
        "schema": 1, "parent_commit": "461942c0bf616518e668d236d1c6b1596665a7dd",
        "source_id": "Q:Coherent-Main-X-four-pole-BBP",
        "source_sha256": {name: digest((ROOT/name).read_bytes()) for name in SOURCES},
        "sequential": {"N": 4, "H": 3, "identity_checked": True,
                       "formal_energy_terms": len(sequential.normalized_spectral_excess.terms)},
        "selected_trace_counterexample": selected_trace_counterexample(),
        "relative_trace_rows": traces,
        "conductor_rows": [asdict(conductor_growth_certificate(n)) for n in (8, 32, 128)],
        "universal_budget_rows": [
            {"N_power_of_two": exponent, "width": prescribed_width(2**exponent),
             "growth_count_upper": conductor_growth_count_upper(2**exponent),
             "birth_innovation_upper": conductor_birth_innovation_budget(2**exponent)}
            for exponent in (16, 64, 256, 1024)],
        "spectral_green": [asdict(spectral_green_budget(n, h))
                           for n, h in ((64, 4), (1000, 100), (1000000, 10000))],
        "matched_countermodels": mutants,
        "exact_conductor_countermodel": {
            "horizon": 32, "source_id": locked["source_id"],
            "exact_state_denominators": all(u.denominator == q for u, q in
                                            zip(locked["states"], locked["conductors"])),
            "positive_forcing": all(r > 0 for r in locked["forcing"]),
            "authentic_four_pole_source": False,
        },
        "even_parity_walsh": walsh_digit_energy(even),
        "pi_normality_proved": False,
        "remaining_flat_step_estimate": "OPEN",
        "authority": "EXACT FINITE replay; universal statements require the paper proofs",
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    actual = report()
    if args.verify:
        expected = json.loads(args.verify.read_text())
        if actual != expected:
            raise SystemExit("FAIL: source hash or exact research receipt differs")
        print("PASS: exact spectral-purity receipt and source hashes match")
    else:
        data = json.dumps(actual, indent=2, sort_keys=True)+"\n"
        if args.write:
            args.write.write_text(data)
            print(f"Wrote exact finite receipt: {args.write}")
        else:
            print(data, end="")


if __name__ == "__main__":
    main()
