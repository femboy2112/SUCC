"""Exact hostile finite controls for rooted orbit and LCM prime-jet reconstruction."""
import itertools
import unittest
from fractions import Fraction
from math import comb, gcd, lcm

from observational_succ.orbit_clock_genesis import (
    ClockSourceError, FiniteUnarySource, FreeUnaryRay, RootedCycle,
    minimal_superclock, minimal_clock_growth, join_irreducible_periods,
    exact_log_current_coefficients, central_binomial_state_bound,
    periodic_shadow, source_vs_instrument_no_ghost,
)


def independent_prime_power(n):
    """Calibration only: factor by naive division, unrelated to LCM progression."""
    if n < 2: return (1,0)
    t=n; factors=[]; d=2
    while d*d<=t:
        if t %d ==0:
            e=0
            while t%d==0:
                t//=d; e+=1
            factors.append((d,e))
        d+=1
    if t>1: factors.append((t,1))
    return factors[0] if len(factors)==1 else (1,0)


def brute_cyclic_map_exists(transitions, modulus):
    """Fully independent source morphism enumerator for tiny arbitrary graphs."""
    t=transitions; root=0
    visited=[]; seen=set(); x=root
    while x not in seen:
        seen.add(x); visited.append(x); x=t[x]
    for rest in itertools.product(range(modulus),repeat=len(visited)-1):
        f=dict(zip(visited,(0,)+rest))
        if all(f[t[v]]==(f[v]+1)%modulus for v in visited):
            return True
    return False


class SourceOrbitTests(unittest.TestCase):
    def test_free_ray_is_symbolic_and_has_quotients_all_checked_sizes(self):
        ray=FreeUnaryRay('e0')
        for m in range(1,20):
            for t in range(60):
                self.assertEqual(ray.quotient(m,t),t%m)
                self.assertEqual(ray.successor(ray.state(t)),ray.state(t+1))
        self.assertNotIsInstance(ray,FiniteUnarySource)

    def test_finite_cycle_allows_exact_divisor_quotients_only(self):
        for d in range(1,20):
            t=tuple((j+1)%d for j in range(d))
            src=FiniteUnarySource(t)
            self.assertEqual(src.orbit_signature()['period'],d)
            for m in range(1,20):
                self.assertEqual(src.can_factor_to(m),d%m==0)
                if d%m==0:
                    f=src.factor_to(m)
                    self.assertEqual(len(f),d)
                else:
                    with self.assertRaises(ClockSourceError):src.factor_to(m)

    def test_eventually_periodic_tail_allows_divisors_of_eventual_period(self):
        src=FiniteUnarySource((1,2,3,1,4),source_id='external')
        sig=src.orbit_signature()
        self.assertEqual((sig['preperiod'],sig['period']),(1,3))
        self.assertEqual(sig['unreachable_state_count'],1)
        self.assertTrue(src.can_factor_to(3))
        self.assertFalse(src.can_factor_to(2))
        self.assertEqual(src.factor_to(3),{0:0,1:1,2:2,3:0})

    def test_all_tiny_sources_and_target_periods_against_bruteforce_maps(self):
        checked=0
        for n in range(1,5):
            for arrows in itertools.product(range(n),repeat=n):
                source=FiniteUnarySource(tuple(arrows))
                for m in range(1,7):
                    expected=brute_cyclic_map_exists(arrows,m)
                    self.assertEqual(source.can_factor_to(m),expected,(arrows,m))
                    checked+=1
        self.assertEqual(checked,1728)

    def test_unreachable_states_are_not_fake_sources(self):
        source=FiniteUnarySource((1,0,3,2,4))
        self.assertEqual(source.orbit_signature()['period'],2)
        self.assertEqual(source.orbit_signature()['unreachable_state_count'],3)
        self.assertFalse(source.can_factor_to(3))

    def test_every_finite_positive_transcript_has_a_periodic_shadow(self):
        for depth in (0,1,2,3,7,19,100):
            receipt=periodic_shadow(depth)
            self.assertTrue(receipt['states_before_horizon_all_distinct'])
            self.assertGreater(receipt['actual_repetition_at'],depth)
            self.assertFalse(receipt['free_orbit_certified'])

    def test_neither_self_built_instrument_nor_its_product_is_new_source_data(self):
        r=source_vs_instrument_no_ghost(4,5)
        self.assertEqual(r['joint_synchronized_period'],20)
        self.assertFalse(r['instrument_is_source_factor'])
        self.assertTrue(r['new_instrument_cannot_authenticate_new_source_prime'])
        yes=source_vs_instrument_no_ghost(20,5)
        self.assertTrue(yes['instrument_is_source_factor'])

    def test_invalid_source_identity_and_malformed_paths(self):
        with self.assertRaises(ClockSourceError): FiniteUnarySource((1,0),2)
        with self.assertRaises(ClockSourceError): FiniteUnarySource((1,True))
        with self.assertRaises(ClockSourceError): FiniteUnarySource(())
        with self.assertRaises(ClockSourceError): FiniteUnarySource((0,),source_id='')
        with self.assertRaises(ClockSourceError): FreeUnaryRay('')
        with self.assertRaises(ClockSourceError): FreeUnaryRay().state(-1)
        with self.assertRaises(ClockSourceError): FreeUnaryRay().successor(('wrong',0))
        with self.assertRaises(ClockSourceError): periodic_shadow(10000)


