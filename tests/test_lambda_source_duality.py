"""Exact finite tests for SUCC's typed lambda and inverse-branch duality.

All tests are algebraic over rational values unless explicitly labelled
NUMERICAL_DIAGNOSTIC. Original BBP forcing is imported unchanged.
They do not claim an asymptotic signed Fourier saving or pi normality.
"""
from __future__ import annotations

import cmath
import unittest
from fractions import Fraction as Q
from itertools import product
from math import isclose, sqrt, pi

from observational_succ import lambda_source_duality as ld
from observational_succ.succ_internal_matrix_walk import authentic_r, circle
from observational_succ import oily_macaroni_totient as ot


class FiniteLambdaTests(unittest.TestCase):
    def test_exponential_and_evaluation(self):
        X=(0,1,2);Y=(False,True)
        exp=ld.exponential_object(X,Y)
        self.assertEqual(len(exp),8)
        ev=ld.evaluation_arrow(X,Y)
        for f in exp:
            for x in X:
                self.assertEqual(ev.apply((f,x)),f[x])

    def test_curry_and_uncurry_exact_round_trip(self):
        from observational_succ.beck_chevalley_source import finite_map
        A=('s0','s1');X=(0,1,2);Y=(0,1)
        f=finite_map(tuple(product(A,X)),Y,
                     lambda pair: (int(pair[0]=='s1')+pair[1])%2)
        g=ld.curry_arrow(f,A,X,Y)
        self.assertEqual(g.domain,A)
        self.assertEqual(ld.uncurry_arrow(g,A,X,Y),f)
        self.assertEqual(ld.curry_arrow(ld.uncurry_arrow(g,A,X,Y),A,X,Y),g)
        with self.assertRaises(ld.DualityDomainError):
            ld.curry_arrow(f,A,X,('mismatch',))

    def test_church_iterator_is_typed_and_not_nonautonomous_source(self):
        from observational_succ.beck_chevalley_source import finite_map
        carrier=(0,1,2,3)
        succ=finite_map(carrier,carrier,lambda x:(x+1)%4)
        for n in range(12):
            self.assertEqual(ld.ChurchIterator(n).apply(succ,0),n%4)
        with self.assertRaises(ld.DualityDomainError):
            ld.ChurchIterator(2).apply(finite_map((0,1),(0,1,2),lambda x:x),0)
        self.assertNotEqual(authentic_r(1),authentic_r(2))
        self.assertNotEqual(authentic_r(2),authentic_r(3))

    def test_oversized_exponential_rejected(self):
        with self.assertRaises(ld.DualityDomainError):
            ld.exponential_object(range(13),(0,1))


