"""Exact and independent hostile tests for prime-form heat/Mellin SUCC.

Proof obligations are established algebraically in accompanying dossier; these
finite tests are calibrated regression controls and not universal verification.
"""
from __future__ import annotations
import unittest
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial

from observational_succ.prime_form_heat import (
    AffineSource, SourceHeatError, prime, digits_apply, digit_inverse,
    affine_commutator, digit_isometry_image, digit_isometry_adjoint,
    polynomial_heat, polynomial_translate, gaussian_even_moment,
    prime_powers_up_to, prime_power_witness, prime_jet_exact_coefficients,
    tree_depth_dirichlet,tree_depth_limit,tree_depth_remainder,local_radix_euler,
    gaussian_arch_factor,gaussian_arch_integral,prime_jet_heat,
    prime_jet_mellin_truncated,prime_jet_log_derivative,prime_tail_upper_numeric,
    coset_theta,coset_theta_fourier,theta,theta_tail_upper,
    completed_lambda_split,completed_lambda_standard,completed_lambda_split_tail_upper,
    spectral_depth_heat,
)


class TestAffineSource(unittest.TestCase):
    def test_all_integer_divisions_euclidean(self):
        for p in (2,3,4,5,6,7):
            src=AffineSource(p)
            for n in range(-100,101):
                q,b=src.inverse(n)
                self.assertEqual((src.step(q,b),b),(n,n%p))

    def test_prime_label_mutation(self):
        for p in (2,3,5,7,11):
            self.assertTrue(AffineSource(p,require_prime=True).require_prime)
        for p in (4,6,9,10):
            with self.assertRaises(SourceHeatError):
                AffineSource(p,require_prime=True)
        self.assertEqual(AffineSource(6).step(2,5),17)

    def test_missing_basis_source_epoch_controls(self):
        for params in ({'source_id':''},{'basis_id':''},{'epoch':-1},{'epoch':1.0}):
            with self.assertRaises(SourceHeatError):AffineSource(5,**params)
        for b in (-1,5):
            with self.assertRaises(SourceHeatError):AffineSource(5).step(3,b)
        with self.assertRaises(SourceHeatError):AffineSource(True)
        with self.assertRaises(SourceHeatError):AffineSource(2.0)

    def test_mixed_radix_original_and_reconstruction(self):
        for rs in ((2,3,5),(5,2,3),(3,3,2),(2,2,2)):
            seen=[]
            for word in product(*(range(p) for p in rs)):
                value=digits_apply(rs,word,0)
                seen.append(value)
                self.assertEqual(digit_inverse(rs,value),(0,tuple(word)))
                for q in (-3,-1,0,2):
                    actual=digits_apply(rs,word,q)
                    self.assertEqual(digit_inverse(rs,actual),(q,tuple(word)))
            self.assertEqual(sorted(seen),list(range(__import__('math').prod(rs))))

    def test_commutator_matches_two_orders(self):
        for p,q in ((2,2),(2,3),(3,5),(6,7)):
            for b in range(p):
                for c in range(q):
                    lhs=AffineSource(p).step(AffineSource(q).step(9,c),b)
                    rhs=AffineSource(q).step(AffineSource(p).step(9,b),c)
                    self.assertEqual(lhs-rhs,affine_commutator(p,b,q,c))
        self.assertEqual(affine_commutator(2,1,3,1),-1)

    def test_cuntz_digit_operators_on_bilateral_carrier(self):
        for p in (2,3,5,6):
            for n in range(-32,33):
                b=n%p
                self.assertEqual(digit_isometry_adjoint(p,b,n),(n-b)//p)
                self.assertEqual(sum(digit_isometry_adjoint(p,j,n) is not None for j in range(p)),1)
                for c in range(p):
                    for q in range(-3,4):
                        self.assertEqual(digit_isometry_adjoint(p,c,digit_isometry_image(p,b,q)),q if c==b else None)

    def test_cuntz_is_not_prime_test(self):
        # The arithmetic component p=6 passes all digit Hilbert space relations.
        self.assertEqual(digit_isometry_adjoint(6,5,17),2)
        with self.assertRaises(SourceHeatError): local_radix_euler(6,2)

    def test_prime_form_primality_not_decided_by_coprimality(self):
        src=AffineSource(5,require_prime=True)
        self.assertEqual(src.step(1,1),6)  # coprime digit, composite output
        self.assertEqual(src.step(2,1),11)
        self.assertEqual(src.step(1,0),5)
        for q in range(2,15):
            self.assertFalse(prime(src.step(q,0)))


class TestHeatInsidePascal(unittest.TestCase):
    def test_heat_monomials_independent_manual_laplacian(self):
        for n in range(0,18):
            for t in (Q(0),Q(1,7),Q(2,3)):
                poly=tuple(int(i==n) for i in range(n+1))
                target=polynomial_heat(poly,t)
                # Independent iterative repeated second derivatives of a monomial.
                acc=[Q(0)]*(n+1)
                cur=[Q(x) for x in poly]
                for j in range(n//2+1):
                    for i,v in enumerate(cur):acc[i]+=v*t**j/factorial(j)
                    cur=[(i+2)*(i+1)*cur[i+2] if i+2<len(cur) else Q(0) for i in range(n+1)]
                self.assertEqual(target,tuple(acc))

    def test_heat_semigroup(self):
        for coeff in ((1,2,3,4,5,6),(-3,0,5,4,1,0,2),(0,)*8+(1,)):
            c=polynomial_heat(polynomial_heat(coeff,Q(2,7)),Q(3,11))
            self.assertEqual(c,polynomial_heat(coeff,Q(2,7)+Q(3,11)))

    def test_heat_commutes_with_pascal_unit_translation(self):
        for coeff in ((0,0,0,0,1),(1,2,-3,4,0,1),(5,-4,3,0,0,0)):
            for d in (Q(-1,2),Q(0),Q(7,5)):
                self.assertEqual(polynomial_translate(polynomial_heat(coeff,Q(2,9)),d),
                                 polynomial_heat(polynomial_translate(coeff,d),Q(2,9)))

    def test_heat_even_moments_from_constant_coefficient(self):
        for n in range(0,12):
            for t in (Q(0),Q(1,5),Q(3,2)):
                poly=(Q(0),)*(2*n)+(Q(1),)
                self.assertEqual(polynomial_heat(poly,t)[0],gaussian_even_moment(n,t))

    def test_heat_does_not_preserve_fixed_degree(self):
        self.assertEqual(polynomial_heat((0,0,1),Q(1,2)),(1,0,1))
        self.assertEqual(polynomial_heat((0,0,0,1),Q(1,2)),(0,3,0,1))

    def test_negative_heat_time_and_bad_coeffs_refused(self):
        with self.assertRaises(SourceHeatError):polynomial_heat((1,2),-1)
        with self.assertRaises(SourceHeatError):polynomial_translate((1,2),0.5)
        with self.assertRaises(SourceHeatError):gaussian_even_moment(1,-1)


class TestArithmeticJet(unittest.TestCase):
    def test_prime_powers_against_independent_factorization(self):
        for N in (2,3,10,30,100,400):
            table={n:(p,k) for n,p,k in prime_powers_up_to(N)}
            oracle={}
            for n in range(2,N+1):
                fac=[];v=n
                d=2
                while d*d<=v:
                    while v%d==0:
                        fac.append(d);v//=d
                    d+=1
                if v>1:fac.append(v)
                if len(set(fac))==1:oracle[n]=(fac[0],len(fac))
                self.assertEqual(prime_power_witness(n),oracle.get(n))
            self.assertEqual(table,oracle)

    def test_distinguish_fake_composite_6(self):
        vals=dict(prime_jet_exact_coefficients(30))
        self.assertNotIn(6, vals)
        self.assertEqual(vals[8],2)
        self.assertEqual(vals[9],3)
        self.assertEqual(vals[25],5)
        self.assertNotIn(12,vals)
        self.assertNotIn(18,vals)
        self.assertEqual(sorted(n for n,_ in prime_jet_exact_coefficients(30)),sorted(vals))

    def test_local_raw_tree_shifted_pole_and_measure_debt(self):
        for p in (2,3,5,6):
            for s in (2,3,4):
                for depth in (0,1,2,7,16):
                    for weighting in ("raw_count","level_normalized"):
                        trunc=tree_depth_dirichlet(p,depth,s,weighting=weighting)
                        rem=tree_depth_remainder(p,depth,s,weighting=weighting)
                        self.assertEqual(trunc+rem,tree_depth_limit(p,s,weighting=weighting))
                        self.assertGreater(rem,0)
                self.assertNotEqual(tree_depth_limit(p,s,weighting="raw_count"),tree_depth_limit(p,s,weighting="level_normalized"))
                if prime(p):
                    self.assertEqual(tree_depth_limit(p,s,weighting="level_normalized"),local_radix_euler(p,s))

    def test_weighting_not_fake_trace(self):
        self.assertEqual(tree_depth_dirichlet(2,1,2,weighting="raw_count"),Q(3,2))
        self.assertEqual(tree_depth_dirichlet(2,1,2,weighting="level_normalized"),Q(5,4))
        # Without weight, there are 2 distinct eigenvectors at depth one.
        self.assertEqual(1+2*Q(2)**(-2),Q(3,2))

    def test_prime_jet_mellin_matches_log_derivative_with_tail(self):
        import mpmath as mp
        for s in (2,3):
            n=400
            truncated=prime_jet_mellin_truncated(s,N=n,dps=50)
            full=prime_jet_log_derivative(s,dps=50)
            tail=prime_tail_upper_numeric(n,s,dps=50)*abs(gaussian_arch_factor(s,dps=50))
            self.assertLessEqual(abs(full-truncated),tail)
            self.assertGreater(abs(full-truncated),mp.mpf('1e-10'))

    def test_prime_jet_heat_positive_and_composite_mutation(self):
        import mpmath as mp
        h=prime_jet_heat(Q(1,5),80,dps=45)
        self.assertGreater(h,0)
        self.assertLess(h,mp.mpf('100'))
        self.assertRaises(SourceHeatError,prime_jet_heat,0,80)
        self.assertRaises(SourceHeatError,prime_jet_mellin_truncated,Q(1,2),80)

    def test_false_euler_product_at_composite_base(self):
        self.assertEqual(tree_depth_limit(6,2,weighting="level_normalized"),Q(36,35))
        with self.assertRaises(SourceHeatError):local_radix_euler(6,2)


class TestFourierAndCompletion(unittest.TestCase):
    def test_local_arch_gaussian_mellin_independent_integral(self):
        import mpmath as mp
        for s in (2,3,Q(5,2),2+0.3j):
            closed=gaussian_arch_factor(s,dps=45)
            integral=gaussian_arch_integral(s,dps=45)
            self.assertLess(abs(closed-integral),mp.mpf('1e-29'))

    def test_wrong_gaussian_scale_changes_arch_factor(self):
        import mpmath as mp
        ref=gaussian_arch_factor(2,dps=40)
        wrong=gaussian_arch_factor(2,scale=Q(3,2),dps=40)
        self.assertLess(abs(wrong/ref-mp.mpf(2)/3),mp.mpf('1e-38'))
        with self.assertRaises(SourceHeatError):gaussian_arch_factor(2,scale=0)
        with self.assertRaises(SourceHeatError):gaussian_arch_factor(0)

    def test_all_residue_theta_splits_against_lattice_trace(self):
        import mpmath as mp
        for p in (2,3,5,6):
            t=Q(2,5)
            lhs=sum((coset_theta(p,b,t,20,dps=40) for b in range(p)),mp.mpf(0))
            full=theta(t,cut=60,dps=40)
            self.assertLess(abs(lhs-full),mp.mpf('1e-32'))

    def test_finite_to_spectral_poisson_residue_dual(self):
        import mpmath as mp
        for p,b,t in ((2,0,Q(1,2)),(2,1,Q(3,4)),(3,1,Q(2,5)),(5,2,Q(2,5)),(6,3,Q(2,5))):
            direct=coset_theta(p,b,t,cut=26,dps=45)
            spectral=coset_theta_fourier(p,b,t,cut=26,dps=45)
            self.assertLess(abs(direct-spectral),mp.mpf('1e-30'))

    def test_nonzero_affine_phase_is_essential(self):
        import mpmath as mp
        p=5;t=Q(2,5)
        residue0=coset_theta_fourier(p,0,t,cut=24,dps=45)
        residue1=coset_theta_fourier(p,1,t,cut=24,dps=45)
        self.assertGreater(abs(residue0-residue1),mp.mpf('0.05'))

    def test_theta_modular_functional_equation(self):
        import mpmath as mp
        for t in (Q(2,3),Q(3,2),Q(1,4),Q(4)):
            tau=mp.mpf(t.numerator)/t.denominator
            lhs=theta(tau,cut=34,dps=45)
            rhs=theta(1/tau,cut=34,dps=45)/mp.sqrt(tau)
            self.assertLess(abs(lhs-rhs),mp.mpf('1e-35'))

    def test_theta_n_tail_enclosure_analytic_bound(self):
        import mpmath as mp
        for t in (Q(2,5),Q(1),Q(2)):
            for N in (2,3,5,9):
                low=theta(t,cut=N,dps=50)
                high=theta(t,cut=45,dps=50)
                self.assertLessEqual(abs(high-low),theta_tail_upper(t,N,dps=50))

    def test_completed_lambda_zero_independent_theta_split(self):
        import mpmath as mp
        for s in (Q(5,2),Q(1,2),0.7+5j,-2.2+3j):
            v=completed_lambda_split(s,cut=9,dps=45)
            w=completed_lambda_standard(s,dps=45)
            self.assertLess(abs(v-w),mp.mpf('1e-32'))
            self.assertLess(abs(v-completed_lambda_split(1-s,cut=9,dps=45)),mp.mpf('1e-32'))

    def test_theta_split_tail_certificate_in_critical_strip(self):
        import mpmath as mp
        for s in (0.25+3j,0.5+8j,0.8+2j):
            for cut in (1,2,4):
                diff=abs(completed_lambda_split(s,cut=14,dps=45)-completed_lambda_split(s,cut=cut,dps=45))
                self.assertLessEqual(diff,completed_lambda_split_tail_upper(cut,dps=45))

    def test_no_zeros_as_input_works_at_complex_values(self):
        import mpmath as mp
        s=mp.mpc('0.6','13.2')
        z=completed_lambda_split(s,cut=9,dps=42)
        self.assertLess(abs(z-completed_lambda_standard(s,dps=42)),mp.mpf('1e-30'))

    def test_spectral_depth_heat_measure_changes_trace(self):
        import mpmath as mp
        raw=spectral_depth_heat(3,Q(1,4),4,weighting="raw_count",dps=45)
        norm=spectral_depth_heat(3,Q(1,4),4,weighting="level_normalized",dps=45)
        self.assertGreater(raw,norm)
        self.assertGreater(norm,0)
        self.assertLess(raw,10)

    def test_theta_and_prime_jet_are_different_sources(self):
        # Number of n<=16 is 16; number of prime powers <=16 strictly smaller.
        primes={n for n,p,k in prime_powers_up_to(16)}
        self.assertNotEqual(primes,set(range(1,17)))
        self.assertIn(16,primes)
        self.assertNotIn(12,primes)

    def test_wrong_source_pole_hypothesis(self):
        # Depth-state multiplicity p^k shifts from local Euler factor ζ_p(s)
        # to ζ_p(s-1), so p-normalization is a theorem-bearing source choice.
        p=3;s=2
        self.assertEqual(tree_depth_limit(p,s,weighting="raw_count"),Q(3,2))
        self.assertEqual(tree_depth_limit(p,s,weighting="level_normalized"),Q(9,8))
        self.assertNotEqual(Q(3,2),Q(9,8))


class TestPrimeFormCosetIsolation(unittest.TestCase):
    def test_zero_coset_prime_isolates_all_local_jets(self):
        from observational_succ.prime_form_heat import prime_jets_zero_coset
        for p in (2,3,5,7,11):
            jets=prime_jets_zero_coset(p,2000)
            self.assertTrue(jets)
            self.assertTrue(all(n==p**k and base==p for n,base,k in jets))
            self.assertEqual(set(n for n,_,_ in jets),set(p**k for k in range(1,15) if p**k<=2000))

    def test_squarefree_composite_radix_kills_jet_branch(self):
        from observational_succ.prime_form_heat import prime_jets_zero_coset,prime_zero_coset_mellin_local
        for p in (6,10,12,15,18,30):
            self.assertFalse(prime_jets_zero_coset(p,2000))
            self.assertIsNone(prime_zero_coset_mellin_local(p,2))

    def test_prime_power_radix_is_truncated_local_jet(self):
        from observational_succ.prime_form_heat import prime_jets_zero_coset,prime_zero_coset_mellin_local
        self.assertEqual(prime_jets_zero_coset(4,80),((4,2,2),(8,2,3),(16,2,4),(32,2,5),(64,2,6)))
        self.assertEqual(prime_zero_coset_mellin_local(4,2),(2,Q(1,16)/(1-Q(1,4))))
        self.assertEqual(prime_zero_coset_mellin_local(2,2),(2,Q(1,4)/(1-Q(1,4))))
        self.assertNotEqual(prime_zero_coset_mellin_local(4,2),prime_zero_coset_mellin_local(2,2))

    def test_prime_zero_coset_rational_dirichlet_tail_exact(self):
        from observational_succ.prime_form_heat import prime_zero_coset_mellin_local
        for p in (2,3,5):
            for s in (2,3,4):
                _,geom=prime_zero_coset_mellin_local(p,s)
                truncated=sum((Q(p)**(-k*s) for k in range(1,20)),Q(0))
                self.assertGreater(geom,truncated)
                self.assertEqual(geom-truncated,Q(p)**(-20*s)/(1-Q(p)**(-s)))

    def test_exact_heat_affine_scaling_p_and_b(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import heat_affine_pullback
        mp.mp.dps=50
        for p in (2,3,5,6):
            for b in range(p):
                for n in (-4,0,3):
                    direct,pulled=heat_affine_pullback(p,b,n,Q(2,5))
                    self.assertLess(abs(direct-pulled),mp.mpf('1e-40'))

    def test_actual_fourier_rotation_of_affine_cosets(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import residue_fourier_character,residue_fourier_character_dual
        for p in (2,3,5,6):
            for r in (0,1,p-1):
                a=residue_fourier_character(p,r,Q(2,5),cut=23,dps=45)
                b=residue_fourier_character_dual(p,r,Q(2,5),cut=23,dps=45)
                self.assertLess(abs(a-b),mp.mpf('1e-35'))

    def test_spectral_exponent_mutation_shifts_gamma_order(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import spectral_power_mellin_factor
        a=spectral_power_mellin_factor(3,1,dps=45)
        b=spectral_power_mellin_factor(3,2,dps=45)
        self.assertGreater(abs(a-b),mp.mpf('0.05'))
        self.assertLess(abs(b-gaussian_arch_factor(3,dps=45)),mp.mpf('1e-39'))
        with self.assertRaises(SourceHeatError):spectral_power_mellin_factor(2,0)

    def test_both_flat_and_prime_sources_need_separate_proof(self):
        from observational_succ.prime_form_heat import primary_radix_factor
        self.assertEqual(primary_radix_factor(9),(3,2))
        self.assertEqual(primary_radix_factor(16),(2,4))
        self.assertIsNone(primary_radix_factor(14))
        self.assertTrue(prime(7))

class TestPascalInteriorHeatLimit(unittest.TestCase):
    def test_polynomial_finite_heat_to_gaussian_exact_fourth_moment(self):
        from observational_succ.prime_form_heat import fourth_moment_pascal_limit, iterated_pascal_heat_polynomial
        for n in (1,2,3,10,17,50,100):
            for t in (Q(1,4),Q(2,3)):
                finite,gauss,gap=fourth_moment_pascal_limit(n,t)
                actual=iterated_pascal_heat_polynomial((0,0,0,0,1),t,n)[0]
                self.assertEqual(actual,finite)
                self.assertEqual(gauss,polynomial_heat((0,0,0,0,1),t)[0])
                self.assertEqual(gap,Q(8)*t*t/n)

    def test_pascal_heat_char_quantitative_all_n(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import symmetric_pascal_character,symmetric_pascal_error_certificate
        for t,u in ((Q(1),Q(1,2)),(Q(3,5),Q(2,3)),(Q(2),Q(1,3))):
            for n in (40,100,200,500):
                target=mp.exp(-mp.mpf(t.numerator)/t.denominator*(mp.mpf(u.numerator)/u.denominator)**2)
                approx=symmetric_pascal_character(n,t,u,dps=45)
                bound=symmetric_pascal_error_certificate(n,t,u)
                self.assertLess(abs(approx-target),mp.mpf(bound.numerator)/bound.denominator+mp.mpf('1e-39'))

    def test_correlated_pascal_source_mutant_not_heat(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import symmetric_pascal_character,symmetric_pascal_correlated_character
        t=Q(1);u=Q(1)
        n=120
        iid=symmetric_pascal_character(n,t,u,dps=45)
        correlated=symmetric_pascal_correlated_character(n,t,u,dps=45)
        self.assertLess(abs(iid-mp.exp(-1)),mp.mpf('0.02'))
        self.assertGreater(abs(correlated-mp.exp(-1)),mp.mpf('0.1'))

    def test_exact_heat_generator_degree_four(self):
        from observational_succ.prime_form_heat import iterated_pascal_heat_polynomial
        t=Q(1,3)
        for n in (10,50,150):
            finite=iterated_pascal_heat_polynomial((0,0,0,0,1),t,n)
            limit=polynomial_heat((0,0,0,0,1),t)
            self.assertEqual(finite[4],limit[4])
            self.assertEqual(finite[2],limit[2])
            self.assertLess(finite[0],limit[0])

    def test_centered_uniform_digit_gaussian_limit_prime_blind(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import digit_bulk_character
        t=Q(1);u=Q(1,2)
        target=mp.exp(-mp.mpf(1)/4)
        for p in (2,3,5,6,8):
            a=digit_bulk_character(p,100,t,u,dps=45)
            b=digit_bulk_character(p,800,t,u,dps=45)
            self.assertLess(abs(b-target),abs(a-target))
            self.assertLess(abs(b-target),mp.mpf('0.005'))

    def test_hypotheses_and_fair_coin_error_bound_validation(self):
        from observational_succ.prime_form_heat import symmetric_pascal_error_certificate,one_step_pascal_heat_on_polynomial
        with self.assertRaises(SourceHeatError):symmetric_pascal_error_certificate(2,1,2)
        self.assertEqual(one_step_pascal_heat_on_polynomial((0,0,1),Q(1),8),(Q(1,4),0,1))
        with self.assertRaises(SourceHeatError):one_step_pascal_heat_on_polynomial((1,1),-1,8)

class TestCompletedSourceIndependentRoutes(unittest.TestCase):
    def test_actual_mellin_integral_vs_finite_dirichlet_sum(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import prime_mellin_heat_integral_numeric
        for s in (2,Q(5,2)):
            integral=prime_mellin_heat_integral_numeric(s,22,dps=32)
            closed=prime_jet_mellin_truncated(s,22,dps=32)
            self.assertLess(abs(integral-closed),mp.mpf('1e-25'))

    def test_source_derived_entire_xi_special_values(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import xi_from_theta
        self.assertEqual(xi_from_theta(0,dps=40),mp.mpf('0.5'))
        self.assertEqual(xi_from_theta(1,dps=40),mp.mpf('0.5'))
        for s in (mp.mpc("0.3","2"),Q(1,2),-2+4j):
            self.assertLess(abs(xi_from_theta(s,cut=10,dps=42)-xi_from_theta(1-s,cut=10,dps=42)),mp.mpf('1e-35'))

    def test_theta_continuation_at_negative_trivial_zero_without_zero_oracle(self):
        # Γ has a pole and ζ has a zero at negative even s, but modular split
        # gives a finite Lambda value directly without either lookup.
        import mpmath as mp
        val=completed_lambda_split(-2,cut=10,dps=45)
        self.assertTrue(mp.isfinite(val.real))
        self.assertTrue(mp.isfinite(val.imag))
        self.assertGreater(abs(val),mp.mpf('0.01'))

class TestScientificReceipt(unittest.TestCase):
    def test_replay_complete_scientific_receipt(self):
        import json
        from pathlib import Path
        from scripts.prime_form_heat_probe import receipt
        root=Path(__file__).resolve().parents[1]
        expected=json.loads((root/'research/2026-10-14/PRIME_FORM_HEAT_RECEIPT.json').read_text(encoding='utf-8'))
        actual=receipt()
        self.assertEqual(actual,expected)
        self.assertFalse(actual['source_pin']['RH_proved'])
        self.assertFalse(actual['source_pin']['source_authenticated_physical'])
        self.assertEqual(actual['arithmetic_zero_cosets']['p5_local_log_coefficient_s2'],'1/24')
        self.assertEqual(actual['arithmetic_zero_cosets']['radix6_jets_upto_650'],[])

class TestOneGlobalArchimedeanGate(unittest.TestCase):
    def test_two_routes_to_finite_euler_product_match_exactly(self):
        from observational_succ.prime_form_heat import smooth_finite_euler,smooth_word_dirichlet_independent
        for primes in ((2,3),(2,5),(2,3,5),(3,5,7)):
            for d in (0,1,2,3):
                for s in (1,2,3):
                    self.assertEqual(smooth_word_dirichlet_independent(primes,d,s),smooth_finite_euler(primes,d,s))

    def test_unique_integer_carrier_at_multiplicative_depth(self):
        from observational_succ.prime_form_heat import smooth_prime_word_source
        for primes in ((2,3),(2,3,5),(5,7,11)):
            words=smooth_prime_word_source(primes,2)
            self.assertEqual(len(words),3**len(primes))
            self.assertEqual(len({n for n,_ in words}),3**len(primes))
            self.assertIn((1,(0,)*len(primes)),words)

    def test_gamma_only_once_for_multi_prime_carrier(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import truncated_global_heat_mellin,smooth_finite_euler
        pp=(2,3,5);s=2;d=3
        global_mellin=truncated_global_heat_mellin(pp,d,s,dps=45)
        local_product=smooth_finite_euler(pp,d,s)
        gamma=gaussian_arch_factor(s,dps=45)
        self.assertLess(abs(global_mellin-gamma*mp.mpf(local_product.numerator)/local_product.denominator),mp.mpf('1e-41'))
        wrong=gamma**len(pp)*mp.mpf(local_product.numerator)/local_product.denominator
        self.assertGreater(abs(global_mellin-wrong),mp.mpf('0.05'))

    def test_global_gaussian_integral_independent_of_factorized_euler(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import smooth_heat_integral_numeric,truncated_global_heat_mellin
        val=smooth_heat_integral_numeric((2,3),2,2,dps=36)
        deriv=truncated_global_heat_mellin((2,3),2,2,dps=36)
        self.assertLess(abs(val-deriv),mp.mpf('1e-27'))

    def test_euler_finite_prime_to_all_lattice_error_bound(self):
        import mpmath as mp
        from observational_succ.prime_form_heat import full_prime_cutoff_euler,global_euler_to_lattice_tail_upper
        for B in (3,5,7,13,29):
            for s in (2,3):
                prod=full_prime_cutoff_euler(B,s)
                val=mp.mpf(prod.numerator)/prod.denominator
                residual=mp.zeta(s)-val
                bound=global_euler_to_lattice_tail_upper(B,s)
                self.assertGreater(residual,0)
                self.assertLessEqual(residual,mp.mpf(bound.numerator)/bound.denominator)

    def test_finite_euler_contains_all_first_P_integer_addresses(self):
        from observational_succ.prime_form_heat import full_prime_cutoff_euler,all_integer_prefix_dirichlet
        for B in (5,7,11,19):
            for s in (1,2,3):
                self.assertGreaterEqual(full_prime_cutoff_euler(B,s),all_integer_prefix_dirichlet(B,s))

    def test_global_euler_diverges_for_sigma_le_one(self):
        # Finite prime sets satisfy E_P(1) >= H_P, a diverging lower bound.
        from observational_succ.prime_form_heat import full_prime_cutoff_euler,all_integer_prefix_dirichlet
        for B in (3,5,7,11,17,31):
            self.assertGreaterEqual(full_prime_cutoff_euler(B,1),all_integer_prefix_dirichlet(B,1))
        self.assertLess(full_prime_cutoff_euler(3,1),full_prime_cutoff_euler(31,1))

    def test_fake_composite_prime_and_duplicated_prime_refused(self):
        from observational_succ.prime_form_heat import smooth_prime_word_source,full_prime_cutoff_euler
        with self.assertRaises(SourceHeatError):smooth_prime_word_source((2,6),2)
        with self.assertRaises(SourceHeatError):smooth_prime_word_source((2,2),2)
        with self.assertRaises(SourceHeatError):smooth_prime_word_source((2,3),11)
        with self.assertRaises(SourceHeatError):full_prime_cutoff_euler(121,2)

if __name__=="__main__":unittest.main()
