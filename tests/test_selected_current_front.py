"""Exact original BBP selected-current research tests, no pi digits."""
from __future__ import annotations
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

MOD=Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'selected_current_front'/'selected_current.py'
spec=importlib.util.spec_from_file_location('selected_current_front',MOD)
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def independent_crossing_integral(x:F,y:F,m:int)->F:
    """Integrate an equality of two bin labels from all *critical origins*."""
    edges={F(0),F(1)}
    for p in (F(x),F(y)):
        edges.update(((F(j,m)-p)%1 for j in range(m)))
    edges=sorted(edges)
    mismatch=F(0)
    for lo,hi in zip(edges,edges[1:]):
        origin=(lo+hi)/2
        if c.bin_index(x,m,origin)!=c.bin_index(y,m,origin):
            mismatch+=hi-lo
    return mismatch


class SelectedSourceExactness(unittest.TestCase):
    def test_original_immutable_source(self):
        self.assertEqual(c.source_force(1),F(47,15))
        self.assertEqual(c.source_force(2),F(106,819))
        self.assertEqual(c.source_epoch(1),(F(2,15),))

    def test_preregistered_independent_original_source_epochs(self):
        for A in (40,80,160):
            with self.subTest(A=A):
                self.assertEqual(c.source_epoch(A),c.independent_modular_epoch(A))
                self.assertEqual(len(c.source_epoch(A)),A)
                self.assertTrue(all(x.denominator%2 for x in c.source_epoch(A)))

    def test_preregistered_all_meshes_slow_cylinder(self):
        for A in (40,80,160):
            p=c.source_epoch(A)
            for m in (8,16,32):
                with self.subTest(A=A,m=m):
                    q=c.canonical_vs_translated_bound(p,m)
                    self.assertLessEqual(q['canonical_energy'],q['certified_upper'])
                    self.assertGreaterEqual(q['translation_averaged_half_mesh'],1)

    def test_independent_exact_origin_integral_synthetic(self):
        sources=[(F(0),F(1,4)),(F(0),F(1,3),F(2,3)),
                 (F(1,5),)*5,(F(1,2),F(1,2),F(1,2),F(1,7))]
        for p in sources:
            for m in (2,4,8,16):
                with self.subTest(p=p,m=m):
                    self.assertEqual(c.translated_energy(p,m),c.independent_origin_integral(p,m))

    def test_preregistered_exact_origin_integral_original(self):
        for A in (12,24):
            p=c.source_epoch(A)
            for m in (4,8,16):
                with self.subTest(A=A,m=m):
                    self.assertEqual(c.translated_energy(p,m),c.independent_origin_integral(p,m))

    def test_selected_branch_square_at_levels(self):
        for A in (40,80):
            p=c.source_epoch(A)
            for depth in (0,1,2):
                with self.subTest(A=A,depth=depth):
                    self.assertEqual(c.exact_current_increment(p,depth),
                                     c.independent_branch_square(p,depth))
                    self.assertGreaterEqual(c.translated_branch_increment(p,depth),0)

    def test_exact_shift_average_of_time_branch_squares(self):
        p=c.source_epoch(12)
        for level in (0,1):
            # Independent breakpoint integration for two adjacent depths.
            self.assertEqual(c.translated_branch_increment(p,level),
                             c.independent_origin_integral(p,16**(level+1))-
                             c.independent_origin_integral(p,16**level))

    def test_original_source_positive_bound_on_preregistered_epochs(self):
        for A in (40,80,160):
            for n in range(A,2*A):
                self.assertGreater(c.source_force(n+1),0)
                self.assertLess(c.source_force(n+1),F(15,(8*n+1)*(8*n+2)))

    def test_translated_boundary_crossing_identity(self):
        for p,q,m in ((F(1,5),F(3,10),8),(F(0),F(1,8),4),
                      (F(7,17),F(2,17),8),(F(1,4),F(3,4),16)):
            with self.subTest(p=p,q=q,m=m):
                self.assertEqual(independent_crossing_integral(p,q,m),
                                 min(F(1),m*c.circle_distance(q-p)))

    def test_actual_original_forcing_crossings_and_bound(self):
        for A in (12,40,80):
            # Verify each actual arrow from exact rational source and forcing.
            x=F(0)
            for n in range(1,2*A+1):
                old=x;x=(16*x+c.source_force(n))%1
                if A+1<=n<=2*A:
                    self.assertEqual(c.circle_distance(x-(16*old)%1),
                                     c.circle_distance(c.source_force(n)))
            for m in (4,8,16):
                with self.subTest(A=A,m=m):
                    self.assertLessEqual(c.forced_boundary_mean(A,m),c.forced_boundary_cap(A,m))
                    self.assertGreaterEqual(c.source_stationarity_ell1_cap(A,m),0)

    def test_gamma_energy_transport_with_synthetic_monotone_tail(self):
        # This checks a general Lipschitz comparison with a declared artificial
        # tail. It is not a measurement of true unknown pi or the actual Gamma T.
        for A in (12,40):
            p=c.source_epoch(A)
            synthetic=tuple((x+F(1,128*n*n))%1 for n,x in enumerate(p,A))
            for m in (8,16):
                actual=abs(c.translated_energy(p,m)-c.translated_energy(synthetic,m))
                self.assertLessEqual(actual,c.gamma_tail_energy_transport_bound(A,m))

    def test_rotational_gauge_keeps_selected_tent_energy(self):
        p=c.source_epoch(40)
        for t in (F(1,7),F(3,16),F(19,37)):
            self.assertEqual(c.translated_energy(p,16),
                             c.translated_energy(tuple((x+t)%1 for x in p),16))

    def test_point_mass_cannot_be_made_haar_by_origin_average(self):
        for m in (4,16,256):
            witness=c.periodic_fixed_point_control(m)
            self.assertEqual(witness['canonical_energy'],m)
            self.assertEqual(witness['translated_energy'],m)

    def test_endpoint_and_zero_anchoring(self):
        p=(F(0), F(1,16), F(1,2), F(15,16))
        self.assertEqual(c.bin_index(F(1,16),16),1)
        self.assertEqual(c.bin_index(F(0),16),0)
        self.assertEqual(c.bin_index(F(-1,16),16),15)
        self.assertGreaterEqual(c.translated_energy(p,16),1)

    def test_invalid_mesh_and_empty_inputs(self):
        with self.assertRaises(ValueError):c.translated_energy((),16)
        self.assertEqual(c.translated_energy((F(0),),1),1)
        with self.assertRaises(ValueError):c.tent_kernel(F(0),1)
        with self.assertRaises(ValueError):c.canonical_vs_translated_bound((F(0),),5)
        with self.assertRaises(ValueError):c.source_epoch(0)
        with self.assertRaises(ValueError):c.source_force(0)


if __name__ == '__main__': unittest.main()