class CyclotomicTests(unittest.TestCase):
    def test_zeta_8_sign_and_zeta_16_unity(self):
        z=ld.Cyclo16.zeta(1)
        t=ld.Cyclo16.one()
        for _ in range(8):t=t*z
        self.assertEqual(t,-ld.Cyclo16.one())
        self.assertEqual(t*t,ld.Cyclo16.one())
        for h in range(-25,26):
            self.assertEqual(ld.Cyclo16.zeta(h).conjugate(),ld.Cyclo16.zeta(-h))

    def test_true_root_of_unity_cancellation_not_formal_group_algebra(self):
        for h in range(-64,65):
            actual=ld.uniform_inverse_character(h)
            expect=ld.Cyclo16.one() if h%16==0 else ld.Cyclo16.zero()
            self.assertEqual(actual,expect,h)

    def test_koopman_and_perron_exact_inverses(self):
        for r in (Q(0),Q(47,15),Q(1,7),-Q(9,5)):
            for h in range(-34,35):
                cert=ld.exact_koopman_perron_square(h,r)
                self.assertEqual(cert['perron_after_koopman'],ld.FourierCharacter(h,Q(0)))
                self.assertEqual(cert['koopman_after_perron'],
                                 ld.FourierCharacter(h,Q(0)) if h%16==0 else None)
                self.assertFalse(cert['selected_weyl_saving_proved'])

    def test_kooppf_pointwise_on_rational_fibers(self):
        for r in (Q(5,11),Q(47,15),Q(0)):
            for y in (Q(0),Q(2,15),Q(8,13)):
                t=circle(y-r)
                fibers=tuple((t+j)/16 for j in range(16))
                self.assertEqual(len(set(fibers)),16)
                for x in fibers:
                    self.assertEqual(circle(16*x+r),y)
                # P K f(y) = f(y) for a nontrivial rational observable.
                f=lambda v:v*v+v
                self.assertEqual(sum((f(circle(16*x+r)) for x in fibers),Q(0))/16,f(y))

    def test_endpoint_packet_char_nonzero_and_exact_inverse(self):
        weights=ld.packet_fold_mod16()
        self.assertEqual(sum(weights),1)
        self.assertGreater(ld.fourier_parseval_defect(weights),0)
        for h in range(16):
            z=ld.Cyclo16.zeta(h)
            F=ld.branch_fourier(weights,h)
            rhs=(ld.Cyclo16.one()*2-z)
            self.assertEqual(F*rhs*rhs,ld.Cyclo16.one(),h)
            self.assertNotEqual(F,ld.Cyclo16.zero())
            self.assertGreaterEqual(abs(F.evaluation())+1e-12,1/9)

    def test_source_packet_grade_fold_uses_original_om_law(self):
        folded=ld.packet_fold_mod16()
        for depth in (16,32,64):
            truncated=tuple(sum((ot.endpoint_weight(j)
                                 for j in range(digit,depth,16)),Q())
                            for digit in range(16))
            for j in range(16):
                self.assertLessEqual(folded[j]-truncated[j],ot.compiler_error(depth))
            self.assertEqual(sum((folded[j]-truncated[j] for j in range(16)),Q()),
                             ot.compiler_error(depth))
        odd=ld.primitive_packet_fold_mod16()
        self.assertEqual(sum(odd),1)
        self.assertEqual(ot.primitive_mass(16),Q(4,9))

    def test_primitive_packet_character_exact_and_cannot_be_uniform(self):
        weights=ld.primitive_packet_fold_mod16()
        self.assertEqual(sum(weights),1)
        self.assertGreaterEqual(ld.fourier_parseval_defect(weights),1)
        # Every primitive grade is odd; the h=8 character is -1, not 0.
        self.assertEqual(ld.branch_fourier(weights,8),-ld.Cyclo16.one())
        for h in range(16):
            z=ld.Cyclo16.zeta(h)
            F=ld.branch_fourier(weights,h)
            self.assertEqual(F*(ld.Cyclo16.one()*4-z*z)*(ld.Cyclo16.one()*4-z*z),z*9)
            self.assertNotEqual(F,ld.Cyclo16.zero())

    def test_branch_weights_must_be_exact_probabilities(self):
        with self.assertRaises(ld.DualityDomainError):
            ld.branch_fourier((Q(1),)*15,1)
        with self.assertRaises(ld.DualityDomainError):
            ld.branch_fourier((0.1,)*(16),1)
        with self.assertRaises(ld.DualityDomainError):
            ld.fourier_parseval_defect((Q(1),)*16)

    def test_rational_parseval_equals_numeric_fourier(self):
        for weights in ((Q(1,16),)*16,ld.packet_fold_mod16(),
                        ld.primitive_packet_fold_mod16(),
                        (Q(1),)+(Q(0),)*15):
            energy=ld.fourier_parseval_defect(weights)
            modes=sum(abs(ld.branch_fourier(weights,h).evaluation())**2 for h in range(1,16))
            self.assertAlmostEqual(modes,float(energy),places=11)


