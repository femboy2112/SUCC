"""Reproducible focused source and oscillator tests (separate from proof)."""
import cmath
import math
import random
import unittest
from fractions import Fraction
from observational_succ.pinbed_oscillator_bridge import (
    aperture_factor, energy_pair, energy_transfer_bound, evolve_mode,
    four_pole, heterodyne_decode, heterodyne_qi, local_plaquette,
    mode_recovery_and_defect, mode_vector, mode_weight,
    source_history, two_tone_frame_constants,
)


class OscillatorBridgeTests(unittest.TestCase):
    def test_source_perfect_flatness_even_for_wrong_seeds(self):
        for seed in (0,Fraction(1,3),Fraction(-2,7)):
            v=source_history(90,seed)
            self.assertTrue(all(local_plaquette(v,n)==0 for n in range(90)))
        mutated=list(source_history(20))
        mutated[12]=(mutated[12]+Fraction(1,7))%1
        self.assertNotEqual(local_plaquette(tuple(mutated),11),0)
        self.assertEqual(four_pole(1),Fraction(47,15))

    def test_mode_syzygy_and_projection_recover_coherent_carrier(self):
        a=(math.sqrt(5)-1)/2
        for h in list(range(-60,0))+list(range(1,61)):
            m=cmath.exp(-2j*math.pi*h/17)
            f=mode_vector(a,h,m)
            got,resid=mode_recovery_and_defect(a,h,f)
            self.assertAlmostEqual(abs(got-m),0,delta=1e-12)
            self.assertLess(resid,1e-25)
            bad=(f[0],f[1]+0.05j)
            _,defect=mode_recovery_and_defect(a,h,bad)
            self.assertGreater(defect,0)

    def test_explicit_dynamics_naturality_composition_and_hostile_mutant(self):
        a=(math.sqrt(5)-1)/2
        for x in (0,0.12,0.43):
            for h in (1,2,7,19):
                b,t=16,0.031
                input_f=mode_vector(a,b*h,cmath.exp(-2j*math.pi*b*h*x))
                after=evolve_mode(a,h,b,t,input_f)
                expected=mode_vector(a,h,cmath.exp(-2j*math.pi*h*(b*x+t)))
                for u,v in zip(after,expected):
                    self.assertAlmostEqual(abs(u-v),0,delta=1e-12)
                with self.assertRaises(ValueError):
                    evolve_mode(a,h,b,t,(input_f[0],input_f[1]+1j))
        # General affine composition: (c,u)(b,t)=(bc,ct+u)
        b,t,c,u=3,0.125,5,-0.1
        x=0.17
        for h in (1,2,4):
            initial=mode_vector(a,b*c*h,cmath.exp(-2j*math.pi*b*c*h*x))
            intermediate=evolve_mode(a,c*h,b,t,initial)
            composed=evolve_mode(a,h,c,u,intermediate)
            once=evolve_mode(a,h,b*c,c*t+u,initial)
            for v,w in zip(composed,once):
                self.assertAlmostEqual(abs(v-w),0,delta=1e-12)

    def test_heterodyne_positive_intensity_recovers_signed_information(self):
        rng=random.Random(2026)
        for _ in range(100):
            x=Fraction(rng.randint(-30,30),rng.randint(1,21))
            y=Fraction(rng.randint(-30,30),rng.randint(1,21))
            intensities=heterodyne_qi(x,y)
            self.assertEqual(heterodyne_decode(intensities),(x,y))
        with self.assertRaises(ValueError):
            heterodyne_decode((0,0,0))

    def test_two_tone_continuum_coercivity_and_bounded_times16(self):
        a=(math.sqrt(5)-1)/2
        lo,hi=two_tone_frame_constants(a)
        self.assertGreater(lo,0)
        norm=16*(hi/lo)**.5
        self.assertLess(norm,112)
        for h in list(range(-600,0))+list(range(1,601)):
            w=mode_weight(a,h)
            self.assertGreaterEqual((1+abs(h))**2*w+1e-8,lo)
            self.assertLessEqual((1+abs(h))**2*w,hi+1e-8)
            self.assertLessEqual((w/mode_weight(a,16*h))**.5,norm+1e-8)
        self.assertGreater(energy_pair((Fraction(0),),a),1)
        self.assertAlmostEqual(energy_transfer_bound(a,64),energy_transfer_bound(a,32)/4)

    def test_independent_direct_pair_energy_checks(self):
        a=(math.sqrt(5)-1)/2
        samples=(Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4))
        direct=energy_pair(samples,a)
        spectral=0.
        for h in list(range(-2000,0))+list(range(1,2001)):
            coeff=sum(cmath.exp(-2j*math.pi*h*float(x)) for x in samples)/len(samples)
            spectral += mode_weight(a,h)*abs(coeff)**2
        lo,hi=two_tone_frame_constants(a)
        self.assertLess(abs(direct-spectral),2*hi/2000)
        for A in (16,32,64,128):
            src=source_history(2*A)
            self.assertGreaterEqual(energy_pair(src[A:2*A],a),-1e-8)

    def test_negative_moment_not_probability_even_if_channel_syzygy(self):
        # m_0=1, m_{+/-1}=2 passes rank-one channel algebra but fails
        # probability positivity: [[1,2],[2,1]] determinant -3.
        a=0.618
        for h in (-1,1):
            _, residual=mode_recovery_and_defect(a,h,mode_vector(a,h,2))
            self.assertLess(residual,1e-20)
        self.assertEqual(1*1-2*2,-3)

if __name__=='__main__': unittest.main()
