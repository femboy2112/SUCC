"""All exact rational tests of source-marked 2-adic/dual Lorentz-shaped bridge.

Hostile controls separate a representation boost from a physical speed limit,
and congruence from selected real phase. No source replacement or pi digits.
"""
import importlib.util
from fractions import Fraction as Q
from pathlib import Path
import random
import unittest

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'research'/'2026-11-03'/'causal_lorentz_gluing'/'causal_lorentz.py'
spec=importlib.util.spec_from_file_location('causal_lorentz',SOURCE)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ExactCotangent(unittest.TestCase):
    def test_source_algebra_eighth_return_both_duals(self):
        self.assertEqual(m.eight_step_cotangent()[0],tuple(tuple(m.I4[i][j]/16 for j in range(4)) for i in range(4)))
        self.assertTrue(all(m.halfclock_channel_signs()))
        self.assertEqual(m.parent.power(m.parent.U,8),m.parent.scale(m.parent.ONE,Q(1,16)))

    def test_cotangent_lift_preserves_exact_pairing_and_metric(self):
        self.assertTrue(m.split_metric_preserved())
        A=m.cotangent_lift_matrix()
        self.assertEqual(m.matpow(A,8),m.matmul(m.matpow(A,4),m.matpow(A,4)))
        rng=random.Random(20261103)
        for _ in range(35):
            v=tuple(Q(rng.randint(-10,10),rng.randint(1,7)) for _ in range(4))
            f=tuple(Q(rng.randint(-10,10),rng.randint(1,7)) for _ in range(4))
            w,g=m.cotangent_step(v,f)
            self.assertEqual(m.dual_pair(v,f),m.dual_pair(w,g))
            self.assertEqual(m.split_q(v,f),m.split_q(w,g))

    def test_source_selected_null_plane_and_canonical_gamma(self):
        b,f=m.source_selected_null_plane()
        self.assertEqual(m.dual_pair(b,f),1)
        eight=m.eight_step_cotangent()
        self.assertEqual(m.matvec(eight[0],b),tuple(v/16 for v in b))
        self.assertEqual(m.matvec(eight[1],f),tuple(16*v for v in f))
        data=m.boost_from_scale(16)
        self.assertEqual(data['gamma'],Q(257,32))
        self.assertEqual(data['gamma_beta'],Q(255,32))
        self.assertEqual(data['beta'],Q(255,257))
        self.assertEqual(data['half_rapidity_parameter'],Q(15,17))
        self.assertEqual(data['gamma']**2-data['gamma_beta']**2,1)
        self.assertEqual((257**2-255**2),32**2)

    def test_exact_lorentz_form_and_velocity_composition(self):
        for c in (Q(1),Q(4),Q(13,5)):
            for t,x in ((Q(1),Q(0)),(Q(3,4),Q(1,6)),(Q(1),-c), (Q(0),Q(1))):
                a,b=m.transform_lorentz(t,x,c=c)
                self.assertEqual(m.lorentz_interval(t,x,c),m.lorentz_interval(a,b,c))
            a,b=m.transform_lorentz(Q(1),c,lam=16,c=c)
            self.assertEqual(b,c*a)  # one future null ray stays null
        g=m.boost_from_scale(16)
        self.assertEqual(m.boost_from_scale(Q(16)*Q(16))['matrix'],m.matmul(g['matrix'],g['matrix']))

    def test_gauge_scale_not_physical_c_or_convergence(self):
        for c in (1,2,4,11):
            t,x=m.transform_lorentz(1,0,c=c)
            self.assertEqual(t,Q(257,32))
            self.assertEqual(x/c,Q(255,32))
            self.assertEqual(m.lorentz_interval(t,x,c),c*c)
        self.assertFalse(m.model_snapshot()['pi_normality_proved'])

    def test_metric_preservation_is_not_source_authentication(self):
        # A wrong dual action and source-changed same-return filter clarify scope.
        T=m.multiplication_matrix()
        wrong=tuple(tuple(T[i][j] if i<4 and j<4 else
                          T[i-4][j-4] if i>=4 and j>=4 else Q(0)
                          for j in range(8)) for i in range(8))
        self.assertFalse(m.split_metric_preserved(wrong))
        self.assertEqual(m.boost_from_scale(3)['gamma'],Q(5,3))
        self.assertNotEqual(m.boost_from_scale(3)['gamma'],m.boost_from_scale(16)['gamma'])
        for n in (1,2,3,8):
            # Identical Gaussian successor and eighth clock, changed readout/source.
            self.assertGreater(m.parent.mutated_mellin_source(n,Q(1,8))-m.source_r(n),0)
        self.assertFalse(m.model_snapshot()['pi_normality_proved'])

    def test_flat_source_frame_groupoid_and_twisted_loop(self):
        A=m.frame_transport(-2,3)
        B=m.frame_transport(3,9)
        C=m.frame_transport(9,-2)
        self.assertEqual(m.matmul(C,m.matmul(B,A)),m.identity(8))
        self.assertTrue(m.split_metric_preserved(A))
        bad=m.signed_holonomy_mutant()
        self.assertTrue(m.split_metric_preserved(bad))
        self.assertNotEqual(m.matmul(bad,m.matmul(C,m.matmul(B,A))),m.identity(8))


