"""Focused exact tests. Nothing here claims generic pi normality or positive Collatz termination."""
import unittest
from fractions import Fraction
from parity_dual import (shortcut, parity_address, inverse_parity_mod,
    inverse_parity_reverse_mod, four_step_branch, parity_word_table,
    hex_word_to_address, bbp_forcing, bbp_hex_prefix, bbp_prefix_interval,
    bbp_collatz_seed_residue, transported_omega_mod, complement_parity_address)


class DualCategoryTests(unittest.TestCase):
    def test_low_two_parity_bits_equal_state_mod4(self):
        for a in range(-256,257):
            self.assertEqual(parity_address(a,2),a%4)

    def test_odd_quarter_classes(self):
        for k in range(-70,70):
            self.assertEqual((parity_address(4*k+1,2),parity_address(4*k+3,2)),(1,3))

    def test_four_bit_permutation(self):
        p=parity_word_table()
        self.assertEqual(p,(0,5,10,3,4,1,6,7,8,13,2,11,12,9,14,15))
        self.assertEqual(sorted(p),list(range(16)))
        self.assertEqual(tuple(p[p[j]] for j in range(16)),tuple(range(16)))

    def test_inverse_formula_vs_branch_replay(self):
        for bits in range(1,11):
            for word in range(1<<bits):
                seed=inverse_parity_mod(word,bits)
                self.assertEqual(seed,inverse_parity_reverse_mod(word,bits))
                self.assertEqual(parity_address(seed,bits),word)

    def test_block_affine_and_cylinders(self):
        for a in range(-100,101):
            word,s,b,c=four_step_branch(a)
            self.assertEqual(c,(3**s*a+b)//16)
            self.assertEqual(word,parity_word_table()[a%16])

    def test_one_hex_16_branches(self):
        for word in range(16):
            seed=inverse_parity_mod(word,4)
            self.assertEqual(parity_address(seed,4),word)
            for k in range(-9,10):
                a=seed+16*k
                self.assertEqual(parity_address(a,4),word)

    def test_collatz_four_versus_nibble_shift(self):
        for bits in (8,12):
            for addr in range(0,1<<bits, (1 if bits==8 else 11)):
                seed=inverse_parity_mod(addr,bits)
                a=seed
                for _ in range(4):
                    a=shortcut(a)
                self.assertEqual(a% (1<<(bits-4)), inverse_parity_mod(addr>>4,bits-4))

    def test_mirror_complement_is_negation_plus_minus_one(self):
        for bits in range(1,9):
            for a in range(1<<bits):
                self.assertEqual(complement_parity_address(a,bits),((1<<bits)-1)^a)

    def test_omega_is_involution_and_commutes_with_4_step(self):
        for a in range(128):
            bits=9
            omega=transported_omega_mod(a,bits)
            self.assertEqual(transported_omega_mod(omega,bits),a)
            # Four causal steps cost four precision bits.
            c4=a
            o4=omega
            for _ in range(4):
                c4=shortcut(c4)
                o4=shortcut(o4)
            self.assertEqual(o4%(1<<(bits-4)),
                             transported_omega_mod(c4,bits-4))

    def test_omega_nontrivial_examples(self):
        self.assertEqual(transported_omega_mod(0,12),(1<<12)-1)  # omega(0)=-1
        self.assertEqual(transported_omega_mod(1,12),2)
        self.assertEqual(transported_omega_mod(2,12),1)

    def test_source_forcing_identity(self):
        for n in range(1,40):
            self.assertEqual(bbp_forcing(n),Fraction(120*n*n-89*n+16,
                (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
            self.assertGreater(bbp_forcing(n),0)

    def test_rational_bbp_prefix(self):
        a,b=bbp_prefix_interval(12)
        self.assertLess(a,b)
        self.assertEqual(bbp_hex_prefix(12,12),'3243F6A8885A')

    def test_source_selected_collatz_seed_prefix(self):
        digits,addr,seed=bbp_collatz_seed_residue()
        self.assertEqual(digits,'3243F6A8885A')
        self.assertEqual(addr,0xA5888A6F3423)
        self.assertEqual(seed,0x138D4B466283)
        self.assertEqual(parity_address(seed,48),addr)
        self.assertEqual(seed%16,3)
        self.assertEqual(seed%256,131)

    def test_reflection_is_not_raw_state_negation(self):
        self.assertNotEqual(shortcut(-3), -shortcut(3))
        self.assertNotEqual(transported_omega_mod(3,8), (-1-3)%256)

    def test_source_claim_is_not_uniform_mixing(self):
        # A constant zero digit word is also perfectly well encoded.
        self.assertEqual(parity_address(inverse_parity_mod(0,32),32),0)
        # The affine map cannot force digit statistics by itself.
        self.assertEqual(inverse_parity_mod(0,32),0)

    def test_binary_inverse_control(self):
        # Inversion distinguishes allowed 2-adic inverse parity branches.
        for v in range(100):
            a=(2*v-1)*pow(3,-1,1<<12) % (1<<12)
            self.assertEqual(parity_address(a,1),1)
            self.assertEqual(shortcut(a)%(1<<11), v%(1<<11))


if __name__=='__main__':unittest.main()
