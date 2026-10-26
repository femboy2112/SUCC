"""Adversarial exact certificates for phase-labelled null SUCC structures.

Independent algebraic/direct-path oracles; not a π-normality claim.
"""
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ import seinfeld_phase as P


def original_bbp_states(depth: int) -> tuple[Q, ...]:
    """Independent literal four-pole source definition; no input pi digits."""
    states = [Q()]
    for j in range(1, depth+1):
        forcing = Q(4,8*j-7)-Q(2,8*j-4)-Q(1,8*j-3)-Q(1,8*j-2)
        states.append(16*states[-1] + forcing)
    return tuple(states)


class UnitPhaseCover(unittest.TestCase):
    def test_root_phase_fibers_double(self):
        for k in range(8):
            roots = P.root_turns(k)
            self.assertEqual(len(roots),2**k)
            self.assertEqual(len(set(roots)),2**k)
            self.assertTrue(all(0 <= x < 1 and ((2**k)*x).denominator == 1 for x in roots))
            self.assertEqual(roots[0],0)

    def test_original_anchor_u_eq_one_still_unique(self):
        for k in range(1,7):
            self.assertEqual([phase for phase in P.root_turns(k) if phase==0],[0])

    def test_formal_integer_polynomial(self):
        for k in range(7):
            coeff=P.root_power_defect(k)
            m=2**k
            self.assertEqual(len(coeff),m+1)
            self.assertEqual((coeff[0],coeff[-1]),(-1,1))
            self.assertTrue(all(v==0 for v in coeff[1:-1]))
            self.assertEqual(sum(coeff[j]*2**j for j in range(m+1)),2**m-1)

    def test_unit_phase_jet_in_ideal_mod_ideal_squared(self):
        for m in (1,2,3,4,8,16,31):
            coeff=P.jet_of_unit_relation(m,3)
            self.assertEqual(coeff,(0,m,comb(m,2)))
            eps=Q(1,128)
            # Exact independent evaluation of the first two Taylor jets.
            val=(1+eps)**m-1
            low=m*eps+comb(m,2)*eps**2
            self.assertEqual((val-low)/eps**3, sum((Q(comb(m,j))*eps**(j-3) for j in range(3,m+1)),Q()))

    def test_bad_inputs_fail_closed(self):
        for f,args in [(P.root_turns,(-1,)),(P.jet_of_unit_relation,(0,2)),
                       (P.root_power_defect,(21,)),(P.jet_of_unit_relation,(2,0))]:
            with self.assertRaises(P.PhaseSourceError): f(*args)


class FrobeniusThickening(unittest.TestCase):
    def test_single_geometric_point_nontrivial_nilpotent_algebra(self):
        for k in range(1,9):
            report=P.frobenius_thickening(k)
            self.assertEqual((report['rank'],report['nilpotency_index']), (2**k,2**k))
            self.assertEqual(report['geometric_points_over_algebraic_closure'],1)
            self.assertTrue(report['unit_power_one'])
            self.assertTrue(report['top_nonzero'])
            self.assertTrue(report['top_zero'])

    def test_frobenius_freshman_dream_exact_mod_two(self):
        for k in range(1,8):
            m=2**k
            self.assertEqual(P.gf2_nilpotent_power(3,m,m),1)
            self.assertEqual(P.gf2_nilpotent_power(2,m-1,m),1<<(m-1))
            self.assertEqual(P.gf2_nilpotent_power(2,m,m),0)
            self.assertTrue(all(comb(m,j)%2==0 for j in range(1,m)))

    def test_frobenius_not_same_as_complex_phase_root_count(self):
        for k in range(1,6):
            self.assertEqual(len(P.root_turns(k)),2**k)
            self.assertEqual(P.frobenius_thickening(k)['geometric_points_over_algebraic_closure'],1)


