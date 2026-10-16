"""A precise POSITIVITY growth gate for recursively modeled source observers.

Two logically distinct results:
(1) A compatible inductive system of PSD finite Hermitian source forms
    defines a PSD algebraic union form; a continuous form extends PSD to
    the dense global test space. Conversely a strictly negative GLOBAL
    witness in that topology is detected on a finite source-test stage.
(2) Finite source Fourier/reconstruction compatibility does not give
    cross-block Schur positivity. Stage self-signs and source-identity are
    different obligations; no bounded spectrum gap is assumed.

Implementation: exact finite symmetric Q matrices only (calibration).
Analytic global statement in OBSERVER_TATE_ATOMIC_RECONSTRUCTION.md.
Actual Suzuki source intervals come exclusively from SHA-pinned originals.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .recursive_operator_gluing import (
    CouplingError, principal_minors, psd, certify_schur
)


class GrowthGateError(ValueError):
    """False source-coherence, wrong quadratic domain or typed block."""


def _rat(v) -> Q:
    if type(v) not in (int,Q):
        raise GrowthGateError("Only exact rational finite source data")
    return Q(v)


def _gram(A):
    if (type(A) is not tuple or not 1<=len(A)<=6 or
            any(type(row) is not tuple or len(row)!=len(A) for row in A)):
        raise GrowthGateError("Exact 1..6 dimensional square source Gram required")
    out=tuple(tuple(_rat(v) for v in row) for row in A)
    if any(out[i][j]!=out[j][i] for i in range(len(out)) for j in range(i)):
        raise GrowthGateError("Source Gram must be real symmetric")
    return out


@dataclass(frozen=True)
class FiniteGrowthReceipt:
    dimension: int
    signed_source_scope: str
    coherent_with_previous_stage: bool
    each_component_positive: bool
    cross_interactions_positive: bool
    negative_principal_witness: tuple[int,...] | None
    negative_principal_determinant: Q | None
    global_infinite_source_proved_positive: bool = False
    RH_proved: bool = False


def certify_finite_growth(
        previous: tuple[tuple[int|Q,...],...],
        cross: tuple[int|Q,...], new_diagonal: int|Q,
        *, scope: str="DECLARED_FINITE_RATIONAL_SOURCE_NOT_WEIL") -> FiniteGrowthReceipt:
    """Canonical stage n -> n+1, all exact principal minors.

    G_new=[[G_old,c],[c*,d]], G_old must genuinely match source
    restriction and be PSD. Even if both old G and d are PSD, positive
    extension requires a Schur/range condition on c. Returns exact
    offending principal minor; absence of a finite witness is not an
    all-future global certificate.
    """
    A=_gram(previous)
    n=len(A)
    if (type(cross) is not tuple or len(cross)!=n or
            type(scope) is not str or not scope):
        raise GrowthGateError("Source cross block has wrong arity/identity")
    c=tuple(_rat(v) for v in cross)
    d=_rat(new_diagonal)
    if not psd(A):
        raise GrowthGateError("Previous source stage is not PSD")
    M=tuple(A[i]+(c[i],) for i in range(n))+(c+(d,),)
    errors=tuple((idx,det) for idx,det in principal_minors(M) if det<0)
    return FiniteGrowthReceipt(
        n+1,scope,True,d>=0,len(errors)==0,
        errors[0][0] if errors else None,
        errors[0][1] if errors else None)


def exact_scalar_schur_source_gate(a:int|Q,b:int|Q,d:int|Q)->dict:
    """Complete 1+1 PSD theorem and a rational explicit negative direction.

    If a>0: G>=0 iff d-b²/a>=0; negative direction (-b/a,1)
    realizes the exact Schur value otherwise.
    If a=0: source PSD requires b=0, d>=0. b!=0 is a
    RANGE-INCLUSION defect; an explicit negative direction is given.
    """
    A,B,D=_rat(a),_rat(b),_rat(d)
    if A<0:
        witness=(Q(1),Q())
        defect=A
        status="OLD_STAGE_NEGATIVE"
    elif A==0 and B:
        witness=(-Q(abs(D)+1,B),Q(1))
        defect=A*witness[0]**2+2*B*witness[0]*witness[1]+D
        status="ZERO_RANGE_CROSS_OBSTRUCTION"
    elif A==0:
        witness=(Q(),Q(1)) if D<0 else None
        defect=D if D<0 else Q()
        status="NEW_DIAGONAL_NEGATIVE" if D<0 else "SINGULAR_RANGE_COMPATIBLE"
    else:
        schur=D-B*B/A
        witness=(-B/A,Q(1)) if schur<0 else None
        defect=schur
        status="NEGATIVE_SCHUR_CROSS" if schur<0 else "POSITIVE_GROWTH"
    if witness is not None:
        q=A*witness[0]**2+2*B*witness[0]*witness[1]+D*witness[1]**2
        if q>=0:
            raise ArithmeticError("Explicit negative cross certificate forged")
    return {"a":A,"b":B,"d":D,"status":status,
            "PSD":witness is None,
            "explicit_negative_direction":witness,
            "signed_source_value":defect,
            "rank_or_schur_gate_required":True,
            "source_is_actual_zeta":False,"RH_proved":False}


def checked_finite_gram_tower(
        stages: tuple[tuple[tuple[int|Q,...],...],...]) -> dict:
    """Verify every principal minor and source restriction of each stage.

    No finite tower is called a proof about its unseen stages. A theorem
    about an INFINITE filtered/cofinal compatible tower is separate.
    """
    if type(stages) is not tuple or not 1<=len(stages)<=6:
        raise GrowthGateError("Finite growth history 1..6 stages required")
    previous=None
    methods=0
    for stage in stages:
        G=_gram(stage)
        if previous is not None:
            if len(G)<=len(previous) or tuple(tuple(row[:len(previous)])
                              for row in G[:len(previous)])!=previous:
                raise GrowthGateError("New source model changed an established old pairing")
        negatives=tuple((ix,d) for ix,d in principal_minors(G) if d<0)
        methods+=2**len(G)-1
        if negatives:
            return {"prefixes_verified_before_failure":methods-(2**len(G)-1),
                    "first_negative_stage_dimension":len(G),
                    "negative_principal":negatives[0],
                    "finite_stage_failure":True,
                    "global_positive_proved":False,
                    "RH_proved":False}
        previous=G
    return {"finite_levels":len(stages),"last_dimension":len(previous),
            "checked_principal_minors":methods,
            "all_supplied_source_stages_PSD":True,
            "entire_infinite_tower_verified":False,
            "global_positive_proved":False,
            "RH_proved":False}


def unseen_sign_mutant(verified_prefix_size:int)->dict:
    """Finite reports cannot distinguish a late negative global form.

    I and I-2|e_M><e_M| agree on the first N coordinate observers
    whenever M>N. Returns a FINITE explicit first failure at N+1.
    This is the existing SUCC IdealHard IH-01 countermodel reused as
    a calibration, not claimed to be a negative original-zeta witness.
    """
    if type(verified_prefix_size) is not int or not 1<=verified_prefix_size<=6:
        raise GrowthGateError("Finite tested prefix 1..6")
    n=verified_prefix_size
    old=tuple(tuple(Q(int(i==j)) for j in range(n)) for i in range(n))
    bad=certify_finite_growth(old,tuple(Q() for _ in range(n)),Q(-1))
    if bad.cross_interactions_positive:
        raise AssertionError("Future negative direction falsely certified")
    return {"identical_on_first":n,"new_negative_at":n+1,
            "previous_all_PSD":True,"first_negative_principal":bad.negative_principal_witness,
            "two_global_sources_indistinguishable_on_tested_prefix":True,
            "original_Weil_negative_witness":False,"RH_proved":False}


def true_suzuki_anchored_two_point_source(x:int|Q,y:int|Q,J:int=128)->dict:
    """Real original pinned Suzuki signed Gram 2x2, OUTWARD Fractions.

    Reuses source_weil_hierarchy.py via suzuki_legendre_source._pinned_source
    (Git blob SHA), not a made-up positive covariance. Its original
    infinite Gamma potential lies below finite-J g_J by at most
    source.gamma_tail(J). Domain max(|x|,|y|,|x-y|)<=2.
    A single 2x2 certificate is NOT a proof for all test functions.
    """
    if (type(x) not in (int,Q) or type(y) not in (int,Q)
            or type(J) is not int or not 1<=J<=128):
        raise GrowthGateError("Exact original source anchored points and truncation")
    from .suzuki_legendre_source import _pinned_source
    src=_pinned_source()
    xx,yy=Q(x),Q(y)
    radius=max(abs(xx),abs(yy),abs(xx-yy))
    if not xx or not yy or xx==yy or radius>2:
        raise GrowthGateError("Nonzero distinct points on original signed source window")
    if Q(4*J-3,2)*radius>128:
        raise GrowthGateError("Pinned original source exp evaluator exceeds its 128-domain")
    def interval(t):
        if t==0:
            return Q(),Q()
        I=src.screw_interval(abs(t),J)
        return I.lo-src.gamma_tail(J),I.hi
    def K(a,b):
        if not a or not b:return Q(),Q()
        cross=interval(a-b);la=interval(a);lb=interval(b)
        return cross[0]-la[1]-lb[1],cross[1]-la[0]-lb[0]
    xxI,yyI,xyI=K(xx,xx),K(yy,yy),K(xx,yy)
    product=(min(a*b for a in xxI for b in yyI),
             max(a*b for a in xxI for b in yyI))
    square=(Q(),max(xyI[0]**2,xyI[1]**2)) if xyI[0]<=0<=xyI[1] else \
        (min(xyI[0]**2,xyI[1]**2),max(xyI[0]**2,xyI[1]**2))
    det=(product[0]-square[1],product[1]-square[0])
    pos=xxI[0]>0 and yyI[0]>0 and det[0]>0
    neg=xxI[1]<0 or yyI[1]<0 or det[1]<0
    if pos and neg:raise ArithmeticError("Authentic Suzuki interval signs conflict")
    return {"points":(xx,yy),"J":J,"source":"SHA_PINNED_AUTHENTIC_SIGNED_WEIL_SUZUKI",
            "Kxx":xxI,"Kyy":yyI,"Kxy":xyI,"determinant":det,
            "certified_finite_sign":"POSITIVE" if pos else "NEGATIVE" if neg else "AMBIGUOUS",
            "global_all_test_sign_proved":False,
            "RH_proved":False}


def dense_smooth_source_gate() -> dict:
    """Theoretical separation of finite-witness falsifiability vs proof.

    Rational translates/rescalings of one normalized Cc∞ bump are LF-dense
    in Cc∞(R) using convolution/approximate identities, then rational
    Riemann sums. For a CONTINUOUS hermitian Weil form Q, Q(f)<0 yields
    finite rational dictionary v with Q(v)<0 (strict open condition).
    Nonnegative Q on EACH finite dictionary span would also imply global
    sign, but *checking any finite prefix* cannot certify later spans.
    """
    return {"test_topology":"C_c_infinity_LF_continuous_Weil_distribution",
            "dictionary":"normalized_smooth_rational_bump_translates_scales",
            "countable_LF_dense_dictionary":"CLASSICAL_DENSITY_THEOREM",
            "negative_real_witness_implies_finite_rational_probe":"CONDITIONAL_ON_CONTINUITY",
            "finite_prefix_positive_implies_RH":False,
            "all_stages_positive_and_source_identified_implies_RH":
               "CONDITIONAL_CLASSICAL_WEIL_CRITERION",
            "ambient_operator_bounded_L2_assumed":False,
            "RH_proved":False}
