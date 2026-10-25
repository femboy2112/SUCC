"""Exact no-float receipts for jointly correcting scalar and graph boundaries."""
import unittest
from fractions import Fraction as Q
from observational_succ.conservative_boundary_flux import (
 BoundaryFluxError, two_sided_euler_budget, rectangle_curvature,
 true_prime_product, laplacian, graph_port_balance, schur_port,
 dynamic_port_operator,
)

class TwoSidedEulerTests(unittest.TestCase):
    def test_exact_two_sided_brackets(self):
        x=two_sided_euler_budget(2,4,5)
        self.assertEqual(x.succ_above,Q(97,144))
        self.assertEqual(x.prime_below,Q(9,16))
        self.assertEqual(x.observable_gap,Q(1,9))
        self.assertEqual(x.succ_error_cap,Q(1,32))
        self.assertEqual(x.prime_error_cap,Q(1,5))
        self.assertLessEqual(x.intersection_lower,x.intersection_upper)
        for n,xcut in ((1,2),(2,3),(3,5),(7,11),(20,23),(30,31)):
            for power in (2,3,4):
                x=two_sided_euler_budget(power,n,xcut)
                self.assertGreaterEqual(x.observable_gap,0)
                self.assertLessEqual(x.observable_gap,x.succ_error_cap+x.prime_error_cap)
    def test_correlated_correction_is_exactly_flat(self):
        for power in (2,3):
            self.assertEqual(rectangle_curvature(power,4,5,7,11),0)
            self.assertEqual(rectangle_curvature(power,11,12,17,23),0)
            self.assertGreater(two_sided_euler_budget(power,4,7).observable_gap,
                               two_sided_euler_budget(power,5,7).observable_gap)
            self.assertGreater(two_sided_euler_budget(power,4,7).observable_gap,
                               two_sided_euler_budget(power,4,11).observable_gap)
    def test_fake_prime_six_breaks_signed_source_gate(self):
        good=two_sided_euler_budget(2,11,11)
        fake=true_prime_product(2,11)*Q(36,35)-1
        self.assertLessEqual(good.prime_below,good.succ_above)
        self.assertGreater(fake,good.succ_above)
    def test_invalid_cutoffs_and_source(self):
        for args in ((2,7,5),(1,3,5),(2,0,5)):
            with self.assertRaises(BoundaryFluxError):two_sided_euler_budget(*args)

