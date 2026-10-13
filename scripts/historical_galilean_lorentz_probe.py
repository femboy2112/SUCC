#!/usr/bin/env python3
"""Reproducible exact SUCC historical Galilean/Lorentz mathematical receipts."""
import json
import sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.galilean_lorentz_succ import (
  galilean_to_lorentz_case, galilean_moving_medium_wave_operator,
  free_particle_galilean,metric_shadow_constraints,rational_boost,ETA,
)
from observational_succ.relativistic_shadow_tower import shadow_transition_demo
from observational_succ.maxwell_transverse_shadow import maxwell_subsystem_demo


def as_jsonable(value):
    if isinstance(value,F):return str(value)
    if isinstance(value,dict):return {k:as_jsonable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [as_jsonable(v) for v in value]
    if hasattr(value,'serialize'):return value.serialize()
    if value is None or isinstance(value,(bool,int,str)):return value
    raise TypeError(f"Unexpected unserializable evidence object {type(value)}")


def main():
    case=galilean_to_lorentz_case()
    shadow=shadow_transition_demo()
    maxwell=maxwell_subsystem_demo()
    moving=galilean_moving_medium_wave_operator(F(3,5))
    old=free_particle_galilean(F(7,2),F(4,3),F(3,5))
    out={
      'status':'EXACT_HISTORICAL_SOURCE_MODEL_RECONSTRUCTION_NOT_HISTORICAL_MEASUREMENT',
      'scope':'1+1 classical Galilean/Lorentz source wave and transverse Maxwell',
      'empirical_source_authentication':False,
      'results':{
        'mechanical_old_field_positive':old,
        'galilean_obstruction':case,
        'distributed_metric_shadows':shadow,
        'transverse_maxwell_subsystem':maxwell,
        'moving_medium_counter_repair':moving,
        'missing_clock_gauge_dimension':metric_shadow_constraints()['free_geometry_dimensions'],
        'with_clock_metric_unique':metric_shadow_constraints(clock=True)['unique_normalized_metric'],
      },
      'source_historical_material':{
        'Einstein1905':'https://sites.pitt.edu/~jdnorton/teaching/HPS_0410/chapters/origins_pathway/On-the_electrodynamics/index.html',
        'MichelsonMorley1887':'https://ajsonline.org/article/62505-on-the-relative-motion-of-the-earth-and-the-luminiferous-ether',
        'MITwave':'https://stuff.mit.edu/afs/athena/course/8/8.20/www/sols/sol1.pdf',
      },
      'all_3d_Maxwell_measured':False,
      'Lorentz_ontology_uniquely_established':False,
      'RH_or_Weil_positivity_proved':False,
    }
    assert case['galilean_quadratic_wave_failure']==F(-42,25)
    assert case['lorentz_operator_defect']==[['0','0'],['0','0']]
    assert shadow['constructed']['metric']==ETA
    assert shadow['insufficient']['status']=='UNRESOLVED'
    assert moving['same_form_vacuum_operator'] is False
    assert maxwell['galilean_principal_trace']==F(-6,5)
    print(json.dumps(as_jsonable(out),sort_keys=True,indent=2))

if __name__=='__main__':main()
