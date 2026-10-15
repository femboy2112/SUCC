"""Exact local controls for a *mathematical* Hilbert/Zeno certificate scheme."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.hilbert_zeno import (
    SourceKey, HilbertZenoError, hilbert_xy, hilbert_index, hilbert_cells,
    cell_center, hilbert_prefix, hilbert_refinement_children, optimal_open_path_length, RationalPolynomial2, certify_square,
    certify_square_adaptive, blind_tent, holder_no_go_dimension, hilbert_cube_error, hilbert_cube_horizon, QuadraticSource,
    cube_parameter_grid, certify_hilbert_cube, exact_neumann_legendre_2x2,
    hilbert_source_bridge_check, normalized_neumann_legendre_2x2,
)


SOURCE = SourceKey("declared-rational-source", 0, "polynomial-xy", "unit-square")
H = SourceKey("declared-Hilbert-model", 0, "orthonormal-e_j", "weighted-ell2-cube")


def poly(*terms):
    return RationalPolynomial2(SOURCE, tuple((i,j,F(c)) for i,j,c in terms))


class HilbertGeometry(unittest.TestCase):
    def test_all_finite_orders_bijective_and_manhattan_unit(self):
        for level in range(6):
            side = 2**level
            path = tuple(hilbert_cells(level))
            self.assertEqual(len(path), side**2)
            self.assertEqual(len(set(path)), side**2)
            self.assertEqual(set(path), set(product(range(side), repeat=2)))
            self.assertEqual(path[0], (0,0))
            self.assertEqual(path[-1], (side-1,0))
            for index, (x,y) in enumerate(path):
                self.assertEqual(hilbert_xy(level,index),(x,y))
                self.assertEqual(hilbert_index(level,x,y),index)
            self.assertTrue(all(abs(x1-x0)+abs(y1-y0)==1
                                for (x0,y0),(x1,y1) in zip(path,path[1:])))

    def test_quaternary_prefixes_are_source_refining_nested_cells(self):
        for level in range(0,5):
            for x,y in product(range(2**level),repeat=2):
                i=hilbert_index(level,x,y)
                self.assertEqual(hilbert_refinement_children(level,x,y),
                                 (4*i,4*i+1,4*i+2,4*i+3))
        stamp=SourceKey("Hilbert-address",0,"quaternary-prefix","[0,1]^2")
        for digits in ((1,),(1,2),(1,2,0),(1,2,0,3),(1,2,0,3,2)):
            c=hilbert_prefix(stamp,digits)
            self.assertEqual(c.level,len(digits))
            self.assertEqual(c.completion_radius_inf,F(1,2**(len(digits)+1)))
            self.assertTrue(all(lo<=mid<=hi for lo,mid,hi
                                in zip(c.lower_left,c.midpoint,c.upper_right)))
        p=hilbert_prefix(stamp,(1,2))
        q=hilbert_prefix(stamp,(1,2,0,3,2))
        self.assertTrue(all(a<=b<=c for a,b,c in zip(p.lower_left,q.midpoint,p.upper_right)))
        self.assertTrue(all(abs(a-b)<=p.completion_radius_inf
                            for a,b in zip(p.midpoint,q.midpoint)))

    def test_origin_to_completion_quantitative_zeno(self):
        key=SourceKey("a",0,"base4","square")
        for level in range(1,11):
            first=hilbert_prefix(key,(0,)*level)
            last=hilbert_prefix(key,(3,)*level)
            self.assertEqual(first.cell,(0,0))
            self.assertEqual(last.cell,(2**level-1,0))
            self.assertEqual(first.midpoint,(F(1,2**(level+1)),)*2)
            self.assertLessEqual(max(first.midpoint),first.completion_radius_inf)
            self.assertLessEqual(max(abs(last.midpoint[0]-1),abs(last.midpoint[1])),
                                 last.completion_radius_inf)
        for bad in ((0,4),(2,False),("1",)):
            with self.assertRaises(HilbertZenoError): hilbert_prefix(key,bad)

    def test_path_exact_length_and_cost_diverges(self):
        for level in range(1,7):
            self.assertEqual(optimal_open_path_length(level),F(4**level-1,2**level))
        self.assertGreater(optimal_open_path_length(6),optimal_open_path_length(4))

    def test_cells_approach_source_origin_without_actual_omega_visit(self):
        for level in range(1,10):
            self.assertEqual(cell_center(level,0,0),(F(1,2**(level+1)),)*2)

    def test_malformed_index_and_coordinates_rejected(self):
        for args in ((-1,0),(2,16),(True,0),(1,False)):
            with self.assertRaises(HilbertZenoError): hilbert_xy(*args)
        for args in ((2,4,0),(2,0,4),(1,-1,0)):
            with self.assertRaises(HilbertZenoError): hilbert_index(*args)
        with self.assertRaises(HilbertZenoError): cell_center(2,4,0)

    def test_actual_integrated_zeno_stamp_adapter(self):
        try:
            from observational_succ.zeno_certificate import Stamp
        except ImportError:
            self.skipTest("full integrated Zeno source absent in isolated overlay")
        s=Stamp("authored-source",2,"e_j","H0^1")
        self.assertEqual(SourceKey.from_zeno_stamp(s),
                         SourceKey("authored-source",2,"e_j","H0^1"))

    def test_source_epoch_basis_domain_firewall(self):
        for mutation in (
            SourceKey(SOURCE.source_id, 1, SOURCE.basis, SOURCE.domain),
            SourceKey("fake6", 0, SOURCE.basis, SOURCE.domain),
            SourceKey(SOURCE.source_id, 0, "reversed", SOURCE.domain),
            SourceKey(SOURCE.source_id, 0, SOURCE.basis, "arithmetic"),
        ):
            with self.assertRaises(HilbertZenoError): SOURCE.check(mutation)
        SOURCE.check(SOURCE)
        with self.assertRaises(HilbertZenoError): SourceKey("",0,"b","d")
        with self.assertRaises(HilbertZenoError): SourceKey("s",True,"b","d")
        with self.assertRaises(HilbertZenoError): RationalPolynomial2(SOURCE,((0,0,F(1)),(0,0,F(2))))
        with self.assertRaises(HilbertZenoError): RationalPolynomial2(SOURCE,[(0,0,F(1))])
        with self.assertRaises(HilbertZenoError): poly((0,0,0)).at(F(2),F(0))


class SquarePositiveAndNegative(unittest.TestCase):
    def test_polynomial_derivative_bound_is_exact_source_law(self):
        p=poly((0,0,1),(2,0,F(1,8)),(0,1,-F(1,4)))
        self.assertEqual(p.gradient_l1_bound(),F(1,4))
        self.assertEqual(p.at(F(1,2),F(1,4)),F(1)+F(1,32)-F(1,16))
        for x,y in product((F(0),F(1,3),F(1)),repeat=2):
            self.assertLessEqual(abs(p.at(x,y)-p.at(F(1,2),F(1,2))),
                                 p.gradient_l1_bound()*(abs(x-F(1,2))+abs(y-F(1,2))))

    def test_global_positive_certificate_derived_from_polynomial(self):
        p=poly((0,0,1),(1,0,F(1,8)),(0,1,-F(1,8)))
        r=certify_square(p,2)
        self.assertEqual(r.samples,16)
        self.assertEqual(r.verdict,"GLOBAL_NONNEGATIVE")
        self.assertGreater(r.global_lower,0)
        self.assertFalse(r.physical_observations_performed)
        self.assertFalse(r.source_physically_authenticated)
        self.assertEqual(r.mathematical_path_length,F(15,4))
        for x,y in product((F(0),F(1,7),F(3,5),F(1)),repeat=2):
            self.assertLessEqual(r.global_lower,p.at(x,y))
            self.assertGreaterEqual(r.global_upper,p.at(x,y))

    def test_negative_witness_real_and_unfitted(self):
        p=poly((0,0,-F(1,2)),(1,0,1))
        r=certify_square(p,1)
        self.assertEqual(r.verdict,"NEGATIVE_WITNESS")
        x,y,f=r.minimum_witness
        self.assertEqual(f,p.at(x,y))
        self.assertLess(f,0)

    def test_zero_minimum_does_not_become_finite_positive_proof(self):
        p=poly((0,0,F(1,2)),(1,0,-1),(2,0,1),(0,1,-1),(0,2,1))
        for level in (0,1,2,3):
            r=certify_square(p,level)
            self.assertNotEqual(r.verdict,"GLOBAL_NONNEGATIVE")
            self.assertGreaterEqual(r.lowest,0)

    def test_adaptive_path_prunes_at_coarse_source_resolution(self):
        p=poly((0,0,3),(1,0,F(1,2)),(0,1,-F(1,4)))
        r=certify_square_adaptive(p,5)
        self.assertEqual(r.verdict,"GLOBAL_NONNEGATIVE")
        self.assertEqual(r.evaluated_cells,1)
        self.assertEqual(r.resolved_cells,1)

    def test_adaptive_negative_and_zero_no_go(self):
        n=certify_square_adaptive(poly((0,0,-1)),3)
        self.assertEqual(n.verdict,"NEGATIVE_WITNESS")
        self.assertLess(n.negative_witness[2],0)
        q=poly((0,0,F(1,2)),(1,0,-1),(2,0,1),(0,1,-1),(0,2,1))
        undecided=certify_square_adaptive(q,3)
        self.assertEqual(undecided.verdict,"UNRESOLVED")
        self.assertGreater(undecided.unresolved_cells,0)

    def test_missing_cell_exact_lipschitz_countermodel(self):
        level=3
        all_indices=tuple(range(4**level))
        missing=17
        sampled=tuple(i for i in all_indices if i!=missing)
        witness=blind_tent(level,sampled)
        self.assertEqual(witness.cell,hilbert_xy(level,missing))
        self.assertEqual(witness.at(*witness.center),-F(1,16))
        for i in sampled:
            self.assertEqual(witness.at(*cell_center(level,*hilbert_xy(level,i))),F(0))
        # ||.||_∞ and ||.||_1 both dominate changes of the tent.
        a=cell_center(level,*hilbert_xy(level,0));b=witness.center
        self.assertLessEqual(abs(witness.at(*a)-witness.at(*b)),
                             abs(a[0]-b[0])+abs(a[1]-b[1]))

    def test_no_sourced_modulus_no_finite_sample_decision(self):
        # A polynomial vanishing at every sampled finite point can still be
        # strictly negative at other points; no invented all-stage Lipschitz L.
        level=1
        observed=[cell_center(level,*hilbert_xy(level,i)) for i in range(4)]
        def mutant(x,y):
            z=F(-1)
            for u,v in observed: z*=((x-u)**2+(y-v)**2)
            return z
        self.assertTrue(all(mutant(*p)==0 for p in observed))
        self.assertLess(mutant(F(0),F(0)),0)

    def test_partial_scan_is_not_certification(self):
        with self.assertRaisesRegex(HilbertZenoError,"RESOURCE_BUDGET"):
            certify_square(poly((0,0,1)),4,max_samples=10)
        with self.assertRaisesRegex(HilbertZenoError,"RESOURCE_BUDGET"):
            certify_square_adaptive(poly((0,0,F(1,2)),(1,0,-1),(2,0,1),(0,1,-1),(0,2,1)),4,max_cells=2)


class CompactHilbertCube(unittest.TestCase):
    def test_no_fixed_positive_holder_exponent_fills_infinite_cube(self):
        for alpha, expected in ((F(1),2),(F(1,2),3),(F(1,100),101),(F(3,2),1)):
            N=holder_no_go_dimension(alpha)
            self.assertEqual(N,expected)
            self.assertGreater(alpha*N,1)
        with self.assertRaises(HilbertZenoError): holder_no_go_dimension(F(0))

    def test_effective_horizon_cost_and_resource_debt(self):
        proof=hilbert_cube_horizon(F(1),F(1,3))
        self.assertEqual((proof.coordinate_depth,proof.mesh_level,proof.grid_points), (2,2,16))
        self.assertEqual(proof.error,F(1,3))
        self.assertFalse(proof.physical_tasks_executed)
        with self.assertRaisesRegex(HilbertZenoError,"RESOURCE_BUDGET"):
            hilbert_cube_horizon(F(1),F(1,8),max_points=1000)
        with self.assertRaisesRegex(HilbertZenoError,"COMPUTATION_HORIZON"):
            hilbert_cube_horizon(F(1),F(1,8),max_level=3)

    def test_independent_exact_diagonal_infimum_in_cube_interval(self):
        diagonal=(F(-3,2),F(2),F(-1,7))
        A=tuple(tuple(diagonal[i] if i==j else F(0) for j in range(3)) for i in range(3))
        model=QuadraticSource(H,A,F(2),F(0),True)
        m_true=sum((diagonal[j]/4**(j+1) for j in range(3) if diagonal[j]<0),F(0))
        self.assertEqual(m_true,-F(169,448))
        for level in range(1,5):
            certificate=certify_hilbert_cube(model,level)
            self.assertLessEqual(certificate.global_infimum_lower,m_true)
            self.assertGreaterEqual(certificate.global_infimum_upper,m_true)
            self.assertLess(certificate.global_infimum_upper,0)

    def test_geometric_error_budget_is_exact(self):
        self.assertEqual(hilbert_cube_error(1,2,2),F(1,3))
        self.assertEqual(hilbert_cube_error(3,4,4),F(1,4))
        self.assertGreater(hilbert_cube_error(1,3,3),hilbert_cube_error(1,5,5))
        with self.assertRaises(HilbertZenoError):hilbert_cube_error(-1,2,3)

    def test_two_coordinate_grid_visits_exactly_hilbert_order(self):
        level=2
        values=tuple(cube_parameter_grid(level,2))
        self.assertEqual(len(values),16)
        expected=tuple((F(1,2)*(F(2*x+1,4)-1),
                        F(1,4)*(F(2*y+1,4)-1)) for x,y in hilbert_cells(level))
        self.assertEqual(values,expected)
        self.assertEqual(len(set(values)),16)

    def test_all_dimensional_cell_midpoint_bounds(self):
        for d in (1,2,3):
            pts=tuple(cube_parameter_grid(2,d))
            self.assertEqual(len(pts),4**d)
            for p in pts:
                for j,x in enumerate(p,1):
                    self.assertLessEqual(abs(x),F(1,2**j))

    def test_finite_rank_negative_operator_detected(self):
        A=QuadraticSource(H,((F(-1),F(0)),(F(0),F(1))),F(1),F(0),True)
        result=certify_hilbert_cube(A,2)
        self.assertEqual(result.verdict,"CERTIFIED_NEGATIVE_FINITE_RANK")
        self.assertLess(result.global_infimum_upper,0)
        self.assertLess(result.global_infimum_lower,result.global_infimum_upper)
        self.assertFalse(result.RH_proved)
        self.assertTrue(result.original_operator_identified)

    def test_negative_at_arbitrarily_deep_source_coordinate(self):
        N=5
        missing=QuadraticSource(H,tuple(tuple(F(0) for _ in range(N-1))
                                         for _ in range(N-1)),F(1),F(0),False)
        first=certify_hilbert_cube(missing,1)
        self.assertEqual(first.verdict,"UNRESOLVED")
        self.assertEqual(first.minimum_matrix_value,0)
        self.assertLess(first.global_infimum_lower,0)
        full=tuple(tuple(F(-1) if i==j==N-1 else F(0) for j in range(N)) for i in range(N))
        true=QuadraticSource(H,full,F(1),F(0),True)
        second=certify_hilbert_cube(true,1)
        self.assertEqual(second.verdict,"CERTIFIED_NEGATIVE_FINITE_RANK")
        self.assertEqual(second.minimum_matrix_value,-F(1,4**N*4))
        self.assertLess(second.global_infimum_upper,0)

    def test_positive_operator_sampling_never_forges_global_sign(self):
        A=QuadraticSource(H,((F(1),F(0)),(F(0),F(1))),F(1),F(0),True)
        for level in (1,2,3):
            r=certify_hilbert_cube(A,level)
            self.assertEqual(r.verdict,"UNRESOLVED")
            self.assertLess(r.global_infimum_lower,0)
            self.assertGreaterEqual(r.minimum_matrix_value,0)

    def test_entry_interval_honesty_and_unverified_source(self):
        partial=QuadraticSource(H,((F(-1),),),F(2),F(1,10),False)
        r=certify_hilbert_cube(partial,2)
        self.assertEqual(r.verdict,"CONDITIONAL_NEGATIVE_SOURCE_WITNESS")
        self.assertFalse(r.original_operator_identified)
        self.assertEqual(r.entry_error,F(1,40))

    def test_wrong_exact_source_bound_rejected(self):
        with self.assertRaises(HilbertZenoError):
            QuadraticSource(H,((F(2),),),F(1),F(0),True)
        with self.assertRaises(HilbertZenoError):
            QuadraticSource(H,[[F(1)]],F(1),F(0),True)
        with self.assertRaises(HilbertZenoError):
            QuadraticSource(H,((F(0),F(2)),(F(1),F(0))),F(2))
        with self.assertRaises(HilbertZenoError):
            QuadraticSource(H,((F(1),),),F(1),F(1,4),True)
        with self.assertRaises(HilbertZenoError):
            certify_hilbert_cube(QuadraticSource(H,((F(1),),),F(1),F(0),True),7,max_points=10)

    def test_gram_metric_source_coefficients_not_signed_weil(self):
        x=exact_neumann_legendre_2x2(F(1,2))
        self.assertEqual(x,((F(1,30),F(0)),(F(0),F(1,210))))
        self.assertGreater(x[0][0]*x[1][1]-x[0][1]*x[1][0],0)
        with self.assertRaises(HilbertZenoError): exact_neumann_legendre_2x2(F(0))

    def test_normalized_suzuki_metric_low_block_not_full_weil_operator(self):
        K=normalized_neumann_legendre_2x2(F(1,2))
        self.assertEqual(K,((F(1,10),F(0)),(F(0),F(1,42))))
        # The true metric continues to infinitely many Legendre channels;
        # a finite low block cannot be designated the whole source.
        source=QuadraticSource(H,K,F(1),F(0),False)
        c=certify_hilbert_cube(source,2)
        self.assertEqual(c.verdict,"UNRESOLVED")
        self.assertFalse(c.original_operator_identified)

    def test_actual_integrated_suzuki_source_metric_matches(self):
        try:
            from observational_succ import suzuki_moment_schur
        except ImportError:
            self.skipTest("full SUCC source module absent from isolated local overlay; GitHub CI must test")
        self.assertTrue(hilbert_source_bridge_check())
        self.assertEqual(exact_neumann_legendre_2x2(F(1,2)),
                         suzuki_moment_schur.low_inverse_neumann(F(1,2),2))


if __name__=="__main__":
    unittest.main()
