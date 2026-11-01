"""Exact original-source entropy/finite observer tests; no asymptotic proof claimed."""
import importlib.util
import pathlib
import sys
import unittest
from collections import Counter
from fractions import Fraction as F
from math import log, isclose, cos, sin, pi

ROOT=pathlib.Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'carrier_relative_entropy'

def load_unique(short,filename):
    name='succ_entropy_'+short+'_'+str(abs(hash(str(ROOT))))
    spec=importlib.util.spec_from_file_location(name,ROOT/filename)
    v=importlib.util.module_from_spec(spec)
    sys.modules[name]=v
    spec.loader.exec_module(v)
    return v

m=load_unique('implementation','carrier_entropy.py')
o=load_unique('oracle','independent_oracle.py')

class TestCarrierSource(unittest.TestCase):
    def test_source_first_two(self):
        self.assertEqual(m.source(1),F(47,15))
        self.assertEqual(m.source(2),F(106,819))

    def test_source_exact_holds(self):
        for n in range(1,80):self.assertEqual(m.source(n),m.source_combined(n))

    def test_positive_decrease(self):
        for n in range(1,80):self.assertGreater(m.source(n),m.source(n+1))

    def test_literally_selected_zero(self):
        self.assertEqual(m.selected_states(0),())
        self.assertEqual(m.selected_states(1),(F(47,15),))

    def test_recurrence_against_convolution(self):
        for N in (1,2,3,5,12,24):self.assertEqual(m.selected_states(N),o.convolution_states(N))

    def test_all_odd_denominators(self):
        for a in m.selected_states(48):self.assertEqual(a.denominator%2,1)

    def test_source_stationarity_exact(self):
        for n in (1,2,10,64):
            self.assertEqual(m.source_stationarity_budget(n), (2+o.shifted_successor_error_sum(n))/n)

    def test_source_stationarity_global(self):
        for n in (1,2,32,256):
            self.assertLess(m.source_stationarity_budget(n),F(2, n)+F(15,32*n))

    def test_positive_rational_mutant(self):
        for n in (1,2,5,12):
            prefix=sum((m.source(j)/16**j for j in range(1,n+1)),F(0))
            self.assertEqual(m.rational_completed_counterfeit(n), prefix+m.source(n)/(31*16**n))
            self.assertIsInstance(m.rational_completed_counterfeit(n),F)

    def test_mutant_same_finite_states(self):
        for n in (1,5,14):
            real=m.selected_states(n)
            mutant=[];x=F(0)
            for j in range(1,n+1):
                x=16*x+m.source(j);mutant.append(x)
            self.assertEqual(real,tuple(mutant))

