"""Hostile exact tests of the carrier as the common source-indexed object.

The oracles for source-indexed joint probability, finite partition ordering,
and symbolic deterministic F48 histories are deliberately distinct from the
carrier quotient's own signature/refinement implementation.
"""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from random import Random

from observational_succ.carrier_indexed import (
    ActualHistory, Carrier, CarrierError, CarrierInstrument,
    CarrierQuotient, CarrierStage, audit_descent, checked_descent,
    compare_histories, from_deterministic_lawful_source,
    from_stochastic_history, labels_partition, mass_total,
    minimal_stationary_repair, repair_one_step, CarrierStep,
    transport_actual_history, original_support_is_monotone,
    forget_probabilities, possibility_descent, compose_possibilities,
    deterministic_instrument,
)
from observational_succ.swarm_lawful_history import (
    LawfulSource, Instrument, Event, replay_fiber,
)
from observational_succ.swarm_probability import (
    StochasticHistory, StochasticInstrument,
)


def stage(source="source", n=4, epoch=0, name="root", basis="declared"):
    return CarrierStage(source,basis,epoch,name,tuple(range(n)))


def same_source(n=4, prior=None):
    st=stage(n=n)
    if prior is None:
        prior=tuple(Q(1,n) for _ in range(n))
    prep=tuple(tuple(prior[i] if j==i else Q(0) for j in range(n))
               for i in range(n))
    return Carrier(tuple(range(n)),st,prep)


def action(st, reports, updates=None, *, name="A", enabled=None,
           final=None):
    updates=tuple(range(st.count)) if updates is None else tuple(updates)
    final=st if final is None else final
    values=tuple(dict.fromkeys(reports))
    if enabled is None:
        enabled=tuple(True for _ in st.states)
    return CarrierInstrument(
        name,st,final,values,tuple(enabled),
        tuple(((values.index(z),after,Q(1)),)
              for z,after in zip(reports,updates)))


def canonical_partitions(n):
    for labels in product(range(n),repeat=n):
        if labels_partition(labels)==labels:
            yield labels


def is_refinement(fine,coarse):
    return all(fine[i]!=fine[j] or coarse[i]==coarse[j]
               for i in range(len(fine)) for j in range(len(fine)))


def raw_joint_reindex(original_mass, fine_action, obs_index, before_labels,
                      after_labels):
    """Independent raw atom-loop oracle, not CarrierQuotient or .advance."""
    n_original=len(original_mass)
    n_after=max(after_labels)+1
    after=[[Q(0)]*n_after for _ in range(n_original)]
    for o,row in enumerate(original_mass):
        for c,p in enumerate(row):
            for z,d,w in fine_action.rows[c]:
                if z==obs_index:
                    after[o][after_labels[d]]+=Q(p)*Q(w)
    return tuple(tuple(x for x in row) for row in after)


