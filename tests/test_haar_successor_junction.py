"""Hostile exact tests for Haar-successor two-road theorem (no normality proof)."""
import cmath
import math
import unittest
from fractions import Fraction as F

from observational_succ import duck_bbp
from observational_succ.haar_successor_junction import (
    signed_junction, word_law, collision_energy, haar_w1_upper,
    source_certified_digits, source_dyadic_shadow, exact_w1_to_haar,
    exact_w1_to_first_digit_twirl, temporal_succ_coboundary,
    rational_sqrt_upper,
)


def de_bruijn(k, order):
    arr=[0]*(k*order+1);seq=[]
    def rec(t,p):
        if t>order:
            if order%p==0: seq.extend(arr[1:p+1])
        else:
            arr[t]=arr[t-p];rec(t+1,p)
            for c in range(arr[t-p]+1,k):
                arr[t]=c;rec(t+1,t)
    rec(1,1)
    return seq


class HaarSuccessorJunctionTests(unittest.TestCase):
    def test_original_four_signed_poles(self):
        for n in range(1,200):
            alternative=F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
            self.assertEqual(alternative,duck_bbp.forcing(n))

    def test_certified_original_pi_hex(self):
        ds, phases, rad=source_certified_digits(1,18)
        self.assertEqual(''.join(f'{d:X}' for d in ds),'243F6A8885A308D313')
        self.assertLess(rad,F(1,10**16))
        self.assertTrue(all(F(0)<=x<F(1) for x in phases))

    def test_haar_energy_identity_nonstationary(self):
        digits=list((i*i+5*i+1)%16 for i in range(85))
        for j in range(3):
            z=signed_junction(digits,64,j)
            self.assertEqual(z['low_energy'],z['E_next']-z['E_depth'])
            self.assertEqual(4*z['common_gradient_inner'],z['high_energy']-z['low_energy'])
            self.assertEqual(z['common_energy']+z['half_gradient_energy'],(z['high_energy']+z['low_energy'])/2)
            self.assertLessEqual(20*z['successor_energy'],80*z['low_energy'])
            self.assertGreaterEqual(20*z['successor_energy'],3*z['low_energy'])

    def test_period16_one_digit_haar_false_normality(self):
        digits=list(range(16))*10
        j0=signed_junction(digits,128,0)
        j1=signed_junction(digits,128,1)
        self.assertEqual(j0['E_next'],0)
        self.assertEqual(j0['successor_energy'],0)
        self.assertEqual(j1['E_depth'],0)
        self.assertEqual(j1['low_energy'],15)
        self.assertEqual(j1['gradient_seam'],0)
        self.assertEqual(j1['common_energy'],15)
        self.assertEqual(j1['common_gradient_inner'],0)
        self.assertEqual(j1['high_energy'],j1['low_energy'])

    def test_order2_debruijn_pairs_haar_third_depth_not(self):
        cycle=de_bruijn(16,2)
        self.assertEqual(len(cycle),256)
        digits=cycle*2
        j0=signed_junction(digits,256,0)
        j1=signed_junction(digits,256,1)
        j2=signed_junction(digits,256,2)
        self.assertEqual(j0['low_energy'],0)
        self.assertEqual(j1['low_energy'],0)
        self.assertEqual(j2['gradient_seam'],0)
        self.assertEqual(j2['low_energy'],15)
        self.assertEqual(j2['common_energy'],15)

    def test_sharp_alternating_successor_upper(self):
        digits=[d for d in range(16) for _ in range(5 if d%2==0 else 3)]
        j0=signed_junction(digits+[0],64,0)
        self.assertGreater(j0['low_energy'],0)
        self.assertEqual(j0['successor_energy'],4*j0['low_energy'])

    def test_zero_word_all_child_variation(self):
        z=signed_junction([0]*75,64,1)
        self.assertGreater(z['low_energy'],0)
        self.assertGreater(z['successor_energy'],0)
        self.assertEqual(z['gradient_seam'],30)
        self.assertEqual(z['high_energy'],z['low_energy'])

    def test_signature_exact_in_finite_source(self):
        for A,N in ((16,64),(32,128)):
            ds, _, _=source_certified_digits(A,N+4)
            for j in range(3):
                z=signed_junction(ds,N,j)
                self.assertEqual(4*z['common_gradient_inner'],z['high_energy']-z['low_energy'])
                self.assertLessEqual(abs(z['high_energy']-z['low_energy']),F(4*16**j,N))
                self.assertLessEqual(z['stationarity_l1'],F(2,N))

    def test_character_parseval_source(self):
        A,N=16,64
        ds,_,_=source_certified_digits(A,N+4)
        j=1
        z=signed_junction(ds,N,j)
        p,q=z['edges'],z['suffix']
        character_energy=0.0
        for w in {(a,) for a in range(16)}:
            for h in range(1,16):
                g=sum(cmath.exp(2j*math.pi*h*a/16)*complex(p.get((a,)+w,F(0))) for a in range(16))
                character_energy+=abs(g)**2
        self.assertAlmostEqual((16**j)*character_energy,float(z['high_energy']),places=10)

    def test_executable_rational_sqrt_enclosure(self):
        for q in (F(0),F(2),F(1523,10000),F(7,11)):
            s=rational_sqrt_upper(q)
            self.assertGreaterEqual(s*s,q)
            self.assertLess((s-F(1,2**48))**2,q+F(1,10**8))

    def test_genuine_source_high_road_haar_bound(self):
        for A,N in ((16,64),(32,128)):
            ds,x,error=source_certified_digits(A,N+4)
            w=exact_w1_to_haar(x[:N])
            q=exact_w1_to_first_digit_twirl(x[:N])
            self.assertLessEqual(w+error,F(16,15)*(q+2*error)+F(1,15*N))
            for j in range(3):
                # all comparisons are exact rationals with outward sqrt bound
                witness=haar_w1_upper(signed_junction(ds,N,j))
                self.assertLessEqual(w+error,witness)

    def test_true_source_against_coherent_wrong_seed(self):
        A=64;N=A
        wrong_seed=source_dyadic_shadow(A)
        self.assertNotEqual(wrong_seed,0)
        ds,x,err=source_certified_digits(A,N+4,seed=wrong_seed,tail_depth=105)
        self.assertEqual(set(ds),{0})
        z=signed_junction(ds,N,0)
        self.assertEqual(z['E_next'],15)
        self.assertGreaterEqual(exact_w1_to_haar(x[:N])-err,F(49,100))

    def test_time_successor_vacuity(self):
        # Telescoping is never a substitute for digit-label successor contrasts.
        periodic=[F(0),F(1)]*128+[F(0)]
        avg=temporal_succ_coboundary(periodic)
        self.assertEqual(avg,F(0))
        nonnormal=[0]*100+[1]
        self.assertLessEqual(abs(temporal_succ_coboundary(nonnormal)),F(1,100))
        self.assertGreater(signed_junction([0]*105,100,0)['successor_energy'],0)

    def test_sampling_floor_and_sum_wavelet(self):
        N=128
        ds,_,_=source_certified_digits(32,N+4)
        results=[signed_junction(ds,N,j) for j in range(3)]
        e3=results[-1]['E_next']
        self.assertGreaterEqual(e3,F(16**3,N)-1)
        self.assertGreaterEqual(sum((r['successor_energy'] for r in results),F(0)),F(3,20)*e3)
        self.assertEqual(e3,F(32))

    def test_invalid_input(self):
        with self.assertRaises(ValueError): signed_junction([0]*9,10,0)
        with self.assertRaises(ValueError): word_law([16],1,1)
        with self.assertRaises(ValueError): rational_sqrt_upper(F(-1))

if __name__=='__main__': unittest.main()