class SourcePrecisionCone(unittest.TestCase):
    def test_original_source_integer_and_2_integral(self):
        for n in range(1,1025):
            self.assertEqual(m.forcing_at_integer(n),m.source_r(n))
            self.assertEqual(m.v2(m.source_r(n))>=0,True)
        for n in range(-90,1):
            self.assertEqual(m.v2(m.forcing_at_integer(n))>=0,True)

    def test_sharp_pulse_horizon_for_every_precision(self):
        for k in range(1,113):
            h=m.precision_horizon(k)
            self.assertEqual(h,(k+3)//4)
            self.assertNotEqual(m.pulse_reaches(k,h-1,1),0)
            self.assertEqual(m.pulse_reaches(k,h,1),0)
            self.assertEqual(m.pulse_reaches(k,h+2,1),0)

    def test_original_zero_source_exact_suffix_equals_full(self):
        for bits in (1,2,3,4,5,7,8,13,16,24,41,67):
            for n in (0,1,2,5,7,13,31,64,97,131):
                self.assertEqual(m.source_state_mod(n,bits),m.suffix_source_mod(n,bits))

    def test_glue_before_2adic_quotient_is_mandatory(self):
        for n in (1,2,3,8,13,19,37,63,127):
            a,b=m.parent.mellin_channels(n)
            self.assertEqual(m.v2(a),-5-m.v2(Q(n)))
            self.assertEqual(m.v2(b),-5-m.v2(Q(n)))
            for bits in (1,5,8,13,37):
                self.assertEqual(m.source_glued_mod(n,bits),m.rational_mod_2k(m.source_r(n),bits))
                with self.assertRaises(ValueError):m.rational_mod_2k(a,bits)
                with self.assertRaises(ValueError):m.rational_mod_2k(b,bits)

    def test_no_2adic_to_real_circle_uniform_control(self):
        for k in (1,2,8,16,32,100):
            ghost=m.near_ghost(k)
            self.assertEqual(m.v2(ghost),k)
            self.assertGreaterEqual(ghost,Q(1,3))
            self.assertLess(ghost,Q(1,2))

    def test_same_original_forcing_different_seed_remains_real_shift(self):
        for k in (1,2,7,16,41,100):
            n=m.precision_horizon(k)
            a=m.rational_seed_ambiguity(n,k)
            self.assertEqual(a['residue'],0)
            self.assertEqual(a['real_phase_offset'],Q(1,5))
            if n:
                b=m.rational_seed_ambiguity(n-1,k)
                self.assertNotEqual(b['residue'],0)


class IsometricReferenceFrame(unittest.TestCase):
    def test_original_source_forcing_is_2adic_isometry_at_index(self):
        for x,y in [(0,1),(0,2),(1,5),(-11,17),(123,251),(0,256)]:
            self.assertEqual(m.v2(m.force_difference_quotient_unit(x,y)),0)

    def test_F_zero_and_original_recursion_all_small_precisions(self):
        for k in (1,2,3,4,5,6,7,8,12,16,25):
            self.assertEqual(m.particular_mod(0,k),0)
            for n in (0,1,2,3,9,21,51,100):
                self.assertEqual(m.particular_mod(n,k),m.source_state_mod(n,k))

    def test_every_finite_residue_is_unique_and_shift_is_full_cycle(self):
        for k in range(1,8):
            mod=1<<k
            f=[m.particular_mod(n,k) for n in range(mod)]
            self.assertEqual(sorted(f),list(range(mod)))
            for n,y in enumerate(f):
                self.assertEqual(m.particular_inverse_mod(y,k),n)
                self.assertEqual(m.source_state_successor_mod(y,k),f[(n+1)%mod])
            y=0
            for i in range(mod):
                self.assertEqual(y,f[i])
                y=m.source_state_successor_mod(y,k)
            self.assertEqual(y,0)

    def test_state_map_isometry_despite_contracting_linear_part(self):
        for k in (2,3,4,5,6,7):
            mod=1<<k
            for y in range(mod):
                if y%3:
                    continue
                for z in range(0,mod,max(1,mod//7)):
                    if y==z:
                        continue
                    delta=(y-z)%mod
                    new=(m.source_state_successor_mod(y,k)-m.source_state_successor_mod(z,k))%mod
                    self.assertEqual(m.v2(Q(delta)),m.v2(Q(new)))
                    self.assertNotEqual(new,0)

    def test_independent_absolute_value_shift_modulus(self):
        for k in (3,7,13,19):
            n=12
            self.assertEqual(m.particular_mod(n+1,k),m.source_state_successor_mod(m.particular_mod(n,k),k))
            self.assertEqual(m.particular_inverse_mod(m.particular_mod(n,k),k),n%(1<<k))

if __name__=='__main__':unittest.main()