class SourceSelectedTests(unittest.TestCase):
    def test_authentic_history_and_one_preimage_selector(self):
        states=ld.original_history(35)
        self.assertTrue(ld.verify_original_history(states))
        self.assertEqual(states[0],authentic_r(1))
        selected=ld.witness_selected_branches(states)
        self.assertEqual(len(selected),34)
        for b in selected:
            self.assertEqual(b.current,Q(b.digit+b.remainder,16))
            self.assertEqual(b.remainder,circle(b.successor-b.forcing))
            self.assertTrue(0<=b.digit<16)
            self.assertEqual(b.forcing,authentic_r(b.source_index+1))
            self.assertEqual(b.literal_carry,
                             b.digit+(b.remainder+b.forcing).numerator//(b.remainder+b.forcing).denominator)
            self.assertGreaterEqual(b.conductor, b.forcing.denominator)
            self.assertEqual(b.conductor % b.forcing.denominator,0)

    def test_changed_seed_and_changed_forcing_are_rejected(self):
        source=ld.original_history(12)
        self.assertFalse(ld.verify_original_history((source[0]+Q(1,3),)+source[1:]))
        altered=[];u=Q(1,3)
        for n in range(1,13):
            u=16*u+authentic_r(n);altered.append(u)
        self.assertFalse(ld.verify_original_history(tuple(altered)))
        with self.assertRaises(ld.DualityDomainError):
            ld.witness_selected_branches(tuple(altered))
        altered=list(source);altered[5]+=Q(1,100)
        self.assertFalse(ld.verify_original_history(tuple(altered)))

    def test_exact_conditional_chi2_uniform_control(self):
        u=Q(1,3)
        values=tuple((j+u)/16 for j in range(16))
        b=ld.branch_defect(values,4,authenticate=False)
        self.assertEqual(b.chi_squared,0)
        self.assertEqual(sum(map(sum,b.counts)),16)
        for h in range(1,16):
            phase=sum(cmath.exp(2j*pi*h*float(x)) for x in values)/16
            self.assertLess(abs(phase),1e-13)

    def test_uniform_digit_marginal_not_enough_without_tail(self):
        # Every branch digit occurs once, yet the tail depends on parity.
        # At h=8 the source-free signed phase remains (1-i)/2.
        values=tuple((j+(Q(0) if j%2==0 else Q(1,2)))/16 for j in range(16))
        self.assertEqual(ld.branch_defect(values,1,authenticate=False).chi_squared,0)
        self.assertEqual(ld.branch_defect(values,2,authenticate=False).chi_squared,1)
        z=sum(cmath.exp(2j*pi*8*float(x)) for x in values)/16
        self.assertAlmostEqual(z.real,0.5,places=12)
        self.assertAlmostEqual(z.imag,-0.5,places=12)

    def test_fake_constant_sequence_has_maximal_defect(self):
        vals=(Q(0),)*25
        d=ld.branch_defect(vals,8,authenticate=False)
        self.assertEqual(d.chi_squared,15)
        self.assertFalse(ld.verify_original_history(vals))

    def test_actual_branch_defect_and_fourier_bound(self):
        for N,M in ((16,2),(32,3),(64,4),(112,5)):
            states=ld.original_history(N)
            d=ld.branch_defect(states,M)
            self.assertGreaterEqual(d.chi_squared,0)
            self.assertLessEqual(d.chi_squared,15)
            self.assertEqual(sum(map(sum,d.counts)),N)
            for h in (1,2,3,5,15,17,-3):
                char=sum(cmath.exp(2j*pi*h*float(circle(u))) for u in states)/N
                upper=d.exact_upper_for_primitive_h(h)
                self.assertLessEqual(abs(char),float(upper)+1e-10)

    def test_exact_conditional_mode_energy_parseval(self):
        for values, M, auth in ((ld.original_history(26),4,True),
                                ((Q(0),)*32,3,False),
                                (tuple((j+Q(1,3))/16 for j in range(16)),2,False)):
            b=ld.branch_defect(values,M,authenticate=auth)
            total=sum((b.conditional_mode_energy(h) for h in range(1,16)),ld.Cyclo16.zero())
            self.assertEqual(total,ld.Cyclo16.one()*b.chi_squared)
            self.assertEqual(b.conditional_mode_energy(8),ld.Cyclo16.one()*b.exact_parity_energy())
            for h in range(1,16):
                energy=b.conditional_mode_energy(h)
                self.assertAlmostEqual(energy.evaluation().imag,0,places=10)
                self.assertGreaterEqual(energy.evaluation().real,-1e-12)

    def test_divisible_16_mode_rejected_by_primitive_bound(self):
        d=ld.branch_defect(ld.original_history(8),2)
        with self.assertRaises(ld.DualityDomainError):
            d.exact_upper_for_primitive_h(16)
        with self.assertRaises(ld.DualityDomainError):
            d.exact_upper_for_primitive_h(0)

    def test_exact_full_weyl_bound_all_frequency_levels(self):
        for N in (16,48,96):
            states=ld.original_history(N)
            b=ld.branch_defect(states,4)
            for h in (1,3,16,32,256,16*16*3,-16):
                actual=sum(cmath.exp(2j*pi*h*float(circle(u))) for u in states)/N
                upper=ld.selected_weyl_upper_from_branch_defect(b,h)
                self.assertLessEqual(abs(actual),float(upper)+1e-9)
        with self.assertRaises(ld.DualityDomainError):
            ld.selected_weyl_upper_from_branch_defect(b,0)

    def test_rational_shift_budget_covers_actual_source_modes(self):
        for N in (8,24,100):
            st=ld.original_history(N+1)
            for h in (1,2,3,16,-3):
                aa=sum(cmath.exp(2j*pi*h*float(circle(u))) for u in st[:N])/N
                bb=sum(cmath.exp(2j*pi*16*h*float(circle(u))) for u in st[:N])/N
                finite=ld.source_shift_actual_N_budget(N,h)
                allN=ld.authenticated_shift_budget(N,h)
                self.assertLessEqual(abs(aa-bb),float(finite)+1e-10)
                self.assertLessEqual(finite,allN)

    def test_status_is_fail_closed(self):
        status=ld.status_flags()
        self.assertTrue(status['uniform_branch_fourier_orthogonality'])
        self.assertFalse(status['conditional_chi2_normality_saving_proved'])
        self.assertFalse(status['source_max_entropy_estimate_proved'])
        self.assertFalse(status['pi_base16_normality_proved'])


if __name__=='__main__':
    unittest.main()