class TestFiniteObserver(unittest.TestCase):
    def test_cell_rational_exact(self):
        self.assertEqual(m.cell(F(47,15),1),2)
        self.assertEqual(m.cell(F(1,5),1),3)
        self.assertEqual(m.cell(F(-1,5),1),12)
        self.assertEqual(m.cell(F(0),3),0)

    def test_cells_versus_distinct_oracle(self):
        for x in m.selected_states(71):
            for k in (0,1,2,3):self.assertEqual(m.cell(x,k),o.residue_cell(x,k))

    def test_refinement_exact(self):
        xs=m.selected_states(128)
        for k in (1,2,3):
            self.assertTrue(m.consistent_refinement(m.counts(xs,k+1),k+1,m.counts(xs,k)))
            self.assertTrue(o.brute_prefix_consistency(xs,k))

    def test_wrong_refinement_rejected(self):
        x=m.selected_states(64)
        c2=m.counts(x,2)
        c1=m.counts(x,1)
        c1[0]=c1.get(0,0)+1
        self.assertFalse(m.consistent_refinement(c2,2,c1))

    def test_collision_nonnegative(self):
        xs=m.selected_states(128)
        for k in (0,1,2,3):self.assertGreaterEqual(m.collision_defect_from_counts(m.counts(xs,k),len(xs),k),0)

    def test_collision_signed_pair_oracle(self):
        for N,k in ((4,1),(16,1),(32,2),(48,2)):
            xs=m.selected_states(N);c=m.counts(xs,k)
            self.assertEqual(m.signed_collision_excess(c,N,k),o.pair_excess(xs,k))

    def test_collision_decomposition(self):
        for N in (16,32,64):
            xs=m.selected_states(N)
            for k in (1,2,3):
                q,d,off=m.collision_decomposition(m.counts(xs,k),N,k)
                self.assertEqual(q,d+off)

    def test_exact_selected_receipts(self):
        self.assertEqual(m.collision_defect_from_counts(m.counts(m.selected_states(128),1),128,1),F(47,512))
        self.assertEqual(m.collision_defect_from_counts(m.counts(m.selected_states(256),1),256,1),F(69,2048))
        self.assertEqual(m.collision_defect_from_counts(m.counts(m.selected_states(256),2),256,2),F(121,128))
        self.assertEqual(m.collision_defect_from_counts(m.counts(m.selected_states(512),2),512,2),F(27,64))

    def test_kl_entropy_telescope(self):
        xs=m.selected_states(128);n=len(xs)
        increments=[];prev={0:n}
        for k in (1,2,3):
            c=m.counts(xs,k)
            val=m.conditional_defect(prev,c,n,k-1)
            self.assertGreaterEqual(val,-1e-12)
            increments.append(val)
            self.assertTrue(isclose(sum(increments),m.kl_from_counts(c,n,k),abs_tol=1e-11))
            prev=c

    def test_entropy_nonnegative(self):
        xs=m.selected_states(64)
        for k in (1,2,3):
            c=m.counts(xs,k)
            self.assertGreaterEqual(m.kl_from_counts(c,len(xs),k),-1e-12)
            self.assertLessEqual(m.entropy_from_counts(c,len(xs)),k*log(16)+1e-12)

    def test_empirical_profile_contains_exact_fractions(self):
        p=m.empirical_profile(m.selected_states(32),3)
        self.assertEqual(p['profile'][0]['collision_defect'],'21/32')
        self.assertEqual(len(p['profile']),3)

    def test_resolution_collision_obstruction_exact(self):
        # At M>N the diagonal imposes an unavoidable positive chi-square gap.
        for N,k in ((32,2),(128,3),(256,3)):
            c=m.counts(m.selected_states(N),k)
            q=m.collision_defect_from_counts(c,N,k)
            self.assertGreaterEqual(q,F(16**k,N)-1)
            self.assertGreater(m.exact_resolution_ceiling(N,k),1)

    def test_coherent_completed_same_forcing_seed(self):
        # For completed q=1/5, U_n(q)=16**n/5-T_n.
        # n>=2 has x_n in (3/16,1/4), since T_n<1/(64n^2).
        # The initial seed is irrational and NOT in the original finite register.
        for n in (2,3,4,10,256):
            lower=F(1,5)-F(1,64*n*n)
            self.assertGreater(lower,F(3,16))
            self.assertLess(F(1,5),F(1,4))
        self.assertEqual(m.cell(F(1,5),1),3)

    def test_rigorous_weyl_upper_on_sample(self):
        for N,k,h in ((128,1,1),(256,2,1),(512,2,3),(512,3,3)):
            xs=m.selected_states(N)
            z=sum((complex(cos(2*pi*h*float(x%1)),sin(2*pi*h*float(x%1))) for x in xs),0j)/N
            bound=m.collision_weyl_bound(m.counts(xs,k),N,k,h)
            self.assertLessEqual(abs(z),bound+1e-10)

    def test_certified_rational_fourier_ceiling(self):
        from fractions import Fraction as F
        for N,k,h in ((128,1,1),(256,2,3),(512,3,17)):
            c=m.counts(m.selected_states(N),k)
            q=m.collision_defect_from_counts(c,N,k)
            bound=m.certified_weyl_ceiling(c,N,k,h)
            self.assertIsInstance(bound,F)
            self.assertGreaterEqual((bound-F(44*h,7*16**k))**2,q)
        self.assertEqual(m.rational_sqrt_upper(F(9,16)),F(3,4))
        with self.assertRaises(ValueError):m.certified_weyl_ceiling({0:1},1,1,16)

    def test_trivial_harmonic_rejected(self):
        with self.assertRaises(ValueError):m.collision_weyl_bound({0:3},3,1,16)

    def test_resolution_ceiling(self):
        self.assertEqual(m.exact_resolution_ceiling(128,3),F(4096,128))
        self.assertEqual(m.exact_resolution_ceiling(256,2),F(1))

    def test_wrong_input_rejected(self):
        for f in [lambda:m.selected_states(-1),lambda:m.source(0),
                  lambda:m.cell(0,True),lambda:m.cell(0,1,1),
                  lambda:m.collision_defect_from_counts({0:3},2,1),
                  lambda:m.conditional_path_surprisal(-1)]:
            with self.assertRaises(ValueError):f()

