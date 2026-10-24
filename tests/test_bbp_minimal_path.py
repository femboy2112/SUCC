"""Independent exact arithmetic + hostile minimal-rule controls for BBP."""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_minimal_path import (
    primes_at_most, prime_births_through, prime_birth_count_formula,
    check_first_birth_against_real_state,
    counterfeit_selected_state, counterfeit_birth_step,
    counterfeit_denominator_witness, green_homogeneous_second_order,
    green_order_two_residual_interval, rational_first_order_impossibility,
    finite_prime_support_no_go, counterfeit_first_step,
    prime_power_first_birth, prime_power_birth_test,
    integer_root_floor, prime_power_birth_count,
)
from observational_succ.bbp_source_memory import (
    forcing, rational_counterfeit_tail, rational_counterfeit_forcing,
)


def independent_primes(bound):
    return tuple(p for p in range(3,bound+1,2)
                 if all(p%d for d in range(3,__import__("math").isqrt(p)+1,2)))


def independent_first_birth(p):
    n=1
    while True:
        den=(8*n-7,8*n-4,8*n-3,8*n-2)
        if any(k%p==0 for k in den):
            return n
        n+=1


class ArithmeticBirthCensus(unittest.TestCase):
    def test_census_exact_pole_integer_gate(self):
        for N in range(0,75):
            ps=independent_primes(8*N)
            expected=tuple((p,independent_first_birth(p)) for p in ps
                           if independent_first_birth(p)<=N)
            self.assertEqual(primes_at_most(8*N),ps)
            self.assertEqual(prime_births_through(N),expected)
            groups=prime_birth_count_formula(N)
            self.assertEqual(sum(groups),len(expected))
            self.assertEqual(groups,tuple(sum(p%8==r for p,_ in expected)
                                         for r in (1,5,3,7)))
        self.assertEqual(prime_births_through(1),((3,1),(5,1)))

    def test_every_first_p_birth_is_an_actual_new_rational_carrier(self):
        for p in independent_primes(127):
            receipt=check_first_birth_against_real_state(p)
            self.assertEqual(receipt["p"],p)
            self.assertEqual(receipt["birth"],independent_first_birth(p))
            self.assertTrue(receipt["before_integral"])
            self.assertEqual(receipt["new_valuation"],-1)
        self.assertEqual(finite_prime_support_no_go(3,(3,5)),(7,2))
        with self.assertRaises(ValueError):
            finite_prime_support_no_go(1,(3,5))


    def test_all_depth_first_prime_power_births(self):
        # Independent scan of all four original source denominators.
        for p in (3,5,7,11,13):
            for depth in (1,2,3,4):
                n=prime_power_first_birth(p,depth)
                if n>90:continue
                q=p**depth
                earliest=next(i for i in range(1,n+1)
                              if any(v%q==0 for v in
                                     (8*i-7,8*i-4,8*i-3,8*i-2)))
                self.assertEqual(n,earliest)
                cert=prime_power_birth_test(p,depth,90)
                self.assertEqual(cert["valuation"],-depth)
                self.assertEqual(cert["birth"],n)
        with self.assertRaises(ValueError):
            prime_power_birth_test(13,4,90)

    def test_exact_hierarchy_census_and_even_depth_square_identity(self):
        for N in (1,2,3,10,20,45,90,150):
            for depth in (1,2,3,4):
                primes=independent_primes(8*N)
                expected=sum(prime_power_first_birth(p,depth)<=N for p in primes)
                self.assertEqual(prime_power_birth_count(N,depth),expected)
                if depth==1:
                    self.assertEqual(expected,sum(prime_birth_count_formula(N)))
                if depth==2:
                    limit=__import__("math").isqrt(max(0,8*N-7))
                    self.assertEqual(expected,len(independent_primes(limit)))
        for depth in range(1,9):
            for n in (0,1,2,7,99,1024):
                root=integer_root_floor(n,depth)
                self.assertLessEqual(root**depth,n)
                self.assertGreater((root+1)**depth,n)
        for fake in (True,0,-1):
            with self.assertRaises(ValueError):
                prime_power_first_birth(17,fake)

    def test_strict_composite_and_boolean_rejection(self):
        for fake in (0,1,2,9,21,25,False,True,-3,1.0):
            with self.assertRaises(ValueError):
                check_first_birth_against_real_state(fake)
        for bad in (True,-1,2.0):
            with self.assertRaises(ValueError):
                prime_birth_count_formula(bad)


class HolonomicMinimality(unittest.TestCase):
    def test_exact_second_order_operator_and_irrationality_premise(self):
        for n in range(0,35):
            A,B=green_homogeneous_second_order(n)
            R=forcing(n+2)/forcing(n+1)
            self.assertEqual((A,B),(16+R,16*R))
            self.assertEqual(forcing(n+2)-R*forcing(n+1),0)
            lo,hi=green_order_two_residual_interval(n,12)
            self.assertLess(lo,0)
            self.assertGreater(hi,0)
            self.assertLess(hi-lo,Q(1,1000000))
            for q in (Q(0),Q(16),Q(1,2),Q(-3,7),Q(171,11)):
                d,r=rational_first_order_impossibility(n,q)
                self.assertEqual(d,16-q)
                self.assertGreater(r,0)
        with self.assertRaises(ValueError):
            rational_first_order_impossibility(1,1.0)

    def test_full_infinite_rank_counterfeit_is_selected_zero(self):
        # t_n^*=int u^n (1-u)du has strict Hankel positivity at
        # every finite size by its positive continuous density, although
        # 16*t0=8 -> selected orbit zero for ALL times.
        self.assertEqual(rational_counterfeit_tail(0),Q(1,2))
        self.assertEqual(counterfeit_selected_state(0),0)
        self.assertEqual(counterfeit_first_step(),counterfeit_selected_state(1))
        for n in range(1,120):
            self.assertEqual(counterfeit_selected_state(n),
                             (-rational_counterfeit_tail(n))%1)
            self.assertEqual(
                counterfeit_selected_state(n),
                (16*counterfeit_selected_state(n-1)
                 +rational_counterfeit_forcing(n))%1)
            self.assertGreater(rational_counterfeit_forcing(n),0)
        for p in independent_primes(100):
            cert=counterfeit_denominator_witness(p)
            self.assertEqual(cert["birth"],p-2)
            self.assertEqual(counterfeit_birth_step(p),p-2)
            self.assertEqual(cert["first_valuation"],-1)
            self.assertEqual(cert["selected_circle_phase"],0)


if __name__=="__main__":
    unittest.main()
