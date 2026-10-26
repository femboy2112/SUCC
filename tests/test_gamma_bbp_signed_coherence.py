"""Hostile exact finite and independent numerical checks, not a normality proof."""
from __future__ import annotations

from fractions import Fraction as Q
import random
import unittest

from observational_succ.gamma_bbp_signed_coherence import (
    moment_anchor, signed_moment_crossing, centered_resolvent_certificate,
    authentic_orbit_rational, green_tail_prefix, green_tail_interval,
    finite_twisted_coboundary, summable_tail_budget, weyl_orbit_transport,
    synthetic_atomic_order_countermodel, GammaBridgeError,
)
from observational_succ.zero_one_gamma_bridge import (
    authentic_bbp_forcing, gamma_defect_interval,
)


def mpq(mp, q):
    return mp.mpf(q.numerator)/q.denominator


class SignedMomentAnchorTests(unittest.TestCase):
    def test_exact_source_unit_anchor_at_zero(self):
        a=moment_anchor(0,terms=28)
        self.assertEqual(a.b_moment,Q(47,15))
        self.assertEqual(a.source_id,"Q:Coherent-Main-X-four-pole-BBP")
        import mpmath as mp
        with mp.workdps(90):
            truth=mpq(mp,Q(47,15))/(1-mp.log(2))
            self.assertLess(mpq(mp,a.normalizer.lower),truth)
            self.assertGreater(mpq(mp,a.normalizer.upper),truth)
            self.assertLess(a.normalizer.width,Q(1,10**15))

    def test_moment_ratio_strictly_increases_with_correct_intervals(self):
        previous=None
        for k in (0,1,2,3,4,8,12,30,60):
            a=moment_anchor(k,terms=36)
            if previous is not None:
                self.assertLess(previous.normalizer.upper,a.normalizer.lower)
            previous=a

    def test_signed_cross_two_by_two_determinants_strict_positive(self):
        for k in range(12):
            for lag in range(1,8):
                q=signed_moment_crossing(k,lag,terms=31)
                self.assertTrue(q.strictly_positive)
                self.assertGreater(q.determinant.lower,0)
                self.assertGreater(q.normalized_signed_moment.lower,0)
                self.assertEqual(q.k,k)
                self.assertEqual(q.lag,lag)

    def test_independent_mpmath_determinant_matches_interval(self):
        import mpmath as mp
        with mp.workdps(260):
            for k,lag in ((0,1),(0,5),(2,3),(8,4),(18,7)):
                q=signed_moment_crossing(k,lag,terms=35)
                x=lambda j:mp.mpf(8*j+1)
                g=lambda j:1/x(j)-mp.log1p(1/x(j))
                b=lambda j:mpq(mp,authentic_bbp_forcing(j+1))
                det=b(k+lag)*g(k)-b(k)*g(k+lag)
                self.assertLess(mpq(mp,q.determinant.lower),det)
                self.assertGreater(mpq(mp,q.determinant.upper),det)

    def test_small_parameter_resolvent_has_positive_signed_residual(self):
        import mpmath as mp
        with mp.workdps(105):
            pi_gamma=mp.fsum(mp.power(16,-j)*(1/mp.mpf(8*j+1)-mp.log1p(1/mp.mpf(8*j+1)))
                             for j in range(110))
            delta=mp.pi-mpq(mp,Q(47,15))/(1-mp.log(2))*pi_gamma
            self.assertGreater(delta,0)
            for depth in (2,3,5,9,16):
                c=centered_resolvent_certificate(0,depth=depth,terms=33)
                self.assertTrue(c.pi_anchor_at_zero)
                self.assertGreater(c.signed_resolvent.lower,0)
                self.assertLessEqual(mpq(mp,c.signed_resolvent.lower),delta)
                self.assertGreaterEqual(mpq(mp,c.signed_resolvent.upper),delta)
                self.assertEqual(len(c.finite_positive_terms),depth-1)

    def test_shifted_anchor_positive_at_every_registered_k(self):
        for k in (0,1,2,4,9):
            c=centered_resolvent_certificate(k,depth=7,terms=35)
            self.assertGreater(c.signed_resolvent.lower,0)
            self.assertLess(c.signed_resolvent.width,Q(1,10))
            self.assertEqual(c.pi_anchor_at_zero,k==0)

    def test_invalid_source_charts_rejected(self):
        for f,args in ((moment_anchor,(-1,)),(signed_moment_crossing,(0,0)),
                       (centered_resolvent_certificate,(-1,))):
            with self.assertRaises(GammaBridgeError):f(*args)
        with self.assertRaises(GammaBridgeError):centered_resolvent_certificate(0,parameter=Q(1))
        with self.assertRaises(GammaBridgeError):centered_resolvent_certificate(0,parameter=.0625)


