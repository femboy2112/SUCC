#!/usr/bin/env python3
"""Generate/verify exact periodic certificates, with explicit arithmetic scope."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.periodic_path_certificates import (
    ConfinementCertificate, analyze_periodic, certificate_from_dict,
    gaussian_sieve, gaussian_bound, verify_translation, search_split_prime_prefix,
)


def case(primes, step_squared):
    graph = gaussian_sieve(primes, step_squared)
    proof = analyze_periodic(graph)
    if isinstance(proof, ConfinementCertificate):
        result = gaussian_bound(primes, step_squared, proof)
    else:
        result = {"rational_primes": list(primes), "period": graph.period,
                  "step_squared": step_squared, "vertices": len(graph.residues),
                  **verify_translation(graph, proof)}
    return result, proof


def run():
    inputs = (((2,), 1), ((5,), 1), ((5, 13), 1), ((5, 13), 2),
              ((2, 5, 13), 2), ((2, 3, 5, 13), 2), ((2, 5, 13), 4))
    results = [case(ps, r)[0] for ps, r in inputs]
    assert results[2]["prime_component_upper_bound"] == 580
    assert results[4]["prime_component_upper_bound"] == 580
    assert results[5]["prime_component_upper_bound"] == 104
    assert results[6]["gaussian_prime_walk_certified"] is False
    found = search_split_prime_prefix(1, prime_limit=13)
    bounded = search_split_prime_prefix(2, prime_limit=13)
    capped = search_split_prime_prefix(2, prime_limit=17, max_cells=5000)
    assert found["status"] == "CERTIFICATE_FOUND"
    assert bounded["status"] == "UNRESOLVED_PRIME_LIMIT"
    assert capped["status"] == "UNRESOLVED_RESOURCE_LIMIT"
    return {"status": "EXACT_GAUSSIAN_MOAT_CERTIFICATE_CONTROLS", "cases": results,
            "search_statuses": [found["status"], bounded["status"], capped["status"]],
            "all_step_existence_independently_proved": False,
            "finite_certificates_depend_on_external_existence": False,
            "new_optimal_gaussian_bounds_claimed": False,
            "scope": "exact bounded inputs plus the proved periodic-lift theorem"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--certificate-output", type=Path,
                        help="Write the complete P={2,5,13}, D^2=2 potential certificate")
    parser.add_argument("--verify", type=Path, help="Rebuild source and verify a saved certificate")
    args = parser.parse_args()
    if args.verify:
        envelope = json.loads(args.verify.read_text())
        if set(envelope) != {"schema", "source", "certificate"} or envelope["schema"] != "gaussian-moat-v1":
            raise ValueError("Unknown certificate envelope")
        source = envelope["source"]
        if set(source) != {"rational_primes", "step_squared"}:
            raise ValueError("Unknown arithmetic source fields")
        primes, step_squared = tuple(source["rational_primes"]), source["step_squared"]
        proof = certificate_from_dict(envelope["certificate"])
        graph = gaussian_sieve(primes, step_squared)
        result = (gaussian_bound(primes, step_squared, proof)
                  if isinstance(proof, ConfinementCertificate) else verify_translation(graph, proof))
    else:
        result = run()
    if args.certificate_output:
        _, certificate = case((2, 5, 13), 2)
        envelope = {"schema": "gaussian-moat-v1",
                    "source": {"rational_primes": [2, 5, 13], "step_squared": 2},
                    "certificate": certificate.to_dict()}
        args.certificate_output.parent.mkdir(parents=True, exist_ok=True)
        args.certificate_output.write_text(json.dumps(envelope, separators=(",", ":")) + "\n")
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
