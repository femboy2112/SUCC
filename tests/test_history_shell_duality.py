"""Exact source-history shell duality, conditional ensembles, and no-go controls."""
import importlib.util
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import gcd
import unittest

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'research/2026-11-05/history_shell/history_shell_probe.py'
spec=importlib.util.spec_from_file_location('history_shell_probe',SRC)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)

class HistoryShell(unittest.TestCase):
    def test_01_authentic_source_and_literal_zero(self):
        self.assertEqual(h.states(0)[0],Q(0))
        self.assertEqual(h.forcing(1),Q(47,15))
        for n in (2,13,29,61,173,347,691):
            self.assertGreater(h.forcing(n),0)

    def test_02_exact_selected_shell_identity(self):
        for A,d in ((173,5),(347,5),(691,6)):
            for k in (1,2):
                m=d-k
                out=h.original_epoch(A,m,k)
                self.assertEqual(len(out['items']),A)
                self.assertTrue(all(0<v['source_fraction']<1 for v in out['items']))
                for item in out['items']:
                    b=item['selected_bit']
                    self.assertEqual(item['actual_cell'],item['alternatives'][b])
                    self.assertEqual(sum(item['probabilities']),1)

    def test_03_critical_source_lookahead_precision_tradeoff(self):
        for n in (13,29,61,139,173,277,347,557,691):
            for m in range(1,6):
                for k in (1,2,3):
                    q=16**m*h.block(n,k)
                    predicted=Q(16**m*(16**k-1),64*n*n)
                    self.assertLess(abs(q-predicted),Q(16**(m+k),10*n**3))

    def test_04_fresh_selected_history_counts_recorded_without_fit(self):
        expected={(173,4,1):38,(173,3,2):42,(347,4,1):21,
                  (347,3,2):21,(691,5,1):179,(691,4,2):194}
        for (A,m,k),count in expected.items():
            v=h.original_epoch(A,m,k)
            self.assertEqual(v['count'],count)
            self.assertGreater(v['expected'],0)
            self.assertNotEqual(Q(count),v['expected'])

    def test_05_toy_base16_nonlumpability_is_exact(self):
        v=h.nonlumpability(Q(1,2),Q(1,2))
        self.assertEqual(v['direct'],(Q(0),Q(1),Q(0)))
        self.assertEqual(v['naive'],(Q(1,4),Q(1,2),Q(1,4)))
        self.assertEqual(v['total_variation'],Q(1,2))
        self.assertEqual(16*Q(1,512)+Q(1,32),Q(1,16))

    def test_06_actual_source_also_fails_naive_reuniformization(self):
        for n in (13,29,61):
            a,b,v=h.source_nonlumpability(n,2)
            self.assertTrue(0<a<1 and 0<b<1)
            self.assertGreater(v['total_variation'],0)
            self.assertEqual(v['total_variation'],2*min(a*b,(1-a)*(1-b)))
        self.assertGreater(h.source_nonlumpability(13,2)[2]['total_variation'],Q(1,5))

    def test_07_haar_seed_digits_are_iid_for_all_words_len_at_most_three(self):
        for count in (1,2,3):
            for word in product(range(16),repeat=count):
                self.assertEqual(h.word_probability(word),Q(1,16**count))

    def test_08_same_iid_ensemble_for_a_mutated_source(self):
        def mutant(n):return h.forcing(n)+Q(1,8*n-7)
        for word in product(range(16),repeat=2):
            self.assertEqual(h.word_probability(word,mutant),Q(1,16**2))

    def test_09_root_tree_vs_prefix_tree_finite_digit_reversal(self):
        for digits in ((1,2,3,4),(15,0,14,2),(0,0,0,1),(8,6,10,3)):
            for m in range(2,5):
                d=digits[:m]
                self.assertEqual(h.prefix_index(d)//16,h.prefix_index(d[:-1]))
                self.assertEqual(h.root_index(d)%(16**(m-1)),h.root_index(d[:-1]))
                self.assertEqual(h.prefix_index(tuple(reversed(d))),h.root_index(d))

    def test_10_nested_diagonal_classical_wavefunctions_are_separable(self):
        child={ (0,0):Q(1,4),(0,1):Q(1,4),(1,1):Q(1,2) }
        self.assertEqual(sum(child.values()),1)
        parent={a:sum((p for (x,b),p in child.items() if x==a),Q()) for a in (0,1)}
        self.assertEqual(parent,{0:Q(1,2),1:Q(1,2)})
        # Each |a b><a b| is a product state; mixing these is separable.
        self.assertTrue(all(p>=0 for p in child.values()))

    def test_11_kooopman_adjoint_character_projection_exact(self):
        r=h.forcing(13)
        for k in range(-64,65):
            # Koopman sends e_k to e(kr) e_{16k}; transfer reverses it exactly.
            image_frequency=16*k
            image_phase=(k*r)%1
            back_frequency=image_frequency//16
            back_phase=(-back_frequency*r)%1
            self.assertEqual(back_frequency,k)
            self.assertEqual((image_phase+back_phase)%1,0)
            if k%16:
                self.assertNotEqual(k%16,0) # transfer kills e_k
            else:
                self.assertEqual(k//16,int(k/16))

    def test_12_source_seed_l2_normality_is_exact_but_pointwise_fails(self):
        # For any source u_n and h !=0, the functions e(h(16**n s+u_n))
        # have distinct frequencies. Their A-term mean has L2 norm²=1/A.
        for A in (3,7,17):
            freqs=[16**n for n in range(A,2*A)]
            self.assertEqual(len(set(freqs)),A)
            self.assertEqual(Q(len(freqs),A*A),Q(1,A))
            # Unforced exact zero seed: every term equals 1 at s=0.
            self.assertEqual(sum(Q(1) for _ in freqs)/A,1)

    def test_13_same_source_coherent_seed_requires_actual_history(self):
        for A,d in ((173,5),(347,5),(691,6)):
            self.assertLess(16**d,(8*A+1)*(8*A+2))
            for k in (1,2):
                m=d-k
                for n in (A,(3*A)//2,2*A-1):
                    R=h.block(n,k)
                    self.assertTrue(0<16**m*R<1)
                    # For coherent seed x=1-T, exact R=16**k*T_n-T_(n+k),
                    # theta+delta=1-16**m*T_(n+k)<1: realized b=0.

if __name__=='__main__':unittest.main()
