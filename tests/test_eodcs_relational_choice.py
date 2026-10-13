"""Adversarial relational source transport: set-valued means NOT stochastic."""
import unittest
from fractions import Fraction as Q
from itertools import product
from random import Random

from observational_succ.causal_nerode_succ import SourceChart,SourceTransportError
from observational_succ.eodcs_relational_choice import (
    RelationalIntervention,relational_descent,compose_relations,
    universally_sufficient_refinement,source_likelihood_mutant,
    relational_choice_demo, modal_envelopes, modal_property_verdict,
)


def chart(epoch,states,obs,source="s",basis="basis"):
    return SourceChart(source,epoch,basis,tuple(states),tuple(obs))


class TestRelationalChoice(unittest.TestCase):
    def test_multivalued_source_descends_as_relation_not_deterministic_map(self):
        r=relational_choice_demo()
        self.assertTrue(r["source_multivalued"])
        self.assertTrue(r["set_valued_observation_descends"])
        self.assertFalse(r["deterministic_observation_descends"])
        self.assertTrue(r["support_equal_but_likelihoods_different"])
        self.assertTrue(r["composed_reconciled_observer_is_deterministic"])
        self.assertEqual(r["incompatible_original_fiber_witness"],["s0","s1"])
        self.assertFalse(r["probabilistic_interpretation_inferred_from_support"])
        self.assertFalse(r["physical_source_authenticated"])

    def test_3_state_every_total_serial_relation_against_independent_V_oracle(self):
        states=("a","b","c")
        choices=tuple(tuple(x for x,b in zip(states,bits) if b)
                      for bits in product((0,1),repeat=3) if any(bits))
        # 7**3=343 independent serial transition relation tables.
        for transitions in product(choices,repeat=3):
            old=chart(0,states,("0","0","1"))
            future=chart(1,states,("cold","warm","warm"))
            obj=RelationalIntervention("R",old,future,transitions)
            result=relational_descent(obj)
            # Oracle does NOT use the model's possibility-support accessor.
            state_report=dict(zip(states,old.observations))
            next_report=dict(zip(states,future.observations))
            raw_sets={
                s:frozenset(next_report[t] for t in allowed)
                for s,allowed in zip(states,transitions)
            }
            possibilities=tuple({frozenset(subset) for subset in
                (("cold",),("warm",),("cold","warm"))})
            # Exhaustively check whether some V exists on report image.
            oracle=any(all(V[0 if state_report[s]=="0" else 1]==raw_sets[s]
                           for s in states)
                       for V in product(possibilities,repeat=2))
            self.assertEqual(result.descended_to_set_valued_observer,oracle)
            if result.descended_to_set_valued_observer:
                self.assertEqual(dict(result.full_observed_transition)["0"],
                                 tuple(sorted(raw_sets["a"])))
                self.assertEqual(result.deterministic_observer_possible,
                                 all(len(vals)==1 for vals in raw_sets.values()))
            else:
                s,t,obs,p,q=result.source_witness
                self.assertEqual(state_report[s],state_report[t])
                self.assertNotEqual(p,q)

    def test_universal_refinement_by_all_three_state_partitions(self):
        states=("a","b","c")
        old=chart(0,states,("x","x","y"))
        nxt=chart(1,states,("hot","cold","warm"))
        src=RelationalIntervention("R",old,nxt,
                                  (("a","c"),("b",),("c",)))
        r=relational_descent(src)
        self.assertFalse(r.descended_to_set_valued_observer)
        code=dict(r.canonical_augmented_reports)
        candidates=list(product(("0","1","2"),repeat=3))
        adequate=[]
        for proposal in candidates:
            refinement=tuple(zip(states,proposal))
            adequate_flag=universally_sufficient_refinement(src,refinement)
            if adequate_flag:
                adequate.append(len(set(proposal)))
                self.assertTrue(all(code[a]==code[b] for a in states
                                    for b in states
                                    if dict(refinement)[a]==dict(refinement)[b]))
        self.assertTrue(adequate)
        self.assertEqual(min(adequate),r.new_class_count)

    def test_source_report_support_equality_does_not_imply_equal_likelihoods(self):
        states=("s0","s1")
        source=RelationalIntervention(
            "branch",chart(0,states,("0","0")),
            chart(1,("u","v"),("A","B")),(("u","v"),("u","v")))
        self.assertTrue(relational_descent(source).descended_to_set_valued_observer)
        law=source_likelihood_mutant(source,((Q(1,4),Q(3,4)),
                                             (Q(3,4),Q(1,4))))
        a=dict(law["law_by_source_state"])
        self.assertEqual(a["s0"],(("A",Q(1,4)),("B",Q(3,4))))
        self.assertEqual(a["s1"],(("A",Q(3,4)),("B",Q(1,4))))
        self.assertNotEqual(a["s0"],a["s1"])
        self.assertFalse(law["empirical_calibration_claimed"])

    def test_200_random_relational_compositions_separate_support_from_weights(self):
        rng=Random(20261013)
        for _ in range(200):
            states=("a","b","c")
            old=chart(0,states,tuple(str(rng.randrange(2)) for _ in states))
            mid=chart(1,states,tuple(str(rng.randrange(2)) for _ in states))
            end=chart(2,states,tuple(str(rng.randrange(2)) for _ in states))
            possible=lambda:tuple(s for s in states if rng.randrange(2)) or ("a",)
            first=RelationalIntervention("A",old,mid,
                                         tuple(possible() for s in states))
            second=RelationalIntervention("B",mid,end,
                                          tuple(possible() for s in states))
            composed=compose_relations(first,second)
            for s in states:
                direct={q for t in first.possible_states(s)
                        for q in second.possible_states(t)}
                self.assertEqual(set(composed.possible_states(s)),direct)
            self.assertEqual(composed.before,old)
            self.assertEqual(composed.after,end)
            self.assertEqual(composed.cost,Q(2))

    def test_tight_upper_lower_envelopes_refute_false_exact_transport(self):
        old=chart(0,("s0","s1"),("0","0"))
        next_chart=chart(1,("u0","u1"),("cold","warm"))
        src=RelationalIntervention("R",old,next_chart,(("u0",),("u1",)))
        b=modal_envelopes(src)
        self.assertEqual(len(b),1)
        self.assertEqual(b[0].may_reports,("cold","warm"))
        self.assertEqual(b[0].common_possible_reports,())
        self.assertFalse(b[0].exact_report_level_support)
        self.assertEqual(modal_property_verdict(src,"0",("warm",)),
                         "undecided_without_finer_observation")
        self.assertEqual(modal_property_verdict(src,"0",("cold","warm")),
                         "guaranteed_within_declared_support")
        self.assertEqual(modal_property_verdict(src,"0",()),
                         "impossible_within_declared_support")

    def test_exact_support_descent_iff_may_equals_common_on_each_fiber(self):
        states=("a","b","c")
        opts=tuple(tuple(x for x,on in zip(states,bits) if on)
                   for bits in product((0,1),repeat=3) if any(bits))
        old_reports=(("0","0","0"),("0","0","1"),("0","1","0"),
                     ("1","0","0"),("0","1","1"),("0","1","2"))
        target_reports=("red","green","blue")
        after=chart(1,states,target_reports)
        for old in old_reports:
            src=chart(0,states,old)
            for law in product(opts,repeat=3):
                model=RelationalIntervention("R",src,after,law)
                receipt=relational_descent(model)
                bounds=modal_envelopes(model)
                self.assertEqual(receipt.descended_to_set_valued_observer,
                                 all(b.exact_report_level_support for b in bounds))
                self.assertTrue(all(set(b.common_possible_reports)<=
                                    set(b.may_reports) for b in bounds))
                for b in bounds:
                    hidden=[s for s in states if src.report(s)==b.old_report]
                    full_support=[set(after.report(t) for t in model.possible_states(s))
                                  for s in hidden]
                    self.assertEqual(set(b.may_reports),set.union(*full_support))
                    self.assertEqual(set(b.common_possible_reports),
                                     set.intersection(*full_support))
                    for good in ((),("red",),("green",),("blue",),
                                 ("red","green","blue")):
                        verdict=modal_property_verdict(model,b.old_report,good)
                        if set.union(*full_support)<=set(good):
                            self.assertEqual(verdict,"guaranteed_within_declared_support")
                        elif set.union(*full_support).isdisjoint(good):
                            self.assertEqual(verdict,"impossible_within_declared_support")
                        else:
                            self.assertEqual(verdict,"undecided_without_finer_observation")

    def test_modal_not_misleading_as_probability_or_guaranteed_specific_outcome(self):
        old=chart(0,("s0","s1"),("0","0"))
        next_chart=chart(1,("u0","u1"),("cold","warm"))
        src=RelationalIntervention("R",old,next_chart,
                                    (("u0","u1"),("u0","u1")))
        b=modal_envelopes(src)[0]
        self.assertEqual(b.may_reports,("cold","warm"))
        self.assertEqual(b.common_possible_reports,("cold","warm"))
        self.assertTrue(b.exact_report_level_support)
        # Each report is possible at every hidden state. Neither is
        # GUARANTEED to occur, since either transition may happen.
        self.assertEqual(modal_property_verdict(src,"0",("cold",)),
                         "undecided_without_finer_observation")

    def test_negative_claim_type_gates(self):
        old=chart(0,("s0","s1"),("0","0"))
        next_chart=chart(1,("u0","u1"),("cold","warm"))
        src=RelationalIntervention("R",old,next_chart,(("u0",),("u1",)))
        with self.assertRaises(SourceTransportError):
            modal_property_verdict(src,"unobserved",("cold",))
        with self.assertRaises(SourceTransportError):
            modal_property_verdict(src,"0",("faked-label",))
        with self.assertRaises(SourceTransportError):
            modal_property_verdict(src,"0",["warm"])

    def test_source_type_and_probabilistic_mutation_fail_closed(self):
        src=chart(0,("a","b"),("0","1"))
        target=chart(1,("a","b"),("cold","warm"))
        with self.assertRaises(SourceTransportError):
            RelationalIntervention("bad",src,target,(("a",),()))
        with self.assertRaises(SourceTransportError):
            RelationalIntervention("bad",src,chart(1,("a","b"),("0","1"),source="other"),
                                   (("a",),("b",)))
        with self.assertRaises(SourceTransportError):
            RelationalIntervention("bad",target,src,(("a",),("b",)))
        with self.assertRaises(SourceTransportError):
            RelationalIntervention("bad",src,target,(("a",),("b",)),
                                  physical_source_authenticated=True)
        valid=RelationalIntervention("ok",src,target,(("a",),("b",)))
        with self.assertRaises(SourceTransportError):
            source_likelihood_mutant(valid,((Q(0),),(Q(1),)))
        with self.assertRaises(SourceTransportError):
            source_likelihood_mutant(valid,((Q(1,2),),(Q(1),)))
        with self.assertRaises(SourceTransportError):
            universally_sufficient_refinement(valid,(("b","0"),("a","1")))

    def test_incomplete_source_class_cannot_be_upgraded_by_a_flag(self):
        src=RelationalIntervention(
            "mathematical-partial",chart(0,("a","b"),("0","0")),
            chart(1,("u","v"),("A","B")),(("u",),("u",)),
            all_states_exhaustive=False)
        r=relational_descent(src)
        self.assertTrue(r.descended_to_set_valued_observer)
        self.assertFalse(r.source_class_certified)
        self.assertFalse(r.physical_source_authenticated)


if __name__=="__main__":
    unittest.main()
