"""Typed finite-model superposition: genuine FinSet pullbacks, inferred bridges,
source-relative relational proof, and obstruction certificates.

This module treats a model as a finite relation with explicit ports/domains.
A merge is a natural join, the pullback of the projections to the COMMON
interface, not quantum superposition or unconditional physical identification.
All calculations are exact and finite; source tables are a DECLARED simulator
law, not an empirical attestation. Neither a high heuristic score nor a
consistent pushout authenticates the carrier or proves new physical laws.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import permutations, product, combinations
from typing import Iterable


class GeneticsError(ValueError):
    """Invalid type, source, interface, experiment or representation."""


@dataclass(frozen=True)
class Port:
    name: str
    domain: tuple[str, ...]

    def __post_init__(self):
        if (not self.name or type(self.domain) is not tuple
                or not self.domain or len(set(self.domain)) != len(self.domain)
                or any(type(v) is not str or not v for v in self.domain)):
            raise GeneticsError('A port requires a nonempty finite set of distinct named values')


@dataclass(frozen=True)
class Capsule:
    """One MATHEMATICALLY declared finite relation; not a sourced observation."""
    name: str
    context: str
    source_id: str
    epoch: int
    basis: str
    ports: tuple[Port, ...]
    rows: tuple[tuple[str, ...], ...]
    parents: tuple[str, ...] = ()
    features: frozenset[str] = frozenset()

    def __post_init__(self):
        if (not self.name or not self.context or not self.source_id or not self.basis
                or type(self.epoch) is not int or self.epoch < 0
                or type(self.ports) is not tuple or not self.ports
                or len(set(p.name for p in self.ports)) != len(self.ports)
                or type(self.rows) is not tuple
                or len(set(self.rows)) != len(self.rows)
                or not self.rows or type(self.features) is not frozenset
                or any(type(f) is not str for f in self.features)):
            raise GeneticsError('Malformed typed, nonempty, source-relative finite model')
        for row in self.rows:
            if type(row) is not tuple or len(row) != len(self.ports):
                raise GeneticsError('Malformed state tuple')
            if any(v not in port.domain for port, v in zip(self.ports, row)):
                raise GeneticsError('State violates a declared port domain')

    def value(self, row: tuple[str,...], port_name: str) -> str:
        return row[next(i for i,p in enumerate(self.ports) if p.name == port_name)]

    def signature(self) -> tuple:
        return tuple((p.name, p.domain) for p in self.ports)


def binary_capsule(name: str, context: str, source_id: str,
                   left: str, right: str, xor: int, *, epoch: int=0,
                   basis: str='binary-v1') -> Capsule:
    if type(xor) is not int or xor not in (0,1):
        raise GeneticsError('Binary constraint needs 0 or 1')
    if left == right:
        raise GeneticsError('Two different ports required')
    dom=('0','1')
    return Capsule(name,context,source_id,epoch,basis,
                   (Port(left,dom),Port(right,dom)),
                   tuple((str(a),str(a^xor)) for a in (0,1)),
                   features=frozenset({'affine','parity'}))


def project(model: Capsule, names: tuple[str,...]) -> tuple[tuple[str,...],...]:
    if len(names)!=len(set(names)) or any(p not in {x.name for x in model.ports} for p in names):
        raise GeneticsError('Project only distinct existing ports')
    idx=[next(i for i,p in enumerate(model.ports) if p.name == n) for n in names]
    return tuple(sorted(set(tuple(row[i] for i in idx) for row in model.rows)))


@dataclass(frozen=True)
class PullbackCertificate:
    merged: Capsule|None
    shared: tuple[str,...]
    left_rows: int
    right_rows: int
    compatible_pairs: tuple[tuple[int,int], ...]
    failure_pair: tuple[tuple[str,...],tuple[str,...]]|None

    @property
    def realized(self) -> bool:
        return self.merged is not None


def pullback(a: Capsule, b: Capsule, *, name: str='E-fiber-product') -> PullbackCertificate:
    """Exact finite pullback of row sets over their common value interface.

    No empty relation is falsely promoted to a realized carrier state.
    Intersections only align by EXACT certified canonical port names/domains.
    Cross-source joins require a separately licensed bridge: this function
    refuses source_id/epoch/basis differences rather than equating them.
    """
    if (a.source_id,a.epoch,a.basis)!=(b.source_id,b.epoch,b.basis):
        raise GeneticsError('Cross-source/epoch/basis gluing requires a certified base change')
    ad={p.name:p for p in a.ports};bd={p.name:p for p in b.ports}
    shared=tuple(p.name for p in a.ports if p.name in bd)
    for n in shared:
        if ad[n].domain != bd[n].domain:
            raise GeneticsError('A shared port name cannot silently change its value type')
    merged_ports=a.ports+tuple(p for p in b.ports if p.name not in ad)
    mindex={p.name:i for i,p in enumerate(b.ports)}
    possible=[];rows=[]
    for i,ra in enumerate(a.rows):
        for j,rb in enumerate(b.rows):
            if all(a.value(ra,n)==rb[mindex[n]] for n in shared):
                possible.append((i,j))
                rows.append(ra+tuple(rb[k] for k,p in enumerate(b.ports) if p.name not in ad))
    if not possible:
        return PullbackCertificate(None,shared,len(a.rows),len(b.rows),(),
                                   (a.rows[0],b.rows[0]))
    m=Capsule(name,f'{a.context} ⨝ {b.context}',a.source_id,a.epoch,a.basis,
              merged_ports,tuple(sorted(set(rows))),parents=(a.name,b.name),
              features=a.features|b.features|frozenset({'pullback'}))
    return PullbackCertificate(m,shared,len(a.rows),len(b.rows),tuple(possible),None)


def verify_pullback(a:Capsule,b:Capsule,certificate:PullbackCertificate)->bool:
    """Independent Cartesian row oracle checks universal compatibility set."""
    d=tuple((i,j) for i,ra in enumerate(a.rows) for j,rb in enumerate(b.rows)
            if all(a.value(ra,p.name)==b.value(rb,p.name)
                   for p in a.ports if p.name in {q.name for q in b.ports}))
    if certificate.compatible_pairs!=d:
        raise GeneticsError('Forged fiber-product/compatibility receipt')
    if (certificate.left_rows,certificate.right_rows)!=(len(a.rows),len(b.rows)):
        return False
    if not d:return certificate.merged is None
    m=certificate.merged
    if m is None:return False
    allowed=set()
    for i,j in d:
        ra=a.rows[i];rb=b.rows[j]
        merged=tuple(ra)+tuple(rb[k] for k,p in enumerate(b.ports)
                              if p.name not in {x.name for x in a.ports})
        allowed.add(merged)
    expected_ports=a.ports+tuple(p for p in b.ports if p.name not in {x.name for x in a.ports})
    return (set(m.rows)==allowed and m.ports==expected_ports
            and (m.source_id,m.epoch,m.basis)==(a.source_id,a.epoch,a.basis))


def chain_join(models: tuple[Capsule,...]) -> Capsule|None:
    if not models:raise GeneticsError('At least one model needed')
    current=models[0]
    for i,m in enumerate(models[1:],1):
        r=pullback(current,m,name=f'E-step-{i}')
        if r.merged is None:return None
        current=r.merged
    return current


def minimal_inconsistent_models(models: tuple[Capsule,...]) -> tuple[str,...]|None:
    """Smallest unsatisfiable subset (exhaustive, restricted budget)."""
    if not models or len(models)>12 or len(set(m.name for m in models))!=len(models):
        raise GeneticsError('Require 1..12 distinct candidate models')
    source={(m.source_id,m.epoch,m.basis) for m in models}
    if len(source)!=1:raise GeneticsError('Cannot mix source provenance to forge conflict')
    for n in range(1,len(models)+1):
        for subset in combinations(models,n):
            if chain_join(subset) is None:
                return tuple(m.name for m in subset)
    return None


def functional_dependencies(model: Capsule) -> tuple[tuple[str,str,tuple[tuple[str,str],...]],...]:
    """Exact all-state deterministic one-port maps, including emergent maps."""
    result=[]
    for p in model.ports:
        for q in model.ports:
            if p==q:continue
            f={};ok=True
            for row in model.rows:
                u,v=model.value(row,p.name),model.value(row,q.name)
                if u in f and f[u]!=v:ok=False;break
                f[u]=v
            if ok and len(f)>=2:
                result.append((p.name,q.name,tuple(sorted(f.items()))))
    return tuple(result)


def emergent_dependencies(a:Capsule,b:Capsule,joined:Capsule):
    """An invariant relating ports no single parent even jointly names."""
    ad={p.name for p in a.ports};bd={p.name for p in b.ports}
    return tuple((u,v,m) for u,v,m in functional_dependencies(joined)
                 if (u in ad-bd and v in bd-ad) or (u in bd-ad and v in ad-bd))


@dataclass(frozen=True)
class PairedSourceTable:
    """One mathematical source reports differently named ports to two agents.

    Not empirical attestation; a complete finite source table is explicitly
    an assumption. Observed samples may not exhaust the source class.
    """
    source_id: str
    epoch: int
    basis: str
    left_port: Port
    right_port: Port
    observations: tuple[tuple[str,str,str], ...]  # source state, left, right
    complete_source_class: bool = False

    def __post_init__(self):
        if (not self.source_id or not self.basis or type(self.epoch) is not int
            or self.epoch<0 or not self.observations
            or len({r[0] for r in self.observations})!=len(self.observations)):
            raise GeneticsError('A source-indexed paired observation table is required')
        if any((len(row)!=3 or not row[0] or row[1] not in self.left_port.domain
                or row[2] not in self.right_port.domain) for row in self.observations):
            raise GeneticsError('Unknown source/outcome in paired table')


@dataclass(frozen=True)
class BridgeCandidate:
    source_id: str
    epoch: int
    basis: str
    left_port: Port
    right_port: Port
    mapping: tuple[tuple[str,str], ...]
    supported_rows: int
    complete_source_class: bool

    def __post_init__(self):
        if (not self.source_id or not self.basis or type(self.epoch) is not int
            or self.epoch<0 or type(self.supported_rows) is not int
            or self.supported_rows<0 or type(self.complete_source_class) is not bool):
            raise GeneticsError('Bridge must declare source contract and evidence scope')
        if (tuple(k for k,v in self.mapping)!=self.left_port.domain
            or len(self.mapping)!=len(self.left_port.domain)
            or set(v for k,v in self.mapping)!=set(self.right_port.domain)
            or len({v for k,v in self.mapping})!=len(self.mapping)):
            raise GeneticsError('A bridge must be a full finite value-bijection')

    def forward(self, value:str)->str:
        return dict(self.mapping)[value]


def invent_bijective_bridges(table:PairedSourceTable)->tuple[BridgeCandidate,...]:
    """Synthesize arrows not supplied in grammar; enumerate isomorphisms.

    Completeness is RELATIVE to the finite domains and observed table. A
    candidate valid on incomplete samples remains conjectural for unobserved
    source states. Source-class completeness is a declared assumption.
    """
    left,right=table.left_port,table.right_port
    if len(left.domain)!=len(right.domain):return ()
    result=[]
    for perm in permutations(right.domain):
        f=dict(zip(left.domain,perm))
        if all(f[x]==y for _,x,y in table.observations):
            result.append(BridgeCandidate(table.source_id,table.epoch,table.basis,
                                          left,right,tuple(f.items()),
                                          len(table.observations),table.complete_source_class))
    return tuple(result)


def transport_capsule(model:Capsule,bridge:BridgeCandidate,*,name:str|None=None)->Capsule:
    """Reinterpret right vocabulary in left vocabulary using a SOURCE-typed map.

    Only a candidate hypothesis if the paired table was not exhaustive;
    cannot turn compatible rows into an externally certified physical fact.
    """
    if (model.source_id,model.epoch,model.basis)!=(bridge.source_id,bridge.epoch,bridge.basis):
        raise GeneticsError('Bridge cannot transport an unrelated source version')
    rightname=bridge.right_port.name
    if rightname not in {p.name for p in model.ports}:
        raise GeneticsError('Source target port absent')
    if bridge.left_port.name in {p.name for p in model.ports if p.name!=rightname}:
        raise GeneticsError('Transport causes an unproved variable identification')
    p=next(p for p in model.ports if p.name==rightname)
    if p.domain!=bridge.right_port.domain:
        raise GeneticsError('Transport source domain differs')
    inverse={y:x for x,y in bridge.mapping}
    newports=tuple(bridge.left_port if q.name==rightname else q for q in model.ports)
    newrows=tuple(tuple(inverse[v] if model.ports[k].name==rightname else v
                        for k,v in enumerate(row)) for row in model.rows)
    return Capsule(name or model.name+'-bridged',model.context,model.source_id,model.epoch,
                   model.basis,newports,newrows,parents=(model.name,'bridge:'+str(bridge.mapping)),
                   features=model.features|frozenset({'typed-translation'}))


def bridge_repair_demo()->dict:
    """Two independently named affine fields imply a relation absent in either.

    The source table aligns labels; it is NOT a preinstalled schema bridge.
    """
    source='declared-affine-source'
    a=binary_capsule('clock-parity','clock',source,'x','y',1)
    bd=('cold','warm')
    b=Capsule('thermal-state','thermal',source,0,'binary-v1',
              (Port('temperature_code',bd),Port('z',('0','1'))),
              (('cold','1'),('warm','0')),features=frozenset({'thermal','affine'}))
    table=PairedSourceTable(source,0,'binary-v1',Port('y',('0','1')),
                            Port('temperature_code',bd),
                            (('s0','0','cold'),('s1','1','warm')),True)
    candidates=invent_bijective_bridges(table)
    if len(candidates)!=1:raise AssertionError('Expected one uniquely sourced bridge')
    transported=transport_capsule(b,candidates[0])
    report=pullback(a,transported)
    if not report.realized or not verify_pullback(a,transported,report):
        raise AssertionError('False pullback')
    emergent=emergent_dependencies(a,transported,report.merged)
    return {'bridge':dict(candidates[0].mapping),
            'model_contexts':(a.context,b.context),
            'new_global_states':len(report.merged.rows),
            'new_invariants':emergent,
            'joint_relation_x_z':project(report.merged,('x','z')),
            'new_relation_not_present_in_either_parent':True,
            'source_completeness_is_declared_not_empirical':True,
            'external_carrier_authenticated':False}
