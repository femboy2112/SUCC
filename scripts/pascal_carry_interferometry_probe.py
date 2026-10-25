#!/usr/bin/env python3
"""Selected BBP / Pascal / signed Walsh receipts, exact arithmetic.

Parent module supplies y0=0 and the original four-pole recurrence. This
probe never replaces the authentic source with a random orbit or Galois mean.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.pascal_carry_interferometry import (
    even_parity_countermodel, forcing_pascal_certificate, kummer_carries,
    lucas_mod_p, pascal_source_jet, prime_clock_pascal_gain,
    source_pascal_tomography,
)


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    rows=[source_pascal_tomography(p,tau)
          for p in (41,97,257)
          for tau in (Q(1,4),Q(1,16),Q(1,64))]
    pascal_differences=[forcing_pascal_certificate(n,k)
                        for n in (6,13,33,128) for k in (1,2,4,8)]
    jets=[pascal_source_jet(n,k)
          for n,k in ((6,2),(13,3),(33,4),(33,6),(128,8))]
    prime_clocks=[prime_clock_pascal_gain(p,2,k)
                  for p in (3,5,7,11,13,17,41,97) for k in (1,2,4)]
    lucas_check_count=0
    kummer_check_count=0
    from math import comb
    for p in (2,3,5,7,11,13):
        for n in range(65):
            for k in range(n+1):
                assert lucas_mod_p(n,k,p)==comb(n,k)%p
                lucas_check_count+=1
                actual=comb(n,k)
                val=0
                while actual%p==0:
                    actual//=p
                    val+=1
                assert kummer_carries(n,k,p)==val
                kummer_check_count+=1
    watched=['observational_succ/pascal_carry_interferometry.py',
             'tests/test_pascal_carry_interferometry.py',
             'scripts/pascal_carry_interferometry_probe.py',
             'observational_succ/pi_dyadic_prime_transfer.py']
    result={
      'status':'EXACT_FINITE_and_paper_proofs; no selected asymptotic cancellation',
      'pi_base16_normality':'OPEN','pi_base3_normality':'OPEN',
      'source':'authentic signed BBP with y0=0',
      'previous_branch':'research/pi-dyadic-prime-transfer-2026-10-24',
      'lucas_binomial_cross_checks':lucas_check_count,
      'kummer_binomial_cross_checks':kummer_check_count,
      'pascal_forcing_differences':pascal_differences,
      'source_pascal_jets':jets,
      'prime_clock_gain_controls':prime_clocks,
      'actual_source_rows':rows,
      'three_wise_independent_counterexample':even_parity_countermodel(),
      'theorem_budget':{
        'signed_fourier_jet':'15 integer circle modes plus actual BBP eta and centered delta+ correction',
        'R2_terminal_absolute':'O(d^2*p^(-6/5)) = O(p^(4/5)) = o(d)',
        'Rceil_logp_all_scales':'o(1) total absolute truncation error (paper bound)',
        'signed_jet_O_d':'UNPROVED',
        'selected_four_gate_O_d':'UNPROVED'},
      'source_sha256':{path:sha256((ROOT/path).read_bytes()).hexdigest()
                       for path in watched},
    }
    payload=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.write_text(payload)
    else:
        print(payload,end='')

if __name__=='__main__':
    main()
