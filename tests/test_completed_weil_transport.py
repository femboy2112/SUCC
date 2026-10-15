"""Adversarial source-to-completed-Weil tests; zero positions never queried.

Finite exact checks are NOT universal proofs of imported Weil's criterion.
A separate proof note gives the quantified C^2 arch-rung bound and zero-free
heat Mellin -> prime Dirichlet -> Weil distribution identification.
"""
import unittest
from fractions import Fraction as Q
from math import log as mathlog
import mpmath as mp

from observational_succ.completed_weil_transport import (
    WeilTransportError, von_mangoldt_labels, _prime,
    prime_heat, heat_mellin_normalization, heat_mellin_prime_fraction,
    prime_heat_tail_bound,complete_logderivative_from_heat,
    independent_xi_logderivative,arch_spectral_symbol,
    arch_contact,arch_real_kernel,arch_renorm_density,arch_integrand,
    arch_ladder_integrand,arch_ladder_remainder_bound,arch_c2_envelope,
    compact_arch,tent_convolution,tent_bounds,compact_weil_tent,
    arch_exponential_resolvent,arch_resolvent_integral,
    arch_resolvent_ladder,arch_resolvent_ladder_error,
    pole_resolvent,fake_composite6_resolvent_defect,
    half_density_mutation_defect,source_laplace_injective_scope,
    arch_resolvent_fourier,halfdensity_mellin_tent,
    additive_tent_fourier,arch_spectral_tent_numeric,
    arch_spectral_parity_conductor_resolvent,
    accelerated_arch_c2_remainder_bound, renormalized_arch_ladder,
    sobolev_operator_ladder_bound,
)


class ArithmeticSourceTest(unittest.TestCase):
    def test_mangoldt_against_independent_trial_factorization(self):
        for N in (2,6,30,300,701):
            mapping=dict(von_mangoldt_labels(N))
            for n in range(2,N+1):
                factors=[];m=n;p=2
                while p*p<=m:
                    while m%p==0:factors.append(p);m//=p
                    p+=1
                if m>1:factors.append(m)
                expected=factors[0] if len(set(factors))==1 else None
                self.assertEqual(mapping.get(n),expected)
        self.assertNotIn(6,dict(von_mangoldt_labels(100)))

    def test_prime_indices_exact_mutations(self):
        tape=dict(von_mangoldt_labels(60))
        self.assertEqual(tape[4],2)
        self.assertEqual(tape[8],2)
        self.assertEqual(tape[9],3)
        self.assertEqual(tape[49],7)
        for n in (6,10,12,15,18,30,50): self.assertNotIn(n,tape)

    def test_prime_source_inputs_rejected(self):
        for n in (0,1,-1,2.0,True,200001):
            with self.assertRaises(WeilTransportError):von_mangoldt_labels(n)

    def test_true_prime_heat_nonnegative_but_not_a_form_sign(self):
        for t in (Q(1,50),Q(1,3),Q(1)):
            self.assertGreater(prime_heat(t,100),0)
            self.assertGreater(heat_mellin_prime_fraction(3,100).real,0)
        self.assertLess(arch_exponential_resolvent(2),0)  # sign is NOT inherited

    def test_mellin_gaussian_normalization(self):
        mp.mp.dps=40
        for s in (Q(2),Q(3),Q(4)):
            val=heat_mellin_normalization(s)
            rhs=mp.power(mp.pi,-mp.mpf(s.numerator)/(2*s.denominator))*mp.gamma(mp.mpf(s.numerator)/(2*s.denominator))
            self.assertLess(abs(val-rhs),mp.mpf('1e-36'))

    def test_mellin_finite_prime_heat_independent_improper_integral(self):
        mp.mp.dps=35;s=3;N=20
        weights=[(n,p) for n,p in von_mangoldt_labels(N)]
        integrated=mp.fsum(mp.quad(lambda t:mp.log(p)*mp.exp(-mp.pi*t*n*n)*t**(mp.mpf(s)/2-1),[0,mp.mpf('0.1'),1,mp.inf]) for n,p in weights)
        predicted=heat_mellin_normalization(s)*heat_mellin_prime_fraction(s,N)
        self.assertLess(abs(integrated-predicted),mp.mpf('1e-27'))

    def test_global_prime_heat_tail_majorant(self):
        mp.mp.dps=40
        for sig,N in ((Q(3,2),300),(Q(2),100),(Q(3),60)):
            true_partial=heat_mellin_prime_fraction(sig,N)
            # independent analytic continuation-free Dirichlet ζ'/ζ oracle for σ>1
            oracle=-mp.diff(mp.zeta,mp.mpf(sig.numerator)/sig.denominator)/mp.zeta(mp.mpf(sig.numerator)/sig.denominator)
            self.assertLess(abs(oracle-true_partial),prime_heat_tail_bound(sig,N))

    def test_tail_rejects_critical_strip(self):
        for s in (Q(1),Q(1,2),Q(0)):
            with self.assertRaises(WeilTransportError):prime_heat_tail_bound(s,100)
        with self.assertRaises(WeilTransportError):prime_heat_tail_bound(2,2)
        for s in (Q(1),Q(1,2),Q(0)):
            with self.assertRaises(WeilTransportError):source_laplace_injective_scope(s)
        c=source_laplace_injective_scope(Q(5,4))
        self.assertFalse(c['finite_evidence_sufficient'])


