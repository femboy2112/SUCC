#!/usr/bin/env python3
"""Deterministic, exact Oily->observer finite-difference receipt."""
from __future__ import annotations
import json
from fractions import Fraction as Q
from pathlib import Path
from sys import path

path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.wavefront_oracle_two_stage import (
    SourceGeometry,run_two_stages,recurrence_residual,
    depth_defect_residual,critical_grade,critical_second_difference,
    finite_memory_information_defects,
)

def f(q):
    q=Q(q)
    return f"{q.numerator}/{q.denominator}" if q.denominator!=1 else str(q.numerator)

def main():
    xs=(Q(1,5),Q(1,2),Q(4,5),Q(1))
    source=[Q((j*j+5)%17-6,j+1) for j in range(20)]
    runs=[]
    for x in xs:
        g=SourceGeometry(x)
        e1,e2=run_two_stages(source,x)
        residual=recurrence_residual(source,x)
        defect=depth_defect_residual(source,x)
        assert not any(residual) and not any(defect)
        runs.append({"x":f(x),"u":f(g.u),"v":f(g.v),
            "characteristic_discriminant":f(g.discrim),
            "source_total_R":f(g.source_total()),
            "packet_first_six":[f(g.grade_probability(j)) for j in range(6)],
            "first_stage_sample":[f(v) for v in e1[:7]],
            "second_stage_sample":[f(v) for v in e2[:7]],
            "all_20_order2_residuals_zero":True,
            "all_20_depth_defect_residuals_zero":True})
    endpoint={"w_first_eight":[f(critical_grade(j)) for j in range(8)],
        "second_difference_first_80_all_zero":all(critical_second_difference(j)==0 for j in range(80)),
        "extra_mean":f(SourceGeometry(Q(1)).mean_extra_delay()),
        "extra_variance":f(SourceGeometry(Q(1)).variance_extra_delay()),
        "min_physical_latency":2,
        "mean_physical_latency":f(2+SourceGeometry(Q(1)).mean_extra_delay())}
    assert endpoint["second_difference_first_80_all_zero"]
    out={"source":"original Oily positive BBP packet, Main XIII research status",
        "epistemic_optimality":"UNVERIFIED: formal causal filter only",
        "controls":{"iid_innovation_variance_one_MSE_depth_0_to_3":
            [f(v) for v in finite_memory_information_defects(9,3, Q(1))],
            "predictable_innovation_MSE_depth_0_to_3":
            [f(v) for v in finite_memory_information_defects(9,3, Q(0))]},
        "runs":runs,"critical":endpoint,
        "claims":"WEO-01..07 scoped; WEO-08..09 unverified"}
    target=Path(__file__).resolve().parents[1]/"research/2026-10-28/WAVEFRONT_ORACLE_TWO_STAGE_RECEIPT.json"
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(f"WEO_SOURCE_RECURSION_VERIFIED four rational x, 80 critical differences; {target}")

if __name__=='__main__':main()