class CarrierSemantics(unittest.TestCase):
    def test_preparation_and_exact_types_are_not_empirically_authenticated(self):
        orig=same_source()
        self.assertEqual(orig.root().evidence,1)
        self.assertEqual(orig.root().original_posterior,(Q(1,4),)*4)
        self.assertEqual(orig.root().originals_supported,frozenset(range(4)))
        with self.assertRaises(CarrierError):
            Carrier(orig.originals,orig.stage,orig.preparation,True)
        with self.assertRaises(CarrierError):
            Carrier(orig.originals,orig.stage,
                    ((Q(1,4),0,0,0),)*3 + ((0,0,0,0),))
        with self.assertRaises(CarrierError):
            Carrier(orig.originals,orig.stage,
                    ((0.25,0,0,0),)*4)
        with self.assertRaises(CarrierError):
            CarrierStage("other","basis",-1,"bad",(1,))
        with self.assertRaises(CarrierError):
            CarrierStage("other","basis",0,"bad",("dup","dup"))
        with self.assertRaises(CarrierError):
            Carrier(orig.originals,orig.stage,
                    ((Q(-1),0,0,2),)+orig.preparation[1:])
        self.assertEqual(labels_partition((7,9,7,2)),(0,1,0,2))

    def test_original_truth_survives_destructive_carrier_erasure(self):
        first=stage(n=2)
        collapsed=stage(n=1,epoch=1,name="erased")
        prepared=same_source(2)
        erase=action(first,("zero","one"),(0,0),final=collapsed,name="read/erase")
        seen0=prepared.root().advance(erase,"zero")
        seen1=prepared.root().advance(erase,"one")
        self.assertEqual(seen0.original_posterior,(1,0))
        self.assertEqual(seen1.original_posterior,(0,1))
        self.assertEqual(seen0.current.states,seen1.current.states)
        self.assertEqual(seen0.decide_original(("cold","warm")).value,"cold")
        self.assertEqual(seen1.decide_original(("cold","warm")).value,"warm")
        self.assertEqual(seen0.evidence,Q(1,2))
        self.assertEqual(seen0.events[0].conditional_likelihood,Q(1,2))
        self.assertEqual(seen0.events[0].before,"root")
        self.assertEqual(seen0.events[0].after,"erased")
        self.assertTrue(seen0.verify({"read/erase":erase}))
        self.assertTrue(seen1.verify({"read/erase":erase}))
        wrong=replace(seen0,mass=((Q(1,3),),(Q(1,6),)))
        with self.assertRaises(CarrierError):
            wrong.verify({"read/erase":erase})
        with self.assertRaises(CarrierError):
            prepared.root().advance(erase,"not-a-receipt")
        with self.assertRaises(CarrierError):
            seen0.advance(erase,"zero")

    def test_availability_is_not_a_free_hidden_state_sensor(self):
        st=stage(n=2)
        source=same_source(2)
        conditional=action(st,(0,0),name="conditional",enabled=(True,False))
        self.assertFalse(source.root().available(conditional))
        with self.assertRaises(CarrierError):
            source.root().advance(conditional,0)
        only_zero=Carrier(("source0","source1"),st,
                          ((1,0),(0,0)))
        self.assertTrue(only_zero.root().available(conditional))
        self.assertEqual(only_zero.root().advance(conditional,0).evidence,1)
        q=CarrierQuotient(st,(0,0),"coarse")
        verdict=audit_descent(conditional,q,q)
        self.assertFalse(verdict.valid)
        self.assertEqual(verdict.witness.issue,"ENABLEDNESS")

    def test_full_joint_kernel_not_receipt_marginals_or_support(self):
        st=stage(n=2)
        after=stage(n=2,epoch=1,name="after")
        coin=CarrierInstrument(
            "correlated",st,after,("z","w"),(True,True),
            (
              ((0,0,Q(1,2)),(1,1,Q(1,2))),
              ((0,1,Q(1,2)),(1,0,Q(1,2)))
            ))
        q0=CarrierQuotient(st,(0,0),"observation")
        q1=CarrierQuotient(after,(0,1),"new report")
        verdict=audit_descent(coin,q0,q1)
        self.assertFalse(verdict.valid)
        self.assertEqual(verdict.witness.issue,"JOINT_RECEIPT_AND_NEXT")
        # Both original report marginals are exactly fair; both next-state
        # marginals are exactly fair. Correlations are the only difference.
        for row in coin.rows:
            self.assertEqual(tuple(sum((p for z,_,p in row if z==j),Q(0))
                                   for j in (0,1)),(Q(1,2),)*2)
            self.assertEqual(tuple(sum((p for _,c,p in row if c==j),Q(0))
                                   for j in (0,1)),(Q(1,2),)*2)
        with self.assertRaises(CarrierError):
            checked_descent(coin,q0,q1)

    def test_equal_possibility_support_but_unequal_probabilities(self):
        st=stage(n=2)
        coin=CarrierInstrument(
            "coin",st,st,("yes","no"),(True,True),
            (
                ((0,0,Q(1,4)),(1,0,Q(3,4))),
                ((0,1,Q(3,4)),(1,1,Q(1,4)))
            ))
        q=CarrierQuotient(st,(0,0),"forget")
        verdict=audit_descent(coin,q,q)
        self.assertFalse(verdict.valid)
        self.assertEqual(verdict.witness.issue,"JOINT_RECEIPT_AND_NEXT")
        self.assertEqual({z for z,c,p in coin.rows[0]},
                         {z for z,c,p in coin.rows[1]})

    def test_full_joint_lumpability_preserves_original_evidence_and_posterior(self):
        st=stage(n=4)
        src=same_source()
        q=CarrierQuotient(st,(0,0,1,1),"group")
        # Two fine states inside each quotient block make different hidden
        # transitions. Their joint receipt/quotient successor laws agree.
        a=action(st,("left","left","right","right"),name="read")
        t=checked_descent(a,q,q)
        self.assertEqual(t.before.count,2)
        self.assertEqual(t.receipts,("left","right"))
        for receipt in a.receipts:
            ours=compare_histories(src.root(),q,q,a,receipt)
            self.assertTrue(ours["lawful_original_preservation"])
            self.assertEqual(ours["fine_evidence"],Q(1,2))
        coarse=q.root(src)
        self.assertEqual(coarse.originals,src.originals)
        self.assertEqual(coarse.preparation[0],(Q(1,4),0))
        self.assertEqual(coarse.preparation[3],(0,Q(1,4)))

    def test_independent_joint_law_oracle_180_seeded_tables(self):
        rng=Random(1185)
        st=stage(n=4)
        out=stage(n=3,epoch=1,name="next")
        bq=CarrierQuotient(st,(0,0,1,1),"before")
        aq=CarrierQuotient(out,(0,1,1),"after")
        for j in range(180):
            source=same_source(4)
            fine=[]
            for c in range(4):
                # Complete strictly nonnegative rational atom table.
                w=[rng.randrange(5) for k in range(6)]
                if not sum(w):
                    w[0]=1
                fine.append(tuple((r,d,Q(w[r*3+d],sum(w)))
                                  for r in range(2) for d in range(3)))
            if j % 3 == 0:
                # Plant a lawful q-fiber-constant kernel so the sufficiency
                # (verdict.valid) branch below is actually exercised, not skipped.
                fine[1]=fine[0]
                fine[3]=fine[2]
            a=CarrierInstrument("seed"+str(j),st,out,("u","v"),
                                (True,True,True,True),tuple(fine))
            verdict=audit_descent(a,bq,aq)
            raw=[]
            for row in a.rows:
                tally={}
                for z,d,p in row:
                    key=(z,aq.labels[d])
                    tally[key]=tally.get(key,Q(0))+p
                raw.append(tally)
            independent=(raw[0]==raw[1] and raw[2]==raw[3])
            self.assertEqual(verdict.valid,independent)
            if verdict.valid:
                coarse=checked_descent(a,bq,aq)
                for z,receipt in enumerate(a.receipts):
                    if not any(p > 0 for row in source.preparation
                               for c, m in enumerate(row) if m > 0
                               for j, _, p in a.rows[c] if j == z):
                        continue
                    fine_next=source.root().advance(a,receipt)
                    coarse_next=bq.root(source).root().advance(coarse,receipt)
                    expected=raw_joint_reindex(source.preparation,a,z,
                                               bq.labels,aq.labels)
                    self.assertEqual(coarse_next.mass,expected)
                    self.assertEqual(aq.push(fine_next.mass),expected)
                    self.assertEqual(coarse_next.evidence,fine_next.evidence)
                    self.assertEqual(coarse_next.original_posterior,
                                     fine_next.original_posterior)

    def test_impossible_event_and_wrong_stage_fail_closed(self):
        st=stage(n=2)
        source=same_source(2)
        a=action(st,("yes","yes"))
        with self.assertRaises(CarrierError):
            source.root().advance(a,"no")
        after=stage(n=2,epoch=1,name="later")
        with self.assertRaises(CarrierError):
            CarrierInstrument("backwards",after,st,(0,), (True,True),
                              (((0,0,1),),((0,0,1),)))
        foreign=stage("different",n=2,epoch=1,name="future")
        with self.assertRaises(CarrierError):
            CarrierInstrument("wrong source",st,foreign,(0,),(True,True),
                              (((0,0,1),),((0,0,1),)))
        with self.assertRaises(CarrierError):
            CarrierInstrument("float",st,st,(0,),(True,True),
                              (((0,0,0.5),(0,1,0.5)),((0,0,1),)))
        with self.assertRaises(CarrierError):
            CarrierQuotient(st,(1,1),"noncanonical")


