"""Original-source exact source/prime/lag tests; float uses are diagnostics only."""
import importlib.util
from pathlib import Path
from fractions import Fraction as F
import unittest
import random
import math

P = Path(__file__).resolve().parents[1] / 'research/2026-11-03/archimedean_oily_shear/oily_shear.py'
SPEC = importlib.util.spec_from_file_location('oily_shear',P)
f = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(f)


class GammaOilyShear(unittest.TestCase):
    def test_original_source_four_poles_polynomial(self):
        for n in range(1,257):
            den=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            self.assertEqual(f.r(n),F(120*n*n-89*n+16,den))
            self.assertGreater(f.r(n),0)
            self.assertLess(f.r(n+1),f.r(n))

    def test_true_source_upper_envelopes(self):
        for n in (1,2,3,17,37,73,137):
            lo,hi=f.tail_interval(n,32)
            self.assertLess(F(0),lo)
            self.assertLess(hi,f.beta_cap(n))
            self.assertLess(hi-lo,F(1,16**30))

    def test_gamma_shear_positive_and_one_order_gain(self):
        for n in (1,3,17,37,73,137):
            for d in (1,3,7,17):
                lo,hi=f.shear_interval(n,d,32)
                self.assertGreater(lo,0)
                self.assertLess(hi, f.shear_cap(n,d))
                self.assertLess(f.shear_cap(n,d),f.shear_cube_cap(n,d))

    def test_completely_monotone_first_finite_differences(self):
        # Finite confirmations only; the all-k statement is paper-proved by the positive integral.
        for d in (1,3,11):
            rows=[f.shear_interval(n,d,32) for n in range(10,20)]
            for (lo1,hi1),(lo2,hi2) in zip(rows,rows[1:]):
                self.assertGreater(lo1,hi2)

    def test_gamma_lag_telescopes(self):
        for A,d in ((37,1),(37,7),(73,17),(137,3)):
            # Sum fixed-depth lower and upper intervals, still a mathematically valid enclosure.
            lowers=[]; uppers=[]
            for n in range(A, A+17):
                lo,hi=f.shear_interval(n,d,24)
                lowers.append(lo);uppers.append(hi)
            self.assertGreater(sum(lowers),0)
            self.assertLess(sum(uppers),f.telescoped_shear_upper(A,d))
            self.assertLessEqual(f.telescoped_shear_upper(A,d),d*f.beta_cap(A))
            self.assertLessEqual(f.uniform_signed_lag_chord_upper(A,d,1),F(44,7)*d*f.beta_cap(A))

    def test_externally_checked_high_precision_pi_identity(self):
        # Validation against pi is explicitly noncertifying and NOT source construction.
        import mpmath as mp
        for n,d in ((17,1),(37,3),(73,7),(137,17)):
            mp.mp.dps=400
            u=f.exact_original_orbit(n+d)
            direct=u[n+d]-u[n]
            phase=(16**d-1)*16**(n-1)*mp.pi
            zz=mp.mpf(direct.numerator)/direct.denominator-phase
            lo,hi=f.shear_interval(n,d,32)
            self.assertGreater(zz,mp.mpf(lo.numerator)/lo.denominator)
            self.assertLess(zz,mp.mpf(hi.numerator)/hi.denominator)

    def test_oily_digamma_square_difference(self):
        # Finite diagnostics of inherited SUCC #474 formula, not a proof of positivity.
        import mpmath as mp
        mp.mp.dps=90
        for n,d in ((3,1),(17,3),(37,7),(73,11)):
            D=lambda x: mp.digamma(x+1)-mp.log(x)
            k=((D(n)**2-D(n+d)**2)/16)
            lo,hi=f.shear_interval(n,d,36)
            self.assertGreater(k,mp.mpf(hi.numerator)/hi.denominator)


