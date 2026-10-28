#!/usr/bin/env python3
"""Independent Fraction sweep of Gamma's complete uniform speed domain.

Imports no census, witness, source generator, or certificate implementation.
The primary census uses a common integer grid and a single-band criterion.
This replay instead rebuilds and merges every actual Fraction source band
for surviving pairs, with the larger uniform B_n cutoff.
"""
import argparse
from fractions import Fraction as F
import hashlib
from itertools import combinations
import json
from pathlib import Path


def gaps(n, speeds):
    bands = sorted((max(F(0), F(k*n-1, n*v)), min(F(1), F(k*n+1, n*v)))
                   for v in speeds for k in range(v+1))
    result, end = [], F(0)
    for a, b in bands:
        if a > end:
            result.append((end, a))
        end = max(end, b)
    if end < 1:
        result.append((end, F(1)))
    return result


def census(n):
    if n < 5:
        raise ValueError('The proved bound requires n>=5')
    bound = F(56) if n == 5 else F(60) if n == 6 else F((n-2)**2*(n-1), n-4)
    max_first = (bound.numerator-1)//bound.denominator
    covers, first_count, second_count, raw_count = [], 0, 0, 0
    for r1, r2 in combinations(range(1, n), 2):
        retained = tuple(v for v in range(1, n) if v not in (r1, r2))
        for w1 in range(n, max_first+1):
            first_count += 1
            residual = gaps(n, retained+(w1,))
            if not residual:
                raise ArithmeticError('A one-insertion cover contradicts Gamma-05')
            raw_count += (2*(n-1)-1)*w1
            max_width = max(b-a for a, b in residual)
            cap = min(2*(n-1)*w1, F(2, n)//max_width)
            for w2 in range(w1+1, cap+1):
                second_count += 1
                if not gaps(n, retained+(w1, w2)):
                    covers.append({'removed': [r1,r2], 'inserted': [w1,w2]})
    return {'n': n, 'uniform_first_bound': [bound.numerator,bound.denominator],
            'first_count': first_count, 'bounded_pair_domain': raw_count,
            'full_fraction_cover_checks': second_count, 'covers': covers}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--min-n',type=int,default=5)
    parser.add_argument('--max-n',type=int,default=8)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if not 5 <= args.min_n <= args.max_n:
        parser.error('require 5<=min-n<=max-n')
    records=[]
    for n in range(args.min_n,args.max_n+1):
        row=census(n)
        records.append(row)
        print(n, row['first_count'], row['full_fraction_cover_checks'],row['covers'],flush=True)
    result={'schema':'succ.lonely-runner.independent-census.v1',
            'authority':'Executed Fraction union sweep; Gamma paper proof supplies finite completeness.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'no_primary_census_import':True, 'records':records}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':
    main()
