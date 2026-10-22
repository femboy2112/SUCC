"""Exact finite boundary selection, fake pin, and hostile same-DtN source tests."""
import unittest
from fractions import Fraction as Q
from observational_succ.boundary_realization_selection import (
    BoundarySourceError, FiniteNetwork, PredictedBranch, BoundaryObservation,
    matrix_inverse, boundary_response, boundary_glue,
    conductance_from_two_terminal_response, surviving_branches,
    eligible_empirical_pin, modeled_alpha_anchor_rejection,
)


def resistor(conductance):
    return FiniteNetwork(2,(0,1),((0,1,conductance),))


def series_path(capacitance=1):
    return FiniteNetwork(3,(0,2),((0,1,Q(1)),(1,2,Q(1))),
                         ((1,Q(capacitance)),))


class BoundarySchurTests(unittest.TestCase):
    def test_exact_schur_complement_series_and_direct_same_static_DtN(self):
        a=boundary_response(resistor(Q(1,2)),0)
        b=boundary_response(series_path(),0)
        self.assertEqual(a,b)
        self.assertEqual(a,((Q(1,2),-Q(1,2)),(-Q(1,2),Q(1,2))))
        self.assertEqual(conductance_from_two_terminal_response(a),Q(1,2))

    def test_dynamic_heldout_boundary_response_splits_same_DC_models(self):
        a=boundary_response(resistor(Q(1,2)),1)
        b=boundary_response(series_path(),1)
        self.assertEqual(a,((Q(1,2),-Q(1,2)),(-Q(1,2),Q(1,2))))
        self.assertEqual(b,((Q(2,3),-Q(1,3)),(-Q(1,3),Q(2,3))))
        self.assertNotEqual(a,b)

    def test_capacitance_mutation_changes_dynamic_only(self):
        self.assertEqual(boundary_response(series_path(0),0),
                         boundary_response(series_path(17),0))
        self.assertNotEqual(boundary_response(series_path(1),1),
                            boundary_response(series_path(3),1))

    def test_two_interface_responses_glue_by_sum_of_fluxes(self):
        a=boundary_response(resistor(Q(1,3)))
        b=boundary_response(resistor(Q(1,2)))
        glued=boundary_glue(a,b)
        self.assertEqual(glued,((Q(5,6),-Q(5,6)),(-Q(5,6),Q(5,6))))
        self.assertEqual(conductance_from_two_terminal_response(glued),Q(5,6))

    def test_static_energy_response_is_symmetric_and_has_zero_constant_flux(self):
        for net in (resistor(Q(5,7)),series_path(),series_path(0)):
            M=boundary_response(net)
            self.assertEqual(M[0][1],M[1][0])
            self.assertEqual(sum(M[0]),0)
            self.assertEqual(sum(M[1]),0)
            self.assertGreaterEqual(M[0][0],0)

    def test_exact_inverse_and_internal_singularity_fail_closed(self):
        self.assertEqual(matrix_inverse(((Q(2),Q(-1)),(Q(-1),Q(2)))),
                         ((Q(2,3),Q(1,3)),(Q(1,3),Q(2,3))))
        with self.assertRaises(BoundarySourceError):
            matrix_inverse(((Q(1),Q(1)),(Q(2),Q(2))))
        net=FiniteNetwork(3,(0,1),((0,1,Q(1)),))
        with self.assertRaises(BoundarySourceError):
            boundary_response(net)

    def test_static_observational_equivalence_not_topological_isomorphism(self):
        direct=resistor(Q(1,2))
        series=series_path()
        self.assertNotEqual(direct.count,series.count)
        for _ in range(10):
            self.assertEqual(boundary_response(direct,0),
                             boundary_response(series,0))


