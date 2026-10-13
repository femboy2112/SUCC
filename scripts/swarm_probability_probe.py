#!/usr/bin/env python3
"""Freeze exact C17--C24 controls; does not claim to run Lean or measure physics."""
import json
from fractions import Fraction as Q
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.swarm_probability import (
    CPInstrument, Experiment, StochasticHistory, StochasticInstrument,
    bayes_product_square, causal_ville_audit, commutation_defect, compose,
    compose_cp, find_garbling, law_descent, optimal_zero_error_cost,
    reversible_memory_lift,
)


def deterministic(name, reports, after, *, cost=1, source="bits", space="bits"):
    return StochasticInstrument(name, source, space, space, len(after),
                                tuple(((r, y, Q(1)),) for r, y in zip(reports, after)), Q(cost))


def receipt():
    states = tuple(range(4))
    good = deterministic("goodA", tuple(s//2 for s in states), states)
    bad = deterministic("badA", tuple(s//2 for s in states), tuple(2*(s//2) for s in states))
    b = deterministic("badB", tuple(s%2 for s in states), tuple(s%2 for s in states))
    root = StochasticHistory.original("bits", "bits", (Q(1,4),)*4)
    parity = (0,1,1,0)
    read_reset = StochasticInstrument("read_reset", "bit", "bit", "zero", 1,
                                      ((("zero",0,1),),(("one",0,1),)))
    reset_root = StochasticHistory.original("bit", "bit", (Q(1,2),Q(1,2)))
    hs = tuple(reset_root.advance(read_reset,o) for o in ("zero","one"))
    if any(not h.verify({"read_reset":read_reset}) for h in hs):
        raise ArithmeticError("Read-before-reset replay failed")
    probabilistic = StochasticInstrument("coin", "s", "x", "y", 1, (
        (("yes",0,Q(1,4)),("no",0,Q(3,4))),
        (("yes",0,Q(3,4)),("no",0,Q(1,4)))))
    descent = law_descent(probabilistic,(0,0),(0,))
    latent = StochasticHistory.from_joint("latent","HL",(
        (Q(1,8),Q(3,8),0,0),(0,0,Q(3,8),Q(1,8))))
    repeat = deterministic("readL",tuple("yes" if s%2 else "no" for s in states),
                           states,source="latent",space="HL")
    once = latent.advance(repeat,"yes")
    twice = once.advance(repeat,"yes")
    fresh = StochasticInstrument("fresh","latent","HL","HL",4,tuple(
        (("yes",s,Q(3,4) if s<2 else Q(1,4)),
         ("no",s,Q(1,4) if s<2 else Q(3,4))) for s in states))
    independently = latent.advance(fresh,"yes").advance(fresh,"yes")
    direct,staged = bayes_product_square((Q(1,2),Q(1,2)),
        ((Q(1,3),Q(2,3)),)*2,((Q(1,4),Q(3,4)),)*2,
        ((Q(3,4),Q(3,4)),(Q(1,4),Q(1,4))),((1,1),(1,1)))
    more = Experiment("bit",((Q(3,4),Q(1,4)),(Q(1,4),Q(3,4))))
    less = Experiment("bit",((Q(5,8),Q(3,8)),(Q(3,8),Q(5,8))))
    noncomparable_a = Experiment("three",((1,0),(0,1),(0,1)))
    noncomparable_b = Experiment("three",((0,1),(1,0),(0,1)))
    read_a = deterministic("a",tuple(s//2 for s in states),states)
    read_b = deterministic("b",tuple(s%2 for s in states),states)
    null = StochasticHistory.original("s","bit",(Q(3,4),Q(1,4)))
    alt = StochasticHistory.original("s","bit",(Q(1,4),Q(3,4)))
    read = deterministic("read",("no","yes"),(0,1),source="s",space="bit")
    ville = causal_ville_audit(null,alt,(read,),lambda h:"read",2,9)
    zero,one = ((1,0),(0,0)),((0,0),(0,1))
    erase = CPInstrument("erase",(("done",(zero,((0,1),(0,0)))),))
    measure = CPInstrument("Z",((0,(zero,)),(1,(one,))))
    recorded = compose_cp(measure,erase)
    data = {
        "schema":"SWARM-C-PROBABILITY-1",
        "parent_sha":"5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "C17":{
            "same_current_different_original":hs[0].current_posterior==hs[1].current_posterior
                and hs[0].original_posterior!=hs[1].original_posterior,
            "recorded_original_posteriors":[h.original_posterior for h in hs],
            "equal_support_probability_descent":descent.descends,
            "law_descent_witness":descent.witness,
            "coarsest_refinement_classes":len(set(descent.refinement)),
            "post_state_emission_factorization_on_fixed_singleton_carrier":False,
        },
        "C18":{
            "first_posterior_H":once.original_posterior[0],
            "duplicate_posterior_H":twice.original_posterior[0],
            "duplicate_conditional_probability":twice.events[-1].conditional_probability,
            "fresh_independent_posterior_H":independently.original_posterior[0],
            "factorized_bayes_gluing_commutes":direct==staged,
            "separator_posterior_H":sum((p for row in direct[0] for p in row),Q(0)),
        },
        "C19":{
            "erased_carriers_equal":erase.event(zero,"done")[1]==erase.event(one,"done")[1],
            "recorded_original0_probability":recorded.event(zero,(0,"done"))[0],
            "recorded_original1_probability":recorded.event(one,(1,"done"))[0],
            "multiple_kraus_per_outcome":2,
            "model":"finite real rational CP instrument; dimensions at most four",
        },
        "C20":{
            "exact_garbling":find_garbling(more,less),
            "reverse_garbling_exists":find_garbling(less,more) is not None,
            "noncomparable":find_garbling(noncomparable_a,noncomparable_b) is None
                and find_garbling(noncomparable_b,noncomparable_a) is None,
            "same_one_step_A_readout":True,
            "after_preserving_A_continuation_cost":optimal_zero_error_cost(
                root.advance(good,0),(b,),parity,1).cost,
            "after_destructive_A_continuation_cost":optimal_zero_error_cost(
                root.advance(bad,0),(b,),parity,7).cost,
        },
        "C21":{
            "destructive_parity_cost":optimal_zero_error_cost(root,(bad,b),parity,7).cost,
            "preserving_parity_cost":optimal_zero_error_cost(root,(good,b),parity,2).cost,
            "no_reset_in_menu":True,
            "horizon":7,
            "unbounded_no_go_has_paper_proof":True,
        },
        "C22":{
            "nondestructive_reads_commute":commutation_defect(read_a,read_b) is None,
            "destructive_reads_defect":commutation_defect(bad,b),
            "full_report_subkernels_checked":True,
        },
        "C23":{
            "calibrated_duplicate_evidence_ville":ville,
            "naive_squared_LR_expectation":Q(1,4)*9+Q(3,4)*Q(1,9),
            "naive_threshold9_crossing_probability":Q(1,4),
            "threshold9_ville_bound":Q(1,9),
        },
        "C24":{
            "reset_bit_memory_cardinality":reversible_memory_lift((0,0))[0],
            "invertible_map_memory_cardinality":reversible_memory_lift((0,1))[0],
            "three_to_one_fiber_memory_cardinality":reversible_memory_lift((0,0,1,0,1))[0],
            "energy_claim_from_kernel_alone":False,
        },
        "scope":{
            "classical_mathematics_and_declared_source_models":True,
            "lean_invoked":False,
            "physical_source_authenticated":False,
            "psychological_or_RH_result":False,
        },
    }
    assert data["C17"]["same_current_different_original"]
    assert not data["C17"]["equal_support_probability_descent"]
    assert data["C18"]["duplicate_posterior_H"] == Q(3,4)
    assert data["C18"]["fresh_independent_posterior_H"] == Q(9,10)
    assert data["C19"]["erased_carriers_equal"]
    assert data["C20"]["noncomparable"]
    assert data["C20"]["after_destructive_A_continuation_cost"] is None
    assert data["C21"]["preserving_parity_cost"] == 2
    assert data["C21"]["destructive_parity_cost"] is None
    assert data["C22"]["nondestructive_reads_commute"]
    assert data["C22"]["destructive_reads_defect"] is not None
    assert data["C23"]["naive_squared_LR_expectation"] == Q(7,3)
    return data


if __name__ == "__main__":
    print(json.dumps(receipt(),default=lambda x:str(x) if isinstance(x,Q) else x,indent=2,sort_keys=True))
