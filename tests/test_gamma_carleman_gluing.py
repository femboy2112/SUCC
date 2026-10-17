import unittest
from fractions import Fraction as F
from observational_succ.gamma_carleman_gluing import (
    gamma_ou_dirichlet_channel, original_gamma_jump_upper,
    touching_carleman_moment_witness, dyadic_gamma_edge_lower,
    touching_source_gluing_gate,)
from observational_succ.gamma_edge_compensation import CompensationError

class DirichletCarlemanTests(unittest.TestCase):
    def test_authentic_gamma_rungs_are_nonnegative_forms(self):
        for j in range(40):
            x=gamma_ou_dirichlet_channel(j)
            self.assertEqual(x['alpha'],F(4*j+1,2))
            self.assertEqual(x['jump_mass'],F(4,4*j+1))
            self.assertEqual(x['one_half_dirichlet_prefactor'],F(1,2))

    def test_compact_gamma_jump_kernel_upper(self):
        for r in [F(1,100),F(1,10),F(1),F(10)]:
            d=original_gamma_jump_upper(r)
            self.assertEqual(d['rational_upper'],1+F(1,2)/r)
        with self.assertRaises(CompensationError):original_gamma_jump_upper(0)

    def test_touching_carleman_high_moment_nonvanishing(self):
        for m in range(9):
            x=touching_carleman_moment_witness(m)
            self.assertGreater(x['positive_carlemann_half_limit_greater_than'],0)
            self.assertTrue(x['touching_gamma_cross_does_not_vanish_in_K_limit'])
        self.assertTrue(touching_carleman_moment_witness(4)['applies_even_at_four_moment_high_cut'])
        self.assertEqual(touching_carleman_moment_witness(4)['positive_carlemann_half_limit_greater_than'],F(13,90531302400))

    def test_symbolic_astronomical_gamma_depth_without_iteration(self):
        d=F(1,2**36)
        p=dyadic_gamma_edge_lower(d)
        self.assertEqual(p['conceptual_true_Gamma_mode_count'],2**32)
        self.assertEqual(p['dyadic_group_depth'],32)
        self.assertGreater(p['full_source_edge_K_margin_from_dyadic_proof'],10)

    def test_finite_touching_source_conditional_gluing_with_huge_depth(self):
        # This is a mathematical conditional c_B=1/2, not an authenticated bulk source.
        p=touching_source_gluing_gate(F(1,2**36),F(1,4),F(1,2))
        self.assertTrue(p['strict_gluing_condition'])
        self.assertTrue(p['touching_no_gap'])
        self.assertFalse(p['source_bulk_margin_proved'])
        self.assertFalse(p['covers_all_primitive_F_decompositions'])
        self.assertFalse(p['RH_proved'])

    def test_not_every_shallow_depth_wins(self):
        p=touching_source_gluing_gate(F(1,32),F(1,4),F(1,2))
        self.assertFalse(p['strict_gluing_condition'])
        self.assertLess(p['full_source_edge_K_margin_from_dyadic_proof'],0)

    def test_invalid_source_and_horizon_gates(self):
        for j in (-1,False,1.3):
            with self.assertRaises(CompensationError):gamma_ou_dirichlet_channel(j)
        for d,b,c in [(F(1,32),0,F(1)),(F(1,32),F(1,4),0),
                      (F(1,31),F(1,4),F(1)),(F(1,32),F(1),F(1)),
                      (F(1,32),F(1,4),True)]:
            with self.assertRaises(CompensationError):touching_source_gluing_gate(d,b,c)

if __name__=='__main__':unittest.main()
