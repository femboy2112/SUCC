"""Independent finite oracles and analytic negative controls for all-places SUCC.

External mpmath.zeta is used ONLY by comparison tests, never in the source
continuation evaluator. Physical attestation and new mathematical priority absent.
"""
import cmath
import math
import unittest
from fractions import Fraction as Q
from itertools import product

import mpmath as mp

from observational_succ.all_places_zeta import (
    PlaceModelError, SourceIndexedPlaceAtlas, additive_character_integer_defect,
    continuation_tail_rational, crt_source, factors, fake_composite_source_contradiction,
    finite_sieve_source_zero_prediction, finite_sieved_dirichlet,
    glued_completed_zeta, glued_unit_sieve, glued_xi,
    local_fractional_part, mobius, model_interaction_mellin_residual,
    place_primes, prime_unit_shell_factor, primitive_self_dual_clock,
    product_formula_rational, ramanujan_crt_factorized, ramanujan_exact,
    rational_place_valuations, source_unit_sieve, squarefree_modulus,
    symmetric_model_mutant, theta_refinement_residual,
    theta_unit_sieve_mobius, theta_units_spatial, theta_units_spectral,
    totient, truncated_omega_zero_leading, two_prime_cube_membership,
    unit_residue_labels, twisted_reflection_defect,
    finite_clock_gaussian_fourier, finite_clock_gaussian_rational_bound,
    analytic_gaussian_fourier,
)

class PlaceSourceTests(unittest.TestCase):
    def test_genuine_primes_only(self):
        self.assertEqual(place_primes([2,3,5,11]),(2,3,5,11))
        for bad in [(6,), (2,2), (5,3), (0,), (1,), (2.0,)]:
            with self.subTest(bad=bad),self.assertRaises(PlaceModelError):
                place_primes(bad)

    def test_product_formula_exhaustive_rational(self):
        seen=0
        for n in range(-40,41):
            if not n:continue
            for d in range(1,25):
                q=Q(n,d)
                self.assertEqual(product_formula_rational(q),1)
                self.assertEqual(product_formula_rational(q),Q(1))
                seen+=1
        self.assertEqual(seen,1920)

    def test_product_formula_negative_wrong_p_adic_sign(self):
        q=Q(3,8)
        v=rational_place_valuations(q)
        wrong=abs(q)
        for p,k in v.items():wrong*=Q(p)**k
        self.assertNotEqual(wrong,Q(1))
        self.assertEqual(product_formula_rational(q),1)

    def test_fractional_local_character(self):
        self.assertEqual(local_fractional_part(Q(7,12),2),Q(1,4))
        self.assertEqual(local_fractional_part(Q(7,12),3),Q(1,3))
        self.assertEqual(local_fractional_part(Q(7,12),5),0)
        self.assertEqual(additive_character_integer_defect(Q(7,12)),0)
        self.assertNotEqual(Q(7,12)-local_fractional_part(Q(7,12),2),0)

    def test_additive_global_character_all_small_fractions(self):
        for num in range(-27,28):
            for den in range(1,18):
                self.assertIsInstance(additive_character_integer_defect(Q(num,den)),int)

    def test_character_missing_place_refuted(self):
        q=Q(7,12)
        remaining=q-local_fractional_part(q,2)
        self.assertNotEqual(remaining.denominator,1)

    def test_crt_and_actual_original_sources(self):
        for residues in product(range(2),range(3),range(5)):
            n,mod=crt_source(residues,(2,3,5))
            self.assertEqual(mod,30)
            self.assertEqual(tuple(n%p for p in (2,3,5)),residues)
        self.assertEqual(len({crt_source(r,(2,3,5))[0] for r in product(range(2),range(3),range(5))}),30)

    def test_reject_incompatible_source_models(self):
        with self.assertRaises(PlaceModelError):crt_source((1,3),(4,6))
        a=SourceIndexedPlaceAtlas('Z',0,'B',(2,))
        b=SourceIndexedPlaceAtlas('Z',0,'B',(3,))
        self.assertEqual(a.join(b).sieve_modulus,6)
        for other in [SourceIndexedPlaceAtlas('alien',0,'B',(3,)),
                      SourceIndexedPlaceAtlas('Z',1,'B',(3,)),
                      SourceIndexedPlaceAtlas('Z',0,'B2',(3,)),
                      SourceIndexedPlaceAtlas('Z',0,'B',(3,),Q(2)),
                      SourceIndexedPlaceAtlas('Z',0,'B',(3,),Q(1),-1),a]:
            with self.subTest(other=other),self.assertRaises(PlaceModelError):
                a.join(other)

    def test_crt_atlas_coherence_all_orders(self):
        base=SourceIndexedPlaceAtlas('zeta',0,'real-selfdual')
        m=[SourceIndexedPlaceAtlas('zeta',0,'real-selfdual',(p,)) for p in (2,3,5)]
        self.assertEqual(base.join(m[0]).join(m[1]).join(m[2]),
                         base.join(m[2]).join(m[1]).join(m[0]))

    def test_local_prime_shells_direct_geometric(self):
        for p in (2,3,5,11):
            for s in (1,2,3):
                a=prime_unit_shell_factor(p,s,6)
                b=sum((Q(1,p**(s*k)) for k in range(7)),Q(0))
                self.assertEqual(a,b)
                self.assertEqual(prime_unit_shell_factor(p,s),Q(p**s,p**s-1))

    def test_fake6_local_factor_refused(self):
        with self.assertRaises(PlaceModelError):prime_unit_shell_factor(6,2)
        with self.assertRaises(PlaceModelError):primitive_self_dual_clock(6,2,0)

    def test_finite_local_fourier_selfdual_orthogonality(self):
        # Independent direct complex DFT: modulus p^(2r), subgroup p^r Z.
        for p,r in ((2,1),(2,2),(3,1),(3,2),(5,1)):
            m=p**(2*r);h=p**r
            for k in range(m):
                direct=sum((cmath.exp(-2j*math.pi*k*x/m) for x in range(0,m,h)),0j)/h
                self.assertAlmostEqual(direct.real,primitive_self_dual_clock(p,r,k),places=9)
                self.assertAlmostEqual(direct.imag,0,places=9)

    def test_mutated_clock_not_selfdual(self):
        p,r=3,2
        modulus=p**(2*r)
        wrong_stride=p**(r+1)
        # normalized sum of wrong H at k=0 is p^(r-1)/p^r, not one
        wrong=sum(1 for _ in range(0,modulus,wrong_stride))/p**r
        self.assertNotEqual(wrong,primitive_self_dual_clock(p,r,0))


