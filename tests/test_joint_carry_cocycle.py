"""Exact new original-source p2/real carry tests; no pi digits or Weyl assertions."""
import importlib.util
import random
import unittest
from fractions import Fraction as Q
from pathlib import Path

PATH=Path(__file__).resolve().parents[1]/'research/2026-11-03/joint_carry_cocycle/joint_carry.py'
SPEC=importlib.util.spec_from_file_location('joint_carry', PATH)
f=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(f)


class OriginalSourceContracts(unittest.TestCase):
    def test_source_HG_is_original_four_pole_exact(self):
        for n in range(1,301):
            self.assertEqual(f.real_source(n)+f.gaussian_source(n), f.original_r(n))
            self.assertEqual(f.depth2(f.original_r(n)),0)
            self.assertEqual(f.v2_rational(f.real_source(n)),-5-f.v2_integer(n))
            self.assertEqual(f.v2_rational(f.gaussian_source(n)),-5-f.v2_integer(n))

    def test_exact_parity_harmonic_injection(self):
        for n in range(1,2501):
            self.assertEqual(f.principal2(f.real_source(n)),f.source_principal_binary(n))
            self.assertEqual(f.principal2(f.gaussian_source(n)),
                             (-f.source_principal_binary(n))%1)

    def test_short_cone_vs_stream_all_small_indices(self):
        for n,h,g in f.principal_cocycle_stream(1024):
            self.assertEqual(h, f.principal_short_cone(n,'H'))
            self.assertEqual(g, f.principal_short_cone(n,'G'))
            self.assertEqual((h+g)%1,0)
            if n:
                self.assertLessEqual(f.depth2(h),f.source_depth_envelope(n))

    def test_harmonic_clock_independent_formula(self):
        # Standalone harmonic/parity evaluator is slower; 8 test horizons.
        for n in (1,2,3,7,16,33,88,255):
            self.assertEqual(f.principal_harmonic_clock(n),f.principal_short_cone(n))

    def test_anchors_all_k_without_full_prefix(self):
        for k in tuple(range(1,32))+(47,89,193):
            self.assertEqual(f.principal_short_cone(1<<k), f.anchor_principal(k)[0])
            self.assertEqual(f.principal_short_cone(1<<k,'G'),f.anchor_principal(k)[1])
            self.assertEqual(f.depth2(f.principal_short_cone(1<<k)),k+5)

    def test_tropical_source_debt_bursts(self):
        for k in list(range(1,41)) + [47,89,193]:
            for d in range(min(10,(k-1)//5+1)):
                n=(1<<k)+d
                pred=f.anchor_window_depth(k,d)
                self.assertEqual(f.depth2(f.principal_short_cone(n)),pred)
                self.assertEqual(f.depth2(f.principal_short_cone(n,'G')),pred)

    def test_p2_depth_envelope_is_globally_sharp(self):
        values=list(f.principal_cocycle_stream(4096))
        for n,h,g in values:
            if n:
                self.assertLessEqual(f.depth2(h),f.source_depth_envelope(n))
                self.assertEqual(f.depth2(h),f.depth2(g))
                if n&(n-1)==0:self.assertEqual(f.depth2(h),f.source_depth_envelope(n))

    def test_source_short_cone_bounds_and_mutation_guards(self):
        for a in (-1, 0):
            with self.assertRaises(ValueError):f.source_memory_horizon(a)
        with self.assertRaises(ValueError):f.real_source(0)
        with self.assertRaises(ValueError):f.principal_short_cone(1,'wrong')
        for n in (1,2,17,257,12289):
            L=f.source_memory_horizon(n)
            self.assertEqual(L,min(n,(f.source_depth_envelope(n)+3)//4))


class SelectedRealCarry(unittest.TestCase):
    def test_local_real_modulus_vs_fraction_oracle(self):
        direct=f.full_zero_seed_channels(85)
        modular=list(f.full_zero_seed_modular(85))
        for (n,a,b,u),(m,x,y,z) in zip(direct,modular):
            self.assertEqual(n,m)
            self.assertEqual((a%1,b%1,u%1),(x,y,z))
            if n:
                self.assertEqual(f.principal2(a),f.principal2(x))
                self.assertEqual(f.real_carry_cocycle(a,b)['carry_difference'],
                                 f.real_carry_cocycle(x,y)['carry_difference'])

    def test_modular_selected_real_gluing_and_boundary_formula(self):
        for n,x,y,u in f.full_zero_seed_modular(384):
            if not n:continue
            cert=f.real_carry_cocycle(x,y)
            self.assertEqual(cert['glued_real_phase'],u)
            self.assertEqual(cert['glued_odd_phase'],u)
            self.assertEqual(cert['carry_difference'],
                             cert['odd_low_crossing']-cert['odd_high_crossing'])
            self.assertEqual(cert['dyadic_gaussian_part'],f.principal_short_cone(n,'G'))

    def test_random_prime_odd_cofactor_general_identity(self):
        rng=random.Random(20261103)
        for _ in range(240):
            k=rng.randrange(1,15)
            dd=1<<k
            a=rng.randrange(1,dd,2)
            u=Q(a,dd)+Q(rng.randrange(-50,51),5)
            v=-Q(a,dd)+Q(rng.randrange(-50,51),7)
            self.assertEqual(f.depth2(u+v),0)
            c=f.real_carry_cocycle(u,v)
            self.assertEqual(c['glued_real_phase'],(u+v)%1)

    def test_source_anchor_real_odd_carry_is_not_identical_general(self):
        # Source n=3 is an EXACT counterexample to naive equality of carries.
        n,x,y,u=list(f.full_zero_seed_modular(5))[3]
        assert n==3
        c=f.real_carry_cocycle(x,y)
        self.assertNotEqual(c['real_carry'],c['odd_carry'])

    def test_coherent_odd_place_counterfeit_zero_boundary_crossings(self):
        for D in (4,5,9,29,79):
            z=f.coherent_odd_counterfeit(D)
            self.assertEqual((z['odd_low_crossing'],z['odd_high_crossing']), (0,0))
            self.assertEqual(z['glued_real_phase'],Q(4,5))
            self.assertEqual(z['dyadic_gaussian_part'],Q(1,1<<D))

    def test_odd_gauge_changes_real_carry_not_phase_or_q2(self):
        a,b=-Q(1,32),Q(1,32)+Q(1,5)
        a2,b2=a+Q(1,5),b-Q(1,5)
        self.assertEqual(a+b,a2+b2)
        self.assertEqual(f.principal2(a),f.principal2(a2))
        self.assertEqual(f.principal2(b),f.principal2(b2))
        self.assertNotEqual(f.real_binary_carry(a,b),f.real_binary_carry(a2,b2))

    def test_odd_phases_are_not_p2_integral_reductions(self):
        a,b=-Q(1,64),Q(1,64)+Q(1,7)
        self.assertEqual(f.glue_odd_character_phase(a,b),Q(1,7))
        with self.assertRaises(ValueError):f.glue_odd_character_phase(a,b-Q(1,128))


class CausalCarryCoboundary(unittest.TestCase):
    def test_all_source_integer_carry_steps_are_one_binary_coboundary(self):
        for cert in f.carry_coboundary_stream(512):
            self.assertIn(cert['carry_coboundary'],(-16,-15,0,1))
            self.assertEqual(cert['carry_coboundary'],
                             cert['next_kappa']-16*cert['old_kappa'])

    def test_source_real_carry_matches_modular_oracle_at_every_time(self):
        receipts=list(f.carry_coboundary_stream(128))
        for n,x,y,u in f.full_zero_seed_modular(128):
            if n==0:continue
            c=receipts[n-1]
            self.assertEqual((c['next_real'],c['next_gaussian'],c['next_original']),
                             (x,y,u))
            self.assertEqual(c['next_kappa'],f.real_binary_carry(x,y))

    def test_incorrect_two_channel_signed_local_formula_is_falsified(self):
        c=next(f.carry_coboundary_stream(1))
        self.assertNotEqual(c['carry_coboundary'],
                            16*c['old_kappa']-c['next_kappa'])


class PrecisionBudget(unittest.TestCase):
    def test_sharp_local_principal_precision_tax(self):
        for k in (1,2,8,17):
            for B in (0,1,3,13):
                d=f.precision_tax_witness(k,B)
                self.assertEqual(d['glued_second'],1<<(k-1))

    def test_original_glued_source_precision_reconstruction(self):
        for n,x,y,u in f.full_zero_seed_channels(85):
            if n==0:continue
            B=f.source_depth_envelope(n)
            for k in (1,2,5,11):
                self.assertEqual(f.scaled_sum_mod(x,y,k,B),
                                 u.numerator*pow(u.denominator,-1,1<<k)%(1<<k))

    def test_real_fractional_part_is_NOT_original_2adic_unwrapped_state(self):
        n,x,y,u=list(f.full_zero_seed_modular(3))[1]
        self.assertEqual(n,1)
        # Original full U_1 = 47/15 (odd 2-adically), but {U_1}=2/15
        # is even 2-adically. Literal integer carry 3 is load-bearing.
        self.assertEqual(u,Q(2,15))
        self.assertEqual(f.original_r(1),Q(47,15))
        self.assertNotEqual(f.scaled_sum_mod(x,y,2,f.source_depth_envelope(n)),
                            f.original_r(1).numerator*pow(f.original_r(1).denominator,-1,4)%4)

    def test_nonintegral_unlegitimized_reductions_rejected(self):
        with self.assertRaises(ValueError):f.scaled_sum_mod(Q(1,16),Q(0),4,1)
        with self.assertRaises(ValueError):f.glue_odd_character_phase(Q(1,8),Q(0))


if __name__=='__main__':unittest.main()
