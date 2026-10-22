"""Observation-anchored boundary rigidity and exact finite DtN counterexamples.

Classical finite weighted graph Laplacians, Schur complements, and interval
identification. This does NOT predict alpha, Euler's gamma, a gravitational
metric, or a physical source. Its purpose is to distinguish a mutually
exclusive model realization from an empirical-fit tautology.

No third-party packages. Every finite model value is Fraction-exact.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q


class BoundarySourceError(ValueError):
    """Malformed source geometry, ill-typed prediction, or uncalibrated probe."""


def rational(x):
    if type(x) not in (int,Q):
        raise BoundarySourceError("exact integer/Fraction expected, not float/bool")
    return Q(x)


def matrix_inverse(M):
    """Independent Gauss-Jordan inverse, exact rational arithmetic."""
    n=len(M)
    if not n or any(len(row)!=n for row in M):
        raise BoundarySourceError("nonempty square finite matrix required")
    a=[[rational(v) for v in row]+[Q(i==j) for j in range(n)]
       for i,row in enumerate(M)]
    for k in range(n):
        pivot=next((j for j in range(k,n) if a[j][k]),None)
        if pivot is None:
            raise BoundarySourceError("singular internal operator: DtN undefined")
        a[k],a[pivot]=a[pivot],a[k]
        v=a[k][k]
        a[k]=[z/v for z in a[k]]
        for j in range(n):
            if j==k:continue
            r=a[j][k]
            a[j]=[u-r*v for u,v in zip(a[j],a[k])]
    return tuple(tuple(r[n:]) for r in a)


def matmul(A,B):
    n=len(A)
    if not n or not B or any(len(r)!=len(A[0]) for r in A) or any(len(r)!=len(B[0]) for r in B) or len(A[0])!=len(B):
        raise BoundarySourceError("incompatible matrices")
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),Q())
                       for j in range(len(B[0]))) for i in range(n))


def matadd(A,B):
    if not A or len(A)!=len(B) or any(len(r)!=len(s) for r,s in zip(A,B)):
        raise BoundarySourceError("nonmatching boundary spaces")
    return tuple(tuple(rational(x)+rational(y) for x,y in zip(r,s))
                 for r,s in zip(A,B))


@dataclass(frozen=True)
class FiniteNetwork:
    count: int
    boundary: tuple[int,...]
    edges: tuple[tuple[int,int,Q],...]
    shunts: tuple[tuple[int,Q],...] = ()

    def __post_init__(self):
        if type(self.count) is not int or self.count<2 or self.count>12:
            raise BoundarySourceError("2..12 physical vertices required")
        if type(self.boundary) is not tuple or len(self.boundary)<2 or len(set(self.boundary))!=len(self.boundary):
            raise BoundarySourceError("two or more distinct boundary vertices required")
        if any(type(v) is not int or not 0<=v<self.count for v in self.boundary):
            raise BoundarySourceError("wrong boundary vertex")
        for u,v,g in self.edges:
            if type(u) is not int or type(v) is not int or u==v or not(0<=u<self.count and 0<=v<self.count) or rational(g)<=0:
                raise BoundarySourceError("positive conductance and lawful undirected edge required")
        for v,c in self.shunts:
            if type(v) is not int or not 0<=v<self.count or rational(c)<0:
                raise BoundarySourceError("nonnegative capacitance on lawful node required")


def boundary_response(net:FiniteNetwork,frequency=0):
    """DtN/Y(s) of a finite positive resistor network with shunts s*c.

    Exact Schur elimination of unobserved interior. At s=0, standard
    static Dirichlet-to-Neumann; at real s>=0, an RC Laplace-domain response.
    Shunts may be physical added measurement structure, not a mathematical
    consequence of a static resistor graph.
    """
    if type(net) is not FiniteNetwork:
        raise BoundarySourceError("finite network required")
    s=rational(frequency)
    if s<0:
        raise BoundarySourceError("nonnegative real Laplace parameter required")
    L=[[Q() for _ in range(net.count)] for _ in range(net.count)]
    for u,v,g in net.edges:
        g=rational(g)
        L[u][u]+=g;L[v][v]+=g
        L[u][v]-=g;L[v][u]-=g
    for v,c in net.shunts:
        L[v][v]+=s*rational(c)
    b=net.boundary
    interior=tuple(i for i in range(net.count) if i not in b)
    C=tuple(tuple(L[i][j] for j in b) for i in b)
    if not interior:return C
    A=tuple(tuple(L[i][j] for j in interior) for i in interior)
    B=tuple(tuple(L[i][j] for j in b) for i in interior)
    Bt=tuple(tuple(L[i][j] for j in interior) for i in b)
    subtract=matmul(Bt,matmul(matrix_inverse(A),B))
    return tuple(tuple(C[i][j]-subtract[i][j] for j in range(len(b)))
                 for i in range(len(b)))


def boundary_glue(*responses):
    """Common-interface glue: same potential and flux sum (no hidden coupling)."""
    if not responses:
        raise BoundarySourceError("at least one boundary interface required")
    result=responses[0]
    for r in responses[1:]:result=matadd(result,r)
    return result


def conductance_from_two_terminal_response(M):
    if len(M)!=2 or any(len(r)!=2 for r in M):
        raise BoundarySourceError("2-terminal DC response required")
    if M[0][0]!=M[1][1] or M[0][1]!=M[1][0] or M[0][0]!=-M[0][1]:
        raise BoundarySourceError("matrix not a two-terminal static Laplacian")
    return M[0][0]


@dataclass(frozen=True)
class PredictedBranch:
    """Frozen-before-measurement prediction; class ID = declared physical gauge."""
    name: str
    equivalence_class: str
    predicted: Q
    theory_error: Q = Q()

    def __post_init__(self):
        if not self.name or not self.equivalence_class:
            raise BoundarySourceError("source model and gauge class required")
        rational(self.predicted)
        if rational(self.theory_error)<0:
            raise BoundarySourceError("nonnegative independent theory error required")


@dataclass(frozen=True)
class BoundaryObservation:
    """Recorded scalar interval, not inherently a physically verified datum."""
    value: Q
    instrument_error: Q
    source_kind: str = "synthetic"
    source_id: str = ""
    instrument_id: str = ""
    predeclared_predictions: bool = False
    independent_of_candidate_fitting: bool = False

    def __post_init__(self):
        rational(self.value)
        if rational(self.instrument_error)<0:
            raise BoundarySourceError("nonnegative measurement error required")
        if self.source_kind not in ("synthetic","physical_transcript"):
            raise BoundarySourceError("invalid source provenance type")


def surviving_branches(branches, observation):
    """Exact interval overlap; never assert global uniqueness from a scalar alone."""
    if type(observation) is not BoundaryObservation or not branches:
        raise BoundarySourceError("exact observed interval and finite family required")
    b=tuple(branches)
    if any(type(x) is not PredictedBranch for x in b):
        raise BoundarySourceError("predeclared typed candidate models required")
    if len({x.name for x in b})!=len(b):
        raise BoundarySourceError("duplicate model identities")
    c=rational(observation.value)
    e=rational(observation.instrument_error)
    survivors=tuple(x for x in b if abs(rational(x.predicted)-c)<=
                    rational(x.theory_error)+e)
    classes=tuple(sorted({x.equivalence_class for x in survivors}))
    distinct_preds=tuple(sorted({rational(x.predicted) for x in survivors}))
    return {
        "survivors":tuple(x.name for x in survivors),
        "equivalence_classes":classes,
        "unique_class_within_declared_family":len(classes)==1,
        "distinct_prediction_values":distinct_preds,
        "physically_attested_by_software":False,
        "source_law_verified":False,
        "prediction_frozen_before_data":observation.predeclared_predictions,
        "independent_of_candidate_fitting":observation.independent_of_candidate_fitting,
        "candidate_family_complete_in_reality":False,
    }


def eligible_empirical_pin(result,observation):
    """Conservative epistemic gate: not a physical proof from a JSON assertion."""
    if type(observation) is not BoundaryObservation:
        raise BoundarySourceError("physical observation envelope required")
    return {
        "candidate_fiber_is_unique":result["unique_class_within_declared_family"],
        "reported_provenance_complete":bool(
            observation.source_kind=="physical_transcript"
            and observation.source_id and observation.instrument_id
            and observation.predeclared_predictions
            and observation.independent_of_candidate_fitting),
        "measurement_independently_authenticated":False,
        "global_physical_geometry_proved":False,
    }


def modeled_alpha_anchor_rejection():
    """An external measured constant is NOT predicted by simply writing it in."""
    return {
        "observational_constant":"fine_structure_alpha",
        "free_parameter_matching_data_is_not_a_prediction":True,
        "source_independent_holdout_required":True,
        "physical_measurements_performed_here":False,
    }
