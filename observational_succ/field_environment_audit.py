"""E-tower environmental closure report: never conflate independent gates.

A finite report can certify the declared source TARGET without claiming that
local graph integrability, physical instrument law, or ontological origin is
proved. Missing structural checks remain explicitly NOT_CHECKED.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Hashable, Sequence

from .field_relative_closure import FiniteField, ClosureError, minimal_inconsistent_core
from .field_probe_repair import repair, RepairCertificate
from .field_context_descent import SourceVoltageGraph,DescentAudit,VoltageCertificate


@dataclass(frozen=True)
class EnvironmentalReport:
    source_id: str
    basis_id: str
    original_target: str
    realization_status: str
    compatible_states: tuple[Hashable,...]
    target_status: str
    proved_target_value: Hashable | None
    conflicting_sources: tuple[Hashable,Hashable] | None
    inconsistent_core: tuple[tuple[str,Hashable],...] | None
    repair: RepairCertificate | None
    graph_status: str
    graph_certificate: VoltageCertificate | None
    context_status: str
    unverified_external_source: bool = True


def inspect_environment(field:FiniteField, evidence:Sequence[tuple[str,Hashable]],
                        target:str, *,candidate_new_probes:Sequence[str]=(),
                        graph:SourceVoltageGraph|None=None,
                        frame:DescentAudit|None=None,
                        search_budget:int=65536)->EnvironmentalReport:
    """Compile orthogonal obstruction information; no false success on no-source.

    `candidate_new_probes` is a STATIC mathematical menu. No claim is made
    that new probes are executable on a shared mutable physical carrier.
    """
    if target not in field.targets:
        raise ClosureError("Unknown original target")
    candidates=field.names(candidate_new_probes)
    if frame is not None and frame.old_source_id!=field.source_id:
        raise ClosureError("Frame audit refers to another source")
    if graph is not None and graph.source_id!=field.source_id:
        raise ClosureError("Graph geometry refers to another source")
    r=tuple(evidence)
    fiber=field.source_fiber(r)
    values={field.targets[target][field.states.index(x)] for x in fiber}
    realization="GLOBAL_SOURCE_REALIZED" if fiber else "NO_SOURCE_REALIZATION"
    target_status="DETERMINED" if len(values)==1 else (
                  "UNREALIZABLE" if not fiber else "AMBIGUOUS")
    val=next(iter(values)) if len(values)==1 else None
    disagree=None
    if len(values)>1:
        for i,x in enumerate(fiber):
            if disagree is not None:break
            for y in fiber[i+1:]:
                if field.targets[target][field.states.index(x)]!=field.targets[target][field.states.index(y)]:
                    disagree=(x,y);break
    inconsistency=(minimal_inconsistent_core(field,r,max_subsets=search_budget)
                   if not fiber else None)
    # Graph and frame analyses remain independent even when the target is
    # source-realized; no graph means NOT_CHECKED, never 'integrable'.
    cert=graph.integrate() if graph is not None else None
    if graph is not None:
        graph.verify(cert)
    graph_status=cert.status if cert is not None else "NOT_CHECKED"
    context_status = "NOT_CHECKED" if frame is None else (
        "FULLY_TRANSPORTABLE" if frame.covariance and frame.truth_square and frame.updated_report_proves_original_claim
        else "CONTEXT_BOUNDARY_FAILURE")
    repair_cert=None
    if len(fiber)>1 and len(values)>1 and candidates:
        # Restrict only to currently posterior-compatible original sources;
        # witnessed evidence belongs to a different source report frame.
        positions=tuple(field.states.index(x) for x in fiber)
        post=FiniteField(field.source_id,field.basis_id,fiber,
                         {p:tuple(table[i] for i in positions) for p,table in field.probes.items()},
                         {t:tuple(table[i] for i in positions) for t,table in field.targets.items()})
        repair_cert=repair(post,(),candidates,target,max_subsets=search_budget)
    return EnvironmentalReport(field.source_id,field.basis_id,target,realization,fiber,
                               target_status,val,disagree,
                               inconsistency.minimal_records if inconsistency else None,
                               repair_cert,graph_status,cert,context_status)
