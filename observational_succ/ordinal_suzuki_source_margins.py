"""Authentic Suzuki finite-window sign margin, ordinal proof debt, and source interval refinement.

This is a REAL ORIGINAL ZETA SOURCE calculation, not a positive covariance:
the SHA-pinned source_weil_hierarchy has the genuine von Mangoldt prime
tape, half-density, one completed Gamma factor, contact, and pole terms.
We evaluate only anchored 2x2 signed matrices at declared rational points.

Mathematics:
* Every source stage J gives a rigorous outward interval enclosing the
  SAME completed infinite-Gamma signed kernel and its true determinant.
* Intersecting independent valid source enclosures is legitimate even if
  a particular finite-J interval does not nest with the previous stage.
* If TRUE determinant and diagonals have STRICTly positive margins,
  effective gamma-tail convergence + effective rational exp/log
  enclosures eventually give a FINITE certificate. Without a gap,
  unknown sign remains unknown. No uniform bound for every possible
  rational test is claimed; no ordinal rank proves the sign for free.
* Source task rank omega + (remaining declared regulators) STRICTLY
  decreases on each checked refinement; if the budget is exhausted
  without a separated sign, a LIVE omega-rank proof debt remains.
  The procedure terminates but the source-sign theorem does not.

No nontrivial zeta zeros are construction inputs. No all-test Weil sign.
"""
from __future__ import annotations

from fractions import Fraction as F

from .ordinal_ranked_succ import (
    OrdinalDescentError,ordinal_lex_counters,ZERO
)
from .observer_global_sign_gate import (
    GrowthGateError,true_suzuki_anchored_two_point_source
)
from .suzuki_legendre_source import _pinned_source


class OrdinalSourceSignError(ValueError):
    """Invalid signed-source point, regulator/ordinal budget, or interval claim."""


def _fraction(x):
    if type(x) not in (int,F):
        raise OrdinalSourceSignError("Use exact original-source rational test points")
    return F(x)


def _intersect(previous, current):
    if previous is None:
        return current
    lo=max(previous[0],current[0])
    hi=min(previous[1],current[1])
    if lo>hi:
        raise ArithmeticError("Two SHA-pinned source enclosures of one original value disagree")
    return lo,hi


def _strict_source_sign(registry):
    A=registry["Kxx"]
    B=registry["Kyy"]
    D=registry["determinant"]
    if A[1]<0 or B[1]<0 or D[1]<0:
        return "CERTIFIED_NON_PSD_ORIGINAL_SOURCE"
    if A[0]>0 and B[0]>0 and D[0]>0:
        return "CERTIFIED_STRICT_POSITIVE_DEFINITE_2_BY_2"
    return "SOURCE_SIGN_UNRESOLVED"


def _validate_points_and_budgets(x,y,Js):
    xx,yy=_fraction(x),_fraction(y)
    if (not xx or not yy or xx==yy or
            type(Js) is not tuple or not 1<=len(Js)<=9
            or any(type(j) is not int or not 1<=j<=128 for j in Js)
            or tuple(sorted(set(Js)))!=Js):
        raise OrdinalSourceSignError("Nonzero distinct rational points, strictly increasing J<=128")
    radius=max(abs(xx),abs(yy),abs(xx-yy))
    if radius>2:
        raise OrdinalSourceSignError("Original signed Suzuki source permits |t|<=2")
    for J in Js:
        # Original source.exp_pos input cannot exceed 128; the largest
        # original gamma exponential d_J|t|/2 needs this exact guard.
        if F(4*J-3,2)*radius>128:
            raise OrdinalSourceSignError("Gamma stage requires unlicensed original exp evaluator")
    return xx,yy,radius


