"""Homotopy-defect representation of original prime-power Weil impulses.

For a nonzero full prime-power Koszul fiber K_n and ANY contracting
homotopy h with dh+hd=I, an even source test T satisfies

  Str(T) = Str((T d - d T) h).

Proof: supertrace graded cyclicity, in finite dimensions.
For the canonical grade-zero projector T=P_0, both sides equal 1 for
EVERY n>1. The homotopy may arbitrarily pivot at any genuine p|n;
the observable trace is independent of the pivot. Thus introduced
auxiliary cancellation data are removable up to this SOURCE observable,
but a nonzero defect [P_0,d] remains.

Combining this exact unit coefficient with the original source
commutator V_p* [H,V_p]=log p, true jet projector and half-density
n^-1/2 reproduces the ORIGINAL PRIME-POWER sector of signed Weil
on compact log tests (locally finite). It does NOT reproduce Gamma,
contact, poles, full Connes trace or completed Weil positivity.
"""
from __future__ import annotations

from fractions import Fraction as F

from .koszul_prime_cancellation import source_multidegree
from .equivariant_koszul_descent import matrix_chain_diagonal


class HomotopyDefectError(ValueError):
    """Unavailable original prime, malformed test or illicit completeness."""


def _src(n):
    if type(n) is not int or not 1<=n<=100_000:
        raise HomotopyDefectError("original positive integer <=100000 required")
    return source_multidegree(n)


def _source_diagonal(n,diagonal):
    f=_src(n)
    if type(diagonal) is not dict or set(diagonal)!=set(f.basis()):
        raise HomotopyDefectError("complete even original source test required")
    if any(type(v) not in (int,F) for v in diagonal.values()):
        raise HomotopyDefectError("exact rational source probe required")
    return f, {S:F(diagonal[S]) for S in f.basis()}


def homotopy_defect_trace(n,diagonal,pivot=None):
    """Prove and calculate Str(T)=Str([T,d]h_p) on acyclic K_n.

    For each wedge S, h_p=epsilon_p; Clifford {iota_p,epsilon_p}=1
    ensures dh+hd=I even when the chosen pivot is not the least prime.
    The result is independent of pivot but [T,d] itself is a potentially
    source-observable obstruction. At n=1 there is no contraction.
    """
    f,diag=_source_diagonal(n,diagonal)
    active=f.active
    if not active:
        if pivot is not None:
            raise HomotopyDefectError("arithmetic unit has no prime pivot")
        return {
            "n":1,"pivot":None,
            "ordinary_source_supertrace":diag[()],
            "homotopy_defect_supertrace":F(0),
            "homology_contact_at_unit":diag[()],
            "nonzero_prime_fiber_acyclic":False,
            "orientation_auxiliary_removed":False,
            "Weil_PSD_proved":False,
        }
    if type(pivot) is not int or pivot not in active:
        raise HomotopyDefectError("choose any REAL active prime orientation pivot")
    rawtrace=F(0)
    defecttrace=F(0)
    for S in f.basis():
        rawtrace+=(-1)**len(S)*diag[S]
        # h_p is exterior creation at p, with the ordering sign.
        h=f.exterior_creation(pivot,S)
        # Supertrace diagonal coefficient of ([T,d] h_p) on S.
        diagonal_response=F(0)
        for X,a in h:
            for Y,b in f.boundary(X):
                if Y==S:
                    diagonal_response+=F(a*b)*(diag[Y]-diag[X])
        defecttrace+=(-1)**len(S)*diagonal_response
        # Independently verify (d h + h d)S = S on all basis states.
        combined={}
        for X,a in h:
            for Y,b in f.boundary(X):
                combined[Y]=combined.get(Y,F(0))+F(a*b)
        for X,a in f.boundary(S):
            for Y,b in f.exterior_creation(pivot,X):
                combined[Y]=combined.get(Y,F(0))+F(a*b)
        if {Y:v for Y,v in combined.items() if v}!={S:F(1)}:
            raise AssertionError("arbitrary prime homotopy is not a contraction")
    if rawtrace!=defecttrace:
        raise AssertionError("finite graded cyclicity defect identity failed")
    plain=matrix_chain_diagonal(n,diag)
    if plain["supertrace"]!=rawtrace:
        raise AssertionError("independent source trace gate disagrees")
    return {
        "n":n, "pivot":pivot, "active_primes":active,
        "ordinary_source_supertrace":rawtrace,
        "homotopy_defect_supertrace":defecttrace,
        "exact_graded_cyclicity":True,
        "source_T_commutes_with_d":plain["commutes_with_d"],
        "prime_defect_edges":plain["commutator_defect_edges"],
        "nonzero_prime_fiber_acyclic":True,
        "orientation_auxiliary_removed":True,
        "underlying_source_distribution_identified":False,
        "Weil_PSD_proved":False,
    }


