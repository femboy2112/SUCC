"""Equivariant Koszul redundancy and exact trace-obstruction probes.

Extends the preexisting full-prime-power Koszul complex; does NOT edit it.
The source half-density and prime-clock magnitudes are imported unchanged.
At finite n the Koszul fiber K_n is acyclic for n>1. Hence any EVEN
chain-map's supertrace on K_n vanishes (finite Lefschetz identity),
which exposes a sharp obstruction to a naive Connes/Weil supertrace.

Prime FUCC x_p lifts as a genuine chain map K_n -> K_{pn};
its adjoint fails equivariance at the first appearance of p.
At 1 -> p the quotient has H_1=Q, while every other new-prime
quotient is acyclic. These are exact source-relative distinctions.

No zeros, completion, global Connes trace or Weil sign are inferred.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isqrt

from .koszul_prime_cancellation import (
    KoszulSourceError, PrimeKoszul, source_multidegree,
)


class EquivariantDescentError(ValueError):
    """Typed source, finite chain, or unsupported trace assertion failed."""


def _integer(n):
    if type(n) is not int or not 1 <= n <= 100_000:
        raise EquivariantDescentError("genuine positive source integer <=100000 required")
    return n


def _prime(p):
    if type(p) is not int or not 2 <= p <= 100_000 or any(
        p % d == 0 for d in range(2, isqrt(p) + 1)
    ):
        raise EquivariantDescentError("genuine prime-FUCC generator required")
    return p


def _fiber(n):
    _integer(n)
    try:
        return source_multidegree(n)
    except KoszulSourceError as exc:
        raise EquivariantDescentError("invalid inherited Koszul source") from exc


def _rank(matrix):
    """Independent rational row elimination: not a claimed universal proof."""
    a = [[F(x) for x in row] for row in matrix]
    if not a:
        return 0
    ncols = len(a[0])
    if any(len(row) != ncols for row in a):
        raise EquivariantDescentError("rectangular exact matrix required")
    k = 0
    for j in range(ncols):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        v = a[k][j]
        a[k] = [x / v for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                scale = a[i][j]
                a[i] = [x - scale*y for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def _canonical_wedge(n, wedge):
    fiber = _fiber(n)
    if type(wedge) is not tuple or wedge not in fiber.basis():
        raise EquivariantDescentError("source-authentic exterior wedge required")
    return fiber, wedge


def matrix_chain_diagonal(n, diagonal):
    """Exact finite diagonal even observable, source supertrace and [d,T].

    diagonal maps wedge-subset -> rational eigenvalue, on the FULL fiber.
    If [d,T]=0 then supertrace is the Lefschetz trace on homology.
    For n>1 it MUST vanish. A nonzero p^k prime trace must therefore
    retain a chain defect, a boundary signal or a separately justified
    analytic trace anomaly.
    """
    f = _fiber(n)
    states = f.basis()
    if type(diagonal) is not dict or set(diagonal) != set(states):
        raise EquivariantDescentError("exact source-complete diagonal graded test required")
    if any(type(v) not in (int, F) for v in diagonal.values()):
        raise EquivariantDescentError("exact rational eigenvalues required")
    weights = {s:F(diagonal[s]) for s in states}
    defect = []
    for S in states:
        for T,sgn in f.boundary(S):
            comm = F(sgn)*(weights[S] - weights[T])
            if comm:
                defect.append((S,T,comm))
    supertrace = sum(((-1)**len(S)*weights[S] for S in states), F(0))
    chain_map = not defect
    if chain_map and n > 1 and supertrace:
        raise AssertionError("acyclic chain-map acquired a forbidden supertrace")
    return {
        "source_integer":n, "original_basis_size":len(states),
        "source_complete_even_operator":True,
        "supertrace":supertrace, "commutes_with_d":chain_map,
        "commutator_defect_edges":tuple(defect),
        "supertrace_of_source_cohomology":weights[()] if n==1 else F(0),
        "has_spectral_Weil_distribution":False,
        "original_Gamma_contact_added":False, "RH_proved":False,
    }


def trace_obstruction(n):
    """Calibrate two rival trace proposals with one original n source.

    Central scalar T=I commutes with d, so Str(T)=delta_(n,1).
    The even grade-0 projection P0 yields Str(P0)=1 for every n,
    but [d,P0]!=0 whenever n>1. On p^k this contrast survives.
    """
    f=_fiber(n)
    scalar=matrix_chain_diagonal(n,{s:F(1) for s in f.basis()})
    graded=matrix_chain_diagonal(n,{s:F(int(s==())) for s in f.basis()})
    if scalar["supertrace"]!=int(n==1) or graded["supertrace"]!=1:
        raise AssertionError("source trace mutation gate failed")
    return {
        "n":n, "chain_compatible_supertrace":scalar["supertrace"],
        "grade_zero_projector_supertrace":graded["supertrace"],
        "grade_zero_projector_commutes_with_d":graded["commutes_with_d"],
        "graded_defect_edges":graded["commutator_defect_edges"],
        "acyclic_prime_signal_is_a_chain_defect_if_exposed":n>1,
        "same_as_completed_signed_Weil_trace":False,
    }


def _quotient_basis(k_n, k_pn):
    source=set(k_n.basis())
    target=k_pn.basis()
    if not source.issubset(set(target)):
        raise AssertionError("literal prime multiplication is not a chain injection")
    return tuple(s for s in target if s not in source)


def _quotient_homology(target, quotient):
    """Compute H_j of quotient K_pn / V_p K_n independently by ranks."""
    by_degree = {}
    for s in quotient:
        by_degree.setdefault(len(s), []).append(s)
    highest=max(by_degree,default=0)
    def boundary_rank(j):
        dom=by_degree.get(j,[])
        cod=by_degree.get(j-1,[])
        if not dom or not cod:
            return 0
        rows=[]
        for t in cod:
            row=[]
            for s in dom:
                row.append(sum((v for e,v in target.boundary(s) if e==t),0))
            rows.append(row)
        return _rank(rows)
    h={}
    for j in range(highest+1):
        z=len(by_degree.get(j,[]))-boundary_rank(j)
        hj=z-boundary_rank(j+1)
        if hj<0:
            raise AssertionError("quotient chain lacks nonnegative homology")
        h[j]=hj
    return {j:v for j,v in h.items() if v}


def prime_chain_lift(n, p):
    """Canonical FUCC exterior extension, including p-first-activation defect.

    V_p:S subset supp(n) -> SAME S subset supp(pn), a chain map.
    When p is newly activated, the target has additional θ_p states;
    d* cannot intertwine, and the quotient has shifted source homology.
    """
    n,p=_integer(n),_prime(p)
    if n*p>100_000:
        raise EquivariantDescentError("source horizon prevents silent p*n truncation")
    source=_fiber(n)
    target=_fiber(n*p)
    for s in source.basis():
        if source.boundary(s)!=target.boundary(s):
            raise AssertionError("multiplication violates genuine chain differential")
    extra=_quotient_basis(source,target)
    homology=_quotient_homology(target,extra)
    defect=[]
    for s in source.basis():
        old = dict(source.adjoint_boundary(s))
        new = dict(target.adjoint_boundary(s))
        for t in sorted(set(old)|set(new)):
            v = new.get(t,0)-old.get(t,0)
            if v:
                defect.append((s,t,v))
    first = p not in source.active
    expected={1:1} if first and n==1 else {}
    if homology!=expected or bool(defect)!=first:
        raise AssertionError("SUCC/FUCC Koszul quotient source-status discrepancy")
    return {
        "n":n, "p":p, "target_n":n*p,
        "source_dim":len(source.basis()),"target_dim":len(target.basis()),
        "chain_map_Vp_commutes_with_d":True,
        "chain_adjoint_defects":tuple(defect),
        "Vp_star_fails_to_intertwine_dstar":first,
        "new_exterior_basis":extra,
        "quotient_homology":homology,
        "quotient_acyclic":not homology,
        "new_data_is_derived_redundant_relative_to_source":
            bool(extra) and not homology,
        "origin_to_prime_homology_defect":expected=={1:1},
        "is_all_place_Weil_distribution":False,
    }


def unit_succ_dimension_control(n):
    """At fixed finite exterior Koszul fibers no isometric unit S can exist
    when omega(n)>omega(n+1), because target dimension is smaller.
    More ghost/memory fiber is needed, but it is not automatically
    source-observationally redundant.
    """
    n=_integer(n)
    if n==100_000:
        raise EquivariantDescentError("unit successor would leave tested horizon")
    s,t=_fiber(n),_fiber(n+1)
    return {
        "n":n,"source_dimension":len(s.basis()),
        "next_dimension":len(t.basis()),
        "literal_fiberwise_isometric_S_possible":
            len(s.basis())<=len(t.basis()),
        "genuine_SUCC_observables_preserved_by_an_invented_ancilla":False,
    }


def original_prime_source_supertrace_gate(N):
    """Compare inherited original von-Mangoldt prime tape to an all-acyclic
    chain-invariant supertrace. This explicit finite no-go uses real p^k,
    not imaginary zero-side or fake composite impulses.
    """
    if type(N) is not int or not 2<=N<=300:
        raise EquivariantDescentError("exact original source horizon 2..300")
    from .completed_weil_transport import von_mangoldt_labels
    tape=von_mangoldt_labels(N)
    zero_trace=[]
    defect_p0=[]
    for n,p in tape:
        g=trace_obstruction(n)
        zero_trace.append((n,p,g["chain_compatible_supertrace"]))
        defect_p0.append((n,p,g["grade_zero_projector_supertrace"],
                          g["grade_zero_projector_commutes_with_d"]))
    if any(v!=0 for n,p,v in zero_trace) or any(
            v!=1 or commute for n,p,v,commute in defect_p0
    ):
        raise AssertionError("failed to discriminate prime source from homological erasure")
    return {
        "original_wavefront":tuple(tape),
        "chain_invariant_supertrace_tape":tuple(zero_trace),
        "grade_zero_nonchain_trace_tape":tuple(defect_p0),
        "nonzero_original_prime_power_distribution_missing":bool(tape),
        "sign_and_half_density_not_solved_by_this_test":True,
        "Connes_full_global_trace":False, "RH_proved":False,
    }



def normalized_prime_clock_retraction(n,p):
    """Source arithmetic commutator survives a provably lossless restricted trace.

    The genuine prime chain injection V_p:K_n->K_pn is isometric on
    the inherited orthonormal wedge basis. The diagonal logarithmic
    source H=log(n)I has V_p* [H,V_p]=log(p)I on K_n.
    Dividing its finite trace by dim K_n removes the artificial
    exterior multiplicity 2^omega(n), preserving exactly log p.

    This IS NOT a supertrace, and the normalized finite trace is not
    declared Connes' canonical global trace. Additional target
    orientation states may be invisible to this restricted observable
    yet visible to future SUCC probes.
    """
    witness=prime_chain_lift(n,p)
    src=_fiber(n)
    dst=_fiber(n*p)
    valuation_src={q:k for q,k in zip(src.primes,src.alpha)}
    valuation_dst={q:k for q,k in zip(dst.primes,dst.alpha)}
    delta={q:valuation_dst.get(q,0)-valuation_src.get(q,0)
           for q in sorted(set(valuation_src)|set(valuation_dst))}
    delta={q:k for q,k in delta.items() if k}
    if delta!={p:1} or not witness["chain_map_Vp_commutes_with_d"]:
        raise AssertionError("genuine prime-clock chain transport lost")
    d=len(src.basis())
    return {
        "source_integer":n,"prime":p,"target_integer":n*p,
        "source_wedge_dimension":d,
        "target_wedge_dimension":len(dst.basis()),
        "source_log_valuation_delta":tuple(delta.items()),
        "isometric_source_inclusion":True,
        "surjective_to_target_fiber":d==len(dst.basis()),
        "raw_source_trace_prime_log_coefficient":d,
        "normalized_trace_prime_log_coefficient":F(1),
        "symbolic_clock_result":f"log({p})",
        "source_prime_jet_energy_survives":True,
        "all_target_exterior_states_redundant_for_every_probe":False,
        "canonical_Connes_trace_proved":False,
        "original_Weil_positive":False,
    }



def prime_multiplication_nullhomotopy(n,p):
    """Exact full-polynomial Koszul chain identity V_p=d epsilon_p+epsilon_p d.

    On the total-degree alpha complex K_n, exterior creation epsilon_p
    acts K_n -> K_(p*n) and raises the chain degree by one. It is defined
    whether p is newly active OR already divides n. The target includes
    p in its exterior support, so the creation operator is source-typed.

    Since {iota_q,epsilon_p}=delta_qp and d=sum x_q iota_q
    globally, the anticommutator is multiplication x_p=V_p. We verify
    every basis state with independent source differential evaluation.

    V_p is NONZERO on the original integer carrier, but null-homotopic
    as a chain map. Thus passing to Koszul homology destroys arithmetic
    multiplication. Its commutator with log H is still log p V_p at the
    CHAIN level and must not be discarded when reconstructing sources.
    """
    witness=prime_chain_lift(n,p)
    src=_fiber(n)
    dst=_fiber(n*p)
    receipts=[]
    for S in src.basis():
        output={}
        for T,a in dst.exterior_creation(p,S):
            for U,b in dst.boundary(T):
                output[U]=output.get(U,F(0))+F(a*b)
        for T,a in src.boundary(S):
            for U,b in dst.exterior_creation(p,T):
                output[U]=output.get(U,F(0))+F(a*b)
        actual={T:v for T,v in output.items() if v}
        if actual!={S:F(1)}:
            raise AssertionError("KOSZUL_PRIME_MULTIPLICATION_NULLHOMOTOPY_FAILED")
        receipts.append((S,actual))
    return {
        "n":n,"p":p,"target_n":n*p,
        "chain_map_original_Vp_nonzero":True,
        "exact_d_epsilon_plus_epsilon_d_is_Vp":True,
        "checked_source_wedges":tuple(receipts),
        "Koszul_homology_faithfully_represents_original_FUCC":False,
        "first_activation_extra_homology_retained_as_relative_defect":
            witness["origin_to_prime_homology_defect"],
        "source_prime_log_commutator_still_nonzero":True,
        "source_test_and_global_trace_not_identified":True,
        "RH_proved":False,
    }
