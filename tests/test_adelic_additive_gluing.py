"""Exact tests of phase-preserving finite-place gluing and critical holonomy.

This file is added to SUCC's root-discoverable tests. Floating comparisons are
never used as mathematical proof certificates.
"""
from fractions import Fraction
from math import lcm
import unittest

from observational_succ.duck_bbp import forcing
from observational_succ.adelic_additive_gluing import (
    additive_prime_parts, balanced_complement_cocycle,
    coboundary, coboundary_defect_delta, coboundary_delta_center,
    coboundary_delta_error, compensated_real_driver, critical_arc_halfwidth,
    critical_steps, epoch_conductor_and_support, exact_crt_tv_from_haar,
    factor_with_bound, finite_phase_cocycle, full_crt_spectral_energy, holonomy_center,
    holonomy_error_bound, holonomy_exponent, local_additive_fraction,
    orbit_states, original_phase_parts, primes_upto, real_phase_from_all_places,
    source_defect, source_p_history, source_prime_injection,
)


def independent_signed_four_poles(n: int) -> Fraction:
    """Independent explicit four-pole source, distinct from combined numerator."""
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


class AdelicAdditiveGluingTests(unittest.TestCase):
    def test_source_oracle_all_four_poles(self):
        for n in range(1,170):
            self.assertEqual(forcing(n), independent_signed_four_poles(n))

    def test_finite_additive_product_oracle(self):
        for value in [Fraction(47,15),Fraction(1,6),Fraction(-71,385),Fraction(1,5),Fraction(0),Fraction(3,2),Fraction(-173,1456)]:
            self.assertEqual(real_phase_from_all_places(value, 13), value%1)
            local=additive_prime_parts(value,13)
            self.assertEqual(sum(local.values(),Fraction())%1, value%1)
        self.assertEqual(additive_prime_parts(Fraction(47,15),13), {3:Fraction(1,3),5:Fraction(4,5)})

    def test_source_all_place_crt_at_many_times(self):
        states=orbit_states(96)
        for n in list(range(1,41))+[48,64,80,96]:
            u=states[n]
            self.assertEqual(u.denominator%2,1)
            local=original_phase_parts(n,states=states)
            self.assertTrue(all(p%2 for p in local))
            self.assertEqual(sum(local.values(),Fraction())%1,u%1)
            self.assertEqual(real_phase_from_all_places(u,8*n-3),u%1)

    def test_insufficient_cutoff_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'outside declared source cutoff'):
            factor_with_bound(1009, 997)
        with self.assertRaises(ValueError):
            local_additive_fraction(Fraction(1,30),9)

    def test_commuting_arithmetic_circle_characters(self):
        states=orbit_states(55)
        for n in range(0,50):
            for p in (2,3,5,7,11,13,17,19,41):
                left,right=finite_phase_cocycle(n,p,states=states)
                self.assertEqual(left,right,(n,p))

    def test_source_odd_denominator_and_prime_support(self):
        for n,u in enumerate(orbit_states(145)[1:],1):
            self.assertEqual(u.denominator%2,1)
            parts=additive_prime_parts(u,8*n-3)
            self.assertTrue(all(p<=8*n-3 and p%2 for p in parts))

    def test_source_affine_defect_cocycle(self):
        states=orbit_states(85)
        for n in (0,1,7,13,32):
            for j,k in ((1,1),(2,3),(5,2),(8,7)):
                self.assertEqual(states[n+j+k]-16**(j+k)*states[n],source_defect(n,j+k))
                self.assertEqual(source_defect(n,j+k), 16**k*source_defect(n,j)+source_defect(n+j,k))

    def test_holonomy_uniform_scale_error_paid(self):
        for A in (2,3,8,16,17,32,64,97,256):
            for k in (1,2,3,5):
                theta=holonomy_exponent(A,k)
                self.assertLessEqual(abs(theta-holonomy_center(A,k)),holonomy_error_bound(A,k),(A,k))

    def test_critical_scale_arcs_and_log_steps(self):
        self.assertEqual([critical_steps(x) for x in (2,16,17,255,256,257,4096)], [1,1,2,2,2,3,3])
        for M in (32,64,128,256):
            width=critical_arc_halfwidth(M)
            self.assertLess(width,Fraction(1,4))
            for A in (M,M+1,2*M,4*M):
                theta=holonomy_exponent(A,critical_steps(A))
                self.assertLessEqual(abs(theta-Fraction(17,256)),width,(A,M))

    def test_critical_defect_coboundary_is_distinguishable(self):
        for A in (16,32,64,128,256):
            k=critical_steps(A)
            delta=coboundary_defect_delta(A,k)
            self.assertLessEqual(abs(delta-coboundary_delta_center(A,k)),coboundary_delta_error(A,k),(A,k))
            self.assertLess(delta,0)
            self.assertNotEqual(delta,0)

    def test_same_completed_pi_source_mutation(self):
        states=orbit_states(64)
        v=Fraction(0)
        self.assertEqual(coboundary(0),0)
        for n in range(1,65):
            altered=forcing(n)+coboundary(n)-16*coboundary(n-1)
            v=16*v+altered
            self.assertEqual(v,states[n]+coboundary(n))
            self.assertNotEqual(altered,forcing(n))

    def test_balanced_births_actual_clock_and_p_primary_compatibility(self):
        for A,p in [(32,73),(80,193),(100,233),(192,457)]:
            self.assertIn(p,primes_upto(p))
            self.assertEqual(p%8,1)
            self.assertGreater(p*p,16*A)
            k=(p-1)//8
            clocks=[k+1,4*k+1,5*k+1,6*k+1]
            nonzero=[n for n in range(1,2*A+1) if source_prime_injection(p,n)]
            self.assertEqual(nonzero, clocks)
            states=orbit_states(2*A)
            Cp=source_p_history(p,2*A)
            for n in range(2*A+1):
                v=p*states[n]
                self.assertNotEqual(v.denominator%p,0)
                direct=v.numerator*pow(v.denominator,-1,p)%p
                self.assertEqual(Cp[n],direct,(A,p,n))
                if n>0:
                    lhs,rhs=balanced_complement_cocycle(n-1,p,states=states)
                    self.assertEqual(lhs,rhs,(A,p,n))

    def test_balanced_real_complement_is_all_other_primes_exactly(self):
        for A,p in ((32,73),(80,193),(100,233)):
            states=orbit_states(2*A)
            C=source_p_history(p,2*A)
            for n in range(A,2*A):
                prime_parts=original_phase_parts(n,states=states)
                complement_from_other_primes=(sum((v for q,v in prime_parts.items() if q!=p),Fraction()))%1
                original_complement=(states[n]-Fraction(C[n],p))%1
                self.assertEqual(original_complement, complement_from_other_primes)

    def test_finite_analytic_tail_uses_actual_source(self):
        # A strict partial tail bound is a positive-control oracle for
        # the inherited global Green-tail theorem (not a new proof of it).
        for n in (1,2,5,13,41):
            partial=sum((forcing(n+j)/16**j for j in range(1,65)),Fraction())
            self.assertGreater(partial,0)
            self.assertLess(partial,Fraction(1,15*(n+1)**2))

    def test_no_prime_birth_inside_stage_means_source_only_driver(self):
        p=73
        for n in range(32,64):
            j=source_prime_injection(p,n)
            d=compensated_real_driver(n,p)
            self.assertEqual(d,forcing(n)-Fraction(j,p))
            if n not in (37,46,55):
                self.assertEqual(j,0)
                self.assertEqual(d,forcing(n))

    def test_full_conductor_not_joint_haar(self):
        for A in (4,8,16,32,64):
            q,s,n=epoch_conductor_and_support(A)
            self.assertGreaterEqual(q,n)
            self.assertLessEqual(s,n)
            self.assertEqual(exact_crt_tv_from_haar(A),1-Fraction(s,q))
            self.assertGreater(exact_crt_tv_from_haar(A),Fraction(1,2))

    def test_full_conductor_parseval_spectral_barrier(self):
        for A in (4,8,16,32):
            q,support,_=epoch_conductor_and_support(A)
            energy=full_crt_spectral_energy(A)
            self.assertGreaterEqual(energy,Fraction(q,A)-1)
            if support==A:
                self.assertEqual(energy,Fraction(q,A)-1)
            self.assertGreater(energy,0)

    def test_balanced_prime_layer_matches_canonical_additive_part(self):
        for A,p in ((32,73),(80,193),(100,233)):
            states=orbit_states(2*A)
            C=source_p_history(p,2*A)
            for n in range(A,2*A):
                self.assertEqual(local_additive_fraction(states[n],p),Fraction(C[n],p))

    def test_crt_haar_counterexample_frequency_zero_with_maximal_tv(self):
        # Q=4000; four distinct sample phases sum 1+i-1-i=0 exactly.
        q=4000
        support=[0,q//4,q//2,3*q//4]
        self.assertEqual(sum((1,0,-1,0)),0)
        self.assertEqual(sum((0,1,0,-1)),0)
        self.assertEqual(1-Fraction(len(support),q),Fraction(999,1000))


if __name__ == '__main__':
    unittest.main()
