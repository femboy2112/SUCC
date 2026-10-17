"""Exact finite controls for clock cofinality, no-go and renewal source. """
import unittest
from fractions import Fraction as F
from observational_succ.source_minimality import (
    ClockTheory, SourceLawError, factor, divisors, finite_clock_closure,
    matching_finite_shadow, rooted_diagonal_orbit,
    missing_power_infinite_shadow, unique_pointed_clock_map,
    authenticate_prime_word)
from observational_succ.carry_clock_lift import CarryClock, carry_vs_uncoupled
from observational_succ.renewal_rigidity import (
    MUTANT_A, MUTANT_B, mutant_atoms, calibration_atoms,
    renewal_residual, first_unit_cell, affine_counterexample,
    density_residue_certificate)

class ClockMinimalityTests(unittest.TestCase):
    def test_closure_is_exact_divisor_lattice(self):
        result=finite_clock_closure((4,6,7))
        self.assertEqual(result['lcm'],84)
        self.assertEqual(result['closed_periods'],divisors(84))
        self.assertEqual(result['index_depth'],{2:2,3:1,7:1})

    def test_rooted_product_not_full_product(self):
        orbit=rooted_diagonal_orbit(4,6)
        self.assertEqual(orbit['diagonal_period'],12)
        self.assertEqual(orbit['full_cartesian_size'],24)
        self.assertEqual(orbit['component_count'],2)
        self.assertEqual(len(set(orbit['orbit'])),12)

    def test_coprime_rooted_product_is_full(self):
        o=rooted_diagonal_orbit(5,7)
        self.assertEqual(o['diagonal_period'],35)
        self.assertEqual(len(o['orbit']),35)
        self.assertEqual(o['component_count'],1)

    def test_pro2_has_infinite_refinement_but_not_totality(self):
        p=ClockTheory('pro_p',2)
        self.assertTrue(all(p.permits(2**k) for k in range(1,15)))
        self.assertFalse(p.permits(3))
        self.assertTrue(p.arbitrary_depth(2))
        self.assertFalse(p.arbitrary_depth(3))
        self.assertFalse(p.universal)

    def test_squarefree_has_every_prime_but_no_square(self):
        square=ClockTheory('squarefree')
        for p in (2,3,5,7,11,13):
            self.assertTrue(square.prime_exposure(p))
            self.assertFalse(square.permits(p*p))
        self.assertTrue(square.permits(2*3*5*7))
        self.assertFalse(square.universal)

    def test_finite_support_arbitrary_depth_still_not_universal(self):
        s=ClockTheory('finite_support',(2,3,5))
        self.assertTrue(s.permits(2**5*3**4))
        self.assertFalse(s.permits(7))
        self.assertFalse(s.universal)

    def test_full_has_all_query_depth(self):
        full=ClockTheory('full')
        for p in (2,3,7,11):
            self.assertTrue(full.prime_exposure(p))
            self.assertTrue(full.arbitrary_depth(p))
            self.assertTrue(all(full.permits(p**k) for k in range(1,6)))
        self.assertTrue(full.universal)

    def test_finite_shadow_replays_adaptive_trace(self):
        q=[2,3,4,6,7,14,30,42,84]
        s=matching_finite_shadow(q)
        self.assertEqual(s['finite_signature'],s['full_signature'])
        self.assertEqual(s['stage'],420)
        self.assertFalse(ClockTheory('finite_lcm',420).permits(11))
        self.assertFalse(ClockTheory('finite_lcm',420).permits(2**3))

    def test_unseen_odd_prime_is_not_absent_from_full(self):
        finite=ClockTheory('finite_lcm',210)
        full=ClockTheory('full')
        self.assertEqual(finite.finite_signature((2,3,5,7,10,15)),
                         full.finite_signature((2,3,5,7,10,15)))
        self.assertFalse(finite.permits(11)); self.assertTrue(full.permits(11))

    def test_finite_quotient_system_does_not_expose_all_powers(self):
        cap=ClockTheory('finite_lcm',210)
        self.assertTrue(cap.permits(2)); self.assertFalse(cap.permits(4))
        self.assertTrue(cap.permits(3)); self.assertFalse(cap.permits(9))

    def test_infinite_shadow_has_all_simple_primes_but_caps_depth(self):
        seen=(2,3,4,6,8,9,30,49,210)
        shadow=missing_power_infinite_shadow(seen)
        self.assertTrue(shadow['observationally_equal_on_queries'])
        self.assertEqual(shadow['capped_depth'],3)
        self.assertEqual(shadow['first_missing_power'],16)
        model=ClockTheory('one_prime_cap',(2,3))
        self.assertTrue(all(model.prime_exposure(p) for p in (2,3,5,7,11)))
        self.assertFalse(model.permits(16))
        self.assertTrue(model.permits(3**7))
        self.assertFalse(model.universal)

    def test_unique_rooted_clock_bonding_and_forbidden_map(self):
        self.assertEqual(unique_pointed_clock_map(12,4), tuple(k%4 for k in range(12)))
        self.assertIsNone(unique_pointed_clock_map(12,5))
        # The unrooted equivariant maps C12->C4 have four phases,
        # but f(0)=0 singles out exactly one coherent map.
        f=unique_pointed_clock_map(12,4)
        self.assertEqual(len({tuple((x+c)%4 for x in f) for c in range(4)}),4)
        for k in range(12):
            self.assertEqual(f[(k+1)%12],(f[k]+1)%4)

    def test_all_three_stage_bonding_squares_commute(self):
        for big in range(1,45):
            for mid in divisors(big):
                for small in divisors(mid):
                    a=unique_pointed_clock_map(big,mid)
                    b=unique_pointed_clock_map(mid,small)
                    c=unique_pointed_clock_map(big,small)
                    self.assertEqual(tuple(b[a[k]] for k in range(big)),c)

    def test_virtual_prime_powers_are_not_source_authenticated(self):
        stage=ClockTheory('finite_lcm',30)
        squarefree=ClockTheory('squarefree')
        virtual=authenticate_prime_word(stage,((2,2),))
        self.assertEqual(virtual['index'],4)
        self.assertTrue(virtual['formal_free_word_exists'])
        self.assertFalse(virtual['source_authenticated'])
        self.assertFalse(squarefree.permits(4))
        self.assertTrue(authenticate_prime_word(ClockTheory('full'),((2,2),))['source_authenticated'])
        self.assertEqual(authenticate_prime_word(ClockTheory('full'),((2,2),))['local_haar_mass'],'1/4')
        self.assertTrue(authenticate_prime_word(stage,((2,1),(3,1)))['source_authenticated'])
        self.assertFalse(authenticate_prime_word(stage,((2,2),(3,1)))['source_authenticated'])

    def test_type_guards(self):
        with self.assertRaises(SourceLawError): ClockTheory('pro_p',6)
        with self.assertRaises(SourceLawError): ClockTheory('squarefree',3)
        with self.assertRaises(SourceLawError): ClockTheory('finite_support',(3,2))
        with self.assertRaises(SourceLawError): finite_clock_closure((0,))
        with self.assertRaises(SourceLawError): finite_clock_closure((1000,1001,1003))
        with self.assertRaises(SourceLawError): rooted_diagonal_orbit(4.0,6)
        with self.assertRaises(SourceLawError): ClockTheory('full').finite_signature((False,))

