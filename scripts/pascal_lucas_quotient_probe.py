"""Reproducible exact Lucas quotient and four-bit controls. No pi source claims."""
from __future__ import annotations

import json
from fractions import Fraction as Q
from math import comb

from observational_succ.pascal_lucas_quotient import (
    address_to_pair, four_bit_rank_residual, histogram_average,
    histogram_zeta_apply, lucas_total, lucas_unit, pair_to_address,
    uniform_embedding_tv, zeta_apply, lucas_residue_apply,
)


def main() -> None:
    comparisons = 0
    for p, depth in ((2, 7), (3, 4), (5, 3), (7, 2)):
        for n in range(p**depth):
            for k in range(n+1):
                assert lucas_unit(p,n,k) == (comb(n,k) % p != 0)
                comparisons += 1
        for address in range(lucas_total(p,min(depth,3))):
            m=min(depth,3)
            n,k=address_to_pair(p,m,address)
            assert pair_to_address(p,m,n,k)==address
            comparisons += 1
    quotient_checks=0
    for p,depth in ((2,5),(3,3),(5,2)):
        values=tuple(Q((i*23+11)%31-15,13) for i in range(p**depth))
        assert histogram_average(p,depth,zeta_apply(p,depth,values)) == \
            histogram_zeta_apply(p,depth,histogram_average(p,depth,values))
        quotient_checks += 1
    gate={str(m):str(four_bit_rank_residual(m)) for m in range(4,13)}
    assert gate['5']=='1/40'
    assert uniform_embedding_tv(2,3,4)==Q(15,16)
    assert lucas_residue_apply(3,1,(0,1,0))[2]==2
    assert zeta_apply(3,1,(0,1,0))[2]==1
    left,right=address_to_pair(2,2,3),address_to_pair(2,2,1)
    next_left,next_right=address_to_pair(2,2,4),address_to_pair(2,2,2)
    assert tuple(x.bit_count() for x in left)==tuple(x.bit_count() for x in right)
    assert tuple(x.bit_count() for x in next_left)!=tuple(x.bit_count() for x in next_right)
    data={
        'scope':'exact finite Lucas cells and synthetic rank-gate control; not BBP',
        'lucas_direct_integer_comparisons': comparisons,
        'independent_tensor_quotient_comparisons':quotient_checks,
        'four_bit_synthetic_rank_mse':gate,
        'lucas_state_dimensions': {str(p): [lucas_total(p,m) for m in range(1,5)] for p in (2,3,5)},
        'two_to_three_uniform_overlap_at_four_digits':'1/16',
        'two_to_three_uniform_tv_at_four_digits':'15/16',
        'ternary_succ_rank_descent':'REFUTED: (0,1),(1,0) -> (1,1),(2,0)',
        'prime_three_support_equals_residue':'REFUTED: binom(2,1)=2 mod 3',
        'pi_normality':'OPEN',
    }
    print(json.dumps(data,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