class AuthenticGreenTailTests(unittest.TestCase):
    def test_forward_source_matches_independent_four_pole_polynomial(self):
        state=Q(0)
        for n in range(1,65):
            r=Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(r,authentic_bbp_forcing(n))
            state=16*state+r
            self.assertEqual(authentic_orbit_rational(n),state)

    def test_finite_twisted_coboundary_is_exact_at_unmatched_depths(self):
        for n in (0,1,2,5,15,40):
            for depth in (1,2,3,9,16):
                left,right,source=finite_twisted_coboundary(n,depth)
                self.assertEqual(left-right,source)
                self.assertEqual(source,authentic_bbp_forcing(n+1))

    def test_green_tail_brackets_and_independent_pi_reference(self):
        import mpmath as mp
        with mp.workdps(125):
            for n in (0,1,2,4,9,20):
                u=authentic_orbit_rational(n)
                t=green_tail_interval(n,16)
                truth=mp.power(16,n-1)*mp.pi-mpq(mp,u)
                self.assertGreater(truth,0)
                self.assertLess(mpq(mp,t.lower),truth)
                self.assertGreater(mpq(mp,t.upper),truth)

    def test_green_tail_is_strictly_decreasing_and_positive(self):
        previous=None
        for n in range(25):
            t=green_tail_interval(n,18)
            self.assertGreater(t.lower,0)
            if previous is not None:
                self.assertLess(t.upper,previous.lower)
            previous=t

    def test_summable_tail_mass_sharper_than_uniform_envelope(self):
        universal=Q(17,648)
        old=None
        for K in (0,2,8,16,32,64):
            c=summable_tail_budget(K,depth=14)
            self.assertEqual(c.absolute_upper_by_source,universal)
            self.assertLessEqual(c.mass.upper,universal)
            self.assertLess(c.mass.lower,c.mass.upper)
            if old is not None:
                self.assertLess(c.mass.upper,old.mass.upper)
                self.assertGreater(c.mass.lower,old.mass.lower)
            old=c
        self.assertLess(old.mass.upper,Q(17,1000))

    def test_weyl_phase_bound_is_uniform_in_horizon(self):
        for N in (1,2,10,100,100000):
            b=weyl_orbit_transport(3,N,prefix_count=16,depth=12)
            self.assertEqual(b.uniform_absolute_sum_error,7*3*b.tail_mass.upper)
            self.assertEqual(b.normalized_error,b.uniform_absolute_sum_error/N)
            self.assertFalse(b.cancellation_established)
            self.assertLess(b.uniform_absolute_sum_error,Q(1,2))
        with self.assertRaises(GammaBridgeError):weyl_orbit_transport(0,5)
        with self.assertRaises(GammaBridgeError):weyl_orbit_transport(1,0)

    def test_complex_weyl_difference_checked_against_independent_machin(self):
        # Independent rational Machin value; strictly a holdout diagnostic.
        import mpmath as mp
        with mp.workdps(140):
            atan=lambda b,n:sum((Q((-1)**k,(2*k+1)*b**(2*k+1))
                                  for k in range(n)),Q())
            pi_frac=16*atan(5,115)-4*atan(239,60)
            pi_ref=mpq(mp,pi_frac)
            self.assertLess(abs(pi_ref-mp.pi),mp.mpf('1e-120'))
            for h in (1,2,3):
                total_real=total_rational=0j
                for N in range(1,21):
                    u=authentic_orbit_rational(N)
                    real=mp.power(16,N-1)*pi_ref
                    def phase(x):return mp.exp(2j*mp.pi*h*mp.frac(x))
                    total_real+=phase(real)
                    total_rational+=phase(mpq(mp,u))
                    cap=weyl_orbit_transport(h,N, prefix_count=16,depth=14).uniform_absolute_sum_error
                    self.assertLess(abs(total_real-total_rational),mpq(mp,cap))

    def test_mutated_orbit_does_not_share_exact_original_lift(self):
        true=authentic_orbit_rational(3)
        # Changing even one authenticated source coefficient changes its lift.
        mutated=(16*(16*(authentic_bbp_forcing(1)+Q(1,100))+authentic_bbp_forcing(2))
                 + authentic_bbp_forcing(3))
        self.assertNotEqual(mutated,true)