class PhaseTwistAndCoherence(unittest.TestCase):
    def test_single_prime_affine_path_is_projectively_twisted(self):
        for p in (2,3,5,7,11):
            for n in (1,2,17,p+2):
                a=Q(n+1,p)
                b=Q(n,p)
                self.assertEqual((a-b)%1,P.primitive_clock_affine_holonomy(n,p))
                self.assertEqual(P.primitive_clock_affine_holonomy(n,p),Q(1,p))

    def test_cross_prime_arbitrary_chosen_phases_are_not_coherent(self):
        self.assertEqual(P.naive_cross_prime_defect(1,2,3),Q(2,3))
        self.assertEqual(P.naive_cross_prime_defect(2,2,3),Q(1,3))
        self.assertEqual(P.naive_cross_prime_defect(7,3,5),
                         (Q(7,5)+Q(35,3)-Q(7,3)-Q(21,5))%1)

    def test_primitive_labels_require_primes(self):
        for call,args in [(P.primitive_clock_multiplier_phase,(1,4)),
                          (P.primitive_clock_affine_holonomy,(1,6)),
                          (P.naive_cross_prime_defect,(1,3,9))]:
            with self.assertRaises(P.PhaseSourceError):call(*args)

    def test_flat_prime_squares_reconstruct_global_potential(self):
        f=lambda n:Q(n*n+3*n,29)
        label=lambda p,n:(f(p*n)-f(n))%1
        reconstructed=P.flat_prime_potential(100,label)
        for n in range(1,101):
            self.assertEqual(reconstructed[n],(f(n)-f(1))%1)

    def test_independent_primitive_clocks_fail_full_prime_coherence(self):
        with self.assertRaisesRegex(P.PhaseSourceError,'incompatible all-prime phase'):
            P.flat_prime_potential(12,lambda p,n:Q(n,p))
        self.assertEqual(P.naive_cross_prime_defect(1,2,3),Q(2,3))

    def test_zero_phase_is_flat_but_noninformative(self):
        reconstructed=P.flat_prime_potential(48,lambda p,n:0)
        self.assertEqual(set(reconstructed),{Q(0)})

    def test_exact_global_potential_restores_prime_square(self):
        for f in (lambda x:Q(x*x,7),lambda x:Q(3*x*x+x,29)):
            for a,b in ((2,3),(3,5),(5,7),(2,2)):
                for n in range(1,9):
                    self.assertEqual(P.multiplier_square_defect(n,a,b,f),0)
                    expected=(f(a*b*n)-f(n))%1
                    self.assertEqual((P.multiplier_phase_from_source(n,b,f)+
                                      P.multiplier_phase_from_source(b*n,a,f))%1,expected)

    def test_nonzero_relative_phase_but_flat_full_gradient(self):
        source=lambda x:Q(x*x,11)
        self.assertEqual(P.relative_affine_phase(1,2,source),Q(9,11))
        for n in range(1,10):
            for p in (2,3,5):
                self.assertEqual(P.full_gradient_affine_holonomy(n,p,source),0)

    def test_gauge_reference_changes_relative_diagnostic(self):
        f=lambda n:Q(n*n,11)
        z=lambda n:Q(0)
        self.assertNotEqual(P.relative_affine_phase(1,2,f),P.relative_affine_phase(1,2,z))
        self.assertEqual(P.full_gradient_affine_holonomy(1,2,f),0)
        self.assertEqual(P.full_gradient_affine_holonomy(1,2,z),0)


class AuthenticatedSourceControls(unittest.TestCase):
    def test_original_source_mixed_lag_matches_direct_fourpole_oracle(self):
        states=original_bbp_states(61)
        f=lambda n:states[n]
        for p in (2,3,5):
            for n in range(1,12):
                if max(p*(n+1),2*p*n)>=len(states):continue
                raw=P.source_mixed_phase_lift(n,p,states)
                self.assertEqual(raw%1,P.relative_affine_phase(n,p,f))
                self.assertEqual(P.multiplier_square_defect(n,2,p,f),0)
                self.assertEqual(P.full_gradient_affine_holonomy(n,p,f),0)

    def test_counterfeit_phase_is_small_and_cannot_mix(self):
        source=P.counterfeit_unit_phase
        for p in (2,3,5):
            for n in (1,2,3,4,7,16,31,101):
                phi=P.counterfeit_mixed_phase_lift(n,p)
                self.assertEqual(phi%1,P.relative_affine_phase(n,p,source))
                self.assertLessEqual(abs(phi),P.counterfeit_relative_phase_bound(n,p))
                self.assertEqual(P.multiplier_square_defect(n,2,p,source),0)

    def test_counterfeit_has_nonzero_coherent_rel_phase_but_no_mixing(self):
        vals=[P.counterfeit_mixed_phase_lift(n,2) for n in range(1,65)]
        self.assertTrue(any(v!=0 for v in vals))
        self.assertLess(sum(map(abs,vals),Q()),Q(1,10))
        self.assertTrue(all(abs(v)<Q(1,16*n*n) for n,v in enumerate(vals,1)))

    def test_source_history_must_be_long_enough(self):
        with self.assertRaises(P.PhaseSourceError):
            P.source_mixed_phase_lift(4,5,original_bbp_states(5))

    def test_all_primitive_phases_are_rational_turns(self):
        for n in range(1,10):
            for p in (2,3,5,7):
                x=P.primitive_clock_multiplier_phase(n,p)
                y=P.primitive_clock_affine_holonomy(n,p)
                self.assertIsInstance(x,Q)
                self.assertIsInstance(y,Q)
                self.assertTrue(0<=x<1 and 0<=y<1)


if __name__=='__main__':
    unittest.main()