class CoupledResidueTests(unittest.TestCase):
    def test_ramanujan_exact_against_independent_character_sum(self):
        for m in range(1,17):
            for k in range(-4,5):
                direct=sum((cmath.exp(2j*math.pi*k*r/m) for r in range(m) if math.gcd(r,m)==1),0j)
                actual=ramanujan_exact(m,k)
                self.assertAlmostEqual(actual,direct.real,places=8)
                self.assertAlmostEqual(direct.imag,0,places=8)

    def test_ramanujan_product_requires_genuine_coprime_primes(self):
        for pp in ((2,3),(2,5),(3,7),(2,3,5)):
            m=squarefree_modulus(pp)
            for k in range(-20,21):
                self.assertEqual(ramanujan_exact(m,k),ramanujan_crt_factorized(pp,k))

    def test_unit_residue_crt_interaction(self):
        m=squarefree_modulus((2,3,5))
        self.assertEqual(m,30)
        self.assertEqual(unit_residue_labels(m),(1,7,11,13,17,19,23,29))
        self.assertEqual(len(unit_residue_labels(m)),totient(m))
        for n in range(1,90):
            self.assertEqual(n in source_unit_sieve(30,90),all(n%p for p in (2,3,5)))

    def test_square_model_cube_complete(self):
        for n in range(1,500):
            self.assertEqual(two_prime_cube_membership(1,2,3,n),int(math.gcd(n,6)==1))
            self.assertEqual(two_prime_cube_membership(5,2,3,n),int(math.gcd(n,30)==1))
        with self.assertRaises(PlaceModelError):two_prime_cube_membership(2,2,3,1)
        with self.assertRaises(PlaceModelError):two_prime_cube_membership(1,2,2,1)

    def test_exact_mobius_formula_for_divisor_indicator(self):
        for m in (2,3,4,6,10,12,30):
            for n in range(1,80):
                direct=int(math.gcd(n,m)==1)
                inc=sum(mobius(d) for d in range(1,m+1) if m%d==0 and n%d==0)
                self.assertEqual(direct,inc)

    def test_fake6_source_distinction(self):
        r=fake_composite_source_contradiction(6)
        self.assertEqual(r['counterexample_integer'],2)
        self.assertEqual(r['genuine_zero_order_at_0'],1)
        self.assertFalse(r['fake_excludes_integer'])
        self.assertTrue(r['genuine_excludes_integer'])
        with self.assertRaises(PlaceModelError):fake_composite_source_contradiction(4)

    def test_fake6_not_actual_prime_model(self):
        actual=[n for n in range(1,25) if math.gcd(n,6)==1]
        fake=[n for n in range(1,25) if n%6!=0]
        self.assertIn(2,fake)
        self.assertNotIn(2,actual)
        self.assertNotEqual(actual,fake)

    def test_source_analytic_refinement_at_theta_level(self):
        for m,p in ((1,2),(1,3),(2,3),(6,5)):
            for t in (Q(1,2),Q(1),Q(2)):
                self.assertLess(abs(theta_refinement_residual(m,p,t,25,50)),mp.mpf('1e-44'))

    def test_spectral_theta_equals_sieve_and_mobius(self):
        for m,K in ((1,60),(2,60),(3,60),(6,70),(30,200)):
            for t in (Q(1,2),Q(1)):
                a=theta_units_spatial(m,t,36,60)
                b=theta_units_spectral(m,t,K,60)
                c=theta_unit_sieve_mobius(m,t,36,60)
                self.assertLess(abs(a-b),mp.mpf('2e-20'))
                self.assertLess(abs(a-c),mp.mpf('1e-48'))

    def test_spectral_missing_phase_mutant(self):
        # Replacing the Ramanujan coefficients with +phi(m) produces a wrong theta.
        mp.mp.dps=45
        m,t=6,mp.mpf('0.8')
        true=theta_units_spectral(m,t,70,45)
        wrong=mp.mpf(totient(m))/(m*mp.sqrt(t))*(1+2*sum((mp.exp(-mp.pi*k*k/(m*m*t)) for k in range(1,70)),mp.mpf(0)))
        self.assertGreater(abs(true-wrong),mp.mpf('.2'))

    def test_dirichlet_sieve_genuine_vs_fake_6(self):
        m=6; N=20;s=2
        direct=sum((Q(1,n**s) for n in range(1,N+1) if math.gcd(n,m)==1),Q(0))
        self.assertEqual(finite_sieved_dirichlet(m,s,N),direct)
        fake=sum((Q(1,n**s) for n in range(1,N+1) if n%m),Q(0))
        self.assertNotEqual(direct,fake)


