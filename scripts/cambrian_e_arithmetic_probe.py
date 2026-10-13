#!/usr/bin/env python3
"""Replay exact E25--E30 arithmetic controls and freeze a small receipt.

Numbers printed as fractions are exact. This does not assert source
attestation, universal Weil positivity, or an independent Gaussian moat proof.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.cambrian_e_arithmetic_transport import (
    bounded_denominator_unique, clock_distribution_countermodel,
    connected_from_four_queries, dirichlet_exp_prefix, selfdual_offline_family,
)
from observational_succ.adelic_theta_completion import (
    normalized_self_dual_gaussian_pair, offcritical_self_dual_zero_witness,
    deleted_euler_factor_asymmetry, completed_s2_interval,
)
from observational_succ.diagonal_adele_zeta import (
    DiagonalCarrier, additive_reciprocity, multiplicative_reciprocity,
)
from observational_succ.gamma_interferometer import GammaInterferometer
from observational_succ.source_prime_certificates import CertifiedPrimeSource
from observational_succ.observer_reflection import RationalInterval
from observational_succ.periodic_path_certificates import (
    gaussian_sieve, analyze_periodic, gaussian_bound, verify_translation,
    is_gaussian_prime, ConfinementCertificate,
)


def encode(obj):
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, RationalInterval):
        return {"lower": str(obj.lower), "upper": str(obj.upper)}
    if isinstance(obj, dict):
        return {str(k): encode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [encode(v) for v in obj]
    return obj


def report():
    sources = {}
    genuine = CertifiedPrimeSource.genuine(81)
    fake = {n: F(1) for n in range(1, 82)}
    fake[6] = F(2)
    for name, source in (("genuine", genuine),
                         ("fake_six", CertifiedPrimeSource(GammaInterferometer.from_prefix(fake, 81)))):
        sources[name] = {"diagnostic": source.snapshot.diagnostic(), "tomography": []}
        recovered = dirichlet_exp_prefix(dict(enumerate(source.snapshot.connected)), 81)
        assert recovered == source.snapshot.coefficients
        for n in (2, 4, 6, 8, 12, 20):
            r = connected_from_four_queries(n, source.prime_psi)
            interval = r["coefficient_interval"]
            expected = source.snapshot.connected[n]
            assert interval.lower <= expected <= interval.upper
            sources[name]["tomography"].append({
                "event": n, "times": r["times"], "coefficient": expected,
                "enclosure": interval,
                "at_most_one_rational_denominator_le_100": bounded_denominator_unique(interval, 100),
            })
    residue_fibers = {r: tuple(n for n in range(27) if 3 * n % 27 == r) for r in range(27)}
    active_fibers = {r: ns for r, ns in residue_fibers.items() if ns}
    assert len(active_fibers) == 9 and all(len(ns) == 3 for ns in active_fibers.values())
    sieve = gaussian_sieve((2, 5, 13), 2)
    certificate = analyze_periodic(sieve)
    assert isinstance(certificate, ConfinementCertificate)
    gaussian_positive = gaussian_bound((2, 5, 13), 2, certificate)
    leaking = gaussian_sieve((2, 5, 13), 4)
    escape = analyze_periodic(leaking)
    leak_receipt = verify_translation(leaking, escape)
    composite = (1, 30)
    assert leaking.contains(composite) and not is_gaussian_prime(composite)
    fresh = selfdual_offline_family(3, F(4, 5))
    assert fresh["discriminant"] == F(44, 25)
    q = F(7, 30)
    out = {
        "schema": "succ-cambrian-e-arithmetic-v1",
        "base_sha": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "execution_head_sha": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "python": platform.python_version(),
        "code_sha256": {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                        for p in (ROOT / "observational_succ/cambrian_e_arithmetic_transport.py",
                                  Path(__file__).resolve(), ROOT / "tests/test_cambrian_e_arithmetic_transport.py")},
        "E25_affine_covariance": DiagonalCarrier(q).commuting_square(F(2, 7), F(3), {11: 2, 13: 2}),
        "E25_nonunit_prime_FUCC_clock": {"prime": 3, "modulus": 27,
                                         "image_size": len(active_fibers), "fibers": active_fibers,
                                         "invertible_on_this_clock": False},
        "E26_coherent_unbounded_clock_distribution": [clock_distribution_countermodel(3, r) for r in (1, 2, 4, 8)],
        "E27_diagonal_additive_source": additive_reciprocity(q),
        "E27_diagonal_product_source": multiplicative_reciprocity(q),
        "E28_positive_prime_containment": gaussian_positive,
        "E28_sieve_escape_only": leak_receipt,
        "E28_actual_source_falsifier": {"allowed_sieve_point": composite,
                                        "norm": 901, "norm_factorization": [17, 53],
                                        "gaussian_prime": False},
        "E29_DZ8_replayed": normalized_self_dual_gaussian_pair(F(2), 2),
        "E29_DZ9_replayed": offcritical_self_dual_zero_witness(),
        "E29_fresh_arch_source_mutation": fresh,
        "E29_missing_Euler_factor": deleted_euler_factor_asymmetry(3, 2),
        "E29_standard_s2_completion": completed_s2_interval(29, 8),
        "E30_bounded_source_tomography": sources,
        "unknown_nontrivial_zeta_zeros_used_as_input": False,
        "RH_proved": False,
        "full_Weil_positive_form_proved": False,
        "all_step_Gaussian_theorem_independently_proved": False,
        "mathematical_scope": "finite prime-source tomography; exact local obstructions; paper proofs in dossier",
    }
    return encode(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(report(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
