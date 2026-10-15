"""Ordinal rank vs probability/RSM vs completed Weil sign: source-proof firewall.

Ordinals certify SURE FINITE path termination when every actual edge
strictly decreases a well-founded rank. Ranking SUPERMARTINGALES instead
permit positive-probability edges that increase a state measure and
prove probabilistic (almost-sure) statements under authenticated
conditional transition laws. The two are NOT interchangeable.

A source-correct Loewner/Schur sign cannot be obtained by terminating
a normalizer or by a positive generic semantic martingale. Original
zeta source is not modified and no nontrivial zero positions are read.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .ordinal_ranked_succ import (
    OrdinalCNF,OrdinalDescentError,ordinal_nat,ordinal_lex_counters
)


def almost_sure_termination_source(horizon:int,halt_probability:Q=Q(1,2))->dict:
    """EXACT geometric stopping source, with exceptional infinite graph path.

    At nonterminal state n>=0: HALT probability p, else go to n+1
    probability 1-p, with independent fresh declared Bernoulli draws.
    The tail Pr(tau>t)=(1-p)^t and E[tau]=1/p. Hence Pr(tau<inf)=1.
    The graph nonetheless contains n->n+1 forever as an admissible
    infinite PATH of probability zero, so NO ordinal-valued ranking
    can strictly decrease along *every possible edge*.

    V(n)=1 on active states and V(terminal)=0 satisfies
       E[V_next|active] = 1-p <= V_now-p.
    This is a ranking SUPERMARTINGALE drift rule in REAL numbers,
    not an ordinal expectation and not a zeta/Weil probability law.
    """
    if type(horizon) is not int or not 0<=horizon<=128:
        raise OrdinalDescentError("Bounded geometric stochastic source horizon 0..128")
    if type(halt_probability) is not Q or not 0<halt_probability<=1:
        raise OrdinalDescentError("Exact authenticated rational Bernoulli law required")
    p=halt_probability
    tail=(1-p)**horizon
    return {
        "process":"ACTUAL_DECLARED_GEOMETRIC_STOP_VS_INCREASING_ACTIVE_CLOCK",
        "fresh_draw_law_source_authenticated_empirically":False,
        "mathematical_transition_probability_to_halt":p,
        "mathematical_transition_probability_to_increment":1-p,
        "horizon":horizon,
        "exact_survival_probability":tail,
        "exact_termination_probability_by_horizon":1-tail,
        "infinite_survival_probability":"0_BY_GEOMETRIC_LIMIT",
        "expected_steps":1/p,
        "real_ranking_supermartingale_drift":p,
        "strict_ordinal_rank_all_positive_probability_edges":
            False if p<1 else True,
        "infinite_nonhalting_path_in_source_graph":p<1,
        "source_graph_infinite_path_has_probability_zero":p<1,
        "RH_proved":False,
    }


def ordinal_pathwise_rank_obstruction(horizon:int)->dict:
    """No ordinal can satisfy rho(n+1)<rho(n) for EVERY n>=0.

    Such a rho would give the impossible descending sequence
    rho(0)>rho(1)>rho(2)>... of ordinals.
    Finite prefixes are easy: rho_H(n)=H-n for 0<=n<=H, but
    their source rank maps depend on H and DO NOT define one global rho.
    """
    if type(horizon) is not int or not 1<=horizon<=100000:
        raise OrdinalDescentError("Exact finite nonhalting-prefix horizon")
    local=tuple(horizon-n for n in range(min(horizon,12)+1))
    if not all(x>y for x,y in zip(local,local[1:])):
        raise ArithmeticError("Finite horizon witness not descending")
    return {
        "source_graph":"n_to_n_plus_one_with_all_naturals",
        "prefix_length":horizon,
        "horizon_dependent_rank_first_values":local,
        "each_finite_prefix_has_ordinal_nat_rank":True,
        "one_coherent_global_ordinal_rank_exists":False,
        "reason":"AN_INFINITE_STRICT_DESCENT_OF_ORDINALS_CANNOT_EXIST",
        "not_a_counterexample_to_almost_sure_termination":True,
        "RH_proved":False,
    }


def ordinal_ranked_schur_normalization(a:int|Q,b:int|Q,d:int|Q)->dict:
    """A 2x2 SOURCE-IDENTIFIED congruence preserves sign, cannot create it.

    For a>0, exact completing square:
       [x,y] [[a,b],[b,d]] [x,y]^T
           = a(x+b/a*y)^2 + (d-b^2/a)y^2.
    One invertible change of coordinates brings the source operator
    to diag(a, d-b²/a). A strictly descending tiny ordinal proof
    protocol certifies finite completion, but neither signed Schur
    positivity nor actual zeta identity follows from termination.
    """
    if any(type(z) not in (int,Q) for z in (a,b,d)):
        raise OrdinalDescentError("Exact rational Hermitian source coefficients required")
    A,B,D=Q(a),Q(b),Q(d)
    if A<=0:
        raise OrdinalDescentError("This specific positive-pivot normalizer requires a>0")
    schur=D-B*B/A
    before=ordinal_lex_counters((2,0)) # omega*2
    middle=ordinal_lex_counters((1,3)) # omega+3
    terminal=ordinal_nat(1)
    if not (terminal<middle<before):
        raise ArithmeticError("Ordinal finite signed-Schur proof trace malformed")
    checkpoints=((-B/A,Q(1)),(Q(0),Q(1)),(Q(1),Q(0)))
    for x,y in checkpoints:
        original=A*x*x+2*B*x*y+D*y*y
        transformed=A*(x+B/A*y)**2+schur*y*y
        if original!=transformed:
            raise ArithmeticError("Signed source congruence changed original quadratic law")
    return {
        "source":"DECLARED_RATIONAL_SIGNED_OPERATOR_NOT_ZETA",
        "input_matrix":((A,B),(B,D)),
        "ordinal_rank_trace":tuple(str(x) for x in (before,middle,terminal)),
        "rank_strict_decrease":True,
        "source_congruence_invertible_and_sign_preserving":True,
        "completed_square_pivot":A,
        "completed_square_schur":schur,
        "normalization_terminated":True,
        "source_quadratic_positive":schur>=0,
        "negative_exact_direction":(-B/A,Q(1)) if schur<0 else None,
        "RH_proved":False,
    }


def ordinal_termination_not_weil_positive()->dict:
    """Exact source-preserving NEGATIVE CONTROL for ordinal proof conflation."""
    s=ordinal_ranked_schur_normalization(1,2,1)
    if s["completed_square_schur"]!=-3 or s["source_quadratic_positive"]:
        raise ArithmeticError("Ordinal signed source false positivity shortcut accepted")
    return {
        "original_source_kind":"EXACT_SYNTHETIC_SIGNED_COUPLING",
        "rank_trace":s["ordinal_rank_trace"],
        "one_normal_form_reached":True,
        "source_sign_was_changed_by_normalization":False,
        "terminal_negative_schur":Q(-3),
        "ordinal_termination_implies_original_Weil_PSD":False,
        "missing_RH_hypothesis":
            "AUTHENTIC_ZETA_WEIL_SOURCE_PLUS_GLOBAL_SIGN_PRESERVING_TERMINAL_POSITIVE_LAW",
        "RH_proved":False,
    }


def actual_weil_ordinal_rank_frontier()->dict:
    """Nothing in original RH papers yields an ordinal descent per Schur step.

    To turn an arbitrary long SUCC observer search into a mathematically
    closing finite proof one must CONSTRUCT rho(source state) under true
    prime/Gamma/contact/conductor transitions AND prove rank decreases
    when the algorithm is stuck or refines, with a terminal rule that
    preserves/sign-certifies the authentic completed Weil quadratic.
    Fake ordinal rank on a synthetic Gram cannot provide either premise.
    """
    return {
        "declared_true_source":"ORIGINAL_COMPLETED_TATE_WEIL_SUZUKI",
        "source_finite_to_global_Tate_arithmetic":"CONDITIONAL_UNDER_GLOBAL_POISSON_SOURCE_MAP",
        "Goodstein_all_stage_termination":"CLASSICAL_EPSILON0_WELLFOUNDEDNESS",
        "true_source_Weil_Schur_rank_function":"UNVERIFIED",
        "true_source_rank_descent_every_refinement":"UNVERIFIED",
        "true_source_sign_invariant_under_ranked_normalization":"UNVERIFIED",
        "true_source_positive_terminal_certificate":"UNVERIFIED",
        "original_30_low_Schur_positive":"UNVERIFIED",
        "all_a_completed_Weil_positive":"UNVERIFIED",
        "RH_intrinsically_unprovable":"NOT_ESTABLISHED",
        "RH_proved":False,
    }