class GammaContactLadderTest(unittest.TestCase):
    def test_arch_spectral_symbol_even_and_conductor(self):
        mp.mp.dps=40
        for t in (0,mp.mpf('0.3'),3,17):
            self.assertLess(abs(arch_spectral_symbol(t)-arch_spectral_symbol(-t)),mp.mpf('1e-33'))
            self.assertLess(abs((arch_spectral_symbol(t,conductor=5)-arch_spectral_symbol(t))-mp.log(5)),mp.mpf('1e-33'))

    def test_arch_spectral_symbol_wrong_parity_is_visible(self):
        # Parity remains distinct, but its high-frequency signature can shrink.
        for u,threshold in ((0,'0.01'),(1,'0.01'),(9,'1e-13')):
            self.assertGreater(abs(arch_spectral_symbol(u,parity=1)-arch_spectral_symbol(u,parity=0)),mp.mpf(threshold))

    def test_contact_constant_not_logpi(self):
        mp.mp.dps=40
        self.assertLess(abs((arch_contact()+mp.euler+mp.log(mp.pi))+2*mp.log(2)),mp.mpf('1e-30'))

    def test_arch_kernel_is_positive_but_signed_arch_form(self):
        for x in (Q(1,20),Q(1,2),Q(3)):
            self.assertGreater(arch_real_kernel(x),0)
        self.assertLess(arch_exponential_resolvent(2),0)

    def test_arch_density_small_x_has_finite_contact_limit(self):
        a=Q(2,5)
        h=lambda x:tent_convolution(x,a)
        mp.mp.dps=55
        h0=mp.mpf(4)/15
        self.assertLess(abs(arch_integrand(h,h0,0)-h0/2),mp.mpf('1e-50'))
        for k in (3,5,8,12):
            x=mp.mpf(10)**(-k)
            self.assertLess(abs(arch_integrand(h,h0,x)-h0/2),mp.mpf('3')*x)

    def test_arch_c2_envelope_exact(self):
        for a in (Q(1,4),Q(2,5),Q(4,5),Q(5,3)):
            h0,hsup,h2,C=tent_bounds(a)
            self.assertEqual(h0,2*a/3)
            self.assertEqual(h2,2/a)
            self.assertEqual(C,max(h0+2/a,4*h0))
            for x in (Q(1,100),Q(1,5),Q(1,2),Q(1),Q(3),Q(8)):
                h=lambda t:tent_convolution(t,a)
                self.assertLessEqual(abs(arch_renorm_density(h,mp.mpf(h0.numerator)/h0.denominator,x)),
                                     mp.mpf(C.numerator)/C.denominator*mp.mpf(x.numerator)/x.denominator+mp.mpf('1e-28'))

    def test_arch_ladder_bound_is_exact_rational(self):
        c=arch_c2_envelope(Q(1,3),Q(1,3),Q(5))
        for J in (1,2,4,16,64):
            b=arch_ladder_remainder_bound(c,J)
            self.assertIsInstance(b,Q)
            aa=Q(4*J+1,2)
            self.assertEqual(b,c*(1/(2*aa)+1/aa**2))
            if J>1:self.assertLess(b,arch_ladder_remainder_bound(c,1))
        with self.assertRaises(WeilTransportError):arch_ladder_remainder_bound(-1,2)

    def test_full_arch_ladder_vs_direct_integral_with_proved_enclosure(self):
        mp.mp.dps=40
        for width in (Q(1,4),Q(2,5),Q(4,5)):
            h=lambda x:tent_convolution(x,width)
            a=mp.mpf(width.numerator)/width.denominator
            h0=2*a/3
            direct=compact_arch(h,h0,[0,a,2*a],dps=42)
            C=tent_bounds(width)[3]
            for J in (1,5,20):
                approx=compact_arch(h,h0,[0,a,2*a],J=J,dps=42)
                bound=arch_ladder_remainder_bound(C,J)
                e=mp.mpf(bound.numerator)/bound.denominator
                self.assertLessEqual(abs(direct-approx),e)

    def test_compact_spectral_gamma_independent_oracle(self):
        aa=Q(2,5)
        mp.mp.dps=33
        x=mp.mpf(aa.numerator)/aa.denominator
        direct=compact_arch(lambda y:tent_convolution(y,aa),2*x/3,[0,x,2*x],dps=33)
        spectral=arch_spectral_tent_numeric(aa,cutoff=160,dps=33)
        self.assertLess(abs(direct-spectral),mp.mpf('1e-5'))

    def test_gamma_contact_wrong_normalization_changes_value(self):
        a=Q(2,5)
        z=compact_weil_tent(a,20)
        self.assertNotAlmostEqual(float(z['arch_ladder']),float(z['arch_ladder']+2*mp.log(2)),places=6)

    def test_invalid_arch_inputs_refused(self):
        h=lambda x:tent_convolution(x,Q(1,3))
        for par in (-1,2,True):
            with self.assertRaises(WeilTransportError):arch_spectral_symbol(0,parity=par)
        with self.assertRaises(WeilTransportError):arch_real_kernel(0)
        with self.assertRaises(WeilTransportError):compact_arch(h,Q(1),[0,-1,2])