class SelectedPrimeRadical(unittest.TestCase):
    def test_prime_window_and_inert_second_event(self):
        for A in (48,96):
            pack=f.clean_passports(A)
            self.assertEqual(len(set(pack['primes'])),len(pack['primes']))
            for p,b in pack['plus']:
                self.assertLessEqual(b,A)
                self.assertGreaterEqual(4*(b-1),pack['end']-1)
            for p,b in pack['minus']:
                self.assertLessEqual(b,A)
                self.assertGreaterEqual((3*b+1)//2,pack['end'])
        self.assertEqual((3*12+1)//2,18)
        self.assertLessEqual((3*11+1)//2,17)
        self.assertNotEqual(f.r(18).denominator%47,1)
        self.assertEqual(f.r(18).denominator%47,0)

    def test_all_pairs_actual_denominator_radical(self):
        for A in (48,96):
            pack=f.clean_passports(A)
            seq=f.exact_original_orbit(pack['end']-1)
            for n in range(A,pack['end']):
                for t in range(n+1,pack['end']):
                    g=f.nonalias_radical(pack,t-n)
                    self.assertEqual(g,f.nonalias_radical_gcd(pack,t-n))
                    for h in (1,3,5,A):
                        diff=h*(seq[t]-seq[n])
                        self.assertEqual(diff.denominator%g,0)

    def test_exact_prime_birth_passports_against_original(self):
        for A in (48,96):
            pack=f.clean_passports(A)
            seq=f.exact_original_orbit(pack['end']-1)
            for n in range(A,pack['end']):
                for kind in ('plus','minus'):
                    for p,b in pack[kind]:
                        z=p*seq[n]
                        self.assertNotEqual(z.denominator%p,0)
                        self.assertEqual(z.numerator*pow(z.denominator,-1,p)%p,
                                         f.selected_prime_residue(p,b,n,kind))

    def test_radical_mass_numeric_is_only_finite_observation(self):
        for A in (48,96,192):
            pack=f.clean_passports(A)
            lower=min(f.nonalias_radical(pack,d) for d in range(1,pack['end']-A))
            self.assertGreater(lower,1)
            self.assertLess(f.strict_exponent(),1)
            self.assertGreater(f.strict_exponent(),0)

    def test_large_denominator_has_no_real_spacing(self):
        # Radical growth by itself cannot forbid extremely close real pairs.
        pack=f.clean_passports(96)
        q=pack['product']
        self.assertTrue(q>1000)
        self.assertLess(f.fraction_close(F(1,q),F(0)),F(1,8))
        self.assertEqual(F(1,q).denominator,q)


class CoherentSameForcingSeed(unittest.TestCase):
    def test_seed_matches_every_p_primary_passport_but_clusters(self):
        for A,m in ((16,8),(32,16)):
            pack=f.clean_passports(A)
            proof=f.positive_seed_counterfeit(A,m,pack)
            self.assertEqual(math.gcd(proof['seed'].denominator,pack['product']),1)
            z=f.verify_rational_seed(pack,proof)
            self.assertEqual(z['occupied_cells'],1)
            self.assertEqual(z['E'],m)
            self.assertEqual(z['window_size'],pack['end']-pack['A'])

    def test_seed_constructed_without_pi_digits(self):
        pack=f.clean_passports(32)
        proof=f.positive_seed_counterfeit(32,8,pack)
        self.assertEqual(proof['q']%pack['product'],1)
        self.assertLess(proof['error_upper'],F(1,10*8))
        self.assertNotEqual(proof['seed'],0)

    def test_invalid_calls(self):
        for fn in (lambda:f.r(0),lambda:f.shear_cap(0,1),
                   lambda:f.shear_interval(1,0),lambda:f.clean_passports(7),
                   lambda:f.positive_seed_counterfeit(16,7),
                   lambda:f.nonalias_radical(f.clean_passports(16),0),
                   lambda:f.uniform_signed_lag_chord_upper(10,1,0)):
            with self.assertRaises(ValueError):fn()


if __name__=='__main__':
    unittest.main()

class CertifiedPiLagWithoutPiDigits(unittest.TestCase):
    def test_circle_interval_endpoint_mutations(self):
        cases=[(F(0),F(1,100),'near'),(F(49,100),F(51,100),'far'),
               (F(-1,100),F(1,100),'near'),(F(11,100),F(12,100),'far'),
               (F(9,100),F(11,100),'ambiguous'),(F(99,100),F(101,100),'near'),
               (F(49,100),F(52,100),'far')]
        for lo,hi,result in cases:
            self.assertEqual(f.interval_circle_near_status(lo,hi,10),result)
        for fn in (lambda:f.interval_circle_near_status(F(1),F(0),8),
                   lambda:f.interval_circle_near_status(F(0),F(1),1)):
            with self.assertRaises(ValueError):fn()

    def test_original_source_pi_near_pair_classification_holdouts(self):
        # Exact real-circle classifications for finite completed pi lags,
        # using rational source states + analytic source tail, NO pi digits.
        for A,mesh in ((37,8),(73,8),(137,16)):
            end=(4*A+2)//3
            seq=f.exact_original_orbit(end-1)
            for n in range(A,end):
                for d in range(1,end-n):
                    rec=f.original_pi_lag_certificate(seq,n,d,mesh,24)
                    self.assertNotEqual(rec['classification'],'ambiguous')
                    self.assertEqual(rec['classification']=='near', rec['original_source_near'])
                    self.assertLess(rec['shear_hi'],f.shear_cap(n,d))

    def test_completed_pi_interval_vs_high_precision_reference(self):
        import mpmath as mp
        mp.mp.dps=290
        for n,d in ((37,3),(73,7),(137,11)):
            seq=f.exact_original_orbit(n+d)
            rec=f.original_pi_lag_certificate(seq,n,d,16,32)
            x=(16**d-1)*16**(n-1)*mp.pi
            self.assertLess(mp.mpf(rec['completed_pi_interval_lo'].numerator)/rec['completed_pi_interval_lo'].denominator,x)
            self.assertGreater(mp.mpf(rec['completed_pi_interval_hi'].numerator)/rec['completed_pi_interval_hi'].denominator,x)


class FiniteGlobalShadow(unittest.TestCase):
    def test_gamma_shadow_bands_and_source_tail_enclosure(self):
        for M,m in ((17,8),(49,16),(113,16),(257,32)):
            s=f.gamma_shadow_horizon(M,m)
            self.assertLess(m*s['certified_displacement_upper'],1)
            self.assertGreaterEqual(m*16**(s['guaranteed_extra_steps']+1)*s['tail_upper'],1)
            self.assertGreater(m*s['two_steps_later_lower'],1)
            lo,hi=f.tail_interval(M,42)
            self.assertLess(s['tail_lower'],lo)
            self.assertGreater(s['tail_upper'],hi)
            for q in range(s['guaranteed_extra_steps']+1):
                low,high=f.completed_pi_interval(M,M+q)
                self.assertLess(high-low,F(1,m))
                self.assertLess(high-low,16**q*s['tail_upper'])

    def test_completed_pi_fractional_phase_without_pi_digits(self):
        import mpmath as mp
        mp.mp.dps=390
        for M,q in ((17,2),(49,3),(113,3),(257,4)):
            low,high=f.completed_pi_interval(M,M+q)
            # This is an independent, explicitly noncertifying reference.
            v=16**(M+q-1)*mp.pi
            l=mp.mpf(low.numerator)/low.denominator
            u=mp.mpf(high.numerator)/high.denominator
            self.assertLess(l,v)
            self.assertLess(v,u)
            self.assertIn(f.certified_phase_bin(M,M+q,16),[*range(16),None])

    def test_original_finite_null_bbpf_prefix_is_positive_but_global_zero(self):
        exact={1:F(2,105),2:F(67,90090),3:F(1443053,42833831040)}
        for n,value in exact.items():self.assertEqual(f.finite_null_radial(n),value)
        for N in range(1,20):
            z=f.finite_null_radial(N)
            self.assertGreater(z,0)
            self.assertLess(z,f.finite_null_radial_upper(N))
            if N>1:self.assertLess(z,f.finite_null_radial(N-1))

    def test_source_prime_clocks_with_completely_coherent_fake_real_cloud(self):
        for A,m in ((48,8),(96,16)):
            pack=f.clean_passports(A)
            ghost=f.rational_ghost_cloud(pack,m)
            self.assertEqual(len(ghost['fake_states']),pack['end']-A)
            self.assertTrue(ghost['matches_all_selected_p_residue_clock_values'])
            self.assertTrue(ghost['all_fake_states_one_mesh_bin'])
            self.assertGreaterEqual(ghost['common_conductor_quotient'],ghost['old_prime_product'])
            self.assertLess(ghost['real_arc_radius_upper'],F(1,5*m))
            self.assertGreater(ghost['coprime_residue_fraction'],F(4,5))
            for n in range(A,pack['end']-1):
                # Local source recurrence survives at every selected p.
                for p in pack['primes']:
                    z=p*(ghost['fake_states'][n+1]-16*ghost['fake_states'][n]-f.r(n+1))
                    self.assertNotEqual(z.denominator%p,0)
                    self.assertEqual(z.numerator*pow(z.denominator,-1,p)%p,0)

    def test_neg_controls_and_invalid(self):
        for fcall in (lambda:f.gamma_tail_lower(0),lambda:f.gamma_shadow_horizon(0,8),
                      lambda:f.gamma_shadow_horizon(5,2**40),
                      lambda:f.finite_null_radial(0),lambda:f.completed_pi_interval(7,-1),
                      lambda:f.rational_ghost_cloud(f.clean_passports(48),7)):
            with self.assertRaises(ValueError):fcall()

class ExactDirectionalFlux(unittest.TestCase):
    def test_oriented_boundary_gains_and_losses_with_endpoints(self):
        m=8;rho=F(1,m);sig=F(1,100)
        table=[(rho,0),(rho+sig,1),(rho+sig+F(1,10000),0),
               (1-rho,-1),(1-rho+sig-F(1,10000),-1),
               (1-rho+sig,0),(F(0),0),(F(1,2),0)]
        for d,wanted in table:
            self.assertEqual(f.oriented_boundary_flux(d,sig,m)['signed_flux'],wanted)

    def test_original_source_lag_oriented_flow_when_certified(self):
        # Source intervals [A,ceil(4A/3)) at the preregistered Gamma holdouts.
        for A,m in ((37,8),(73,8),(137,16)):
            end=(4*A+2)//3
            o=f.exact_original_orbit(end-1)
            signed_total=0
            for n in range(A,end):
                for d in range(1,end-n):
                    low,high=f.shear_interval(n,d,36)
                    self.assertLess(high,F(1,m))
                    c=f.original_pi_lag_certificate(o,n,d,m,36)
                    self.assertNotEqual(c['classification'],'ambiguous')
                    z=f.oriented_boundary_flux(o[n+d]-o[n],(low+high)/2,m)
                    self.assertEqual(z['source_near'],c['original_source_near'])
                    self.assertEqual(z['completed_near'],int(c['classification']=='near'))
                    signed_total+=z['signed_flux']
            self.assertEqual(signed_total,0)  # Observed finite, NOT general theorem.

    def test_original_odd_denominators_far_from_binary_boundaries_2adically(self):
        for A in (48,96):
            o=f.exact_original_orbit((4*A+2)//3)
            for n in range(A,(4*A+2)//3):
                for d in range(1,min(7,(4*A+2)//3-n)):
                    for h in (1,2,7,16):
                        self.assertTrue(f.binary_boundary_is_2adic_unit(h*(o[n+d]-o[n]),8))
        self.assertRaises(ValueError,lambda:f.binary_boundary_is_2adic_unit(F(1,2),8))
