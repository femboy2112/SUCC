"""Hilbert 4-adic/dyadic exact source, quadrature and noninvertibility controls."""
import unittest
from fractions import Fraction as Q
from itertools import product
from observational_succ import hilbert_carrier as h

class HilbertFiniteTowerTests(unittest.TestCase):
    def test_exact_bijection_through_order_six(self):
        for k in range(1,7):
            n=1<<k
            seen={h.point(k,d) for d in range(n*n)}
            self.assertEqual(seen,set(product(range(n),repeat=2)))
            for d in range(n*n):
                x,y=h.point(k,d)
                self.assertEqual(h.index(k,x,y),d)

    def test_every_successor_is_one_spatial_cell(self):
        for k in range(1,7):
            r=h.coverage(k)
            self.assertEqual(r["maximum_l1_consecutive_jump"],1)
            self.assertEqual(r["cells"],4**k)
            self.assertEqual(r["dyadic_cell_area"],Q(1,4**k))
            self.assertEqual(r["matched_4adic_time_interval_length"],Q(1,4**k))
            self.assertFalse(r["finite_centers_cover_continuum"])

    def test_all_parent_child_cylinders_cohere(self):
        for k in range(2,6):
            for p in range(1,k+1):
                stride=4**(k-p)
                for j in range(4**p):
                    parent=h.point(p,j)
                    for d in range(j*stride,(j+1)*stride):
                        c=h.prefix_square(k,d,p)
                        self.assertEqual(c["parent_index"],j)
                        self.assertEqual(c["parent_cell"],parent)
                        self.assertTrue(c["coherent_dyadic_source"])

    def test_exact_disjoint_time_cylinders_vs_closed_square(self):
        for k in range(1,5):
            last=Q()
            for d in range(4**k):
                left,right=h.time_cell(k,d)
                self.assertEqual(left,last)
                self.assertEqual(right-left,Q(1,4**k))
                last=right
                X,Y=h.spatial_cell(k,d)
                c=h.center(k,d)
                self.assertTrue(X[0]<c[0]<X[1] and Y[0]<c[1]<Y[1])
            self.assertEqual(last,1)

    def test_hilbert_is_not_two_way_local(self):
        for k,want in ((2,13),(3,53),(4,213)):
            out=h.adjacent_parameter_far_apart(k)
            self.assertEqual(out["max_index_separation_of_spatial_edge_neighbors"],want)
            a,b=out["witness_cells"]
            self.assertEqual(abs(a[0]-b[0])+abs(a[1]-b[1]),1)
            self.assertFalse(out["inverse_locality_globally_guaranteed"])
            self.assertEqual(h.raster_jump(k),1<<k)

    def test_bad_index_coordinates_and_provenance_types(self):
        for fn in (
            lambda:h.point(0,0),lambda:h.point(2,16),
            lambda:h.point(1,0.0),lambda:h.index(3,0.0,1),
            lambda:h.index(2,4,0),lambda:h.prefix_square(2,3,3),
            lambda:h.coverage(9),lambda:h.adjacent_parameter_far_apart(8)
        ):
            with self.assertRaises(h.HilbertCarrierError):fn()


