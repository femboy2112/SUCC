"""Frozen finite miniature carrier audit; run from any working directory."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.miniature_carrier import (  # noqa: E402
    Carrier, Mini, compile_factor, compile_subcarrier, compile_dual_product,
    compile_nested_factor, future_partition, dark_target_witness, cyclic_successor_factor,
)
from observational_succ.miniature_stochastic import (  # noqa: E402
    StochasticCarrier, StochasticMini, joint_factor,
)
from observational_succ.dual_shell_observer import (  # noqa: E402
    meeting_certificate, late_hidden_source, noncommuting_boundary_witness,
)


def receipt() -> dict:
    states = tuple(str(i) for i in range(4))
    step = {str(i): str((i+1) % 4) for i in range(4)}
    p = Carrier(states, {'inc':step},
                {c: str(int(c)%2) for c in states}, ('0',), 'clock4-v1')
    m = Mini(('0','1'), {'flip':{'0':'1','1':'0'}},
             {'0':'0','1':'1'}, '0', 'clock4-v1')
    pi = {c:str(int(c)%2) for c in states}
    factor = compile_factor(p,m,pi,{'flip':('inc',)})
    failed_literal = compile_subcarrier(p,m,{'0':'0','1':'1'},{'flip':('inc',)})
    minst = future_partition(p)
    source = ('00','01','10','11')
    actions = {'left':{c: str(1-int(c[0]))+c[1] for c in source},
               'right':{c:c[0]+str(1-int(c[1])) for c in source}}
    p2 = Carrier(source, actions, {c:c for c in source}, ('00',),'dual-v1')
    bit = Mini(('0','1'), {'flip':{'0':'1','1':'0'}},
               {'0':'0','1':'1'}, '0', 'dual-v1')
    left={c:c[0] for c in source}
    right={c:c[1] for c in source}
    genuine_joint = compile_dual_product(p2,bit,bit,left,right,
                     ('left',),('right',),{c:(c[0],c[1]) for c in source})
    corr_states=('00','11')
    flip={c:('11' if c=='00' else '00') for c in corr_states}
    corr = Carrier(corr_states,{'left':flip,'right':flip},
                   {c:c for c in corr_states},('00',),'dual-v1')
    fake_joint=compile_dual_product(corr,bit,bit,
                     {c:c[0] for c in corr_states},{c:c[1] for c in corr_states},
                     ('left',),('right',),{c:(c[0],c[1]) for c in corr_states})
    hs=tuple(f's{s}m{mm}' for s in '01' for mm in '01')
    hidden_actions={'flip':{c:c[:3]+str(1-int(c[-1])) for c in hs}}
    hidden=Carrier(hs,hidden_actions,{c:c[-1] for c in hs},
                   ('s0m0','s1m0'),'hidden-v1')
    original_target={c:c[1] for c in hs}
    dark=dark_target_witness(hidden,original_target)
    new_actions={**hidden_actions, 'copy_source_to_memory':{c:c[:3]+c[1] for c in hs}}
    expanded=Carrier(hs,new_actions,{c:c[-1] for c in hs},
                     ('s0m0','s1m0'),'hidden-v1')
    lit=dark_target_witness(expanded,original_target)
    # Source-correct stochastic factor and a mutation that preserves only marginals.
    coin = StochasticMini(('a','b'),{'coin':{
        'a':(('H','a',Q(1,2)),('T','b',Q(1,2))),
        'b':(('H','b',Q(1,2)),('T','a',Q(1,2)))
    }},'a','stoch-v1')
    parent_rows={c: (('H',c[0]+c[1],Q(1,2)),
                      ('T',('b' if c[0]=='a' else 'a')+c[1],Q(1,2)))
                 for c in ('a0','a1','b0','b1')}
    stoch=StochasticCarrier(tuple(parent_rows),{'coin':parent_rows},
                            ('a0','a1'),'stoch-v1')
    decoder={c:c[0] for c in parent_rows}
    stoch_yes=joint_factor(stoch,coin,decoder,{'coin':'coin'})
    mutant_rows={**parent_rows,'a1':(('H','b1',Q(1,2)),('T','a1',Q(1,2)))}
    stoch_bad=StochasticCarrier(tuple(parent_rows),{'coin':mutant_rows},
                                ('a0','a1'),'stoch-v1')
    stoch_no=joint_factor(stoch_bad,coin,decoder,{'coin':'coin'})
    # Nested 8-state parent: compile 3 middle steps, each costing 2 ticks.
    e8=tuple(str(i) for i in range(8))
    parent=Carrier(e8,{'tick':{c:str((int(c)+1)%8) for c in e8}},
                   {c:str((int(c)//2)%2) for c in e8},('0',),'nest')
    mid=Mini(tuple(str(i) for i in range(4)),
             {'step':{str(i):str((i+1)%4) for i in range(4)}},
             {str(i):str(i%2) for i in range(4)},'0','nest')
    child=Mini(('0','1'),{'flip':{'0':'1','1':'0'}},
               {'0':'0','1':'1'},'0','nest')
    nested=compile_nested_factor(parent,mid,child,
               {c:str(int(c)//2) for c in e8},
               {str(i):str(i%2) for i in range(4)},
               {'step':('tick','tick')},
               {'flip':('step','step','step')},budget=6)
    shell=meeting_certificate(late_hidden_source(2,4),2,4)
    return {
        'origin':'femboy2112/SUCC',
        'stacked_parent_commit':'2b56342524f93dcbf280bedd44bb64da92b13412',
        'source_attestation':False,
        'invariant_section_rejected':failed_literal['reason'],
        'virtual_factor_certified':factor['certified'],
        'canonical_observable_quotient':minst['final_model_states'],
        'whole_family_cyclic_nonsplit': cyclic_successor_factor(12,4),
        'independent_dual_product_certified':genuine_joint['certified'],
        'ghost_dual_product_rejected':fake_joint['reason'],
        'unobservable_original_source':dark['reason'],
        'source_access_with_new_declared_probe':lit['certified'],
        'stochastic_joint_factor_certified':stoch_yes['certified'],
        'matched_marginal_joint_mutant_rejected':stoch_no['reason'],
        'nested_mini_compilation':{
            'certified': nested['certified'],
            'expanded_parent_primitive_steps': nested['effective_parent_step_cost'],
            'new_primitive_action_created':not nested['no_new_primitive_action_constructed']},
        'zero_centered_shell_connection':{
            'first_four_complementary_shells_zero':not shell['resolved'],
            'remaining_source_energy':str(shell['tail_squared_norm']),
            'successor_projection_commutator':noncommuting_boundary_witness()['commutator_at_cell_1']},
        'original_source_labels_not_read_by_compiler':True,
        'no_nontrivial_zeta_zeros_used':True,
        'no_gamma_or_Weil_positivity_claim':True,
        'RH_proved':False,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output')
    args=ap.parse_args()
    text=json.dumps(receipt(),sort_keys=True,indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(text,encoding='utf-8')
    else:
        print(text,end='')


if __name__=='__main__':
    main()
