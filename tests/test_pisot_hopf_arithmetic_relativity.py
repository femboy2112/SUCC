"""Exact source algebra and hostile controls for arithmetic clock/curvature analogy."""
import math
import unittest
from fractions import Fraction as F
from observational_succ.hopf_source_exact import H, ONE, ZERO, SOURCE_ORIGIN,t_step,pole_quaternion,original_forcing,unwrapped_zero_seed
from observational_succ.pisot_hopf_arithmetic_relativity import (
    harmonic_clock_at,harmonic_succ_tick,harmonic_prime_tick,
    harmonic_dilation_braid_defect,harmonic_dilation_braid_direct,
    braid_defect_bounds,integrable_braid_defect,
    pisot_quadratic_coefficients,pisot_quadratic_trace,
    chiral_eight_step_sync,hopf_local_connection,hopf_curvature_origin,
    hopf_wilson_rectangle,hopf_wilson_rectangle_reverse,source_curvature_probe,
    source_clock_latitude_energy,source_clock_latitude_step,
    source_prime_frame_commutator,source_prime_frame_commutator_direct,
    zero_seed_compact_clock,zero_seed_compact_clock_tick,
    authenticated_chiral_square,authenticated_chiral_bargmann,
    authenticated_chiral_bargmann_ratio,chiral_bargmann_decay_bound
)

class ArithmeticClockTests(unittest.TestCase):
    def test_exact_positive_mixed_frame_defect(self):
        for p in (2,3,5,7,11):
            for n in (1,2,3,5,7,13,37):
                d=harmonic_dilation_braid_defect(n,p)
                self.assertEqual(d,harmonic_dilation_braid_direct(n,p))
                self.assertGreater(d,0)
                lo,main,error=braid_defect_bounds(n,p)
                self.assertLessEqual(lo,d)
                self.assertLess(d,main)
                self.assertLessEqual(main-d,error)

    def test_exact_integrable_clocks_close_all_affine_squares(self):
        for n in (1,2,3,5,8,12):
            for p in (2,3,5,7):
                self.assertEqual(integrable_braid_defect(n,p),0)
                self.assertEqual(harmonic_clock_at(p*n)-harmonic_clock_at(n),harmonic_prime_tick(n,p))
                self.assertEqual(harmonic_clock_at(n+1)-harmonic_clock_at(n),F(1,n))

    def test_harmonic_gamma_and_fibonacci_log_clocks_numerical_only(self):
        # Known classical asymptotics; this floating check is NOT a rigorous proof.
        gamma=0.5772156649015328606
        for n in (64,256,1024,4096):
            defect=float(harmonic_clock_at(n+1))-math.log(n+1)
            self.assertGreater(defect,0)
            self.assertLess(abs(defect-gamma),1/n)
        f0,f1=0,1
        for _ in range(24):f0,f1=f1,f0+f1
        phi=(1+math.sqrt(5))/2
        self.assertLess(abs(float(harmonic_clock_at(f0+1))-24*math.log(phi)+math.log(5)/2-gamma),2/f0)

    def test_pisot_integer_return_certificate(self):
        for m in (1,2,3,5):
            beta=(m+math.sqrt(m*m+4))/2
            for k in range(0,12):
                a,b=pisot_quadratic_coefficients(m,k)
                self.assertLess(abs(a*beta+b-beta**k),1e-6)
                self.assertLess(abs(beta**k+(-1/beta)**k-pisot_quadratic_trace(m,k)),1e-6)

    def test_pisot_source_is_not_needed_for_circle_injection(self):
        # Irrational sqrt(2) is not Pisot; it still gives an injective orbit.
        # This protects against claiming a unique Pisot minimality theorem.
        for n in range(1,45):
            self.assertGreater(abs(math.sin(math.pi*n*math.sqrt(2))),1e-5)

    def test_source_eight_to_one_clock_sync(self):
        for x in (SOURCE_ORIGIN,H(1,2,3,4),H(0,0,3,-5)):
            for n in range(0,7):
                self.assertTrue(chiral_eight_step_sync(x,n))

    def test_original_BBP_real_frame_commutator_source_locked(self):
        for n in range(0,45):
            for p in (2,3,5,7):
                d=source_prime_frame_commutator(n,p)
                self.assertEqual(d,source_prime_frame_commutator_direct(n,p))
                self.assertEqual(d,source_prime_frame_commutator_direct(n,p,F(149,97)))
                self.assertGreater(d,0)
                self.assertEqual(d/F(p-1),original_forcing(n+1))

    def test_original_BBP_compact_green_clock(self):
        self.assertEqual(zero_seed_compact_clock(0),0)
        for n in range(1,36):
            self.assertEqual(zero_seed_compact_clock(n)-zero_seed_compact_clock(n-1),
                             zero_seed_compact_clock_tick(n))
            self.assertGreater(zero_seed_compact_clock_tick(n),0)

    def test_real_seed_distinguisher_survives_clock_analogies(self):
        for n in range(1,7):
            self.assertEqual(unwrapped_zero_seed(n,F(1,3))-unwrapped_zero_seed(n),F(16**n,3))
            self.assertEqual(original_forcing(n),sum(tuple(pole_quaternion(n)),F(0)))

