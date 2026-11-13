"""Exact hostile controls for SUCC finite gauge quotient and scale-gap logic."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
import random
import unittest

from observational_succ.yang_mills_gauge_oracle import (
    AbelianGaugeGraph, GaugeOracleError, Torus4D, wilson_orbit_energy,
    two_state_reflection_eigenvalues, transfer_spectral_ratio,
    gap_lower_from_ratio, quadratic_mass_upper, finite_cutoff_twins,
    compose_s3, trace_s3, nonabelian_trace_counterexample,
    S3GaugeGraph, S3_ELEMENTS, S3_ID, inverse_s3, conjugate_s3, s3_subdivision_square,
)


class GaugeQuotientTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = AbelianGaugeGraph(('a','b','c','d'),
                (('a','b'),('b','c'),('c','d'),('d','a'),('a','c')), 3)

    def test_tree_rank_orbit_count_with_independent_exhaustive_enumeration(self):
        g = self.g
        self.assertEqual(g.cycle_rank,2)
        self.assertEqual((g.orbit_count,g.orbit_size),(9,27))
        states = list(product(range(g.q), repeat=len(g.edges)))
        bags = Counter(g.holonomies(x) for x in states)
        self.assertEqual(len(bags),9)
        self.assertEqual(set(bags.values()), {27})
        self.assertEqual(sum(bags.values()),3**5)

    def test_gauge_action_and_canonical_uniqueness_exhaustive(self):
        g = self.g
        for links in product(range(g.q), repeat=len(g.edges)):
            canonical = g.canonical(links)
            self.assertTrue(all(canonical[i] == 0 for _,_,i,_ in g.tree()))
            self.assertEqual(canonical, g.canonical(canonical))
            for phi in product(range(g.q), repeat=len(g.vertices)):
                candidate = g.transform(links,phi)
                self.assertEqual(g.holonomies(candidate),g.holonomies(links))
                self.assertTrue(g.orbit_equal(candidate,links))

    def test_complete_quotient_pinbed_distinguishes_coarse_false_haar(self):
        g=self.g
        tree_indices={i for _,_,i,_ in g.tree()}
        chords=[i for i in range(len(g.edges)) if i not in tree_indices]
        # All nine quotient points have zero full-source Haar discrepancy.
        all_orbits=[]
        for x,y in product(range(3),repeat=2):
            c=[0]*len(g.edges);c[chords[0]]=x;c[chords[1]]=y
            all_orbits.append(tuple(c))
        self.assertEqual(wilson_orbit_energy(g,tuple(all_orbits)),Q(0))
        one=tuple(all_orbits[:1]*9)
        self.assertEqual(wilson_orbit_energy(g,one),Q(8))
        # Missing one chord gives a perfectly uniform coarse channel,
        # while the actual gauge-quotient distribution remains non-Haar.
        partial=tuple(x for x in all_orbits if g.holonomies(x)[1]==0)
        self.assertEqual(len(set(g.holonomies(x)[0] for x in partial)),3)
        self.assertEqual(wilson_orbit_energy(g,partial),Q(2))
        shifted=tuple(g.transform(x,(0,1,1,2)) for x in partial)
        self.assertEqual(wilson_orbit_energy(g,shifted),wilson_orbit_energy(g,partial))
        with self.assertRaises(GaugeOracleError): wilson_orbit_energy(g,())

    def test_gauge_action_composition_and_global_center(self):
        g = self.g
        links=(1,2,1,0,2)
        phi=(0,1,1,2)
        psi=(2,0,2,1)
        combined=tuple((u+v)%3 for u,v in zip(phi,psi))
        self.assertEqual(g.transform(g.transform(links,phi),psi),g.transform(links,combined))
        self.assertEqual(g.transform(links,(2,2,2,2)),links)
        self.assertEqual(g.holonomies(links),g.holonomies(g.canonical(links)))

    def test_missing_chord_observer_is_incomplete(self):
        g=self.g
        first=(0,0,0,0,0)
        chords=[i for i in range(len(g.edges)) if i not in {t[2] for t in g.tree()}]
        second=tuple(1 if i == chords[-1] else 0 for i in range(len(g.edges)))
        self.assertFalse(g.orbit_equal(first,second))
        self.assertEqual(g.holonomies(first)[0],g.holonomies(second)[0])
        self.assertNotEqual(g.holonomies(first),g.holonomies(second))

    def test_malformed_source_rejected(self):
        with self.assertRaises(GaugeOracleError): AbelianGaugeGraph(('a','b'),(),3)
        with self.assertRaises(GaugeOracleError): AbelianGaugeGraph(('a','a'),(),3)
        with self.assertRaises(GaugeOracleError): AbelianGaugeGraph(('a','b'),(('a','a'),),3)
        with self.assertRaises(GaugeOracleError): AbelianGaugeGraph(('a','b'),(('a','b'),),True)
        with self.assertRaises(GaugeOracleError): self.g.holonomies((0,)*4)
        with self.assertRaises(GaugeOracleError): self.g.transform((0,)*5,(0,)*3)
        with self.assertRaises(GaugeOracleError): self.g.transform((0,)*5,(0,1,2,True))


class FourDimensionalLatticeTest(unittest.TestCase):
    def test_true_4d_plaquette_gauge_invariance_and_bianchi(self):
        rng=random.Random(0xBABA2026)
        for q in (2,3,5):
            t=Torus4D(2,q)
            self.assertEqual((len(t.sites),t.link_count,t.plaquette_count),(16,64,96))
            for case in range(5):
                A=tuple(rng.randrange(q) for _ in range(t.link_count))
                phi=tuple(rng.randrange(q) for _ in range(16))
                B=t.transform(A,phi)
                self.assertEqual(t.curvature_signature(A),t.curvature_signature(B))
                for x in t.sites:
                    for triple in combinations(range(4),3):
                        self.assertEqual(t.cube_bianchi(A,x,*triple),0)
                    for axis in range(4):
                        self.assertEqual(t.wilson_cycle(A,x,axis),t.wilson_cycle(B,x,axis))

    def test_topological_flat_holonomy_defeats_local_curvature_oracle(self):
        for q in (2,3,5):
            t=Torus4D(2,q)
            vacuum=t.zero()
            flat=t.flat_nontrivial()
            self.assertEqual(t.curvature_signature(vacuum),t.curvature_signature(flat))
            self.assertTrue(all(f==0 for f in t.curvature_signature(flat)))
            for x in t.sites:
                self.assertEqual(t.wilson_cycle(flat,x,0),1)
                self.assertEqual(t.wilson_cycle(vacuum,x,0),0)
                for axis in (1,2,3): self.assertEqual(t.wilson_cycle(flat,x,axis),0)
            self.assertNotEqual(vacuum, flat)

    def test_pure_gauge_has_zero_local_and_global_curvature(self):
        rng=random.Random(54)
        t=Torus4D(3,3)
        zero=t.zero()
        pot=tuple(rng.randrange(3) for _ in range(len(t.sites)))
        transformed=t.transform(zero,pot)
        self.assertEqual(t.curvature_signature(transformed),t.curvature_signature(zero))
        for x in t.sites:
            for axis in range(4): self.assertEqual(t.wilson_cycle(transformed,x,axis),0)

    def test_invalid_lattice_inputs_and_bianchi_orders(self):
        t=Torus4D(2,3)
        with self.assertRaises(GaugeOracleError): t.transform(t.zero(),(0,))
        with self.assertRaises(GaugeOracleError): t.curvature_signature((0,)*60)
        with self.assertRaises(GaugeOracleError): t.plaquette(t.zero(),(0,0,0,2),0,1)
        with self.assertRaises(GaugeOracleError): t.plaquette(t.zero(),(0,0,0,0),2,1)
        with self.assertRaises(GaugeOracleError): t.cube_bianchi(t.zero(),(0,0,0,0),2,1,0)
        with self.assertRaises(GaugeOracleError): t.wilson_cycle(t.zero(),(0,0,0,0),4)
        with self.assertRaises(GaugeOracleError): Torus4D(1,2)


class FiniteNonabelianGaugeTest(unittest.TestCase):
    def test_simultaneous_conjugacy_classifies_s3_gauge_orbits(self):
        g=S3GaugeGraph(('u','v'),(('u','v'),('u','v'),('u','v')))
        all_links=tuple(product(S3_ELEMENTS,repeat=3))
        counts=Counter(g.orbit_key(A) for A in all_links)
        # Burnside: (6^2 + 3*2^2 + 2*3^2)/6 = 11.
        self.assertEqual(len(counts),11)
        self.assertEqual(sum(counts.values()),6**3)
        for links in all_links:
            canon=g.canonical_tree(links)
            self.assertEqual(canon[0],S3_ID)
            self.assertEqual(g.orbit_key(canon),g.orbit_key(links))
            for phi in product(S3_ELEMENTS,repeat=2):
                transformed=g.transform(links,phi)
                self.assertEqual(g.orbit_key(transformed),g.orbit_key(links))
                self.assertTrue(g.orbit_equal(transformed,links))
        self.assertTrue(all(g.orbit_equal(x,x) for x in all_links))

    def test_separate_wilson_traces_collapse_nonabelian_joint_classes(self):
        g=S3GaugeGraph(('u','v'),(('u','v'),('u','v'),('u','v')))
        a=(1,0,2)
        b=(0,2,1)
        left=(S3_ID,a,a)
        right=(S3_ID,a,b)
        self.assertEqual(tuple(trace_s3(x) for x in g.chords(left)),(1,1))
        self.assertEqual(tuple(trace_s3(x) for x in g.chords(right)),(1,1))
        self.assertFalse(g.orbit_equal(left,right))
        self.assertEqual((trace_s3(compose_s3(a,a)),trace_s3(compose_s3(a,b))),(3,0))
        self.assertEqual(inverse_s3(compose_s3(a,b)),compose_s3(inverse_s3(b),inverse_s3(a)))
        for h in S3_ELEMENTS:
            self.assertEqual(trace_s3(conjugate_s3(h,a)),trace_s3(a))

    def test_nonabelian_subdivision_naturality_all_7776_exact_cases(self):
        for a,b,gu,gm,gv in product(S3_ELEMENTS,repeat=5):
            square=s3_subdivision_square(a,b,gu,gm,gv)
            self.assertTrue(square['commutes'])
            self.assertEqual(square['through_refinement'],square['transported_coarse'])
            self.assertEqual(square['coarse'],compose_s3(a,b))
        a=(1,0,2);b=(0,2,1)
        self.assertNotEqual(compose_s3(a,b),compose_s3(b,a))
        with self.assertRaises(GaugeOracleError):
            s3_subdivision_square(a,b,S3_ID,(0,0,1),S3_ID)

    def test_nonabelian_malformed_source_and_witness_rejected(self):
        with self.assertRaises(GaugeOracleError): S3GaugeGraph(('u','v'),())
        g=S3GaugeGraph(('u','v'),(('u','v'),('u','v')))
        with self.assertRaises(GaugeOracleError): g.orbit_key((S3_ID,))
        with self.assertRaises(GaugeOracleError): g.transform((S3_ID,S3_ID),(S3_ID,))
        with self.assertRaises(GaugeOracleError): g.transform((S3_ID,S3_ID),((0,0,1),S3_ID))


class TruthTransportAndGapTest(unittest.TestCase):
    def test_finite_reflection_like_kernel_is_psd_iff_characters_nonnegative(self):
        self.assertEqual(two_state_reflection_eigenvalues(Q(2),Q(1)),(Q(3),Q(1)))
        self.assertEqual(two_state_reflection_eigenvalues(Q(1),Q(2)),(Q(3),Q(-1)))
        self.assertEqual(two_state_reflection_eigenvalues(Q(1),Q(-2)),(Q(-1),Q(3)))
        for w0 in range(-2,4):
            for w1 in range(-3,4):
                e=two_state_reflection_eigenvalues(Q(w0),Q(w1))
                self.assertEqual(min(e)>=0, w0>=abs(w1))

    def test_positive_lattice_eigenvalues_do_not_imply_continuum_gap(self):
        seq=[]
        for n in (2,4,8,16,32,64):
            a=Q(1,n)
            ratio=transfer_spectral_ratio(a,'quadratic')
            self.assertTrue(0<ratio<1)
            self.assertLessEqual(gap_lower_from_ratio(a,ratio),quadratic_mass_upper(a))
            seq.append(quadratic_mass_upper(a))
        self.assertEqual(seq,sorted(seq,reverse=True))
        self.assertLess(seq[-1],Q(1,30))

    def test_distinct_physical_gap_scalings_with_identical_finite_cutoffs(self):
        K=9
        for n in range(2,K+1):
            left,right=finite_cutoff_twins(n,K)
            self.assertEqual(left,right)
        for n in (10,16,64,1024):
            left,right=finite_cutoff_twins(n,K)
            self.assertNotEqual(left,right)
            a=Q(1,n)
            # For the second tail, m(a) >= (1-ratio)/a >= 2/5.
            self.assertGreaterEqual(gap_lower_from_ratio(a,right),Q(2,5))
        # First tail has an analytic upper bound tending to zero.
        self.assertLess(quadratic_mass_upper(Q(1,1000)),Q(1,400))

    def test_nonabelian_individual_wilson_traces_incomplete(self):
        r=nonabelian_trace_counterexample()
        self.assertEqual((r['trace_first'],r['trace_second_control'],r['trace_second_other']),(1,1,1))
        self.assertEqual((r['trace_product_control'],r['trace_product_other']),(3,0))
        self.assertEqual(trace_s3(compose_s3((1,0,2),(1,0,2))),3)

    def test_malformed_ratio_and_nonabelian_inputs_rejected(self):
        with self.assertRaises(GaugeOracleError): transfer_spectral_ratio(Q(1),'quadratic')
        with self.assertRaises(GaugeOracleError): transfer_spectral_ratio(Q(1,2),'invalid')
        with self.assertRaises(GaugeOracleError): transfer_spectral_ratio(0.2,'linear')
        with self.assertRaises(GaugeOracleError): gap_lower_from_ratio(Q(1),Q(0))
        with self.assertRaises(GaugeOracleError): quadratic_mass_upper(Q(1))
        with self.assertRaises(GaugeOracleError): two_state_reflection_eigenvalues(1,Q(1))
        with self.assertRaises(GaugeOracleError): compose_s3((0,1,1),(0,1,2))
        with self.assertRaises(GaugeOracleError): trace_s3((0,2,2))
        with self.assertRaises(GaugeOracleError): trace_s3((True,0,2))

if __name__ == '__main__':
    unittest.main()
