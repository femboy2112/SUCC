from fractions import Fraction as F
from itertools import product
from math import prod
import unittest

from observational_succ.finite_euler_rigidity import (
    euler_ratio, inversion_certificate, reflection_obstruction,
    symmetric_atom_poisson_obstruction, positive_selfdual_gap_mutant,
)
from observational_succ.arithmetic_source_minimality import LateBeurlingPair


class FiniteEulerRigidityTest(unittest.TestCase):
    def test_prescribed_camouflage_reflection_falsifier(self):
        m=LateBeurlingPair(3,11)
        U,V=(3,11),(m.a,m.b)
        self.assertEqual((m.a,m.b),(F(9,2),F(77,17)))
        self.assertEqual(euler_ratio(U,V,1),1)
        self.assertEqual(euler_ratio(U,V,2),F(504,517))
        self.assertEqual(euler_ratio(U,V,-1),F(34,21))
        self.assertNotEqual(euler_ratio(U,V,2),euler_ratio(U,V,-1))

    def test_inversion_independent_factorwise_oracle(self):
        # Exhaustive short lists include shared factors, powers and odd count defects.
        lists=[()]+[(x,) for x in (F(3,2),F(2),F(4))]
        lists += list(product((F(2),F(4)),repeat=2))
        for U,V in product(lists,repeat=2):
            for n in (1,2,5):
                with self.subTest(U=U,V=V,n=n):
                    c=inversion_certificate(U,V,n)
                    numerator=prod((-u**n*(1-u**(-n)) for u in U),start=F(1))
                    denominator=prod((-v**n*(1-v**(-n)) for v in V),start=F(1))
                    self.assertEqual(c['negative_value'],numerator/denominator)

    def test_cardinality_is_conclusion_not_hypothesis(self):
        self.assertEqual(reflection_obstruction((2,2),(4,))['order_at_zero'],1)
        self.assertEqual(reflection_obstruction((2,2),())['order_at_zero'],2)
        self.assertEqual(inversion_certificate((2,),(),2)['parity'],-1)
        self.assertFalse(reflection_obstruction((2,2),(4,))['same_multiset'])

    def test_multiplicity_and_coincident_power_controls(self):
        c=reflection_obstruction((2,2,4),(2,4,4))
        self.assertEqual((c['least_unmatched_base'],c['signed_multiplicity']),(2,1))
        self.assertTrue(reflection_obstruction((2,2,4),(4,2,2))['same_multiset'])
        self.assertTrue(reflection_obstruction((),())['same_multiset'])
        # Product scale and count can both agree while the functions differ.
        c=reflection_obstruction((2,6),(3,4))
        self.assertEqual((c['order_at_zero'],c['product_ratio']),(0,1))
        self.assertFalse(c['same_multiset'])

    def test_zero_center_reflection_is_genuine_countermodel(self):
        U,V=(2,6),(3,4)
        for t in (1,2,3,7):
            self.assertEqual(euler_ratio(U,V,t),euler_ratio(U,V,-t))
        self.assertNotEqual(euler_ratio(U,V,2),euler_ratio(U,V,-1))
        self.assertNotEqual(euler_ratio(U,V,2),1)

    def test_heldout_late_sources_fail_exact_reflection(self):
        for p,q in ((3,101),(5,29),(7,53),(11,127),(13,997)):
            m=LateBeurlingPair(p,q)
            self.assertEqual(euler_ratio((p,q),(m.a,m.b),1),1)
            self.assertNotEqual(euler_ratio((p,q),(m.a,m.b),2),
                                euler_ratio((p,q),(m.a,m.b),-1))

    def test_exact_noninteger_atom_poisson_obstructions(self):
        v=symmetric_atom_poisson_obstruction(F(9,2))
        self.assertTrue(v['exact_at_half_integer'])
        self.assertEqual(v['pi_squared_excess_lower'],F(8,81))
        for n in (1,2,17,100):
            self.assertEqual(symmetric_atom_poisson_obstruction(n)['pi_squared_excess_lower'],0)
        for x in (F(77,17),F(10201,100),F(1001,1000)):
            self.assertGreater(symmetric_atom_poisson_obstruction(x)['pi_squared_excess_lower'],0)

    def test_weakening_gap_retains_positive_selfduality(self):
        # Fourier delta_(aZ)=(1/a)delta_(Z/a) swaps the two summands.
        coefficients={F(2):F(2,3),F(1,2):F(1,3)}
        fourier={1/a:w/a for a,w in coefficients.items()}
        self.assertEqual(fourier,coefficients)
        self.assertEqual(sum(coefficients.values()),1)
        self.assertEqual(coefficients[F(1,2)],F(1,3))
        for s in (-3,-1,0,1,2,7):
            self.assertEqual(positive_selfdual_gap_mutant(s),positive_selfdual_gap_mutant(1-s))
        self.assertEqual(positive_selfdual_gap_mutant(1),1)
        self.assertNotEqual(positive_selfdual_gap_mutant(2),1)

    def test_invalid_domains_fail_closed(self):
        for U,V,s in (((1,),(2,),1),((0,),(2,),1),((2.0,),(3,),1),((2,),(3,),0)):
            with self.assertRaises(ValueError):euler_ratio(U,V,s)
        with self.assertRaises(ValueError):inversion_certificate((2,),(3,),True)
        with self.assertRaises(ValueError):symmetric_atom_poisson_obstruction(F(1,2))
        with self.assertRaises(ValueError):symmetric_atom_poisson_obstruction(F(3,2),-1)


if __name__=='__main__':unittest.main()