class ObservationPinnedRigidityTests(unittest.TestCase):
    def test_scalar_observation_selects_class_if_all_other_classes_separated(self):
        models=(
            PredictedBranch("direct","class-d",Q(1,2)),
            PredictedBranch("left","class-l",Q(1,3)),
            PredictedBranch("right","class-r",Q(3,4)),
        )
        obs=BoundaryObservation(Q(1,2),Q(1,100))
        result=surviving_branches(models,obs)
        self.assertEqual(result["survivors"],("direct",))
        self.assertTrue(result["unique_class_within_declared_family"])
        self.assertFalse(result["candidate_family_complete_in_reality"])

    def test_same_full_static_response_does_not_pin_unique_interior(self):
        models=(
            PredictedBranch("edge","edge-topology",Q(1,2)),
            PredictedBranch("path","path-topology",Q(1,2)),
            PredictedBranch("other","other-topology",Q(1,3)),
        )
        obs=BoundaryObservation(Q(1,2),Q())
        result=surviving_branches(models,obs)
        self.assertEqual(result["survivors"],("edge","path"))
        self.assertFalse(result["unique_class_within_declared_family"])

    def test_second_independent_dynamic_boundary_probe_can_split_survivors(self):
        static_branches=(
            PredictedBranch("edge","edge-topology",Q(1,2)),
            PredictedBranch("path","path-topology",Q(1,2))
        )
        first=surviving_branches(static_branches,BoundaryObservation(Q(1,2),Q()))
        self.assertFalse(first["unique_class_within_declared_family"])
        dynamic_branches=(
            PredictedBranch("edge","edge-topology",
                            boundary_response(resistor(Q(1,2)),1)[0][1]),
            PredictedBranch("path","path-topology",
                            boundary_response(series_path(),1)[0][1]),
        )
        second=surviving_branches(dynamic_branches,BoundaryObservation(Q(-1,3),Q(1,100)))
        self.assertTrue(second["unique_class_within_declared_family"])
        self.assertEqual(second["survivors"],("path",))

    def test_exact_interval_precision_controls_boundary_rival_mass(self):
        models=(
            PredictedBranch("one","a",Q(1,2)),
            PredictedBranch("two","b",Q(51,100))
        )
        self.assertEqual(len(surviving_branches(models,BoundaryObservation(Q(1,2),Q(1,100)))["survivors"]),2)
        self.assertEqual(surviving_branches(models,BoundaryObservation(Q(1,2),Q(1,1000)))["survivors"],("one",))

    def test_theory_error_and_measurement_error_are_added_not_confused(self):
        a=PredictedBranch("M","M",Q(1,3),Q(1,30))
        self.assertEqual(surviving_branches((a,),BoundaryObservation(Q(2,5),Q(1,30)))["survivors"],("M",))
        self.assertEqual(surviving_branches((a,),BoundaryObservation(Q(1,2),Q(1,30)))["survivors"],())

    def test_source_provenance_is_not_physically_certified_from_metadata(self):
        m=PredictedBranch("model","model",Q(1,2))
        x=BoundaryObservation(Q(1,2),Q(0),"physical_transcript",
                              "claimed_scope","claimed_device",True,True)
        y=surviving_branches((m,),x)
        e=eligible_empirical_pin(y,x)
        self.assertTrue(e["candidate_fiber_is_unique"])
        self.assertTrue(e["reported_provenance_complete"])
        self.assertFalse(e["measurement_independently_authenticated"])
        self.assertFalse(e["global_physical_geometry_proved"])

    def test_post_fitted_or_synthetic_constant_not_independent_reality_pin(self):
        m=PredictedBranch("fitted_lambda","unknown-geometry",Q(1,2))
        obs=BoundaryObservation(Q(1,2),Q(),"synthetic","","",False,False)
        state=surviving_branches((m,),obs)
        self.assertFalse(eligible_empirical_pin(state,obs)["reported_provenance_complete"])
        self.assertTrue(modeled_alpha_anchor_rejection()["free_parameter_matching_data_is_not_a_prediction"])

    def test_parameter_gauge_equivalence_can_be_unique_despite_multiple_representatives(self):
        m=(PredictedBranch("gauge-A","same-physical-class",Q(1,2)),
           PredictedBranch("gauge-B","same-physical-class",Q(1,2)))
        r=surviving_branches(m,BoundaryObservation(Q(1,2),Q()))
        self.assertTrue(r["unique_class_within_declared_family"])
        self.assertEqual(len(r["survivors"]),2)

    def test_invalid_graph_and_fake_numeric_evidence_fail_closed(self):
        with self.assertRaises(BoundarySourceError):
            FiniteNetwork(2,(0,0),((0,1,Q(1)),))
        with self.assertRaises(BoundarySourceError):
            FiniteNetwork(2,(0,1),((0,1,0.5),))
        with self.assertRaises(BoundarySourceError):
            BoundaryObservation(Q(1,2),Q(-1))
        with self.assertRaises(BoundarySourceError):
            BoundaryObservation(Q(1,2),0,"verified_by_magic")
        with self.assertRaises(BoundarySourceError):
            PredictedBranch("M","M",Q(1,2),-Q(1,10))


if __name__=="__main__":
    unittest.main()
