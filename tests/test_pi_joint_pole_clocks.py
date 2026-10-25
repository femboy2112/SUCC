"""Independent integer-residue/valuation controls for authentic BBP pole clocks."""
from fractions import Fraction as Q
import unittest
from observational_succ.pi_joint_prime_carrier import (
    forcing, four_pole_residues, pole_event, first_prime_birth,
    valuation_rational, crt_pole_joint_period, local_primary, states,
)

class PoleClocks(unittest.TestCase):
    def test_four_classes_and_exact_negative_valuation(self):
        for p in (7,11,13,17,19,23,31):
            for n in range(1,3*p+1):
                actual=(valuation_rational(forcing(n),p)<0)
                self.assertEqual(actual,pole_event(n,p))
                if actual:
                    # Exact order is the maximum pole root depth for this n.
                    depth=1
                    while n%(p**(depth+1)) in four_pole_residues(p,depth+1):
                        depth+=1
                    self.assertEqual(valuation_rational(forcing(n),p),-depth)

    def test_all_scale_four_residues(self):
        for p,k in ((7,1),(7,2),(7,3),(11,1),(11,2),(11,3),
                    (13,1),(13,2),(17,1),(19,1),(23,1)):
            roots=four_pole_residues(p,k)
            self.assertEqual(len(roots),4)
            self.assertEqual(len(set(roots)),4)
            self.assertTrue(all((r%(p**(k-1))) in four_pole_residues(p,k-1)
                                for r in roots if k>1))
            # Direct rational evaluation across the *entire period* for selected sizes.
            if p**k<=1331:
                events={n for n in range(1,p**k+1)
                        if valuation_rational(forcing(n),p)<=-k}
                self.assertEqual(events,{r or p**k for r in roots})

    def test_distinct_prime_crt_independence_exact(self):
        for items in (((7,1),(11,1)),((7,2),(11,1)),
                      ((7,1),(11,1),(13,1)),((7,2),(11,2))):
            M,expected=crt_pole_joint_period(items)
            found=[n for n in range(1,M+1)
                   if all(pole_event(n,p,k) for p,k in items)]
            self.assertEqual(len(found),expected)
            self.assertEqual(Q(len(found),M),
                             __import__('functools').reduce(lambda x,pow: x*Q(4,pow[0]**pow[1]),
                                                            items,Q(1)))

    def test_birth_is_nonzero_and_earlier_components_absent(self):
        xs=states(52)
        for p in (7,11,13,17,19,23,29,31,37,41,43,47):
            first=first_prime_birth(p)
            self.assertTrue(all(not pole_event(n,p) for n in range(1,first)))
            self.assertTrue(pole_event(first,p))
            for n in range(first):
                self.assertEqual(local_primary(xs[n],p),0)
            self.assertNotEqual(local_primary(xs[first],p),0)

    def test_small_prime_failure_controls(self):
        for p in (2,3,5):
            with self.assertRaises(ValueError):four_pole_residues(p)
        for items in (((7,1),(7,2)),((3,1),),((7,0),)):
            with self.assertRaises(ValueError):crt_pole_joint_period(items)
        with self.assertRaises(ValueError):valuation_rational(0,7)

if __name__=='__main__':unittest.main()

class ExceptionalSmallPrimes(unittest.TestCase):
    def test_exact_numerator_and_hensel_resolutions(self):
        from observational_succ.pi_joint_prime_carrier import (
            forcing_product_form,forcing_numerator,exceptional_numerator_root)
        for n in range(1,520):
            self.assertEqual(forcing_product_form(n),forcing(n))
            self.assertEqual(forcing_numerator(n)%15,(n+1)%15)
        self.assertEqual((exceptional_numerator_root(3,2),
                          exceptional_numerator_root(5,2)),(8,24))
        for p in (3,5):
            for depth in range(1,9):
                root=exceptional_numerator_root(p,depth)
                self.assertEqual(forcing_numerator(root)%(p**depth),0)
                self.assertEqual((240*root-89)%p,1)
                if depth>1:
                    self.assertEqual(root%(p**(depth-1)),
                                    exceptional_numerator_root(p,depth-1))
        # p=3: the two pole roots plus numerator root exhaust the three
        # lifts of their shared residue class n=2 modulo 3.
        self.assertEqual({7*pow(8,-1,9)%9,pow(2,-1,9),
                          exceptional_numerator_root(3,2)}, {2,5,8})
        # p=5: they occupy three of the five lifts of residue n=4 mod 5.
        self.assertEqual({7*pow(8,-1,25)%25,pow(4,-1,25),
                          exceptional_numerator_root(5,2)}, {4,19,24})

    def test_cyclotomic_transport_orders_have_shared_composite_clocks(self):
        from observational_succ.pi_joint_prime_carrier import sixteen_clock_order
        expected={(7,1):3,(7,2):21,(11,1):5,(11,2):55,
                  (13,1):3,(13,2):39,(17,1):2,(17,2):34,
                  (19,1):9,(23,1):11,(31,1):5,(3,1):1,(5,1):1}
        for (p,k),order in expected.items():
            self.assertEqual(sixteen_clock_order(p,k),order)
            self.assertEqual(pow(16,order,p**k),1)
            self.assertEqual((p-1)*p**(k-1)%order,0)
        # Local 7- and 13-power transport both require mod-3 time clock.
        self.assertEqual(sixteen_clock_order(7,1),
                         sixteen_clock_order(13,1))
        with self.assertRaises(ValueError):sixteen_clock_order(2,1)
        with self.assertRaises(ValueError):sixteen_clock_order(7,0)

class PoleCounting(unittest.TestCase):
    def test_instantaneous_pole_support_matches_rational_source(self):
        from observational_succ.pi_joint_prime_carrier import (
            source_innovation_poles,primes_through)
        for n in range(1,1301):
            detected=source_innovation_poles(n)
            oracle=tuple(p for p in primes_through(8*n-3) if p>=7 and
                         valuation_rational(forcing(n),p)<0)
            self.assertEqual(detected,oracle)

    def test_per_prime_four_residue_mean_by_complete_periods(self):
        for p in (7,11,13,17,19,23,29,31):
            self.assertEqual(sum(pole_event(n,p) for n in range(1,p+1)),4)
            for times in (2,3,8):
                self.assertEqual(sum(pole_event(n,p) for n in range(1,times*p+1)),
                                 4*times)
