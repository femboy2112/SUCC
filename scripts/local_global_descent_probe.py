#!/usr/bin/env python3
"""Machine-readable finite source-relative local-to-global receipts."""
import json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.local_global_descent import (
    VoltageSource, Dart, construct_chart, assemble_charts, verify_result,
    edge_chart_cover,
)
from observational_succ.nonabelian_local_global import (
    s3_commutator_square, glue_group_charts, verify_group_verdict, sign,
)
from observational_succ.constructive_gluing_tower import (
    gaussian_voltage_source, run_diagonal_tower,
)
from observational_succ.gaussian_holonomy import GaussianSieve
from observational_succ.cycle_support_budget import fundamental_cycle_certificate


def triangle(k):
    vs=((0,),(1,),(2,))
    g=VoltageSource('triangle3',vs,(Dart('a',vs[0],vs[1],(1,)),
         Dart('b',vs[1],vs[2],(1,)),Dart('c',vs[2],vs[0],(k,))),1,3)
    patches=tuple(construct_chart(g,name,ds,lone_vertex=isolated)
                  for name,ds,isolated in edge_chart_cover(g))
    result=assemble_charts(g,patches)
    verify_result(g,patches,result)
    return result


def main():
    positive=triangle(-2)
    negative=triangle(1)
    group,sections=s3_commutator_square()
    gv=glue_group_charts(group,sections)
    verify_group_verdict(group,sections,gv)
    sieve=GaussianSieve(((1,2),(2,3)))
    source=gaussian_voltage_source(sieve,1)
    ladder=run_diagonal_tower(source,levels=3)
    result=ladder.proof_at_E()
    topological=fundamental_cycle_certificate(source)
    assert result.status=='GLUED' and result.largest_component==580
    assert positive.status=='GLUED' and negative.status=='OBSTRUCTED'
    assert topological.global_exact
    assert gv.status=='OBSTRUCTED' and sign(gv.source_holonomy)==1
    data={
      'scope':'CLASSICAL/PROVED LOCAL finite graph/groupoid and declared arithmetic source',
      'fully_independent_source_authentication':False,
      'gaussian_all_D_proved':False,
      'physical_instant_succ':False,
      'yes_triangular_gluing':positive.status,
      'no_triangular_gluing':negative.status,
      'actual_source_negative_displacement':negative.obstruction.displacement,
      'actual_source_negative_cycle_steps':len(negative.obstruction.lifted_walk),
      's3_noncommutative_status':gv.status,
      's3_abelian_sign':sign(gv.source_holonomy),
      's3_nonidentity_transport':gv.source_holonomy,
      'gaussian':{
         'period':source.period,
         'source_digest':source.digest,
         'vertices':result.checked_vertices,
         'directed_darts':result.checked_darts,
         'connected_components':topological.components,
         'fundamental_cycles_in_dart_presentation':topological.independent_cycles,
         'local_independent_charts':result.charts,
         'overlap_conditions':result.overlap_conditions,
         'largest_component':result.largest_component,
         'tower_transmission_events':result.total_hops,
         'tower_chart_references_transmitted':result.transmitted_references,
         'E_epistemic_macro_succ':result.epistemic_macros_at_E,
         'constructed_global_potential_only_at_E':not hasattr(ladder,'potentials'),
       }
    }
    print(json.dumps(data,indent=2,sort_keys=True))

if __name__=='__main__':main()