class FiniteToArchClockTests(unittest.TestCase):
    def test_clock_gaussian_to_arch_integral_with_rational_certificates(self):
        for m,t,R,k,H in ((1,Q(1,2),4,0,8),(1,Q(3,4),8,1,8),
                          (2,Q(1,2),6,1,7),(3,Q(2),6,2,7),
                          (6,Q(1,2),5,2,5),(6,Q(1),12,3,4)):
            val=finite_clock_gaussian_fourier(m,t,R,k,H,65)
            integral=analytic_gaussian_fourier(m,t,k,65)
            bound=finite_clock_gaussian_rational_bound(m,t,R,k,H,24)
            self.assertIsInstance(bound,Q)
            self.assertGreater(bound,0)
            self.assertLess(abs(val-integral),mp.mpf(bound.numerator)/bound.denominator)

    def test_clock_convergence_as_resolution_grows(self):
        errors=[]
        for R in (2,4,8,16):
            approx=finite_clock_gaussian_fourier(1,Q(1,2),R,1,7,65)
            goal=analytic_gaussian_fourier(1,Q(1,2),1,65)
            errors.append(abs(approx-goal))
        self.assertLess(errors[-1],errors[0])
        self.assertLess(errors[-1],mp.mpf('1e-20'))

    def test_bad_fourier_normalization_is_detectable(self):
        exact=analytic_gaussian_fourier(2,Q(1),0,65)
        sampled=finite_clock_gaussian_fourier(2,Q(1),8,0,7,65)
        self.assertLess(abs(exact-sampled),mp.mpf('1e-24'))
        self.assertGreater(abs(exact-sampled*16),mp.mpf('3'))

    def test_missing_periodic_spatial_shells_fails(self):
        exact=analytic_gaussian_fourier(1,Q(1,2),0,65)
        # H=0 would discard most of the real-line source and is refused.
        with self.assertRaises(PlaceModelError):
            finite_clock_gaussian_fourier(1,Q(1,2),8,0,0,65)
        wrong=sum((mp.exp(-mp.pi*mp.mpf('0.5')*(mp.mpf(j)/8)**2)
                   for j in range(8)),mp.mpf(0))/8
        self.assertGreater(abs(wrong-exact),mp.mpf('0.1'))

    def test_observer_nyquist_limit_is_real(self):
        with self.assertRaises(PlaceModelError):
            finite_clock_gaussian_rational_bound(2,Q(1),3,4)
        with self.assertRaises(PlaceModelError):
            finite_clock_gaussian_fourier(2,Q(1),3,4)

    def test_exact_error_does_not_claim_machine_roundoff(self):
        b1=finite_clock_gaussian_rational_bound(1,Q(1),8,1,8,16)
        b2=finite_clock_gaussian_rational_bound(1,Q(1),16,1,8,16)
        self.assertGreater(b1,b2)
        self.assertGreater(b1,0)


class AnalyticInteractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps=55

    @staticmethod
    def reference_completed(s):
        return mp.power(mp.pi,-mp.mpc(s)/2)*mp.gamma(mp.mpc(s)/2)*mp.zeta(s)

    def test_true_global_glued_xi_against_independent_classical_oracle(self):
        for s in (mp.mpf('2.5'),mp.mpc('.3','7'),mp.mpc('-3.2','1.5'),mp.mpc('.7','13')):
            a=glued_xi(s,12,12,60)
            ref=mp.mpf('.5')*s*(s-1)*self.reference_completed(s)
            self.assertLess(abs(a-ref),mp.mpf('1e-43'))

    def test_glued_xi_entire_endpoint_and_symmetry(self):
        self.assertLess(abs(glued_xi(0,12,12,60)-mp.mpf('.5')),mp.mpf('1e-45'))
        self.assertLess(abs(glued_xi(1,12,12,60)-mp.mpf('.5')),mp.mpf('1e-45'))
        for s in (mp.mpc('.1','3'),mp.mpc('-5','4'),mp.mpc('3','11')):
            self.assertLess(abs(glued_xi(s,13,13,60)-glued_xi(1-s,13,13,60)),mp.mpf('1e-45'))

    def test_mellin_identity_in_original_re_gt_1(self):
        for s in (2,mp.mpc('2.7','3')):
            a=glued_completed_zeta(s,12,12,60)
            ref=self.reference_completed(s)
            self.assertLess(abs(a-ref),mp.mpf('1e-43'))

    def test_sieved_continuation_outside_euler_for_several_models(self):
        for m in (2,3,6):
            for s in (mp.mpf('2.5'),mp.mpc('.6','8'),mp.mpc('-3','2')):
                a=glued_unit_sieve(m,s,12,68,60)
                ref=self.reference_completed(s)
                for p in factors(m):ref*=(1-mp.power(p,-s))
                self.assertLess(abs(a-ref),mp.mpf('1e-30'))

    def test_model_to_model_analytic_transport_in_critical_strip(self):
        # Each side is independently constructed from source-indexed theta+Fourier.
        for m,p in ((1,2),(1,3),(2,3),(6,5)):
            for s in (mp.mpc('.4','6'),mp.mpc('-2.5','4')):
                a=model_interaction_mellin_residual(m,p,s,12,120 if m*p==30 else 65,65)
                self.assertLess(abs(a),mp.mpf('1e-23'))

    def test_mutated_refinement_reused_prime_rejected(self):
        with self.assertRaises(PlaceModelError):model_interaction_mellin_residual(2,2,mp.mpf('.5'))
        with self.assertRaises(PlaceModelError):model_interaction_mellin_residual(1,6,mp.mpf('.5'))

    def test_multiplicative_place_reflection_is_twisted_not_naive(self):
        for m in (2,3,6):
            for s in (mp.mpc('.4','6'),mp.mpc('-2','5')):
                a=twisted_reflection_defect(m,s,12,78,65)
                self.assertLess(abs(a),mp.mpf('1e-31'))
                raw=glued_unit_sieve(m,s,12,78,65)-glued_unit_sieve(m,1-s,12,78,65)
                self.assertGreater(abs(raw),mp.mpf('1e-5'))

    def test_local_euler_imaginary_clock_poles_are_sieve_zeros(self):
        # Imaginary clock p^-s=1 produces a ZERO in complementary source.
        # No nontrivial Riemann-zeta zero is used.
        for p in (2,3):
            s=2j*mp.pi/mp.log(p)
            val=glued_unit_sieve(p,s,12,80,67)
            ambient=glued_completed_zeta(s,12,12,67)
            self.assertTrue(mp.isfinite(ambient))
            self.assertLess(abs(val),mp.mpf('1e-36'))

    def test_theta_residue_pole_at_one(self):
        for m in (2,3,6):
            eps=mp.mpf('1e-16')
            val=glued_unit_sieve(m,1+eps,12,68,65)
            self.assertLess(abs(eps*val-mp.mpf(totient(m))/m),mp.mpf('1e-12'))

    def test_non_euler_region_at_zero_prime_vs_two_primes(self):
        mp.mp.dps=68
        a=glued_unit_sieve(2,0,13,70,68)
        b=glued_unit_sieve(3,0,13,70,68)
        c=glued_unit_sieve(6,0,13,70,68)
        self.assertLess(abs(a+mp.log(2)),mp.mpf('1e-38'))
        self.assertLess(abs(b+mp.log(3)),mp.mpf('1e-38'))
        self.assertLess(abs(c),mp.mpf('1e-35'))
        z=mp.mpf('1e-8')
        slope=glued_unit_sieve(6,z,13,70,68)/z
        self.assertLess(abs(slope+mp.log(2)*mp.log(3)),mp.mpf('1e-7'))
        self.assertEqual(finite_sieve_source_zero_prediction((2,3))['order'],1)
        self.assertEqual(finite_sieve_source_zero_prediction((2,))['order'],0)

    def test_fake_six_changes_global_complex_behavior(self):
        # The wrong model treats 6 as ONE independent p; its analytic value at
        # zero would be -log6 instead of the genuine 2+3 source's exact zero.
        self.assertEqual(truncated_omega_zero_leading((2,3))['vanishing_order_at_0'],1)
        fake=-mp.log(6)
        actual=glued_unit_sieve(6,0,12,70,60)
        self.assertGreater(abs(actual-fake),mp.mpf('1.7'))

    def test_uniform_rational_error_bound_at_any_imaginary_frequency(self):
        for m,n,K,M,s in ((2,6,22,6,mp.mpc('-3','50')),
                           (6,8,55,8,mp.mpc('.4','20')),
                           (1,6,18,8,mp.mpc('3','35'))):
            eps=continuation_tail_rational(m,n,K,M,24)
            self.assertIsInstance(eps,Q)
            self.assertGreater(eps,0)
            if m==1:
                # Entire xi bound differs by |s(s-1)|/2 multiplier; compare Λ.
                approx=glued_completed_zeta(s,n,K,65)
                true=self.reference_completed(s)
            else:
                approx=glued_unit_sieve(m,s,n,K,65)
                true=self.reference_completed(s)
                for p in factors(m):true*=1-mp.power(p,-s)
            self.assertLess(abs(approx-true),mp.mpf(eps.numerator)/eps.denominator)

    def test_certificate_denies_unreasonable_cutoffs(self):
        with self.assertRaises(PlaceModelError):continuation_tail_rational(30,2,2,30)
        with self.assertRaises(PlaceModelError):continuation_tail_rational(1,1,1,100)

    def test_finite_rational_sieved_values_match_direct_source(self):
        self.assertEqual(finite_sieved_dirichlet(6,2,8),Q(1)+Q(1,25)+Q(1,49))
        self.assertNotEqual(finite_sieved_dirichlet(2,2,8),finite_sieved_dirichlet(6,2,8))

    def test_finite_sampled_globally_symmetric_mutant(self):
        samples=(Q(2),Q(3),Q(4))
        for x in samples:
            self.assertEqual(symmetric_model_mutant(samples,x),0)
            self.assertEqual(symmetric_model_mutant(samples,1-x),0)
        for x in (Q(1,2),Q(5,2),Q(-5)):
            self.assertEqual(symmetric_model_mutant(samples,x),symmetric_model_mutant(samples,1-x))
        self.assertNotEqual(symmetric_model_mutant(samples,Q(1,2)),0)

    def test_euler_product_has_spurious_imaginary_boundary_poles(self):
        # p^{-s}=1 at s=2*pi*i/log(p); completed Lambda has poles ONLY at 0,1.
        p=2
        s=2j*mp.pi/mp.log(p)
        self.assertLess(abs(1-mp.power(p,-s)),mp.mpf('1e-53'))
        self.assertTrue(mp.isfinite(glued_completed_zeta(s,12,12,60)))

    def test_no_inferred_RH(self):
        # No question about nontrivial zeros is read by any constructive API.
        self.assertEqual(finite_sieve_source_zero_prediction((2,3,5))['order'],2)
        self.assertIn('log(5)',truncated_omega_zero_leading((2,3,5))['leading_coefficient'])


if __name__ == '__main__':
    unittest.main()
