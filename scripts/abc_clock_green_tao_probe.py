#!/usr/bin/env python3
"""Finite exact ABC envelope census with adversarial prime-AP controls.

Run from a checkout: python scripts/abc_clock_green_tao_probe.py --limit 1200
No result of this census can establish an unrestricted ABC upper bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from json import dumps

from observational_succ.abc_clock_families import (
    ABCTriple, exact_local_clock, finite_envelope, prime_progression_lifts, radical,
)


def summary(limit: int = 1200) -> dict:
    split = limit // 2
    epsilons = (F(0), F(1, 10), F(1, 2))
    train = finite_envelope(split, epsilons)
    holdout = finite_envelope(limit, epsilons, split+1)
    comparisons = {}
    for e in epsilons:
        tv, tt = train["maxima"][e]
        hv, ht = holdout["maxima"][e]
        unseen = set(holdout["families"][e]) - set(train["families"][e])
        comparisons[str(e)] = {
            "train_witness": [tt.a, tt.b, tt.c],
            "holdout_witness": [ht.a, ht.b, ht.c],
            "train_raised_score": str(tv),
            "holdout_raised_score": str(hv),
            "holdout_exceeds_train": hv > tv,
            "unseen_holdout_family_count": len(unseen),
        }
    prime_ap = {}
    for triple in ((3, 5, 7), (5, 11, 17)):
        linear, square = prime_progression_lifts(*triple)
        prime_ap["-".join(map(str,triple))] = {
            "linear_abc": [linear.a,linear.b,linear.c],
            "linear_ris": linear.ris,
            "square_abc": [square.a,square.b,square.c],
            "square_ris": square.ris,
            "square_radical": square.radical,
            "square_abc_excess": str(square.abc_quality_excess(F(0))),
        }
    positive_nonprime_ap = ABCTriple(63,1,64)  # 7,8,9 are NOT all primes.
    return {
        "scope": "FINITE ENUMERATION, not a universal bound or ABC/RH proof",
        "upper_c_inclusive": limit,
        "train_upper_c_inclusive": split,
        "train_primitive_unordered_triples": train["count"],
        "holdout_primitive_unordered_triples": holdout["count"],
        "train_abc_hits_eps0": train["hits_eps0"],
        "holdout_abc_hits_eps0": holdout["hits_eps0"],
        "finite_envelope": comparisons,
        "local_haar_p2_k2": {k:str(v) for k,v in exact_local_clock(2,2).items()},
        "green_tao_prime_progression_lifts": prime_ap,
        "hostile_nonprime_square_lift_abc_hit": {
            "abc":[positive_nonprime_ap.a,positive_nonprime_ap.b,positive_nonprime_ap.c],
            "rad": positive_nonprime_ap.radical,
            "ratio": str(positive_nonprime_ap.abc_quality_excess(F(0))),
        },
        "source_firewall": "No zeta zeros, Green-Tao implementation, ABC oracle, or RH positivity involved",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit",type=int,default=1200,
                        help="3..10000: upper c bound (runtime grows quadratically)")
    args = parser.parse_args()
    if args.limit < 6:
        parser.error("limit >=6 required for train/holdout")
    print(dumps(summary(args.limit), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
