"""Exact-and-adversarial focused regression for zero-origin spectral flux."""
import math
import random
import unittest
from collections import Counter
from fractions import Fraction

from observational_succ.duck_bbp import forcing, tail_interval
from observational_succ.zero_origin_spectral_flux import (
    channel_forcings, certified_zero_orbit, histograms_cyclic,
    histograms_linear, discrepancy_energy, refinement_flux, energy_ladder,
    online_word_surplus, fft_radix_two, spectral_line_summary,
    temporal_flux, spectrum_by_clock_residue, spectral_feedback_toy,
    signed_vdc_energy, de_bruijn_hex, channel_phase_summary,
)
import importlib.util
from pathlib import Path
_EPATH=Path(__file__).resolve().parents[1]/"research/2026-11-08/zero_origin_spectral_flux/experiment.py"
_ESPEC=importlib.util.spec_from_file_location("succ_zero_origin_flux_experiment",_EPATH)
_E=importlib.util.module_from_spec(_ESPEC)
_ESPEC.loader.exec_module(_E)
check_machin_prefix=_E.check_machin_prefix
machin_interval=_E.machin_interval
longest_run=_E.longest_run

class SourceFaithful(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trace=certified_zero_orbit(512)

    def test_original_four_pole_exact(self):
        for n in range(1,257):
            x=Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)
            self.assertEqual(x,forcing(n))
            self.assertEqual(sum(channel_forcings(n)),x)
            self.assertTrue(all(q>0 for q in channel_forcings(n)))

    def test_literal_zero_seed_and_first64(self):
        self.assertEqual(self.trace.seed,0)
        self.assertEqual(''.join('0123456789ABCDEF'[d] for d in self.trace.digits[:64]),
                         '243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89')
        self.assertEqual(self.trace.verified_phase_steps,512)

    def test_strict_digit_tail_certification(self):
        x=Fraction()
        for n in range(1,513):
            x=(16*x+forcing(n))%1
            lo,hi=tail_interval(n,20)
            self.assertEqual(int(16*(x+lo))%16,self.trace.digits[n-1])
            self.assertEqual(int(16*(x+hi))%16,self.trace.digits[n-1])

    def test_independent_machin_bracket(self):
        self.assertEqual(check_machin_prefix(self.trace.digits,128)['verified_digits'],128)
        lo,hi=machin_interval(256,128)
        self.assertLess(lo,Fraction(22,7))
        self.assertGreater(hi,Fraction(3))
        self.assertLess(hi-lo,Fraction(1,16**128))

    def test_all_channels_reconstruct_original_circle(self):
        x=Fraction();s=[Fraction(),Fraction(),Fraction()]
        for n in range(1,513):
            parts=channel_forcings(n)
            x=(16*x+forcing(n))%1
            s=[(16*v+part)%1 for v,part in zip(s,parts)]
            self.assertEqual(sum(s)%1,x)
        self.assertEqual(len(self.trace.channel_phases[0]),512)

    def test_any_unresolved_tail_fails_closed(self):
        with self.assertRaises(ValueError):
            certified_zero_orbit(0)
        with self.assertRaises(ValueError):
            certified_zero_orbit(2,-1)

