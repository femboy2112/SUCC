"""Exact and adversarial finite tests of BBP sourced chiral loop probes."""
import unittest
from fractions import Fraction
from cmath import exp, pi
from chiral_probe import (
    forcing, forcing_compact, source_states, mod_fraction, return_jet,
    expected_jet16, expected_jet32, expected_ratio32, source_chirality,
    time_projection, four_walsh_channels, invert_walsh_channels,
    forcing_mutant, mutant_states, g, v2_fraction, tail_interval,
    circle_midpoint, complex_loop_signal, squared_two_path_output, phase,
)


class ExactChiralTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q16 = source_states(90)
        cls.q256 = source_states(290)
        cls.mutant = mutant_states(90)

    def test_exact_original_four_poles_positive_and_negative(self):
        for n in range(-50,100):
            self.assertEqual(forcing(n),forcing_compact(n))

    def test_modular_phase_11_11_3_3_one_loop(self):
        for n in range(3,50):
            self.assertEqual(return_jet(self.q16,n,1),expected_jet16(n))

    def test_modular_phase_two_loop_scales(self):
        for n in range(4,20):
            self.assertEqual(return_jet(self.q256,n,2),expected_jet16(n))

    def test_7_plusminus_4_source_character(self):
        self.assertEqual([expected_jet16(n) for n in range(4)], [11,11,3,3])
        for n in range(16):
            self.assertEqual(expected_jet16(n),7+4*source_chirality(n))
            self.assertEqual((expected_jet16(n)-7)**2,16)

    def test_multiplicative_inverse_and_opposite_circle_phases(self):
        for n in range(16):
            a=expected_jet16(n);b=expected_jet16(n+2)
            self.assertEqual((a*b)%16,1)
            self.assertEqual((b-a)%16,8)
            self.assertAlmostEqual(abs(phase(a)+phase(b)),0,places=12)

    def test_second_32_adic_root_branch_table_one_loop(self):
        for n in range(3,40):
            self.assertEqual(return_jet(self.q16,n,1,5), expected_jet32(n))

    def test_second_32_adic_root_branch_table_two_loop_scales(self):
        for n in range(4,21):
            self.assertEqual(return_jet(self.q256,n,2,5),expected_jet32(n))

    def test_next_precision_commutator_is_plusminus_i(self):
        for k,states,start in [(1,self.q16,3),(2,self.q256,4)]:
            for n in range(start,start+15):
                delta = (return_jet(states,n+2,k,5)-return_jet(states,n,k,5))%32
                self.assertEqual(delta, expected_ratio32(n))
                expected = -1j if n%2==0 else 1j
                self.assertLess(abs(exp(2j*pi*delta/32)-expected),2e-14)
                self.assertEqual(delta%16,8)

    def test_pauli_anticommutation_on_four_original_clock_states(self):
        # Each operation on a basis vector is exact in Z (after normalizing phase).
        for n in range(4):
            # Shift^2 Z |n> and Z Shift^2 |n> must differ by sign.
            a=source_chirality(n)
            b=source_chirality((n+2)%4)
            self.assertEqual(a,-b)
            self.assertEqual(a*a,1)
        self.assertEqual(sum(source_chirality(n) for n in range(4)),0)

    def test_walsh_channels_are_complete_and_no_dc_leak(self):
        data=[2-3j,8+1j,-6+4j,5-7j]
        ch=four_walsh_channels(data)
        self.assertEqual(invert_walsh_channels(ch),data)
        self.assertEqual(four_walsh_channels([1,1,1,1])['high'],0)
        self.assertEqual(four_walsh_channels([1,1,1,1])['low'],0)
        self.assertEqual(four_walsh_channels([1,1,1,1])['joint'],0)

    def test_source_chirality_is_4_tap_koopman_filter(self):
        f=[3,7,11,13]
        self.assertEqual(sum(source_chirality(n)*f[n] for n in range(4)),
                         f[0]+f[1]-f[2]-f[3])
        # (1-K)(1+K)^2 = 1+K-K^2-K^3 coefficient-by-coefficient
        a=[1,2,1];b=[1,-1]
        conv=[sum(a[j]*b[k-j] for j in range(len(a)) if 0<=k-j<len(b))
              for k in range(4)]
        self.assertEqual(conv,[1,1,-1,-1])

    def test_genuine_source_tail_interval_positive_and_shrinking(self):
        for n in [3,7,12,20]:
            a,b=tail_interval(n,6)
            c,d=tail_interval(n,12)
            self.assertGreater(a,0)
            self.assertGreater(b,a)
            self.assertLessEqual(a,c)
            self.assertLessEqual(d,b)

    def test_exact_zero_anchored_coboundary_mutant_history(self):
        for n in range(90):
            self.assertEqual(self.mutant[n],self.q16[n]+g(n))
        self.assertEqual(g(0),0)

    def test_mutant_forcing_remains_2_adic_isometry(self):
        for a in range(-12,13):
            for b in range(-12,13):
                if a==b: continue
                self.assertEqual(v2_fraction(forcing_mutant(a)-forcing_mutant(b)),
                                 v2_fraction(Fraction(a-b)))

    def test_same_clock_isometry_mutant_kills_anticommutator(self):
        for n in range(3,42):
            j=return_jet(self.mutant,n,1)
            self.assertEqual(j,(expected_jet16(n)+4*n)%16)
            self.assertEqual(return_jet(self.mutant,n+2,1),j)
        self.assertEqual([return_jet(self.mutant,n,1) for n in range(4,8)],
                         [11,15,11,15])

    def test_four_time_interferometer_circle_phase_smoke(self):
        # NOT a certified numerical proof of an infinite result. Phase error
        # includes float and individually bounded exact rational Green tails.
        for n in range(5,17):
            v0=complex_loop_signal(self.q16,n,1,1,12)
            v2=complex_loop_signal(self.q16,n+2,1,1,12)
            z0=circle_midpoint(self.q16,n)
            zq=circle_midpoint(self.q16,n+16)
            predicted=-exp(2j*pi*255*(zq-z0))
            self.assertLess(abs(v2*v0.conjugate()-predicted),3e-10)
            energy=squared_two_path_output(v0,v2)
            self.assertAlmostEqual(energy,2-2*predicted.real*(-1),places=8)

    def test_wrong_seed_locked_phase_null(self):
        for n in range(3,11):
            v0=phase(return_jet(self.q16,n,1))
            v2=phase(return_jet(self.q16,n+2,1))
            self.assertLess(abs(v0+v2),2e-14)
            self.assertLess(squared_two_path_output(v0,v2),2e-26)

    def test_rational_loop_periodic_nonnormal_null(self):
        q=16
        # x=1/(16^16-1) is a periodic nonnormal orbit, hence z_(n+q)=z_n.
        x=Fraction(1,16**q-1)
        for n in range(10):
            z=((16**n*x)%1)
            zz=((16**(n+q)*x)%1)
            self.assertEqual(z,zz)

    def test_causal_response_normality_sufficient_one_mode_bound(self):
        # Pointwise elementary inequality, checked finite grid as control only.
        for j in range(1001):
            z=j/1001
            em=2-2*exp(2j*pi*255*z).real
            e1=2-2*exp(2j*pi*z).real
            self.assertLessEqual(em, 255**2*e1+1e-11)

    def test_wrong_source_energy_signal_not_generic_norm(self):
        # Original and mutant have identical base-16 isometric clock
        # marginals, but original two-step source phase is anticommuting.
        for n in range(3,20):
            self.assertEqual(return_jet(self.q16,n,1,4)%2,
                             return_jet(self.mutant,n,1,4)%2)
            self.assertEqual((return_jet(self.q16,n+2,1)-return_jet(self.q16,n,1))%16,8)
            self.assertEqual((return_jet(self.mutant,n+2,1)-return_jet(self.mutant,n,1))%16,0)


if __name__ == '__main__':
    unittest.main()
