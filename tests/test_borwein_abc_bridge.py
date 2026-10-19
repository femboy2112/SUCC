"""Independent arithmetic hard/soft interface and strict noncomparison controls."""
import unittest
from fractions import Fraction as Q
from math import prod

from observational_succ.borwein_abc_bridge import borwein_abc_contact
from observational_succ.borwein_abc_contacts import ContactError
from observational_succ.borwein_prime_clock import first_boundary_leak


class BorweinABCHardSoftTests(unittest.TestCase):
    def test_soft_plateau_misses_actual_prime_power_divisibility(self):
        clocks=((3,1),(5,1))
        good=borwein_abc_contact(1,29,clocks,scale=Q(1,4)) # c=30
        bad=borwein_abc_contact(1,30,clocks,scale=Q(1,4)) # c=31
        self.assertEqual(good.actual_residues,(0,0))
        self.assertEqual(bad.actual_residues,(1,1))
        self.assertTrue(good.hard_all_locked)
        self.assertFalse(bad.hard_all_locked)
        self.assertEqual(good.smoothed_mass,Q(1))
        self.assertEqual(bad.smoothed_mass,Q(1))
        self.assertLess(borwein_abc_contact(1,30,clocks,scale=Q(1))
                        .smoothed_mass,Q(1))

    def test_hard_true_can_have_soft_mass_strictly_below_one(self):
        primes=(3,5,7,11,13,17,19,23,29)
        clocks=tuple((q,1) for q in primes)
        c=prod(primes)
        out=borwein_abc_contact(1,c-1,clocks)
        self.assertTrue(out.hard_all_locked)
        self.assertEqual(out.c,c)
        self.assertEqual(out.modulus,c)
        self.assertEqual(out.actual_residues,(0,)*len(primes))
        self.assertLess(out.smoothed_mass,Q(1))
        leak=first_boundary_leak(tuple(Q(1,q) for q in primes))
        self.assertEqual(Q(1)-out.smoothed_mass,leak)
        self.assertGreater(leak,0)

    def test_prime_power_contacts_and_height_gate_are_source_exact(self):
        clocks=((2,7),(3,1))
        x=borwein_abc_contact(3,125,clocks)
        self.assertFalse(x.hard_all_locked) # 128 divisible 2^7 not 3
        self.assertEqual(x.actual_residues,(0,2))
        self.assertTrue(borwein_abc_contact(1,8,((3,2),)).hard_all_locked)
        y=borwein_abc_contact(1,8,((2,4),))
        self.assertTrue(y.archimedean_forbidden)
        self.assertFalse(y.hard_all_locked)
        self.assertEqual(y.modulus,16)

    def test_no_soft_order_or_exact_probability_inference(self):
        values=[
          borwein_abc_contact(1,29,((3,1),(5,1))),
          borwein_abc_contact(1,30,((3,1),(5,1))),
          borwein_abc_contact(1,8,((3,2),)),
          borwein_abc_contact(5,1024,((2,5),(3,1),(5,1))),
        ]
        for x in values:
            self.assertEqual(x.hard_all_locked,x.c % x.modulus==0)
            self.assertGreaterEqual(x.smoothed_mass,Q(0))
            self.assertLessEqual(x.smoothed_mass,Q(1))
        # Source real arithmetic truth and modeled smoothing are distinct.
        self.assertEqual(values[0].smoothed_mass,values[1].smoothed_mass)
        self.assertNotEqual(values[0].hard_all_locked,values[1].hard_all_locked)

    def test_fake_clock_and_nonprimitive_input_rejected(self):
        for clocks in (((4,1),),((3,0),),((2,1),(2,3)),
                       ((5,1),(3,1)),[],()):
            with self.assertRaises(ContactError):
                borwein_abc_contact(1,8,clocks)
        for args in ((0,8), (2,4), (True,7), (4,True)):
            with self.assertRaises(ContactError):
                borwein_abc_contact(*args,((3,1),))
        with self.assertRaises(ContactError):
            borwein_abc_contact(1,8,((3,1),),Q(-1))
        with self.assertRaises(ContactError):
            borwein_abc_contact(1,8,((3,1),),0.1)


if __name__=="__main__":
    unittest.main()