class CarryClockTests(unittest.TestCase):
    def test_nontrivial_carry_advances_power_clock(self):
        c=CarryClock(4,2)
        self.assertEqual(c.period(),8)
        self.assertEqual(c.certificate()['rooted_period'],8)
        self.assertTrue(c.certificate()['faithful_full_lift'])

    def test_uncoupled_product_fails_at_prime_powers(self):
        data=carry_vs_uncoupled(4,2)
        self.assertEqual(data['coupled_period'],8)
        self.assertEqual(data['uncoupled_period'],4)
        self.assertTrue(data['carry_is_strict_lift'])

    def test_corrupt_carry_has_hidden_components(self):
        c=CarryClock(4,2,2)
        self.assertEqual(c.period(),4)
        self.assertFalse(c.certificate()['faithful_full_lift'])
        self.assertEqual(c.certificate()['total_components'],2)
        self.assertEqual(c.certificate()['rooted_period'],4)

    def test_coprime_carry_amount_is_sufficient(self):
        self.assertEqual(CarryClock(6,5,2).period(),30)
        self.assertEqual(CarryClock(3,6,4).period(),9)
        self.assertEqual(CarryClock(3,6,4).certificate()['total_components'],2)

    def test_iterated_carry_lifts_realize_prime_power_depth(self):
        m=2
        lengths=[]
        for _ in range(6):
            m=CarryClock(m,2).period()
            lengths.append(m)
        self.assertEqual(lengths,[4,8,16,32,64,128])

    def test_projected_low_counter_is_lawful(self):
        c=CarryClock(6,3)
        for x,y in c.orbit():
            nx,ny=c.step((x,y))
            self.assertEqual(nx,(x+1)%6)
        self.assertEqual(c.certificate()['rooted_period'],18)

    def test_invalid_clock_source_fails_closed(self):
        with self.assertRaises(SourceLawError): CarryClock(True,2)
        with self.assertRaises(SourceLawError): CarryClock(4,2,1.5)
        with self.assertRaises(SourceLawError): CarryClock(100,100)
        with self.assertRaises(SourceLawError): CarryClock(4,2).step((4,0))


class RenewalRationalMutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actual=mutant_atoms(240)
        cls.canonical=calibration_atoms(240)

    def test_rational_mutation_is_collision_free_through_horizon(self):
        self.assertEqual(set(self.actual.values()),{1})
        self.assertEqual(self.actual[F(1)],1)
        self.assertNotIn(F(3),self.actual)
        self.assertIn(F(35,11),self.actual)
        self.assertEqual(list(self.actual)[:5],[F(1),F(2),F(35,11),F(4),F(9,2)])

    def test_one_unit_calibration_survives_density_mutation(self):
        self.assertEqual(first_unit_cell(self.actual),F(1))
        self.assertEqual(first_unit_cell(self.canonical),F(1))

    def test_exact_canonical_renewal_no_residual_within_horizon(self):
        self.assertEqual(renewal_residual(self.canonical,240),{})

    def test_renewal_refutes_mutant_at_third_atom(self):
        residual=renewal_residual(self.actual,240)
        self.assertEqual(residual['3'],'-1')
        self.assertEqual(residual['35/11'],'1')

    def test_rank_braid_refutes_mutant(self):
        self.assertIsNotNone(affine_counterexample(self.actual))
        self.assertIsNone(affine_counterexample(self.canonical))

    def test_density_one_exact_euler_residue(self):
        c=density_residue_certificate()
        self.assertEqual(c['zeta_factor_at_one'],'1')
        self.assertEqual(c['original_local_density'],'8/15')
        self.assertEqual((1-1/MUTANT_A)*(1-1/MUTANT_B),F(8,15))

    def test_at_hundred_density_is_approximate_only(self):
        n=len(mutant_atoms(120))
        self.assertGreater(n,50)
        self.assertNotEqual(mutant_atoms(120),calibration_atoms(120))
        self.assertTrue(density_residue_certificate()['proof_of_density_one_is_analytic_not_finite_enumeration'])

    def test_reject_missing_or_invalid_probes(self):
        with self.assertRaises(SourceLawError): mutant_atoms(0)
        with self.assertRaises(SourceLawError): calibration_atoms(True)
        with self.assertRaises(SourceLawError): first_unit_cell({F(1):2,F(2):1})

if __name__=='__main__': unittest.main()
