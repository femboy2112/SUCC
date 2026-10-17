"""Deterministic exact probe: independent true-source gate optional."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.prime_hinge_chiral_edge import (
    EdgeHinge, high_moment_chiral_certificate,
    polynomial_prime_derivative_gram, polynomial_prime_quadratic,
    authentic_prime2_interval_gate,
)


def pack(value):
    if isinstance(value,Q):return str(value)
    if isinstance(value,tuple) or isinstance(value,list):return [pack(x) for x in value]
    if isinstance(value,dict):return {str(k):pack(v) for k,v in value.items()}
    return value


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--source',action='store_true',help='also verify the installed authentic original Suzuki source')
    args=parser.parse_args()
    hinge=EdgeHinge(Q(1,2),Q(3,4),Q(1))
    pos=high_moment_chiral_certificate(hinge,4,sign=-1)
    neg=high_moment_chiral_certificate(hinge,4,sign=1)
    poly=(Q(0),Q(2))
    result={'geometry':'single symmetric prime hinge two-edge identity',
            'synthetic_rational_calibration':{'a':'1/2','b':'3/4','w':'1'},
            'hs_squared':hinge.hs_squared(),
            'prime_quadratic_P1':polynomial_prime_quadratic(hinge,poly,poly),
            'derivative_gram_P1':polynomial_prime_derivative_gram(hinge,(poly,))[0][0],
            'positive_high_relative_witness':pos,
            'negative_high_relative_witness':neg,
            'actual_source_authenticated':False,
            'complete_original_source_sign':'OPEN','RH_proved':False}
    if args.source:
        result['actual_prime2_source_gate']=authentic_prime2_interval_gate()
        result['actual_source_authenticated']=True
    if args.verify:
        assert result['prime_quadratic_P1']==Q(-61,15360)
        assert result['derivative_gram_P1']==Q(53,7680)
        assert result['positive_high_relative_witness']['sharp_ratio']==Q(1)
        assert result['negative_high_relative_witness']['sharp_ratio']==Q(-1)
        assert result['positive_high_relative_witness']['gradient_to_K_cost']==Q(234)/(hinge.width**2)
    print(json.dumps(pack(result),indent=2,sort_keys=True))

if __name__=='__main__':
    main()