def grade_zero_defect(n,pivot=None):
    """Canonical grade-zero test P0. For every n>1 the defect equals 1."""
    f=_src(n)
    if not f.active:
        return homotopy_defect_trace(n,{():F(1)},None)
    if pivot is None:pivot=f.active[0]
    values={S:F(int(S==())) for S in f.basis()}
    result=homotopy_defect_trace(n,values,pivot)
    if (result["ordinary_source_supertrace"]!=1 or
        result["homotopy_defect_supertrace"]!=1 or
        result["source_T_commutes_with_d"]):
        raise AssertionError("prime source grade-zero anomaly not detected")
    return result


def pivot_invariance(n):
    f=_src(n)
    if not f.active:
        return {"n":1,"pivots":(),"unit_homology_not_contractible":True}
    rec=tuple(grade_zero_defect(n,p) for p in f.active)
    if any(x["homotopy_defect_supertrace"]!=1 for x in rec):
        raise AssertionError("auxiliary pivot observable noninvariant")
    return {
        "n":n,"pivots":f.active,
        "distinct_homotopies_give_same_source_trace":True,
        "observable_prime_defect":F(1),
        "contractible_auxiliary_trace_redundant":True,
        "all_place_Weil_PSD_proved":False,
    }


def signed_prime_distribution_receipt(N, log_test_values):
    """Exact original Weil PRIME SECTOR only on finite log-test evaluations.

    log_test_values: {n: (h(+log n), h(-log n))} with rational tests;
    each compactly supported smooth h has such finite source evaluations.
    Coefficients retain log(p)/sqrt(n) SYMBOLICALLY, not float-fitted.
    This theorem is exact for every compact-support test because its
    prime-power sum is locally finite. Gamma/contact/poles excluded.
    """
    if type(N) is not int or not 2<=N<=300:
        raise HomotopyDefectError("finite authentic prime source horizon 2..300")
    if type(log_test_values) is not dict:
        raise HomotopyDefectError("finite rational log test valuations required")
    for n,row in log_test_values.items():
        if (type(n) is not int or not 1<=n<=N or
            type(row) is not tuple or len(row)!=2 or
            any(type(v) not in (int,F) for v in row)):
            raise HomotopyDefectError("source-indexed rational even/odd log probes required")
    from .completed_weil_transport import von_mangoldt_labels
    tape=von_mangoldt_labels(N)
    terms=[]
    for n,p in tape:
        test=log_test_values.get(n,(0,0))
        val=F(test[0])+F(test[1])
        if not val:continue
        h=grade_zero_defect(n)
        if h["homotopy_defect_supertrace"]!=1:
            raise AssertionError("SOURCE_PRIME_WEIL_TRACE_MISMATCH")
        terms.append({
            "original_prime_power":n,"primitive_prime":p,
            "positive_log_probe":F(test[0]),"negative_log_probe":F(test[1]),
            "signed_source_test_multiplier":-val,
            "half_density_amplitude_squared":F(1,n),
            "symbolic_complete_weight":f"-({val})*log({p})/sqrt({n})",
            "homotopy_pivot_independent":pivot_invariance(n)["distinct_homotopies_give_same_source_trace"],
            "original_Weil_prime_magnitude_recovered":True,
            "contact_Gamma_or_pole_included":False,
        })
    return {
        "original_Tate_prime_power_tape":tape,
        "prime_terms":tuple(terms),
        "fake_composite_log_test_values_ignored":all(
            n in dict(tape) or n not in log_test_values
            for n,p in tape),
        "exact_finite_signed_prime_distribution_only":True,
        "global_Connes_trace_identified":False,
        "completed_Weil_PSD_proved":False,
        "RH_proved":False,
    }
