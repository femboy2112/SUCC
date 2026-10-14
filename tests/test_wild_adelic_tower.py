"""Exact hostile tests of the WILD-ADELIC mathematical source tower.

The probes verify source-defined finite algebra, not externally certified 3D
embeddings, Pontryagin/CECH theorems or the Riemann Hypothesis.
"""
import unittest
from fractions import Fraction as F
from math import gcd

from observational_succ.wild_adelic_tower import (
    WildTowerError, TowerLaw, ExteriorEmbeddingContract,
    CohomologyWindingCertificate, fiber_isomorphism_on_finite_stage,
    finite_arithmetic_no_free_tail, rational_folner_energy,
    source_qualified_folner_energy,
    unbounded_filling_debt, pinched_tame_arc_inverse_lipschitz_bound,
)


def factorial():
    return TowerLaw('arithmetic/Z', 14, 'phase@one-real-place', 'factorial')


def dyadic():
    return TowerLaw('arithmetic/Z', 14, 'phase@one-real-place', 'constant', 2)


class TowerSourceAndLimits(unittest.TestCase):
    def test_source_law_fails_closed(self):
        with self.assertRaises(WildTowerError):
            TowerLaw('Z',0,'phase','unknown')
        with self.assertRaises(WildTowerError):
            TowerLaw('Z',0,'phase','constant',1)
        with self.assertRaises(WildTowerError):
            TowerLaw('Z',0,'phase','constant',2,(3,))
        with self.assertRaises(WildTowerError):
            TowerLaw('Z',0,'phase','prefix_constant',2,(1,))
        with self.assertRaises(WildTowerError):
            TowerLaw('Z',-1,'phase','factorial')

    def test_factorial_cofinal_denominators(self):
        s=factorial()
        self.assertEqual(tuple(s.D(n) for n in range(7)),
                         (1,2,6,24,120,720,5040))
        self.assertEqual(tuple(s.degree(n) for n in range(1,7)),
                         (2,3,4,5,6,7))
        self.assertEqual(s.localized_generator(5),F(1,720))
        for n in range(5):
            for k in range(n,7):
                self.assertEqual(s.stage_map(n,k)*s.D(n),s.D(k))

    def test_dyadic_not_universal(self):
        s=dyadic()
        self.assertEqual([s.D(n) for n in range(6)], [1,2,4,8,16,32])
        self.assertTrue(s.prime_unbounded(2))
        self.assertFalse(s.prime_unbounded(3))
        self.assertEqual(s.dual_kernel_order(12),3)
        self.assertTrue(s.scale_automorphism(4))
        self.assertFalse(s.scale_automorphism(6))

    def test_distinct_primes_not_q(self):
        s=TowerLaw('Z',0,'clock','distinct_primes')
        self.assertEqual([s.degree(n) for n in range(1,7)], [2,3,5,7,11,13])
        self.assertEqual(s.D(4),210)
        for p in (2,3,5,7,11,13):
            self.assertFalse(s.prime_unbounded(p))
            self.assertEqual(s.dual_kernel_order(p),p)
        self.assertFalse(s.scale_automorphism(30))

    def test_localization_membership_exact_against_stage_search(self):
        for s in (dyadic(),factorial(),TowerLaw('s',0,'b','constant',6),
                  TowerLaw('s',0,'b','prefix_constant',5,(2,3,8)),
                  TowerLaw('s',0,'b','distinct_primes')):
            for den in range(1,101):
                # Small denominators: the first 25 levels contain all
                # relevant small primes in the distinct-prime source.
                empirical = any(s.D(n)%den==0 for n in range(101 if s.kind == 'factorial' else 26))
                self.assertEqual(s.admits_rational(F(1,den)),empirical,
                                 (s.kind,den))
        self.assertTrue(factorial().admits_rational(F(17,120)))
        self.assertFalse(dyadic().admits_rational(F(17,120)))

    def test_finite_prime_occurrence_does_not_invert_p(self):
        s=TowerLaw('source',0,'angles','prefix_constant',5,(2,2,3))
        self.assertEqual(s.bounded_prime_depth(2),2)
        self.assertTrue(s.admits_rational(F(1,4)))
        self.assertFalse(s.admits_rational(F(1,8)))
        self.assertTrue(s.prime_unbounded(5))
        self.assertTrue(s.admits_rational(F(1,5**8)))
        self.assertEqual(s.dual_kernel_order(60),12)

    def test_constant_composite_is_structural_not_prime_euler(self):
        s=TowerLaw('Z',0,'clock','constant',6)
        self.assertTrue(s.scale_automorphism(2))
        self.assertTrue(s.scale_automorphism(3))
        self.assertFalse(s.scale_automorphism(5))
        with self.assertRaises(WildTowerError):
            s.prime_jet(6,3)
        self.assertEqual(s.prime_jet(3,4),(3,9,27,81))

    def test_automorphism_theorem_by_exact_finite_cokernel(self):
        for kind,constant in [('constant',2),('constant',6),('constant',15),('factorial',2),('distinct_primes',2)]:
            s=TowerLaw('s',0,'b',kind,constant)
            for m in range(1,37):
                self.assertEqual(s.scale_automorphism(m),s.dual_kernel_order(m)==1)
                self.assertEqual(m % s.dual_kernel_order(m),0)

    def test_prime_indexing_requires_a_genuine_prime(self):
        with self.assertRaises(WildTowerError): factorial().prime_unbounded(6)
        with self.assertRaises(WildTowerError): factorial().prime_jet(6,2)
        self.assertEqual(factorial().prime_jet(2,3),(2,4,8))


