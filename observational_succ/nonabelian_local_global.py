"""Nonabelian local-to-global descent over finite permutation-group connections.

A chart carries a GROUP-valued section f with f(head)=U_edge * f(tail).
Gauge freedoms act on the RIGHT: f -> f*s_i. On an overlap vertex,
transition t_ij=f_j(v)^(-1)f_i(v), requiring s_j=t_ij*s_i. The entire
Cech MULTIGRAPH must have identity ordered cycle products. Pairwise and
triple identities at single points do not eliminate topology around loops.

The finite S_3 instance tests noncommuting holonomy invisible to the
abelian sign quotient. This is established nonabelian groupoid/torsor
gluing mathematics applied within SUCC, not discovered physical phase.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from hashlib import sha256
import json


class NonAbelianError(ValueError):
    pass


Perm=tuple[int,...]


def ident(n:int)->Perm:return tuple(range(n))


def validate(p:Perm,n:int)->None:
    if type(p) is not tuple or sorted(p)!=list(range(n)):
        raise NonAbelianError('Expected actual invertible finite permutation')


def mul(a:Perm,b:Perm)->Perm:
    if len(a)!=len(b):raise NonAbelianError('Group dimensions disagree')
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a:Perm)->Perm:
    n=len(a);validate(a,n);v=[0]*n
    for i,j in enumerate(a):v[j]=i
    return tuple(v)


def sign(a:Perm)->int:
    """Classical abelianization S3 -> C2; parity is not full holonomy."""
    inv=sum(1 for i in range(len(a)) for j in range(i+1,len(a)) if a[i]>a[j])
    return -1 if inv%2 else 1


@dataclass(frozen=True)
class GroupEdge:
    key:str
    tail:str
    head:str
    transport:Perm


@dataclass(frozen=True)
class GroupGraph:
    name:str
    vertices:tuple[str,...]
    edges:tuple[GroupEdge,...]
    degree:int

    def __post_init__(self):
        if not self.name or len(set(self.vertices))!=len(self.vertices) or not self.vertices:
            raise NonAbelianError('Invalid group-valued source')
        if type(self.degree) is not int or self.degree<1:
            raise NonAbelianError('Permutation carrier must have positive size')
        if len(set(e.key for e in self.edges))!=len(self.edges):
            raise NonAbelianError('Duplicate source edge')
        for e in self.edges:
            if e.tail not in self.vertices or e.head not in self.vertices or not e.key:
                raise NonAbelianError('False source edge')
            validate(e.transport,self.degree)

    @property
    def digest(self):
        return sha256(json.dumps((self.name,self.vertices,
               tuple((e.key,e.tail,e.head,e.transport) for e in self.edges),self.degree)).encode()).hexdigest()


@dataclass(frozen=True)
class GroupChart:
    name:str
    source_digest:str
    vertices:tuple[str,...]
    edge_ids:tuple[str,...]
    sections:tuple[tuple[str,Perm],...]


@dataclass(frozen=True)
class GroupOverlap:
    left:str
    right:str
    vertex:str
    transition:Perm


@dataclass(frozen=True)
class GroupVerdict:
    status:str
    source_digest:str
    charts:int
    vertex_sections:tuple[tuple[str,Perm],...]
    overlaps:tuple[GroupOverlap,...]
    obstruction_cycle:tuple[tuple[int,int],...]
    obstruction_product:Perm
    source_loop:tuple[tuple[str,int],...]
    source_holonomy:Perm


def _adj(g:GroupGraph,ids:tuple[str,...]):
    table={d.key:d for d in g.edges}
    if len(set(ids))!=len(ids) or any(k not in table for k in ids):
        raise NonAbelianError('Unknown or repeated local edge')
    adj={v:[] for v in g.vertices}
    for key in ids:
        d=table[key]
        adj[d.tail].append((d.head,d.transport))
        adj[d.head].append((d.tail,inverse(d.transport)))
    return adj


def construct_group_chart(g:GroupGraph,name:str,ids:tuple[str,...],
                          *,isolated:str|None=None)->GroupChart:
    table={d.key:d for d in g.edges}
    if ids:
        if any(k not in table for k in ids):raise NonAbelianError('Unknown edge')
        verts={v for k in ids for v in (table[k].tail,table[k].head)}
    elif isolated in g.vertices:
        verts={isolated}
    else:raise NonAbelianError('Empty chart')
    adj=_adj(g,ids)
    root=next(v for v in g.vertices if v in verts)
    phi={root:ident(g.degree)};q=deque([root])
    while q:
        u=q.popleft()
        for v,t in adj[u]:
            expected=mul(t,phi[u])
            if v not in phi:
                phi[v]=expected;q.append(v)
            elif phi[v]!=expected:
                raise NonAbelianError('Local group holonomy already obstructs section')
    if set(phi)!=verts:raise NonAbelianError('Disconnected group chart')
    return GroupChart(name,g.digest,tuple(v for v in g.vertices if v in phi),ids,
                      tuple((v,phi[v]) for v in g.vertices if v in phi))


def verify_group_chart(g:GroupGraph,c:GroupChart):
    if c.source_digest!=g.digest or not c.name or not c.vertices or len(set(c.vertices))!=len(c.vertices):
        raise NonAbelianError('Source or chart mismatch')
    table={d.key:d for d in g.edges}; phi=dict(c.sections)
    if len(phi)!=len(c.sections) or set(phi)!=set(c.vertices):
        raise NonAbelianError('Forged group section domain')
    for value in phi.values():validate(value,g.degree)
    adj=_adj(g,c.edge_ids)
    seen={c.vertices[0]};q=deque([c.vertices[0]])
    while q:
        for v,t in adj[q.popleft()]:
            if v not in seen:seen.add(v);q.append(v)
    if seen!=set(c.vertices):raise NonAbelianError('Disconnected chart statement')
    for key in c.edge_ids:
        d=table[key]
        if d.tail not in phi or d.head not in phi or phi[d.head]!=mul(d.transport,phi[d.tail]):
            raise NonAbelianError('False local group-arrow equation')


def _cycle_product(o:tuple[GroupOverlap,...],walk:tuple[tuple[int,int],...],n:int):
    if not walk:raise NonAbelianError('Empty nonabelian cycle')
    f=o[walk[0][0]]
    here=f.left if walk[0][1]==1 else f.right
    start=here;p=ident(n)
    for idx,sgn in walk:
        if idx<0 or idx>=len(o) or sgn not in (-1,1):raise NonAbelianError('Bad group cycle token')
        e=o[idx];src,dst=(e.left,e.right) if sgn==1 else (e.right,e.left)
        if here!=src:raise NonAbelianError('Noncomposable group loop')
        here=dst
        t=e.transition if sgn==1 else inverse(e.transition)
        p=mul(t,p)
    if here!=start:raise NonAbelianError('Non-closed group loop')
    return p



def _chart_group_path(g:GroupGraph,c:GroupChart,src:str,dst:str):
    if src==dst:return ()
    table={e.key:e for e in g.edges}
    adj={v:[] for v in g.vertices}
    for key in c.edge_ids:
        e=table[key]
        adj[e.tail].append((e.head,key,1))
        adj[e.head].append((e.tail,key,-1))
    parent={};seen={src};q=deque([src])
    while q and dst not in seen:
        u=q.popleft()
        for v,key,sgn in adj[u]:
            if v not in seen:
                seen.add(v);parent[v]=(u,key,sgn);q.append(v)
    if dst not in seen:raise NonAbelianError('No chart groupoid route')
    path=[];v=dst
    while v!=src:
        u,key,sgn=parent[v];path.append((key,sgn));v=u
    return tuple(reversed(path))


def _unfold_group_loop(g:GroupGraph,charts:dict[str,GroupChart],
                       overlaps:tuple[GroupOverlap,...],cycle:tuple[tuple[int,int],...]):
    path=[]
    for i,(idx,sign) in enumerate(cycle):
        edge=overlaps[idx]
        nextidx,nextsgn=cycle[(i+1)%len(cycle)]
        nxt=overlaps[nextidx]
        target=edge.right if sign==1 else edge.left
        expected=nxt.left if nextsgn==1 else nxt.right
        if target!=expected:raise NonAbelianError('Cocycle walk discontinuity')
        path.extend(_chart_group_path(g,charts[target],edge.vertex,nxt.vertex))
    return tuple(path)


def _walk_group_holonomy(g:GroupGraph,walk:tuple[tuple[str,int],...]):
    if not walk:raise NonAbelianError('Require nontrivial group source walk')
    table={e.key:e for e in g.edges}
    result=ident(g.degree);src=None;current=None
    for key,sgn in walk:
        if key not in table or sgn not in (-1,1):raise NonAbelianError('Bad source group edge')
        e=table[key]
        u,v,t=(e.tail,e.head,e.transport) if sgn==1 else (e.head,e.tail,inverse(e.transport))
        if current is not None and u!=current:raise NonAbelianError('Noncomposable source group walk')
        if src is None:src=u
        current=v
        result=mul(t,result)
    if current!=src:raise NonAbelianError('Non-closed source group walk')
    return result

def glue_group_charts(g:GroupGraph,charts:tuple[GroupChart,...])->GroupVerdict:
    if not charts or len({c.name for c in charts})!=len(charts):
        raise NonAbelianError('Distinct group charts required')
    table={e.key for e in g.edges}
    for c in charts:verify_group_chart(g,c)
    if set().union(*(set(c.vertices) for c in charts))!=set(g.vertices) or set().union(*(set(c.edge_ids) for c in charts))!=table:
        raise NonAbelianError('Source cover incomplete')
    pot={c.name:dict(c.sections) for c in charts}
    memberships={v:[] for v in g.vertices}
    for c in charts:
        for v in c.vertices:memberships[v].append(c.name)
    overlap=[]
    for v in g.vertices:
        names=memberships[v]
        for i in range(len(names)):
            for j in range(i+1,len(names)):
                a,b=names[i],names[j]
                overlap.append(GroupOverlap(a,b,v,mul(inverse(pot[b][v]),pot[a][v])))
    overlap=tuple(overlap)
    adj={c.name:[] for c in charts}
    for i,e in enumerate(overlap):
        adj[e.left].append((e.right,i,1,e.transition))
        adj[e.right].append((e.left,i,-1,inverse(e.transition)))
    shifts={};parent={}
    def route(x):
        back=[]
        while x in parent:
            p,j,s=parent[x];back.append((j,s));x=p
        return tuple(reversed(back))
    for root in adj:
        if root in shifts:continue
        shifts[root]=ident(g.degree);q=deque([root])
        while q:
            u=q.popleft()
            for v,idx,sgn,t in adj[u]:
                new=mul(t,shifts[u])
                if v not in shifts:
                    shifts[v]=new;parent[v]=(u,idx,sgn);q.append(v)
                elif shifts[v]!=new:
                    cycle=route(u)+((idx,sgn),)+tuple((j,-s) for j,s in reversed(route(v)))
                    h=_cycle_product(overlap,cycle,g.degree)
                    if h==ident(g.degree):raise AssertionError('Group-cycle mismatch')
                    source_walk=_unfold_group_loop(g,{c.name:c for c in charts},overlap,cycle)
                    source_holonomy=_walk_group_holonomy(g,source_walk)
                    if source_holonomy==ident(g.degree):
                        raise AssertionError('Cech obstruction did not yield source curvature')
                    return GroupVerdict('OBSTRUCTED',g.digest,len(charts),(),overlap,cycle,h,source_walk,source_holonomy)
    global_sec={}
    for c in charts:
        for v,gv in c.sections:
            value=mul(gv,shifts[c.name])
            if v in global_sec and global_sec[v]!=value:
                raise AssertionError('Group gluing failed unexpectedly')
            global_sec[v]=value
    for e in g.edges:
        if global_sec[e.head]!=mul(e.transport,global_sec[e.tail]):
            raise AssertionError('Wrong transported group arrow')
    return GroupVerdict('GLUED',g.digest,len(charts),
        tuple((v,global_sec[v]) for v in g.vertices),overlap,(),ident(g.degree),(),ident(g.degree))


def verify_group_verdict(g:GroupGraph,charts:tuple[GroupChart,...],verdict:GroupVerdict):
    if verdict.source_digest!=g.digest or verdict.charts!=len(charts):
        raise NonAbelianError('False group source receipt')
    for c in charts:verify_group_chart(g,c)
    if (set().union(*(set(c.vertices) for c in charts))!=set(g.vertices)
            or set().union(*(set(c.edge_ids) for c in charts))!={e.key for e in g.edges}):
        raise NonAbelianError('Global group source cover incomplete')
    rebuilt=[];pot={c.name:dict(c.sections) for c in charts}
    for v in g.vertices:
        names=[c.name for c in charts if v in c.vertices]
        for i in range(len(names)):
            for j in range(i+1,len(names)):
                a,b=names[i],names[j]
                rebuilt.append(GroupOverlap(a,b,v,mul(inverse(pot[b][v]),pot[a][v])))
    if tuple(rebuilt)!=verdict.overlaps:raise NonAbelianError('False overlap group transitions')
    if verdict.status=='OBSTRUCTED':
        if verdict.vertex_sections or verdict.obstruction_product==ident(g.degree):
            raise NonAbelianError('False nonidentity obstruction')
        if _cycle_product(verdict.overlaps,verdict.obstruction_cycle,g.degree)!=verdict.obstruction_product:
            raise NonAbelianError('Wrong ordered nonabelian holonomy')
        if _unfold_group_loop(g,{c.name:c for c in charts},verdict.overlaps,verdict.obstruction_cycle)!=verdict.source_loop:
            raise NonAbelianError('Wrong expanded groupoid source path')
        if (_walk_group_holonomy(g,verdict.source_loop)!=verdict.source_holonomy
                or verdict.source_holonomy==ident(g.degree)):
            raise NonAbelianError('False original-source nonabelian curvature')
    elif verdict.status=='GLUED':
        if verdict.obstruction_cycle or verdict.source_loop or verdict.source_holonomy!=ident(g.degree) or verdict.obstruction_product!=ident(g.degree):
            raise NonAbelianError('Contradictory group gluing result')
        phi=dict(verdict.vertex_sections)
        if len(phi)!=len(verdict.vertex_sections) or set(phi)!=set(g.vertices):
            raise NonAbelianError('Incomplete global group section')
        for e in g.edges:
            if phi[e.head]!=mul(e.transport,phi[e.tail]):
                raise NonAbelianError('Wrong global group transport equation')
        for c in charts:
            gauge=mul(inverse(pot[c.name][c.vertices[0]]),phi[c.vertices[0]])
            if any(phi[v]!=mul(pot[c.name][v],gauge) for v in c.vertices):
                raise NonAbelianError('Global group section not chartwise descended')
    else:raise NonAbelianError('Invalid status')


def s3_commutator_square()->tuple[GroupGraph,tuple[GroupChart,...]]:
    a=(1,0,2);b=(0,2,1)
    # Around the square: a,b,a^-1,b^-1. Individual sign parity
    # cancels, but the ordered commutator remains nonidentity in S3.
    edges=(GroupEdge('east','v0','v1',a),GroupEdge('north','v1','v2',b),
           GroupEdge('west','v2','v3',inverse(a)),GroupEdge('south','v3','v0',inverse(b)))
    graph=GroupGraph('S3-nonabelian-commutator',('v0','v1','v2','v3'),edges,3)
    charts=tuple(construct_group_chart(graph,'chart-'+d.key,(d.key,)) for d in edges)
    return graph,charts
