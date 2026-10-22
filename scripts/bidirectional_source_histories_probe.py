"""Deterministic exact source-provenance probe for BIDIR-HISTORY-2026-10-22.

Run: python scripts/bidirectional_source_histories_probe.py --verify-receipt
No floats, fabricated p-adic carrier, quantum amplitude simulator, or physics fit.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.growing_dtn_history import ConductiveState
from observational_succ.bidirectional_source_histories import (
    LabelledMarkovSource,bicausal_observation_quotient,
    endpoint_marginal,lift_field_growth_source,distinguishable_order_budget,
)


def diamond():
    return ConductiveState(('L','R','u','v'),('L','R'),(
        ('L','u',Q(1)),('u','R',Q(1)),('L','v',Q(1)),('v','R',Q(1))))


def digest_path_measure(paths):
    canonical='\n'.join(f'{path.start_clock}|{",".join(path.labels)}|{mass}'
                        for path,mass in sorted(paths.items(),key=lambda pair:pair[0].labels))
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()


def report():
    base=diamond()
    small=lift_field_growth_source(base,
        {'a':('L','u',Q(1)),'b':('u','v',Q(1))},2,Q(1,3))
    small_paths=small.segment(1,3,frozenset())
    small_weights={','.join(p.labels):str(mass) for p,mass in small_paths.items()}
    assert small_weights=={'a,b':'7/11','b,a':'4/11'}
    assert all(small.pathwise_balance(path,{frozenset():Q(1)})['equal']
               for path in small_paths)
    candidates={'a':('L','u',Q(1)),'b':('u','v',Q(1)),
                'c':('L','R',Q(1,2)),'d':('R','v',Q(1,3)),
                'e':('L','v',Q(2,3))}
    rich=lift_field_growth_source(base,candidates,5,Q(1,3))
    braid=rich.affine_braid(2,2,frozenset({'a'}))
    left,right=braid['S_then_Vp_paths'],braid['Vp_then_Sp_paths']
    assert left==right and len(left)==24 and sum(left.values(),Q())==1
    assert len(endpoint_marginal(left))==1
    actual_reverse=rich.posterior_paths(2,6,{x:Q(x==frozenset({'a'})) for x in rich.levels[1]},
                                         frozenset(candidates))
    assert actual_reverse==left
    # Brute-force path probability multiplication is independent of the
    # route-decomposition control; labelled source data are not reconstructed
    # from the (single) endpoint. Individual paths carry distinct rational mass.
    independently={}
    for path in left:
        mass=Q(1)
        for j,label in enumerate(path.labels):
            clock=1+j # prefix begins at clock 2, so transition index = j+1
            x,y=path.states[j:j+2]
            mass*=next(q for ell,z,q in rich.transitions[clock][x]
                       if ell==label and z==y)
        independently[path]=mass
    assert independently==left
    bare=base
    hidden=bare.with_edge('u','v',Q(7))
    a=bare.with_edge('L','u',Q(1))
    b=hidden.with_edge('L','u',Q(1))
    c=LabelledMarkovSource(((bare,hidden),(a,b)),
         ({bare:(('probe_Lu',a,Q(1)),),hidden:(('probe_Lu',b,Q(1)),)},))
    quotient=bicausal_observation_quotient(c,{bare:Q(1,2),hidden:Q(1,2)},
       ({bare:bare.response(),hidden:hidden.response()},
        {a:a.response(),b:b.response()}))
    assert quotient['initial_partitions'][0]==(0,0)
    assert quotient['partitions'][0]==(0,1)
    assert a.energy((0,1))==Q(7,6) and b.energy((0,1))==Q(49,41)
    file_paths=('observational_succ/bidirectional_source_histories.py',
                'tests/test_bidirectional_source_histories.py',
                'scripts/bidirectional_source_histories_probe.py')
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in file_paths}
    return {
        'source_commit_parent':'391c304e768d073ae747459d279e14d5357092e5',
        'source_branch_parent':'research/history-dtn-succ-fucc-2026-10-22',
        'arith_clock':'p=2,n=2, 2->3->6 versus 2->4->5->6',
        'braid_complete_paths':len(left),
        'braid_probability':str(sum(left.values(),Q())),
        'braid_paths_source_identical':left==right,
        'braid_pathmeasure_sha256':digest_path_measure(left),
        'braid_complete_endpoint_states':len(endpoint_marginal(left)),
        'braid_independent_path_product':independently==left,
        'material_two_order_weights':small_weights,
        'material_two_order_endpoint_count':len(endpoint_marginal(small_paths)),
        'material_two_order_nonexchangeable':small_weights['a,b']!=small_weights['b,a'],
        'material_hidden_edge_current_response_equal':bare.response()==hidden.response(),
        'material_future_probe_effective_conductances':[str(a.energy((0,1))),str(b.energy((0,1)))],
        'future_safe_quotient_splits_hidden_material':quotient['partitions'][0]==(0,1),
        'four_events_required_source_order_bits':distinguishable_order_budget(4)['minimal_binary_bits'],
        'five_events_required_source_order_bits':distinguishable_order_budget(5)['minimal_binary_bits'],
        'source_hash_sha256':hashes,
        'scope':'exact finite synthetic source/finite passive DtN, not intrinsic prime physics, not RH',
    }


def main():
    observed=report()
    receipt=ROOT/'research/2026-10-22/BIDIR_SOURCE_HISTORIES_RECEIPT.json'
    if '--verify-receipt' in sys.argv:
        if not receipt.is_file():
            raise SystemExit('expected committed receipt missing')
        expected=json.loads(receipt.read_text(encoding='utf-8'))
        if observed!=expected:
            raise SystemExit('source-hashed receipt mismatch; rerun and inspect, never blindly overwrite')
    print(json.dumps(observed,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
