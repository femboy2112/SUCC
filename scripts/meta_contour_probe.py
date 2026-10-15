"""Deterministic finite proof receipt; genuine theta contour separately source-replayed."""
import argparse
import json
from itertools import product, combinations
from pathlib import Path

from observational_succ.recursive_model_interactions import (
    SourceCarrier, leaf, join, project, global_fiber, min_unsat_cores,
    available_information_signature, distinguishable_pairs
)
from observational_succ.recursive_operator_gluing import certify_schur
from observational_succ.certified_contour_observer import (
    certified_contour, point, square
)


def receipt():
    U=SourceCarrier('declared-three-bit-source',0,'abc',('a','b','c'),tuple(product('01',repeat=3)))
    A=leaf(U,'AB_EQUATE',('a','b'),(('0','0'),('1','1')))
    B=leaf(U,'BC_EQUATE',('b','c'),(('0','0'),('1','1')))
    C=leaf(U,'AC_DIFFER',('a','c'),(('0','1'),('1','0')))
    m=join(U,A,B)
    pair_counts=[len(global_fiber(U,pair)) for pair in combinations((A,B,C),2)]
    signature=available_information_signature(U,tuple(tuple(w[i] for w in U.worlds) for i in (0,1)))
    before=distinguishable_pairs(signature)
    after=distinguishable_pairs(tuple((x,x==('1','1')) for x in signature))
    sc=certify_schur(((1,),),((2,),),((1,),))
    return {
      'source':'EXACT_DECLARED_FINITE_SOURCE_NOT_PHYSICAL',
      'parent':'96fbc5eac5705573014c0c8bbd4fc85c63bf1fd9',
      'total_worlds':len(U.worlds),
      'AB_BC_fiber':len(global_fiber(U,(A,B))),
      'derived_AC':[list(x) for x in sorted(project(U,m,('a','c')).allowed)],
      'pairwise_model_fiber_counts':pair_counts,
      'three_way_fiber':len(global_fiber(U,(A,B,C))),
      'minimal_obstruction_support':[sorted(x) for x in min_unsat_cores(U,(A,B,C))],
      'data_processing_distinguishable_pairs':[len(before),len(after)],
      'toy_winding_counts':[
          certified_contour((point(2),),square(1),2).count,
          certified_contour((point(-1,-1),point(1)),square(2),3).count,
          certified_contour((point(1),point(0),point(-1)),square(2),3).count,
      ],
      'positive_marginals_signed_global_schur':str(sc.schur[0][0]),
      'genuine_theta_source_contour_in_this_receipt':'NOT_RUN_IN_FINITE_RECEIPT',
      'completed_weil_positivity':'UNVERIFIED',
      'rh_proved':False,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    data=receipt()
    if args.verify:
        assert data == json.loads(args.verify.read_text(encoding='utf8'))
        print('META_CONTOUR_FINITE_RECEIPT_VERIFIED')
    else:
        print(json.dumps(data,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