class SpliceTests(unittest.TestCase):
    def test_splice_generates_every_small_rooted_cycle_without_prime_seeds(self):
        clock=RootedCycle.initial('synthetic')
        for n in range(1,61):
            self.assertEqual(clock.period,n)
            self.assertEqual(clock.source_id,'synthetic')
            self.assertEqual(FiniteUnarySource(clock.transition).orbit_signature()['period'],n)
            if n<60:clock=clock.splice()

    def test_successive_splice_is_not_false_refinement(self):
        previous=RootedCycle.initial()
        successor=previous.splice()
        self.assertEqual(len(successor.quotient_to(previous)),2)
        for period in range(2,13):
            old=successor
            newer=old.splice()
            with self.assertRaises(ClockSourceError):newer.quotient_to(old)
            previous=old;successor=newer

    def test_legitimate_quotient_maps_from_c12_only_to_divisors(self):
        clock=RootedCycle.initial()
        clocks={1:clock}
        for n in range(2,13):
            clock=clock.splice()
            clocks[n]=clock
        for m in range(1,13):
            if 12%m==0:self.assertEqual(len(clocks[12].quotient_to(clocks[m])),12)
            else:
                with self.assertRaises(ClockSourceError):clocks[12].quotient_to(clocks[m])

    def test_fake_malformed_period_eight_refused(self):
        # An 8-state machine containing an actual 4-cycle plus 4 unreachable states.
        with self.assertRaises(ClockSourceError): RootedCycle((1,2,3,0,5,6,7,4))
        src=FiniteUnarySource((1,2,3,0,5,6,7,4))
        self.assertEqual(src.orbit_signature()['period'],4)
        self.assertFalse(src.can_factor_to(8))

    def test_missing_fresh_state_budget_refuses_splice(self):
        c=RootedCycle.initial()
        c=c.splice(state_budget=2)
        with self.assertRaises(ClockSourceError): c.splice(state_budget=2)

    def test_broken_morphisms_forbid_phase_ghosts(self):
        source=FiniteUnarySource((1,2,3,0))
        original=source.factor_to(2)
        shifted={x:(y+1)%2 for x,y in original.items()}
        self.assertNotEqual(shifted[source.root],0)
        self.assertEqual(original[source.root],0)


