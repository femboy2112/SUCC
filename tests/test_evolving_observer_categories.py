from dataclasses import replace
from itertools import product, combinations
from random import Random
import unittest
from observational_succ.evolving_observer_categories import (
    Action, Readout, FiniteDynamics, Experiment, SynthesisError, partition, refines,
    discover_representation, verify_quotient, first_defect, factor_map,
    pair_automaton_partition, observed_partition, ObstructionArchive,
    join_partitions, adjunction_holds, transformation_monoid,
)


def register():
    states = list(product((0, 1), repeat=3))
    return FiniteDynamics('register', 0, 'bits',
        (Action('rotate', tuple(states.index((y, z, x)) for x,y,z in states)),),
        (Readout('first', tuple(x for x,y,z in states)),))


def partitions(n):
    def rec(p):
        if len(p) == n:
            yield tuple(p)
        else:
            for k in range(max(p, default=-1)+2):
                yield from rec(p+[k])
    yield from rec([])


class EvolvingObserverCategoryTests(unittest.TestCase):
    def test_new_tests_are_constructed_from_source_defects(self):
        s=register(); q=discover_representation(s)
        self.assertEqual(q.block_counts,(2,4,8))
        self.assertEqual([len(t.word) for t in q.tests],[0,1,2])
        self.assertTrue(verify_quotient(s,q))

    def test_generator_squares_imply_all_fresh_words(self):
        s=register(); q=discover_representation(s)
        for length in (7,19,101):
            for x in range(8):
                k=q.labels[x]
                for _ in range(length): k=q.actions[0].after[k]
                self.assertEqual(q.readouts[0].values[k],s.readouts[0].values[s.run(x,('rotate',)*length)])

    def test_complete_source_checker_matches_different_pair_oracle(self):
        rng=Random(92451)
        for _ in range(160):
            n=rng.randrange(2,9)
            s=FiniteDynamics('rnd',0,'v',tuple(Action(str(k),tuple(rng.randrange(n) for _ in range(n))) for k in range(2)),
                (Readout('r',tuple(rng.randrange(3) for _ in range(n))),))
            q=discover_representation(s,seed=rng.randrange(10000))
            self.assertEqual(q.labels,pair_automaton_partition(s))
            self.assertLessEqual(len(q.witnesses),n-q.block_counts[0])

    def test_minimality_compared_against_every_partition(self):
        rng=Random(42)
        for _ in range(40):
            n=4
            s=FiniteDynamics('all-partitions',0,'v',(Action('a',tuple(rng.randrange(n) for _ in range(n))),),
                             (Readout('r',tuple(rng.randrange(2) for _ in range(n))),))
            q=discover_representation(s)
            for p in partitions(n):
                observable=all(p[x]!=p[y] or s.readouts[0].values[x]==s.readouts[0].values[y] for x in range(n) for y in range(n))
                stable=all(p[x]!=p[y] or p[s.actions[0].after[x]]==p[s.actions[0].after[y]] for x in range(n) for y in range(n))
                if observable and stable:
                    self.assertTrue(refines(p,q.labels))
                    f=factor_map(p,q.labels)
                    self.assertEqual(tuple(f[k] for k in p),q.labels)

    def test_repair_commutes_with_fusion_on_same_carrier(self):
        rng=Random(4401)
        for _ in range(70):
            n=5
            actions=(Action('a',tuple(rng.randrange(n) for _ in range(n))),)
            l=Readout('l',tuple(rng.randrange(2) for _ in range(n)))
            r=Readout('r',tuple(rng.randrange(2) for _ in range(n)))
            ql=discover_representation(FiniteDynamics('same',0,'v',actions,(l,)))
            qr=discover_representation(FiniteDynamics('same',0,'v',actions,(r,)))
            q=discover_representation(FiniteDynamics('same',0,'v',actions,(l,r)))
            self.assertEqual(q.labels,join_partitions(ql.labels,qr.labels))

    def test_all_word_alias_retains_hidden_copies(self):
        s=FiniteDynamics('copies',0,'v',(Action('flip',(1,0,3,2)),), (Readout('r',(0,1,0,1)),))
        q=discover_representation(s)
        self.assertEqual(q.states,2)
        self.assertEqual(q.labels,(0,1,0,1))
        self.assertFalse(refines(q.labels,(0,1,2,3)))

    def test_counterexample_is_hard_constraint_not_fitness(self):
        s=register(); seeds=(Experiment((),'first'),)
        bad=first_defect(s,seeds)
        book=ObstructionArchive(s); book.learn(bad)
        self.assertFalse(book.admits(observed_partition(s,seeds)))
        self.assertTrue(book.admits(discover_representation(s).labels))

    def test_archive_rejects_false_witness(self):
        s=register(); w=first_defect(s,(Experiment((),'first'),))
        with self.assertRaises(SynthesisError): ObstructionArchive(s).learn(replace(w,outcomes=(0,0)))

    def test_archive_cannot_be_replayed_across_interventions(self):
        s=register(); w=first_defect(s,(Experiment((),'first'),))
        changed=replace(s,version=1)
        with self.assertRaises(SynthesisError): ObstructionArchive(changed).learn(w)

    def test_certificate_binds_source_and_toolkit(self):
        s=register(); q=discover_representation(s)
        with self.assertRaises(SynthesisError): verify_quotient(replace(s,version=1),q)
        with self.assertRaises(SynthesisError): verify_quotient(replace(s,actions=(Action('rotate',tuple(range(8))),)),q)

    def test_forged_quotient_edge_is_rejected(self):
        s=register();q=discover_representation(s)
        with self.assertRaises(SynthesisError):verify_quotient(s,replace(q,actions=(Action('rotate',tuple(range(8))),)))

    def test_forged_grammar_trace_is_rejected(self):
        s=register();q=discover_representation(s)
        with self.assertRaises(SynthesisError):verify_quotient(s,replace(q,block_counts=(2,3,8)))
        with self.assertRaises(SynthesisError):verify_quotient(s,replace(q,witnesses=tuple(reversed(q.witnesses))))

    def test_no_growth_is_not_a_proof_of_impossibility(self):
        with self.assertRaisesRegex(SynthesisError,'UNRESOLVED'):
            discover_representation(register(),max_refinements=0)

    def test_primitive_context_validates_full_domains(self):
        with self.assertRaises(SynthesisError):FiniteDynamics('x',0,'v',(Action('bad',(0,2)),),(Readout('r',(0,1)),))
        with self.assertRaises(SynthesisError):FiniteDynamics('x',0,'v',(),(Readout('r',(0,1)),))
        with self.assertRaises(SynthesisError):FiniteDynamics('',0,'v',(Action('a',(0,1)),),(Readout('r',(0,1)),))

    def test_no_unlicensed_experiment(self):
        with self.assertRaises(SynthesisError):Experiment(('alien',),'first').values(register())

    def test_comparison_maps_compose_naturally(self):
        a=(0,1,2,3);b=(0,0,1,1);c=(0,0,0,0)
        ab=factor_map(a,b);bc=factor_map(b,c);ac=factor_map(a,c)
        self.assertEqual(tuple(bc[k] for k in ab),ac)
        with self.assertRaises(SynthesisError):factor_map(c,b)

    def test_actual_predicate_adjunction_exhaustive(self):
        for f in product(range(2),repeat=3):
            for bits in product((False,True),repeat=3):
                p=frozenset(i for i,b in enumerate(bits) if b)
                for qbits in product((False,True),repeat=2):
                    q=frozenset(i for i,b in enumerate(qbits) if b)
                    self.assertTrue(adjunction_holds(f,p,q))

    def test_repaired_object_is_idempotent(self):
        s=register();q=discover_representation(s)
        qs=FiniteDynamics('quotient',0,'v',q.actions,q.readouts)
        second=discover_representation(qs)
        self.assertEqual(second.states,q.states)
        self.assertEqual(len(second.witnesses),2)

    def test_constant_readout_does_not_invent_knowledge(self):
        s=FiniteDynamics('dark',0,'v',(Action('a',(1,2,0)),),(Readout('r',(0,0,0)),))
        q=discover_representation(s)
        self.assertEqual(q.states,1)
        self.assertEqual(len(q.witnesses),0)

    def test_transformation_monoid_preserves_noninvertible_maps(self):
        s=FiniteDynamics('erase',0,'v',(Action('erase',(0,0)),),(Readout('r',(0,1)),))
        q=discover_representation(s);m=transformation_monoid(q)
        self.assertFalse(m['is_group']);self.assertEqual(len(m['elements']),2)

    def test_proposal_audits_never_erase_obstruction_repair(self):
        for seed in range(20):
            q=discover_representation(register(),seed=seed,proposal_audits=12)
            self.assertEqual(q.states,8)
            self.assertTrue(any(not ok for _,ok in q.candidate_trace))

if __name__=='__main__':unittest.main()
