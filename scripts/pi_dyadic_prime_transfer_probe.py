#!/usr/bin/env python3
"""Independent Machin pi cylinder checks + exact BBP 16-branch tomography.

Deterministic finite receipt: not a normality certificate, not a fitted
asymptotic. Machin intervals and the BBP recurrence use separate formulas.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_dyadic_prime_transfer import (
    cross_radix_bad_cylinders, decode_target_prefix,
    dyadic_carry_branch_certificate,
)


def _atan_bounds(q: int, terms: int) -> tuple[Q, Q]:
    a = sum((Q((-1) ** k, (2*k+1)*q**(2*k+1))
             for k in range(terms)), Q())
    b = a + Q((-1) ** terms, (2*terms+1)*q**(2*terms+1))
    return min(a,b), max(a,b)


def _pi_machin_bounds(terms: int = 90) -> tuple[Q, Q]:
    a5, b5 = _atan_bounds(5, terms)
    a239, b239 = _atan_bounds(239, terms)
    return 16*a5 - 4*b239, 16*b5 - 4*a239


def _selected_pi_digit_probe() -> dict:
    low, high = _pi_machin_bounds()
    assert 3 < low < high < 4 and (high-low) < Q(1, 2**300)
    rows = []
    for base in (2,3,5,7,11,13,16):
        for n in (1,2,4,8):
            q = base ** n
            target_a = ((low-3)*q).__floor__()
            target_b = ((high-3)*q).__floor__()
            if target_a != target_b:
                raise AssertionError("pi p-digit prefix not Machin certified")
            minimum_bits = (q-1).bit_length()
            for k in range(minimum_bits, minimum_bits+120):
                j0 = ((low-3)*(1<<k)).__floor__()
                j1 = ((high-3)*(1<<k)).__floor__()
                if j0 != j1:
                    continue
                guess = decode_target_prefix(j0, k, base, n)
                if guess == target_a:
                    break
            else:
                raise AssertionError("failed to certify a bounded pi prefix")
            assert 0 <= j0 < (1<<k)
            # Store only integer digit codes and certified depths, not huge intervals.
            rows.append({"base":base,"digits":n,"bit_depth":k,
                         "ideal_bits":minimum_bits,"extra_bits":k-minimum_bits,
                         "target_prefix_integer":target_a,
                         "binary_prefix_integer":j0,
                         "decoding_unique":True})
    return {"machin_terms_per_arctangent":90,
            "strict_interval_width_below_2_to_minus_300":True,
            "pi_source":"16*atan(1/5)-4*atan(1/239), exact alternating rational enclosures",
            "rows":rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    finite = [dyadic_carry_branch_certificate(p, tau)
              for p in (41,97,257)
              for tau in (Q(1,4),Q(1,16),Q(1,64))]
    meshes = [cross_radix_bad_cylinders(p, 3, ((p**3-1).bit_length()+4))
              for p in (2,3,5,7,11,13,16)]
    meshes = [{**row,"bad_haar_mass":str(row['bad_haar_mass'])}
              for row in meshes]
    # Reassert the bit-level and primitive-shell identities by a method
    # independent of a particular observed histogram.
    for q in range(2,40):
        k=(q-1).bit_length()+5
        # formula for a general q (including mixed 2,3 factors)
        bad=sum(1 for a in range(1,q) if (a*(1<<k))%q)
        assert bad==q-gcd(q,1<<k)
    watched=["observational_succ/pi_dyadic_prime_transfer.py",
             "tests/test_pi_dyadic_prime_transfer.py",
             "scripts/pi_dyadic_prime_transfer_probe.py"]
    out={"claim_status":"EXACT_FINITE_PLUS_CONDITIONAL_THEOREMS",
         "pi_normality":"OPEN","selected_1_over_16_branch_loss":"UNVERIFIED",
         "probe_type":"adversarial_exact_and_independent_machin",
         "branch_rows":finite,"mesh_rows":meshes,
         "selected_pi_prefixes":_selected_pi_digit_probe(),
         "file_sha256":{path:sha256((ROOT/path).read_bytes()).hexdigest()
                         for path in watched}}
    payload=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.write_text(payload)
    else:
        print(payload,end='')


if __name__=='__main__':
    main()
