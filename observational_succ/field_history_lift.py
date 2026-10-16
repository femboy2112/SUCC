"""The SOURCE HISTORY gate missing from pointwise finite-to-global duality.

A bijective reconstruction of quotient POINTS need not be a faithful
representation of SOURCE EVENTS, action words, their order, winding,
or the cost of performing them.

The true additive adelic compact quotient (R×Zhat)/Z identifies
(t,z) and (t+k,z+k) for every k∈Z. Those are one quotient POINT,
but the declared source action of translating by k is a nonempty
history and must not be silently collapsed into a zero-cost event.
Finite cyclic quotient alias can be repaired by increasing modulus;
global diagonal quotient alias persists at POINT level unless the
observer gains a source-labeled lift/cocycle/path instrument.

Classical quotient math, no nontrivial zeta zeros or RH sign.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .tate_adele_quotient_descent import adele_solenoid_proof_contract


class HistoryLiftError(ValueError):
    """Missing source event/cost or invalid quotient path witness."""


@dataclass(frozen=True)
class SourceHistoryReceipt:
    original_source: str
    target: str
    starting_lift: int
    ending_lift: int
    visible_start: int
    visible_end: int
    action_steps: int
    endpoint_collision: bool
    original_history_trivial: bool
    source_event_faithful_from_endpoint_only: bool
    source_lift_observed: bool
    RH_proved: bool = False


def finite_successor_history_alias(modulus:int,steps:int)->SourceHistoryReceipt:
    """SUCC S:x->x+1 at source integer lift, q_N(x)=x mod N.

    If steps is nonzero multiple of N, q_N(S^steps x)=q_N(x), though
    the lawful performed history has positive cost 'steps'. Thus
    quotient-object naturality loses ordered transition information.
    """
    if (type(modulus) is not int or type(steps) is not int
            or not 2<=modulus<=100000 or not 0<steps<=1000000):
        raise HistoryLiftError("Genuine nonzero source successor steps and finite modulus")
    visible=steps%modulus
    return SourceHistoryReceipt(
        "ORIGINAL_SUCC_INTEGER_SHIFT",
        "FINITE_RESIDUE_QUOTIENT_Z_MOD_N",
        0,steps,0,visible,steps,visible==0,
        False,not (visible==0),False
    )


def exact_finite_refinement_repairs_fixed_history(steps:int)->dict:
    """For a FIXED nonzero displacement, modulus |steps|+1 separates it.

    This prevents falsely calling any one fixed integer history
    permanently indistinguishable under the FULL divisibility tower.
    Unlike the real-profinite diagonal quotient, the residue tower
    eventually sees every fixed integer displacement.
    """
    if type(steps) is not int or not 0<steps<=99999:
        raise HistoryLiftError("Fixed actual positive integer source history required")
    old_modulus=steps
    large=steps+1
    # old modulus 1 would not be a valid genuine finite ring stage;
    # use max(2,steps), with collision only when steps>=2.
    if steps>=2:
        coarse=finite_successor_history_alias(steps,steps)
        if not coarse.endpoint_collision:
            raise ArithmeticError("Original coarse source history should alias")
    refined=finite_successor_history_alias(large,steps)
    if refined.endpoint_collision:
        raise ArithmeticError("Fine source observer failed to distinguish fixed history")
    return {"true_source_steps":steps,
            "sufficient_distinguishing_modulus":large,
            "refined_endpoint":refined.visible_end,
            "fixed_history_eventually_distinguished_by_residue_tower":True,
            "finitely_observed_identity_does_not_prove_global_source_identity":True,
            "RH_proved":False}


def diagonal_adelic_lift_history(integer_shift:int)->dict:
    """Actual real-profinite solenoid quotient forgets diagonal Z lift.

    Let x=(t,z)∈R×Zhat, k∈Z. The original exact source action is
    x -> x+(k,k). The quotient X=(R×Zhat)/Z identifies those
    endpoints for EVERY k. A history observer preserving source
    action labels/winding can distinguish zero-event from k-shift.
    This is a POINT-quotient nonfaithfulness theorem, not a claim
    that full path-lift data is fundamentally unrecoverable.
    """
    if type(integer_shift) is not int or integer_shift==0 or abs(integer_shift)>1000000:
        raise HistoryLiftError("Nonzero exact source diagonal translation required")
    carrier=adele_solenoid_proof_contract()
    if not carrier["adelic_quotient_compact"]:
        raise ArithmeticError("Missing authentic real-profinite source carrier")
    return {"underlying_true_global_source":"(R_times_Zhat)_WITH_DIAGONAL_Z_ACTION",
            "quotient_source":"(R_times_Zhat)/Z_IS_A_Q/Q",
            "nontrivial_integer_lift_event":integer_shift,
            "quotient_endpoint_different":False,
            "source_event_nontrivial":True,
            "ordered_lift_path_suppressed_by_point_quotient":True,
            "source_lift_cocycle_must_be_retained_for_history_claim":True,
            "finite_integer_residue_tower_discriminator_is_different_problem":True,
            "physical_action_event_performed":False,
            "RH_proved":False}


def history_faithfulness_requirement()->dict:
    """Exact distinction between object and morphism faithfulness."""
    return {
        "global_point_model_bijection":"ATOM_SOURCE_TEST_ALGEBRA_PROFINITE_DUALITY",
        "source_event_category":"ACTION_PATH_OR_CAUSAL_HISTORY_WITH_ORDER_AND_COST",
        "quotient_state_map_injective_on_events":False,
        "required_repair":"SOURCE_LIFT_OR_SOURCE_AUTHORIZED_PATH_COCYCLE",
        "global_source_point_identified_implies_performed_history_identified":False,
        "actual_genuine_Weil_sign_proved":False,
        "RH_proved":False
    }



def exact_finite_source_periodization(modulus:int,
                                      source_lifts:tuple[tuple[int,int|Q],...])->dict:
    """A finite original-lattice-source model of TATE'S PERIODIZATION STEP.

    Given a finitely supported rational function phi:Z->Q, its correct
    quotient-periodization on Z/N is
       (P_N phi)(a) = sum_{k∈Z} phi(a+kN).
    Since phi has finite support, this is a FINITE exact source sum.
    Naively evaluating only phi(a) on the chosen representative
    forgets genuine lattice lifts; same quotient-point representation
    is NOT enough to reconstruct phi's periodized value.

    The adelic Poisson construction analogously needs
       P_Phi([x])=sum_{q∈Q} Phi(x+q)
    with convergence and SOURCE-LABELED lifts. This finite toy proves
    only the necessary categorical gate, NOT global Tate Poisson.
    """
    if (type(modulus) is not int or not 2<=modulus<=128
            or type(source_lifts) is not tuple
            or not 1<=len(source_lifts)<=64):
        raise HistoryLiftError("Exact finite integer-lattice source and quotient required")
    if any(type(z) is not tuple or len(z)!=2
           or type(z[0]) is not int or type(z[1]) not in (int,Q)
           or abs(z[0])>100000
           for z in source_lifts):
        raise HistoryLiftError("Typed rational finite-support original lattice function required")
    places=[n for n,v in source_lifts]
    if len(places)!=len(set(places)):
        raise HistoryLiftError("Duplicate source lift would double count original event")
    source={n:Q(v) for n,v in source_lifts}
    periodized=tuple(sum((v for n,v in source.items() if n%modulus==a),Q())
                     for a in range(modulus))
    representative_only=tuple(source.get(a,Q()) for a in range(modulus))
    lift_buckets=tuple(tuple(sorted(n for n in source if n%modulus==a))
                       for a in range(modulus))
    return {"source":"FINITE_SUPPORT_LATTICE_Z_WITH_ORDERED_LIFT_IDENTITIES",
            "quotient":"Z_MOD_N",
            "modulus":modulus,
            "all_source_lifts":tuple(sorted(source)),
            "correct_periodization":periodized,
            "naive_representative_evaluation":representative_only,
            "lattice_lift_buckets":lift_buckets,
            "endpoint_quotient_alone_determines_periodization":
                periodized==representative_only,
            "Tate_adelic_infinite_periodization_constructed":False,
            "Tate_global_Poisson_proved":False,
            "RH_proved":False}