class SpectralAlgebra(unittest.TestCase):
    def test_exact_debruijn_shallow_flat_deep_nonflat(self):
        seq=de_bruijn_hex(3)
        self.assertEqual(len(seq),4096)
        e=energy_ladder(seq,4)
        self.assertEqual(e['energies'],[0,0,0,15])
        self.assertEqual(e['new_mode_flux'],[0,0,15])
        self.assertEqual(e['support'],[16,256,4096,4096])

    def test_periodic_balanced_flips_at_depth2(self):
        seq=tuple(range(16))*32
        e=energy_ladder(seq,3)
        self.assertEqual(e['energies'][0],0)
        self.assertEqual(e['energies'][1],15)
        self.assertEqual(e['energies'][2],255)

    def test_order_permutation_same_depth1_not_depth2(self):
        seq=tuple(range(16))*16
        sorted_same=tuple(d for d in range(16) for _ in range(16))
        p=energy_ladder(seq,2);q=energy_ladder(sorted_same,2)
        self.assertEqual(p['energies'][0],q['energies'][0])
        self.assertNotEqual(p['energies'][1],q['energies'][1])

    def test_flux_exact_many_mutants(self):
        rng=random.Random(18)
        for n in (4,8,16,31,64,257):
            for mode in range(5):
                seq=tuple(rng.randrange(16) for _ in range(n))
                ladder=energy_ladder(seq,min(4,n))
                self.assertTrue(all(x>=0 for x in ladder['new_mode_flux']))
                for i,e in enumerate(ladder['new_mode_flux']):
                    self.assertEqual(e,ladder['energies'][i+1]-ladder['energies'][i])

    def test_reject_wrong_parent_marginals(self):
        seq=(0,1,2,3,4,5,6,7)
        c=histograms_cyclic(seq,1)
        d=histograms_cyclic(seq,2)
        d[(0,1)]+=1
        with self.assertRaises(ValueError):
            refinement_flux(c,d,8,1)

    def test_exact_linear_arrival_balance(self):
        for seq in ((1,)*31,tuple(range(16))*4,de_bruijn_hex(2)):
            for depth in (1,2,3):
                if depth<=len(seq):
                    v=online_word_surplus(seq,depth)
                    count=histograms_linear(seq,depth)
                    m=sum(count.values())
                    b=16**depth
                    final=Fraction(sum(c*c for c in count.values()))-Fraction(m*m,b)
                    self.assertEqual(v['unscaled_discrepancy_final'],final)
                    self.assertEqual(v['reinforcing']+v['opposing']+v['neutral'],m)

    def test_digit_history_cyclic_vs_linear_boundary(self):
        seq=tuple(range(16))*4
        for k in (1,2,3,4):
            c=histograms_cyclic(seq,k)
            d=histograms_linear(seq,k)
            self.assertEqual(sum(c.values())-sum(d.values()),k-1)

    def test_parseval_pure_line(self):
        # z_n=e(n/16): one frequency bin carries all power.
        vals=[complex(math.cos(2*math.pi*n/16),math.sin(2*math.pi*n/16)) for n in range(16)]
        spec=fft_radix_two(vals)
        self.assertAlmostEqual(abs(spec[1]/16),1,places=12)
        self.assertLess(sum(abs(spec[k])**2 for k in range(16) if k!=1),1e-20)

    def test_fft_invalid(self):
        with self.assertRaises(ValueError):
            fft_radix_two([0]*3)
        with self.assertRaises(ValueError):
            spectral_line_summary([0]*16,0)

    def test_all_character_modes_detect_uniform_marginal(self):
        seq=tuple(range(16))*16
        self.assertAlmostEqual(spectral_line_summary(seq,1)['dc_power'],0,places=12)
        self.assertAlmostEqual(spectral_line_summary((1,)*256,1)['dc_power'],1,places=12)

    def test_periodic_spectral_line(self):
        seq=tuple(range(16))*16
        s=spectral_line_summary(seq,1)
        self.assertAlmostEqual(s['largest_nonzero_power'],1,places=12)
        self.assertEqual(s['largest_nonzero_index'],16)
        self.assertAlmostEqual(s['power_at_period_16'],1,places=12)

    def test_signed_temporal_flux_reinforcement(self):
        seq=tuple(range(16))*16
        s=temporal_flux(seq,1,16,1)
        self.assertAlmostEqual(s['terminal_power'],1,places=12)
        self.assertAlmostEqual(s['mean_signed_work'],len(seq)/2,places=8)
        flat=temporal_flux((0,)*256,1,16,1)
        self.assertLess(flat['terminal_power'],1e-20)

    def test_stratified_periodic_bias_even_with_flat_global(self):
        seq=tuple(range(16))*16
        self.assertAlmostEqual(spectrum_by_clock_residue(seq,16)['max_within_class_digit_bias'],15/16)

    def test_toy_beta_zero_equals_uniform_baseline(self):
        rng=random.Random(1122)
        naive=tuple(min(15,int(rng.random()*16)) for _ in range(100))
        self.assertEqual(spectral_feedback_toy(100,seed=1122,beta=0),naive)

    def test_toy_does_not_forbid_clumps(self):
        seq=spectral_feedback_toy(4096,seed=42,beta=.65)
        self.assertTrue(all(0<=d<=15 for d in seq))
        self.assertGreater(longest_run(seq),1)
        self.assertLess(spectral_line_summary(seq,1)['largest_nonzero_power'],1)

    def test_source_joint_not_product_of_marginals(self):
        t=certified_zero_orbit(128)
        q=channel_phase_summary(t)
        self.assertGreater(q['factorization_residual_modulus'],0.01)

    def test_signed_original_orbit_lag_equal_two_implementations(self):
        t=certified_zero_orbit(128)
        for h in (1,2,7):
            for H in (1,2,4,8,32,64):
                r=signed_vdc_energy(t.orbit_phases,h,H)
                self.assertGreaterEqual(r['signed_energy'],-1e-9)
                self.assertLessEqual(r['weyl_power'],r['vdc_upper_bound']+1e-10)

    def test_no_false_coherent_decay(self):
        phases=(0.,)*128
        for H in (1,2,8,64):
            z=signed_vdc_energy(phases,1,H)
            self.assertAlmostEqual(z['weyl_power'],1,places=10)
            self.assertGreater(z['signed_energy'],0.5)

if __name__=='__main__':
    unittest.main()
