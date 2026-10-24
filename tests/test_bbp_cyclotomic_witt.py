"""Adversarial exact rational controls for the BBP p^2 filtered lift."""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_cyclotomic_witt import (
    integral_reduction, source_square_bursts, quotient_relation,
    lift_source_shear, direct_filtered_p2_endpoints,
    twisted_filtered_p2_endpoints,
)
from observational_succ.bbp_cyclotomic_birth import first_witt_holonomy
from observational_succ.bbp_source_memory import forcing

class BBPCyclotomicWittLiftTests(unittest.TestCase):
    def test_fermat_quotient_and_p2_return(self):
        for p in (17,41,73,97,113,137,193,257,313):
            m=(p-1)//8
            M=(p*p-1)//8
            q, q2, qlift=quotient_relation(p)
            self.assertEqual(2*q%p,q2)
            self.assertEqual(q,qlift)
            self.assertEqual(pow(16,M,p*p),(1+p*q)%(p*p))
            self.assertEqual((pow(16,8*M+1,p*p)-16*(1+8*p*q))%(p*p),0)
            self.assertEqual(first_witt_holonomy(p),q)

    def test_source_filtered_recurrence_matches_independent_event_transport(self):
        for p in (17,41,73,97,113,137,193,257,313):
            m=(p-1)//8
            kmax=min(m,10)
            direct=direct_filtered_p2_endpoints(p,kmax)
            twisted=twisted_filtered_p2_endpoints(p,kmax)
            self.assertEqual(direct,twisted,p)
            for k in range(1,kmax+1):
                M=(p*p-1)//8
                self.assertEqual(source_square_bursts(p,k),
                  tuple((8*k-a)*M+k for a in (7,4,3,2)))
                self.assertEqual(integral_reduction(forcing(k),p,2)%p,
                                 twisted[k-1]%p if k==1 else
                    (twisted[k-1]-16*twisted[k-2])%p)
            self.assertNotEqual(integral_reduction(lift_source_shear(1),p,1),0)
            # Nonzero Fermat-quotient shear makes the naive lift false.
            self.assertNotEqual(direct[0],integral_reduction(forcing(1),p,2),p)

    def test_source_domain_and_mutated_carries(self):
        for bad in (1,2,9,21,False):
            with self.assertRaises(ValueError):source_square_bursts(bad,1)
        for bad in (0,-1,True):
            with self.assertRaises(ValueError):source_square_bursts(17,bad)
        with self.assertRaises(ValueError):source_square_bursts(17,3)
        with self.assertRaises(ValueError):integral_reduction(Q(1,17),17)
        with self.assertRaises(ValueError):integral_reduction(Q(3,4),17,0)
        self.assertEqual(direct_filtered_p2_endpoints(17,0),())

if __name__=='__main__':unittest.main()
