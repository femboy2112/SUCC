"""Classical Hermite/mixture adversarial source-selection tests with exact proofs."""
import random
import unittest
from fractions import Fraction as Q
from math import factorial
from itertools import product

from observational_succ.shadow_archimedean_tests import (
    GaussianScaleShadow,HermiteShadowImpostor,construct_hermite_impostor,
    hermite_fourier_one,polynomial_eval,relative_mellin_polynomial,
    ShadowSourceError)

class ShadowArchimedeanTests(unittest.TestCase):
    def test_classical_hermite_physicists_h4_h8_exact(self):
        self.assertEqual(hermite_fourier_one(0),(1,))
        self.assertEqual(hermite_fourier_one(1),(12,-96,64))
        self.assertEqual(hermite_fourier_one(2),(1680,-26880,53760,-28672,4096))

    def test_explicit_positive_nongaussian_same_mellin_two(self):
        # Polynomial from 912 H0 -216 H4 + H8
        # P=1024*y*(4*y^3-28*y^2+39*y-6).
        p=(Q(0),Q(-6144),Q(39936),Q(-28672),Q(4096))
        from observational_succ.shadow_archimedean_tests import (
            polynomial_add,polynomial_scale)
        h=polynomial_add(polynomial_add(polynomial_scale(hermite_fourier_one(0),912),
                   polynomial_scale(hermite_fourier_one(1),-216)),hermite_fourier_one(2))
        self.assertEqual(h,p)
        self.assertEqual(relative_mellin_polynomial(h,2),0)
        self.assertEqual(relative_mellin_polynomial(h,4),30720)
        self.assertEqual(polynomial_eval(h,0),0)
        # For y>=7, P>=0; for [0,7], P>=-9_877_504.
        eta=Q(1,20_000_000)
        for y in (Q(0),Q(1,10),Q(1),Q(3),Q(7),Q(100)):
            if y<=7:
                self.assertGreater(1+eta*polynomial_eval(h,y),Q(1,2))
            else:
                self.assertGreater(1+eta*polynomial_eval(h,y),1)
        self.assertNotEqual(1+eta*polynomial_eval(h,1),1)

    def test_construct_canonical_indistinguishable_positive_alternative(self):
        model=construct_hermite_impostor((2,),source_id='test-real-place')
        report=model.checks()
        self.assertEqual(report['fourier_eigenvalue'],1)
        self.assertEqual(report['f_at_zero'],1)
        self.assertEqual(report['integral_f'],1)
        self.assertFalse(report['canonical_gaussian_forced'])
        self.assertEqual(relative_mellin_polynomial(model.polynomial,2),0)
        self.assertEqual(model.ratio_at_y(0),1)
        self.assertGreaterEqual(model.ratio_at_y(3),Q(1,2))

    def test_arbitrary_finite_even_moments_and_finite_point_samples(self):
        for moments,points in [((2,4,6),(Q(1,4),Q(1),Q(2))),
                               ((2,),()),((),(Q(1,2),Q(3,2))),
                               ((2,4,6,8),(Q(1,5),))]:
            model=construct_hermite_impostor(moments,points)
            self.assertNotEqual(model.ratio_at_y(Q(17,13)),1)
            self.assertEqual(tuple(relative_mellin_polynomial(model.polynomial,m)
                                   for m in moments),(0,)*len(moments))
            self.assertTrue(all(polynomial_eval(model.polynomial,y)==0 for y in points))
            for j in range(12):
                self.assertGreaterEqual(model.ratio_at_y(Q(j,2)),Q(1,2))

    def test_any_finite_probes_impostor_generator_seeded(self):
        rng=random.Random(1234)
        for _ in range(30):
            moments=tuple(2*i for i in sorted(rng.sample(range(1,7),rng.randint(0,3))))
            points=tuple(sorted(Q(x,8) for x in rng.sample(range(1,16),rng.randint(0,3))))
            model=construct_hermite_impostor(moments,points)
            self.assertEqual(model.polynomial[0],0)
            self.assertGreater(model.polynomial[-1],0)
            self.assertTrue(model.epsilon>0)
            self.assertEqual(model.ratio_at_y(0),1)

    def test_prevent_forced_positive_impostor_without_margin(self):
        model=construct_hermite_impostor((2,4),(Q(1),))
        with self.assertRaises(ShadowSourceError):
            HermiteShadowImpostor(model.source_id,model.polynomial,10,
                                 model.positivity_cutoff,model.sampled_moments,
                                 model.sampled_y,model.modes)

    def test_noncanonical_normalized_selfdual_gaussian_pair(self):
        f=GaussianScaleShadow('selfdual',(Q(2),Q(1,2)),(Q(1,3),Q(2,3)))
        r=f.moment_shadow()
        self.assertEqual(r['C2'],Q(3,2))
        self.assertEqual(r['variance_gap'],Q(1,2))
        self.assertTrue(r['fourier_selfdual'])
        self.assertEqual(r['triangle_L1_error_upper'],Q(2,3))
        self.assertFalse(r['canonical_gaussian_forced'])

    def test_mellin_moment_one_selects_canonical_within_positive_mixture(self):
        canonical=GaussianScaleShadow('canonical',(Q(1),),(Q(1),))
        out=canonical.moment_shadow()
        self.assertEqual(out['variance_gap'],0)
        self.assertTrue(out['canonical_gaussian_forced'])
        for b in (Q(2),Q(3),Q(5,2)):
            f=GaussianScaleShadow('pair',(b,1/b),(1/(1+b),b/(1+b)))
            o=f.moment_shadow()
            self.assertGreater(o['variance_gap'],0)
            self.assertTrue(o['fourier_selfdual'])
            self.assertLessEqual(o['triangle_L1_error_upper']**2,o['variance_gap'])

    def test_mixture_nonselfdual_requires_separate_provenance(self):
        # Mean b=1 does NOT imply self-Fourier; it still yields a moment gap.
        f=GaussianScaleShadow('non-selfdual',(Q(1,2),Q(3,2)),(Q(1,2),Q(1,2)))
        o=f.moment_shadow()
        self.assertEqual(o['variance_gap'],Q(1,4))
        self.assertFalse(o['fourier_selfdual'])
        with self.assertRaises(ShadowSourceError):
            GaussianScaleShadow('negative',(Q(1),),(Q(-1),))
        with self.assertRaises(ShadowSourceError):
            GaussianScaleShadow('float',(0.5,Q(2)),(Q(1,3),Q(2,3)))

    def test_quantitative_L1_shadow_stability_and_compact_zero_free(self):
        canonical=GaussianScaleShadow('a',(Q(1),),(Q(1),))
        self.assertTrue(canonical.compact_mellin_multiplier_zero_exclusion(10000)['certificate'])
        tiny=Q(1,10**12)
        f=GaussianScaleShadow('mostly canonical',(Q(1),Q(2),Q(1,2)),
                              (1-tiny,tiny/3,2*tiny/3))
        self.assertEqual(f.first_scale_moment,1)
        o=f.moment_shadow()
        self.assertEqual(o['variance_gap'],tiny*Q(1,2))
        self.assertTrue(f.compact_mellin_multiplier_zero_exclusion(2)['certificate'])
        self.assertFalse(f.compact_mellin_multiplier_zero_exclusion(10**9)['certificate'])

    def test_reject_non_normalized_source_moments(self):
        f=GaussianScaleShadow('norm invalid',(Q(2),),(Q(1),))
        with self.assertRaises(ShadowSourceError):
            f.moment_shadow()

if __name__=='__main__':unittest.main()

class ExplicitHermiteMultiplierTests(unittest.TestCase):
    def test_selfdual_multiplier_reflection_and_exact_c2_alias(self):
        from observational_succ.shadow_archimedean_tests import explicit_positive_hermite_multiplier
        for s in (Q(-3),Q(-1),Q(0),Q(1,5),Q(1,2),Q(1),Q(2),Q(3)):
            self.assertEqual(explicit_positive_hermite_multiplier(s),
                             explicit_positive_hermite_multiplier(1-s))
        for s in (-1,0,1,2):
            self.assertEqual(explicit_positive_hermite_multiplier(Q(s)),1)
        self.assertGreater(explicit_positive_hermite_multiplier(Q(4)),1)
