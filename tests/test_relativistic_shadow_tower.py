"""Exact distributed source-relative Lorentz metric reconstruction tests."""
import unittest
from fractions import Fraction as F
from itertools import permutations,product

from observational_succ.galilean_lorentz_succ import ETA,Mat2,interval_form
from observational_succ.relativistic_shadow_tower import (
    SourceShadows,MetricProbeReceipt,ShadowTowerError,PROBES,VECTOR,
    assemble_metric,finite_source_ontology_limit,shadow_transition_demo,
)

class RelativisticShadowTowerTests(unittest.TestCase):
    def setUp(self):
        self.source=SourceShadows("src","basis-v0",3,ETA)
        self.recs=tuple(self.source.observe(p,owner) for p,owner in zip(PROBES,("A","B","E")))
        self.args={"source_id":"src","basis_id":"basis-v0","version":3}

    def test_two_climbers_cannot_reconstruct_normalized_metric(self):
        r=assemble_metric(self.recs[:2],**self.args)
        self.assertEqual(r['status'],'UNRESOLVED')
        self.assertEqual(r['remaining_probes'],('unit_clock',))
        self.assertEqual(r['remaining_dimensions'],1)

    def test_full_genuine_shadow_triangles_reconstruct_geometry_without_precomputed_metric(self):
        for ordering in permutations(self.recs):
            r=assemble_metric(ordering,**self.args)
            self.assertEqual(r['status'],'GLOBAL_GEOMETRY_CONSTRUCTED')
            self.assertEqual(r['metric'],ETA)
            self.assertTrue(r['matches_minkowski'])
            self.assertFalse(r['externally_authenticated_physics'])

    def test_rational_general_symmetric_sources_reconstruct_own_metric(self):
        for a,b,d in product((F(-2),F(0),F(1,2),F(2)),repeat=3):
            metric=Mat2(a,b,b,d)
            source=SourceShadows('S','B',0,metric)
            recs=[source.observe(p,'observer') for p in PROBES]
            report=assemble_metric(recs,source_id='S',basis_id='B',version=0)
            self.assertEqual(report['metric'],metric)

    def test_conflicting_source_recursively_rejected(self):
        forged=MetricProbeReceipt('src','basis-v0',3,'right_null',F(1),'other')
        result=assemble_metric(self.recs+(forged,),**self.args)
        self.assertEqual(result['status'],'INCONSISTENT_SOURCE')
        self.assertFalse(result['claims_verified'])

    def test_source_mutation_basis_and_epoch_gates(self):
        for changed in (
            MetricProbeReceipt('other','basis-v0',3,'right_null',0,'A'),
            MetricProbeReceipt('src','unknown',3,'right_null',0,'A'),
            MetricProbeReceipt('src','basis-v0',4,'right_null',0,'A')
        ):
            with self.assertRaises(ShadowTowerError):
                assemble_metric(self.recs+(changed,),**self.args)

    def test_shadows_are_data_not_preloaded_geometry(self):
        source=SourceShadows('src','basis-v0',3,Mat2(5,2,2,-7))
        reports=tuple(source.observe(p,'E') for p in PROBES)
        result=assemble_metric(reports,**self.args)
        self.assertFalse(result['matches_minkowski'])
        self.assertEqual(result['metric'],Mat2(5,2,2,-7))

    def test_empty_and_partial_updates_are_finite_not_assumed_global(self):
        self.assertEqual(assemble_metric((),**self.args)['remaining_dimensions'],3)
        for rec in self.recs:
            self.assertEqual(assemble_metric((rec,),**self.args)['remaining_dimensions'],2)

    def test_duplicate_same_valid_report_preserves_proof(self):
        result=assemble_metric(self.recs+(self.recs[0],),**self.args)
        self.assertEqual(result['metric'],ETA)
        self.assertEqual(result['rank'],3)

    def test_unknown_instrument_or_bad_type_rejected(self):
        with self.assertRaises(ShadowTowerError):self.source.observe('forged','A')
        with self.assertRaises(ShadowTowerError):assemble_metric(("not-a-receipt",),**self.args)
        with self.assertRaises(ShadowTowerError):MetricProbeReceipt('src','basis',0,'unit_clock',0.5,'A')

    def test_ontology_is_not_inferred_from_geometry(self):
        r=finite_source_ontology_limit()
        self.assertTrue(r['operationally_equivalent'])
        self.assertTrue(r['ontology_property_differs'])
        self.assertFalse(r['physical_ether_existence_resolved'])

    def test_accumulation_determines_knowledge_not_proper_time(self):
        demo=shadow_transition_demo()
        self.assertEqual(demo['insufficient']['status'],'UNRESOLVED')
        self.assertEqual(demo['constructed']['status'],'GLOBAL_GEOMETRY_CONSTRUCTED')
        self.assertEqual(demo['constructed']['metric'],ETA)

    def test_rational_shadow_replay(self):
        r=assemble_metric(self.recs,**self.args)
        for rec in self.recs:
            self.assertEqual(interval_form(r['metric'],VECTOR[rec.probe]),rec.result)

if __name__=='__main__':unittest.main()
