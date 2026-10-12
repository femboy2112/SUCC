"""No inherited global potential: autonomous local charts and E gluing."""
import unittest
from dataclasses import replace
from observational_succ.local_global_descent import Dart, VoltageSource, edge_chart_cover
from observational_succ.constructive_gluing_tower import (
    IndependentPatchTower, GluingTowerError, gaussian_voltage_source,run_diagonal_tower
)
from observational_succ.gaussian_holonomy import GaussianSieve, quotient_holonomy


def triangle(escape):
    verts=((0,),(1,),(2,))
    return VoltageSource('triangle',verts,
        (Dart('a',verts[0],verts[1],(1,)),Dart('b',verts[1],verts[2],(1,)),
         Dart('c',verts[2],verts[0],(1 if escape else -2,))),1,3)


class IndependentTowerTests(unittest.TestCase):
    def test_independent_triangle_gluing_at_E(self):
        graph=triangle(False)
        tower=run_diagonal_tower(graph,levels=2,patches=edge_chart_cover(graph))
        self.assertFalse(hasattr(tower,'potentials'))
        cert=tower.proof_at_E()
        self.assertEqual(cert.status,'GLUED')
        self.assertEqual(cert.largest_component,3)
        self.assertEqual(cert.checked_darts,3)
        self.assertEqual(cert.epistemic_macros_at_E,1)
        self.assertEqual(len(tower.result.global_potential),3)
        with self.assertRaisesRegex(GluingTowerError,'already'):
            tower.proof_at_E()

    def test_independent_triangle_failure_constructs_an_actual_source_walk(self):
        graph=triangle(True)
        tower=run_diagonal_tower(graph,levels=2,patches=edge_chart_cover(graph))
        cert=tower.proof_at_E()
        self.assertEqual(cert.status,'OBSTRUCTED')
        self.assertEqual(abs(cert.obstruction[0]),3)
        self.assertGreaterEqual(cert.expanded_obstruction_steps,3)
        self.assertIsNone(cert.largest_component)

    def test_missing_diagonal_proof_is_not_equivalent_to_full_source(self):
        graph=triangle(False)
        tower=run_diagonal_tower(graph,levels=2,patches=edge_chart_cover(graph),complete=False)
        with self.assertRaisesRegex(GluingTowerError,'complete lawful'):
            tower.proof_at_E()

    def test_bad_source_digest_and_corrupt_local_chart_rejected(self):
        graph=triangle(False)
        for kind in ('source','potential','origin','parents'):
            tower=run_diagonal_tower(graph,levels=2,patches=edge_chart_cover(graph))
            rec=tower.issued['edge-0']
            if kind=='source':bad=replace(rec,source_digest='wrong')
            elif kind=='origin':bad=replace(rec,origin='B0')
            elif kind=='parents':bad=replace(rec,parents=('fictional',))
            else:
                ch=rec.chart
                potentials=tuple((v, tuple(k+5 for k in coords)) if i==1 else (v,coords)
                                 for i,(v,coords) in enumerate(ch.potentials))
                bad=replace(rec,chart=replace(ch,potentials=potentials))
            tower.issued['edge-0']=bad
            with self.assertRaises(GluingTowerError):
                tower.proof_at_E()

    def test_replay_not_just_eventual_possession(self):
        graph=triangle(False)
        tower=run_diagonal_tower(graph,levels=2,patches=edge_chart_cover(graph))
        # Giving E possession without an actual licensed communication violates replay.
        tower.actions=[a for a in tower.actions if not(a[0]=='relay' and a[2]=='E')]
        with self.assertRaisesRegex(GluingTowerError,'disagree'):
            tower.proof_at_E()

    def test_cannot_climb_before_lower_floor_support(self):
        graph=triangle(False)
        tower=IndependentPatchTower(graph,levels=2,patches=edge_chart_cover(graph))
        with self.assertRaisesRegex(GluingTowerError,'lacks lawful'):
            tower.construct_at('A1','edge-2')
        with self.assertRaises(GluingTowerError):
            tower.relay('E','A0',('edge-0',))

    def test_real_gaussian_crt_sieve_constructs_global_without_candidate(self):
        sieve=GaussianSieve(((1,2),(2,3)))
        source=gaussian_voltage_source(sieve,1)
        tower=run_diagonal_tower(source,levels=3)
        self.assertEqual(len(tower.issued),462)
        self.assertEqual(len(tower.actions)-len(tower.issued),14)
        cert=tower.proof_at_E()
        self.assertEqual(cert.status,'GLUED')
        self.assertEqual(cert.checked_vertices,2304)
        self.assertEqual(cert.checked_darts,4356)
        self.assertEqual(cert.overlap_conditions,2280)
        self.assertEqual(cert.largest_component,580)
        self.assertEqual(len(tower.result.global_potential),2304)
        self.assertEqual(quotient_holonomy(sieve,1).largest_finite_quotient_component,580)

    def test_false_arithmetic_factor_rejected_before_tower_build(self):
        with self.assertRaises(Exception):
            gaussian_voltage_source(GaussianSieve(((3,4),)),1)


if __name__=='__main__': unittest.main()
