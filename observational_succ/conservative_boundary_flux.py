"""Source-typed two-sided scalar errors and exact graph port-energy flux.

No physical energy claim is made for zeta residues. The scalar errors are
nonnegative comparison budgets for real r>1 only. Graph energy identities
require positive undirected conductances and invertible grounded interior.
Classical inputs: Euler product, convexity, Schur complement/Kron reduction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt


class BoundaryFluxError(ValueError):
    """Invalid exact source, graph, partition or cutoff."""


def q(value):
    if type(value) not in (int, F):
        raise BoundaryFluxError("require exact rational, not float or bool")
    return F(value)


def verify_int(value, minimum, maximum=10000):
    if type(value) is not int or not minimum <= value <= maximum:
        raise BoundaryFluxError("invalid bounded integer source index")
    return value


def genuine_primes(bound):
    verify_int(bound, 2, 10000)
    return tuple(p for p in range(2,bound+1)
                 if all(p%d for d in range(2,isqrt(p)+1)))


def true_prime_product(power, bound):
    verify_int(power,2,8)
    value=F(1)
    for p in genuine_primes(bound):
        value *= F(p**power,p**power-1)
    return value


@dataclass(frozen=True)
class TwoSidedEulerBudget:
    power:int
    successor_cutoff:int
    prime_cutoff:int
    succ_above:F
    prime_below:F
    observable_gap:F
    succ_error_cap:F
    prime_error_cap:F
    intersection_lower:F
    intersection_upper:F


def two_sided_euler_budget(power, successor_cutoff, prime_cutoff):
    """G(r) lies between D_N and P_X-1/(r-1); gap=delta_N+R_X.

    Domain integer r>=2, N<=X; true primes only. The proof of gap>=0
    uses zeta and convexity, not numerical zeta evaluation.
    """
    verify_int(power,2,8)
    verify_int(successor_cutoff,1,5000)
    verify_int(prime_cutoff,2,10000)
    if successor_cutoff>prime_cutoff:
        raise BoundaryFluxError("required cofinal source chart N<=X")
    N=successor_cutoff
    r=power
    h=sum((F(1,n**r) for n in range(1,N+1)),F())
    partial_integral=(F(1)-F(1,N**(r-1)))/(r-1)
    above=h-partial_integral
    below=true_prime_product(r,prime_cutoff)-F(1,r-1)
    gap=above-below
    cap_a=F(1,2*N**r)
    cap_b=F(1,(r-1)*prime_cutoff**(r-1))
    if not F(0)<=gap<=cap_a+cap_b:
        raise ArithmeticError("exact SUCC/FUCC signed flux budget contradicted")
    lo=max(below,above-cap_a)
    hi=min(above,below+cap_b)
    if lo>hi:
        raise ArithmeticError("exact lower/upper certificates inconsistent")
    return TwoSidedEulerBudget(r,N,prime_cutoff,above,below,gap,
                               cap_a,cap_b,lo,hi)


def rectangle_curvature(power, n, n_next, x, x_next):
    """Zero mixed difference is a FLATNESS control, not independent evidence.

    Gap(n,x)=SUCC(n)-FUCC(x). A nonzero rectangle means the assumed
    independent cutoff/source maps are incompatible or interact.
    """
    verify_int(n,1,5000)
    verify_int(n_next,n,5000)
    verify_int(x,2,10000)
    verify_int(x_next,x,10000)
    if n_next>x:
        raise BoundaryFluxError("all four source charts need N<=X")
    a=two_sided_euler_budget(power,n,x).observable_gap
    b=two_sided_euler_budget(power,n_next,x).observable_gap
    c=two_sided_euler_budget(power,n,x_next).observable_gap
    d=two_sided_euler_budget(power,n_next,x_next).observable_gap
    return a-b-c+d


def matrix(rows):
    rows=tuple(tuple(q(x) for x in row) for row in rows)
    if not rows or any(len(row)!=len(rows) for row in rows):
        raise BoundaryFluxError("nonempty square matrix expected")
    if any(rows[i][j]!=rows[j][i]
           for i in range(len(rows)) for j in range(i+1,len(rows))):
        raise BoundaryFluxError("symmetric matrix expected")
    return rows


def inverse(rows):
    a=matrix(rows)
    n=len(a)
    aug=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if aug[i][j]),None)
        if pivot is None:
            raise BoundaryFluxError("singular/unobservable internal block")
        aug[j],aug[pivot]=aug[pivot],aug[j]
        v=aug[j][j]
        aug[j]=[x/v for x in aug[j]]
        for i in range(n):
            if i!=j:
                f=aug[i][j]
                aug[i]=[x-f*y for x,y in zip(aug[i],aug[j])]
    return tuple(tuple(row[n:]) for row in aug)


def mv(a,v):
    if any(len(row)!=len(v) for row in a):
        raise BoundaryFluxError("vector dimensions differ")
    return tuple(sum((x*y for x,y in zip(row,v)),F()) for row in a)


def dot(v,w):
    if len(v)!=len(w):
        raise BoundaryFluxError("dot dimensions differ")
    return sum((x*y for x,y in zip(v,w)),F())


def partitions(size,boundary):
    if not isinstance(boundary,tuple) or not boundary or len(set(boundary))!=len(boundary):
        raise BoundaryFluxError("nonempty ordered boundary ports without repeats")
    if any(type(i) is not int or not 0<=i<size for i in boundary):
        raise BoundaryFluxError("invalid port index")
    internal=tuple(i for i in range(size) if i not in boundary)
    if not internal:
        raise BoundaryFluxError("at least one internal state required")
    return boundary, internal


def schur_port(matrix_source,boundary):
    """Exact Schur short for an invertible interior block; no PSD implied."""
    a=matrix(matrix_source)
    B,I=partitions(len(a),boundary)
    d_inv=inverse(tuple(tuple(a[i][j] for j in I) for i in I))
    cross=tuple(tuple(a[i][j] for j in I) for i in B)
    corrected=tuple(tuple(
        a[i][j]-sum((cross[u][k]*d_inv[k][t]*cross[v][t]
                     for k in range(len(I)) for t in range(len(I))),F())
        for v,j in enumerate(B)) for u,i in enumerate(B))
    return corrected


def _positive_laplacian(a):
    if (any(sum(row)!=0 for row in a) or
            any(a[i][j]>0 for i in range(len(a)) for j in range(len(a)) if i!=j)):
        raise BoundaryFluxError("positive-conductance graph Laplacian required")
    return a


def laplacian(node_count,edges):
    """Undirected positive rational conductances; parallel edges allowed."""
    verify_int(node_count,2,20)
    if not isinstance(edges,tuple) or not edges:
        raise BoundaryFluxError("nonempty tuple of source-labelled edge triples")
    a=[[F(0) for _ in range(node_count)] for _ in range(node_count)]
    for edge in edges:
        if not isinstance(edge,tuple) or len(edge)!=3:
            raise BoundaryFluxError("edge must be (node,node,positive conductance)")
        i,j,weight=edge
        if (type(i) is not int or type(j) is not int
                or not 0<=i<node_count or not 0<=j<node_count or i==j):
            raise BoundaryFluxError("no self-loop, missing or out-of-range nodes")
        c=q(weight)
        if c<=0:
            raise BoundaryFluxError("positive conductance required")
        a[i][i]+=c
        a[j][j]+=c
        a[i][j]-=c
        a[j][i]-=c
    return matrix(a)


@dataclass(frozen=True)
class GraphPortBalance:
    effective_laplacian:tuple
    harmonic_interior:tuple
    raw_energy:F
    port_energy:F
    hidden_energy:F
    observed_boundary_current:tuple
    effective_boundary_current:tuple
    interior_residual_current:tuple
    transported_boundary_error:tuple
    full_current_sum:F


def graph_port_balance(laplacian_source,boundary,potentials):
    """E(u)=E_min(boundary)+<interior_current,D^-1 interior_current>.

    j_boundary - j_effective = L_BI D^-1 j_interior. This transport is
    EXACT, not a norm estimate; only harmonic states have zero residual.
    """
    a=matrix(laplacian_source)
    B,I=partitions(len(a),boundary)
    _positive_laplacian(a)
    u=tuple(q(v) for v in potentials)
    if len(u)!=len(a):
        raise BoundaryFluxError("one potential per node required")
    ub=tuple(u[i] for i in B)
    ui=tuple(u[i] for i in I)
    d=tuple(tuple(a[i][j] for j in I) for i in I)
    dinv=inverse(d)
    a_bi=tuple(tuple(a[i][j] for j in I) for i in B)
    a_ib=tuple(tuple(a[i][j] for j in B) for i in I)
    harmonic=tuple(-x for x in mv(dinv,mv(a_ib,ub)))
    j=mv(a,u)
    jb=tuple(j[i] for i in B)
    ji=tuple(j[i] for i in I)
    eff=schur_port(a,B)
    jeff=mv(eff,ub)
    transferred=mv(a_bi,mv(dinv,ji))
    raw=dot(u,j)
    port=dot(ub,jeff)
    hidden=dot(ji,mv(dinv,ji))
    if raw!=port+hidden or any(jb[i]-jeff[i]!=transferred[i] for i in range(len(B))):
        raise ArithmeticError("source energy or boundary flux decomposition failed")
    if sum(j)!=0 or raw<port or hidden<0:
        raise ArithmeticError("graph conductance/signed energy assumptions violated")
    return GraphPortBalance(eff,harmonic,raw,port,hidden,jb,jeff,ji,
                            transferred,sum(j))


def dynamic_port_operator(laplacian_source,internal_masses,boundary,laplace_frequency):
    """K(s)=L+s diag(M) interior, Schur(K). Constant static response can
    mask distinct positive storage/memory; s>0 rational only.
    """
    a=matrix(laplacian_source)
    _positive_laplacian(a)
    masses=tuple(q(m) for m in internal_masses)
    if len(masses)!=len(a) or any(m<0 for m in masses):
        raise BoundaryFluxError("nonnegative mass on each graph node")
    s=q(laplace_frequency)
    if s<0:
        raise BoundaryFluxError("use real nonnegative Laplace frequency")
    K=tuple(tuple(a[i][j]+(s*masses[i] if i==j else 0)
                  for j in range(len(a))) for i in range(len(a)))
    return schur_port(K,boundary)


def normalized_weights(weights):
    p=tuple(q(w) for w in weights)
    if not p or any(w<=0 for w in p) or sum(p)!=1:
        raise BoundaryFluxError("common strictly positive source probability, total one")
    return p


def partition(groups,n):
    if not isinstance(groups,tuple) or not groups:
        raise BoundaryFluxError("finite tuple of nonempty observational fibers")
    if any(not isinstance(g,tuple) or not g for g in groups):
        raise BoundaryFluxError("empty or untyped observation class")
    entries=[i for g in groups for i in g]
    if any(type(i) is not int or not 0<=i<n for i in entries):
        raise BoundaryFluxError("invalid observation index")
    if sorted(entries)!=list(range(n)):
        raise BoundaryFluxError("source partition must cover exactly once")
    return groups


def conditional_project(values,weights,groups):
    """Finite conditional expectation of common-source rational data."""
    v=tuple(q(x) for x in values)
    p=normalized_weights(weights)
    if len(v)!=len(p):
        raise BoundaryFluxError("source/probability dimension mismatch")
    groups=partition(groups,len(v))
    result=[F(0)]*len(v)
    for group in groups:
        mass=sum((p[i] for i in group),F())
        mean=sum((p[i]*v[i] for i in group),F())/mass
        for i in group:
            result[i]=mean
    return tuple(result)


def squared_source_norm(values,weights):
    v=tuple(q(x) for x in values)
    p=normalized_weights(weights)
    if len(v)!=len(p):
        raise BoundaryFluxError("source dimension mismatch")
    return sum((w*x*x for w,x in zip(p,v)),F())


@dataclass(frozen=True)
class NestedInformationBudget:
    coarse_projection:tuple
    fine_projection:tuple
    coarse_unresolved:F
    fine_unresolved:F
    visible_innovation:F
    orthogonality_cross:F


def nested_information_budget(values,weights,coarse,fine):
    """Orthogonal error flux for genuine refinement under one source measure.

    ||v-Pcoarse v||² = ||v-Pfine v||² + ||(Pfine-Pcoarse)v||².
    No such law is asserted for nonnested partitions or different measures.
    """
    v=tuple(q(x) for x in values)
    p=normalized_weights(weights)
    coarse=partition(coarse,len(v))
    fine=partition(fine,len(v))
    if any(not any(set(f).issubset(set(c)) for c in coarse) for f in fine):
        raise BoundaryFluxError("fine observations must refine coarse partition")
    pc=conditional_project(v,p,coarse)
    pf=conditional_project(v,p,fine)
    ec=tuple(x-y for x,y in zip(v,pc))
    ef=tuple(x-y for x,y in zip(v,pf))
    innovation=tuple(x-y for x,y in zip(pf,pc))
    coarse_res=squared_source_norm(ec,p)
    fine_res=squared_source_norm(ef,p)
    gained=squared_source_norm(innovation,p)
    crossed=sum((w*x*y for w,x,y in zip(p,ef,innovation)),F())
    if coarse_res!=fine_res+gained or crossed!=0:
        raise ArithmeticError("source metric and nested orthogonality violated")
    return NestedInformationBudget(pc,pf,coarse_res,fine_res,gained,crossed)


@dataclass(frozen=True)
class CorrelatedEnergyLedger:
    total:F
    visible:F
    unresolved:F
    cross_term:F


def correlated_energy_ledger(source,approximation,weights):
    """Exact correlation debt in a DECLARED common weighted Hilbert metric.

    ||source||²=||approx||²+||source-approx||²+2<approx,source-approx>.
    The signed cross term may be negative. The identity is mathematical
    bookkeeping, not independently measured physical energy.
    """
    source=tuple(q(x) for x in source)
    approximation=tuple(q(x) for x in approximation)
    p=normalized_weights(weights)
    if len(source)!=len(approximation) or len(source)!=len(p):
        raise BoundaryFluxError("both sides require the SAME source-indexed metric")
    residue=tuple(x-y for x,y in zip(source,approximation))
    total=squared_source_norm(source,p)
    visible=squared_source_norm(approximation,p)
    unresolved=squared_source_norm(residue,p)
    crossed=2*sum((w*x*y for w,x,y in zip(p,approximation,residue)),F())
    if total!=visible+unresolved+crossed:
        raise ArithmeticError("exact correlated error-energy ledger failed")
    return CorrelatedEnergyLedger(total,visible,unresolved,crossed)


@dataclass(frozen=True)
class DynamicConservationBalance:
    boundary_input_power:F
    resistive_dissipation:F
    hidden_storage_rate:F
    interior_time_derivative:tuple


def rc_power_balance(laplacian_source,boundary,potentials,capacities):
    """Instantaneous exact RC balance with no interior driving sources.

    Interior C_i u_i'=-(L u)_i and j_B=(Lu)_B imply
      <u_B,j_B> = u^T L u + d/dt[sum_i C_i u_i^2/2].
    Voltage source power in equals dissipation + change in stored energy.
    This is literal circuit energy under the declared RC interpretation.
    """
    a=matrix(laplacian_source)
    B,I=partitions(len(a),boundary)
    _positive_laplacian(a)
    u=tuple(q(v) for v in potentials)
    c=tuple(q(x) for x in capacities)
    if len(u)!=len(a) or len(c)!=len(I) or any(cap<=0 for cap in c):
        raise BoundaryFluxError("positive storage per internal vertex required")
    j=mv(a,u)
    udot=tuple(-j[i]/cap for i,cap in zip(I,c))
    supplied=dot(tuple(u[i] for i in B),tuple(j[i] for i in B))
    dissipation=dot(u,j)
    rate=sum((cap*u[i]*v for i,cap,v in zip(I,c,udot)),F())
    if supplied!=dissipation+rate or dissipation<0:
        raise ArithmeticError("physical RC energy identity violated")
    return DynamicConservationBalance(supplied,dissipation,rate,udot)


def linear_map(rows,source_dimension):
    if type(source_dimension) is not int or source_dimension<1:
        raise BoundaryFluxError("positive source dimension")
    a=tuple(tuple(q(t) for t in row) for row in rows)
    if not a or any(len(row)!=source_dimension for row in a):
        raise BoundaryFluxError("valid nonempty rectangular linear transport required")
    return a


def _idempotent(a):
    return all(sum((a[i][k]*a[k][j] for k in range(len(a))),F())==a[i][j]
               for i in range(len(a)) for j in range(len(a)))


@dataclass(frozen=True)
class TwoDomainTransportBudget:
    exact_target:tuple
    finite_target:tuple
    total_residual:tuple
    target_cutoff_residual:tuple
    transported_source_residual:tuple
    total_squared:F
    target_squared:F
    source_squared:F
    cross_term:F
    target_projection_orthogonal:bool


def two_domain_transport_budget(transport,source,source_projector,target_projector):
    """F x - Q F P x = (I-Q)F x + Q F(I-P)x.

    For orthogonal Q, pieces lie in orthogonal target subspaces and their
    squared norms add. For oblique Q, the signed cross term is essential.
    Maps must share a declared exact finite source/target Euclidean metric.
    """
    x=tuple(q(v) for v in source)
    f=linear_map(transport,len(x))
    P=linear_map(source_projector,len(x))
    Q=linear_map(target_projector,len(f))
    if len(P)!=len(x) or len(Q)!=len(f):
        raise BoundaryFluxError("source/target projection dimensions")
    if not _idempotent(P) or not _idempotent(Q):
        raise BoundaryFluxError("honest idempotent truncation maps required")
    y=mv(f,x)
    yp=mv(f,mv(P,x))
    finite=mv(Q,yp)
    full_res=tuple(a-b for a,b in zip(y,finite))
    target_res=tuple(a-b for a,b in zip(y,mv(Q,y)))
    src_res=mv(Q,mv(f,tuple(a-b for a,b in zip(x,mv(P,x)))))
    if any(u!=v+w for u,v,w in zip(full_res,target_res,src_res)):
        raise ArithmeticError("cross-domain correction identity violated")
    a2=dot(full_res,full_res)
    t2=dot(target_res,target_res)
    s2=dot(src_res,src_res)
    cross=2*dot(target_res,src_res)
    if a2!=t2+s2+cross:
        raise ArithmeticError("cross-domain norm transfer identity violated")
    orth=all(Q[i][j]==Q[j][i] for i in range(len(Q)) for j in range(len(Q)))
    if orth and cross!=0:
        raise ArithmeticError("orthogonal target projector must kill cross term")
    return TwoDomainTransportBudget(y,finite,full_res,target_res,src_res,
                                    a2,t2,s2,cross,orth)
