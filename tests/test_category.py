"""Finite Yoneda and bridge tests: exact, no zeta zeros."""
import unittest

from observational_succ.core import BudgetExceeded, DomainError
from observational_succ.yoneda import (
    Arrow, DivisibilityCategory, PathCategory, FiniteFunctor, CompanionBridge,
    ValuationCategory, valuation_bridge, forget_path_bridge,
    restricted_yoneda, representable_natural_transform,
    enumerate_natural_transforms, validate_yoneda,
    co_yoneda_companion, verify_companion_actions)


class YonedaTests(unittest.TestCase):
    def test_thin_category_composition(self):
        c = DivisibilityCategory((1, 2, 3, 6, 12))
        self.assertEqual(len(c.hom(2, 3)), 0)
        self.assertEqual(c.compose(c.hom(6, 12)[0], c.hom(2, 6)[0]), c.hom(2, 12)[0])
        self.assertEqual(c.compose(c.identity(2),c.identity(2)),c.identity(2))
        with self.assertRaises(DomainError):
            c.compose(c.hom(1, 2)[0], c.hom(1, 3)[0])

    def test_path_category_keeps_distinct_histories(self):
        c = PathCategory(range(1, 13), (2, 3))
        paths6 = c.hom(1, 6)
        paths12 = c.hom(1, 12)
        self.assertEqual({x.word for x in paths6}, {(2,3),(3,2)})
        self.assertEqual({x.word for x in paths12}, {(2,2,3),(2,3,2),(3,2,2)})
        self.assertEqual(c.compose(c.hom(2,6)[0],c.hom(1,2)[0]),Arrow(1,6,(2,3)))
        self.assertEqual(c.compose(c.identity(6),paths6[0]),paths6[0])
        self.assertEqual(c.compose(paths6[0],c.identity(1)),paths6[0])

    def test_path_associativity_and_coherence(self):
        c = PathCategory(range(1, 13), (2, 3))
        first=c.hom(1,2)[0]
        second=c.hom(2,4)[0]
        third=c.hom(4,12)[0]
        self.assertEqual(c.compose(third,c.compose(second,first)),
                         c.compose(c.compose(third,second),first))
        self.assertEqual(c.compose(third,c.compose(second,first)).word,(2,2,3))

    def test_bounded_path_exploration_not_false_no_paths(self):
        with self.assertRaises(BudgetExceeded):
            PathCategory(range(1, 13), (2,3),max_depth=1).hom(1,6)
        with self.assertRaises(BudgetExceeded):
            PathCategory(range(1, 13), (2,3),max_paths=1).hom(1,6)
        with self.assertRaises(DomainError):
            PathCategory(range(1,13), (2,1))

    def test_full_yoneda_finite_path_and_thin(self):
        c=PathCategory(range(1,7),(2,3))
        report=validate_yoneda(c,1,6)
        self.assertEqual(report['source_hom_count'],2)
        self.assertEqual(report['natural_transform_count'],2)
        self.assertTrue(report['surjective'])
        t=DivisibilityCategory((1,2,3,6))
        self.assertEqual(validate_yoneda(t,2,3)['natural_transform_count'],0)
        self.assertEqual(validate_yoneda(t,1,6)['natural_transform_count'],1)

    def test_restricted_yoneda_spurious_morphism(self):
        c=DivisibilityCategory((1,2,3,6))
        local=validate_yoneda(c,2,3,(1,))
        self.assertEqual(local['source_hom_count'],0)
        self.assertEqual(local['natural_transform_count'],1)
        self.assertFalse(local['surjective'])
        global_report=validate_yoneda(c,2,3)
        self.assertEqual(global_report['natural_transform_count'],0)

    def test_shadow_objects_indistinguishable_under_thin_probes(self):
        c=DivisibilityCategory(range(1,13))
        self.assertEqual(restricted_yoneda(c,6,(1,2,3)),
                         restricted_yoneda(c,12,(1,2,3)))
        self.assertNotEqual(restricted_yoneda(c,6,(1,2,3,4)),
                            restricted_yoneda(c,12,(1,2,3,4)))
        paths=PathCategory(range(1,13),(2,3))
        self.assertEqual(len(restricted_yoneda(paths,6,(1,))[0]),2)
        self.assertEqual(len(restricted_yoneda(paths,12,(1,))[0]),3)

    def test_path_forgetting_is_functor_but_not_faithful(self):
        c=PathCategory(range(1,13),(2,3))
        f=forget_path_bridge(c)
        report=f.verify()
        self.assertGreater(report['composable_pairs_checked'],0)
        self.assertFalse(f.hom_faithfulness()['faithful'])
        h1,h2=c.hom(1,6)
        self.assertNotEqual(h1,h2)
        self.assertEqual(f.arrow_image(h1),f.arrow_image(h2))

    def test_formal_log_valuation_bridge_is_fully_faithful(self):
        c=DivisibilityCategory((1,2,3,4,6,8,9,12,18,36))
        f=valuation_bridge(c)
        self.assertTrue(f.verify()['composable_pairs_checked']>0)
        self.assertTrue(f.hom_faithfulness()['full'])
        self.assertTrue(f.hom_faithfulness()['faithful'])
        a=f.arrow_image(c.hom(1,2)[0])
        b=f.arrow_image(c.hom(2,12)[0])
        composed=f.target.compose(b,a)
        self.assertEqual(composed.word,(2,2,3))
        self.assertEqual(f.target.grade(composed),tuple(sorted(a.word+b.word)))
        with self.assertRaises(DomainError):
            f.target.grade(Arrow(a.source,a.target,(3,)))  # false log 2

    def test_functor_rejects_fake_arrow_and_wrong_composition(self):
        c=PathCategory(range(1,7),(2,3))
        bad=FiniteFunctor(c,DivisibilityCategory(range(1,7)),lambda x:x,
                          lambda arrow: Arrow(arrow.source,arrow.source))
        with self.assertRaises(DomainError):bad.verify()
        flip=FiniteFunctor(c,c,lambda x:x,
             lambda arrow: Arrow(arrow.source,arrow.target,
                                tuple(reversed(arrow.word)) if len(arrow.word)==2 else arrow.word))
        with self.assertRaises(DomainError):flip.verify()

    def test_companion_profunctor_naturality_interchange(self):
        source=PathCategory(range(1,13),(2,3))
        f=forget_path_bridge(source)
        bridge=CompanionBridge(f)
        x=source.hom(1,2)[0]
        middle=f.target.hom(2,6)[0]
        y=f.target.hom(6,12)[0]
        self.assertTrue(bridge.verify_interchange(x,middle,y))
        self.assertEqual(bridge.left_action(x,middle), f.target.hom(1,6)[0])
        self.assertEqual(bridge.right_action(y,middle), f.target.hom(2,12)[0])

    def test_co_yoneda_reconstructs_bridge_from_history_witnesses(self):
        source=PathCategory(range(1,7),(2,3))
        bridge=CompanionBridge(forget_path_bridge(source))
        result=co_yoneda_companion(bridge,1,6)
        self.assertEqual(result['raw_witness_pairs'],5)
        self.assertEqual(result['equivalence_classes'],1)
        self.assertEqual(result['target_hom_count'],1)
        self.assertEqual(result['forgotten_history_classes'],4)
        self.assertEqual(verify_companion_actions(bridge)['status'],
                         'verified_finite_companion_actions')

    def test_co_yoneda_valuation_target_and_resource_budget(self):
        c=DivisibilityCategory((1,2,3,6))
        bridge=CompanionBridge(valuation_bridge(c))
        target=bridge.functor.object_image(6)
        self.assertEqual(co_yoneda_companion(bridge,1,target)['equivalence_classes'],1)
        with self.assertRaises(BudgetExceeded):
            co_yoneda_companion(bridge,1,target,max_pairs=1)
        with self.assertRaises(BudgetExceeded):
            co_yoneda_companion(bridge,1,target,max_relations=1)
        with self.assertRaises(BudgetExceeded):
            verify_companion_actions(bridge,max_checks=1)

    def test_representable_transform_commutes_with_context_composition(self):
        c=PathCategory(range(1,7),(2,3))
        arrow=c.hom(2,6)[0]
        eta=representable_natural_transform(c,arrow,c.objects)
        k=c.hom(1,2)[0]
        self.assertEqual(eta[1][k],c.compose(arrow,k))
        self.assertIn(eta,enumerate_natural_transforms(c,2,6,c.objects))


if __name__ == '__main__':
    unittest.main()
