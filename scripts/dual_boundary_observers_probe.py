#!/usr/bin/env python3
"""Exact dual E/E'' source-correlating and boundary-gluing receipt."""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from observational_succ.dual_boundary_observers import (
    DualFiniteTower, TwoSidedHarmonicCarrier,
    unit_path_two_port, symmetric_binary_chain_end_correlation)
from observational_succ.shared_carrier_descent import SharedCarrierGraph
from observational_succ.dual_chart_riemann_roch import (
    cech_dimensions, dual_chart_from_global, cech_reduce)


def report():
    full=tuple(product((0,1),repeat=2))
    parity=tuple(a^b for a,b in full)
    t=DualFiniteTower('original 2-bit carrier',1,full,(F(1,4),)*4,
                      ((0,0,1,1),),((0,1,0,1),))
    xor={name:t.claim_factors(parity,name)['factors']
         for name in ('left','right','joint')}
    assert xor=={'left':False,'right':False,'joint':True}
    assert t.common_factor()['component_count']==1
    three=tuple(product((0,1),repeat=3))
    k=DualFiniteTower('original 3-bit carrier',1,three,(F(1,8),)*8,
                     (tuple((c,a) for c,a,b in three),),
                     (tuple((c,b) for c,a,b in three),))
    common=k.common_factor()
    assert common['component_count']==2
    assert common['exact_common_witness_covariance']==F(1,4)
    source=DualFiniteTower('3-state',1,(0,1,2),(F(1,3),)*3,
                           ((0,0,1),),((0,1,1),))
    target=(F(0),F(1),F(2))
    fg=source.conditional_expectation(source.conditional_expectation(target,'right'),'left')
    gf=source.conditional_expectation(source.conditional_expectation(target,'left'),'right')
    anti=source.correlation_receipt((0,1,0))
    assert fg != gf and anti['estimate_covariance']==-F(1,36)
    left=SharedCarrierGraph('one-carrier',9,(0,1,2),(0,2),
                            ((0,1,F(1)),(1,2,F(1))))
    right=SharedCarrierGraph('one-carrier',9,(2,3,4),(2,4),
                             ((2,3,F(1)),(3,4,F(1))))
    dual=TwoSidedHarmonicCarrier(left,right,(0,),(4,),(2,))
    joined=dual.interface_solution({0:0},{4:1})
    assert joined['source_field']=={0:0,1:F(1,4),2:F(1,2),3:F(3,4),4:1}
    path=unit_path_two_port(12)
    markov=symmetric_binary_chain_end_correlation(12,F(1,4))
    assert path['effective_conductance']==F(1,12)
    assert markov['endpoint_covariance']==F(1,4096)
    rr={str(k):cech_dimensions(k) for k in (-3,-2,-1,0,1,2,3)}
    section=dual_chart_from_global(2,{0:F(1),1:F(2),2:F(3)})
    obstruction=cech_reduce(-2,{-1:F(1)})
    assert all(x['genus_zero_rr_verified'] for x in rr.values())
    assert section['infinity_chart']=={0:F(3),1:F(2),2:F(1)}
    assert obstruction['obstruction_class']=={-1:F(1)}
    return {
      'riemann_sphere_dual_chart':{
          'rr_dimensions':{k:{'h0':v['h0_dimension'],'h1':v['h1_dimension'],
                               'chi':v['euler_characteristic']} for k,v in rr.items()},
          'k2_zero_chart':{str(k):str(v) for k,v in section['zero_chart'].items()},
          'k2_infinity_chart':{str(k):str(v) for k,v in section['infinity_chart'].items()},
          'k_minus2_obstruction':{str(k):str(v) for k,v in obstruction['obstruction_class'].items()},
          'actual_archimedean_arithmetic_identified':False},
      'status':'PROVED LOCAL conditional classical models; exact Fraction calculations',
      'common_fundamental_carrier_physically_authenticated':False,
      'archimedean_prime_or_gamma_identified':False,
      'RH_implied':False,
      'two_bit_join_proves_parity_when_each_side_cannot':xor,
      'shared_nonconstant_witness':{
          'components':common['component_count'],
          'source_masses':list(map(str,common['common_component_masses'])),
          'covariance':str(common['exact_common_witness_covariance'])},
      'projection_order_noncommutation':{
          'left_after_right':list(map(str,fg)),
          'right_after_left':list(map(str,gf)),
          'negative_covariance_same_carrier':str(anti['estimate_covariance'])},
      'joined_harmonic_halves':{
          'interface':{str(q):str(v) for q,v in joined['interface'].items()},
          'source_field':{str(q):str(v) for q,v in joined['source_field'].items()},
          'interface_flux_zero':all(x==0 for x in joined['interface_flux_residual'].values()),
          'energy':str(joined['global_energy'])},
      'infinite_separation_controls':{
          'unit_resistor_12_effective_conductance':str(path['effective_conductance']),
          'shared_markov_12_endpoint_covariance':str(markov['endpoint_covariance']),
          'same_endpoint_marginals_do_not_force_correlation':True},
      'final_epistemic_macro_updates_claimed_constant_time':False,
    }

if __name__=='__main__':
    print(json.dumps(report(),sort_keys=True,indent=2))