class FiniteBehavioralRepair(unittest.TestCase):
    def test_stationary_observer_repair_generates_minimal_necessary_splits(self):
        st=stage(n=4)
        base=action(st,("same","same","different","different"),name="read")
        flip=action(st,("ok","ok","ok","ok"),(0,2,2,0),name="change")
        seed=(0,0,1,1)
        result=minimal_stationary_repair(st,(base,flip),seed)
        self.assertEqual(result.partition,(0,1,2,3))
        self.assertTrue(result.stabilized)
        self.assertTrue(result.steps)
        q=CarrierQuotient(st,result.partition,"maximally-informative")
        for a in (base,flip):
            self.assertTrue(audit_descent(a,q,q).valid)
        # Original weaker quotient cannot support action "change".
        old=CarrierQuotient(st,seed,"initial")
        self.assertFalse(audit_descent(flip,old,old).valid)

    def test_exhaustive_coarsest_partition_oracle_for_90_random_sources(self):
        rng=Random(98271)
        st=stage(n=4)
        all_partitions=tuple(canonical_partitions(4))
        for trial in range(90):
            seed=rng.choice(all_partitions)
            actions=tuple(action(
                st,tuple(rng.randrange(2) for _ in range(4)),
                tuple(rng.randrange(4) for _ in range(4)),
                name="a"+str(i),
                enabled=tuple(bool(rng.randrange(2)) for _ in range(4)))
                for i in range(2))
            repair=minimal_stationary_repair(st,actions,seed)
            final=CarrierQuotient(st,repair.partition,"fixed")
            self.assertTrue(all(audit_descent(a,final,final).valid for a in actions))
            candidates=[
                p for p in all_partitions
                if is_refinement(p,seed) and all(
                    audit_descent(a,CarrierQuotient(st,p,"candidate"),
                                  CarrierQuotient(st,p,"candidate")).valid
                    for a in actions)]
            self.assertTrue(candidates)
            min_blocks=min(len(set(p)) for p in candidates)
            self.assertEqual(len(set(repair.partition)),min_blocks)
            self.assertEqual([p for p in candidates if len(set(p))==min_blocks],
                             [repair.partition])
            self.assertLessEqual(len(repair.steps),4-len(set(seed)))

    def test_stationary_source_contract_mutations(self):
        st=stage(n=2)
        later=stage(n=2,epoch=1,name="later")
        bad=action(st,(0,1),final=later)
        with self.assertRaises(CarrierError):
            minimal_stationary_repair(st,(bad,))
        with self.assertRaises(CarrierError):
            minimal_stationary_repair(st,())
        with self.assertRaises(CarrierError):
            minimal_stationary_repair(st,(action(st,(0,1),name="x"),)*2)
        with self.assertRaises(CarrierError):
            minimal_stationary_repair(st,(action(st,(0,1)),),(0,))


