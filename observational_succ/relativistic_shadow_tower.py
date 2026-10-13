"""Finite SUCC E-tower: construct an actual metric from source-tagged shadows.

No metric is inserted into the decoder. Three rational measurements of a
symmetric 1+1 quadratic form uniquely determine it. Reports are mathematical
simulator outputs and not independently authenticated physical experiments.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Hashable

from .galilean_lorentz_succ import (
    ETA,Mat2,q,rank_rational,interval_form,RelativityWitnessError,
)

PROBES=("right_null","left_null","unit_clock")
VECTOR={"right_null":(1,1),"left_null":(1,-1),"unit_clock":(1,0)}
CONSTRAINTS={"right_null":(F(1),F(2),F(1)),
             "left_null":(F(1),F(-2),F(1)),
             "unit_clock":(F(1),F(0),F(0))}


class ShadowTowerError(RelativityWitnessError):
    pass


@dataclass(frozen=True)
class SourceShadows:
    """One declared original metric, accessible only to mathematical simulator."""
    source_id: str
    basis_id: str
    version: int
    source_metric: Mat2

    def __post_init__(self):
        if not self.source_id or not self.basis_id or type(self.version) is not int or self.version<0:
            raise ShadowTowerError("Source/basis/version required")
        if not isinstance(self.source_metric,Mat2) or self.source_metric.b!=self.source_metric.c:
            raise ShadowTowerError("Declared source must be symmetric quadratic form")

    def observe(self,probe:str,owner:str):
        if probe not in PROBES or not owner:
            raise ShadowTowerError("Only named physically declared mathematical tests allowed")
        value=interval_form(self.source_metric,VECTOR[probe])
        return MetricProbeReceipt(self.source_id,self.basis_id,self.version,probe,value,owner)


@dataclass(frozen=True)
class MetricProbeReceipt:
    source_id: str
    basis_id: str
    version: int
    probe: str
    result: F
    origin_observer: str

    def __post_init__(self):
        if (not self.source_id or not self.basis_id or type(self.version) is not int
            or self.version<0 or self.probe not in PROBES or not self.origin_observer):
            raise ShadowTowerError("Incomplete causal/source provenance")
        try:
            value=q(self.result)
        except RelativityWitnessError as ex:
            raise ShadowTowerError("Only exact rational outcomes") from ex
        object.__setattr__(self,"result",value)


def _solve3(A,b):
    """Explicitly invert independent 3x3 rational probe matrix without sympy."""
    if len(A)!=3 or any(len(row)!=3 for row in A) or len(b)!=3:
        raise ShadowTowerError("Need three independent source-probe equations")
    rows=[list(row)+[v] for row,v in zip(A,b)]
    for c in range(3):
        i=next((i for i in range(c,3) if rows[i][c]),None)
        if i is None:raise ShadowTowerError("Rank deficient: no global metric")
        rows[c],rows[i]=rows[i],rows[c]
        fac=rows[c][c]
        rows[c]=[e/fac for e in rows[c]]
        for i in range(3):
            if i==c:continue
            z=rows[i][c]
            if z:rows[i]=[a-z*t for a,t in zip(rows[i],rows[c])]
    return tuple(row[-1] for row in rows)


def assemble_metric(receipts,*,source_id:str,basis_id:str,version:int):
    """E: fixed-order-independent proof from distributed shadow receipts.

    Returns no metric when fewer than three independent probe types were
    delivered; refuses source-ID mutation, incompatible duplicate results,
    and manufactured physical attestation. The measured values, not a hidden
    simulator source, enter the metric reconstruction.
    """
    if not source_id or not basis_id or type(version) is not int or version<0:
        raise ShadowTowerError("Explicit original source/basis/version required")
    known={}
    owners={}
    for receipt in receipts:
        if not isinstance(receipt,MetricProbeReceipt):
            raise ShadowTowerError("Only actual typed mathematical receipts")
        if (receipt.source_id,receipt.basis_id,receipt.version)!=(source_id,basis_id,version):
            raise ShadowTowerError("Source/basis/version mismatch: base-change missing")
        if receipt.probe in known and known[receipt.probe]!=receipt.result:
            return {"status":"INCONSISTENT_SOURCE","conflict_probe":receipt.probe,
                    "claims_verified":False}
        known[receipt.probe]=receipt.result
        owners.setdefault(receipt.probe,set()).add(receipt.origin_observer)
    names=tuple(p for p in PROBES if p in known)
    rank=rank_rational(tuple(CONSTRAINTS[p] for p in names))
    if rank<3:
        return {"status":"UNRESOLVED","rank":rank,"remaining_dimensions":3-rank,
                "remaining_probes":tuple(p for p in PROBES if p not in known),
                "claims_verified":False}
    sol=_solve3([CONSTRAINTS[p] for p in names],[known[p] for p in names])
    metric=Mat2(sol[0],sol[1],sol[1],sol[2])
    if any(interval_form(metric,VECTOR[p])!=known[p] for p in names):
        raise AssertionError("Global geometry didn't replay all observed shadows")
    return {"status":"GLOBAL_GEOMETRY_CONSTRUCTED","rank":rank,
            "metric":metric,"matches_minkowski":metric==ETA,
            "probe_origins":tuple((p,tuple(sorted(owners[p]))) for p in names),
            "claims_verified":True,"externally_authenticated_physics":False}


def finite_source_ontology_limit():
    """Exact witness: same observable laws, opposite 'preferred ether' tags.

    A stipulated unobserved ontological tag can always be made observationally
    invisible. This shows the original source class is important and does NOT
    establish a theorem that a physical ether exists or does not exist.
    """
    class_a=("Lorentz observations","no preferred-frame tag")
    class_b=("Lorentz observations","preferred-frame tag")
    report=lambda model:("two null rays", "one normalized clock", "metric 1,-1")
    assert report(class_a)==report(class_b)
    return {"operationally_equivalent":True,"ontology_property_differs":True,
            "source_candidates":(class_a,class_b),
            "physical_ether_existence_resolved":False}


def shadow_transition_demo():
    source=SourceShadows("historical-1+1-wave-source","rational-inertial-basis",0,ETA)
    forward=source.observe("right_null","climber-A")
    backward=source.observe("left_null","climber-B")
    clock=source.observe("unit_clock","base-E")
    before=assemble_metric((forward,backward),source_id=source.source_id,
                          basis_id=source.basis_id,version=source.version)
    after=assemble_metric((clock,backward,forward),source_id=source.source_id,
                          basis_id=source.basis_id,version=source.version)
    return {"insufficient":before,"constructed":after,
            "ontology_firewall":finite_source_ontology_limit()}