class CompleteLogDerivativeTest(unittest.TestCase):
    def test_resolvent_gamma_from_three_independent_routes(self):
        mp.mp.dps=40
        for s in (Q(5,4),Q(3,2),Q(2),Q(3)):
            a=arch_exponential_resolvent(s)
            b=arch_resolvent_integral(s,dps=42)
            c=arch_resolvent_fourier(s,dps=42)
            self.assertLess(abs(a-b),mp.mpf('1e-34'))
            self.assertLess(abs(a-c),mp.mpf('1e-34'))

    def test_resolvent_ladder_signed_bound(self):
        for s in (Q(5,4),Q(3,2),Q(2),Q(3),Q(5)):
            exact=arch_exponential_resolvent(s)
            for J in (1,2,5,20,50):
                approx=arch_resolvent_ladder(s,J)
                self.assertGreaterEqual(exact-approx,-mp.mpf('1e-28'))
                self.assertLessEqual(exact-approx,arch_resolvent_ladder_error(s,J))

    def test_pole_resolvent_two_actual_poles(self):
        for s in (2,3,5):
            self.assertAlmostEqual(float(pole_resolvent(s)),float(2/Q(s)+2/Q(s-1)),places=13)

    def test_completed_weil_from_heat_matches_independent_xi_for_all_tests(self):
        for s,N in ((Q(3,2),2000),(Q(2),1000),(Q(3),500),(Q(4),100)):
            full=independent_xi_logderivative(s)
            via=complete_logderivative_from_heat(s,N)
            tail=prime_heat_tail_bound(s,N)
            self.assertLess(abs(full-via),2*tail)

    def test_two_false_routes_are_rejected(self):
        mp.mp.dps=40;s=3
        correct=independent_xi_logderivative(s)
        primepart=heat_mellin_prime_fraction(s,300)
        # Naive gamma multiplication (rather than normalization and log deriv.)
        wrong=heat_mellin_normalization(s)*primepart
        self.assertGreater(abs(correct-wrong),mp.mpf('0.02'))
        # Drop Γ contact and 0,1 poles: pure prime current is not full Weil.
        self.assertGreater(abs(correct+2*primepart),mp.mpf('0.1'))

    def test_halfdensity_mutations_visible(self):
        mp.mp.dps=42
        for shift in (Q(0),Q(1)):
            self.assertGreater(abs(half_density_mutation_defect(3,150,shift)),mp.mpf('0.01'))
        self.assertLess(abs(half_density_mutation_defect(3,150,Q(1,2))),mp.mpf('1e-40'))

    def test_laplace_measures_differ_for_fake6(self):
        for s in (Q(3,2),Q(2),Q(3)):
            expected=-2*mp.log(6)*mp.power(6,-mp.mpf(s.numerator)/s.denominator)
            self.assertLess(abs(fake_composite6_resolvent_defect(s)-expected),mp.mpf('1e-33'))

    def test_positive_heat_and_gamma_do_not_force_mutant_weil_sign(self):
        s=2
        genuine=independent_xi_logderivative(s).real
        fake=genuine+fake_composite6_resolvent_defect(s,delta=100)
        self.assertGreater(genuine,0)
        self.assertLess(fake,0)

    def test_conductor_parity_delta_preserved_from_gamma(self):
        s=2
        even=arch_exponential_resolvent(s)
        odd=arch_exponential_resolvent(s,conductor=5,parity=1)
        delta=mp.log(5)+mp.digamma(mp.mpf('1.5'))-mp.digamma(1)
        self.assertLess(abs(odd-even-delta),mp.mpf('1e-30'))
        self.assertLess(abs(arch_spectral_parity_conductor_resolvent(2,5,1)-odd),mp.mpf('1e-30'))

    def test_reject_unsourced_exits(self):
        for x in (1,Q(1,2),0):
            with self.assertRaises(WeilTransportError):complete_logderivative_from_heat(x,20)
            with self.assertRaises(WeilTransportError):independent_xi_logderivative(x)
            with self.assertRaises(WeilTransportError):arch_exponential_resolvent(x)
            with self.assertRaises(WeilTransportError):pole_resolvent(x)


