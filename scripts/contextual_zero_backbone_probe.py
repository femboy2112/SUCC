#!/usr/bin/env python3
"""One-source finite SUCC observer/zero/policy and hostile evidence replay."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q

from observational_succ.coherent_zero_relations import Poly, ZeroRelation
from observational_succ.contextual_zero_navigation import (
    Probe,Move,SourceField,initial_knowledge,inspect_zero,model_observe,
    model_move,plan_guaranteed,check_policy,realize_policy_in_model,gauge_potential,
)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    source='synthetic-Z4-observer'
    names=('x',)
    x=Poly.var(names,'x')
    field=SourceField(source,names,tuple((Q(i),) for i in range(4)),
       (ZeroRelation(source,'finite carrier identity',x*(x-1)*(x-2)*(x-3)),
        ZeroRelation(source,'reflexive identity',x-x)),
       (Probe(source,'observe-position',x,1),),
       (Move(source,'left',(3,0,1,2),1),Move(source,'right',(1,2,3,0),1)))
    initial=initial_knowledge(field,budget=3)
    proposal=plan_guaranteed(field,initial,(0,))
    outcomes=[]
    for actual in range(4):
        observed,w=realize_policy_in_model(field,initial,actual,(0,),proposal.policy)
        outcomes.append({'initial_world':actual,'goal_world':w,'spent':3-observed.budget,
                         'events':[e.kind for e in observed.journal]})
    after_observe=model_observe(field,initial,2,'observe-position')
    after_move,new_world=model_move(field,after_observe,2,'right')
    initial_claim=inspect_zero(field,initial,x-2)
    learned_claim=inspect_zero(field,after_observe,x-2)
    moved_claim=inspect_zero(field,after_move,x-2)
    if args.verify:
        assert initial_claim.compatible_with_current_belief
        assert not initial_claim.entailed_at_current_belief
        assert learned_claim.entailed_at_current_belief
        assert not learned_claim.global_on_finite_carrier
        assert not moved_claim.compatible_with_current_belief
        assert new_world==3
        assert not initial.journal
        assert proposal.worst_cost==check_policy(field,initial,(0,),proposal.policy)==3
        assert all(w['goal_world']==0 and w['spent']<=3 for w in outcomes)
        assert gauge_potential((1,3,7),1)==gauge_potential((11,13,17),1)
    print(json.dumps({
       'source':source,
       'declared_environment_only':True,
       'zero_ideal_refinement':{'initial_entailed':initial_claim.entailed_at_current_belief,
                                'learned_entailed':learned_claim.entailed_at_current_belief,
                                'after_move_entailed':moved_claim.entailed_at_current_belief},
       'goal':0,'guarantee':proposal.status,'worst_case_paid_cost':proposal.worst_cost,
       'candidate_policy_not_actualized':len(initial.journal)==0,
       'per_hidden_world_receipts':outcomes,
       'local_verification':'passed' if args.verify else 'not_requested',
       'physical_source_authenticated':False,
       'QFT_vacuum_claim':False,
       'pi_normality_proved':False,
       'RH_proved':False,
    },indent=2,sort_keys=True))


if __name__=='__main__':
    main()