class TestAdversarialInformation(unittest.TestCase):
    def test_debruijn_exact_all_two_blocks(self):
        cy=m.debruijn_cycle(16,2)
        self.assertEqual(len(cy),256)
        self.assertEqual(len(set(cy)),16)
        self.assertEqual(set(m.cyclic_word_counts(cy,2).values()),{1})

    def test_debruijn_independent_word_count(self):
        cy=m.debruijn_cycle(16,2)
        for k in (1,2,3):
            self.assertEqual(m.cyclic_word_counts(cy,k),o.cyclic_window_count(cy,k))

    def test_maximal_finite_entropy_but_nonnormal(self):
        cy=m.debruijn_cycle(16,2)
        c2=m.cyclic_word_counts(cy,2)
        c3=m.cyclic_word_counts(cy,3)
        self.assertEqual(m.collision_defect_from_counts(c2,256,2),F(0))
        self.assertEqual(m.collision_defect_from_counts(c3,256,3),F(15))
        self.assertTrue(isclose(m.entropy_from_counts(c2,256),2*log(16)))
        self.assertTrue(isclose(m.conditional_entropy_increment(c2,c3,256,2),0,abs_tol=1e-12))
        self.assertTrue(isclose(m.conditional_defect(c2,c3,256,2),log(16)))

    def test_all_finite_debruijn_orders_are_false_positives(self):
        for depth in (1,2,3):
            cycle=m.debruijn_cycle(16,depth)
            N=len(cycle)
            c=m.cyclic_word_counts(cycle,depth)
            c_next=m.cyclic_word_counts(cycle,depth+1)
            self.assertEqual(len(c),16**depth)
            self.assertEqual(set(c.values()),{1})
            self.assertEqual(m.collision_defect_from_counts(c,N,depth),F(0))
            self.assertEqual(m.collision_defect_from_counts(c_next,N,depth+1),F(15))
            self.assertTrue(isclose(m.conditional_defect(c,c_next,N,depth),log(16)))

    def test_debruijn_prior_information_false_positive(self):
        cy=m.debruijn_cycle(16,2)
        zeros=(0,)*len(cy)
        # Identical surprise under a declared uniform prior, unlike realized frequency distributions.
        self.assertEqual(m.conditional_path_surprisal(2),m.conditional_path_surprisal(2))
        self.assertEqual(len(m.cyclic_word_counts(zeros,2)),1)
        self.assertEqual(len(m.cyclic_word_counts(cy,2)),256)

    def test_debruijn_conditional_deficit_persists_over_cycles(self):
        cy=m.debruijn_cycle(16,2)
        for rep in (1,2,5):
            c2={w:v*rep for w,v in m.cyclic_word_counts(cy,2).items()}
            c3={w:v*rep for w,v in m.cyclic_word_counts(cy,3).items()}
            self.assertEqual(m.collision_defect_from_counts(c2,256*rep,2),F(0))
            self.assertEqual(m.collision_defect_from_counts(c3,256*rep,3),F(15))

    def test_fixed_uniform_branch_count_for_all_zero(self):
        zeros=(F(0),)*64
        uniform=m.conditional_path_surprisal(3)
        self.assertTrue(isclose(uniform,3*log(16)))
        self.assertTrue(isclose(m.kl_from_counts(m.counts(zeros,3),64,3),3*log(16)))

    def test_coherence_without_normality(self):
        zeros=(F(0),)*64
        for k in (1,2,3):
            self.assertTrue(m.consistent_refinement(m.counts(zeros,k+1),k+1,m.counts(zeros,k)))
        self.assertEqual(m.source_stationarity_budget(100,0,0),F(0))

if __name__=='__main__':unittest.main()
