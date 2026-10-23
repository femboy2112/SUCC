"""Deterministic, exact-rational HISTORY-DTN execution receipt (no physics fitting)."""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from observational_succ.growing_dtn_history import (
    ConductiveState, field_weighted_subset_process,
    exact_forward_backward, history_affine_square, replay,
)


def diamond():
    return ConductiveState(('L','R','u','v'),('L','R'),(
        ('L','u',F(1)),('u','R',F(1)),('L','v',F(1)),('v','R',F(1))))


def receipt():
    base=diamond()
    hidden=base.with_edge('u','v',F(7))
    ordinary=base.with_edge('L','u',F(1))
    revealed=hidden.with_edge('L','u',F(1))
    a,g1=base.adaptive_edge('u','v',1,(0,1),1)
    b,g2=ordinary.adaptive_edge('u','v',1,(0,1),1)
    a=a.with_edge('L','u',1)
    labels={'a':('L','u',F(1)),'b':('u','v',F(1)),
            'c':('L','R',F(1))}
    levels,kernels=field_weighted_subset_process(base,labels,2,F(1,3))
    fb=exact_forward_backward(levels,kernels,{frozenset():F(1)},
                              {x:F('a' in x) for x in levels[-1]})
    states=replay(base,(('L','u',1),('L','R',F(1,2)),('u','v',F(3))))
    chart=history_affine_square(states,1,2)
    return {
        'claim_type':'CLASSICAL identities + PROVED LOCAL exact rational finite models',
        'underlying_network':'2 electrodes, 2 symmetric interior vertices, 4 unit arms',
        'initial_effective_conductance':str(base.energy((0,1))),
        'hidden_edge_strength':'7',
        'hidden_present_DtN_equal':hidden.response()==base.response(),
        'future_unmodified_effective_conductance':str(ordinary.energy((0,1))),
        'future_hidden_effective_conductance':str(revealed.energy((0,1))),
        'future_probe_distinguishes':ordinary.response()!=revealed.response(),
        'feedback_conductance_order_a':str(g1),
        'feedback_conductance_order_b':str(g2),
        'feedback_effective_order_a':str(a.energy((0,1))),
        'feedback_effective_order_b':str(b.energy((0,1))),
        'feedback_order_defect':str(b.energy((0,1))-a.energy((0,1))),
        'two_direction_event_probability':str(fb['event_probability']),
        'two_direction_overlap_all_equal':len(set(fb['overlap']))==1,
        'two_direction_overlap':list(map(str,fb['overlap'])),
        'arithmetic_clock_routes':[list(chart['S_then_Vp_indices']),
                                   list(chart['Vp_then_Sp_indices'])],
        'arith_clock_same_terminal_DtN':chart['terminal_equal'],
        'physical_FUCC_action_from_wood_derived':False,
        'cherenkov_physical_inference':False,
        'RH_proved':False,
    }


if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]
    r=receipt()
    for rel in ('observational_succ/growing_dtn_history.py',
                'tests/test_growing_dtn_history.py',
                'scripts/growing_dtn_history_probe.py'):
        r.setdefault('source_sha256',{})[rel]=hashlib.sha256((root/rel).read_bytes()).hexdigest()
    print(json.dumps(r,indent=2,sort_keys=True))
