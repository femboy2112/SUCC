import unittest
from fractions import Fraction as F
from observational_succ.bidirectional_hilbert import (
  dot, orthogonal_innovations, compatible_functionals_square_norm,
  hidden_target_counterexample)
from observational_succ.bidirectional_cut import CutSourceError

class OrthogonalTowers(unittest.TestCase):
    def test_exact_residual_difference_of_squares(self):
        target=(F(1),F(2),F(3),F(4))
        basis=((F(1),F(0),F(0),F(0)),
               (F(1),F(1),F(0),F(0)),
               (F(1),F(1),F(1),F(0)),
               (F(1),F(1),F(1),F(1)))
        a=orthogonal_innovations(target,basis)
        self.assertEqual(a['norm_sq'],30)
        self.assertEqual(a['innovation_energies'],(1,4,9,16))
        self.assertEqual(a['residual_sq'],(29,25,16,0))
        self.assertEqual(a['surviving'],0)

    def test_linear_dependence_does_not_fake_observability(self):
        t=(F(1),F(2),F(0))
        a=orthogonal_innovations(t,((F(1),F(0),F(0)),
                  (F(2),F(0),F(0)),(F(0),F(1),F(0))))
        self.assertEqual(a['innovation_energies'],(1,0,4))
        self.assertEqual(a['surviving'],0)

    def test_compatible_readings_can_hide_target(self):
        a=hidden_target_counterexample()
        self.assertEqual(a['surviving'],1)
        self.assertEqual(a['innovation_energies'],(0,0,0,0))
        self.assertEqual(sum(a['innovation_energies'])+a['surviving'],1)

    def test_compatible_functionals_can_be_unbounded(self):
        coords=tuple(F(1) for _ in range(18))
        self.assertEqual(compatible_functionals_square_norm(coords),tuple(range(1,19)))
        self.assertEqual(compatible_functionals_square_norm(tuple(F(1,2**n) for n in range(10)))[-1],
                         sum((F(1,4**n) for n in range(10)),F(0)))

    def test_source_guards(self):
        with self.assertRaises(CutSourceError): orthogonal_innovations((1,2),((1,2,3),))
        with self.assertRaises(CutSourceError): dot((1,),(1,2))
        with self.assertRaises(CutSourceError): compatible_functionals_square_norm((1.0,))

if __name__=='__main__':unittest.main()
