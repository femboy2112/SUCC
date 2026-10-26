"""Independent finite controls for the collision/resonance audit."""
from fractions import Fraction as Q
import unittest

from observational_succ.bbp_resonance_collision import (
    collision_ladder_budget, conductor_supported_counterfeit,
)
from observational_succ.pi_source_collision import (
    bbp_forcing, bbp_states, cell_collision, prime_window, small_ball_pairs,
)
from observational_succ.bbp_cyclotomic_birth import p_primary_phase


class ResonanceCollisionTests(unittest.TestCase):
    def test_ladder_budget_uses_authentic_cells(self):
        for count, depth, h, modes in ((12, 1, 1, 1), (32, 2, -3, 2), (64, 3, 2, 2)):
            budget = collision_ladder_budget(count, depth, h, modes)
            bins = {}
            for n in range(1, count+1):
                # Independent unwrapped source sum retains the complete history.
                value = sum((16**(n-j)*bbp_forcing(j) for j in range(1,n+1)), Q()) % 1
                label = (value*16**depth).__floor__()
                bins[label] = bins.get(label, 0)+1
            self.assertEqual(budget.energy, Q(16**depth*sum(v*v for v in bins.values()),count*count))
            self.assertGreaterEqual(budget.energy, 1)
            self.assertGreaterEqual(budget.squared_upper, 0)
            self.assertLessEqual(budget.squared_upper, 1)
            residues = {(h*16**j) % budget.cells for j in range(modes)}
            self.assertEqual(len(residues), modes)
            self.assertNotIn(0, residues)

    def test_finite_ladder_certificate_can_be_nonvacuous(self):
        budget = collision_ladder_budget(256, 1)
        self.assertLess(budget.squared_upper, 1)

    def test_source_forcing_inequality_fresh_exact_controls(self):
        # The all-n claim has an inherited algebraic proof; this is regression.
        for n in (1, 2, 13, 57, 113, 257):
            self.assertTrue(0 < bbp_forcing(n+1) < Q(15,64*n*n))

    def test_counterfeit_uses_no_new_conductor_and_retains_primary(self):
        for p in (17, 41, 73, 97, 113):
            fake = conductor_supported_counterfeit(p)
            true = prime_window(p)
            self.assertNotEqual(fake.complement, true.complement)
            for q, w, z, local in zip(fake.allowed_denominators, fake.complement,
                                      fake.selected, fake.local):
                self.assertEqual(q % w.denominator, 0)
                self.assertEqual(w.denominator % p != 0, True)
                self.assertEqual(p_primary_phase(z, p), int(local*p))
                self.assertTrue(0 < z < Q(1,q))
                self.assertEqual((local+w) % 1, z)
            self.assertGreater(fake.minimum_denominator, 256)
            for cells in (16, 64, 256):
                self.assertEqual(cell_collision(fake.selected, cells), cells)
                self.assertEqual(small_ball_pairs(fake.selected, Q(1,cells)), len(fake.selected)**2)
            # Fail the actual recurrence: a label alone cannot authenticate it.
            residuals = [((fake.complement[t+1]-16*fake.complement[t]
                           -bbp_forcing(true.start+2+t)) % 1)
                         for t in range(len(fake.complement)-1)]
            self.assertTrue(any(residuals))

    def test_domains_and_aliased_ladder_rejected(self):
        for args in ((0,1,1,1),(3,0,1,1),(3,1,0,1),(3,1,1,2),(3,1,16,1)):
            with self.assertRaises(ValueError):
                collision_ladder_budget(*args)
        for p in (3,5,9,25,True):
            with self.assertRaises(ValueError):
                conductor_supported_counterfeit(p)


if __name__ == '__main__':
    unittest.main()
