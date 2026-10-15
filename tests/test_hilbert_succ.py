"""Exact Hilbert successor tests: honest finite geometry, strata, source pinned original Weil."""
from __future__ import annotations

from dataclasses import replace
import json
from fractions import Fraction as Q
from math import isqrt, comb
from pathlib import Path
import unittest

from observational_succ.hilbert_succ import (
    HilbertCell, HilbertSourceError, PINNED_WEIL_BLOB, ORIGINAL_WEIL_SOURCE,
    rational, hilbert_index_xy, hilbert_xy_index, hilbert_cell, hilbert_cells,
    hilbert_parent, hilbert_parent_consistency, hilbert_adjacency_receipt,
    interval_clock_vector, spatial_chart_to_clock, clock_to_spatial_chart,
    hilbert_inner_product, hilbert_refinement, lipschitz_square_error,
    hilbert_square_midpoint_average, monomial_square_integral, monomial_strata,
    diagonal_band_true_integral, diagonal_band_hilbert_sample,
    diagonal_zeno_mutant, hilbert_dimension_obstruction,
    genuine_suzuki_hilbert_scan, source_rayleigh_by_hilbert_succ,
    source_locality_budget, source_scan_locality_check,
    source_certified_rayleigh_interval, original_weil_measure_strata,
    source_hilbert_hilbert_schmidt_identity,
)


