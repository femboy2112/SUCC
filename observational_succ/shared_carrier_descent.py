"""Finite shared-carrier epistemic descent and exact boundary harmonic reduction.

Two distinct structures:
(1) Observations of one declared source C: joint-fiber/claim factorization;
    no horizontal communication can separate an observationally aliased pair.
(2) A finite weighted graph as a declared physical/mathematical carrier:
    if its interior satisfies the discrete harmonic law, full Dirichlet
    boundary data uniquely determine the bulk and a boundary-only energy.

Neither a common source identifier nor numerical coincidence authenticates an
external physical carrier. Mathematical results are elementary/classical.
Everything claimed exact is computed with fractions.Fraction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from typing import Hashable, Mapping, Sequence


class CarrierDescentError(ValueError):
    """Unlicensed source, erroneous table, incompatible evidence or invalid BVP."""


def exact(v: object) -> F:
    if type(v) is int or type(v) is F:
        return F(v)
    raise CarrierDescentError("Use exact integers and rational Fractions, not floats")


@dataclass(frozen=True)
class Evidence:
    source_id: str
    source_version: int
    basis_id: str
    probe: str
    outcome: Hashable
    observer: str


@dataclass(frozen=True)
class SharedSource:
    """All declared observations refer to one exact finite source universe.

    Outputs are ordered alongside 'states'. No assumed independence or
    unobserved physical state is passed to the recipient's decoder.
    """
    source_id: str
    version: int
    basis_id: str
    states: tuple[Hashable, ...]
    observations: Mapping[str, tuple[Hashable, ...]]
    claims: Mapping[str, tuple[Hashable, ...]]

    def __post_init__(self) -> None:
        if (not self.source_id or not self.basis_id or type(self.version) is not int
                or self.version < 0):
            raise CarrierDescentError("Source, version and basis required")
        if not self.states or len(set(self.states)) != len(self.states):
            raise CarrierDescentError("Source states must be nonempty/distinct/hashable")
        if not self.observations or not self.claims:
            raise CarrierDescentError("Declare at least one probe and target claim")
        for label, table in tuple(self.observations.items()) + tuple(self.claims.items()):
            if not isinstance(label, str) or not label or len(table) != len(self.states):
                raise CarrierDescentError("Named source tables must cover every source state")
            for value in table:
                hash(value)

    def report(self, probe: str, source: Hashable, observer: str) -> Evidence:
        """Simulator-only preparation of an honest report from named source.

        No algorithm receiving a report can infer that it was prepared honestly.
        """
        if probe not in self.observations or not observer or source not in self.states:
            raise CarrierDescentError("Unknown source, probe or observer")
        i = self.states.index(source)
        return Evidence(self.source_id, self.version, self.basis_id,
                        probe, self.observations[probe][i], observer)

    def fiber(self, reports: Sequence[Evidence]) -> tuple[Hashable, ...]:
        """Exact intersection of source constraints; may be empty (refutation)."""
        relevant = tuple(reports)
        for e in relevant:
            if not isinstance(e, Evidence) or (e.source_id,e.source_version,e.basis_id) != (
                    self.source_id,self.version,self.basis_id):
                raise CarrierDescentError("Forged/stale source or wrong basis")
            if e.probe not in self.observations or not e.observer:
                raise CarrierDescentError("Undeclared probe or owner")
        result = []
        for i, s in enumerate(self.states):
            if all(self.observations[e.probe][i] == e.outcome for e in relevant):
                result.append(s)
        return tuple(result)

    def conclude(self, reports: Sequence[Evidence], claim: str) -> dict:
        """Prove one original-source target iff constant on nonempty fiber."""
        if claim not in self.claims:
            raise CarrierDescentError("Original-source claim not declared")
        candidate_sources = self.fiber(reports)
        if not candidate_sources:
            return {"status":"INCONSISTENT_SOURCE", "fiber":(), "value":None}
        values = {self.claims[claim][self.states.index(s)] for s in candidate_sources}
        if len(values) == 1:
            return {"status":"PROVED", "fiber":candidate_sources, "value":next(iter(values))}
        return {"status":"UNRESOLVED", "fiber":candidate_sources, "value":None}

    def factorization(self, probes: Sequence[str], claim: str) -> dict:
        """Characterize existence of T=g o O on all admissible source states."""
        probes = tuple(probes)
        if len(set(probes)) != len(probes) or any(p not in self.observations for p in probes):
            raise CarrierDescentError("Unknown or duplicated probes")
        if claim not in self.claims:
            raise CarrierDescentError("Unknown original-source claim")
        obs_values = {}
        for i, source in enumerate(self.states):
            signature = tuple(self.observations[p][i] for p in probes)
            value = self.claims[claim][i]
            if signature in obs_values and obs_values[signature][1] != value:
                other_source, old_value = obs_values[signature]
                return {"factors":False,"counterexample":(other_source,source),
                        "shared_transcript":signature,
                        "conflicting_claims":(old_value,value)}
            obs_values[signature] = (source,value)
        return {"factors":True,"observable_signatures":len(obs_values),
                "all_sources_separated":len(obs_values)==len(self.states),
                "decode_table":tuple((sig,pair[1]) for sig,pair in obs_values.items())}

    def pairwise_and_global_consistency(self, reports: Sequence[Evidence]) -> dict:
        """Pairwise realizability need not imply a joint source witness."""
        r=tuple(reports)
        pairwise=all(bool(self.fiber((r[i],r[j])))
                     for i in range(len(r)) for j in range(i+1,len(r)))
        jointly=bool(self.fiber(r))
        return {"pairwise_realizable":pairwise,"globally_realizable":jointly,
                "shared_source_fiber":self.fiber(r)}


def _solve(A: Sequence[Sequence[F]], b: Sequence[F]) -> tuple[F,...]:
    """Exact rational Gaussian elimination with a singularity witness."""
    n=len(b)
    if len(A)!=n or any(len(row)!=n for row in A):
        raise CarrierDescentError("Not a square Dirichlet system")
    aug=[[exact(x) for x in A[i]]+[exact(b[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if aug[i][j]!=0),None)
        if pivot is None:
            raise CarrierDescentError("Unanchored interior component: singular Laplacian")
        aug[j],aug[pivot]=aug[pivot],aug[j]
        inv=aug[j][j]
        aug[j]=[v/inv for v in aug[j]]
        for i in range(n):
            if i!=j:
                fac=aug[i][j]
                if fac:
                    aug[i]=[x-fac*y for x,y in zip(aug[i],aug[j])]
    return tuple(row[n] for row in aug)


@dataclass(frozen=True)
class SharedCarrierGraph:
    """Conductance graph; every connected component must meet boundary.

    A carrier graph plus boundary values specifies a UNIQUE interior only
    under the separately declared harmonic/minimum-energy law.
    """
    carrier_id: str
    version: int
    vertices: tuple[Hashable,...]
    boundary: tuple[Hashable,...]
    edges: tuple[tuple[Hashable,Hashable,F],...]

    def __post_init__(self) -> None:
        if not self.carrier_id or type(self.version) is not int or self.version<0:
            raise CarrierDescentError("Exact source carrier identity and version needed")
        if not self.vertices or len(set(self.vertices))!=len(self.vertices):
            raise CarrierDescentError("Distinct finite carrier vertices required")
        if not self.boundary or len(set(self.boundary))!=len(self.boundary) or (
                set(self.boundary)-set(self.vertices)):
            raise CarrierDescentError("Boundary must be nonempty subset of carrier")
        labels={v:i for i,v in enumerate(self.vertices)}
        edges=[]
        seen=set()
        for u,v,w in self.edges:
            if u not in labels or v not in labels or u==v:
                raise CarrierDescentError("Edges must join two declared distinct vertices")
            key=frozenset((u,v))
            if key in seen:
                raise CarrierDescentError("Use unique undirected edges")
            seen.add(key)
            wt=exact(w)
            if wt<=0:
                raise CarrierDescentError("All conductances must be positive")
            edges.append((u,v,wt))
        object.__setattr__(self,'edges',tuple(edges))
        adjacency={v:set() for v in self.vertices}
        for u,v,_ in edges:
            adjacency[u].add(v);adjacency[v].add(u)
        visited=set()
        boundary=set(self.boundary)
        for vertex in self.vertices:
            if vertex in visited:continue
            frontier=[vertex]
            visited.add(vertex)
            component=set()
            while frontier:
                current=frontier.pop()
                component.add(current)
                for other in adjacency[current]:
                    if other not in visited:
                        visited.add(other);frontier.append(other)
            if not(component & boundary):
                raise CarrierDescentError("Every connected component must reach boundary")

    @property
    def interiors(self) -> tuple[Hashable,...]:
        return tuple(v for v in self.vertices if v not in set(self.boundary))

    def laplacian(self) -> tuple[tuple[F,...],...]:
        n=len(self.vertices)
        L=[[F(0) for _ in range(n)] for _ in range(n)]
        where={v:i for i,v in enumerate(self.vertices)}
        for u,v,w in self.edges:
            i,j=where[u],where[v]
            L[i][i]+=w;L[j][j]+=w
            L[i][j]-=w;L[j][i]-=w
        return tuple(tuple(row) for row in L)

    def complete_harmonic(self, boundary_values: Mapping[Hashable,F]) -> dict[Hashable,F]:
        """Construct the unique minimum-energy harmonic extension (exact)."""
        if set(boundary_values)!=set(self.boundary):
            raise CarrierDescentError("All and only declared boundary E reports required")
        b={v:exact(boundary_values[v]) for v in self.boundary}
        inside=self.interiors
        if not inside:
            return {v:b[v] for v in self.vertices}
        at={v:i for i,v in enumerate(self.vertices)}
        L=self.laplacian()
        A=[[L[at[u]][at[v]] for v in inside] for u in inside]
        rhs=[-sum((L[at[u]][at[v]]*b[v] for v in self.boundary),F(0)) for u in inside]
        interior_values=_solve(A,rhs)
        answer={**b,**dict(zip(inside,interior_values))}
        return {v:answer[v] for v in self.vertices}

    def energy(self, field: Mapping[Hashable,F]) -> F:
        if set(field)!=set(self.vertices):
            raise CarrierDescentError("Energy demands all carrier vertices")
        values={v:exact(x) for v,x in field.items()}
        return sum((F(1,2)*w*(values[u]-values[v])**2
                    for u,v,w in self.edges),F(0))

    def flux(self, field: Mapping[Hashable,F]) -> dict[Hashable,F]:
        if set(field)!=set(self.vertices):
            raise CarrierDescentError("Flux demands all carrier vertices")
        v={key:exact(value) for key,value in field.items()}
        L=self.laplacian()
        return {u:sum((L[i][j]*v[x] for j,x in enumerate(self.vertices)),F(0))
                for i,u in enumerate(self.vertices)}

    def boundary_operator(self) -> tuple[tuple[F,...],...]:
        """Schur complement DtN map, constructed by exact harmonic bases."""
        n=len(self.boundary)
        columns=[]
        for j in range(n):
            b={v:F(int(i==j)) for i,v in enumerate(self.boundary)}
            field=self.complete_harmonic(b)
            flux=self.flux(field)
            columns.append(tuple(flux[v] for v in self.boundary))
        matrix=tuple(tuple(columns[j][i] for j in range(n)) for i in range(n))
        if any(matrix[i][j]!=matrix[j][i] for i in range(n) for j in range(n)):
            raise AssertionError("Conductance source produced nonsymmetric DtN")
        if any(sum(row,F(0)) for row in matrix):
            raise AssertionError("DtN must annihilate the constant boundary field")
        return matrix

    def boundary_energy(self, boundary_values: Mapping[Hashable,F]) -> F:
        if set(boundary_values)!=set(self.boundary):
            raise CarrierDescentError("Boundary data mismatch")
        b=tuple(exact(boundary_values[v]) for v in self.boundary)
        N=self.boundary_operator()
        val=F(1,2)*sum((b[i]*N[i][j]*b[j]
                        for i in range(len(b)) for j in range(len(b))),F(0))
        if val!=self.energy(self.complete_harmonic(boundary_values)):
            raise AssertionError("Failed exact interior/boundary energy identification")
        return val

    def completion_receipt(self, boundary_values: Mapping[Hashable,F]) -> dict:
        field=self.complete_harmonic(boundary_values)
        flux=self.flux(field)
        if any(flux[v] for v in self.interiors):
            raise AssertionError("Failed source harmonicity")
        energ=self.energy(field)
        if energ!=self.boundary_energy(boundary_values):
            raise AssertionError("Boundary-only holographic energy mismatch")
        return {"carrier_id":self.carrier_id,"source_version":self.version,
                "boundary_vertices":len(self.boundary),
                "interior_vertices":len(self.interiors),
                "reconstructed_interior":tuple((v,field[v]) for v in self.interiors),
                "global_energy":energ,"boundary_only_energy":energ,
                "harmonic_law_assumed":True,"physical_source_authenticated":False}
