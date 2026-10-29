"""Exact hostile controls for SUCC's direction-weighted carry observers."""
import math
import sys
import unittest
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research/2026-10-29/orthogonal_entropy_carry'))
import orthogonal_carry as oc

class DirectionalCarryTests(unittest.TestCase):
    def test_original_four_poles(self):
        self.assertEqual(oc.authentic_r(1),Q(47,15))
        self.assertEqual(oc.authentic_r(2),Q(106,819))
        self.assertEqual(oc.authentic_r(3),Q(829,19635))

    def test_rational_source_upper_bound(self):
        for n in range(3,256):
            self.assertGreater(oc.source_upper_gap(n),0)

    def test_translated_positive_integer_polynomial(self):
        for k in range(0,256):
            n=k+3
            positive=272*k**4+2418*k**3+7754*k**2+10408*k+4713
            self.assertEqual(oc.source_bound_polynomial(n),positive)

    def test_strict_positive_r(self):
        for n in range(1,256):
            self.assertGreater(oc.authentic_r(n),0)

    def test_strict_decrease_r(self):
        for n in range(2,256):
            self.assertLess(oc.authentic_r(n+1),oc.authentic_r(n))

    def test_16power_zero_run(self):
        for n in range(3,300):
            t=oc.zero_run(n)
            self.assertLessEqual(16**t,n*n)
            self.assertGreater(16**(t+1),n*n)

    def test_explicit_first_boundary_corrections(self):
        for n in (3,4,8,16,31,64,128):
            for c in range(1,17):
                r=oc.authentic_r(n)
                before=Q(c,16)-r/32
                x,k,d,mis=oc.step(before,n)
                self.assertTrue(mis)
                self.assertEqual(k,c)
                self.assertEqual(d,c-1)
                self.assertEqual(x,r/2)

    def test_all_sixteen_corrections_force_zeros(self):
        for n in range(3,151):
            for c in range(1,17):
                _,carries=oc.forced_run_from_correction(n,c)
                self.assertEqual(carries,[0]*oc.zero_run(n))

    def test_no_new_mismatch_inside_run(self):
        for n in range(3,151):
            for c in (1,6,15,16):
                r=oc.authentic_r(n)
                x=Q(c,16)-r/32
                x,k,d,mis=oc.step(x,n)
                self.assertTrue(mis)
                for j in range(1,oc.zero_run(n)+1):
                    x,k,d,mis=oc.step(x,n+j)
                    self.assertEqual((k,d,mis),(0,0,False))

    def test_no_forced_correction_downwards(self):
        seeds=[Q(0),Q(1,15),Q(1,7),Q(123,256),Q(15,16),Q(-5,16)]
        for seed in seeds:
            for n,(c,d,mis) in enumerate(oc.trace(seed,128),start=1):
                if n>=2:
                    self.assertIn(c-d,(0,1))

    def test_normalized_mod16_repair(self):
        for seed in (Q(0),Q(1,7),Q(15,16)):
            for c,d,mis in oc.trace(seed,256)[1:]:
                self.assertEqual((c%16!=d),mis)

    def test_allseed_counting_bound(self):
        for N in (3,4,8,16,64,128,256,512):
            for seed in (Q(0),Q(1,7),Q(1,15),Q(23423,65537)):
                c=sum(mis for _,_,mis in oc.trace(seed,N))
                self.assertLessEqual(c,oc.mismatch_bound(N))

    def test_counting_bound_all_possible_M(self):
        for N in (4,64,256):
            for M in range(3,N+1):
                self.assertLessEqual(oc.mismatch_bound(N,M),N)

    def test_tv_block_coupling_bound(self):
        for seed in (Q(0),Q(1,7),Q(15,16)):
            t=oc.trace(seed,220)
            corrected=[c%16 for c,d,m in t]
            bare=[d for c,d,m in t]
            E=sum(m for c,d,m in t)
            for k in (1,2,3,4):
                p=oc.empirical_words(corrected,k)
                q=oc.empirical_words(bare,k)
                self.assertLessEqual(oc.total_variation(p,q),Q(min(220-k+1,k*E),220-k+1))

    def test_q6_primitive_marginal_transport(self):
        for seed in (Q(0),Q(7,13)):
            t=oc.trace(seed,256)
            corrected=sum(oc.primitive_digit(c%16) for c,d,m in t)
            bare=sum(oc.primitive_digit(d) for c,d,m in t)
            self.assertLessEqual(abs(corrected-bare),sum(m for c,d,m in t))

    def test_source_neutral_zero_seed(self):
        p=oc.trace(Q(0),4)
        self.assertEqual([c for c,d,m in p][:2],[3,2])

    def test_positive_local_thermodynamic_pressure(self):
        t=oc.trace(Q(0),512)
        C=[c%16 for c,d,m in t];D=[d for c,d,m in t]
        E=sum(m for c,d,m in t)
        for k in (1,2,3):
            p=oc.empirical_words(C,k);q=oc.empirical_words(D,k)
            f={word: (1.2 if oc.primitive_digit(word[0]) else -1.2) for word in p.keys()|q.keys()}
            diff=abs(oc.local_pressure(p,f)-oc.local_pressure(q,f))
            upper=oc.pressure_difference_bound(float(oc.total_variation(p,q)),1.2)
            self.assertLessEqual(diff,upper+1e-12)
            self.assertLessEqual(float(oc.total_variation(p,q)),k*E/(512-k+1))

    def test_entropy_continuity_block_bound(self):
        t=oc.trace(Q(0),512)
        C=[c%16 for c,d,m in t];D=[d for c,d,m in t]
        for k in (1,2,3):
            p=oc.empirical_words(C,k);q=oc.empirical_words(D,k)
            delta=float(oc.total_variation(p,q))
            self.assertLessEqual(abs(oc.shannon(p)-oc.shannon(q)),oc.entropy_continuity_bound(k,delta)+1e-10)

    def test_walsh_orthogonal_exact(self):
        for j in range(16):
            for k in range(16):
                val=sum(oc.walsh(d,j)*oc.walsh(d,k) for d in range(16))
                self.assertEqual(val,16 if j==k else 0)

    def test_walsh_chi2_equality(self):
        p=oc.empirical_words([c%16 for c,d,m in oc.trace(Q(0),256)],1)
        lhs=oc.chi2_walsh(p)
        rhs=sum((16*(p.get((d,),Q())-Q(1,16))**2 for d in range(16)),Q())
        self.assertEqual(lhs,rhs)

    def test_full_fourbit_interaction_countermodel(self):
        # Classical parity obstruction, already recognized by SUCC PR #271.
        even=[d for d in range(16) if d.bit_count()%2==0]
        p={(d,):Q(1,8) for d in even}
        a=oc.walsh_coefficients(p)
        self.assertEqual(a[0],1)
        self.assertEqual(a[1:15],[Q(0)]*14)
        self.assertEqual(a[15],1)
        self.assertEqual(oc.chi2_walsh(p),1)
        self.assertAlmostEqual(oc.entropy_deficit(p,1),math.log(2))

    def test_walsh_stability_under_correction(self):
        t=oc.trace(Q(0),300)
        p=oc.empirical_words([c%16 for c,d,m in t],1)
        q=oc.empirical_words([d for c,d,m in t],1)
        E=sum(m for c,d,m in t)
        for a,b in zip(oc.walsh_coefficients(p),oc.walsh_coefficients(q)):
            self.assertLessEqual(abs(a-b),Q(2*E,len(t)))

    def test_debruijn_two_symbol_word_normality_countermodel(self):
        word=oc.debruijn16(2)
        self.assertEqual(len(word),256)
        for k in (1,2):
            p=oc.circular_words(word,k)
            self.assertEqual(len(p),16**k)
            self.assertEqual(set(p.values()),{Q(1,16**k)})
        self.assertLess(len(oc.circular_words(word,3)),16**3)

    def test_stationary_forward_backward_equal_even_nonuniform(self):
        a=oc.debruijn16(2)
        b=[0]*128+[1]*128
        for w in (a,b,[0,1,2]*64):
            for k in (1,2,3):
                f,g=oc.stationary_forward_backward_entropy(w,k)
                self.assertEqual(f,g)

    def test_directional_cycle_positive_entropy_production(self):
        p_forward=Q(3,4);p_backward=Q(1,8);p_stay=Q(1,8)
        self.assertEqual(p_forward+p_backward+p_stay,1)
        # Stationary uniform 3-state circulation; both conditional H agree.
        entropy_production=float(p_forward-p_backward)*math.log(float(p_forward/p_backward))
        self.assertAlmostEqual(entropy_production,5/8*math.log(6))
        self.assertGreater(entropy_production,0)

    def test_explicit_prior_and_mutant_variation(self):
        with self.assertRaises(ValueError): oc.authentic_r(0)
        with self.assertRaises(ValueError): oc.zero_run(2)
        with self.assertRaises(ValueError): oc.mismatch_bound(2)
        with self.assertRaises(ValueError): oc.walsh(16,0)
        with self.assertRaises(ValueError): oc.debruijn16(4)
        with self.assertRaises(ValueError): oc.source_upper_gap(2)

if __name__=='__main__':
    unittest.main()