class HilbertQuadratureTests(unittest.TestCase):
    def test_exact_affine_integral_any_finite_stage(self):
        poly=h.RationalPolynomial("law",0,((0,0,Q(7)),(1,0,Q(3)),(0,1,Q(-2))))
        for k in range(1,6):
            r=h.exact_quadrature(poly,k)
            self.assertEqual(r["hilbert_midpoint_integral"],poly.integral())
            self.assertEqual(r["absolute_error_exact"],0)
            self.assertEqual(r["source_hessian_error_upper"],0)
            self.assertFalse(r["actual_physical_observations"])

    def test_quadratic_hessian_bound_is_exact_sharp(self):
        poly=h.RationalPolynomial("x²+y²",0,((2,0,Q(1)),(0,2,Q(1))))
        self.assertEqual(poly.integral(),Q(2,3))
        for k in range(1,7):
            r=h.exact_quadrature(poly,k)
            self.assertEqual(r["absolute_error_exact"],Q(1,6*4**k))
            self.assertEqual(r["source_hessian_error_upper"],Q(1,6*4**k))
            self.assertTrue(r["quadrature_is_source_authenticated"])

    def test_cross_term_hessian_bound_vs_true_cancelation(self):
        p=h.RationalPolynomial("xy",0,((1,1,Q(1)),))
        for k in (1,2,4):
            r=h.exact_quadrature(p,k)
            self.assertEqual(r["hilbert_midpoint_integral"],Q(1,4))
            self.assertEqual(r["absolute_error_exact"],0)
            self.assertEqual(r["source_hessian_error_upper"],Q(1,16*4**k))

    def test_complex_polynomial_independent_original_integral(self):
        p=h.RationalPolynomial("mixed",2,(
           (0,0,Q(1)),(2,1,Q(2,3)),(1,3,Q(-5,7)),(3,3,Q(13,19))))
        self.assertEqual(p.integral(),Q(1)+Q(1,9)-Q(5,56)+Q(13,304))
        for k in (1,2,4,5):
            r=h.exact_quadrature(p,k)
            self.assertLessEqual(r["absolute_error_exact"],r["source_hessian_error_upper"])
            self.assertLessEqual(r["absolute_error_exact"],r["source_gradient_error_upper"])

    def test_original_polynomial_source_mutation_rejected(self):
        for fn in (
            lambda:h.RationalPolynomial("",0,((1,0,Q(1)),)),
            lambda:h.RationalPolynomial("x",-1,((1,0,Q(1)),)),
            lambda:h.RationalPolynomial("x",0,((1,0,1.0),)),
            lambda:h.RationalPolynomial("x",0,((1,0,1),(1,0,2))),
            lambda:h.RationalPolynomial("x",0,((9,0,1),)),
            lambda:h.exact_quadrature("x+y",2),
            lambda:h.exact_quadrature(h.RationalPolynomial("x",0,((1,0,1),)),7),
        ):
            with self.assertRaises(h.HilbertCarrierError):fn()


class HilbertL2ObserverTests(unittest.TestCase):
    def test_finite_cylinder_isometry_even_without_inverse_continuity(self):
        for k in range(1,6):
            n=1<<k
            u=tuple(tuple(Q((x+1)*(y+3),7) for y in range(n)) for x in range(n))
            v=tuple(tuple(Q((-1)**(x+y)*(x+y+1),11) for y in range(n))
                    for x in range(n))
            source=sum((u[x][y]*v[x][y] for x in range(n) for y in range(n)),Q())/n**2
            self.assertEqual(h.exact_cell_inner_product(k,u,v),source)
            self.assertEqual(h.exact_cell_inner_product(k,u,u),
                             sum((w*w for row in u for w in row),Q())/n**2)

    def test_conditional_expectation_of_linear_x_has_exact_L2_rate(self):
        x=h.RationalPolynomial("x_coord",0,((1,0,Q(1)),))
        for k in range(1,6):
            r=h.dyadic_conditional_L2(x,k)
            self.assertEqual(r["original_L2_norm_squared"],Q(1,3))
            self.assertEqual(r["L2_squared_error_exact"],Q(1,12*4**k))
            self.assertEqual(r["spatial_cell_mass"],r["time_cylinder_mass"])
            self.assertTrue(r["finite_source_step_isometry"])
            self.assertFalse(r["Hilbert_pullback_H1_isometry_proved"])

    def test_conditional_martingale_decreases_for_polynomial(self):
        p=h.RationalPolynomial("curvature",0,((2,0,Q(1)),(0,2,Q(1)),(1,1,Q(-2))))
        values=[h.dyadic_conditional_L2(p,k)["L2_squared_error_exact"]
                for k in range(1,6)]
        self.assertTrue(all(a>b>=0 for a,b in zip(values,values[1:])))

    def test_hidden_Haar_refutes_uniform_L2_unit_ball_rate(self):
        for k in (1,2,3,4,7):
            c=h.hidden_unit_Haar(k)
            self.assertEqual(c["L2_norm_squared"],Q(1))
            self.assertEqual(c["cell_average"],Q())
            self.assertEqual(c["dyadic_observer_projection_norm_squared"],Q())
            self.assertTrue(c["operator_norm_I_minus_P_equals_one"])
            self.assertFalse(c["universal_L2_unit_ball_rate_exists"])
            self.assertFalse(c["actual_Weil_spectral_direction_authenticated"])

    def test_float_and_incomplete_L2_arrays_refused(self):
        with self.assertRaises(h.HilbertCarrierError):
            h.exact_cell_inner_product(1,((1,2),),((1,2),))
        with self.assertRaises(h.HilbertCarrierError):
            h.exact_cell_inner_product(1,((0.0,1),(1,0)),((1,0),(0,1)))



