"""Finite-to-global uniform Hilbert contraction gluing: exact-source type firewall.

Classical theorem (written in FIELD_LIMIT_TRICHOTOMY.md):
For fixed real/complex Hilbert spaces H+,H- and prescribed vectors
(v_i,w_i), a global contraction T:H+->H- with Tv_i=w_i for ALL indices
exists IFF every FINITE collection of those equations admits a
contraction. Proof: unit ball B(H+,H-) WOT compact, every constraint
Tv_i=w_i WOT closed, finite intersection property. It also follows
algebraically from all-finite norm dominance on the span.

Uniform contractive bound and a common source Hilbert carrier are
ESSENTIAL. If finite models use changing Hilbert presentations, one
must first construct coherent source-preserving transports.
This theorem does NOT prove original Suzuki/Weil finite dominance!
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .recursive_operator_gluing import (
    determinant, inverse, product, psd, principal_minors,transpose
)


class ContractiveDescentError(ValueError):
    """Forged finite Hilbert source, incompatible cross norm or nonuniform chart."""


def _r(v) -> Q:
    if type(v) not in (int,Q):
        raise ContractiveDescentError("Only exact rational finite feature coordinates")
    return Q(v)


def _vectors(V):
    if (type(V) is not tuple or not 1<=len(V)<=6
            or type(V[0]) is not tuple or not 1<=len(V[0])<=6
            or any(type(v) is not tuple or len(v)!=len(V[0]) for v in V)):
        raise ContractiveDescentError("Exact nonempty finite feature family, dimensions<=6")
    return tuple(tuple(_r(x) for x in v) for v in V)


def _dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q())


def _gram(V):
    return tuple(tuple(_dot(v,w) for w in V) for v in V)


def _subtract(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(len(A))) for i in range(len(A)))


def _columns_to_rows(columns,dimension):
    if not columns:
        return tuple(tuple() for _ in range(dimension))
    return tuple(tuple(col[j] for col in columns) for j in range(dimension))


@dataclass(frozen=True)
class FiniteContractionReceipt:
    source: str
    equations: int
    positive_dimension: int
    negative_dimension: int
    positive_gram_psd: bool
    negative_gram_psd: bool
    signed_gram_psd: bool
    negative_principal_witness: tuple[tuple[int,...],Q] | None
    rational_canonical_operator: tuple[tuple[Q,...],...] | None
    exact_source_equations_verified: bool
    exact_operator_contractivity_verified: bool
    global_infinite_source_certified: bool = False
    RH_proved: bool = False


def exact_finite_feature_contraction(
        positive_vectors: tuple[tuple[int|Q,...],...],
        negative_vectors: tuple[tuple[int|Q,...],...],
        *,source:str="SYNTHETIC_RATIONAL_FEATURES_NOT_ORIGINAL_SUZUKI"
        ) -> FiniteContractionReceipt:
    """Exact Gram dominance and a canonical minimal rational contraction.

    For a list of source equations T v_i = w_i, let G+=V*V and
    G-=W*W. A contraction exists iff G+-G- >=0 as a quadratic form.
    On its positive-feature span the map is UNIQUE when it exists,
    even if the coordinates of the v_i are dependent.

    Extend by zero on orthocomplement: if B is independent source
    v-column basis, T=W_B (B*B)^(-1) B*, rational. Verify ALL input
    equations and I-T*T>=0 EXACTLY. This is a FINITE model tool only,
    not an original-source signed zeta sign certificate.
    """
    pos=_vectors(positive_vectors)
    neg=_vectors(negative_vectors)
    if len(pos)!=len(neg) or type(source) is not str or not source:
        raise ContractiveDescentError("Matched source-indexed feature vectors required")
    plus=_gram(pos)
    minus=_gram(neg)
    sign=_subtract(plus,minus)
    if not psd(plus) or not psd(minus):
        raise ArithmeticError("Euclidean feature Grams must each be PSD")
    failures=tuple((inds,value) for inds,value in principal_minors(sign) if value<0)
    if failures:
        return FiniteContractionReceipt(source,len(pos),len(pos[0]),len(neg[0]),
            True,True,False,failures[0],None,False,False)
    source_bases=[]
    for i,v in enumerate(pos):
        subset=tuple(pos[j] for j in source_bases+[i])
        if determinant(_gram(subset))>0:
            source_bases.append(i)
    positive_dim=len(pos[0])
    negative_dim=len(neg[0])
    if source_bases:
        B=tuple(pos[i] for i in source_bases)
        U=tuple(neg[i] for i in source_bases)
        M=transpose(_columns_to_rows(B,positive_dim))
        G=_gram(B)
        Ginv=inverse(G)
        # Rows of U are column-transposes; Q×rank, B matrix rank×P
        WB=_columns_to_rows(U,negative_dim)
        Op=product(product(WB,Ginv),M)
    else:
        Op=tuple(tuple(Q() for _ in range(positive_dim))
                 for _ in range(negative_dim))
    for v,w in zip(pos,neg):
        actual=tuple(_dot(row,v) for row in Op)
        if actual!=w:
            raise ArithmeticError("Source equations incompatible with claimed Gram domination")
    # I_p - T* T positive: an EXACT operator norm <=1 certificate.
    OpT=transpose(Op)
    OpTOp=product(OpT,Op)
    gap=tuple(tuple(Q(int(i==j))-OpTOp[i][j] for j in range(positive_dim))
              for i in range(positive_dim))
    if not psd(gap):
        raise ArithmeticError("Original finite Hilbert map is not contractive")
    return FiniteContractionReceipt(source,len(pos),positive_dim,negative_dim,
        True,True,True,None,Op,True,True)


def unbounded_finite_growth_obstruction(depth:int)->dict:
    """Every finite source system has a BOUNDED solution, but no UNIFORM bound.

    On Hilbert l2, constraints T e_n = (n+1)e_n for n>=1 have
    finite-prefix solutions diag(2,...,N+1,0,0,...) of norm N+1.
    For ALL n any linear extension T has ||T||>=n+1, so no bounded
    T exists. This is a genuine cross-stage *uniformity* obstruction.
    No false claim that it violates contraction compactness: finite
    prefix already fails norm<=1 at its first nontrivial stage.
    """
    if type(depth) is not int or not 1<=depth<=1000000:
        raise ContractiveDescentError("Exact positive finite norm-growth stage")
    return {"finite_constraints":depth,
            "optimal_prefix_operator_norm":depth+1,
            "one_bounded_operator_per_finite_prefix":True,
            "uniform_operator_bound_across_all_stages":False,
            "global_bounded_operator_exists":False,
            "fixed_hilbert_source_spaces":"l2_to_l2",
            "field":"FUCKED_FOR_BOUNDED_GLOBAL_MAP_WITHOUT_UNIFORM_GROWTH_BOUND",
            "RH_proved":False}


def compact_operator_constraint_lift_theorem() -> dict:
    """Classical WOT compactness theorem, properly source-typed.

    If the source feature vectors v_i∈H+,w_i∈H- share FIXED Hilbert
    spaces and EVERY finite constraint T v_i=w_i is feasible with
    one UNIFORM bound ||T||<=1, then all constraints are realized
    by one T in the WOT-compact contraction unit ball.

    A single positive finite Gram check does NOT establish the ALL
    FINITE SUBSETS premise. For actual Suzuki K+=K+-K-, that premise
    is exactly global Weil positivity/RH in another representation.
    """
    return {
        "source_spaces":"ONE_FIXED_PAIR_OF_HILBERT_SPACES",
        "compact_object":"UNIT_BALL_B(Hplus,Hminus)_WEAK_OPERATOR_TOPOLOGY",
        "required_premise":"EVERY_FINITE_SUBSET_HAS_NORM_LE_1_SOLUTION",
        "each_exact_constraint_WOT_closed":True,
        "global_solution":"CLASSICAL_COMPACTNESS_CONDITIONAL_THEOREM",
        "canonical_restriction_to_generated_positive_span":
            "UNIQUE_IF_SOLUTION_EXISTS",
        "global_operator_algorithm_from_finite_feasibility":
            "NOT_PROVIDED",
        "actual_Suzuki_all_finite_constraints_verified":False,
        "RH_proved":False,
    }


def true_source_suzuki_contractivity_wall()->dict:
    """Use SUCC's actual K+/K- status, not synthetic rational fit."""
    return {
        "original_completed_weil":"SIGNED_TRUE_ZETA_SOURCE",
        "authentic_Suzuki_source_relation":"K_g=K_plus-K_minus",
        "fixed_interval_Hilbert_features":"APOLLO_PREEXISTING_SOURCE_CONSTRUCTION",
        "prime_activation_chart_issue":
            "POSITIVE_NEGATIVE_FEATURES_CHANGE_BY_NEUTRAL_PAIRS",
        "uniform_source_transports_for_all_a_proved":False,
        "all_finite_source_difference_grams_PSD":False,
        "WOT_compactness_can_replace_source_sign_proof":False,
        "RH_proved":False,
    }
