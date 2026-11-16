"""Reproduce finite controls and verify the saved code-bound receipt.

--write records intended outputs after review; it does not certify a paper
theorem. The full repository run has its own native_validation.json log.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import unittest

import audit_probe
import complex_banks
import integer_information
import phase_aperture


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def canonical(data):
    return json.dumps(data, indent=2, sort_keys=True, allow_nan=False) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.discover(str(HERE), pattern="test_*.py")
    outcome = unittest.TextTestRunner(verbosity=1).run(suite)
    if not outcome.wasSuccessful():
        return 1
    reports = {
        "INTEGER_RESULTS.json": integer_information.report(),
        "COMPLEX_RESULTS.json": complex_banks.control_report(),
        "AUDIT_RESULTS.json": audit_probe.report(),
        "PHASE_APERTURE_RESULTS.json": phase_aperture.report(),
    }
    files = sorted(HERE.glob("*.py")) + [ROOT / "tests/test_adaptive_boundary_resolution.py"]
    receipt = {
        "scope": "Finite exact controls; paper theorems and classical imports are separately audited.",
        "published_parent": "f4151c4ae877ee43c4b7d130174b6bec1dbab9d6",
        "focused_test_count": outcome.testsRun,
        "code_sha256": {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in files},
        "reports_sha256": {name: hashlib.sha256(canonical(data).encode()).hexdigest()
                           for name, data in reports.items()},
        "Goldbach_proved": False,
        "formal_proof_assistant_verification": False,
    }
    reports["VALIDATION_RESULTS.json"] = receipt
    for name, data in reports.items():
        target, rendered = HERE / name, canonical(data)
        if args.write:
            target.write_text(rendered)
        elif not target.exists() or target.read_text() != rendered:
            raise SystemExit("Saved report is missing or stale: " + name)
    arithmetic = reports["AUDIT_RESULTS.json"]["arithmetic_audit"]
    print(canonical({
        "reports": sorted(reports),
        "focused_tests": outcome.testsRun,
        "integer_product_twins": len(reports["INTEGER_RESULTS.json"]["witnesses"]),
        "arithmetic_damped_certificates": len(arithmetic["damped_certificates"]),
        "positive_damped_certificates": sum(row["positive"] for row in arithmetic["damped_certificates"]),
        "packet_exact_counts": sum(row["observed_packet_recovers_count"] for row in arithmetic["damped_certificates"]),
        "uniform_mass_budget_exact_counts": sum(row["sharp_mass_completeness_budget_met"] for row in arithmetic["damped_certificates"]),
        "single_channel_exact_counts": len(arithmetic["single_channel_certificates"]),
        "Goldbach_proved": False,
    }), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
