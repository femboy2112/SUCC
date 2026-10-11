"""Hostile exact circle translations: identities, charts, group law, path winding.

Finite computations here use only Fraction arithmetic. Global covering and
winding claims are mathematical lemmas in the research note, not simulations
that execute infinitely many path probes.
"""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.circle_translation import (
    CircleTranslationError, CirclePolynomial, GaussianRational,
    TrigFourierPolynomial, rational_stereographic_chart,
    stereographic_inverse, multiply_circle_points,
    periodic_point_signature, winding_alias_for_rational_samples,
    cross_language_circle_demo,
)


class CircleTranslatorTests(unittest.TestCase):
    def setUp(self):
        self.x, self.y = CirclePolynomial.x(), CirclePolynomial.y()
        self.one = CirclePolynomial.scalar(1)

    def test_polynomial_quotient_circle_relation_and_normal_form(self):
        x, y = self.x, self.y
        self.assertEqual(x*x + y*y, self.one)
        self.assertEqual(y*y, self.one-x*x)
        self.assertEqual(x.power(2)+y.power(2)-self.one, CirclePolynomial())
        self.assertEqual(y.power(3), y-(x*x)*y)
        self.assertEqual(x.power(4)+y.power(4),
                         self.one-(x*x*y*y).scale(2))
        p = CirclePolynomial.from_monomials({
            (2,0): 1,(0,2): 1,(0,0):-1,
        })
        self.assertEqual(p,CirclePolynomial())
        with self.assertRaises(CircleTranslationError):
            x.at_circle(Q(0),Q(0))
        self.assertEqual(x.at_circle(Q(3,5),Q(4,5)),Q(3,5))
        self.assertEqual(y.at_circle(Q(3,5),Q(4,5)),Q(4,5))

    def test_both_languages_translate_exact_identity_and_ring_arithmetic(self):
        x,y = self.x,self.y
        f = ((x+y).power(4)*(x-y).power(3)
             + x.power(5).scale(Q(3,7)) + y.power(4))
        g = y.power(3)-x.power(2).scale(5)+self.one
        F=TrigFourierPolynomial.from_circle(f)
        G=TrigFourierPolynomial.from_circle(g)
        self.assertEqual(TrigFourierPolynomial.from_circle(f+g),F+G)
        self.assertEqual(TrigFourierPolynomial.from_circle(f*g),F*G)
        self.assertEqual(TrigFourierPolynomial.from_circle(f-g),F-G)
        self.assertEqual(F.to_circle(),f)
        self.assertEqual(G.to_circle(),g)
        self.assertEqual((F*G).to_circle(),f*g)
        self.assertEqual(TrigFourierPolynomial.from_circle(x*x+y*y),
                         TrigFourierPolynomial.scalar(1))
        self.assertEqual(TrigFourierPolynomial.from_circle(
                         x*x+y*y-self.one), TrigFourierPolynomial())

    def test_independent_fourier_trig_identity_controls(self):
        c,s=TrigFourierPolynomial.cos(),TrigFourierPolynomial.sin()
        self.assertEqual(c*c+s*s,TrigFourierPolynomial.scalar(1))
        self.assertEqual(c.to_circle(),self.x)
        self.assertEqual(s.to_circle(),self.y)
        self.assertEqual((c*c-s*s).to_circle(),
                         self.x.power(2).scale(2)-self.one)
        self.assertEqual((c*s).scale(2).to_circle(),
                         (self.x*self.y).scale(2))
        with self.assertRaises(CircleTranslationError):
            TrigFourierPolynomial(((1,GaussianRational(1)),))
        with self.assertRaises(CircleTranslationError):
            TrigFourierPolynomial(((0,GaussianRational(0,1)),))
        with self.assertRaises(CircleTranslationError):
            CirclePolynomial.scalar(Q(1,2)).at_circle(0.5,0)

    def test_all_small_monomials_and_products_cross_languages(self):
        monomials=[]
        for i,j in product(range(4),repeat=2):
            f=self.x.power(i)*self.y.power(j)
            monomials.append(f)
            encoded=TrigFourierPolynomial.from_circle(f)
            self.assertEqual(encoded.to_circle(),f)
        # 256 independent multiplication interface checks.
        for f,g in product(monomials, repeat=2):
            self.assertEqual(
                TrigFourierPolynomial.from_circle(f*g),
                TrigFourierPolynomial.from_circle(f)*
                TrigFourierPolynomial.from_circle(g),
            )
        self.assertEqual(len(monomials)**2,256)

    def test_circle_chart_is_exact_but_misses_one_point(self):
        self.assertEqual(rational_stereographic_chart(0),(Q(1),Q(0)))
        self.assertEqual(rational_stereographic_chart(1),(Q(0),Q(1)))
        self.assertEqual(rational_stereographic_chart(-1),(Q(0),Q(-1)))
        self.assertEqual(rational_stereographic_chart(Q(1,2)),(Q(3,5),Q(4,5)))
        for n,d in [(-5,2),(-1,7),(0,1),(1,1),(2,3),(10,1)]:
            t=Q(n,d)
            x,y=rational_stereographic_chart(t)
            self.assertEqual(x*x+y*y,1)
            self.assertEqual(stereographic_inverse(x,y),t)
            self.assertNotEqual((x,y),(Q(-1),Q(0)))
        self.assertIsNone(stereographic_inverse(-1,0))
        with self.assertRaises(CircleTranslationError):
            stereographic_inverse(0,0)
        with self.assertRaises(CircleTranslationError):
            rational_stereographic_chart(float(1))

    def test_rotation_group_operation_has_same_algebra_and_trig_law(self):
        point=rational_stereographic_chart(Q(1,2))
        second=rational_stereographic_chart(Q(1,3))
        self.assertEqual(point,(Q(3,5),Q(4,5)))
        self.assertEqual(second,(Q(4,5),Q(3,5)))
        self.assertEqual(multiply_circle_points(point,second),(Q(0),Q(1)))
        identity=(Q(1),Q(0))
        inverse=(point[0],-point[1])
        self.assertEqual(multiply_circle_points(identity,point),point)
        self.assertEqual(multiply_circle_points(point,inverse),identity)
        for a,b,c in product(
                [rational_stereographic_chart(Q(n,5)) for n in range(-3,4)],
                repeat=3):
            left=multiply_circle_points(multiply_circle_points(a,b),c)
            right=multiply_circle_points(a,multiply_circle_points(b,c))
            self.assertEqual(left,right)
        with self.assertRaises(CircleTranslationError):
            multiply_circle_points((0,0),(1,0))

    def test_finite_quarter_samples_cannot_determine_winding(self):
        times=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
        one=winding_alias_for_rational_samples(1,times)
        self.assertEqual(one.original_turns,1)
        self.assertEqual(one.aliased_turns,5)
        self.assertTrue(one.finite_samples_equal)
        self.assertFalse(one.winding_numbers_equal)
        self.assertEqual(one.exact_winding_difference,4)
        self.assertEqual(one.original_points,one.aliased_points)
        self.assertEqual(one.original_points,(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(0)))
        self.assertFalse(one.physical_infinity_observed)

    def test_general_finite_rational_time_sampling_has_aliasing_construction(self):
        lists=[
            (),
            (Q(0),),
            (Q(0),Q(1)),
            (Q(1,2),Q(2,3),Q(7,10)),
            (Q(-1,7),Q(7,11),Q(5,9),Q(0)),
            tuple(Q(n,12) for n in range(13)),
        ]
        for times in lists:
            for k in range(-3,4):
                witness=winding_alias_for_rational_samples(k,times)
                self.assertTrue(witness.finite_samples_equal)
                self.assertNotEqual(witness.original_turns,witness.aliased_turns)
                self.assertEqual(
                    periodic_point_signature(witness.original_turns,times),
                    periodic_point_signature(witness.aliased_turns,times))
                self.assertGreater(witness.exact_winding_difference,0)
        with self.assertRaises(CircleTranslationError):
            periodic_point_signature(True,(Q(0),))
        with self.assertRaises(CircleTranslationError):
            winding_alias_for_rational_samples(1,(0.5,))

    def test_known_finite_winding_prior_allows_a_discriminating_exact_probe(self):
        # Hypothesis class k in [-K,K]. A single fixed rational time
        # t=1/(2K+1) distinguishes all bounded candidate rotations.
        for bound in range(1,8):
            t=Q(1,2*bound+1)
            sources=range(-bound,bound+1)
            observed=[periodic_point_signature(k,(t,))[0] for k in sources]
            self.assertEqual(len(set(observed)),len(observed))
            # A much larger unbounded winding family defeats that prior.
            self.assertEqual(periodic_point_signature(1,(t,)),
                             periodic_point_signature(2*bound+2,(t,)))

    def test_finite_cardinal_samples_cannot_certify_global_trig_identity(self):
        # cos(theta) and cos(5theta) agree on the four cardinal points but
        # are DISTINCT polynomial/trigonometric functions on the full circle.
        fifth=TrigFourierPolynomial._cos_multiple(5)
        self.assertNotEqual(fifth,self.x)
        cardinal=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1)))
        for x,y in cardinal:
            self.assertEqual(fifth.at_circle(x,y),self.x.at_circle(x,y))
        self.assertNotEqual(fifth.at_circle(Q(3,5),Q(4,5)),Q(3,5))

    def test_demo_declares_boundaries_without_claiming_physical_theorem(self):
        report=cross_language_circle_demo()
        self.assertEqual(report["status"],"EXACT_CIRCLE_POLYNOMIAL_TRIG_TRANSLATOR")
        self.assertTrue(report["coordinate_ring_identity_zero"])
        self.assertTrue(report["trigonometric_polynomial_identity_zero"])
        self.assertTrue(report["group_law_preserved"])
        self.assertTrue(report["identical_finite_phase_samples"])
        self.assertTrue(report["different_true_winding_numbers"])
        self.assertEqual(report["matching_sampled_windings"],[1,5])
        self.assertFalse(report["full_path_observability_proved_by_samples"])
        self.assertFalse(report["general_two_theory_translation_proved"])
        self.assertFalse(report["RH_claimed"])


if __name__=="__main__":
    unittest.main()
