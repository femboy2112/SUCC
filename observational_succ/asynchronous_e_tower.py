"""Asynchronous causal evidence and proof acceptance at E, without global 'now'.

Finite mathematical event logs with original-source proof fibers and licensed
causal communication. Distinct frame coordinate times cannot manufacture a
receipt; source authenticity and real probe/communication hardware are
DECLARED assumptions, not verified physical properties.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from types import MappingProxyType
from typing import Hashable, Mapping

from .covariant_observer_frames import CausalLedger, CausalEvent, EventPoint, FrameError


class TowerError(ValueError):
    pass


@dataclass(frozen=True)
class OriginalCarrierTheory:
    source_id: str
    basis_id: str
    states: tuple[Hashable,...]
    probes: Mapping[str,tuple[Hashable,...]]
    claims: Mapping[str,tuple[Hashable,...]]

    def __post_init__(self):
        if not self.source_id or not self.basis_id or not self.states or len(set(self.states))!=len(self.states):
            raise TowerError("One declared source, shared basis and nonempty states")
        if not self.probes or not self.claims:
            raise TowerError("At least one probe and one source-relative target")
        for name,table in tuple(self.probes.items())+tuple(self.claims.items()):
            if not name or len(table)!=len(self.states):
                raise TowerError("Every table must be total on original source class")
            for value in table:hash(value)
        object.__setattr__(self,"probes",MappingProxyType({k:tuple(v) for k,v in self.probes.items()}))
        object.__setattr__(self,"claims",MappingProxyType({k:tuple(v) for k,v in self.claims.items()}))

    def simulated_probe(self,probe:str,source:Hashable)->Hashable:
        """Simulator ONLY. E never receives 'source' in the acceptance method."""
        if probe not in self.probes or source not in self.states:raise TowerError("Unknown source/probe")
        return self.probes[probe][self.states.index(source)]

    def compatible_sources(self,readings:tuple[tuple[str,Hashable],...])->tuple[Hashable,...]:
        for key,value in readings:
            if key not in self.probes:raise TowerError("Undeclared proof probe")
            hash(value)
        return tuple(s for i,s in enumerate(self.states) if all(self.probes[key][i]==value
                      for key,value in readings))

    def conclude(self,readings:tuple[tuple[str,Hashable],...],claim:str)->dict:
        if claim not in self.claims:raise TowerError("Undeclared original source target")
        fiber=self.compatible_sources(readings)
        if not fiber:return {"status":"INCONSISTENT_SOURCE","fiber":(),"claim_value":None}
        values={self.claims[claim][self.states.index(s)] for s in fiber}
        if len(values)==1:return {"status":"PROVED","fiber":fiber,"claim_value":next(iter(values))}
        return {"status":"UNRESOLVED","fiber":fiber,"claim_value":None}


@dataclass(frozen=True)
class EvidenceTower:
    ledger: CausalLedger
    theory: OriginalCarrierTheory

    def __post_init__(self):
        if {e.source_id for e in self.ledger.events}!={self.theory.source_id}:
            raise TowerError("Causal carrier identity does not match proof source")
        for e in self.ledger.events:
            if e.kind=="probe":
                if len(e.payload)!=3 or e.payload[2]!=self.theory.basis_id:
                    raise TowerError("Probe must include source-basis version and outcome")
                if e.payload[0] not in self.theory.probes:
                    raise TowerError("Unlicensed empirical probe")

    def evidence_at(self,checkpoint:str)->tuple[tuple[str,Hashable],...]:
        probelist=self.ledger.certified_probes_at(checkpoint)
        return tuple((e.payload[0],e.payload[1]) for e in probelist)

    def decide(self,checkpoint:str,claim:str)->dict:
        """Only authentic-to-the-DECLARED-log original-source probe facts are decoded."""
        facts=self.evidence_at(checkpoint)
        result=self.theory.conclude(facts,claim)
        result.update({"checkpoint":checkpoint,"source_id":self.theory.source_id,
                       "basis_id":self.theory.basis_id,
                       "causal_probe_count":len(facts),
                       "causal_probes":tuple(e.ident for e in self.ledger.certified_probes_at(checkpoint)),
                       "physical_sensor_authentication":False,
                       "one_epistemic_macro_update_not_instantaneous":True})
        return result

    def minimal_support(self,checkpoint:str,claim:str,*,max_probes:int=16)->dict:
        """Find smallest received proof-support subset, never invent receipts."""
        probes=self.ledger.certified_probes_at(checkpoint)
        if len(probes)>max_probes:raise TowerError("Proof-support combinatorial resource limit")
        full=self.decide(checkpoint,claim)
        if full["status"]!="PROVED":return {"status":full["status"],"support":()}
        for k in range(len(probes)+1):
            for selection in combinations(probes,k):
                r=self.theory.conclude(tuple((e.payload[0],e.payload[1]) for e in selection),claim)
                if r["status"]=="PROVED" and r["claim_value"]==full["claim_value"]:
                    return {"status":"PROVED","support":tuple(e.ident for e in selection),
                            "source_fiber":r["fiber"],"minimum_size":k}
        raise AssertionError("Full valid proof-support not found")

    def checkpoint_chain(self,checkpoints:tuple[str,...],claim:str)->dict:
        """Compare a LOCAL, causally growing chain of receipt checkpoints.

        Different chains need not share clock times. Each successor must list
        the previous checkpoint among its actual causal ancestors. This is a
        finite trace, not a theorem that an infinite fair delivery occurs.
        """
        if not checkpoints or len(set(checkpoints))!=len(checkpoints):
            raise TowerError("A nonempty causal checkpoint sequence is required")
        stages=[]
        for index,k in enumerate(checkpoints):
            if self.ledger.get(k).kind!="checkpoint":raise TowerError("Noncheckpoint in E chain")
            if index and checkpoints[index-1] not in self.ledger.causal_ancestry(k):
                raise TowerError("A checkpoint is not causally descended from the previous one")
            stages.append(self.decide(k,claim))
        first=next((i for i,z in enumerate(stages) if z["status"]=="PROVED"),None)
        return {"first_proof_index":first,"status_by_stage":tuple(x["status"] for x in stages),
                "final_claim_value":stages[-1]["claim_value"],
                "final_probe_ids":stages[-1]["causal_probes"],
                "source_id":self.theory.source_id}

    def claim_frame_invariance(self,checkpoint:str,claim:str,*frames)->dict:
        """Acceptance uses causal event IDs, never coordinate-time simultaneity."""
        if not frames:raise TowerError("Supply at least one explicit observer frame")
        decision=self.decide(checkpoint,claim)
        cuts=tuple(self.ledger.slice_at_anchor(frame,checkpoint) for frame in frames)
        # Different coordinate cuts MAY disagree; decision still uses same ancestry.
        return {"decision":decision["status"],"value":decision["claim_value"],
                "different_coordinate_cuts":len(set(cuts))>1,
                "same_causal_receipts":True,"causal_receipt_count":decision["causal_probe_count"]}


def asynchronous_e_demo()->dict:
    from fractions import Fraction as F
    from .covariant_observer_frames import LorentzFrame
    theory=OriginalCarrierTheory("one-declared-source","two-bits-v1",
        ("00","01","10","11"),
        {"a":(0,0,1,1),"b":(0,1,0,1)},
        {"XOR":(0,1,1,0)})
    led=CausalLedger((
      CausalEvent("branch_A",EventPoint(0,-1),"probe",theory.source_id,(),("a",1,theory.basis_id)),
      CausalEvent("branch_B",EventPoint(0,1),"probe",theory.source_id,(),("b",0,theory.basis_id)),
      CausalEvent("E_early",EventPoint(1,0),"checkpoint",theory.source_id,("branch_A",)),
      CausalEvent("E_late",EventPoint(2,0),"checkpoint",theory.source_id,("branch_A","branch_B","E_early")),
      CausalEvent("E_initial",EventPoint(0,0),"checkpoint",theory.source_id),
      ))
    tower=EvidenceTower(led,theory)
    early=tower.decide("E_early","XOR")
    late=tower.decide("E_late","XOR")
    support=tower.minimal_support("E_late","XOR")
    two_frames=tower.claim_frame_invariance("E_initial","XOR",
      LorentzFrame.identity(),LorentzFrame.boost("x",F(1,3)))
    if early["status"]!="UNRESOLVED" or late["claim_value"]!=1 or late["status"]!="PROVED":
        raise AssertionError("False asynchronous original-source proof")
    return {"early_status":early["status"],"late_status":late["status"],
            "accepted_original_XOR":late["claim_value"],
            "minimal_causal_proof_support":support["support"],
            "one_E_inference_macro_step":True,
            "different_simultaneity_cuts":two_frames["different_coordinate_cuts"],
            "receipt_latency_physical":True,
            "real_carrier_authentication":False}