class CompactWeilActualityTest(unittest.TestCase):
    def test_prime_source_locally_finite_exact_windows(self):
        cases=[(Q(1,4),()),(Q(2,5),(2,)),(Q(3,5),(2,3)),(Q(4,5),(2,3,4))]
        for aa,primes in cases:
            z=compact_weil_tent(aa,8)
            self.assertEqual(z['prime_support'],primes)
            self.assertTrue(z['genuine'])

    def test_compact_h_genuine_weil_interval_from_arch_tail(self):
        a=Q(4,5)
        z=compact_weil_tent(a,15)
        h=lambda x:tent_convolution(x,a)
        alpha=mp.mpf(a.numerator)/a.denominator
        direct=compact_arch(h,z['h0'],[0,alpha,2*alpha],dps=42)
        true_eval=z['pole']+z['prime']+direct
        self.assertLess(abs(true_eval-z['q_ladder']),z['error_bound'])
        self.assertEqual(z['prime_support'],(2,3,4))

    def test_fake6_mutant_changes_only_one_off_diagonal_impulse(self):
        a=Q(1)
        original=compact_weil_tent(a,20)
        bad=compact_weil_tent(a,20,fake6=1)
        h=tent_convolution(mp.log(6),a)
        predicted=-2*mp.log(6)*mp.power(6,-mp.mpf('0.5'))*h
        self.assertLess(abs(bad['q_ladder']-original['q_ladder']-predicted),mp.mpf('1e-33'))
        self.assertFalse(bad['genuine'])
        self.assertAlmostEqual(float(bad['pole']),float(original['pole']),places=12)
        self.assertAlmostEqual(float(bad['arch_ladder']),float(original['arch_ladder']),places=12)

    def test_drop_poles_or_change_halfdensity_fails_identity(self):
        a=Q(1)
        true=compact_weil_tent(a,9)
        no=compact_weil_tent(a,9,omit_poles=True)
        wrong=compact_weil_tent(a,9,half_density=Q(0))
        self.assertLess(abs(true['q_ladder']-no['q_ladder']-true['pole']),mp.mpf('1e-34'))
        self.assertGreater(abs(true['q_ladder']-wrong['q_ladder']),mp.mpf('0.1'))
        self.assertFalse(no['genuine'])
        self.assertFalse(wrong['genuine'])

    def test_no_prime_on_compact_short_window(self):
        a=Q(1,4)
        z=compact_weil_tent(a,J=30)
        self.assertEqual(z['prime_support'],())
        self.assertEqual(z['prime'],0)
        self.assertGreater(z['error_bound'],0)

    def test_independent_mellin_halfdensity_chart(self):
        for aa in (Q(1,3),Q(3,4)):
            for u in (0,Q(1,2),2):
                observed=halfdensity_mellin_tent(aa,u)
                predicted=additive_tent_fourier(aa,u)
                self.assertLess(abs(observed-predicted),mp.mpf('1e-25'))
            mutant=halfdensity_mellin_tent(aa,2,offset=Q(1))
            true=additive_tent_fourier(aa,2)
            self.assertGreater(abs(mutant-true),mp.mpf('0.001'))


