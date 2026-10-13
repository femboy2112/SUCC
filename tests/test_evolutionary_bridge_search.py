"""Genetic proposal != proof. Exhaustive small grammar is independent oracle."""
import unittest
from fractions import Fraction as Q
from observational_succ.relational_model_genetics import (
    Port,Capsule,binary_capsule,PairedSourceTable,GeneticsError,project,
)
from observational_succ.evolutionary_bridge_search import (
    Genome,GeneticSearchReport,genetic_discovery_demo,evolve_bridges,
    evaluate,mutate,crossover,grow_new_model,ternary_fusion_demo,
)
from random import Random


def fixture():
    src='carrier-src'
    a=binary_capsule('A','mechanical',src,'x','y',1)
    b=Capsule('B','thermal',src,0,'binary-v1',
              (Port('temp',('cold','warm')),Port('z',('0','1'))),
              (('cold','1'),('warm','0')))
    table=PairedSourceTable(src,0,'binary-v1',Port('y',('0','1')),
                            Port('temp',('cold','warm')),
                            (('s0','0','cold'),('s1','1','warm')),True)
    return a,b,table

class GeneticTests(unittest.TestCase):
    def test_ten_seeds_find_verified_bridge_and_exact_optimum(self):
        a,b,t=fixture()
        for seed in range(10):
            r=evolve_bridges(a,b,t,seed=seed)
            self.assertIsNotNone(r.discovered_verified_bridge)
            self.assertTrue(r.genetic_reached_bounded_optimum)
            self.assertEqual(project(r.exact_derived_model,('x','z')),(('0','0'),('1','1')))
            self.assertFalse(r.discovered_verified_bridge is None)

    def test_genome_mutation_preserves_bijection_type(self):
        a,b,t=fixture()
        rng=Random(19)
        x=Genome(('cold','warm'),True,True)
        for _ in range(200):
            x=mutate(x,rng)
            self.assertEqual(set(x.permutation),{'cold','warm'})
            y=crossover(x,Genome(('warm','cold'),True,True),rng)
            self.assertEqual(set(y.permutation),{'cold','warm'})

    def test_wrong_mapping_can_be_favored_but_not_certified(self):
        a,b,t=fixture()
        bad=evaluate(Genome(('warm','cold'),True,True),a,b,t)
        self.assertFalse(bad.certified_by_source_table)
        self.assertFalse(bad.verified_pullback)
        self.assertEqual(bad.source_violations,2)

    def test_no_parent_no_new_invariant(self):
        a,b,t=fixture()
        r=evaluate(Genome(('cold','warm'),True,False),a,b,t)
        self.assertEqual(r.new_relations,())
        self.assertFalse(r.verified_pullback)

    def test_incomplete_source_class_never_source_certified(self):
        a,b,t=fixture()
        incomplete=PairedSourceTable(t.source_id,t.epoch,t.basis,t.left_port,t.right_port,
                                     t.observations,False)
        r=evolve_bridges(a,b,incomplete,seed=3)
        self.assertFalse(r.best.certified_by_source_table)
        self.assertIsNone(r.discovered_verified_bridge)
        self.assertIsNone(r.exact_derived_model)

    def test_wrong_epoch_cannot_create_verified_bridge(self):
        a,b,t=fixture()
        bad=PairedSourceTable(t.source_id,2,t.basis,t.left_port,t.right_port,t.observations,True)
        with self.assertRaises(GeneticsError):evolve_bridges(a,b,bad)

    def test_exact_optimum_available_without_stochastic_search_success(self):
        a,b,t=fixture()
        r=evolve_bridges(a,b,t,seed=1,population=4,generations=1)
        self.assertIsInstance(r.exhaustive_optimum,Q)
        self.assertLessEqual(r.best.fitness,r.exhaustive_optimum)

    def test_restricted_resource_input_checks(self):
        a,b,t=fixture()
        with self.assertRaises(GeneticsError):evolve_bridges(a,b,t,population=2)
        with self.assertRaises(GeneticsError):evolve_bridges(a,b,t,generations=0)

    def test_derived_arrow_is_real_new_model(self):
        a,b,t=fixture()
        r=evolve_bridges(a,b,t,seed=4)
        child=grow_new_model(r.exact_derived_model,'x','z')
        self.assertEqual(child.signature(),(('x',('0','1')),('z',('0','1'))))
        self.assertEqual(project(child,('x','z')),(('0','0'),('1','1')))
        self.assertIn('learned-arrow',child.features)

    def test_proof_of_absent_relation_rejected(self):
        a,b,t=fixture()
        r=evolve_bridges(a,b,t,seed=0)
        with self.assertRaises(GeneticsError):grow_new_model(r.exact_derived_model,'z','nonexistent')

    def test_three_symbol_semantic_bridge_born_not_preloaded(self):
        out=ternary_fusion_demo(seed=1)
        self.assertTrue(out['genetic_succeeded'])
        self.assertTrue(out['bounded_optimum_verified'])
        self.assertEqual(out['grammar_size'],24)
        self.assertEqual(out['new_mod3_invariant'],(('0','0'),('1','1'),('2','2')))
        self.assertEqual(out['discovered_bridge'],{'0':'cold','1':'warm','2':'hot'})

    def test_genetic_failure_seed_zero_is_honest_not_a_false_theorem(self):
        out=ternary_fusion_demo(seed=0)
        self.assertFalse(out['genetic_succeeded'])
        self.assertTrue(out['bounded_oracle_rescue_used'])
        self.assertFalse(out['bounded_optimum_verified'])
        self.assertEqual(out['new_mod3_invariant'],(('0','0'),('1','1'),('2','2')))

    def test_twenty_seeded_searches_with_proof_oracle_separated(self):
        results=tuple(ternary_fusion_demo(s) for s in range(20))
        self.assertEqual(sum(x['genetic_succeeded'] for x in results),17)
        self.assertEqual(sum(x['bounded_oracle_rescue_used'] for x in results),3)
        self.assertTrue(all(x['new_mod3_invariant']==(('0','0'),('1','1'),('2','2')) for x in results))

    def test_demo_presents_all_truth_boundaries(self):
        out=genetic_discovery_demo(4)
        self.assertTrue(out['bounded_grammar_optimum_achieved'])
        self.assertTrue(out['probabilistic_fitness_is_not_a_proof'])
        self.assertFalse(out['physical_source_authenticated'])

if __name__=='__main__':unittest.main()