class SourceFlowAndGlobalInverse(unittest.TestCase):
    def test_real_flow_compatible(self):
        for s in (factorial(),dyadic()):
            for t in (F(0),F(2,7),F(-5,3),7,F(23,11)):
                self.assertTrue(s.compatible_phases(s.real_flow_phases(t,9)))

    def test_local_root_is_not_unique(self):
        s=factorial()
        n=3
        self.assertEqual(len({F(k,2) for k in range(2)}),2)
        self.assertTrue(s.scale_automorphism(2))
        self.assertTrue(s.scale_automorphism(30))
        # A finite circle has an m-element kernel for each positive integer m.
        self.assertEqual(len({F(k,6) for k in range(6)}),6)

    def test_deeper_levels_supply_true_inverse(self):
        s=factorial()
        for m in (2,3,4,6,10,12,30):
            for target in (F(1,7),F(-3,11),F(13,19)):
                for n in (0,1,2,5):
                    k=s.inverse_level(n,m)
                    self.assertEqual(s.stage_map(n,k)%m,0)
                    source=s.real_flow_phases(target,k)
                    y=s.inverse_coordinate(n,m,source)
                    self.assertEqual((m*y)%1,source[n])
                    self.assertEqual(y,s.real_flow_phases(target/m,n)[n])

    def test_inverse_unique_across_deeper_levels(self):
        s=factorial()
        n,m=4,15
        k=s.inverse_level(n,m)
        phases=s.real_flow_phases(F(11,13),k+5)
        base=s.inverse_coordinate(n,m,phases)
        for j in range(k,k+5):
            if s.stage_map(n,j)%m==0:
                self.assertEqual(base,(F(s.stage_map(n,j)//m)*phases[j])%1)

    def test_p_solenoid_shift_inverse(self):
        s=dyadic()
        theta=s.real_flow_phases(F(7,13),7)
        for n in range(6):
            self.assertEqual(s.inverse_level(n,2),n+1)
            self.assertEqual(s.inverse_coordinate(n,2,theta),theta[n+1])

    def test_noninvertible_multiplier_cannot_be_faked(self):
        for s,m in ((dyadic(),3),(TowerLaw('s',0,'b','distinct_primes'),2)):
            with self.assertRaises(WildTowerError): s.inverse_level(0,m)
            with self.assertRaises(WildTowerError): s.inverse_coordinate(0,m,s.real_flow_phases(1,8))

    def test_incompatible_source_phases_rejected(self):
        s=factorial()
        ph=list(s.real_flow_phases(F(5,9),8))
        ph[5]=(ph[5]+F(1,17))%1
        with self.assertRaises(WildTowerError): s.inverse_coordinate(0,3,tuple(ph))

    def test_wrong_report_type_rejected(self):
        s=factorial()
        with self.assertRaises(WildTowerError): s.real_flow_phases(0.1,3)
        self.assertFalse(s.compatible_phases((F(0), F(2,3))))

    def test_factorial_archimedean_profinite_bridge(self):
        s=factorial()
        for m in range(2,30):
            n=1
            while s.D(n)%m: n+=1
            for r in range(-m,m+1):
                self.assertEqual(s.delta_circle_root(m,r,n),r%m)
                self.assertEqual(s.finite_fiber_residues(r,n)[-1]%m,r%m)
                self.assertEqual((s.real_flow_phases(F(r,m),n)[0]*m)%1,F(0))
        with self.assertRaises(WildTowerError):
            dyadic().delta_circle_root(4,1,2)

    def test_nested_coordinate_fiber_reduction(self):
        s=factorial()
        for r in (-37,-1,0,1,57):
            for n in range(1,9):
                z=fiber_isomorphism_on_finite_stage(s,n,r)
                self.assertEqual((s.degree(n)*z)%1,fiber_isomorphism_on_finite_stage(s,n-1,r))


class AmbientEmbeddingAndCech(unittest.TestCase):
    def test_intrinsic_cohomology_integer_transport(self):
        for s in (dyadic(),factorial(),TowerLaw('s',0,'b','distinct_primes')):
            c=CohomologyWindingCertificate(s)
            for i in range(4):
                for j in range(i,8):
                    for w in (-7,0,1,17):
                        z,val=c.transport(i,j,w)
                        self.assertEqual(val,s.localization_value(i,w))
                        self.assertEqual(val,s.localization_value(j,z))

    def test_unknotted_meridian_requires_ambient_source(self):
        s=factorial()
        with self.assertRaises(WildTowerError):
            ExteriorEmbeddingContract(s,'exterior','OTHER',s.epoch,'unknotted_torus')
        with self.assertRaises(WildTowerError):
            ExteriorEmbeddingContract(s,'exterior',s.source_id,s.epoch+1,'unknotted_torus')
        with self.assertRaises(WildTowerError):
            ExteriorEmbeddingContract(s,'exterior',s.source_id,s.epoch,'wild_claim')
        unk=ExteriorEmbeddingContract(s,'standard nested cable',s.source_id,s.epoch,'unknotted_torus')
        for n in range(3):
            self.assertEqual(unk.meridian_transport(n,n+3,1),s.D(n+3)//s.D(n))
        unspecified=ExteriorEmbeddingContract(s,'unknown placement',s.source_id,s.epoch,'unspecified')
        with self.assertRaises(WildTowerError): unspecified.exterior_group_value(2,1)

    def test_two_models_same_arithmetic_group_different_source_authority(self):
        s=factorial()
        c=CohomologyWindingCertificate(s)
        u=ExteriorEmbeddingContract(s,'unknotted cable',s.source_id,s.epoch,'unknotted_torus')
        for i in range(5):
            self.assertEqual(c.transport(0,i,1)[1],u.exterior_group_value(i,s.D(i)))
        # Equality relies on TWO separate theorems: Cech continuity for the
        # intrinsic tower; unknotted embedding+meridian maps for its exterior.

    def test_euclidean_vs_rational_localization(self):
        s=factorial()
        for d in range(1,55):
            n=0
            while s.D(n)%d: n+=1
            self.assertEqual(s.localization_value(n,s.D(n)//d),F(1,d))
        dy=dyadic()
        for n in range(2,10):
            self.assertEqual(dy.localization_value(n,1),F(1,2**n))


class NoFreeTailAndHilbertSignFirewall(unittest.TestCase):
    def test_all_shared_prefixes_are_blind(self):
        for prefix in ((2,), (2,3,5), (2,3,5,7,11), (6,6,4,9)):
            result=finite_arithmetic_no_free_tail(prefix,2,3)
            self.assertTrue(result['p_invertible_if_p_tail'])
            self.assertFalse(result['p_invertible_if_r_tail'])
            self.assertEqual(result['prefix_product'],__import__('math').prod(prefix))
            self.assertFalse(result['source_law_equality_claimed'])

    def test_finite_prefix_of_q_does_not_prove_universal_prime_invertibility(self):
        n=8
        common=tuple(k+1 for k in range(1,n+1))
        a=TowerLaw('s',0,'b','prefix_constant',2,common)
        b=TowerLaw('s',0,'b','prefix_constant',3,common)
        self.assertEqual(tuple(a.degree(i) for i in range(1,n+1)), common)
        self.assertEqual(tuple(b.degree(i) for i in range(1,n+1)), common)
        self.assertTrue(a.scale_automorphism(2))
        self.assertFalse(b.scale_automorphism(2))

    def test_folner_exact_energy_tends_to_zero(self):
        steps=[(F(1,2),F(1)),(F(-2,3),F(2)),(F(4,5),F(1,7))]
        energies=[rational_folner_energy(steps,N) for N in (5,30,100,500)]
        self.assertEqual(energies[-1],F(2*(15+2*20)+F(1,7)*2*24,1001))
        self.assertTrue(all(x>y for x,y in zip(energies,energies[1:])))
        self.assertLess(energies[-1],F(1,5))
        self.assertEqual(rational_folner_energy([],2),0)

    def test_source_qualified_translation_folner(self):
        s=dyadic()
        steps=[(F(1,2),F(1)),(F(3,8),F(7,4))]
        self.assertEqual(source_qualified_folner_energy(s,steps,100),
                         rational_folner_energy(steps,100))
        with self.assertRaises(WildTowerError):
            source_qualified_folner_energy(s,[(F(1,3),F(1))],100)
        self.assertGreater(source_qualified_folner_energy(factorial(),[(F(1,3),F(1))],100),0)

    def test_folner_not_a_weil_sign_theorem(self):
        with self.assertRaises(WildTowerError):
            rational_folner_energy([(F(1,2),F(-1))],10)
        with self.assertRaises(WildTowerError):
            rational_folner_energy([(0.3,F(1))],10)
        with self.assertRaises(WildTowerError):
            rational_folner_energy([(F(1),F(1))],0)

    def test_tame_arc_condition_number_explodes(self):
        self.assertEqual([pinched_tame_arc_inverse_lipschitz_bound(n)
                          for n in range(1,9)], [2,4,8,16,32,64,128,256])
        with self.assertRaises(WildTowerError):
            pinched_tame_arc_inverse_lipschitz_bound(0)
        # One finite chart remains tame for every n, but its inverse
        # Lipschitz lower bound cannot remain uniformly bounded.

    def test_abstract_filling_debt_not_a_geometric_model(self):
        for bound in (1,4,12):
            t=unbounded_filling_debt(bound+1,bound)
            self.assertFalse(t['bounded_witness_exists'])
            self.assertEqual(t['first_unfillable_stage_for_budget'],bound+1)
            self.assertFalse(t['one_global_finite_witness_exists'])
            self.assertTrue(unbounded_filling_debt(bound,bound)['bounded_witness_exists'])


if __name__=='__main__':
    unittest.main()
