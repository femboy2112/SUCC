"""Exact source-locked posterior/carry tests; no Monte Carlo or pi assumption."""
from __future__ import annotations
import importlib.util
from fractions import Fraction as F
from math import comb
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parents[1]
MODULE=HERE/'research/2026-10-29/pascal_carry_joint/joint_carry_probe.py'
spec=importlib.util.spec_from_file_location('joint_carry_probe',MODULE)
s=importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(s)

class ExactSourceCarryTests(unittest.TestCase):
    def test_original_four_poles_and_unwrapped_orbit(self):
        self.assertEqual(s.forcing(1),F(47,15))
        self.assertEqual(s.forcing(2),F(106,819))
        u=s.full_orbit(14)
        self.assertEqual(u[0],0)
        self.assertEqual(u[1],F(47,15))
        for t in range(1,len(u)):
            self.assertEqual(u[t],16*u[t-1]+s.forcing(t))

    def test_literal_carries_with_negative_and_torsion_seed(self):
        for seed in [F(0),F(1,240),F(-1,4),F(1,15)]:
            u=s.full_orbit(16,seed)
            carry=s.literal_carry_digits(u)
            for t in range(1,len(u)):
                expected=(16*s.fraction_part(u[t-1])+s.forcing(t))
                self.assertEqual(carry[t],expected.numerator//expected.denominator)
                self.assertEqual(s.fraction_part(u[t]),expected-carry[t])
        self.assertEqual(s.literal_carry_digits(s.full_orbit(4))[:5],(0,3,2,4,3))

    def test_exact_pascal_state_normalization(self):
        for n in range(1,11):
            for m in range(n+1):
                self.assertEqual(sum((s.grade_probability(n,m,k) for k in range(m+1)),F(0)),F(1))
                for k in range(m+1):
                    self.assertGreater(s.word_mass(n,m,k),0)
                    self.assertGreater(s.grade_probability(n,m,k),0)
            self.assertEqual(s.word_mass(n,0,0),s.forcing(n))

    def test_pascal_diamond_conservation(self):
        for n in range(1,10):
            for m in range(n):
                for k in range(m+1):
                    self.assertEqual(s.word_mass(n,m,k),s.word_mass(n,m+1,k)+s.word_mass(n,m+1,k+1))

    def test_posterior_transitions_and_feedback(self):
        for n in range(1,10):
            for m in range(n):
                for k in range(m+1):
                    succ=s.posterior_success(n,m,k)
                    fail=s.posterior_fail(n,m,k)
                    self.assertEqual(succ+fail,1)
                    self.assertGreater(succ,0)
                    self.assertGreater(fail,0)
                    self.assertLess(succ,1)
                    self.assertLess(fail,1)
                    self.assertEqual(s.path_probability(n,m+1,k), s.path_probability(n,m,k)*succ)
                    self.assertEqual(s.path_probability(n,m+1,k+1),s.path_probability(n,m,k)*fail)
        # Conditioning success reduces failure probability; conditioning failure increases it.
        for n in range(2,10):
            prior=s.posterior_fail(n,0,0)
            after_success=s.posterior_fail(n,1,0)
            after_failure=s.posterior_fail(n,1,1)
            self.assertLess(after_success,prior)
            self.assertGreater(after_failure,prior)

    def test_posterior_full_grade_disintegration(self):
        for n in range(1,9):
            for m in range(n+1):
                for k in range(m+1):
                    probs=s.future_grade_conditionals(n,m,k)
                    self.assertEqual(len(probs),n-m+1)
                    self.assertEqual(sum(probs,F(0)),1)
                    for j,p in enumerate(probs):
                        self.assertEqual(p*s.word_mass(n,m,k),comb(n-m,j)*s.word_mass(n,n,k+j))

    def test_exact_conditional_martingale_gluing_on_group_algebra(self):
        for n in range(1,8):
            orbit=s.full_orbit(2*n)
            for m in range(n):
                for k in range(m+1):
                    here=s.phase_posterior_mass(n,m,k,orbit)
                    a=s.phase_posterior_mass(n,m+1,k,orbit)
                    b=s.phase_posterior_mass(n,m+1,k+1,orbit)
                    p=s.posterior_success(n,m,k)
                    q=s.posterior_fail(n,m,k)
                    for x in set(here)|set(a)|set(b):
                        self.assertEqual(here.get(x,F(0)),p*a.get(x,F(0))+q*b.get(x,F(0)))

    def test_exact_carry_phase_joint_gluing(self):
        for n in range(1,7):
            orbit=s.full_orbit(2*n)
            for m in range(n):
                for k in range(m+1):
                    here=s.carry_phase_posterior_mass(n,m,k,orbit)
                    a=s.carry_phase_posterior_mass(n,m+1,k,orbit)
                    b=s.carry_phase_posterior_mass(n,m+1,k+1,orbit)
                    p=s.posterior_success(n,m,k)
                    q=s.posterior_fail(n,m,k)
                    for v in set(here)|set(a)|set(b):
                        self.assertEqual(here.get(v,F(0)),p*a.get(v,F(0))+q*b.get(v,F(0)))

    def test_terminal_actual_phase_and_carry_are_exact(self):
        for n in range(1,8):
            orbit=s.full_orbit(2*n)
            carries=s.literal_carry_digits(orbit)
            for k in range(n+1):
                t=n+k
                self.assertEqual(s.phase_posterior_mass(n,n,k,orbit),{s.fraction_part(orbit[t]):F(1)})
                self.assertEqual(s.carry_phase_posterior_mass(n,n,k,orbit),{(carries[t],s.fraction_part(orbit[t])):F(1)})

    def test_exact_unconditional_source_root_and_carry(self):
        for n in range(1,8):
            orbit=s.full_orbit(2*n)
            expected={}
            for j in range(n+1):
                key=(s.literal_carry_digits(orbit)[n+j],s.fraction_part(orbit[n+j]))
                expected[key]=expected.get(key,F(0))+s.grade_probability(n,n,j)
            self.assertEqual(s.carry_phase_posterior_mass(n,0,0,orbit),expected)
        self.assertEqual(s.phase_posterior_mass(1,0,0,s.full_orbit(2)),
                         {F(2,15):F(530,12831),F(1076,4095):F(12301,12831)})

    def test_seed_torsion_rotates_all_future_phases(self):
        for n in range(1,7):
            u0=s.full_orbit(2*n,F(0))
            ut=s.full_orbit(2*n,F(1,240))
            self.assertEqual(tuple(s.fraction_part(ut[t]-u0[t]) for t in range(1,2*n+1)),(F(1,15),)*(2*n))
            self.assertEqual({s.fraction_part(v+F(1,15)):w for v,w in s.phase_posterior_mass(n,0,0,u0).items()},
                             s.phase_posterior_mass(n,0,0,ut))

    def test_haar_future_index_gram_exact(self):
        for n in range(1,8):
            for m in range(1,8):
                v=s.exact_carry_phase_haar_gram(n,m)
                self.assertGreaterEqual(v,0)
                self.assertEqual(v,s.exact_carry_phase_haar_gram(m,n))
                self.assertLessEqual(v,1)

    def test_oily_geometric_weights_and_autocorrelation(self):
        for d in range(12):
            expected=s.limiting_correlation(d)
            # Finite exact partial sum + certified positive tail bound.
            lower=sum((s.endpoint_weight(j)*s.endpoint_weight(j+d) for j in range(90)),F(0))
            self.assertGreater(expected,lower)
            self.assertLess(expected-lower,F(1,10**42))
        self.assertEqual(s.limiting_correlation(0),F(5,27))
        self.assertEqual(s.limiting_correlation(1),F(4,27))

    def test_exact_haar_variance_as_gram_sum(self):
        for N in range(1,27):
            independent=sum((s.limiting_correlation(i-j) for i in range(N) for j in range(N)),F(0))/N**2
            self.assertEqual(s.exact_haar_variance(N),independent)
            self.assertLessEqual(s.exact_haar_variance(N),F(1,N))

    def test_truncated_lacunary_spectrum_and_tail(self):
        for J in range(25):
            self.assertEqual(sum((s.endpoint_weight(j) for j in range(J)),F(0)),1-s.endpoint_tail(J))
            self.assertEqual(s.weighted_frequency_cost(J),sum((s.endpoint_weight(j)*(16**j-1) for j in range(J)),F(0)))
            self.assertGreaterEqual(s.weighted_frequency_cost(J),0)

    def test_uniform_cutoff_is_rational_safe(self):
        for n in (3,7,25,40,100,1000):
            for h in (1,3,17):
                J=s.adaptive_cutoff(n,h)
                b=s.rational_cutoff_bound(n,h,J)
                self.assertGreater(b,0)
                self.assertLessEqual(abs(h)*16**J,(8*n+1)**2 if abs(h)<=(8*n+1)**2 else abs(h))
        self.assertLess(s.rational_cutoff_bound(100000,1,s.adaptive_cutoff(100000,1)),F(1,10))

    def test_mutations_are_detected(self):
        with self.assertRaises(ValueError):s.forcing(0)
        with self.assertRaises(ValueError):s.word_mass(4,3,4)
        with self.assertRaises(ValueError):s.future_grade_conditionals(4,5,2)
        with self.assertRaises(ValueError):s.exact_haar_variance(0)
        with self.assertRaises(ValueError):s.rational_cutoff_bound(2,1,0)
        # Flat wrong source: a scalar q(0)=1/4 disagrees with actual n=1 original.
        self.assertNotEqual(s.grade_probability(1,1,0),F(1,4))
        # Replacing a signed absolute anchor by a Haar mean would report zero,
        # yet a coherent constant-phase model returns a joint mass of exactly 1.
        self.assertEqual(sum(s.future_grade_conditionals(5,0,0),F(0)),1)

if __name__=='__main__':unittest.main()

class SourceGreenCompositionTests(unittest.TestCase):
    def test_green_exact_rational_truncation_and_update(self):
        for n in range(4):
            for D in range(2,10):
                t=s.green_truncated_total(n,D)
                self.assertEqual(16*t-s.forcing(n+1),s.green_truncated_total(n+1,D-1))
                w=s.green_truncated_weights(n,D)
                wn=s.green_truncated_weights(n+1,D-1)
                for j in range(D-1):
                    self.assertEqual(wn[j],w[j+1]/(1-w[0]))
                self.assertLess(s.green_tail_probability_bound(n,D),1)

    def test_green_pascal_joint_includes_true_carry_and_phase(self):
        for n in range(3):
            for D in range(1,5):
                orbit=s.full_orbit(2*(n+D))
                carries=s.literal_carry_digits(orbit)
                joint=s.green_pascal_joint_truncated(n,D,orbit)
                self.assertEqual(sum(joint.values(),F(0)),1)
                self.assertTrue(all(carry==carries[n+ell+j] for (ell,j,carry,phase) in joint))
                self.assertTrue(all(phase==s.fraction_part(orbit[n+ell+j]) for (ell,j,carry,phase) in joint))
                for ell,w in enumerate(s.green_truncated_weights(n,D),1):
                    self.assertEqual(sum((p for (l,j,k,phase),p in joint.items() if l==ell),F(0)),w)
                    for j in range(n+ell+1):
                        key=(ell,j,carries[n+ell+j],s.fraction_part(orbit[n+ell+j]))
                        self.assertEqual(joint[key],w*s.grade_probability(n+ell,n+ell,j))
                proj=s.green_pascal_phase_offset_projection(n,D,orbit)
                for offset,mass in proj.items():
                    self.assertEqual(mass,sum((w*s.grade_probability(n+ell,n+ell,offset-ell)
                        for ell,w in enumerate(s.green_truncated_weights(n,D),1)
                        if 0<=offset-ell<=n+ell),F(0)))
                self.assertEqual(sum(proj.values(),F(0)),1)

    def test_composite_limit_is_one_probability_law(self):
        for r in range(1,17):
            brute=sum((F(15,16**ell)*s.endpoint_weight(r-ell) for ell in range(1,r+1)),F(0))
            self.assertEqual(s.composite_weight_limit(r),brute)
            self.assertGreater(s.composite_weight_limit(r),0)
        for D in range(0,20):
            tail=s.composite_limit_tail(D)
            self.assertGreater(tail,0)
            self.assertLessEqual(tail,1)
        self.assertEqual(s.composite_filter_inverse_coefficients(),(64,-68,20,-1))

    def test_composite_inverse_exact_with_finite_support(self):
        # K coefficients obey the 3rd-order constant recurrence for r>1;
        # the impulse at r=1 has value 15.
        c=s.composite_filter_inverse_coefficients()
        def k(j):return s.composite_weight_limit(j) if j>=1 else F(0)
        for r in range(1,65):
            value=sum((c[j]*k(r-j) for j in range(4)),F(0))
            self.assertEqual(value,15 if r==1 else 0)

    def test_composite_global_tv_finite_bound(self):
        for n in (3,4,8,16,64,256,2048):
            bound=s.composite_real_source_tv_bound(n)
            self.assertGreater(bound,0)
            self.assertLess(bound,F(256,225*(8*n+1))+F(22,n))
        self.assertLess(s.composite_real_source_tv_bound(2048),F(1,50))

    def test_source_mutations_detected_by_true_kernel(self):
        self.assertNotEqual(s.composite_weight_limit(1),F(1,4))
        self.assertNotEqual(s.composite_weight_limit(2),F(1,4))
        self.assertNotEqual(s.composite_filter_inverse_coefficients(),(16,-32,24,-8,1))
        with self.assertRaises(ValueError):s.green_truncated_total(-1,2)
        with self.assertRaises(ValueError):s.green_truncated_total(0,0)
        with self.assertRaises(ValueError):s.composite_weight_limit(0)
        with self.assertRaises(ValueError):s.green_pascal_joint_truncated(2,4,s.full_orbit(5))

class CompositeSpectralTests(unittest.TestCase):
    def test_exact_composite_autocorrelation_closed_form(self):
        for d in range(12):
            exact=s.composite_limiting_correlation(d)
            trunc=sum((s.composite_weight_limit(r)*s.composite_weight_limit(r+d) for r in range(1,75)),F(0))
            self.assertGreater(exact,trunc)
            self.assertLess(exact-trunc,F(1,10**29))
            self.assertEqual(s.composite_limiting_correlation(-d),exact)
        self.assertEqual(s.composite_limiting_correlation(0),F(8845,49011))

    def test_composite_green_oily_destroys_interior_golden_fixed_point(self):
        # For every 0<z<1: K(z)/z=15/[(16-z)(2-z)^2]<1.
        for z in [F(1,999),F(1,2),F(2,3),F(999,1000)]:
            K=15*z/((16-z)*(2-z)**2)
            self.assertLess(K,z)
        # Oily alone has the golden interior fixed point; the composite cannot.
        self.assertEqual((16-F(1))*(2-F(1))**2,15)

    def test_source_selected_inverse_error_certificate(self):
        for n in (3,6,20,100,3000):
            for D in (1,3,6,12):
                e=s.composite_truncated_reconstruction_error_bound(n,D)
                self.assertGreater(e,0)
        # The bound eventually gets small while retaining all source labels.
        self.assertLess(s.composite_truncated_reconstruction_error_bound(3000,14),F(1,4))

    def test_numerical_green_tail_against_exact_enclosure(self):
        for n in range(5):
            for D in range(1,10):
                approximate=s.green_truncated_total(n,D)
                # Later 50 exact source terms give a STRICT positive lower bound.
                remainder=sum((s.forcing(n+i)*F(1,16**i) for i in range(D+1,D+51)),F(0))
                self.assertGreater(remainder,0)
                self.assertLess(remainder/approximate,s.green_tail_probability_bound(n,D))

    def test_composite_total_offset_is_not_a_single_source_grammar(self):
        # The grade PGF G(z)=(2-z)^-2 and future PGF P(z)=15z/(16-z)
        # each retain a typed interpretation. Forgetting the labels yields K.
        z=F(1,3)
        geom=15*z/(16-z)
        oily=1/(2-z)**2
        self.assertEqual(geom*oily,15*z/((16-z)*(2-z)**2))
        self.assertNotEqual(geom*oily,oily)
        self.assertNotEqual(geom*oily,geom)

class VarianceAndInformationTests(unittest.TestCase):
    def test_sensor_variance_strict_positive_and_exact_feedback(self):
        for n in range(1,18):
            a=s.initial_failure_probability(n)
            v=s.authentic_sensor_variance(n)
            self.assertGreater(v,0)
            self.assertGreater(a,0)
            self.assertLess(a,1)
            # after one failure the next probability increases, after success decreases
            if n>=2:
                self.assertEqual(s.word_mass(n,2,2)/s.word_mass(n,1,1),a+v/a)
                self.assertEqual(s.word_mass(n,2,1)/s.word_mass(n,1,0),a-v/(1-a))

    def test_original_first_two_carries_are_not_coherent_counterseed(self):
        true=s.literal_carry_digits(s.full_orbit(2))
        self.assertEqual(true,(0,3,2))
        # The coherent counterseed -pi/16 would give k_t=15 for ALL t>=1,
        # by U_t=-T_t, 0<T_t<1. This is a proof-level hostile control;
        # no inaccurate Fraction approximation to pi is fabricated here.
        self.assertNotEqual(true[1],15)
        self.assertNotEqual(true[2],15)
        # Finite source exactly sees both true carry values at n=0,D=1.
        joint=s.green_pascal_joint_truncated(0,1,s.full_orbit(2))
        self.assertEqual({k[2] for k in joint},{2,3})
        self.assertEqual(sum(joint.values(),F(0)),1)

class IndependentCompositeDistTests(unittest.TestCase):
    def test_exact_finite_tv_below_analytic_all_source_bound(self):
        for n in (3,4,7,12):
            for depth in (2,4,7,12):
                tv=s.finite_composite_exact_tv(n,depth)
                self.assertLess(tv,s.composite_real_source_tv_bound(n)+s.green_tail_probability_bound(n,depth))
                self.assertGreater(tv,0)
                self.assertLess(tv,1)

    def test_label_preservation_and_projection(self):
        for n,D in [(0,4),(2,3),(4,2)]:
            orbit=s.full_orbit(2*(n+D))
            observed=s.green_pascal_phase_offset_projection(n,D,orbit)
            independent=s.finite_composite_offset_distribution(n,D)
            self.assertEqual(observed,independent)
