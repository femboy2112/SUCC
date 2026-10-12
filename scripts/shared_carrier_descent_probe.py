#!/usr/bin/env python3
"""Emit exact finite shared-carrier and holographic boundary certificates."""
import json
import sys
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.shared_carrier_descent import SharedSource, Evidence, SharedCarrierGraph


def run():
    C=SharedSource('fundamental-source',1,'bit-frame',tuple(range(8)),
        {'a':tuple((i>>2)&1 for i in range(8)),
         'b':tuple((i>>1)&1 for i in range(8)),
         'c':tuple(i&1 for i in range(8))},
        {'parity':tuple(i.bit_count()%2 for i in range(8))})
    recovered=C.conclude(tuple(C.report(p,5,'E-'+p) for p in ('a','b','c')),'parity')
    partial=C.factorization(('a','b'),'parity')
    even=SharedSource('parity-carrier',1,'even-frame',(0,3,5,6),
                      {str(k):tuple((i>>k)&1 for i in (0,3,5,6)) for k in (0,1,2)},
                      {'even-parity':(0,0,0,0)})
    inconsistent=even.pairwise_and_global_consistency(tuple(
        Evidence('parity-carrier',1,'even-frame',str(k),1,'E-'+str(k)) for k in (0,1,2)))
    G=SharedCarrierGraph('ring+center',0,('b0','b1','b2','b3','u'),
        ('b0','b1','b2','b3'),
        (('b0','b1',1),('b1','b2',1),('b2','b3',1),('b3','b0',1),
         ('u','b0',1),('u','b1',1),('u','b2',1),('u','b3',1)))
    energy=G.completion_receipt({'b0':1,'b1':0,'b2':0,'b3':0})
    P=SharedCarrierGraph('three-edge-path',0,('a','u','v','b'),('a','b'),
                         (('a','u',1),('u','v',1),('v','b',1)))
    path=P.completion_receipt({'a':0,'b':1})
    return {'source_factorization_complete':recovered['status']=='PROVED',
            'source_alias_without_all_probes':not partial['factors'],
            'pairwise_consistent_but_globally_impossible':(
                inconsistent['pairwise_realizable'] and not inconsistent['globally_realizable']),
            'wheel':energy,'wheel_DtN':G.boundary_operator(),
            'two_interior_path':path,'path_DtN':P.boundary_operator(),
            'nested_reduction':P.nested_boundary_reduction(('a','u','b')), 
            'global_interior_source_certified':False,
            'archimedean_place_identified':False,
            'conditional_harmonic_law':True}

if __name__=='__main__':
    r=run()
    assert r['nested_reduction']['commuting_square_verified'] is True
    assert r['source_factorization_complete']
    assert r['pairwise_consistent_but_globally_impossible']
    assert r['wheel']['reconstructed_interior']==(('u',F(1,4)),)
    assert r['two_interior_path']['reconstructed_interior']==(('u',F(1,3)),('v',F(2,3)))
    print(json.dumps(r,default=str,sort_keys=True,indent=2))