class ExistingCodeBridges(unittest.TestCase):
    def test_deterministic_f48_history_support_matches_adapter(self):
        source=LawfulSource("real-class", tuple(range(4)), (
            Instrument("read_a", tuple(range(4)),(0,0,1,1),(True,)*4),
            Instrument("read_b", tuple(range(4)),(0,1,0,1),(True,)*4),
            Instrument("flip", (1,0,3,2),("ok",)*4,(True,)*4)))
        carrier,actions=from_deterministic_lawful_source(source,(Q(1,4),)*4)
        words=[
            (),
            (Event("read_a",0),),
            (Event("read_a",1),Event("read_b",1)),
            (Event("flip","ok"),Event("read_b",1),Event("read_a",0)),
        ]
        for word in words:
            current=carrier.root()
            for e in word:
                current=current.advance(actions[e.action],e.outcome)
            old=replay_fiber(source,word)
            expected=frozenset(o for o,c in old.configurations)
            self.assertEqual(current.originals_supported,expected)
            self.assertEqual({(o,c) for o,row in enumerate(current.mass)
                              for c,v in enumerate(row) if v>0},
                             set(old.configurations))
        with self.assertRaises(CarrierError):
            from_deterministic_lawful_source(source,(Q(1,3),)*4)

    def test_stochastic_history_adapter_respects_joint_and_rejects_lossy_origin(self):
        stoch=StochasticHistory.from_joint("s","original",
                         ((Q(1,2),0),(0,Q(1,2))))
        fine=StochasticInstrument("measure","s","original","next",1,
                         (((0,0,Q(1,4)),(1,0,Q(3,4))),
                          ((0,0,Q(3,4)),(1,0,Q(1,4)))))
        root,carrier_action=from_stochastic_history(stoch,fine)
        for z in (0,1):
            ours=root.root().advance(carrier_action,z)
            theirs=stoch.advance(fine,z)
            self.assertEqual(ours.original_posterior,theirs.original_posterior)
            self.assertEqual(ours.evidence,theirs.path_probability)
            self.assertEqual(tuple(tuple(v/ours.evidence for v in row)
                                   for row in ours.mass),theirs.joint)
        with self.assertRaises(CarrierError):
            from_stochastic_history(stoch.advance(fine,0),fine)
        wrong=StochasticInstrument("wrong","other","original","next",1,
                    (((0,0,1),),((0,0,1),)))
        with self.assertRaises(CarrierError):
            from_stochastic_history(stoch,wrong)



