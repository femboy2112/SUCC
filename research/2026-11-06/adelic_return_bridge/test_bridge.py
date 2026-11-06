"""Finite hostile probes of the authentic BBP cross-place carry/phase seam."""
from __future__ import annotations
import unittest
from fractions import Fraction
from math import floor
from bridge import (original_source, independent_four_pole, source_z, mod2_fraction,
                    raw_phases, d_circle, exact_return_witness, normalized_phase_diagnostics,
                    reconstruct_frac, carry_increments, carry_mod_recent, v_padic_mod,
                    real_phase_from_2adic_carry, shadow, source_return_sum_mod, return_fiber_energy_float)

class CrossPlaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.phases,cls.carries=raw_phases(2240)
        cls.increments=carry_increments(cls.phases)

    def test_original_four_signed_poles(self):
        for n in range(1,201):
            self.assertEqual(original_source(n),independent_four_pole(n))
            self.assertEqual(original_source(n).denominator%2,1)

    def test_unwrapped_recurrence_independent_carry(self):
        u=Fraction(0)
        for n in range(0,381):
            if n:
                u=16*u+independent_four_pole(n)
            self.assertEqual(u,Fraction(self.carries[n])+self.phases[n])

    def test_2adic_source_completion_and_literal_zero(self):
        for k in range(1,25):
            self.assertEqual(v_padic_mod(0,k),0)
        for n in [0,1,2,3,9,17,43,149,293]:
            for k in [1,2,3,4,8,9,16,20]:
                v=(mod2_fraction(self.phases[n],k)+self.carries[n])%(1<<k)
                self.assertEqual(v,v_padic_mod(n,k))

    def test_carry_recent_window_exact(self):
        for n in [0,1,2,7,13,43,73,149,293]:
            for k in [1,2,3,4,5,8,9,12,13,17,24]:
                self.assertEqual(carry_mod_recent(self.increments,n,k),self.carries[n]%(1<<k))

    def test_witness_pre_registered_k9_10_11(self):
        for k in (9,10,11):
            w=exact_return_witness(self.phases,self.carries,k)
            self.assertTrue(w['unwrapped_residues_equal'])
            self.assertTrue(w['exact_ge_quarter'])
            self.assertEqual(w['n'],128)
            self.assertNotEqual(w['fractional_left_residue'],w['fractional_right_residue'])

    def test_2adic_permutations_exact(self):
        for k in range(1,9):
            r={v_padic_mod(n,k) for n in range(1<<k)}
            self.assertEqual(r,set(range(1<<k)))

    def test_known_denominator_reconstruction(self):
        for n in [1,2,7,17,43,73,149,293,587]:
            x=self.phases[n]
            k=max(1,x.denominator.bit_length())
            v=(mod2_fraction(x,k)+self.carries[n])%(1<<k)
            self.assertEqual(reconstruct_frac((v-self.carries[n])%(1<<k),x.denominator,k),x)
            self.assertEqual(real_phase_from_2adic_carry(n,k,x,self.carries[n]),x)
            self.assertLessEqual(x.denominator,1<<k)

    def test_carry_omission_changes_phase_reconstruction(self):
        n=73
        x=self.phases[n]
        k=x.denominator.bit_length()
        raw=(mod2_fraction(x,k)+self.carries[n])%(1<<k)
        self.assertNotEqual(raw,mod2_fraction(x,k))
        # An unlogged carry can produce a *different, plausible* fractional phase.
        wrong=reconstruct_frac(raw,x.denominator,k)
        self.assertNotEqual(wrong,x)

    def test_rational_ambiguity_below_denominator_bit_depth(self):
        for d in [3,5,17,137,12345]:
            k=d.bit_length()-1
            self.assertTrue((1<<k)<d)
            # 0 and 2^k are distinct valid numerators both congruent mod2^k.
            self.assertEqual(0%(1<<k),(1<<k)%(1<<k))

    def test_periodic_2power_factor_calibration(self):
        beta=Fraction(1,17)
        self.assertEqual((16*beta)%1,Fraction(16,17))
        self.assertEqual((16*16*beta)%1,beta)
        for k in range(1,10):
            self.assertEqual((pow(16,1<<k,17)),1)
        # Sharpness of the positive-expansivity constant 1/17.
        for n in range(20):
            z=(pow(16,n,17)*beta)%1
            self.assertEqual(d_circle(z,0),Fraction(1,17))

    def test_shadow_padic_isometry_nonhaar_real(self):
        self.assertEqual(shadow(0),0)
        for k in range(1,8):
            vals={mod2_fraction(shadow(n),k) for n in range(1<<k)}
            self.assertEqual(len(vals),1<<k)
        for n in [50,200,1000]:
            self.assertTrue(shadow(n)<Fraction(1,n*n))

    def test_future_source_replicates_present_2adically(self):
        for k in range(1,11):
            q=1<<k
            for n in [0,7,43,128]:
                self.assertEqual(source_return_sum_mod(n,q,k),v_padic_mod(n,k))

    def test_conditional_return_energy_bounds_weyl(self):
        for k,M in [(3,64),(4,32),(5,16)]:
            d=return_fiber_energy_float(self.phases,k,M)
            self.assertGreaterEqual(d['return_energy_float']+1e-10,d['signed_weyl_squared_float'])
            self.assertLessEqual(d['return_energy_float'],1+1e-10)

    def test_source_mutants_identify_which_boundary_is_specific(self):
        def first_pole_mutant(z):
            return source_z(z)+Fraction(1,8*z-7)
        def pmod(q,k):
            return mod2_fraction(q,k)
        # Original source V(0)=0. The 4->5 pole mutant fails already at mod 2.
        self.assertEqual(pmod(source_z(0),1),0)
        self.assertEqual(pmod(first_pole_mutant(0),1),1)
        # A nonoriginal rational source coboundary preserves V(0)=0 and Haar.
        def H(z): return Fraction(z,(2*z-1)**4)
        def gauge(z): return source_z(z)+2*H(z)-32*H(z-1)
        self.assertNotEqual(gauge(2),source_z(2))
        for k in range(1,7):
            M=1<<k
            def vmut(n):
                return sum((16**j)*pmod(gauge(n-j),k)
                           for j in range((k+3)//4))%M
            self.assertEqual(vmut(0),0)
            self.assertEqual(len({vmut(n) for n in range(M)}),M)

    def test_surrogate_holdout_reports_not_proof(self):
        for k in [9,10]:
            d=normalized_phase_diagnostics(self.phases,self.carries,k)
            self.assertTrue(d['surrogate_exact_mean_zero'])
            self.assertGreater(d['rms_phase_error_float'],1)
            self.assertLessEqual(d['weyl_abs_float'],1)

    def test_error_bound_for_tail_2adic_close_returns(self):
        for k in (9,10,11):
            w=exact_return_witness(self.phases,self.carries,k)
            n=w['n'];q=1<<k
            raw_gap=d_circle(self.phases[n+q],self.phases[n])
            # For actual completed z, the real distance is >= raw_gap - |T_n|-|T_(n+q)|.
            self.assertGreater(raw_gap-Fraction(2,15*(n+1)**2), Fraction(1,5))

if __name__=='__main__': unittest.main()
