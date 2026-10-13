"""Exact hostile tests for typed reusable categorical model capsules and discovered adapters."""
import random
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.dynamic_boundary_inverse import (
    RCNetwork,star,triangle,twin_hubs,serial_pendant,
)
from observational_succ.categorical_repair_synthesis import positive_passive_alias
from observational_succ.categorical_model_bridges import (
    ModelCapsule,BridgeError,certify_all_frequency,thermal_correspondence,
    build_markov_bridge,derivative_sign_certificates,finite_passivity_shadow_test,
    parallel_network,parallel_context_response,feedback_response,
    context_reuse_receipt,categorical_bridge_demo,discover_model_connections,context_depth_witness,
    boundary_taylor_jet,feedback_jet,graded_context_substitution,
)


def capsule(network, *,domain="electrical_RC",source_id="same-original",epoch=0,basis_id="3-port"):
    return ModelCapsule(network,domain,source_id,epoch,basis_id)


class ContextualAbstractionTests(unittest.TestCase):
    def test_complete_dynamic_star_twin_are_reusable(self):
        a,b=capsule(star()),capsule(twin_hubs())
        x=certify_all_frequency(a,b)
        self.assertTrue(x.equivalent)
        self.assertEqual(x.degree_bound,3)
        self.assertEqual(x.test_points,tuple(map(Q,range(4))))
        for s in (0,1,2,3,4,11,17,100):
            self.assertEqual(a.response(s),b.response(s))

    def test_static_y_delta_not_dynamic_contextual_equivalence(self):
        a,b=capsule(star()),capsule(triangle())
        self.assertEqual(a.response(0),b.response(0))
        w=certify_all_frequency(a,b)
        self.assertFalse(w.equivalent)
        self.assertEqual(w.witness[0],Q(1))
        self.assertNotEqual(a.response(1),b.response(1))

    def test_composition_preserves_verified_black_box_equivalence(self):
        a,b=capsule(star()),capsule(twin_hubs())
        third=triangle()
        x=context_reuse_receipt(a,b,third,feedback_strength=Q(3,5))
        self.assertTrue(x["parallel_all_frequency_equivalent"])
        self.assertTrue(x["feedback_equal"])
        for s in (0,1,5,21):
            lhs=parallel_network(a.network,third).response(s)
            rhs=parallel_network(b.network,third).response(s)
            self.assertEqual(lhs,rhs)
            self.assertEqual(feedback_response(a,s,Q(3,5)),
                             feedback_response(b,s,Q(3,5)))

    def test_parallel_rc_conductances_sum_for_distinct_networks(self):
        s=star();t=triangle()
        out=parallel_network(s,t)
        for z in (0,1,2,7,Q(1,2)):
            self.assertEqual(out.response(z),parallel_context_response(s,t,z))
        self.assertEqual(len(out.interior),1)

    def test_parallel_associative_for_boundary_black_boxes(self):
        a,b,c=star(cap=2),twin_hubs(cap=3),triangle()
        left=parallel_network(parallel_network(a,b),c)
        right=parallel_network(a,parallel_network(b,c))
        for s in (0,1,5):self.assertEqual(left.response(s),right.response(s))

    def test_hidden_intervention_can_destroy_black_box_equivalence(self):
        first=star()
        twin=twin_hubs()
        modified=RCNetwork("one-hub-intervened",twin.vertices,twin.boundary,
            twin.edges,(("h0",Q(3,2)),("h1",Q(1))))
        self.assertNotEqual(first.response(1),modified.response(1))
        self.assertFalse(certify_all_frequency(capsule(first),capsule(modified)).equivalent)

    def test_context_source_epoch_basis_and_units_are_not_free(self):
        a=capsule(star())
        with self.assertRaises(BridgeError):certify_all_frequency(a,capsule(twin_hubs(),epoch=1))
        with self.assertRaises(BridgeError):certify_all_frequency(a,capsule(twin_hubs(),source_id="rival"))
        with self.assertRaises(BridgeError):certify_all_frequency(a,capsule(twin_hubs(),basis_id="opposite"))
        with self.assertRaises(BridgeError):certify_all_frequency(a,capsule(twin_hubs(),domain="thermal_diffusion"))
        with self.assertRaises(BridgeError):certify_all_frequency(a,capsule(twin_hubs()),adapter="fake")
        with self.assertRaises(BridgeError):feedback_response(a,1,-1)

    def test_bad_port_names_cannot_be_unseen(self):
        net=RCNetwork("permuted",("a","b","c","h"),("c","b","a"),
            star().edges,star().capacitors)
        with self.assertRaises(BridgeError):certify_all_frequency(capsule(star()),capsule(net))

    def test_cross_domain_link_is_math_not_shared_physics(self):
        a=capsule(serial_pendant())
        adapter=thermal_correspondence(a,new_source_id="separate-thermal-model")
        th=adapter["target"]
        self.assertEqual(th.domain,"thermal_diffusion")
        self.assertNotEqual(th.source_id,a.source_id)
        self.assertFalse(adapter["same_physical_carrier_asserted"])
        self.assertFalse(adapter["same_empirical_units_asserted"])
        cert=certify_all_frequency(a,th,adapter="thermal_electrical_law")
        self.assertTrue(cert.equivalent)
        self.assertFalse(cert.physical_source_identity_authenticated)
        self.assertEqual(adapter["adapter"]["voltage"],"temperature")
        with self.assertRaises(BridgeError):thermal_correspondence(th)
        with self.assertRaises(BridgeError):thermal_correspondence(a,new_source_id=a.source_id)

    def test_library_discovers_unrelated_models_through_common_law(self):
        a=capsule(star())
        b=capsule(twin_hubs())
        c=thermal_correspondence(a)["target"]
        d=capsule(triangle())
        x=discover_model_connections((a,b,c,d))
        self.assertEqual(len(x.links),3)
        self.assertEqual(len(x.components),2)
        self.assertEqual(sorted(len(cc) for cc in x.components),[1,3])
        self.assertTrue(any("FINITE_SOURCE_WITNESS" in v[2] for v in x.falsified))
        self.assertFalse(x.cross_domain_actual_carrier_identity)

    def test_no_automatic_link_between_incompatible_originals(self):
        a=capsule(star())
        b=capsule(twin_hubs(),source_id="another-source")
        x=discover_model_connections((a,b))
        self.assertFalse(x.links)
        self.assertIn("INVALID_CONTEXT",x.falsified[0][2])

    def test_graded_model_abstraction_transfers_without_inner_states(self):
        a,b=capsule(star()),capsule(twin_hubs())
        for k in range(7):
            result=graded_context_substitution(a,b,k,impedance=Q(2,3))
            self.assertTrue(result["matching_k_jet"])
            self.assertTrue(result["feedback_context_matches"])
            self.assertTrue(result["all_frequency"])
            self.assertEqual(boundary_taylor_jet(a.network,k),
                             boundary_taylor_jet(b.network,k))

    def test_graded_same_static_signature_not_first_dynamic_jet(self):
        a,b=capsule(star()),capsule(triangle())
        self.assertTrue(graded_context_substitution(a,b,0)["matching_k_jet"])
        first=graded_context_substitution(a,b,1)
        self.assertFalse(first["matching_k_jet"])
        self.assertEqual(first["first_failed_order"],1)

    def test_graded_feedback_jet_agrees_with_exact_first_derivative(self):
        a=capsule(serial_pendant())
        jets=boundary_taylor_jet(a.network,3)
        f=feedback_jet(jets,Q(1,2))
        self.assertEqual(f[0],feedback_response(a,0,Q(1,2)))
        # Difference quotient converges to the calculated first jet coefficient.
        # Instead of floating limits, use formal series product at each order:
        n=len(f[0]);eye=tuple(tuple(Q(1 if i==j else 0) for j in range(n)) for i in range(n))
        for k in range(4):
            zero=tuple(tuple(Q(0) for j in range(n)) for i in range(n))
            left=tuple(tuple(sum((Q(1,2)*sum(jets[j][i][a]*f[k-j][a][col] for a in range(n))
                                          for j in range(k+1)),Q(0))
                           +(f[k][i][col] if k==0 else f[k][i][col])
                           for col in range(n)) for i in range(n))
            self.assertEqual(left,jets[k])

    def test_grade_context_requires_source_and_domain(self):
        with self.assertRaises(BridgeError):graded_context_substitution(capsule(star()),capsule(star(),epoch=1),2)
        with self.assertRaises(BridgeError):boundary_taylor_jet(star(),-1)
        with self.assertRaises(BridgeError):boundary_taylor_jet(star(),11)

    def test_first_order_abstraction_detects_hidden_memory_at_next_level(self):
        s=capsule(star());d=capsule(triangle());t=capsule(twin_hubs())
        self.assertEqual(context_depth_witness(s,d)["first_distinguishing_level"],
                         "FIRST_DYNAMIC_DERIVATIVE")
        self.assertEqual(context_depth_witness(s,t)["first_distinguishing_level"],
                         "NO_BOUNDARY_DISTINCTION_ALL_FREQUENCIES")
        self.assertFalse(context_depth_witness(s,t)["hidden_intervention_equivalence"])

    def test_wrong_initial_parameters_have_same_dc_but_different_first_memory(self):
        s=capsule(star(cap=2))
        wrong=capsule(star(cap=3))
        self.assertEqual(s.response(0),wrong.response(0))
        self.assertEqual(context_depth_witness(s,wrong)["first_distinguishing_level"],
                         "FIRST_DYNAMIC_DERIVATIVE")

    def test_context_depth_bad_semantics_rejected(self):
        s=capsule(star())
        with self.assertRaises(BridgeError):context_depth_witness(s,capsule(star(),epoch=1))

    def test_library_rejects_duplicated_model_identity(self):
        a=capsule(star())
        with self.assertRaises(BridgeError):discover_model_connections((a,a))


