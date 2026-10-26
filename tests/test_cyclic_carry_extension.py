"""All finite maps checked, with lost-carry and phase-alias countermodels."""
import itertools
import unittest
from fractions import Fraction as Q
from observational_succ import cyclic_carry_extension as ce


class CyclicCarryExtensionTests(unittest.TestCase):
    def test_exact_sequence_and_all_additions(self):
        for bits in (2,3,4,5):
            size=1<<bits
            kernel={a for a in range(size) if a%2==0}
            image={ce.join_residue(u,0,bits) for u in range(size//2)}
            self.assertEqual(kernel,image)
            self.assertEqual({a%2 for a in range(size)},{0,1})
            for a,b in itertools.product(range(size),repeat=2):
                lift=ce.add_lifts(ce.split_residue(a,bits),ce.split_residue(b,bits),bits)
                self.assertEqual(ce.join_residue(*lift,bits),(a+b)%size)

    def test_cocycle_associativity_and_nontriviality(self):
        for b,d,f in itertools.product((0,1),repeat=3):
            self.assertEqual(ce.carry_cocycle(b,d)+ce.carry_cocycle((b+d)%2,f),
                             ce.carry_cocycle(d,f)+ce.carry_cocycle(b,(d+f)%2))
        for bits in (2,3,4,5,6):
            for t in range(1<<(bits-1)):
                full,fiber=ce.section_homomorphism_defects(t,bits)
                self.assertNotEqual(full,0)
                self.assertNotEqual(fiber,0)

    def test_zero_cocycle_mutation_changes_group(self):
        # In C16, the lift of parity one squares to 2, not to zero.
        proper=ce.add_lifts((0,1),(0,1))
        split_mutant=(0,0)
        self.assertEqual(ce.join_residue(*proper),2)
        self.assertNotEqual(ce.join_residue(*proper),ce.join_residue(*split_mutant))

    def test_character_descent_checked_on_every_fiber(self):
        for h in range(-32,33):
            constant=all(ce.character_phase(a,h)==ce.character_phase(a%2,h)
                         for a in range(16))
            self.assertEqual(constant,ce.character_descends_to_parity(h))
        self.assertFalse(ce.character_descends_to_parity(4))
        self.assertTrue(ce.character_descends_to_parity(8))

    def test_same_parity_different_fourier_energy(self):
        c=ce.parity_alias_control()
        self.assertTrue(c['parity_pushforward_equal'])
        self.assertEqual(c['phase_pair'],(Q(0),Q(1,2)))
        self.assertNotEqual(c['coherent_squared_magnitude'],c['cancelled_squared_magnitude'])
        self.assertFalse(c['dynamic_source_selected'])

    def test_invalid_domains(self):
        for bad in (True,1.5,'2'):
            with self.assertRaises(ValueError):ce.split_residue(bad)
        with self.assertRaises(ValueError):ce.split_residue(0,1)
        with self.assertRaises(ValueError):ce.join_residue(0,2)
        with self.assertRaises(ValueError):ce.carry_cocycle(True,1)

    def test_even_mode_keeps_cross_digit_fourth_interaction(self):
        support=ce.even_mode_cross_digit_support()
        self.assertEqual(len(support),128)
        for size in (1,2,3):
            for subset in itertools.combinations(range(8),size):
                histogram={bits:0 for bits in itertools.product((0,1),repeat=size)}
                for k in support:
                    histogram[tuple((k>>i)&1 for i in subset)]+=1
                self.assertEqual(set(histogram.values()),{128//(1<<size)})
        for shift in (0,4):
            self.assertEqual([sum(((k>>shift)&15)==d for k in support)
                              for d in range(16)],[8]*16)
        reduced=ce.even_mode_cyclotomic_coefficients()
        self.assertTrue(any(reduced))
        # Independently reduce X^k for exp(2*pi*i*2k/256).
        independent=[Q() for _ in range(64)]
        for k in support:
            residue=k%128
            independent[residue%64]+=Q(1 if residue<64 else -1,128)
        self.assertEqual(tuple(independent),reduced)


if __name__=='__main__':
    unittest.main()
