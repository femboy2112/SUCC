#!/usr/bin/env python3
"""Bounded exact witnesses for E34; no analytic zero or floating inputs.

Finite checks are regressions for the dossier's written proofs, not their
universal certificate. Formal character exponents encode fifth/third roots
of unity exactly; the window packet below is bookkeeping for an unchanged
phase and half-density, not an approximate functional equation for mutants.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from observational_succ.arithmetic import factorization
from observational_succ.core import DomainError
from observational_succ.diagonal_adele_zeta import (
    DiagonalSourceError, valuation, valuations,
)
from observational_succ.hasse_theta_seam import (
    SUCCDifferenceSource, _source_prime_power,
)
from observational_succ.prime_clock_yoneda import (
    ArithmeticFunctorError, PrimeClockSource,
)
from observational_succ.resource_probe import ValuationWord

SOURCE_PARENT = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
ORIGIN_COMMIT = "ba075348b7bcc66d938b3e0ca96c26e95bba340a"
SOURCES = (
    "provenance/IMPORT_MANIFEST.json",
    "observational_succ/arithmetic.py",
    "observational_succ/resource_probe.py",
    "observational_succ/yoneda.py",
    "observational_succ/hasse_theta_seam.py",
    "observational_succ/ordinal_succ_report.py",
    "observational_succ/diagonal_adele_zeta.py",
    "observational_succ/prime_clock_yoneda.py",
    "observational_succ/clock_mahler_interpolation.py",
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def must_reject(thunk, error):
    try:
        thunk()
    except error:
        return True
    raise AssertionError("Native source gate admitted the negative control")


def cov(weights):
    """Independent exact covariance of actual integer valuation features."""
    labels = range(1, len(weights) + 1)
    features = [(Q(valuation(n, 2)), Q(valuation(n, 3))) for n in labels]
    total = sum(weights, Q())
    means = [sum((w*f[j] for w, f in zip(weights, features)), Q())/total
             for j in range(2)]
    mat = [[sum((w*(f[i]-means[i])*(f[j]-means[j])
                 for w, f in zip(weights, features)), Q())/total
            for j in range(2)] for i in range(2)]
    det = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    require(mat[0][0] >= 0 and mat[1][1] >= 0 and det >= 0,
            "Positive finite source lost covariance PSD")
    return {"matrix": [[str(x) for x in row] for row in mat],
            "determinant": str(det), "PSD": True}


def packet(source, normalized_t):
    """Formal phase-matched window; x=t/(2*pi) is supplied exactly.

    Coefficients are rational multipliers of 1/sqrt(n). The unchanged
    formal character is z*prod_p X_p**v_p(n) and its inverse, where X_p
    specializes to exp(-i*t*log(p)). Thus X_6=X_2*X_3 is preserved.
    No character value or square root is approximated.
    """
    x = Q(normalized_t)
    require(x >= 1, "Positive normalized factor-square window required")
    window = isqrt(x.numerator//x.denominator)
    require(window <= source.horizon, "Missing integrated coefficient")
    return {n: (source.coefficients[n], "1/sqrt(%d)" % n,
                (1, factorization(n)),
                (-1, tuple((p, -k) for p, k in factorization(n))))
            for n in range(1, window+1)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    rows = []
    require(all(pow(u, 2, 8) == 1 for u in (1, 3, 5, 7))
            and pow(3, 1, 8) != 1, "p=2 least unit exponent control failed")
    for p in (2, 3, 5, 7):
        for k in range(5):
            n = p**k
            gap = p*n-n
            require(gap == (p-1)*n and valuation(gap, p) == k,
                    "Prime-jet invariant failed")
            require(valuation(p*n, p) == valuation(n, p)+1,
                    "FUCC did not shift valuation")
            rows.append({"p": p, "k": k, "integer": n,
                         "gap": gap, "gap_valuation": k})

    no_go = []
    for p in (2, 3, 5, 7):
        a, b = p-1, p*p-1
        before = [valuation(a, p), valuation(b, p)]
        after = [valuation(a+1, p), valuation(b+1, p)]
        require(before == [0, 0] and after == [1, 2],
                "Successor no-go witness failed")
        no_go.append({"p": p, "integers": [a, b],
                      "before": before, "after_successor": after})

    finite_depth_no_go = []
    for p in (2, 3, 5):
        for r in range(1, 4):
            a, b, modulus = p**r-1, p**(r+1)-1, p**r
            require(a % modulus == b % modulus,
                    "Cancellation witness did not match finite residue jet")
            require(valuation(a, p) == valuation(b, p) == 0,
                    "Cancellation witness did not match input valuations")
            require([valuation(a+1, p), valuation(b+1, p)] == [r, r+1],
                    "Finite-depth successor no-go failed")
            finite_depth_no_go.append({"p": p, "r": r,
                "source_integers": [a, b], "common_residue": a % modulus,
                "successor_valuations": [r, r+1]})

    # Full prime-word encoding retains the positive integer; one-coordinate
    # projection above does not. No hidden bounded-window closure is assumed.
    for n in range(1, 65):
        word = ValuationWord.from_integer(n)
        reconstructed = 1
        for p, k in word.factors:
            reconstructed *= p**k
        require(reconstructed == n, "Full valuation word lost its source")
        for p in (2, 3, 5):
            require(word.multiply_prime(p) == ValuationWord.from_integer(p*n),
                    "Native multiplication square failed")

    square_checks = 0
    for n in range(1, 65):
        for d in range(4):
            require((n+d)**2 == n*n+2*d*n+d*d,
                    "Square-successor transport failed")
            for m in (2, 3, 6):
                require((m*n)**2 == m*m*n*n,
                        "Square-dilation transport failed")
                require((m*n+d)-m*(n+d) == d*(1-m),
                        "Affine address defect failed")
                square_checks += 1
    require(2**2-1**2 != 3**2-2**2,
            "A fixed square increment unexpectedly existed")
    require(4 % 2 == 0 and 5 % 3 != 0,
            "Successor unexpectedly preserved divisibility")
    factor_rows = []
    for N in range(1, 101):
        pairs = [(a, N//a) for a in range(1, N+1) if N % a == 0]
        lower = [(a, b) for a, b in pairs if a <= b]
        require(lower == [(a, N//a) for a in range(1, isqrt(N)+1)
                          if N % a == 0], "Square-root cone failed")
        diagonal = int(isqrt(N)**2 == N)
        require(len(pairs) == 2*len(lower)-diagonal,
                "Diagonal counted twice or omitted")
        if N in (1, 6, 25, 36):
            factor_rows.append({"N": N, "lower_pairs": lower,
                               "diagonal_count": diagonal})

    phase_controls = []
    for p, real_prime, composite in ((5, 11, 6), (3, 7, 4)):
        fine = p*p
        coarse_real = [(real_prime*x) % p for x in range(p)]
        coarse_fake = [(composite*x) % p for x in range(p)]
        require(coarse_real == coarse_fake, "Phase matching failed")
        # Character chi_j has exact exponent j*reported_address mod p.
        phases = [[(j*x) % p for x in coarse_real] for j in range(p)]
        fake_phases = [[(j*x) % p for x in coarse_fake] for j in range(p)]
        require(phases == fake_phases, "A character detected equal residues")
        require(real_prime % fine != composite % fine,
                "Fine precision did not split the calibrated alias")
        prime_source = PrimeClockSource(p, 1, 1, 1, real_prime)
        require(prime_source.coordinate_defect() == 0,
                "Coarse affine defect should vanish")
        rejected = must_reject(
            lambda: PrimeClockSource(p, 1, 1, 1, composite),
            ArithmeticFunctorError)
        phase_controls.append({"place": p, "prime": real_prime,
            "fake_composite": composite, "coarse_dilation": coarse_real,
            "coarse_character_exponents": phases,
            "fine_x_one_outputs": [real_prime % fine, composite % fine],
            "native_composite_source_rejected": rejected})

    genuine = SUCCDifferenceSource.zeta(8)
    fake = SUCCDifferenceSource.from_prefix(
        {n: 2 if n == 6 else 1 for n in range(1, 9)}, 8)
    require(_source_prime_power(6) is None,
            "Composite impulse became a prime-power event")
    require(fake.coefficients[6]-fake.coefficients[2]*fake.coefficients[3] == 1,
            "Non-Euler source multiplicativity control failed")
    before, at = Q(143, 4), Q(36)
    require(packet(genuine, before) == packet(fake, before),
            "A future coefficient leaked below its square horizon")
    delta = [n for n in packet(genuine, at)
             if packet(genuine, at)[n] != packet(fake, at)[n]]
    require(delta == [6], "Phase-matched window did not isolate n=6")
    cov_real, cov_fake = cov([Q(1)]*6), cov([Q(1)]*5+[Q(2)])

    refused = {
        "zero_valuation": must_reject(lambda: valuation(0, 2), DiagonalSourceError),
        "zero_full_word": must_reject(lambda: ValuationWord.from_integer(0), DomainError),
        "zero_product_formula": must_reject(lambda: valuations(0), DiagonalSourceError),
        "composite_word": must_reject(lambda: ValuationWord(((6, 1),)), DomainError),
    }
    provenance = {}
    for path in SOURCES:
        data = (ROOT/path).read_bytes()
        frozen = subprocess.run(["git", "show", SOURCE_PARENT+":"+path],
                                cwd=ROOT, check=True, capture_output=True).stdout
        require(data == frozen, "Source differs from immutable parent: "+path)
        provenance[path] = hashlib.sha256(data).hexdigest()
    out = {
        "schema": "E34-exact-1", "source_parent": SOURCE_PARENT,
        "founding_origin_commit": ORIGIN_COMMIT,
        "native_module_origins": {
            "prime_clock_yoneda.py": "f060d465a808877210a02bae4c37b73268513a5d",
            "diagonal_adele_zeta.py": "1efd485031cdaab40bb8598242a5e5f2617330fb",
            "clock_mahler_interpolation.py": "1d5b354fecc19eeb50d5e2e9a23dfaf4b44979b6"},
        "origin_object_inspection": {
            "initial_command": "git cat-file -t "+ORIGIN_COMMIT,
            "initial_cwd": "/home/leah/succ_lab/swm-e34",
            "initial_exit": 128,
            "initial_result": "Origin commit is not an object in the target repository",
            "resolved_cwd": "/home/leah/FuckingRH",
            "resolved_exit": 0,
            "resolved_commands": [
                "git cat-file -t "+ORIGIN_COMMIT,
                "git ls-tree "+ORIGIN_COMMIT+" actualization/hasse_theta_seam.py actualization/resource_probe.py actualization/yoneda.py actualization/ordinal_succ_report.py actualization/arithmetic.py",
                "git show "+ORIGIN_COMMIT+":actualization/hasse_theta_seam.py | sed -n '515,555p'",
                "git show "+ORIGIN_COMMIT+":actualization/resource_probe.py | sed -n '20,78p'",
                "git show "+ORIGIN_COMMIT+":actualization/yoneda.py | sed -n '129,145p'"]},
        "session_separate_provenance_validation": {
            "command": "PYTHONDONTWRITEBYTECODE=1 python scripts/verify_provenance.py",
            "observed_exit": 0, "items": 72,
            "archives_byte_identical": 17, "namespace_migrations": 55,
            "mathematical_truth_established": False},
        "command": "python research/2026-10-13/SWARM_ATLAS/E34_probe.py --receipt research/2026-10-13/SWARM_ATLAS/E34_receipt.json",
        "status": "BOUNDED_EXACT_PROBE_PASSED", "expected_exit": 0,
        "proof_status": "PROVED LOCAL written algebra; TESTED MODEL finite native controls; no kernel certificate",
        "prime_jet_rows": rows, "successor_no_go": no_go,
        "two_adic_unit_countercontrol": {"modulus": 8,
            "unit_group_cardinality": 4, "least_common_unit_exponent": 2},
        "finite_depth_successor_no_go": finite_depth_no_go,
        "full_word_integer_checks": 64, "square_affine_checks": square_checks,
        "factor_cone_products_checked": 100, "factor_cone_examples": factor_rows,
        "phase_matched_composite_controls": phase_controls,
        "phase_matched_nonEuler_control": {
            "source": "a(n)=1+[n=6] for all n; tested prefix 1..8",
            "coprime_multiplicativity_defect_at_2_3": "1",
            "normalized_window_before": str(before),
            "normalized_window_at": str(at), "first_changed_packet": delta,
            "unchanged_phase_and_half_density": True,
            "prime_phase_basis": "X_n=prod_p X_p^v_p(n), X_p=exp(-i*t*log(p)); z=exp(i*theta(t))",
            "formal_delta": "(z*X_6+z^-1*X_6^-1)/sqrt(6)",
            "numerical_nonzero_at_each_t_claimed": False,
            "mutant_approximate_functional_equation_claimed": False},
        "valuation_covariance_genuine": cov_real,
        "valuation_covariance_nonEuler": cov_fake,
        "native_domain_refusals": refused,
        "source_sha256": provenance,
        "own_artifacts_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (Path(__file__), Path(__file__).with_name("E34.md"))},
        "nontrivial_zero_inputs": False, "RH_progress_claimed": False,
        "analytic_remainder_certificate": False,
        "academic_novelty_claimed": False,
    }
    encoded = json.dumps(out, indent=2, sort_keys=True)+"\n"
    if args.receipt:
        args.receipt.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