class EnergyGraphPortTests(unittest.TestCase):
    def setUp(self):
        self.l3=laplacian(3,((0,1,Q(1)),(1,2,Q(1))))
        self.l4=laplacian(4,((0,1,Q(1)),(1,2,Q(1)),(2,3,Q(1))))
    def test_harmonic_hidden_energy_and_boundary_currents_exact(self):
        x=graph_port_balance(self.l3,(0,2),(Q(1),Q(0),Q(0)))
        self.assertEqual(x.effective_laplacian,
                         ((Q(1,2),Q(-1,2)),(Q(-1,2),Q(1,2))))
        self.assertEqual(x.harmonic_interior,(Q(1,2),))
        self.assertEqual((x.raw_energy,x.port_energy,x.hidden_energy),(Q(1),Q(1,2),Q(1,2)))
        self.assertEqual(x.interior_residual_current,(Q(-1),))
        self.assertEqual(x.transported_boundary_error,(Q(1,2),Q(1,2)))
        self.assertEqual(x.full_current_sum,Q(0))
        y=graph_port_balance(self.l3,(0,2),(Q(1),Q(1,2),Q(0)))
        self.assertEqual((y.raw_energy,y.port_energy,y.hidden_energy),(Q(1,2),Q(1,2),Q(0)))
        self.assertEqual(y.transported_boundary_error,(Q(0),Q(0)))
    def test_nested_eliminations_associate_exactly(self):
        direct=schur_port(self.l4,(0,3))
        first=schur_port(self.l4,(0,2,3))
        second=schur_port(first,(0,2))
        self.assertEqual(direct,second)
        self.assertEqual(direct,((Q(1,3),Q(-1,3)),(Q(-1,3),Q(1,3))))
        raw=graph_port_balance(self.l4,(0,3),(Q(1),Q(2),Q(0),Q(0)))
        partial=graph_port_balance(self.l4,(0,2,3),(Q(1),Q(2),Q(0),Q(0)))
        self.assertEqual((raw.raw_energy,raw.port_energy,raw.hidden_energy),
                         (Q(5),Q(1,3),Q(14,3)))
        self.assertEqual((partial.port_energy,partial.hidden_energy),(Q(1,2),Q(9,2)))
        self.assertEqual(raw.hidden_energy,partial.hidden_energy+Q(1,6))
    def test_one_port_is_observationally_trivial_static(self):
        self.assertEqual(schur_port(self.l3,(0,)),((Q(0),),))
        another=laplacian(3,((0,1,Q(2)),(1,2,Q(3))))
        self.assertEqual(schur_port(another,(0,)),((Q(0),),))
        self.assertNotEqual(schur_port(self.l3,(0,2)),schur_port(another,(0,2)))
    def test_dynamic_hidden_storage_not_captured_by_static_schur(self):
        static=schur_port(self.l3,(0,2))
        a=dynamic_port_operator(self.l3,(0,1,0),(0,2),Q(1))
        b=dynamic_port_operator(self.l3,(0,2,0),(0,2),Q(1))
        self.assertEqual(static,((Q(1,2),Q(-1,2)),(Q(-1,2),Q(1,2))))
        self.assertEqual(a,((Q(2,3),Q(-1,3)),(Q(-1,3),Q(2,3))))
        self.assertEqual(b,((Q(3,4),Q(-1,4)),(Q(-1,4),Q(3,4))))
        self.assertNotEqual(a,b)
        self.assertEqual(dynamic_port_operator(self.l3,(0,1,0),(0,2),Q(0)),static)
    def test_bad_graph_and_unseen_island_are_rejected(self):
        with self.assertRaises(BoundaryFluxError):laplacian(2,((0,1,Q(-1)),))
        with self.assertRaises(BoundaryFluxError):laplacian(2,((0,0,Q(1)),))
        with self.assertRaises(BoundaryFluxError):laplacian(2,((0,1,.5),))
        two_component=laplacian(4,((0,1,Q(1)),(2,3,Q(1))))
        with self.assertRaises(BoundaryFluxError):schur_port(two_component,(0,))
        with self.assertRaises(BoundaryFluxError):graph_port_balance(self.l3,(0,2),(0,))
        from observational_succ.conservative_boundary_flux import rc_power_balance
        signed=((Q(-1),Q(1),Q(0)),(Q(1),Q(-2),Q(1)),(Q(0),Q(1),Q(-1)))
        with self.assertRaises(BoundaryFluxError):graph_port_balance(signed,(0,2),(1,0,0))
        with self.assertRaises(BoundaryFluxError):dynamic_port_operator(signed,(0,1,0),(0,2),1)
        with self.assertRaises(BoundaryFluxError):rc_power_balance(signed,(0,2),(1,0,0),(1,))
        with self.assertRaises(BoundaryFluxError):dynamic_port_operator(self.l3,(0,-1,0),(0,2),1)

if __name__=='__main__':unittest.main()

class NestedObservationTests(unittest.TestCase):
    def test_exact_variance_transport(self):
        from observational_succ.conservative_boundary_flux import nested_information_budget
        q=(Q(1,4),)*4
        z=nested_information_budget((1,2,3,4),q,((0,1,2,3),),((0,1),(2,3)))
        self.assertEqual(z.coarse_projection,(Q(5,2),)*4)
        self.assertEqual(z.fine_projection,(Q(3,2),Q(3,2),Q(7,2),Q(7,2)))
        self.assertEqual((z.coarse_unresolved,z.fine_unresolved,z.visible_innovation,z.orthogonality_cross),
                         (Q(5,4),Q(1,4),Q(1),Q(0)))
    def test_source_incompatibility_rejected(self):
        from observational_succ.conservative_boundary_flux import nested_information_budget
        q=(Q(1,4),)*4
        with self.assertRaises(BoundaryFluxError):
            nested_information_budget((1,2,3,4),q,((0,1),(2,3)),((0,2),(1,3)))
        with self.assertRaises(BoundaryFluxError):
            nested_information_budget((1,2,3,4),(Q(1,3),)*4,((0,1,2,3),),((0,1),(2,3)))
        with self.assertRaises(BoundaryFluxError):
            nested_information_budget((1,2,3,4),q,((0,1,2,3),),((0,1),(1,2,3)))