class TestHilbertFinitePaths(unittest.TestCase):
    def test_exact_cells_and_inverse(self):
        for level in range(0,6):
            n=1<<level
            seen=set()
            for d in range(n*n):
                x,y=hilbert_index_xy(level,d)
                self.assertEqual(hilbert_xy_index(level,x,y),d)
                seen.add((x,y))
            self.assertEqual(len(seen),n*n)

    def test_quartic_source_prefix_natural(self):
        for level in range(1,6):
            self.assertTrue(hilbert_parent_consistency(level))
            for d in (0,1, (1<<(2*level))//2, (1<<(2*level))-1):
                parent_idx=hilbert_parent(level,d)[1]
                x,y=hilbert_index_xy(level,d)
                self.assertEqual((x//2,y//2),hilbert_index_xy(level-1,parent_idx))

    def test_succ_movement_is_always_edge(self):
        for level in range(1,6):
            rep=hilbert_adjacency_receipt(level)
            self.assertEqual(rep['source_cells'],4**level)
            self.assertEqual(rep['distinct'],4**level)
            self.assertEqual(rep['max_taxicab_step'],1)
            self.assertFalse(rep['nonlawful_transitions'])
            self.assertTrue(rep['parent_consistency'])
            self.assertFalse(rep['actual_infinity_completed'])

    def test_level_zero_is_one_global_proto_cell(self):
        self.assertEqual(hilbert_index_xy(0,0),(0,0))
        self.assertEqual(hilbert_xy_index(0,0,0),0)
        self.assertEqual(hilbert_cell(0,0).clock_midpoint,Q(1,2))
        self.assertRaises(HilbertSourceError,hilbert_parent,0,0)

    def test_small_hilbert_is_not_raster_scan(self):
        ordered=[hilbert_index_xy(2,d) for d in range(16)]
        self.assertNotEqual(ordered,[(x,y) for x in range(4) for y in range(4)])
        self.assertEqual(max(abs(ordered[k][0]-ordered[k+1][0])+abs(ordered[k][1]-ordered[k+1][1])
                             for k in range(15)),1)
        raster=[(x,y) for x in range(4) for y in range(4)]
        self.assertEqual(max(abs(raster[k][0]-raster[k+1][0])+abs(raster[k][1]-raster[k+1][1])
                             for k in range(15)),4)

    def test_spatial_clock_roundtrip(self):
        for level in range(4):
            n=1<<level
            src=tuple(tuple(Q((3*i+7*j)%11,13) for j in range(n)) for i in range(n))
            mapped=spatial_chart_to_clock(level,src)
            self.assertEqual(clock_to_spatial_chart(level,mapped),src)
            self.assertEqual(len(mapped),n*n)

    def test_exact_step_norm_and_cross_pairing(self):
        for level in range(4):
            n=1<<(2*level)
            v=tuple(Q((i%5)-2,7) for i in range(n))
            w=tuple(Q((i%7)-3,5) for i in range(n))
            lhs=hilbert_inner_product(level,v,w)
            fine_v=hilbert_refinement(level,v)
            fine_w=hilbert_refinement(level,w)
            self.assertEqual(lhs,hilbert_inner_product(level+1,fine_v,fine_w))
            spatial=clock_to_spatial_chart(level,v)
            children=clock_to_spatial_chart(level+1,fine_v)
            for x in range(1<<level):
                for y in range(1<<level):
                    self.assertEqual({children[2*x+i][2*y+j] for i in (0,1) for j in (0,1)},
                                     {spatial[x][y]})

    def test_unitary_not_operator_sign_magic(self):
        # A negative indefinite diagonal form stays negative after a Hilbert permutation.
        v=(Q(1),Q(0),Q(0),Q(0))
        spatial=( (Q(-3),Q()), (Q(),Q(5)) )
        perm=spatial_chart_to_clock(1,spatial)
        self.assertEqual(sorted(perm),[Q(-3),Q(),Q(),Q(5)])
        self.assertEqual(sum(x*x for x in v),1)
        self.assertLess(min(perm),0)

    def test_exact_input_and_resource_guards(self):
        calls=[
            lambda: rational(True), lambda: rational(0.5),
            lambda: hilbert_index_xy(1,True),lambda:hilbert_index_xy(-1,0),
            lambda:hilbert_index_xy(9,0),lambda:hilbert_index_xy(2,16),
            lambda:hilbert_xy_index(2,4,1),lambda:hilbert_xy_index(2,False,1),
            lambda:hilbert_parent_consistency(0),
            lambda:interval_clock_vector(2,(Q(),)*3),
            lambda:spatial_chart_to_clock(1,((0,1),)),
            lambda:hilbert_refinement(6,(Q(),)*4096),
        ]
        for call in calls:
            with self.subTest(call=str(call)):
                with self.assertRaises(HilbertSourceError):call()


class TestDyadicAnalyticSource(unittest.TestCase):
    def test_exact_integral_midpoint_error_bound(self):
        for level in range(0,6):
            avg=hilbert_square_midpoint_average(level,lambda x,y:x*x+y*y)
            n=1<<level
            exact=Q(2,3)
            self.assertEqual(exact-avg,Q(1,6*n*n))
            self.assertLessEqual(abs(exact-avg),lipschitz_square_error(level,Q(4)))

    def test_monomial_exact_integrals(self):
        for i in range(5):
            for j in range(5):
                self.assertEqual(monomial_square_integral(i,j),Q(1,(i+1)*(j+1)))
        self.assertEqual(hilbert_square_midpoint_average(3,lambda x,y:x+y),1)
        self.assertEqual(hilbert_square_midpoint_average(3,lambda x,y:x*y),Q(1,4))

    def test_lipschitz_certificates_dont_accept_invented_sign(self):
        self.assertEqual(lipschitz_square_error(3,Q(4)),Q(1,4))
        with self.assertRaises(HilbertSourceError):lipschitz_square_error(4,Q(-1))
        with self.assertRaises(HilbertSourceError):
            hilbert_square_midpoint_average(2,lambda x,y:0.125)

    def test_same_space_different_measure_strata(self):
        r=monomial_strata(1,1,Q(1,2))
        self.assertEqual(r['bulk_area_measure'],Q(1,4))
        self.assertEqual(r['diagonal_contact_measure'],Q(1,3))
        self.assertEqual(r['one_dimensional_shift_graph_measure'],Q(5,48))
        self.assertTrue(r['geometric_shift_is_NOT_authenticated_prime'])
        self.assertNotEqual(r['bulk_area_measure'],r['diagonal_contact_measure'])
        self.assertNotEqual(r['diagonal_contact_measure'],r['one_dimensional_shift_graph_measure'])

    def test_strata_formulas_from_independent_polynomial_integrals(self):
        for i,j in [(0,0),(1,0),(0,2),(2,2),(3,1)]:
            b=Q(2,5);r=monomial_strata(i,j,b)
            # Primitive for (x+b)^i x^j checked by exact binomial expansion.
            term=sum(Q(comb(i,k))*b**(i-k)*(1-b)**(j+k+1)/Q(j+k+1)
                     for k in range(i+1))
            self.assertEqual(r['one_dimensional_shift_graph_measure'],term)

    def test_exact_delta_mollifier_vs_pixel_observer(self):
        for level in range(1,6):
            n=1<<level
            r=diagonal_zeno_mutant(level)
            self.assertEqual(r['bulk_2d_midpoint_observer'],n)
            self.assertEqual(r['true_2d_area_integral'],1-Q(1,4*n*n))
            self.assertGreater(r['bulk_2d_midpoint_observer'],r['true_2d_area_integral'])
            self.assertTrue(r['two_limit_exchange_unjustified'])

    def test_mollifier_order_of_limits_is_not_a_theorem(self):
        # For fixed fine enough mesh compared with eps, midpoint sampling approaches area.
        # For eps_n=mesh^2 the samples grow like N while integral tends to one.
        self.assertEqual(diagonal_band_hilbert_sample(4,Q(1,256)),16)
        self.assertEqual(diagonal_band_true_integral(Q(1,256)),Q(1023,1024))
        self.assertEqual(diagonal_band_hilbert_sample(5,Q(1,1024)),32)
        self.assertEqual(diagonal_band_true_integral(Q(1,1024)),Q(4095,4096))

    def test_contact_is_singular_not_any_2d_lebesgue_density(self):
        r=monomial_strata(2,0,Q(1,4))
        self.assertEqual(r['bulk_area_measure'],Q(1,3))
        self.assertEqual(r['diagonal_contact_measure'],Q(1,3))
        self.assertNotEqual(r['one_dimensional_shift_graph_measure'],Q(1,3))
        # For support measure it is graph/diagonal dimensionality, not a coincidental scalar.
        x=monomial_strata(1,1,Q(1,4))
        self.assertEqual(x['diagonal_contact_measure'],Q(1,3))
        self.assertNotEqual(x['bulk_area_measure'],x['diagonal_contact_measure'])

    def test_wrong_measure_or_bad_density_refused(self):
        for fn in (
            lambda:monomial_strata(1,2,0),
            lambda:monomial_strata(1,2,1),
            lambda:monomial_strata(1,2,Q(-1,2)),
            lambda:monomial_strata(1,2,0.3),
            lambda:diagonal_band_hilbert_sample(1,0),
            lambda:diagonal_band_true_integral(Q(2)),
            lambda:hilbert_dimension_obstruction(0,Q(1,2)),
            lambda:hilbert_dimension_obstruction(2,0.5),
        ):
            with self.subTest(fn=fn):
                with self.assertRaises(HilbertSourceError):fn()

    def test_holder_dimension_debt_for_infinite_ambient_carrier(self):
        self.assertTrue(hilbert_dimension_obstruction(2,Q(3,4))['surjective_holder_map_refuted'])
        self.assertTrue(hilbert_dimension_obstruction(3,Q(1,2))['surjective_holder_map_refuted'])
        self.assertFalse(hilbert_dimension_obstruction(3,Q(1,3))['surjective_holder_map_refuted'])
        for d in (2,4,8,16,64):
            self.assertTrue(hilbert_dimension_obstruction(d,Q(2,d))['surjective_holder_map_refuted'])
            self.assertEqual(hilbert_dimension_obstruction(d,Q(1,d))['covering_volume_power'],0)


class TestOriginalWeilHilbertAdapter(unittest.TestCase):
    """Runs on real integrated main source in GitHub CI; never mocked as RH evidence."""
    @classmethod
    def setUpClass(cls):
        source=Path(__file__).resolve().parents[1]/'observational_succ'/'source_weil_hierarchy.py'
        if not source.exists():
            raise unittest.SkipTest('ISOLATED LOCAL OVERLAY ONLY: original Weil source absent; REMOTE CI MUST REQUIRE IT')
        cls.scan=genuine_suzuki_hilbert_scan(Q(1,2),3,2)

    def test_actual_source_singular_strata_are_not_flat_area(self):
        v=original_weil_measure_strata(Q(1,2))
        self.assertEqual(v['source_blob'],PINNED_WEIL_BLOB)
        self.assertEqual(v['gamma_positive_bulk']['dimension'],2)
        self.assertTrue(v['gamma_positive_bulk']['kernel_needs_diagonal_cancellation'])
        self.assertEqual(v['contact_diagonal']['dimension'],1)
        self.assertLess(v['contact_diagonal']['coefficient_interval'][1],0)
        self.assertEqual([q['n'] for q in v['prime_shift_graphs']],[2])
        self.assertEqual(v['prime_shift_graphs'][0]['primitive_prime'],2)
        self.assertEqual(v['pole_even']['coefficient'],2)
        self.assertEqual(v['pole_odd']['coefficient'],-2)
        self.assertFalse(v['original_RH_positivity_proved'])

    def test_prime_wavefront_and_false_composite_fail(self):
        v=original_weil_measure_strata(Q(1))
        self.assertEqual([q['n'] for q in v['prime_shift_graphs']],[2,3,4,5,7])
        self.assertNotIn(6,[q['n'] for q in v['prime_shift_graphs']])
        self.assertEqual(next(q for q in v['prime_shift_graphs'] if q['n']==4)['primitive_prime'],2)
        with self.assertRaises(HilbertSourceError):original_weil_measure_strata(0.5)

    def test_original_source_pinned_and_negative_not_suppressed(self):
        scan=self.scan
        self.assertEqual(scan.source_blob,PINNED_WEIL_BLOB)
        self.assertEqual(scan.source,ORIGINAL_WEIL_SOURCE)
        self.assertTrue(scan.signed_kernel)
        self.assertFalse(scan.rh_proved)
        self.assertGreater(scan.source_operator_norm_error,0)
        self.assertEqual(len(scan.hilbert_matrix_cells),16)

    def test_original_matrix_exact_hilbert_vs_raster(self):
        from observational_succ import source_weil_hierarchy as source
        parent=source.stage(Q(1,2),3,4)
        self.assertEqual(parent.center[0][0],self.scan.hilbert_matrix_cells[0][2])
        for idx,(x,y,value) in enumerate(self.scan.hilbert_matrix_cells):
            self.assertEqual((x,y),hilbert_index_xy(2,idx))
            self.assertEqual(parent.center[x][y],value)

    def test_original_source_rayleigh_equals_parent_original(self):
        from observational_succ import source_weil_hierarchy as source
        v=(Q(1),Q(-1),Q(2),Q(-2))
        actual=source_rayleigh_by_hilbert_succ(self.scan,v)
        self.assertEqual(actual,source.exact_rayleigh(source.stage(Q(1,2),3,4).center,v))
        lo,hi=source_certified_rayleigh_interval(self.scan,v)
        self.assertEqual((lo+hi)/2,actual)
        self.assertEqual(hi-lo,2*self.scan.source_operator_norm_error)

    def test_genuine_operator_hs_as_clock_energy_not_sign(self):
        h=source_hilbert_hilbert_schmidt_identity(self.scan)
        self.assertTrue(h['exact_L2_source_identity'])
        self.assertEqual(h['signed_matrix_HS_norm_squared'],
                         h['hilbert_clock_energy_scaled'])
        self.assertTrue(h['Hilbert_flattening_does_not_imply_PSD'])

    def test_true_gamma_and_prime_source_locality(self):
        rep=source_scan_locality_check(self.scan)
        self.assertTrue(rep['all_consecutive_original_source_readouts_lipschitz_certified'])
        self.assertLessEqual(rep['maximum_exact_difference'],source_locality_budget(self.scan))
        self.assertFalse(rep['whole_Weil_PSD_proved'])

    def test_source_controls_refuse_fake_spectral_labels(self):
        with self.assertRaises(HilbertSourceError):
            source_rayleigh_by_hilbert_succ(replace(self.scan,source='composite6_primitive'),(1,-1,2,-2))
        with self.assertRaises(HilbertSourceError):
            source_rayleigh_by_hilbert_succ(replace(self.scan,rh_proved=True),(1,-1,2,-2))
        with self.assertRaises(HilbertSourceError):
            source_rayleigh_by_hilbert_succ(replace(self.scan,hilbert_matrix_cells=self.scan.hilbert_matrix_cells[::-1]),(1,-1,2,-2))
        with self.assertRaises(HilbertSourceError):
            source_rayleigh_by_hilbert_succ(self.scan,(1,1,-1,0))

    def test_true_source_stage_refinement_has_existing_error_not_hilbert_magic(self):
        n4=self.scan
        n8=genuine_suzuki_hilbert_scan(Q(1,2),3,3)
        v=(1,-1,2,-2)
        coarse=source_rayleigh_by_hilbert_succ(n4,v)
        fine=source_rayleigh_by_hilbert_succ(n8,tuple(x for k in v for x in (k,k)))
        self.assertLessEqual(abs(coarse-fine),n4.source_operator_norm_error+n8.source_operator_norm_error)
        self.assertFalse(n8.rh_proved)


if __name__=='__main__':
    unittest.main()


class TestScientificReceipt(unittest.TestCase):
    def test_exact_original_rational_source_replay(self):
        from scripts.hilbert_succ_probe import receipt
        root=Path(__file__).resolve().parents[1]
        saved=root/'research'/'2026-10-14'/'HILBERT_SUCC_SOURCE_RECEIPT.json'
        self.assertEqual(json.loads(saved.read_text()),receipt())
        self.assertFalse(receipt()['RH_PROVED'])
        self.assertFalse(receipt()['physical_infinite_traversal'])
