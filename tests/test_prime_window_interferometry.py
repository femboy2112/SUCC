"""Research-only tests: exact source, prime windows, honest finite numerics."""
import cmath
import math
import unittest
import sys
from pathlib import Path
RESEARCH=Path(__file__).resolve().parents[1]/'research/2026-11-01/prime_window_interferometry'
sys.path.insert(0,str(RESEARCH))
from fractions import Fraction as F
from prime_window import (source,combined_source,edge,states_through,prime,primes5,
    window,order16,period_split,phase,split_window,original_window,kernel,
    energy_direct,energy_kernel)
from interval import prove_window,certify_both_directions

class PrimeWindowResearch(unittest.TestCase):
    def test_four_poles_and_three_edges(self):
        self.assertEqual(source(1), F(47,15))
        for n in range(1,175):
            self.assertEqual(source(n),combined_source(n))
            self.assertEqual(source(n),2*edge(n,3)+edge(n,4)+edge(n,5))

    def test_window_exact_dilation(self):
        for p in primes5(1500):
            a,b,L=window(p);k=(p-5)//8
            self.assertEqual((a,b,L),(k+1,4*k+2,3*k+2))
            self.assertEqual((a,b),((p+3)//8,(p-1)//2))
            self.assertEqual(L,b-a+1)

    def test_period_odd_half_period(self):
        for p in primes5(2000):
            d,t,full,remainder=period_split(p)
            self.assertEqual(pow(16,d,p),1)
            self.assertTrue(all(pow(16,j,p)!=1 for j in range(1,d)))
            self.assertEqual(t%2,1)
            self.assertEqual(remainder,(d+1)//2)
            self.assertEqual(full*d+remainder,window(p)[2])
        self.assertEqual(period_split(13),(3,1,1,2))
        self.assertEqual(period_split(109),(9,3,4,5))
        self.assertEqual(period_split(397),(11,9,13,6))

    def test_source_convolution_independent(self):
        us=states_through(60)
        for N,u in enumerate(us):
            self.assertEqual(u,sum((16**(N-j)*combined_source(j) for j in range(1,N+1)),F(0)))

    def test_unique_newborn_p_primary_and_edge4(self):
        us=states_through(265)
        for p in primes5(509):
            a,b,L=window(p)
            self.assertLess(b,len(us))
            for n in range(a,b+1):
                v=us[n]+F(16**(n-a),p)
                self.assertNotEqual(v.denominator%p,0)
                self.assertEqual((p*us[n]).denominator%p!=0, True)
                self.assertEqual((p*us[n]).numerator*pow((p*us[n]).denominator,-1,p)%p,
                                 (-pow(16,n-a,p))%p)
            # Source at first birth has -1/p only in f_4.
            self.assertEqual((p*(edge(a,4)+F(1,p))).denominator%p!=0,True)
            self.assertEqual((p*edge(a,3)).denominator%p!=0,True)
            self.assertEqual((p*edge(a,5)).denominator%p!=0,True)

    def test_complex_identity_numerical_only(self):
        us=states_through(265)
        for p in (13,29,37,53,109,269,373,397,509):
            for h in (1,3,5):
                prim,cof,joint=split_window(p,us,h)
                direct=original_window(p,us,h)
                self.assertLess(abs(direct-joint),1e-9)
                self.assertLessEqual(abs(prim),window(p)[2]+1e-9)
                self.assertLessEqual(abs(cof),window(p)[2]+1e-9)

    def test_kernel_exact_gram(self):
        X=61;us=states_through(32)
        z=[1+0j]+[phase(u,3) for u in us[1:]]
        direct=energy_direct(X,z)
        gram=energy_kernel(X,z)
        self.assertLess(abs(direct-gram),1e-8)
        self.assertLess(abs(gram.imag),1e-8)
        self.assertGreaterEqual(gram.real,-1e-8)
        for n in range(1,25):
            for m in range(1,25):
                brute=sum(window(p)[0]<=n<=window(p)[1] and
                          window(p)[0]<=m<=window(p)[1] for p in primes5(X))
                self.assertEqual(kernel(X,n,m),brute)

    def test_coherent_and_alternating_controls(self):
        X=253;ps=primes5(X);N=(X-1)//2
        coherent=[1+0j]*(N+1)
        self.assertEqual(energy_direct(X,coherent),sum(window(p)[2]**2 for p in ps))
        alt=[1+0j]+[(-1)**n+0j for n in range(1,N+1)]
        self.assertLessEqual(energy_direct(X,alt),len(ps))

    def test_shared_core_and_nonindependent_prime_copies(self):
        p,q=269,373
        a=max(window(p)[0],window(q)[0]);b=min(window(p)[1],window(q)[1])
        self.assertGreater(b-a,0)
        us=states_through(b)
        for n in range(a,b+1):
            xp=-F(16**(n-window(p)[0]),p)
            xq=-F(16**(n-window(q)[0]),q)
            vp=us[n]-xp;vq=us[n]-xq
            self.assertEqual(xp+vp,xq+vq)
            self.assertNotEqual(vp.denominator%p,0)
            self.assertNotEqual(vq.denominator%q,0)

    def test_p_free_cofactor_fake_can_rephase(self):
        p=397;a,b,L=window(p);q=p+1
        for j in range(L):
            t=pow(16,j,p)
            k=(2*t*q+p)//(2*p)
            v=F(k,q)
            self.assertTrue(v.denominator%p)
            self.assertLessEqual(abs(v-F(t,p)),F(1,2*q))

    def test_exact_anti_monotonicity_both_directions(self):
        rows=certify_both_directions()
        self.assertEqual([(r['prime'],r['h'],r['strict_order']) for r in rows],
                         [(373,1,'joint_larger'),(397,3,'joint_smaller')])
        self.assertTrue(all(F(r['certified_gap_lower'])>0 for r in rows))

    def test_invalid_domains(self):
        for p in (2,5,9,17,257):
            with self.assertRaises(ValueError):window(p)
        for n in (-1,0):
            with self.assertRaises(ValueError):source(n)
        with self.assertRaises(ValueError):states_through(-1)

    def test_rational_interval_holdout_receipts(self):
        # 15 exact rational-interval finite bounds, not asymptotics.
        expected={269:(True,False,False),373:(False,False,True),
                  397:(False,False,True),509:(False,False,True),997:(True,True,True)}
        for p in expected:
            rows=prove_window(p)
            self.assertEqual(tuple(row['under_1_16'] for row in rows),expected[p])
            self.assertTrue(all(row['upper_l1'] for row in rows))
            self.assertEqual([row['h'] for row in rows],[1,3,5])
            self.assertTrue(all(F(row['upper_l1'])<F(1,4) for row in rows))
            if p!=397:self.assertTrue(all(row['under_1_8'] for row in rows))

if __name__=='__main__':unittest.main()