class CorrelationDebtTests(unittest.TestCase):
    def test_cross_term_can_be_negative_without_projection(self):
        from observational_succ.conservative_boundary_flux import correlated_energy_ledger
        d=correlated_energy_ledger((1,1),(2,2),(Q(1,2),Q(1,2)))
        self.assertEqual((d.total,d.visible,d.unresolved,d.cross_term),
                         (Q(1),Q(4),Q(1),Q(-4)))
        e=correlated_energy_ledger((1,2),(1,1),(Q(1,2),Q(1,2)))
        self.assertEqual((e.total,e.visible,e.unresolved,e.cross_term),
                         (Q(5,2),Q(1),Q(1,2),Q(1)))
        self.assertNotEqual(e.visible+e.unresolved,e.total)
    def test_cross_source_metric_mismatch_rejected(self):
        from observational_succ.conservative_boundary_flux import correlated_energy_ledger
        with self.assertRaises(BoundaryFluxError):
            correlated_energy_ledger((1,2),(1,), (Q(1,2),Q(1,2)))

class RCPowerTests(unittest.TestCase):
    def test_exact_source_power_dissipation_storage(self):
        from observational_succ.conservative_boundary_flux import rc_power_balance
        l=laplacian(3,((0,1,Q(1)),(1,2,Q(1))))
        v=rc_power_balance(l,(0,2),(Q(1),Q(0),Q(0)),(Q(2),))
        self.assertEqual((v.boundary_input_power,v.resistive_dissipation,
                         v.hidden_storage_rate,v.interior_time_derivative),
                         (Q(1),Q(1),Q(0),(Q(1,2),)))
        # At an arbitrary off-equilibrium state, storage draws real power.
        w=rc_power_balance(l,(0,2),(Q(1),Q(1,4),Q(0)),(Q(2),))
        self.assertEqual((w.boundary_input_power,w.resistive_dissipation,
                          w.hidden_storage_rate), (Q(3,4),Q(5,8),Q(1,8)))
    def test_missing_storage_capacity_is_not_silent(self):
        from observational_succ.conservative_boundary_flux import rc_power_balance
        l=laplacian(3,((0,1,Q(1)),(1,2,Q(1))))
        with self.assertRaises(BoundaryFluxError):
            rc_power_balance(l,(0,2),(Q(1),Q(0),Q(0)),(Q(0),))

class TwoDomainTransportTests(unittest.TestCase):
    def test_exact_orthogonal_two_boundary_error_energy(self):
        from observational_succ.conservative_boundary_flux import two_domain_transport_budget
        x=two_domain_transport_budget(((1,2,1),(0,1,1)),(1,2,3),
             ((1,0,0),(0,1,0),(0,0,0)),((1,0),(0,0)))
        self.assertEqual(x.exact_target,(Q(8),Q(5)))
        self.assertEqual(x.finite_target,(Q(5),Q(0)))
        self.assertEqual(x.total_residual,(Q(3),Q(5)))
        self.assertEqual(x.target_cutoff_residual,(Q(0),Q(5)))
        self.assertEqual(x.transported_source_residual,(Q(3),Q(0)))
        self.assertEqual((x.total_squared,x.target_squared,x.source_squared,x.cross_term),
                        (Q(34),Q(25),Q(9),Q(0)))
        self.assertTrue(x.target_projection_orthogonal)
    def test_oblique_projection_has_negative_interference_and_is_not_lost(self):
        from observational_succ.conservative_boundary_flux import two_domain_transport_budget
        x=two_domain_transport_budget(((1,2,1),(0,1,1)),(1,2,3),
             ((1,0,0),(0,1,0),(0,0,0)),((1,1),(0,0)))
        self.assertFalse(x.target_projection_orthogonal)
        self.assertEqual(x.total_residual,(Q(1),Q(5)))
        self.assertEqual(x.target_cutoff_residual,(Q(-5),Q(5)))
        self.assertEqual(x.transported_source_residual,(Q(6),Q(0)))
        self.assertEqual((x.total_squared,x.target_squared,x.source_squared,x.cross_term),
                        (Q(26),Q(50),Q(36),Q(-60)))
    def test_invalid_nonidempotent_or_wrong_dimensions_rejected(self):
        from observational_succ.conservative_boundary_flux import two_domain_transport_budget
        with self.assertRaises(BoundaryFluxError):
            two_domain_transport_budget(((1,0),), (1,2), ((2,0),(0,0)), ((1,),))
        with self.assertRaises(BoundaryFluxError):
            two_domain_transport_budget(((1,0),), (1,2), ((1,0),(0,0)), ((1,0),(0,0)))