class HopfCurvatureTests(unittest.TestCase):
    def test_authentic_chiral_commuting_square_nontrivial_holonomy(self):
        from observational_succ.hopf_source_exact import j_chirality
        vertices=authenticated_chiral_square(0)
        self.assertEqual(tuple(tuple(z) for z in vertices),(
            (F(2),F(0),F(0),F(0)),
            (F(1),F(1),F(0),F(0)),
            (F(0),F(0),F(1),F(-1)),
            (F(0),F(0),F(2),F(0)),
        ))
        W=authenticated_chiral_bargmann(0)
        self.assertEqual(tuple(W),(F(109),F(-40),F(-28),F(-10)))
        self.assertEqual(W.norm2(),F(14365))
        self.assertEqual(authenticated_chiral_bargmann_ratio(0),F(11881,14365))
        self.assertNotEqual(W,H(W.a))

    def test_bargmann_holonomy_rapidly_decays(self):
        for n in range(0,25):
            W=authenticated_chiral_bargmann(n)
            eps=chiral_bargmann_decay_bound(n)
            self.assertLessEqual((W-ONE).norm2(),eps*eps)
            self.assertGreaterEqual(authenticated_chiral_bargmann_ratio(n),0)
            self.assertLessEqual(authenticated_chiral_bargmann_ratio(n),1)
        self.assertLess(chiral_bargmann_decay_bound(25),F(1,100000))

    def test_connection_pure_imaginary(self):
        for x in (ZERO,H(1),H(1,2,3,4)):
            for v in (H(1,3),H(0,0,1,1)):
                self.assertEqual(hopf_local_connection(x,v).a,0)

    def test_exact_nonzero_hopf_curvature(self):
        v=SOURCE_ORIGIN
        w=t_step(v)
        self.assertEqual(source_curvature_probe(),H(0,4))
        self.assertEqual(hopf_curvature_origin(v,w),H(0,4))
        self.assertEqual(hopf_curvature_origin(w,v),H(0,-4))
        self.assertEqual(hopf_curvature_origin(v,v.scale(3)),ZERO)

    def test_exact_wilson_loop_orientation_and_nontriviality(self):
        v=SOURCE_ORIGIN; w=t_step(v)
        for eps in (F(1,10),F(1,50),F(1,100)):
            loop=hopf_wilson_rectangle(v,w,eps)
            reverse=hopf_wilson_rectangle_reverse(v,w,eps)
            self.assertEqual(reverse,loop.conj())
            self.assertNotEqual(loop.b,0)
            # infinitesimal curvature: Im(W)/eps² -> F_0(v,w)=4i.
            self.assertEqual(loop.b/eps**2,F(4)+F(20)*eps**2)

    def test_noncommuting_hopf_loop_holonomies(self):
        v=SOURCE_ORIGIN
        w1=t_step(v);w2=t_step(w1)
        w_loop1=hopf_wilson_rectangle(v,w1,F(1,10))
        w_loop2=hopf_wilson_rectangle(v,w2,F(1,10))
        self.assertNotEqual(w_loop1*w_loop2,w_loop2*w_loop1)

    def test_source_chart_rapidity_mobius(self):
        for n in range(0,25):
            self.assertEqual(source_clock_latitude_step(source_clock_latitude_energy(n)),source_clock_latitude_energy(n+1))
        self.assertEqual(source_clock_latitude_energy(0),F(3,5))
        self.assertEqual(source_clock_latitude_energy(2),F(0))
        self.assertEqual(source_clock_latitude_energy(8),F(-63,65))

    def test_no_source_hypothesis_from_hopf_curvature(self):
        # Local Hopf curvature depends only on chosen plane, not on authentic BBP seed.
        for seed in (F(0),F(1,3)):
            self.assertEqual(source_curvature_probe(),H(0,4))
            self.assertNotEqual(unwrapped_zero_seed(1,seed),unwrapped_zero_seed(1,seed+1))

if __name__=='__main__':unittest.main()
