"""Research-only exact controls for CT-01..CT-09, not a pi-normality proof.

This test imports only the isolated additive research module; no historical
source, production recurrence, or formal theorem contract is changed.
"""
import math
import random
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
    "research" / "2026-10-31" / "counterfactual_triangle"))
from counterfactual_carrier import (
    bbp_source, original_states, green_tail_bracket, pi_bracket,
    certified_hex_digits, word_and_walsh_certificate, tent_vector,
    tent_occupation, tent_defect, vector_l1, finite_tail_transport,
    triangle_refinement)

class CounterfactualCarrierTests(unittest.TestCase):
    def test_source_exact_four_poles_and_pi_enclosure(self):
        self.assertEqual(bbp_source(1),Fraction(47,15))
        for n in range(1,50):
            a = 8*n-7
            self.assertEqual(bbp_source(n),Fraction(120*n*n-89*n+16,
                (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
            self.assertEqual(bbp_source(n),Fraction(6,a*(a+3))+
                Fraction(4,a*(a+4))+Fraction(5,a*(a+5)))
        lo,hi=pi_bracket(100)
        self.assertLess(lo,Fraction(355,113))
        self.assertLess(hi,Fraction(355,113))
        self.assertEqual(certified_hex_digits(18),"243f6a8885a308d313")

    def test_selected_green_and_exact_tail_bracket(self):
        states=original_states(28)
        lo_pi,hi_pi=pi_bracket(90)
        for n,u in enumerate(states,1):
            a,b=green_tail_bracket(n,32)
            self.assertLess(a,b)
            self.assertLess(b,Fraction(1,(8*n+1)**2))
            self.assertLess(u+a,(16**(n-1))*hi_pi)
            self.assertGreater(u+b,(16**(n-1))*lo_pi)

    def test_walsh_energy_exact_parseval_and_localization(self):
        for d in ("0"*120,"01"*60,"0123456789abcdef"*9,
                  certified_hex_digits(130)):
            for depth in (1,2,3):
                x=word_and_walsh_certificate(d,depth,100)
                self.assertEqual(x['Q']-1,x['energy'])
                self.assertLessEqual(x['max_word_bias'],x['localization_upper'])
                self.assertLessEqual(x['max_current'],1)

    def test_debruijn_fixed_depth_false_positive(self):
        alphabet='0123456789abcdef'
        def debruijn(k,n):
            a=[0]*(k*n);seq=[]
            def db(t,p):
                if t>n:
                    if n%p==0:seq.extend(a[1:p+1])
                else:
                    a[t]=a[t-p];db(t+1,p)
                    for j in range(a[t-p]+1,k):
                        a[t]=j;db(t+1,t)
            db(1,1)
            return ''.join(alphabet[x] for x in seq)
        stream=debruijn(16,2)*4
        self.assertEqual(word_and_walsh_certificate(stream,1,256)['Q'],1)
        self.assertEqual(word_and_walsh_certificate(stream,2,256)['Q'],1)
        self.assertEqual(word_and_walsh_certificate(stream,3,256)['Q'],16)

    def test_tent_partition_and_exact_l1_lipschitz(self):
        rng=random.Random(1729)
        for q in (16,256):
            for _ in range(100):
                a=Fraction(rng.randrange(-10000,10000),10007)
                b=Fraction(rng.randrange(-10000,10000),10007)
                va=tent_vector(a,q);vb=tent_vector(b,q)
                self.assertEqual(sum(va.values()),1)
                aa=[va.get(j,Fraction(0)) for j in range(q)]
                bb=[vb.get(j,Fraction(0)) for j in range(q)]
                dist=abs((a-b)%1)
                dist=min(dist,1-dist)
                self.assertLessEqual(vector_l1(aa,bb),2*q*dist)
            xs=[Fraction(2*t+1,2*q) for t in range(q)]
            self.assertTrue(all(p==Fraction(1,q) for p in tent_occupation(xs,q)))
            self.assertEqual(tent_defect(xs,q),0)

    def test_source_hat_transport(self):
        for N,q in ((12,16),(50,16),(30,256)):
            t=finite_tail_transport(N,q,12)
            self.assertLessEqual(t['observed_rational'],t['certified_upper'])
            self.assertLessEqual(t['certified_upper'],t['universal_upper'])
            self.assertLess(t['missing_tail_upper'],Fraction(1,1000))
        self.assertGreater(tent_defect([Fraction(0)]*40,16),1)

    def test_nonnormal_word_bias_forces_collision_growth(self):
        for stream,k,m,N in (("0"*300,1,3,250),
                ("01"*200,1,3,250),
                (certified_hex_digits(260),1,3,250)):
            x=word_and_walsh_certificate(stream,m,N)
            p1=word_and_walsh_certificate(stream,k,N)
            eps=p1['max_word_bias']
            delta=max(Fraction(0),2*eps-Fraction(2*m,N))
            lower=Fraction(m//k,2)*delta**2
            self.assertGreaterEqual(math.log(float(x['Q']))+1e-12,float(lower))

    def test_pointwise_sixteen_fiber_refinement(self):
        rng=random.Random(404)
        for q in (16,256):
            for _ in range(60):
                x=Fraction(rng.randrange(-20000,20000),19873)
                coarse=tent_vector(16*x,q)
                fine=tent_vector(x,16*q)
                for j in range(q):
                    self.assertEqual(coarse.get(j,0),
                        sum((fine.get(j+t*q,0) for t in range(16)),Fraction(0)))

    def test_exact_source_ward_coboundary_and_bound(self):
        for N,q in ((8,16),(64,16),(256,256),(512,16),(1024,16)):
            w=triangle_refinement(N,q)
            self.assertEqual(w['observed'],
                tuple(a+b for a,b in zip(w['boundary'],w['forcing'])))
            self.assertLessEqual(w['l1'],w['source_upper'])
            self.assertLess(w['source_upper'],w['universal_upper'])

    def test_nonnormal_invariant_and_coherent_seed_controls(self):
        for q in (16,256):
            coarse=tent_vector(Fraction(0),q)
            fine=tent_vector(Fraction(0),16*q)
            self.assertEqual(sum(abs(coarse.get(j,0)-sum(
                fine.get(j+t*q,0) for t in range(16))) for j in range(q)),0)
            self.assertEqual(sum(abs(coarse.get(j,0)-Fraction(1,q))
                                 for j in range(q)),2-Fraction(2,q))
        # Changed-seed same-forcing U_n(s*)=-T_n converges to Dirac at 0.
        # Rational truncated T_n suffice for a finite adversarial measurement.
        coherent=tuple(-green_tail_bracket(n,16)[0] for n in range(1,257))
        self.assertGreater(tent_defect(coherent,16),Fraction(9,5))


class GlobalWardChargeTests(unittest.TestCase):
    def test_exact_finite_global_charge_cauchy_certificate(self):
        from counterfactual_carrier import certified_forcing_charge
        for q in (16,256):
            prior=certified_forcing_charge(128,q)
            self.assertEqual(prior['sum_coordinates'],0)
            for N in (256,512):
                nex=certified_forcing_charge(N,q)
                self.assertEqual(nex['sum_coordinates'],0)
                self.assertLessEqual(vector_l1(prior['prefix'],nex['prefix']),
                                     prior['tail_l1_upper'])
                prior=nex

if __name__=="__main__":
    unittest.main()
