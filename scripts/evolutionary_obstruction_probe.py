#!/usr/bin/env python3
"""Reproducible exact receipts; the learner never sees benchmark coordinates."""
from pathlib import Path
from fractions import Fraction as Q
from dataclasses import replace
from itertools import product
import json
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.obstruction_discovery_lab import discovery_case
from observational_succ.evolving_bridge_search import evolve_with_obstructions
from observational_succ.evolutionary_bridge_search import ternary_fusion_demo
from observational_succ.relational_model_genetics import Capsule, Port, PairedSourceTable, project
from observational_succ.source_aware_amalgamation import (
    Context, Marginal, separator_bayes_square, StochasticAction, Hypothesis,
    CausalReceipt, EvolvingEvidence, credal_target_interval,
)
from observational_succ.evolving_observer_categories import (
    Action, Readout, FiniteDynamics, PartialTransitionTable, SynthesisError,
)


def bridge_case(n):
    values=tuple(map(str,range(n))); coded=tuple('token'+str((2*i+1)%n) for i in range(n))
    left=Capsule('clock','clock','same',0,'v',(Port('x',values),Port('y',values)),
                 tuple((str(i),str((i+1)%n)) for i in range(n)))
    right=Capsule('thermal','thermal','same',0,'v',(Port('t',coded),Port('z',values)),
                  tuple((coded[i],str((i-1)%n)) for i in range(n)))
    table=PairedSourceTable('same',0,'v',Port('y',values),Port('t',coded),
                            tuple(('s'+str(i),str(i),coded[i]) for i in range(n)),True)
    reports=[evolve_with_obstructions(left,right,table,seed=i) for i in range(20)]
    return {'domain_size':n,'runs':len(reports),
            'all_source_checked':all(r.complete_declared_source for r in reports),
            'new_relation':project(reports[0].child,('x','z')),
            'max_checks':max(len(r.proposals) for r in reports),
            'max_counterexamples':max(len(r.exclusions) for r in reports),
            'full_enumerator_used':any(r.full_permutation_enumeration_used for r in reports)}


def probabilistic_receipt():
    context=Context('shared-carrier',0,'joint-law')
    rows=tuple(product((0,1),repeat=2))
    left=Marginal(context,('a','y'),rows,(Q(3,8),Q(1,8),Q(1,8),Q(3,8)))
    right=Marginal(context,('y','b'),rows,(Q(1,4),)*4)
    sq=separator_bayes_square(left,right,{(0,):Q(1,4),(1,):Q(3,4)})
    identity=((Q(1),Q(0)),(Q(0),Q(1)))
    erase=StochasticAction('erase',('0','1'),((Q(1),Q(0)),)*2,identity)
    flip=StochasticAction('flip',('0','1'),((Q(0),Q(1)),(Q(1),Q(0))),identity)
    h=Hypothesis('source',(Q(1,2),Q(1,2)),(erase,flip),('old0','old1'))
    e=EvolvingEvidence(context,(h,),(Q(1),))
    pending=e.receive(CausalReceipt('late',1,context,'flip','1'))
    complete=e.receive(CausalReceipt('early',0,context,'erase','0'))
    positive=Marginal(context,('a','b'),rows,(Q(1,2),Q(0),Q(0),Q(1,2)))
    negative=Marginal(context,('a','b'),rows,(Q(0),Q(1,2),Q(1,2),Q(0)))
    pri=left.project(('y',)); post=sq['posterior'].project(('y',))
    duplicate_weights={y:post[y]*post[y]/pri[y] for y in pri}
    wrong_probability=duplicate_weights[(1,)]/sum(duplicate_weights.values(),Q(0))
    return {'separator_posterior':[[str(k[0]),str(v)] for k,v in sq['posterior'].project(('y',)).items()],
            'counted_shared_evidence':sq['shared_evidence_count'],
            'wrong_squared_evidence_posterior':str(wrong_probability),
            'delayed_before_gap_filled':pending,
            'after_causal_replay':complete,
            'current_state':sorted({current for _,_,current in e.joint}),
            'same_marginals_joint_equality_range':credal_target_interval((positive,negative),lambda r:r['a']==r['b'])}


def main():
    spec=json.loads((Path(__file__).resolve().parents[1]/'research/2026-10-13/DISCOVERY_PRECOMMIT.json').read_text())
    all_cases=[spec['calibration']]+spec['heldout']
    result={
        'schema':'succ-evolutionary-obstruction-v1',
        'base_commit':'1cb30a3d92420f1197fc1615a68fb4309c0e036d',
        'precommitted_design_commit':'93d67f25b1552f0aa78aff0589ca1a59baa32f7a',
        'scope':'exact finite simulator laws; fixed composition metagrammar; no unknown-human-theorem claim',
        'opaque_discovery_cases':[discovery_case(c['prime'],c['label_seed']) for c in all_cases],
        'old_genetic_failed_seeds':[i for i in range(20) if not ternary_fusion_demo(i)['genetic_succeeded']],
        'constraint_evolution':[bridge_case(n) for n in (3,5,7)],
        'joint_evidence':probabilistic_receipt(),
        'universal_lean_kernel':'formal/obstruction_synthesis/RepairKernel.lean; verification status is CI, not a literal proof flag',
        'python_algorithm_formally_refined_to_lean':False,
        'unrestricted_grammar_invention':False,
        'physical_source_authenticated':False,
        'RH_or_Weil_positivity_proved':False,
    }
    print(json.dumps(result,default=lambda x:str(x) if isinstance(x,Q) else repr(x),indent=2,sort_keys=True))

if __name__=='__main__':main()
