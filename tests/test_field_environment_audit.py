"""E integrates source/claim/environmental checks without exploding on no source."""
import unittest
from observational_succ.field_relative_closure import FiniteField,ClosureError
from observational_succ.field_environment_audit import inspect_environment
from observational_succ.field_context_descent import SourceVoltageGraph,audit_descent


def field():
    states=((0,0),(0,1),(1,0),(1,1))
    return FiniteField("E-original","basis1",states,
        {"a":(0,0,1,1),"b":(0,1,0,1)},
        {"xor":(0,1,1,0)})

class EnvironmentalIntegrationTests(unittest.TestCase):
    def test_ambiguous_target_returns_exact_rival_and_one_probe_repair(self):
        f=field()
        r=inspect_environment(f,(("a",0),),"xor",candidate_new_probes=("b",))
        self.assertEqual(r.realization_status,"GLOBAL_SOURCE_REALIZED")
        self.assertEqual(r.target_status,"AMBIGUOUS")
        self.assertEqual(r.conflicting_sources,((0,0),(0,1)))
        self.assertEqual(r.repair.selected,("b",))
        self.assertEqual(r.graph_status,"NOT_CHECKED")
        self.assertEqual(r.context_status,"NOT_CHECKED")
        self.assertTrue(r.unverified_external_source)

    def test_a_mathematical_global_proof_does_not_authenticate_carrier(self):
        f=field()
        graph=SourceVoltageGraph("E-original",0,(0,1),((0,1,(5,)),),1)
        r=inspect_environment(f,(("a",0),("b",1)),"xor",graph=graph)
        self.assertEqual(r.target_status,"DETERMINED")
        self.assertEqual(r.proved_target_value,1)
        self.assertEqual(r.graph_status,"GLOBAL_POTENTIAL")
        self.assertTrue(r.unverified_external_source)

    def test_source_realized_target_but_holonomy_still_fails(self):
        f=field()
        graph=SourceVoltageGraph("E-original",0,(0,1,2),
                   ((0,1,(1,)),(1,2,(1,)),(2,0,(1,))),1)
        r=inspect_environment(f,(("a",0),("b",1)),"xor",graph=graph)
        self.assertEqual(r.target_status,"DETERMINED")
        self.assertEqual(r.graph_status,"NONZERO_HOLONOMY")
        self.assertEqual(abs(r.graph_certificate.escape.translation[0]),3)

    def test_unrealized_evidence_must_not_prove_by_explosion(self):
        f=field()
        r=inspect_environment(f,(("a",0),("a",1)),"xor")
        self.assertEqual(r.target_status,"UNREALIZABLE")
        self.assertIsNone(r.proved_target_value)
        self.assertEqual(len(r.inconsistent_core),2)

    def test_frame_covariance_not_a_target_proof(self):
        f=field()
        updated=FiniteField("altered","basis1",(0,),{"a":(0,)},{"xor":(0,)})
        report=audit_descent(f,updated,(0,0,0,0),("a",),("a",),"xor","xor")
        self.assertTrue(report.covariance)
        self.assertFalse(report.truth_square)
        r=inspect_environment(f,(("a",0),),"xor",frame=report)
        self.assertEqual(r.context_status,"CONTEXT_BOUNDARY_FAILURE")

    def test_good_frame_transport_has_its_own_status(self):
        f=field()
        g=FiniteField("updated","basis1",f.states,f.probes,f.targets)
        frame=audit_descent(f,g,tuple(f.states),("a","b"),("a","b"),"xor","xor")
        r=inspect_environment(f,(("a",1),("b",1)),"xor",frame=frame)
        self.assertEqual(r.context_status,"FULLY_TRANSPORTABLE")
        self.assertEqual(r.proved_target_value,0)

    def test_source_mismatch_is_a_precondition_error_not_global_counterexample(self):
        f=field()
        g=SourceVoltageGraph("forged",0,(0,),(),1)
        with self.assertRaisesRegex(ClosureError,"another source"):
            inspect_environment(f,(),"xor",graph=g)

    def test_environmental_empty_received_history_ambiguous_not_false(self):
        f=field()
        r=inspect_environment(f,(),"xor")
        self.assertEqual(r.target_status,"AMBIGUOUS")
        self.assertEqual(len(r.compatible_states),4)

if __name__=='__main__':unittest.main()