class FullCarrierComposition(unittest.TestCase):
    def test_two_stage_original_law_evidence_and_supported_target_transport(self):
        root_stage=stage(n=4)
        middle=stage(n=4,epoch=1,name="intermediate")
        terminal=stage(n=1,epoch=2,name="collapsed")
        src=same_source()
        q0=CarrierQuotient(root_stage,(0,0,1,1),"observable-before")
        q1=CarrierQuotient(middle,(0,0,1,1),"observable-middle")
        q2=CarrierQuotient(terminal,(0,),"observable-end")
        change=action(root_stage,("ok",)*4,(1,0,3,2),
                      name="swap-inside-fibers",final=middle)
        read=action(middle,("left","left","right","right"),(0,0,0,0),
                    name="read-then-erase",final=terminal)
        steps=(CarrierStep(change,q0,q1,"ok"),
               CarrierStep(read,q1,q2,"right"))
        cert=transport_actual_history(
            src,q0,steps,original_target=("L","L","R","R"))
        self.assertEqual(cert.actual_history_length,2)
        self.assertEqual(cert.public_trace,
                         (("swap-inside-fibers","ok"),("read-then-erase","right")))
        self.assertEqual(cert.fine_path_probability,Q(1,2))
        self.assertEqual(cert.coarse_path_probability,Q(1,2))
        self.assertEqual(cert.original_posterior,(0,0,Q(1,2),Q(1,2)))
        self.assertEqual(cert.original_support,frozenset((2,3)))
        self.assertTrue(cert.evidence_equal_at_every_prefix)
        self.assertTrue(cert.original_joint_law_equal_at_every_prefix)
        self.assertTrue(cert.original_target_transport_valid)
        self.assertTrue(original_support_is_monotone(
            src.root(),(change,read),("ok","right")))

    def test_comparison_requires_same_source_and_exact_legal_actual_history(self):
        root_stage=stage(n=2)
        next_stage=stage(n=2,epoch=1,name="next")
        src=same_source(2)
        q0=CarrierQuotient(root_stage,(0,0),"old")
        q1=CarrierQuotient(next_stage,(0,0),"new")
        # Equality of next reports alone does not imply next-state law
        # factorization when hidden receipt probabilities differ.
        noisy=CarrierInstrument("noisy",root_stage,next_stage,("yes","no"),
            (True,True),
            (((0,0,Q(1,4)),(1,1,Q(3,4))),
             ((0,1,Q(3,4)),(1,0,Q(1,4)))))
        with self.assertRaises(CarrierError):
            transport_actual_history(src,q0,
                (CarrierStep(noisy,q0,q1,"yes"),))
        with self.assertRaises(CarrierError):
            transport_actual_history(src,q0,
                (CarrierStep(noisy,q0,q1,"never-happened"),))
        bad_view=CarrierQuotient(next_stage,(0,1),"foreign")
        with self.assertRaises(CarrierError):
            transport_actual_history(src,q0,
                (CarrierStep(noisy,bad_view,q1,"yes"),))

    def test_one_step_information_refinement_is_coarsest_in_all_partitions(self):
        root_stage=stage(n=4)
        after=stage(n=2,epoch=1,name="next")
        before=CarrierQuotient(root_stage,(0,0,1,1),"before")
        future=CarrierQuotient(after,(0,1),"future")
        act=action(root_stage,("ok",)*4,(0,1,1,1),name="reveal-next",
                   final=after)
        repair=repair_one_step(before,((act,future),))
        self.assertTrue(repair.all_declared_one_step_squares_commute)
        self.assertEqual(repair.after.labels,(0,1,2,2))
        self.assertEqual((repair.old_classes,repair.refined_classes,
                          repair.new_information_classes),(2,3,1))
        candidates=[
            part for part in canonical_partitions(4)
            if is_refinement(part,before.labels) and audit_descent(
                act,CarrierQuotient(root_stage,part,"candidate"),future).valid]
        self.assertTrue(candidates)
        self.assertEqual(min(len(set(part)) for part in candidates),3)
        self.assertEqual([p for p in candidates if len(set(p))==3],
                         [repair.after.labels])
        self.assertFalse(audit_descent(act,before,future).valid)

    def test_one_step_repair_keeps_disabled_action_semantics(self):
        st=stage(n=2)
        next_stage=stage(n=1,epoch=1,name="next")
        initial=CarrierQuotient(st,(0,0),"old")
        future=CarrierQuotient(next_stage,(0,),"after")
        act=action(st,("same","same"),(0,0),
                   name="conditional",enabled=(True,False),final=next_stage)
        repair=repair_one_step(initial,((act,future),))
        self.assertEqual(repair.after.labels,(0,1))
        self.assertEqual(repair.new_information_classes,1)
        self.assertTrue(audit_descent(act,repair.after,future).valid)
        self.assertFalse(audit_descent(act,initial,future).valid)

    def test_repeated_action_name_requires_stage_indexed_actual_registry(self):
        before=stage(n=2)
        middle=stage(n=2,epoch=1,name="middle")
        after=stage(n=2,epoch=2,name="after")
        original=same_source(2)
        first=action(before,("ok","ok"),name="read",final=middle)
        second=action(middle,("done","done"),name="read",final=after)
        performed=original.root().advance(first,"ok").advance(second,"done")
        self.assertEqual(len(performed.events),2)
        self.assertTrue(performed.verify({
            ("read","root",0,"middle",1):first,
            ("read","middle",1,"after",2):second,
        }))
        with self.assertRaises(CarrierError):
            performed.verify({"read":second})
        forged=replace(performed,events=(
            performed.events[0],
            replace(performed.events[1],after_epoch=55)))
        with self.assertRaises(CarrierError):
            forged.verify({
                ("read","root",0,"middle",1):first,
                ("read","middle",1,"after",2):second,
            })

    def test_exact_source_negative_controls_do_not_retroactively_update_history(self):
        st=stage(n=2)
        src=same_source(2)
        q=CarrierQuotient(st,(0,1),"current")
        a=action(st,("zero","one"),name="read")
        h=src.root().advance(a,"one")
        self.assertEqual(h.originals_supported,frozenset((1,)))
        self.assertTrue(h.verify({"read":a}))
        with self.assertRaises(CarrierError):
            h.verify({})
        # A forged event probability is rejected; the original belief is immutable.
        fake=replace(h,events=(replace(h.events[0],
                                       conditional_likelihood=Q(1,7)),))
        with self.assertRaises(CarrierError):
            fake.verify({"read":a})
        self.assertEqual(src.root().originals_supported,frozenset((0,1)))



