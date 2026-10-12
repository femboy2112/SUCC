"""Source-faithful local-to-global construction via overlap 1-cocycles.

A finite voltage graph G with integral displacements is covered by CONNECTED
edge charts. Each agent constructs a chart potential from its own chart edges;
no globally fitted potential is supplied. The receiver can glue those charts
iff every cycle of the (MULTI-)overlap graph has zero signed transition sum.

Overlap multiplicity matters: a pair of disconnected intersections may already
carry a nontrivial two-edge Cech cycle. A failed gluing returns an independently
verifiable closed walk in the ORIGINAL source graph, not just a narrative.

This is elementary graph cohomology/voltage-graph theory, not a new general
sheaf theorem, source authentication, physically instantaneous computation,
or the uniform arithmetic existence theorem for Gaussian primes.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Hashable, Iterable

Vertex = Hashable
Vector = tuple[int, ...]


class DescentError(ValueError):
    """Invalid source, patch, receipt, or attempted global proof."""


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def neg(a: Vector) -> Vector:
    return tuple(-x for x in a)


def sub(a: Vector, b: Vector) -> Vector:
    return add(a, neg(b))


@dataclass(frozen=True)
class Dart:
    key: str
    tail: Vertex
    head: Vertex
    displacement: Vector


@dataclass(frozen=True)
class VoltageSource:
    source_id: str
    vertices: tuple[Vertex, ...]
    darts: tuple[Dart, ...]
    dimension: int
    period: int | None = None

    def __post_init__(self):
        if not self.source_id or type(self.dimension) is not int or self.dimension < 1:
            raise DescentError('Declare an exact source identity and positive dimension')
        if (not self.vertices or len(set(self.vertices)) != len(self.vertices)
                or len(set(d.key for d in self.darts)) != len(self.darts)):
            raise DescentError('Distinct, nonempty source vertices and dart identities required')
        if self.period is not None and (type(self.period) is not int or self.period < 1):
            raise DescentError('Invalid periodic source')
        vs = set(self.vertices)
        for d in self.darts:
            if (not isinstance(d.key, str) or not d.key or d.tail not in vs or d.head not in vs
                    or type(d.displacement) is not tuple or len(d.displacement) != self.dimension
                    or any(type(k) is not int for k in d.displacement)):
                raise DescentError('Malformed source dart / displacement')
        if self.period is not None:
            if any(not isinstance(v, tuple) or len(v) != self.dimension
                   or any(type(x) is not int or not 0 <= x < self.period for x in v)
                   for v in self.vertices):
                raise DescentError('Periodic vertices must be canonical integer addresses')
            for d in self.darts:
                if any((d.tail[k] + d.displacement[k] - d.head[k]) % self.period
                       for k in range(self.dimension)):
                    raise DescentError('Source displacement does not commute with reduction')

    @property
    def digest(self) -> str:
        data = (self.source_id, self.dimension, self.period,
                tuple(repr(v) for v in self.vertices),
                tuple((d.key, repr(d.tail), repr(d.head), d.displacement) for d in self.darts))
        return sha256(json.dumps(data, separators=(',', ':')).encode()).hexdigest()

    def index(self) -> dict[str, Dart]:
        return {d.key: d for d in self.darts}


@dataclass(frozen=True)
class Chart:
    name: str
    source_digest: str
    vertices: tuple[Vertex, ...]
    dart_ids: tuple[str, ...]
    potentials: tuple[tuple[Vertex, Vector], ...]


@dataclass(frozen=True)
class Overlap:
    left: str
    right: str
    vertex: Vertex
    delta: Vector   # shift[right] - shift[left] = delta


@dataclass(frozen=True)
class Obstruction:
    cycle: tuple[tuple[int, int], ...]    # (overlap index, signed direction)
    displacement: Vector
    # One independent, expanded closed walk on the original source graph.
    lifted_walk: tuple[tuple[str, int], ...]


@dataclass(frozen=True)
class DescentResult:
    source_digest: str
    status: str
    global_potential: tuple[tuple[Vertex, Vector], ...]
    chart_shifts: tuple[tuple[str, Vector], ...]
    overlaps: tuple[Overlap, ...]
    obstruction: Obstruction | None
    chart_count: int
    checked_darts: int


def _adjacency(graph: VoltageSource, dart_ids: Iterable[str]) -> dict[Vertex, list[tuple[Vertex, str, int, Vector]]]:
    adj = {v: [] for v in graph.vertices}
    table = graph.index()
    for key in dart_ids:
        if key not in table:
            raise DescentError('Patch contains unknown source edge')
        d = table[key]
        adj[d.tail].append((d.head, key, 1, d.displacement))
        adj[d.head].append((d.tail, key, -1, neg(d.displacement)))
    return adj


def construct_chart(graph: VoltageSource, name: str, dart_ids: Iterable[str],
                    *, lone_vertex: Vertex | None = None) -> Chart:
    """Independent local construction. Failure of a local cycle is honest.

    Never fits to a global potential; only this chart's declared source darts.
    Undirected incidence is the groupoid of formal reversible proof paths.
    For physically directed actions inverse paths require an additional license.
    """
    ids = tuple(dart_ids)
    table = graph.index()
    if len(set(ids)) != len(ids):
        raise DescentError('Duplicate local dart')
    if any(key not in table for key in ids):
        raise DescentError('Unknown local source edge')
    if ids:
        vs = {v for key in ids for v in (table[key].tail, table[key].head)}
    elif lone_vertex in graph.vertices:
        vs = {lone_vertex}
    else:
        raise DescentError('Nonempty connected edge chart or one isolated source vertex required')
    adj = _adjacency(graph, ids)
    root = next(v for v in graph.vertices if v in vs)
    phi = {root: (0,) * graph.dimension}
    q = deque([root])
    while q:
        u = q.popleft()
        for v, key, sign, weight in adj[u]:
            expected = add(phi[u], weight)
            if v not in phi:
                phi[v] = expected
                q.append(v)
            elif phi[v] != expected:
                raise DescentError(f'Local chart {name}: nonzero voltage cycle at {key}')
    if set(phi) != vs:
        raise DescentError('The patch is not connected; split it into connected charts')
    return Chart(name, graph.digest, tuple(v for v in graph.vertices if v in vs), ids,
                 tuple((v, phi[v]) for v in graph.vertices if v in vs))


def verify_chart(graph: VoltageSource, chart: Chart) -> None:
    if not chart.name or chart.source_digest != graph.digest:
        raise DescentError('Stale or false source fingerprint')
    if (len(set(chart.vertices)) != len(chart.vertices)
            or len(set(chart.dart_ids)) != len(chart.dart_ids)
            or len(set(v for v, _ in chart.potentials)) != len(chart.potentials)):
        raise DescentError('Duplicate chart objects')
    phi = dict(chart.potentials)
    if set(phi) != set(chart.vertices) or not set(phi).issubset(graph.vertices):
        raise DescentError('Chart values do not exactly cover its declared vertices')
    if any(type(p) is not tuple or len(p) != graph.dimension
           or any(type(a) is not int for a in p) for p in phi.values()):
        raise DescentError('Potentials must be exact integral vectors')
    table = graph.index()
    if not set(chart.dart_ids).issubset(table):
        raise DescentError('Unknown chart source edge')
    adj = _adjacency(graph, chart.dart_ids)
    for key in chart.dart_ids:
        d = table[key]
        if d.tail not in phi or d.head not in phi or sub(phi[d.head], phi[d.tail]) != d.displacement:
            raise DescentError('Local edge equation invalid or endpoint missing')
    start = chart.vertices[0]
    seen = {start}
    queue = deque([start])
    while queue:
        for v, *_ in adj[queue.popleft()]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    if seen != set(chart.vertices):
        raise DescentError('Connected chart requirement violated')


def _chart_route(graph: VoltageSource, chart: Chart, start: Vertex,
                 end: Vertex) -> tuple[tuple[str, int], ...]:
    if start == end:
        return ()
    a = _adjacency(graph, chart.dart_ids)
    parent: dict[Vertex, tuple[Vertex, str, int]] = {}
    queue = deque([start])
    seen = {start}
    while queue and end not in seen:
        u = queue.popleft()
        for v, key, sign, _ in a[u]:
            if v not in seen:
                seen.add(v)
                parent[v] = (u, key, sign)
                queue.append(v)
    if end not in seen:
        raise DescentError('Chart has no connecting path')
    route = []
    x = end
    while x != start:
        u, key, sign = parent[x]
        route.append((key, sign))
        x = u
    return tuple(reversed(route))


def _unfold_obstruction(graph: VoltageSource, charts: dict[str, Chart],
                        overlaps: tuple[Overlap, ...], cycle: tuple[tuple[int,int], ...]) -> tuple[tuple[str,int], ...]:
    walk = []
    for n, (idx, sign) in enumerate(cycle):
        curr = overlaps[idx]
        next_idx, next_sign = cycle[(n+1) % len(cycle)]
        upcoming = overlaps[next_idx]
        destination_chart = curr.right if sign == 1 else curr.left
        from_next = upcoming.left if next_sign == 1 else upcoming.right
        if destination_chart != from_next:
            raise DescentError('Overlap cycle is not composable')
        walk.extend(_chart_route(graph, charts[destination_chart], curr.vertex, upcoming.vertex))
    return tuple(walk)


def _cycle_value(overlaps: tuple[Overlap, ...], cycle: tuple[tuple[int,int], ...],
                 dimension: int) -> Vector:
    result = (0,) * dimension
    if not cycle:
        raise DescentError('Empty cycle witness')
    first = overlaps[cycle[0][0]]
    start = first.left if cycle[0][1] == 1 else first.right
    current = start
    for idx, sign in cycle:
        if type(idx) is not int or not 0 <= idx < len(overlaps) or sign not in (-1,1):
            raise DescentError('Malformed overlap loop')
        link = overlaps[idx]
        src, dst = (link.left, link.right) if sign == 1 else (link.right, link.left)
        if src != current:
            raise DescentError('Overlap loop is not causally composable')
        current = dst
        result = add(result, link.delta if sign == 1 else neg(link.delta))
    if current != start:
        raise DescentError('Overlap loop is not closed')
    return result


def verify_closed_walk(graph: VoltageSource, walk: tuple[tuple[str,int], ...],
                       expected: Vector) -> None:
    if not walk or expected == (0,) * graph.dimension:
        raise DescentError('Nontrivial closed source walk required')
    table = graph.index()
    position = None
    first = None
    total = (0,) * graph.dimension
    for key, sign in walk:
        if key not in table or sign not in (-1,1):
            raise DescentError('Invalid original-source walk edge')
        d = table[key]
        u, v, delta = (d.tail, d.head, d.displacement) if sign == 1 else (d.head, d.tail, neg(d.displacement))
        if position is not None and u != position:
            raise DescentError('Discontinuous original-source walk')
        if first is None:
            first = u
        total = add(total, delta)
        position = v
    if position != first or total != expected:
        raise DescentError('Invalid global obstruction displacement')


def _candidate_overlaps(graph: VoltageSource, charts: tuple[Chart,...]) -> tuple[Overlap,...]:
    # Every common vertex is retained, not only one representative per pair.
    # This detects disconnected overlaps and parallel Čech arrows.
    members: dict[Vertex, list[str]] = {v: [] for v in graph.vertices}
    pots = {c.name: dict(c.potentials) for c in charts}
    for c in charts:
        for v in c.vertices:
            members[v].append(c.name)
    res = []
    for v in graph.vertices:
        entries = members[v]
        for i in range(len(entries)):
            for j in range(i+1,len(entries)):
                left, right = entries[i], entries[j]
                res.append(Overlap(left,right,v,sub(pots[left][v],pots[right][v])))
    return tuple(res)


def assemble_charts(graph: VoltageSource, charts: Iterable[Chart], *,
                    max_overlaps: int=200_000) -> DescentResult:
    charts = tuple(charts)
    if not charts or len(set(c.name for c in charts)) != len(charts):
        raise DescentError('At least one distinctly named chart is required')
    for c in charts:
        verify_chart(graph,c)
    if set().union(*(set(c.vertices) for c in charts)) != set(graph.vertices):
        raise DescentError('Source vertex coverage is incomplete')
    if set().union(*(set(c.dart_ids) for c in charts)) != set(graph.index()):
        raise DescentError('Source dart coverage is incomplete')
    overlaps = _candidate_overlaps(graph,charts)
    if len(overlaps) > max_overlaps:
        raise DescentError('Declared overlap resource budget exhausted')
    chart_map = {c.name: c for c in charts}
    adj: dict[str, list[tuple[str,int,int,Vector]]] = {c.name: [] for c in charts}
    for i, edge in enumerate(overlaps):
        adj[edge.left].append((edge.right,i,1,edge.delta))
        adj[edge.right].append((edge.left,i,-1,neg(edge.delta)))
    shifts: dict[str,Vector] = {}
    parent: dict[str,tuple[str,int,int]] = {}
    zero=(0,)*graph.dimension

    def root_route(c: str) -> tuple[tuple[int,int],...]:
        back=[]
        while c in parent:
            prv,idx,s=parent[c]
            back.append((idx,s))
            c=prv
        return tuple(reversed(back))

    for start in adj:
        if start in shifts:
            continue
        shifts[start]=zero
        queue=deque([start])
        while queue:
            u=queue.popleft()
            for v,i,sign,delta in adj[u]:
                desired=add(shifts[u],delta)
                if v not in shifts:
                    shifts[v]=desired
                    parent[v]=(u,i,sign)
                    queue.append(v)
                elif shifts[v] != desired:
                    cycle=root_route(u)+((i,sign),)+tuple((idx,-s) for idx,s in reversed(root_route(v)))
                    hol=_cycle_value(overlaps,cycle,graph.dimension)
                    if hol == zero:
                        raise AssertionError('Incorrect internal overlap cycle')
                    expanded=_unfold_obstruction(graph,chart_map,overlaps,cycle)
                    verify_closed_walk(graph,expanded,hol)
                    obstruction=Obstruction(cycle,hol,expanded)
                    return DescentResult(graph.digest,'OBSTRUCTED',(),(),overlaps,obstruction,
                                         len(charts),len(graph.darts))
    total: dict[Vertex,Vector] = {}
    for c in charts:
        for v,p in c.potentials:
            lifted=add(p,shifts[c.name])
            if v in total and total[v] != lifted:
                raise AssertionError('Overlap constraints did not glue')
            total[v]=lifted
    if graph.period is not None:
        for component in _source_components(graph):
            root=next(v for v in graph.vertices if v in component)
            # All differences are multiples of period; gauge-fix one vertex/component.
            # Gauge-fix using actual integer displacement, not its residue.
            true_shift=tuple(root[i]-total[root][i] for i in range(graph.dimension))
            for v in component:
                total[v]=add(total[v],true_shift)
                if any((total[v][i]-v[i])%graph.period for i in range(graph.dimension)):
                    raise AssertionError('Source address reduction broken by valid voltage')
        # Report chart shifts in their original unanchored affine basis.
        # Globally gauge-fixed potentials are verified independently below.
    _verify_global(graph,total)
    return DescentResult(graph.digest,'GLUED',tuple((v,total[v]) for v in graph.vertices),
                         tuple((c.name,shifts[c.name]) for c in charts),overlaps,None,
                         len(charts),len(graph.darts))


def _source_components(graph: VoltageSource) -> tuple[tuple[Vertex,...], ...]:
    adj=_adjacency(graph,(d.key for d in graph.darts))
    seen=set();parts=[]
    for root in graph.vertices:
        if root in seen:continue
        seen.add(root);q=deque([root]);segment=[]
        while q:
            u=q.popleft();segment.append(u)
            for v,*_ in adj[u]:
                if v not in seen:seen.add(v);q.append(v)
        parts.append(tuple(segment))
    return tuple(parts)


def _verify_global(graph: VoltageSource, potentials: dict[Vertex,Vector]) -> None:
    if set(potentials)!=set(graph.vertices):
        raise DescentError('Global potential has incomplete vertex cover')
    for d in graph.darts:
        if sub(potentials[d.head],potentials[d.tail])!=d.displacement:
            raise DescentError('Global potential does not integrate every SUCC arrow')
    if graph.period is not None:
        for v,g in potentials.items():
            if any((g[k]-v[k])%graph.period for k in range(graph.dimension)):
                raise DescentError('Global potential is not an address lift')


def verify_result(graph: VoltageSource, charts: tuple[Chart,...],result: DescentResult) -> None:
    """Independent certificate checker; no call to assembly and no trusting status."""
    if result.source_digest!=graph.digest or result.chart_count!=len(charts) or result.checked_darts!=len(graph.darts):
        raise DescentError('False source/census receipt')
    if len(set(c.name for c in charts))!=len(charts):
        raise DescentError('Repeated chart ID')
    for c in charts:verify_chart(graph,c)
    if set().union(*(set(c.vertices) for c in charts)) != set(graph.vertices) or set().union(*(set(c.dart_ids) for c in charts))!=set(graph.index()):
        raise DescentError('Missing local source coverage')
    overlaps=_candidate_overlaps(graph,charts)
    if overlaps!=result.overlaps:raise DescentError('False overlap transition ledger')
    if result.status=='GLUED':
        if result.obstruction is not None:raise DescentError('Contradictory gluing status')
        phi=dict(result.global_potential)
        if len(phi)!=len(result.global_potential):raise DescentError('Duplicated global vertex')
        _verify_global(graph,phi)
        shifts=dict(result.chart_shifts)
        if set(shifts)!={c.name for c in charts}:raise DescentError('Wrong gauge dictionary')
        # A periodic normalization adds one constant per SOURCE component and
        # does not change overlap compatibility, so check differences on each chart.
        for c in charts:
            vals=dict(c.potentials)
            if len(c.vertices)==0:raise DescentError('Empty chart')
            gauge=sub(phi[c.vertices[0]],vals[c.vertices[0]])
            if any(sub(phi[v],vals[v])!=gauge for v in c.vertices):
                raise DescentError('Global potential not obtained by patchwise gauge')
    elif result.status=='OBSTRUCTED':
        if result.global_potential or result.chart_shifts or result.obstruction is None:
            raise DescentError('Malformed no-gluing witness')
        ob=result.obstruction
        if _cycle_value(overlaps,ob.cycle,graph.dimension)!=ob.displacement or ob.displacement==(0,)*graph.dimension:
            raise DescentError('False Čech cycle class')
        if _unfold_obstruction(graph,{c.name:c for c in charts},overlaps,ob.cycle)!=ob.lifted_walk:
            raise DescentError('Wrong source expansion of overlap cycle')
        verify_closed_walk(graph,ob.lifted_walk,ob.displacement)
    else:
        raise DescentError('Unknown verdict')


def spanning_chart_cover(graph: VoltageSource) -> tuple[tuple[str,tuple[str,...],Vertex|None],...]:
    """Two independent connected charts per nontrivial source component.

    Both own a spanning tree; the non-tree darts are partitioned. The tree
    anchors comparisons, while local candidates are independently built.
    Covers every dart. This is a certificate DESIGN, not discovery of confinement.
    """
    comps=_source_components(graph)
    spec=[]
    for i,verts in enumerate(comps):
        allowed=set(verts)
        ids=[d.key for d in graph.darts if d.tail in allowed and d.head in allowed]
        if not ids:
            spec.append((f'island-{i}',(),verts[0]));continue
        adj=_adjacency(graph,ids)
        seen={verts[0]};q=deque([verts[0]]);tree=set()
        while q:
            u=q.popleft()
            for v,key,_,_ in adj[u]:
                if v not in seen:
                    seen.add(v);q.append(v);tree.add(key)
        # A pair of opposite darts may duplicate the same undirected tree
        # but both must be covered somewhere.
        remaining=[key for key in ids if key not in tree]
        lane_index={key:idx%2 for idx,key in enumerate(remaining)}
        for j in (0,1):
            selected=tuple(key for key in ids if key in tree or lane_index.get(key)==j)
            spec.append((f'component-{i}-lane-{j}',selected,None))
    return tuple(spec)


def edge_chart_cover(graph: VoltageSource) -> tuple[tuple[str,tuple[str,...],Vertex|None],...]:
    """A universally local cover: one edge per patch, islands separate.

    Its local charts are always solvable unless a nonzero-voltage self-loop
    already forbids a local potential. The Čech obstruction therefore exposes
    any *global* escape instead of hiding it inside a large patch.
    """
    spec=[(f'edge-{i}',(d.key,),None) for i,d in enumerate(graph.darts)]
    incident={v for d in graph.darts for v in (d.tail,d.head)}
    spec.extend((f'island-{i}',(),v) for i,v in enumerate(graph.vertices) if v not in incident)
    return tuple(spec)
