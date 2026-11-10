"""Source-mutant, exact arithmetic and hostile seed checks for ASG front."""
import cmath
import unittest
from fractions import Fraction as F
from math import pi
from observational_succ import duck_bbp
from observational_succ.adelic_scale_gluing import (
 source_defect,cocycle,leading_scale,harmonic_coefficient,normalized_defect,
 rational_second_order_residual,residual_bound,log_remainder_bound,
 source_counterseed,finite_place_valuations,finite_place_product,weyl_variation_upper,
 source_numerator_from_one_finite_place,four_pole_denominator,
)


def independent_four_poles(n):
    a=8*n-7
    return F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)


def matched_four_pole_mutant(n):
    a=8*n-7
    # Coefficient perturbation (1,0,-5,4)/10 preserves the 1/n^2 jet.
    return F(41,10*a)-F(2,a+3)-F(3,2*(a+4))-F(3,5*(a+5))


class AdelicScaleGluing(unittest.TestCase):
    def test_source_same_as_independent_four_poles(self):
        for n in list(range(1,200))+[10000,100000]:
            self.assertEqual(duck_bbp.forcing(n),independent_four_poles(n))

    def test_source_rejects_pole_mutant(self):
        for n in [1,2,3,4,5,16,100,500]:
            self.assertNotEqual(duck_bbp.forcing(n),matched_four_pole_mutant(n))

    def test_source_defect_vs_orbit(self):
        for seed in [F(0),F(1,7),-F(5,3)]:
            for n in range(0,12):
                for k in [1,2,3,5]:
                    u1=duck_bbp.lifted_orbit(n+k)+16**(n+k)*seed
                    u0=duck_bbp.lifted_orbit(n)+16**n*seed
                    self.assertEqual(u1-16**k*u0,source_defect(n,k))

    def test_two_path_cocycle(self):
        for n in [0,1,8,19,71]:
            for j in [1,2,4]:
                for k in [1,3,6]:
                    self.assertEqual(*cocycle(n,j,k))

    def test_leading_and_beta_exact_formula(self):
        for k in range(1,17):
            weights=[16**(k-j) for j in range(1,k+1)]
            mass=sum(weights)
            average=F(sum(j*w for j,w in enumerate(weights,1)),mass)
            a,b=F(15,64),F(151,512)
            self.assertEqual(a*mass,leading_scale(k))
            self.assertEqual(b/a-2*average,harmonic_coefficient(k))
            self.assertLess(harmonic_coefficient(k),0)
            self.assertGreater(harmonic_coefficient(k),F(-7,8))

    def test_uniform_all_scales_rational_bound(self):
        # Exact-rational verification; no asymptotic floats or symbolic shortcuts.
        for n in [1,2,3,8,16,31,64,127,255,1024]:
            for k in [1,2,3,4,8,16,24,48]:
                r=rational_second_order_residual(n,k)
                self.assertLessEqual(abs(r),residual_bound(n),(n,k,r))

    def test_pole_mutant_is_discriminated_by_beta(self):
        # Same 1/n^2 coefficient, but true b/a jumps by precisely 1/60.
        for n in [8,32,256,8192]:
            for k in [1,3,5]:
                fm=sum((16**(k-j)*matched_four_pole_mutant(n+j) for j in range(1,k+1)), F(0))
                rm= fm*F(64*n*n,16**k-1)
                self.assertLessEqual(abs(rm-1-(harmonic_coefficient(k)+F(1,60))/n),F(15,n*n))

    def test_finite_place_product_exact(self):
        for value in [F(3,28),F(-100,21),F(1),F(81,125),source_defect(1,1),source_defect(2,2),source_defect(4,3)]:
            v=finite_place_valuations(value)
            self.assertEqual(finite_place_product(value)*abs(value),1)
            self.assertEqual(sum(e for p,e in v.items() if p<2),0)

    def test_invalid_inputs_fail_closed(self):
        bad=[(-1,1),(1,0),(1,-2),(1.5,1),(True,1)]
        for n,k in bad:
            with self.assertRaises(ValueError): source_defect(n,k)
        with self.assertRaises(ValueError): normalized_defect(0,1)
        with self.assertRaises(ValueError): log_remainder_bound(15)
        with self.assertRaises(ValueError): finite_place_valuations(F(0))

    def test_dyadic_seed_odd_p_integral(self):
        for A in [4,8,16,32]:
            seed,ub=source_counterseed(A)
            self.assertEqual(seed.denominator&(seed.denominator-1),0)
            self.assertGreater(seed, -F(4))
            self.assertLess(seed,0)
            self.assertGreater(ub,0)
            # Exact selected real orbit for the epoch is close to zero.
            observed=sum((abs(duck_bbp.lifted_orbit(n)+16**n*seed) for n in range(A,2*A)),F(0))/A
            self.assertLessEqual(observed,ub,(A,float(observed),float(ub)))
            self.assertLess(ub,F(1,3))

    def test_weyl_variation_abel_independently(self):
        # This test checks the generic Abel bound against a directly measured
        # a_n b_n product; the source p-primary test is a separate receipt.
        for L in [3,7,32]:
            aa=[cmath.exp(2j*pi*(n*n%L)/L) for n in range(L)]
            bb=[cmath.exp(2j*pi*((n+1)*3%(L+2))/(L+2)) for n in range(L)]
            prefix=max(abs(sum(aa[:j])) for j in range(1,L+1))
            actual=abs(sum(a*b for a,b in zip(aa,bb)))/L
            self.assertLessEqual(actual,weyl_variation_upper(prefix,tuple(bb))+1e-12)


    def test_actual_finite_place_pins_continuous_rational_source(self):
        # Not just interpolation of arbitrary floats: exact 41-adic 2-digit
        # samples + fixed D and degree/height certificate recover coefficients.
        a,b,c=source_numerator_from_one_finite_place(41,2,120)
        self.assertEqual((a,b,c),(120,-89,16))
        for n in [1,2,3,4,7,31,10000]:
            self.assertEqual(F(a*n*n+b*n+c,four_pole_denominator(n)),duck_bbp.forcing(n))

    def test_finite_place_precision_and_poles_fail_closed(self):
        for args in [(41,1,120),(7,4,120),(2,20,120),(1,20,120)]:
            with self.assertRaises(ValueError): source_numerator_from_one_finite_place(*args)
        mutated=(duck_bbp.forcing(1),duck_bbp.forcing(2),duck_bbp.forcing(3)+F(41**2))
        # A perturbation invisible modulo 41^2 CANNOT be distinguished at
        # the declared finite precision: honest loss of resolution.
        self.assertEqual(source_numerator_from_one_finite_place(41,2,120,mutated),(120,-89,16))
        visible=(duck_bbp.forcing(1),duck_bbp.forcing(2),duck_bbp.forcing(3)+F(1,four_pole_denominator(3)))
        with self.assertRaises(ValueError):
            source_numerator_from_one_finite_place(41,2,120,visible)

    def test_source_seed_independent_pressure(self):
        # A nonnormal coherent completion and zero seed share ALL source defects.
        for A in [4,8,16]:
            s,_=source_counterseed(A)
            for n in range(A,2*A):
                u=duck_bbp.lifted_orbit(n)+16**n*s
                u2=duck_bbp.lifted_orbit(n+2)+16**(n+2)*s
                self.assertEqual(u2-256*u,source_defect(n,2))

if __name__=='__main__': unittest.main()
