"""Adversarial exact tests for finite boundary filter reconstruction."""
import unittest
from fractions import Fraction as F
from observational_succ.boundary_filter_tomography import (
    mat, mul, rank, moments, hankel, observability, reachability,
    filtered_outputs, reconstruct_state_from_filters, identity_filters,
    signed_future_filter, conditional_defect_numerator,
    bbp_forcing, bbp_prefix, source_pin, radial_response)


class BoundaryTests(unittest.TestCase):
    def test_single_port_minimal_hankel(self):
        a=((2,0),(0,3)); b=((1,),(1,)); c=((1,1),)
        z=radial_response(a,b,c,3)
        self.assertEqual(z["hankel_rank"],2)
        self.assertEqual(z["reachable_rank"],2)
        self.assertEqual(z["observable_rank"],2)
        self.assertEqual(z["jets"],((2,),(5,),(13,)))
        self.assertEqual(hankel(a,b,c,2),((2,5),(5,13)))

    def test_hidden_block_is_not_reconstructed(self):
        a=((2,0,0),(0,3,0),(0,0,7))
        b=((1,),(1,),(0,)); c=((1,1,0),)
        z=radial_response(a,b,c,5)
        self.assertEqual((z["hankel_rank"],z["ambient_dimension"]),(2,3))
        self.assertEqual(z["reachable_rank"],2)
        self.assertEqual(z["observable_rank"],2)
        mutant=((2,0,0),(0,3,0),(0,0,17))
        self.assertEqual(moments(a,b,c,9),moments(mutant,b,c,9))

    def test_unobservable_but_reachable(self):
        a=((2,0),(0,3)); b=((1,),(1,)); c=((1,0),)
        self.assertEqual(rank(reachability(a,b)),2)
        self.assertEqual(rank(observability(a,c)),1)
        self.assertEqual(rank(hankel(a,b,c,3)),1)

    def test_filtered_state_recovery(self):
        a=((2,1),(0,3)); b=((1,),(2,)); c=((1,1),)
        bank=identity_filters(2)
        readings=filtered_outputs(a,b,c,bank,5)
        v=b
        for t in range(5):
            self.assertEqual(reconstruct_state_from_filters(c,bank,[x[0] for x in readings[t]]),
                             tuple(x[0] for x in v))
            v=mul(a,v)

    def test_nontrivial_twisted_filter_recovery(self):
        c=((1,2),)
        bank=((1,1),(1,-1))
        self.assertEqual(reconstruct_state_from_filters(c,bank,(11,-5)),(3,4))

    def test_blind_filter_rejected(self):
        with self.assertRaises(ValueError):
            reconstruct_state_from_filters(((1,1),),((1,1),(2,2)),(3,6))
        with self.assertRaises(ValueError):
            reconstruct_state_from_filters(((1,0),),identity_filters(2),(3,0))
        with self.assertRaises(ValueError):
            reconstruct_state_from_filters(((1,1),),identity_filters(2),(3,))
        with self.assertRaises(ValueError):
            reconstruct_state_from_filters(((1,1),),((1,0),(0,1),(1,1)),(2,3,6))

    def test_rank_exact_controls(self):
        self.assertEqual(rank(((1,2),(2,4))),1)
        self.assertEqual(rank(((1,2),(2,5))),2)
        with self.assertRaises(TypeError): mat(((0.5,),))
        with self.assertRaises(ValueError): mul(((1,2),),((1,2),))

    def test_conditional_phase_versus_marginal(self):
        # Alternating bits: marginal balanced, next bit determined.
        digits=(0,1)*8
        filt=signed_future_filter(digits,2,1,1)
        self.assertIn((0,),filt)
        self.assertIn((1,),filt)
        self.assertNotEqual(conditional_defect_numerator(digits,2,1),0)
        self.assertEqual(conditional_defect_numerator((0,1),2,0),0)

    def test_filter_forged_uniform_one_digit(self):
        # Cyclic de Bruijn order-one pattern, nonuniform 2-blocks.
        d=(0,1)*12
        self.assertEqual(conditional_defect_numerator(d,2,0),0)
        self.assertGreater(conditional_defect_numerator(d,2,1),0)

    def test_cyclotomic_filter_exact_formal(self):
        filt=signed_future_filter((0,1,2,3,0,1),4,1,1)
        self.assertEqual(sum(sum(v.values()) for v in filt.values()),5)
        self.assertEqual(filt[(1,)][0],2)
        with self.assertRaises(ValueError): signed_future_filter((0,1),4,0,4)

    def test_bbp_source_and_mutations(self):
        z=bbp_prefix(12)
        self.assertTrue(source_pin(z,0))
        self.assertFalse(source_pin(z,1))
        altered=list(z);altered[5]+=F(1,7)
        self.assertFalse(source_pin(altered,0))
        shifted=bbp_prefix(12,F(1,16))
        self.assertTrue(source_pin(shifted,F(1,16)))
        self.assertFalse(source_pin(shifted,0))
        self.assertEqual(bbp_forcing(1),F(47,15))

    def test_no_source_specific_statistical_gain(self):
        # Even perfect finite boundary reconstruction does not imply Haar.
        a=((1,),);b=((1,),);c=((1,),)
        self.assertEqual(radial_response(a,b,c,4)["hankel_rank"],1)
        self.assertEqual(moments(a,b,c,4),((1,),(1,),(1,),(1,)))
        self.assertGreater(conditional_defect_numerator((0,)*20,2,0),0)


if __name__=="__main__":
    unittest.main()