class MarkovThermalElectricalBridges(unittest.TestCase):
    def test_star_exit_probabilities_and_times_are_exact(self):
        m=build_markov_bridge(star())
        self.assertEqual(m.generator,((Q(-5),),))
        self.assertEqual(m.exit_rates,((Q(1),Q(3,2),Q(5,2)),))
        self.assertEqual(m.exit_probabilities(),((Q(1,5),Q(3,10),Q(1,2)),))
        self.assertEqual(m.expected_absorption_time(),(Q(1,5),))
        self.assertEqual(m.hitting(1),((Q(1,6),Q(1,4),Q(5,12)),))

    def test_serial_generator_and_absorption_is_lawful(self):
        m=build_markov_bridge(serial_pendant())
        self.assertEqual(m.generator,((Q(-7),Q(2)),(Q(4,3),Q(-4,3))))
        self.assertEqual(m.exit_rates,((Q(1),Q(3,2),Q(5,2)),(Q(0),Q(0),Q(0))))
        for row in m.exit_probabilities():self.assertEqual(sum(row),Q(1))
        self.assertTrue(all(t>0 for t in m.expected_absorption_time()))

    def test_feynman_kac_discrete_resolvent_identity(self):
        for n in (star(),serial_pendant(),twin_hubs()):
            m=build_markov_bridge(n)
            for s in (0,1,2,3,Q(1,3),17):
                self.assertEqual(m.boundary_response(s),n.response(s))
            self.assertEqual(len(m.hitting(1)),len(n.interior))

    def test_many_independent_positive_source_networks(self):
        rng=random.Random(201206)
        for _ in range(150):
            g=tuple(rng.randrange(1,11) for _ in range(3))
            a=serial_pendant(g,rng.randrange(1,7),rng.randrange(1,8),rng.randrange(1,9))
            m=build_markov_bridge(a)
            for s in (0,1,2,4):
                self.assertEqual(m.boundary_response(s),a.response(s))
            for row in m.exit_probabilities():
                self.assertEqual(sum(row),Q(1))

    def test_require_positive_storage_to_build_markov_time(self):
        with self.assertRaises(BridgeError):build_markov_bridge(triangle())
        with self.assertRaises(BridgeError):build_markov_bridge(star(cap=0))
        with self.assertRaises(BridgeError):build_markov_bridge(None)
        with self.assertRaises(BridgeError):build_markov_bridge(star()).hitting(-1)

    def test_passive_derivative_signs_exact_all_source_classes(self):
        for net in (star(),serial_pendant(),twin_hubs()):
            for s in (0,1,2,5,Q(1,7)):
                d=derivative_sign_certificates(net,s)
                self.assertTrue(d["loewner_first_positive"])
                self.assertTrue(d["loewner_second_negative"])

    def test_finite_difference_passivity_checks_pass_real_sources(self):
        for net in (star(),serial_pendant(),twin_hubs(),triangle()):
            d=finite_passivity_shadow_test(*(net.response(s) for s in (0,1,2)))
            self.assertTrue(d["monotone_first"])
            self.assertTrue(d["monotone_second"])
            self.assertTrue(d["concave_midpoint"])
            self.assertFalse(d["all_frequency_passivity_certified"])

    def test_fake_measurements_break_monotonicity_and_concavity(self):
        net=star()
        a=net.response(0)
        b=net.response(1)
        c=net.response(2)
        w=finite_passivity_shadow_test(b,a,c)
        self.assertFalse(w["monotone_first"])
        convex_third=tuple(tuple(a[i][j]+3*(b[i][j]-a[i][j]) for j in range(3)) for i in range(3))
        w=finite_passivity_shadow_test(a,b,convex_third)
        self.assertTrue(w["monotone_second"])
        self.assertFalse(w["concave_midpoint"])

    def test_unbounded_context_law_does_not_follow_from_four_samples(self):
        alias=positive_passive_alias((0,1,2,3))
        for s in alias.probe_points:
            self.assertEqual(alias.lower.response(s),alias.higher.response(s))
        self.assertNotEqual(alias.lower.response(alias.first_holdout),
                            alias.higher.response(alias.first_holdout))

    def test_random_passivity_shadows_and_derivatives(self):
        rng=random.Random(2175)
        for _ in range(180):
            net=serial_pendant(tuple(rng.randint(1,8) for _ in range(3)),
                rng.randint(1,7),rng.randint(1,7),rng.randint(1,7))
            s=Q(rng.randrange(0,13),rng.randrange(1,6))
            d=derivative_sign_certificates(net,s)
            self.assertTrue(d["loewner_first_positive"])
            self.assertTrue(d["loewner_second_negative"])
            z=finite_passivity_shadow_test(*(net.response(i) for i in (0,1,2)))
            self.assertTrue(all(z[k] for k in ("monotone_first","monotone_second","concave_midpoint")))

    def test_all_frequency_not_claimed_from_empirical_four_values(self):
        a,b=capsule(star()),capsule(twin_hubs())
        c=certify_all_frequency(a,b)
        self.assertIn("declared orders",c.all_frequency_scope)
        self.assertEqual(len(c.test_points),c.degree_bound+1)
        # One is a source model theorem, the other a physical attestation we do NOT have.
        self.assertFalse(a.public_contract()["physical_origin_authenticated"])

    def test_summary_retains_source_restrictions(self):
        demo=categorical_bridge_demo()
        self.assertEqual(demo["status"],"CERTIFIED_CATEGORY_BRIDGES_AND_CONTEXTUAL_MODEL_ABSTRACTION")
        self.assertFalse(demo["all_representations_physically_same"])
        self.assertFalse(demo["RH_or_Weil_positivity_proved"])
        self.assertTrue(demo["parallel_context_equivalent"])
        self.assertTrue(demo["feedback_context_equivalent"])