class AcceleratedSignedWeilTest(unittest.TestCase):
    def test_accelerated_bound_exact_rational_and_rate(self):
        for a in (Q(1,4),Q(2,5),Q(4,5)):
            h0,H,M2,C=tent_bounds(a)
            old=arch_ladder_remainder_bound(C,32)
            corrected=accelerated_arch_c2_remainder_bound(h0,M2,32)
            self.assertIsInstance(corrected,Q)
            self.assertLess(corrected,old)
            z=accelerated_arch_c2_remainder_bound(h0,M2,64)
            self.assertLess(z/Q(corrected),Q(1,3))

    def test_corr_bound_against_independently_integrated_full_arch(self):
        mp.mp.dps=44
        for a in (Q(1,4),Q(2,5),Q(4,5)):
            h=lambda x:tent_convolution(x,a)
            aa=mp.mpf(a.numerator)/a.denominator
            h0=2*aa/3
            A=compact_arch(h,h0,[0,aa,2*aa],dps=44)
            for J in (1,3,10,30):
                AJ=compact_arch(h,h0,[0,aa,2*aa],J=J,dps=44)
                corr=renormalized_arch_ladder(AJ,h0,J)
                bound=accelerated_arch_c2_remainder_bound(tent_bounds(a)[0],tent_bounds(a)[2],J)
                self.assertLess(abs(A-corr),mp.mpf(bound.numerator)/bound.denominator)

    def test_uniform_sobolev_form_bound(self):
        mp.mp.dps=38
        for a in (Q(1,4),Q(2,5),Q(4,5)):
            aa=mp.mpf(a.numerator)/a.denominator
            h=lambda x:tent_convolution(x,a)
            h0=2*aa/3
            norm2=2*aa/3+2/aa  # exact H1 norm squared of triangular source
            exact=compact_arch(h,h0,[0,aa,2*aa],dps=38)
            for J in (2,5,20):
                approx=compact_arch(h,h0,[0,aa,2*aa],J=J,dps=38)
                eps=sobolev_operator_ladder_bound(J)
                self.assertLess(abs(exact-renormalized_arch_ladder(approx,h0,J)),
                                mp.mpf(eps.numerator)/eps.denominator*norm2)
                self.assertLess(eps,sobolev_operator_ladder_bound(J,accelerated=False))

    def test_corrected_operator_norm_rate(self):
        for J in (1,2,4,8,16,64):
            accelerated=sobolev_operator_ladder_bound(J)
            uncorrected=sobolev_operator_ladder_bound(J,accelerated=False)
            self.assertGreater(accelerated,0)
            self.assertLess(accelerated,uncorrected)
        for J in (16,32,64):
            self.assertLess(sobolev_operator_ladder_bound(2*J)/sobolev_operator_ladder_bound(J),Q(1,3))

    def test_wrong_counterterm_sign_misses_fast_convergence(self):
        a=Q(2,5);aa=mp.mpf(2)/5
        h=lambda x:tent_convolution(x,a)
        direct=compact_arch(h,2*aa/3,[0,aa,2*aa])
        J=80
        AJ=compact_arch(h,2*aa/3,[0,aa,2*aa],J=J)
        correct=renormalized_arch_ladder(AJ,2*aa/3,J)
        wrong=AJ+2*aa/(3*(4*J+1))
        self.assertLess(abs(correct-direct),abs(wrong-direct))

    def test_source_mutation_survives_arch_renormalization(self):
        a=Q(1);J=20
        t=compact_weil_tent(a,J)
        m=compact_weil_tent(a,J,fake6=5)
        self.assertGreater(abs(m['q_ladder']-t['q_ladder']),0)
        self.assertLess(abs((m['q_ladder']-t['h0']/(4*J+1))-
                            (t['q_ladder']-t['h0']/(4*J+1))-
                            (m['prime']-t['prime'])),mp.mpf('1e-30'))

    def test_bad_norm_or_level_refused(self):
        for args in ((-1,1,1),(1,-1,2),(1,1,0)):
            with self.assertRaises(WeilTransportError):accelerated_arch_c2_remainder_bound(*args)
        with self.assertRaises(WeilTransportError):sobolev_operator_ladder_bound(0)
        with self.assertRaises(WeilTransportError):renormalized_arch_ladder(0,1,0)