class HilbertLimitTubeTests(unittest.TestCase):
    def test_fixed_parameter_has_nested_cells_with_exact_geometric_error(self):
        for t in (Q(),Q(1),Q(1,4),Q(13,17),Q(1,2),Q(2,3)):
            last=None
            for k in range(1,8):
                r=h.parameter_tube(t,k)
                self.assertEqual(r["squared_distance_to_completed_point_upper"],
                                 Q(1,2*4**k))
                X,Y=r["spatial_enclosure"]
                if last:
                    A,B=last["spatial_enclosure"]
                    self.assertTrue(A[0]<=X[0]<=X[1]<=A[1])
                    self.assertTrue(B[0]<=Y[0]<=Y[1]<=B[1])
                self.assertFalse(r["limit_point_physically_observed"])
                last=r

    def test_rational_target_surjection_preimage_tubes_are_nested(self):
        for x,y in ((Q(0),Q(0)),(Q(1),Q(1)),(Q(1,2),Q(1,2)),
                    (Q(1,3),Q(5,7)),(Q(1,8),Q(1,2))):
            last=None
            for k in range(1,7):
                r=h.target_preimage_tube(x,y,k)
                lo,hi=r["time_cylinder"]
                self.assertEqual(hi-lo,Q(1,4**k))
                if last is not None:
                    l0,l1=last
                    self.assertTrue(l0<=lo<=hi<=l1)
                last=lo,hi
                self.assertFalse(r["preimage_parameter_computed_to_infinite_precision"])

    def test_source_target_domain_mutation_rejected(self):
        for fn in (
            lambda:h.parameter_tube(Q(-1),2),
            lambda:h.parameter_tube(0.25,2),
            lambda:h.target_preimage_tube(Q(2),Q(0),2),
            lambda:h.target_preimage_tube(Q(0),0.5,2),
        ):
            with self.assertRaises(h.HilbertCarrierError):fn()




class HilbertLipschitzNoGo(unittest.TestCase):
    def test_no_globally_lipschitz_interval_onto_square(self):
        for L in (Q(),Q(1,100),Q(1),Q(3,2),Q(10),Q(111,3)):
            theorem=h.no_global_lipschitz_space_filler(L)
            self.assertLess(theorem["upper_area_of_image"],1)
            self.assertGreaterEqual(theorem["finite_time_interval_cover_count"],1)
            self.assertFalse(theorem["surjective_with_this_Lipschitz_bound"])
            self.assertFalse(theorem["actual_Hilbert_curve_Lipschitz"])
        with self.assertRaises(h.HilbertCarrierError):
            h.no_global_lipschitz_space_filler(-1)
        with self.assertRaises(h.HilbertCarrierError):
            h.no_global_lipschitz_space_filler(0.5)


if __name__=="__main__":
    unittest.main()
