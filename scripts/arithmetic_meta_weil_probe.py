"""Deterministic, executable source-first Meta-SUCC / Weil research receipt.

This is a proof-checking smoke test for stated exact FINITE inequalities, not a
standalone formal proof of analytic lemmas or any nontrivial zeta-zero claim.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from observational_succ.arithmetic_meta_weil import (
    authentic_prime_tape, first_prime_moment_100_certificate,
    first_prime_boundary_commutator_certificate, dyadic_window_commutator,
    gamma_rungs_multiplier_lower, moment_fourier_leak_upper,
    independent_tent_weil_oracle, valuation_holonomy,
    improved_first_prime_moment_29_certificate,
)
from fractions import Fraction as F


def report():
    K,S,comm=dyadic_window_commutator(3)
    # The high precision readings are numerical controls ONLY. For repeatable
    # receipts mpmath's dps, branch cuts, and test functions are fixed.
    checks={}
    for a in ("0.25","0.5","0.75"):
        raw=independent_tent_weil_oracle(a,40)
        if float(raw["difference"]) >= 1e-25:
            raise ValueError("independent original Weil / Carleman diagnostic disagree")
        # Freeze stable 18-significant-digit readings only.  The retained
        # high-precision 40-dps validation runs separately in unit tests;
        # sub-1e-25 quadrature residue is NOT an exact certificate.
        import mpmath as mp
        checks[a]={
            "source_prime_powers":raw["source_prime_powers"],
            "original_W_18_digits":mp.nstr(mp.mpf(raw["original_W"]),18),
            "carleman_W_18_digits":mp.nstr(mp.mpf(raw["source_carlemann"]),18),
            "observed_abs_difference_below_1e-25": True,
            "rigorous_interval_certificate":False,
        }
    return {
        "schema": "succ-arithmetic-meta-weil-1",
        "parent": "SUCC PR80@cc0d50bb2585db254cf865c66522b9a356eb9d4d",
        "date": "2026-10-14",
        "status": "SOURCE-CONDITIONAL-PROVED-LOCAL",
        "RH_proved":False,
        "independent_academic_priority_verified": False,
        "physical_source_authenticated":False,
        "main_modified":False,
        "genuine_prime_tape_leq_9":list(map(list,authentic_prime_tape(9))),
        "false_composite_6_is_primitive":False,
        "global_prime_gamma_holonomy": "FLAT: exact commuting translations",
        "finite_window_2log2_discrete_control": {
            "gamma_carlemann_kernel": [[str(x) for x in row] for row in K],
            "commutator": [[str(x) for x in row] for row in comm],
            "continuum_Galerkin_claimed":False,
        },
        "true_prime2_continuum_window_commutator":first_prime_boundary_commutator_certificate(),
        "first_prime_101_moment_infinite_dimensional_weil":first_prime_moment_100_certificate(),
        "improved_30_moment_infinite_dimensional_weil":improved_first_prime_moment_29_certificate(),
        "independent_original_weil_crosscheck":checks,
        "signed_complete_weil_identification_is_classical_import":True,
        "full_Weil_sign_proved":False,
        "theorem_verification_scope": "Fraction inequalities + paper derivations + diagnostic mpmath, no Lean proof",
        "next_gate": "source-compatible rigorous Schur complement with finite low-mode block and certified tail; no extra positive holonomy",
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',type=Path)
    p.add_argument('--write',type=Path)
    args=p.parse_args()
    r=report()
    encoded=json.dumps(r,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    if args.verify:
        if args.verify.read_text(encoding='utf-8')!=encoded:
            raise SystemExit('ARITHMETIC_META_WEIL_RECEIPT_DRIFT')
        print('ARITHMETIC_META_WEIL_RECEIPT_VERIFIED')
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True)
        args.write.write_text(encoded,encoding='utf-8')
    if not args.verify and not args.write:
        print(encoded)


if __name__=='__main__':
    main()