if __name__=='__main__':
    unittest.main()

class SourceScrewBridgeTest(unittest.TestCase):
    def test_elementary_screw_gamma_rungs_are_exact_integrals(self):
        from observational_succ.completed_weil_transport import screw_rung_integral
        mp.mp.dps=42
        for R in (Q(1,4),Q(1),Q(2)):
            rr=mp.mpf(R.numerator)/R.denominator
            for j in (0,1,3):
                f=lambda x:(max(mp.mpf(0),rr-x)-rr*mp.exp(-x/2))*mp.exp(-(2*j+mp.mpf('0.5'))*x)
                integral=mp.quad(f,[0,rr,mp.inf])
                self.assertLess(abs(screw_rung_integral(R,j)-integral),mp.mpf('1e-32'))

    def test_screw_source_vs_independent_full_integral_with_remainder(self):
        from observational_succ.completed_weil_transport import (
            screw_potential_J,screw_potential_full_integral,screw_potential_remainder_bound)
        for R in (Q(1,4),Q(1),Q(3,2),Q(2),Q(5,2)):
            rr=mp.mpf(R.numerator)/R.denominator
            target=screw_potential_full_integral(rr,dps=44)
            for J in (1,5,20):
                approx=screw_potential_J(rr,J,dps=44)
                e=screw_potential_remainder_bound(R,J)
                self.assertLess(abs(target-approx),mp.mpf(e.numerator)/e.denominator)

    def test_screw_zero_and_symmetric_kernel(self):
        from observational_succ.completed_weil_transport import screw_potential_J,screw_kernel_J
        for J in (2,8):
            self.assertEqual(screw_potential_J(0,J),0)
            for x,y in ((Q(1,3),Q(2,3)),(Q(1),Q(2))):
                self.assertLess(abs(screw_kernel_J(x,y,J)-screw_kernel_J(y,x,J)),mp.mpf('1e-28'))
                self.assertEqual(screw_kernel_J(x,0,J),0)

    def test_screw_second_derivative_regular_source(self):
        from observational_succ.completed_weil_transport import screw_regular_density,screw_potential_J
        mp.mp.dps=43
        for R in (Q(1,4),Q(7,8),Q(3,2),Q(2)):
            rr=mp.mpf(R.numerator)/R.denominator
            for J in (3,20):
                f=lambda x:screw_potential_J(x,J,dps=43)
                # Finite difference is a calibration, NOT the universal proof;
                # the source potential resets its own precision and therefore
                # should not be passed to mp.diff's complex-step machinery.
                step=mp.mpf('0.00003')
                empirical=(f(rr+step)-2*f(rr)+f(rr-step))/(step*step)
                predicted=screw_regular_density(rr,J)
                self.assertLess(abs(empirical-predicted),mp.mpf('1e-5'))
            exact=screw_regular_density(rr)
            self.assertLess(abs(exact-screw_regular_density(rr,50)),mp.mpf('1e-6'))

    def test_at_prime_powers_density_must_not_erase_delta_atoms(self):
        from observational_succ.completed_weil_transport import screw_regular_density
        with self.assertRaises(WeilTransportError):screw_regular_density(mp.log(2))
        with self.assertRaises(WeilTransportError):screw_regular_density(mp.log(4))
        with self.assertRaises(WeilTransportError):screw_regular_density(0)

    def test_source_mutant_screw_is_exact_prime_form_kink(self):
        from observational_succ.completed_weil_transport import screw_potential_J
        mp.mp.dps=42
        for R in (Q(1),Q(2),Q(3)):
            a=screw_potential_J(R,20)
            b=screw_potential_J(R,20,fake6=3)
            rr=mp.mpf(R.numerator)/R.denominator
            predicted=-3*mp.log(6)/mp.sqrt(6)*max(mp.mpf(0),rr-mp.log(6))
            self.assertLess(abs(b-a-predicted),mp.mpf('1e-30'))

    def test_positive_fake_source_coefficients_and_multiplicativity_failure(self):
        from observational_succ.completed_weil_transport import fake6_positive_dirichlet_coefficient as c
        for n in range(1,301):
            self.assertGreaterEqual(c(n),1)
        self.assertEqual(c(1),1)
        self.assertEqual(c(2),c(3))
        self.assertEqual(c(2)*c(3),1)
        self.assertEqual(c(6),1001)
        self.assertEqual(c(12),1001)
        self.assertEqual(c(36),Q(1)+Q(1000)+Q(1000**2,2))

    def test_analytic_negative_mutant_certificate_independent_of_numerical_eigen(self):
        from observational_succ.completed_weil_transport import (
            fake6_negative_screw_certificate,screw_potential_J,screw_potential_remainder_bound)
        b=fake6_negative_screw_certificate(1000)
        self.assertLess(b,0)
        # Strict analytic bound Psi_fake(2)<17-1000/30; K(2,2)=2Psi_fake(2)<0.
        observed=screw_potential_J(2,30,fake6=1000)
        tail=screw_potential_remainder_bound(Q(2),30)
        self.assertLess(observed+mp.mpf(tail.numerator)/tail.denominator,0)
        with self.assertRaises(WeilTransportError):fake6_negative_screw_certificate(-1)

