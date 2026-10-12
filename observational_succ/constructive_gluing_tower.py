"""Independent chart construction, A/B diagonal relays, global proof at E.

Unlike voltage_tower.py this module NEVER constructs or stores a global
candidate potential upstream. Each A/B agent builds a local connected chart
from its own edge collection. E checks provenance, overlap coherence, and
full source coverage, then constructs the global potential, or a falsifying
original-source walk. One E macro step does not mean zero physical work.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from collections import deque
import json

from .diagonal_tower import ice_climber_tower, TowerError
from .gaussian_holonomy import GaussianSieve, _steps
from .local_global_descent import (
    VoltageSource, Dart, Chart, DescentError, DescentResult, construct_chart,
    verify_chart, assemble_charts, verify_result, spanning_chart_cover,
    edge_chart_cover, _source_components,
)


class GluingTowerError(ValueError):
    """Unknown origin, incorrect local math, incomplete evidence or relay."""


@dataclass(frozen=True)
class ChartReceipt:
    chart_id: str
    origin: str
    source_digest: str
    basis: str
    parents: tuple[str, ...]
    chart: Chart


@dataclass(frozen=True)
class ECertificate:
    status: str
    source_digest: str
    charts: int
    checked_vertices: int
    checked_darts: int
    overlap_conditions: int
    largest_component: int | None
    obstruction: tuple[int, ...] | None
    expanded_obstruction_steps: int
    source_verified_at_E: bool
    total_hops: int
    transmitted_references: int
    epistemic_macros_at_E: int


def gaussian_voltage_source(sieve: GaussianSieve, squared_step: int = 1,
                            *, max_cells: int = 100_000) -> VoltageSource:
    """Build authentic two-conjugate Gaussian source without using any potential.

    Max_cells is an enumeration budget, not an existence obstruction.
    """
    vertices=sieve.allowed_residues(max_cells=max_cells)
    lookup=set(vertices)
    steps=_steps(squared_step)
    q=sieve.period
    darts=[]
    for vi,v in enumerate(vertices):
        for si,d in enumerate(steps):
            w=((v[0]+d[0])%q,(v[1]+d[1])%q)
            if w in lookup:
                darts.append(Dart(f'dart:{vi}:{si}',v,w,d))
    return VoltageSource(f'GaussianSieve:{sieve.factors}:k{squared_step}',
                         vertices,tuple(darts),2,q)


class IndependentPatchTower:
    """One checkable finite model of a diagonal multi-observer proof climb.

    Declared source and authenticated event assumptions remain separated:
    source_digest is a consistency commitment, NOT cryptographic origin.
    """
    def __init__(self,graph: VoltageSource,*,levels: int=3,
                 patches: tuple[tuple[str,tuple[str,...],object|None],...]|None=None):
        self.graph=graph
        self.network=ice_climber_tower(levels)[1]
        self.levels=levels
        if patches is None:
            patches=spanning_chart_cover(graph)
        self.specs={name:(tuple(edges),lone) for name,edges,lone in patches}
        if not self.specs or len(self.specs)!=len(patches):
            raise GluingTowerError('Distinct, nonempty local chart assignments required')
        self.climbers=tuple(f'{lane}{level}' for level in range(levels) for lane in ('A','B'))
        self.assignment={n:[] for n in self.climbers}
        for i,name in enumerate(self.specs):
            self.assignment[self.climbers[i%len(self.climbers)]].append(name)
        self.known={node.name:set() for node in self.network.nodes}
        self.issued:dict[str,ChartReceipt]={}
        self.actions:list[tuple[str,str,str,tuple[str,...]]]=[]
        self.macros=0
        self.basis='local-integral-voltage-v1'
        self.result:DescentResult|None=None

    def _parents(self,origin: str) -> tuple[str,...]:
        level=int(origin[1:])
        if level==0:return ()
        return tuple(name for sender in (f'A{level-1}',f'B{level-1}')
                     for name in self.assignment[sender])

    def construct_at(self,origin: str,name: str) -> ChartReceipt:
        if origin not in self.climbers or name not in self.assignment[origin]:
            raise GluingTowerError('Chart not assigned to this physical/mathematical observer')
        if name in self.issued:
            raise GluingTowerError('Cannot double-issue one origin receipt')
        parents=self._parents(origin)
        if not set(parents).issubset(self.known[origin]):
            raise GluingTowerError('Higher climber lacks lawful lower-floor proof support')
        ids,lone=self.specs[name]
        try:chart=construct_chart(self.graph,name,ids,lone_vertex=lone)
        except DescentError as exc:raise GluingTowerError('Local chart could not be constructed: '+str(exc)) from exc
        receipt=ChartReceipt(name,origin,self.graph.digest,self.basis,parents,chart)
        self.issued[name]=receipt
        self.known[origin].add(name)
        self.actions.append(('issue',origin,origin,(name,)))
        return receipt

    def relay(self,sender: str,receiver: str,names: tuple[str,...]|None=None)->tuple[str,...]:
        try:self.network.link(sender,receiver)
        except TowerError as exc:raise GluingTowerError('Forbidden non-causal or non-diagonal hop') from exc
        if names is None:
            names=tuple(sorted(self.known[sender]-self.known[receiver]))
        if (not names or len(set(names))!=len(names)
                or not set(names).issubset(self.known[sender])
                or any(item not in self.issued for item in names)):
            raise GluingTowerError('Forged/duplicate/empty source receipt relay')
        self.known[receiver].update(names)
        self.actions.append(('relay',sender,receiver,tuple(names)))
        return tuple(names)

    def _replay(self)->None:
        replay={n.name:set() for n in self.network.nodes}
        issued=set()
        for op,sender,receiver,items in self.actions:
            if not items or len(set(items))!=len(items):
                raise GluingTowerError('Invalid action payload')
            if op=='issue':
                if sender!=receiver or len(items)!=1 or items[0] not in self.assignment[sender]:
                    raise GluingTowerError('False local source origin')
                name=items[0]
                if name in issued or not set(self._parents(sender)).issubset(replay[sender]):
                    raise GluingTowerError('No lawful causal history for a local chart')
                issued.add(name);replay[sender].add(name)
            elif op=='relay':
                try:self.network.link(sender,receiver)
                except TowerError as exc:raise GluingTowerError('False network edge') from exc
                if not set(items).issubset(replay[sender]) or not set(items).issubset(issued):
                    raise GluingTowerError('Evidence transported before it existed')
                replay[receiver].update(items)
            else:
                raise GluingTowerError('Unknown event type')
        if issued!=set(self.issued) or replay!=self.known:
            raise GluingTowerError('Causal replay and displayed evidence disagree')

    def proof_at_E(self) -> ECertificate:
        if self.macros:
            raise GluingTowerError('E has already performed its one epistemic commit')
        self._replay()
        if self.known['E']!=set(self.specs):
            raise GluingTowerError('E does not possess complete lawful proof support')
        charts=[]
        for name in self.specs:
            record=self.issued.get(name)
            origin=next(w for w in self.assignment if name in self.assignment[w])
            if (record is None or record.origin!=origin or record.chart_id!=name
                    or record.source_digest!=self.graph.digest or record.basis!=self.basis
                    or record.parents!=self._parents(origin)
                    or record.chart.dart_ids!=self.specs[name][0]):
                raise GluingTowerError('Forged chart/source/origin/parent claim')
            try:verify_chart(self.graph,record.chart)
            except DescentError as exc:raise GluingTowerError('Incorrect local proof') from exc
            charts.append(record.chart)
        try:
            result=assemble_charts(self.graph,tuple(charts))
            verify_result(self.graph,tuple(charts),result)
        except DescentError as exc:raise GluingTowerError('Global gluing cannot be certified') from exc
        self.result=result
        self.macros=1
        sizes=[len(c) for c in _source_components(self.graph)]
        bound=max(sizes) if result.status=='GLUED' else None
        return ECertificate(result.status,self.graph.digest,len(charts),len(self.graph.vertices),
            len(self.graph.darts),len(result.overlaps),bound,
            result.obstruction.displacement if result.obstruction else None,
            len(result.obstruction.lifted_walk) if result.obstruction else 0,
            True,len([x for x in self.actions if x[0]=='relay']),
            sum(len(x[3]) for x in self.actions if x[0]=='relay'),self.macros)


def run_diagonal_tower(graph:VoltageSource,*,levels:int=3,
                       patches:tuple|None=None,complete:bool=True) -> IndependentPatchTower:
    tower=IndependentPatchTower(graph,levels=levels,patches=patches)
    for level in range(levels):
        if level:
            for sender in (f'A{level-1}',f'B{level-1}'):
                for receiver in (f'A{level}',f'B{level}'):
                    if tower.known[sender]-tower.known[receiver]:
                        tower.relay(sender,receiver)
        for lane in ('A','B'):
            who=f'{lane}{level}'
            for chart_id in tower.assignment[who]:
                tower.construct_at(who,chart_id)
    if complete:
        for level in range(levels-1,0,-1):
            for sender,receiver in ((f'A{level}',f'B{level-1}'),
                                    (f'B{level}',f'A{level-1}')):
                if tower.known[sender]-tower.known[receiver]:
                    tower.relay(sender,receiver)
        for sender in ('A0','B0'):
            if tower.known[sender]-tower.known['E']:
                tower.relay(sender,'E')
    return tower
