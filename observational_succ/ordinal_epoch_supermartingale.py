"""Ordinal RANKED macro-steps + genuine probabilistic retry supermartingales.

A source transition system may make stochastic RETRIES at unchanged ordinal
rank. A source-certified conditional hazard lower p>0 at EVERY retry gives
Pr(epoch has not advanced by t)<= (1-p)^t, so each rank decreases
eventually almost surely. By transfinite induction every starting ordinal
rank < epsilon_0 yields almost-sure finite TERMINATION if every rank
decrease is strict and terminal source state is required at rank 0.

This is NOT an expected ordinal. NO signed Weil/Schur positivity follows.
Nonuniform hazards with summable total may leave a positive chance of
stuttering forever; infinite branching can give pathwise termination
with INFINITE expected runtime despite ordinal descent.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .ordinal_ranked_succ import (
    OrdinalDescentError,ordinal_lex_counters,OrdinalProofObligationQueue,
    HierarchicalCountdown
)


def uniform_hazard_ordinal_epoch(
        counts:tuple[int,int,int],hazard:Q,horizon:int)->dict:
    """Exact finite source hazard plus classical all-rank transfinite theorem.

    Declare a conditional transition rule:
      if nonterminal, each retry advances to STRICTLY LOWER ordinal rank
      with conditional probability at least p>0,
      otherwise may remain at same rank but NEVER increase it.
    Any nonterminal epoch reaches a lower rank eventually a.s.,
    and transfinite induction on alpha yields terminal a.s.
    """
    state=OrdinalProofObligationQueue(counts)
    if state.finished:
        raise OrdinalDescentError("Active source epoch required")
    if type(hazard) is not Q or not 0<hazard<=1:
        raise OrdinalDescentError("Exact source conditional progress hazard p in (0,1]")
    if type(horizon) is not int or not 0<=horizon<=4096:
        raise OrdinalDescentError("Finite exact stochastic horizon 0..4096")
    tail=(1-hazard)**horizon
    return {
        "initial_source_rank":str(state.rank),
        "conditional_progress_hazard_lower":hazard,
        "horizon":horizon,
        "survival_upper_at_fixed_rank":tail,
        "macro_rank_never_increases_by_declared_transition_law":True,
        "progress_milestone_strict_ordinal_descent_declared":True,
        "almost_sure_epoch_exit":"PROVED_FROM_UNIFORM_HAZARD",
        "almost_sure_termination_for_all_ordinal_starts":
            "CLASSICAL_TRANSFINITE_INDUCTION_IF_ALL_SOURCE_RANK_TRANSITIONS_VERIFIED",
        "every_infinite_graph_path_terminated":False if hazard<1 else True,
        "physical_probability_source_authenticated":False,
        "original_completed_Weil_terminal_positive":False,
        "RH_proved":False,
    }


def summable_hazard_stuttering_countermodel(horizon:int)->dict:
    """Exact adversarial source: every p_t>0 but chance never exits >=1/2.

    Conditional independent retry at tick t=0,1,.. has hazard
       p_t = 2^(-(t+2)), Σ p_t = 1/2.
    Since product(1-p_i)>=1-Σ p_i, the infinite survival
    probability is at least 1/2 (in fact strictly >1/2).
    Positive progress probability at every finite step is therefore
    INSUFFICIENT for a.s. termination. The ordinal rank has not
    changed on a failure; no rank is illegally expected/decreased.
    """
    if type(horizon) is not int or not 0<=horizon<=256:
        raise OrdinalDescentError("Finite exact summable-hazard horizon 0..256")
    product=Q(1)
    mass=Q()
    for tick in range(horizon):
        p=Q(1,2**(tick+2))
        product*=1-p
        mass+=p
    exact_lower=1-mass
    if not product>=exact_lower>Q(1,2):
        raise ArithmeticError("Exact finite hazard survival lower was corrupted")
    return {
        "positive_hazard_each_finite_tick":True,
        "source_retry_hazard":"p_t=2^(-(t+2))",
        "finite_horizon":horizon,
        "finite_survival_exact":product,
        "partial_hazard_sum":mass,
        "finite_survival_lower":exact_lower,
        "infinite_survival_probability_lower":Q(1,2),
        "almost_sure_epoch_exit":False,
        "source_probability_law_mathematical_only":True,
        "RH_proved":False,
    }


def omega_branch_infinite_expected_length(horizon:int)->dict:
    """SURE finite path by rank, but INFINITE expected number of steps.

    From source rank omega select natural n>=0 with
       P(N=n)=1/((n+1)(n+2)).
    Then strict source transition omega -> n and deterministic
       n -> n-1 -> ... ->0.
    Every chosen n is finite, so EVERY path terminates at tau=n+1.
    The distribution sums to 1 by telescoping, but
       P(tau>h)=1/(h+1), and E[tau]=sum_h>=0 1/(h+1)=infinity.
    This is genuine infinite-branching ordinal termination that
    an ordinary uniform natural length bound cannot express.
    """
    if type(horizon) is not int or not 0<=horizon<=256:
        raise OrdinalDescentError("Finite exact heavy-tail path horizon 0..256")
    mass=sum((Q(1,(n+1)*(n+2)) for n in range(horizon+1)),Q())
    if mass!=1-Q(1,horizon+2):
        raise ArithmeticError("Telescoping ordinal branch source lost probability mass")
    harmonic=sum((Q(1,k+1) for k in range(horizon+1)),Q())
    return {
        "source_rank_before_branch":"ω",
        "source_branch_values":"all finite natural n>=0",
        "source_law":"P(N=n)=1/((n+1)(n+2))",
        "finite_branch_probability_sum":mass,
        "unseen_probability_mass":Q(1,horizon+2),
        "terminates_on_EVERY_sample_path":True,
        "finite_horizon":horizon,
        "exact_tail_probability_tau_gt_horizon":Q(1,horizon+1),
        "truncated_expected_length_lower":harmonic,
        "full_expected_length":"INFINITE_BY_HARMONIC_DIVERGENCE",
        "one_uniform_finite_path_length_bound":False,
        "RH_proved":False,
    }


def giant_geometric_ranked_succ_path(
        digits:tuple[int,...],reset_bits:int,progress_probability:Q)->dict:
    """One finite hierarchical SUCC path with geometric retries.

    Deterministic true ordinal milestone length N=V(digits).
    Each milestone succeeds after independent geometric(p) attempts,
    expected attempts N/p, almost-sure finite; no N steps executed.
    The nonnegative REAL variant V_t (remaining milestone count)
    has conditional drift -p while active:
        E[V_next|V>0] = V-p.
    This is the exact valid martingale-like coupling of Goodstein-
    style ordinal rank with a quantitative source progress law.
    """
    source=HierarchicalCountdown(digits,reset_bits)
    N=source.exact_remaining_steps
    if not N:raise OrdinalDescentError("Nonempty normalizer required")
    if type(progress_probability) is not Q or not 0<progress_probability<=1:
        raise OrdinalDescentError("Exact rational progress probability (0,1] required")
    return {
        "source":"DECLARED_HIERARCHICAL_SUCC_WITH_BERNOULLI_RETRIES",
        "source_rank":str(source.rank),
        "strict_ord_decrease_only_when_milestone_exits":True,
        "source_milestone_count":N,
        "one_milestone_progress_probability":progress_probability,
        "ranking_supermartingale_conditional_drift":progress_probability,
        "expected_total_attempts":Q(N)/progress_probability,
        "almost_sure_finite_source_completion":True,
        "all_graph_paths_finite":progress_probability==1,
        "original_Weil_positive_terminal_proved":False,
        "RH_proved":False,
    }


def true_source_ordinal_martingale_boundary()->dict:
    return {
        "actual_project":"TATE_SUCC_WEIL_SOURCE",
        "source_history":"ORIGINAL_PRIME_POWERS_COMPLETED_REAL_GAMMA_AND_POLES",
        "ordinal_normalizer_decreasing_every_source_step":"UNVERIFIED",
        "source_hazard_uniform_or_divergent":"UNVERIFIED",
        "independent_source_positive_terminal":"UNVERIFIED",
        "actual_completed_Weil_global_positive":"UNVERIFIED",
        "source_probability_from_physical_observation_authenticated":False,
        "RH_proved":False,
    }