class CarrierPerspectiveForgetfulTests(unittest.TestCase):
    def test_probability_implies_support_descent_but_not_conversely(self):
        st=stage(n=2)
        q=CarrierQuotient(st,(0,0),"forget")
        a=CarrierInstrument(
            "different-laws",st,st,("yes","no"),(True,True),
            (((0,0,Q(1,4)),(1,0,Q(3,4))),
             ((0,1,Q(3,4)),(1,1,Q(1,4)))))
        support=forget_probabilities(a)
        self.assertTrue(possibility_descent(support,q,q))
        self.assertFalse(audit_descent(a,q,q).valid)
        self.assertFalse(deterministic_instrument(a))
        good=action(st,("ok","ok"),name="Dirac")
        self.assertTrue(deterministic_instrument(good))
        self.assertTrue(audit_descent(good,q,q).valid)
        self.assertTrue(possibility_descent(forget_probabilities(good),q,q))

    def test_composition_of_supports_is_source_exact_but_not_a_probability(self):
        start=stage(n=2)
        middle=stage(n=3,epoch=1,name="middle")
        end=stage(n=2,epoch=2,name="end")
        a=CarrierInstrument(
            "A",start,middle,("a","b"),(True,True),
            (((0,0,Q(1,2)),(1,1,Q(1,2))),
             ((0,2,Q(1,2)),(1,1,Q(1,2)))))
        b=CarrierInstrument(
            "B",middle,end,("c","d"),(True,True,True),
            (((0,0,Q(1)),),((1,1,Q(1)),),((0,1,Q(1)),)))
        out=compose_possibilities(forget_probabilities(a),
                                  forget_probabilities(b))
        self.assertEqual(out.before,start)
        self.assertEqual(out.after,end)
        self.assertEqual(out.receipts,
                         (("a","c"),("a","d"),("b","c"),("b","d")))
        # Raw oracle: existentially concatenate the two positive atom tables.
        for source in range(start.count):
            expected=set()
            for z,m,p in a.rows[source]:
                for w,y,q in b.rows[m]:
                    expected.add((out.receipts.index((a.receipts[z],b.receipts[w])),y))
            self.assertEqual(set(out.possible[source]),expected)
        self.assertEqual(tuple(out.enabled),(True,True))

    def test_support_cannot_conjure_invalid_action_from_hidden_availability(self):
        st=stage(n=2)
        first=action(st,("ok","ok"),name="A",enabled=(True,False))
        second=action(st,("ok","ok"),name="B")
        result=compose_possibilities(forget_probabilities(first),
                                     forget_probabilities(second))
        self.assertEqual(result.enabled,(True,False))
        self.assertNotEqual(result.possible[0],())

if __name__=="__main__":
    unittest.main()
