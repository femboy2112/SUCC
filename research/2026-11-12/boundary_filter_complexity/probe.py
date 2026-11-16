"""Reproduce exact finite BBP Gram receipts; numerical oracle is separate."""
from dataclasses import asdict
from fractions import Fraction
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.boundary_filter_complexity import certify_bbp_boundary_rank


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return value


def main():
    cases = [(start, degree) for start in (17, 37, 73) for degree in range(1, 5)]
    cases.append((109, 4))
    results = []
    for start, degree in cases:
        cert = certify_bbp_boundary_rank(start, start, degree)
        if cert.eigenvalue_lower <= 0:
            raise AssertionError((start, degree, "finite certificate inconclusive"))
        result = encode(asdict(cert))
        result["verdict"] = cert.verdict
        # Rational lower margin rounded DOWN, not a floating proof value.
        result["margin_floor_millionths"] = int(cert.eigenvalue_lower * 10**6)
        results.append(result)
        print(start, degree, result["margin_floor_millionths"], flush=True)
    payload = {
        "scope": "13 finite original-zero BBP windows; no uniform or asymptotic assertion",
        "source": "canonical duck_bbp four-pole source; common terminal horizon",
        "angle_source": "pi_source_genesis Machin/Taylor outward rational enclosures",
        "verifier": "Gershgorin bound using dyadic upper square roots of box modulus bounds",
        "case_selection": "17/37/73 and reserved 109 were fixed before either implementation; same-model provenance",
        "results": results,
    }
    path = Path(__file__).with_name("receipts") / "certified_gram.json"
    path.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