class SourceBlindCountermodels(unittest.TestCase):
    def test_strict_signed_order_can_coexist_with_rational_nonnormal_value(self):
        c=synthetic_atomic_order_countermodel()
        self.assertTrue(c.strict_cross_moment_order)
        self.assertFalse(c.authentic)
        self.assertIsInstance(c.rational_resolvent,Q)
        self.assertGreater(c.rational_resolvent,0)
        self.assertGreater(c.rational_resolvent.denominator,1)
        # Every rational's eventual radix-16 period is finite, hence nonnormal.

    def test_two_atom_cross_determinants_independent_exact_oracle(self):
        c=synthetic_atomic_order_countermodel()
        moments=lambda items,k:sum((w*t**(8*k) for t,w in items),Q())
        for k in range(10):
            for lag in range(1,12):
                det=(moments(c.source_atoms,k+lag)*moments(c.gamma_atoms,k)-
                     moments(c.source_atoms,k)*moments(c.gamma_atoms,k+lag))
                self.assertGreater(det,0)

    def test_random_exact_signed_moments_source_gates(self):
        rng=random.Random(20261025)
        for _ in range(60):
            k=rng.randrange(0,45)
            lag=rng.randrange(1,12)
            det=signed_moment_crossing(k,lag,terms=30)
            self.assertGreater(det.normalized_signed_moment.lower,0)


if __name__=='__main__': unittest.main()


class EightResidueCarrierTests(unittest.TestCase):
    def test_eight_channel_gamma_exact_prefix_partition(self):
        from observational_succ.gamma_bbp_signed_coherence import gamma_residue_certificate
        for K in (1,2,5,12):
            finite_rows=[gamma_residue_certificate(a,K,terms=28)
                         for a in range(1,9)]
            assert all(c.finite_prefix.lower>0 for c in finite_rows)
            from observational_succ.zero_one_gamma_bridge import gamma_field_certificate
            full=gamma_field_certificate(Q(1),8*K,28)
            self.assertEqual(sum((c.finite_prefix.lower for c in finite_rows),Q()),
                             full.prefix.lower)
            self.assertEqual(sum((c.finite_prefix.upper for c in finite_rows),Q()),
                             full.prefix.upper)

    def test_residue_channels_exact_enclosures_match_gamma_identity(self):
        import mpmath as mp
        from observational_succ.gamma_bbp_signed_coherence import (
            gamma_residue_certificate, gamma_eight_channel_certificate,
        )
        with mp.workdps(130):
            for K in (1,3,8,20):
                full=gamma_eight_channel_certificate(K,terms=35)
                self.assertLess(mpq(mp,full.lower),mp.euler)
                self.assertGreater(mpq(mp,full.upper),mp.euler)
                for a in range(1,9):
                    c=gamma_residue_certificate(a,K,terms=35)
                    aa=mp.mpf(a)/8
                    analytic=mp.loggamma(aa+mp.mpf('0.125'))-mp.loggamma(aa)-mp.digamma(aa)/8
                    self.assertLess(mpq(mp,c.moment.lower),analytic)
                    self.assertGreater(mpq(mp,c.moment.upper),analytic)

    def test_signed_memory_excess_follows_same_zero_anchor(self):
        from observational_succ.gamma_bbp_signed_coherence import signed_green_memory_lower
        lower=signed_green_memory_lower(terms=40)
        self.assertGreater(lower,0)
        self.assertLess(lower,Q(1,10))
        import mpmath as mp
        with mp.workdps(115):
            a=mpq(mp,Q(47,15))/(1-mp.log(2))
            b=mp.nsum(lambda n:(1-mp.power(16,1-n))*(4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2))/15,[2,mp.inf])
            g=mp.nsum(lambda n:(1-mp.power(16,1-n))*(1/(8*n-7)-mp.log1p(1/(8*n-7)))/15,[2,mp.inf])
            self.assertLess(mpq(mp,lower),b-a*g)


class GeneralCarrierClosureTests(unittest.TestCase):
    def test_finite_generators_have_forward_backward_coherent_zeros(self):
        from observational_succ.gamma_bbp_signed_coherence import finite_green_source
        for b in (2,3,4,16,17):
            for source in ((Q(3,2),Q(-1,8),Q(2),Q(0)),
                           (Q(1),Q(0),Q(0)),
                           tuple(Q(k-5,17) for k in range(10))):
                v=finite_green_source(b,source)
                self.assertLessEqual(v.l1_green_actual,v.l1_operator_bound)
                self.assertEqual(v.source_orbit[0],0)
                for n in range(len(source)+1):
                    self.assertEqual(v.source_orbit[n]+v.green_potentials[n],
                                     b**n*v.green_potentials[0])

    def test_missing_source_and_unsupported_radix_fail_closed(self):
        from observational_succ.gamma_bbp_signed_coherence import finite_green_source
        for args in ((1,(Q(1),)),(16,()),(16,(.1,)),(True,(Q(1),))):
            with self.assertRaises(GammaBridgeError):finite_green_source(*args)

    def test_generic_source_is_not_authenticated_pi(self):
        from observational_succ.gamma_bbp_signed_coherence import finite_green_source
        v=finite_green_source(16,(Q(1),Q(1),Q(1),Q(1)))
        self.assertEqual(v.green_potentials[0],Q(4369,65536))
        self.assertNotEqual(v.source_orbit[-1],authentic_orbit_rational(4))