class MinimalJointClockTests(unittest.TestCase):
    def test_minimum_superclock_for_named_periods(self):
        self.assertEqual(minimal_superclock((4,6))['minimum_period'],12)
        self.assertEqual(minimal_superclock((4,6,9))['minimum_period'],36)
        self.assertEqual(minimal_superclock((1,2,3,4,5,6))['minimum_period'],60)

    def test_small_sets_exhaustively_minimal_against_brute_search(self):
        periods=range(1,8)
        checked=0
        for k in range(1,8):
            for combo in itertools.combinations(periods,k):
                l=minimal_superclock(combo)['minimum_period']
                brute=next(i for i in range(1,421) if all(i%m==0 for m in combo))
                self.assertEqual(l,brute)
                checked+=1
        self.assertEqual(checked,127)

    def test_clock_progression_first_twelve_exact(self):
        expected=[1,2,6,12,60,60,420,840,2520,2520,27720,27720]
        rows=minimal_clock_growth(12)
        self.assertEqual([r['minimum_joint_period'] for r in rows],expected)
        self.assertEqual([r['new_capacity_factor'] for r in rows],
                         [1,2,3,2,5,1,7,2,3,1,11,1])
        self.assertTrue(all(r['finite_clock_constructed_and_verified'] for r in rows))
        self.assertTrue(rows[1]['new_observer_is_quotient_of_previous']) # C2 -> C1
        self.assertTrue(all(not r['new_observer_is_quotient_of_previous'] for r in rows[2:]))
        self.assertTrue(all(not r['joint_machine_materialized'] for r in rows))

    def test_capacity_jumps_are_exact_prime_power_tape_to_300(self):
        rows=minimal_clock_growth(300)
        self.assertEqual(len(rows),300)
        for row in rows:
            n=row['horizon'];p,e=independent_prime_power(n)
            self.assertEqual((row['new_capacity_factor'],row['jet_exponent']),
                             (p,e) if p>1 else (1,0), n)
        self.assertEqual(rows[5]['new_capacity_factor'],1) # 6
        self.assertEqual(rows[7]['new_capacity_factor'],2) # 8
        self.assertEqual(rows[8]['new_capacity_factor'],3) # 9

    def test_join_irreducibles_match_only_prime_powers(self):
        items=join_irreducible_periods(120)
        expected=tuple(n for n in range(2,121) if independent_prime_power(n)[0]>1)
        self.assertEqual(items,expected)

    def test_minimal_clock_witness_is_never_full_cartesian_product_by_decree(self):
        x=minimal_superclock((4,6))
        self.assertEqual(x['minimum_period'],12)
        self.assertEqual(4*6,24)
        self.assertTrue(x['full_cartesian_product_not_required'])

    def test_missing_c8_jet_is_delayed_and_detectable(self):
        regular=minimal_superclock(tuple(range(1,9)))['minimum_period']
        missing=minimal_superclock(tuple(n for n in range(1,9) if n!=8))['minimum_period']
        self.assertEqual(regular,840)
        self.assertEqual(missing,420)
        self.assertEqual(regular//missing,2)
        # Removing composite C6 does not change the common carrier.
        omit_six=minimal_superclock(tuple(n for n in range(1,9) if n!=6))['minimum_period']
        self.assertEqual(omit_six,regular)

    def test_horizon_rejects_unconstructed_clock_budget(self):
        with self.assertRaises(ClockSourceError): minimal_clock_growth(10,materialized_clock_budget=9)
        with self.assertRaises(ClockSourceError): minimal_clock_growth(601)
        with self.assertRaises(ClockSourceError): minimal_superclock((1.5,))
        with self.assertRaises(ClockSourceError): minimal_superclock((0,))


class ArithmeticCurrentAndCostTests(unittest.TestCase):
    def test_exact_prime_current_symbolic_coefficients(self):
        n=40; beta=2
        new=exact_log_current_coefficients(n,beta)
        expected={}
        for j in range(2,n+1):
            p,e=independent_prime_power(j)
            if p>1:
                expected[p]=expected.get(p,Fraction(0))+Fraction(1,j**beta)
        self.assertEqual(new,expected)
        self.assertEqual(new[2],Fraction(1,4)+Fraction(1,16)+Fraction(1,64)+Fraction(1,256)+Fraction(1,1024))

    def test_symbolic_jets_no_nonprime_power_impulse(self):
        self.assertNotIn(6,[r['horizon'] for r in minimal_clock_growth(50) if r['new_capacity_factor']>1])
        self.assertIn(49,[r['horizon'] for r in minimal_clock_growth(50) if r['new_capacity_factor']>1])

    def test_binomial_divisibility_exact_numerical_for_all_k(self):
        for n in range(1,51):
            L=minimal_clock_growth(n)[-1]['minimum_joint_period']
            for k in range(n):
                self.assertEqual(L%comb(n-1,k),0)

    def test_information_budget_elementary_exp_lower_bound(self):
        for n in range(1,101):
            data=central_binomial_state_bound(n)
            self.assertTrue(data['bound_checked_exactly'])
            self.assertGreaterEqual(data['least_period']*n,2**(n-1))
            self.assertGreaterEqual(2**data['binary_bits_needed'],data['least_period'])
            if data['binary_bits_needed']:
                self.assertLess(2**(data['binary_bits_needed']-1),data['least_period'])

    def test_state_cost_versus_factorial_overhead(self):
        rows=minimal_clock_growth(12)
        factorial=1
        for row in rows:
            factorial*=row['horizon']
            self.assertLessEqual(row['minimum_joint_period'],factorial)
        self.assertLess(rows[-1]['minimum_joint_period'],factorial)

    def test_type_guards_do_not_accept_floats_or_bools(self):
        for x in (True,False,2.0,'3',-1):
            with self.assertRaises(ClockSourceError): exact_log_current_coefficients(20,x)
        with self.assertRaises(ClockSourceError): RootedCycle((True,))
        with self.assertRaises(ClockSourceError): minimal_superclock((True,))


if __name__=='__main__':
    unittest.main()