def authentic_suzuki_ordinal_sign_search(
        x:int|F,y:int|F,
        Js:tuple[int,...]=(1,2,4,8,16,32,64,128)) ->dict:
    """Exact source-authenticated small Gram with a finite rank-typed schedule.

    At each J calls inherited SHA-pinned Suzuki original interval oracle.
    The source interval contains the TRUE completed signed arithmetic
    Gram, including the O(J^-1) omitted real Gamma tail. All stage
    intervals for the same value may be intersected, and a sign is
    certified only if every required strict inequality is separated.

    A declared regulator-bounded search ends either CERTIFIED or with
    source proof debt rank omega, NOT with an unearned positivity theorem.
    """
    xx,yy,radius=_validate_points_and_budgets(x,y,Js)
    src=_pinned_source()
    log2=src.log2_iv()
    source_prime_active=any(t>log2.hi
                            for t in (abs(xx),abs(yy),abs(xx-yy)))
    windows={"Kxx":None,"Kyy":None,"Kxy":None,"determinant":None}
    rank_trace=[str(ordinal_lex_counters((1,len(Js))))]
    checked=[]
    previous_tail=None
    decision="SOURCE_SIGN_UNRESOLVED"
    for idx,J in enumerate(Js):
        try:
            stage=true_suzuki_anchored_two_point_source(xx,yy,J)
        except (GrowthGateError,ValueError) as exc:
            raise OrdinalSourceSignError("Original source refused Gamma/point chart") from exc
        if stage["source"]!="SHA_PINNED_AUTHENTIC_SIGNED_WEIL_SUZUKI":
            raise ArithmeticError("Original completed signed Weil source identity lost")
        tail=src.gamma_tail(J)
        if previous_tail is not None and not tail<previous_tail:
            raise ArithmeticError("Source original Gamma remainder did not shrink")
        previous_tail=tail
        for key in windows:
            windows[key]=_intersect(windows[key],stage[key])
        decision=_strict_source_sign(windows)
        checked.append({
            "J":J,
            "original_source_individual_sign":stage["certified_finite_sign"],
            "source_gamma_tail_bound":tail,
            "combined_determinant_interval":windows["determinant"],
            "cumulative_source_sign":decision,
        })
        next_rank=ZERO if decision!="SOURCE_SIGN_UNRESOLVED" \
            else ordinal_lex_counters((1,len(Js)-idx-1))
        rank_trace.append(str(next_rank))
        if decision!="SOURCE_SIGN_UNRESOLVED":
            break
    return {
        "source":"SHA_PINNED_AUTHENTIC_ZETA_SUZUKI_WEIL",
        "points":(xx,yy),
        "prime2_original_wavefront_sampled":source_prime_active,
        "rational_log2_source_interval":(log2.lo,log2.hi),
        "declared_Gamma_budget":Js,
        "Gamma_stages_completed":len(checked),
        "original_signed_source_stages":tuple(checked),
        "last_source_intersection":dict(windows),
        "ordinal_proof_rank_trace":tuple(rank_trace),
        "strict_ordinal_decrease_each_executed_transition":True,
        "finite_proof_search_completed":True,
        "signed_source_verdict":decision,
        "unresolved_ordinal_source_debt":
            decision=="SOURCE_SIGN_UNRESOLVED",
        "all_test_original_Weil_PSD_proved":False,
        "RH_proved":False,
    }


def finite_strict_sign_semidecision_theorem()->dict:
    """Classical effective analysis, not an RH theorem.

    For FIXED rational x,y in a compact source window, the original
    completed Suzuki g is computable by a finite prime-power sum, source
    rational approximations of exp/log/Gamma constants, and positive
    omitted Gamma bound B_J->0. Its 2x2 Gram determinant and diagonals
    are computable reals. If their sign is STRICTly separated from 0,
    an unbounded precision/refinement proof search will eventually
    find a directed rational enclosure which witnesses this strict
    inequality. At exactly zero the search can run forever.

    Our actual finite oracle has source-engine budgets J<=128,
    radius<=2 and exp argument<=128: don't claim it implements the
    unbounded mathematical semidecision theorem in full.
    """
    return {
        "source":"ORIGINAL_COMPLETED_ZETA_SUZUKI",
        "mathematical_source_data_effectively_approximable":"CLASSICAL_SOURCE_PLUS_GAMMA_TAIL",
        "strict_nonzero_minor_separation_finitely_semidecidable":
            "CLASSICAL_EFFECTIVE_REAL_COMPARISON_THEOREM",
        "true_zero_margin_requires_additional_source_identity":"NOT_DECIDED_BY_SHRINKING_INTERVALS",
        "finite_code_regulator_cap":128,
        "finite_code_global_sign_decider":False,
        "all_rational_tests_sign_proved":False,
        "RH_proved":False,
    }


def original_zero_margin_stuttering_counterexample(cap:int)->dict:
    """Synthetic interval sequence enclosing the EXACT zero at EVERY stage.

    All intervals [-1/J,+1/J] converge effectively to zero. None
    strictly certifies either positive or negative sign. An ordinal
    countdown can finish checking a finite prefix without completing
    the global sign obligation. NOT a signed zeta zero witness.
    """
    if type(cap) is not int or not 1<=cap<=512:
        raise OrdinalSourceSignError("Finite exact zero-margin countermodel cap")
    intervals=tuple((-F(1,j),F(1,j)) for j in range(1,cap+1))
    return {
        "source":"SYNTHETIC_EXACT_ZERO_NOT_ZETA",
        "regulator_steps":cap,
        "last_interval":intervals[-1],
        "all_finite_intervals_contain_zero":True,
        "strict_sign_separated_at_any_stage":False,
        "source_sign_proof_debt_after_regulator_exhausted":"ω",
        "ordinal_source_search_terminated":True,
        "actual_zeta_witness":False,
        "RH_proved":False,
    }