class GlobalSourceLawFirewallTest(unittest.TestCase):
    def test_fake6_mutant_same_zeros_not_same_completed_source(self):
        from observational_succ.completed_weil_transport import fake6_reflection_log_defect
        self.assertEqual(fake6_reflection_log_defect(2,1),Q(1,36)-6)
        self.assertNotEqual(fake6_reflection_log_defect(2,1000),0)
        self.assertEqual(fake6_reflection_log_defect(2,0),0)
        # exp(delta*6^-s) never vanishes but is not invariant under s->1-s.
        self.assertEqual(fake6_reflection_log_defect(1,1),Q(1,6)-1)
        # Independent exact rational Taylor witness: e^(19/10)>6,
        # so log(6)<19/10. No floating approximation is needed.
        from math import factorial
        self.assertGreater(sum((Q(19,10)**k/factorial(k) for k in range(5)),Q(0)),6)

    def test_frozen_source_receipt_and_mutation_rejection(self):
        import json
        from pathlib import Path
        from scripts.completed_weil_transport_probe import exact_receipt
        path=Path(__file__).resolve().parents[1]/'research/2026-10-14/COMPLETED_WEIL_RECEIPT.json'
        frozen=json.loads(path.read_text(encoding='utf-8'))
        replay=exact_receipt()
        self.assertEqual(replay,frozen)
        self.assertFalse(replay['claims']['zero_positions_read_or_guessed'])
        mutant=json.loads(json.dumps(replay))
        mutant['claims']['full_Weil_positivity']='PROVED'
        self.assertNotEqual(mutant,frozen)
