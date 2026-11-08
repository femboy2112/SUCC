"""Source-specific high-pole Gaussian split strip and exact denominator product.

No asymptotic claims inferred from these finite probes. Universal proof in
THEOREMS.md; PNT in AP is separately cited classical prior art.
"""
from __future__ import annotations
from fractions import Fraction
from math import prod, log
import json
from hologram import state, forcing, is_prime


def split_strip(n:int)->tuple[list[int],list[int]]:
    if n<2:raise ValueError('n>=2')
    primes=[p for p in range(4*n+1,8*n-6) if is_prime(p)]
    return [p for p in primes if p%4==1],[p for p in primes if p%4==3]


def audit(n:int)->dict:
    split,inert=split_strip(n)
    u=state(n);d=u.denominator
    pp=prod(split)
    assert d%pp==0
    assert all((d%p==0 and d%(p*p)!=0) for p in split)
    assert all(d%p for p in inert)
    # Also directly test mutated first-pole: 4 -> 0, split by p mod8.
    um=Fraction(0)
    for j in range(1,n+1):
        um=16*um+forcing(j,(0,-2,-1,-1))
    for p in split:
        if p%8==1:
            assert um.denominator%p!=0
        else:
            assert p%8==5 and um.denominator%p==0
    return {'n':n,'split_count':len(split),'inert_count':len(inert),
            'split_primes':split if n<=32 else [],
            'gaussian_split_product_bits':pp.bit_length(),
            'original_denominator_bits':d.bit_length(),
            'ratio_log_denominator_to_n':round(log(d)/n,10),
            'ratio_log_split_product_to_n':round(sum(log(p) for p in split)/n,10),
            'first_pole_mutant_checked':True}


def main():
    return {'source':'four signed original BBP poles; U0=0',
            'analysis_status':'OBSERVED_FINITE; universal divisor theorem separately PROVED LOCAL',
            'epochs':[audit(n) for n in (8,16,32,64,128,257)]}

if __name__=='__main__':print(json.dumps(main(),sort_keys=True,indent=2))
