"""Independent CRT/local-global prime-phase test controls."""
import unittest
from fractions import Fraction as Q
from observational_succ.pi_rank_lattice import original_state
from observational_succ.pi_odd_prime_character import (
    _odd_prime_powers,odd_prime_phase_factors,rank_filtered_phase)


class OddPrimeCharacterTests(unittest.TestCase):
    def test_original_source_first_fourteen_time_states_all_characters(self):
        comparisons=0
        for n in range(1,15):
            u=original_state(n)
            self.assertEqual(u.denominator%2,1)
            for h in (-5,-1,0,1,2,7):
                factors=odd_prime_phase_factors(u,h)
                self.assertEqual(sum((x for _,_,x in factors),Q())%1,(h*u)%1)
                self.assertTrue(all(p%2 and 0<=v<1 for p,k,v in factors))
                comparisons+=1
        self.assertEqual(comparisons,84)

    def test_positive_negative_explicit_crt(self):
        known={Q(1,15):((3,1,Q(2,3)),(5,1,Q(2,5))),
               Q(47,15):((3,1,Q(1,3)),(5,1,Q(4,5))),
               Q(0):(),Q(-1):()}
        for val,exp in known.items():
            self.assertEqual(odd_prime_phase_factors(val),exp)

    def test_partial_rank_requires_residual_odd_primes(self):
        u=original_state(2)
        known,residual,full=rank_filtered_phase(u,1,(3,5))
        self.assertNotEqual(residual,0)
        self.assertEqual((known+residual)%1,full)
        all_primes=tuple(p for p,k,phase in odd_prime_phase_factors(u))
        _,resid,_=rank_filtered_phase(u,1,all_primes)
        self.assertEqual(resid,0)

    def test_two_adic_integer_has_trivial_unscaled_local_phase(self):
        # Z2-integrality makes local fractional part at p=2 zero,
        # unlike a *scaled* character of [U] mod16^k.
        for n in range(15):
            self.assertEqual(original_state(n).denominator%2,1)
        self.assertNotEqual(odd_prime_phase_factors(Q(32,3)),())
        with self.assertRaises(ValueError):odd_prime_phase_factors(Q(1,2))

    def test_reject_nonprime_budget_and_nonnumeric_inputs(self):
        with self.assertRaises(ValueError):_odd_prime_powers(2)
        with self.assertRaises(ValueError):_odd_prime_powers(9,2)
        with self.assertRaises(ValueError):odd_prime_phase_factors(0.5)
        with self.assertRaises(ValueError):rank_filtered_phase(Q(1,3),1,[3])

    def test_factor_exact_partial_unfactored_guard(self):
        # 10007*10009 has both factors beyond the trial budget 100.
        with self.assertRaises(ValueError):_odd_prime_powers(10007*10009,100)


if __name__=='__main__':unittest.main()
