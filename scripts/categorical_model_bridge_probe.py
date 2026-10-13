"""Exact reproducible SUCC certificate: automated repair and model-to-model adapters."""
from __future__ import annotations
import json
from fractions import Fraction
from observational_succ.categorical_repair_synthesis import categorical_repair_demo
from observational_succ.categorical_model_bridges import (
    categorical_bridge_demo, ModelCapsule, discover_model_connections,
    thermal_correspondence,context_depth_witness,
)
from observational_succ.dynamic_boundary_inverse import star,triangle,twin_hubs


def normalize(value):
    if isinstance(value,Fraction):return str(value)
    if isinstance(value,dict):return {str(k):normalize(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [normalize(v) for v in value]
    if value is None or isinstance(value,(bool,int,str)):return value
    raise TypeError(f"Unsupported exact receipt value: {type(value)}")


def make_receipt():
    repaired=categorical_repair_demo()
    bridged=categorical_bridge_demo()
    electric=ModelCapsule(star(),"electrical_RC","same-original",0,"3-port")
    twin=ModelCapsule(twin_hubs(),"electrical_RC","same-original",0,"3-port")
    static=ModelCapsule(triangle(),"electrical_RC","same-original",0,"3-port")
    thermal=thermal_correspondence(electric)["target"]
    graph=discover_model_connections((electric,twin,static,thermal))
    receipt={"source_repair":repaired,"model_bridges":bridged,
        "automatically_discovered_links":graph.links,
        "rejected_links":graph.falsified,
        "connected_behavior_classes":graph.components,
        "static_vs_dynamic_grade":context_depth_witness(electric,static),
        "star_vs_twin_full_frequency_grade":context_depth_witness(electric,twin),
        "math_not_physical_source_identification":True,
        "external_measurement_authenticated":False,
        "source_to_Weil_positivity_identified":False}
    if repaired["mode_dimension"]!=2 or not bridged["parallel_context_equivalent"] or len(graph.links)!=3:
        raise ArithmeticError("SUCC categorical repair/bridge regression failed")
    return normalize(receipt)


if __name__=="__main__":print(json.dumps(make_receipt(),indent=2,sort_keys=True))
