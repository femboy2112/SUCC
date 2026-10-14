"""Source-independent exact dilation and boundary tests."""
import unittest
from fractions import Fraction as Q
from observational_succ.zero_centered_arch_dilation import (
    DilationError,cell_weight,mellin_weight,dilated_cell_index,
    arch_dilate,weighted_norm2,integer_mellin,block_certificate,
    finite_dilation_receipt)


class ZeroCenteredArchDilationTests(unittest.TestCase):
    def test_block_weight_and_mellin(self):
        for q in (2,3,4,5,6,7):
            for j in range(1,14):
                for s in (1,2,3,4):
                    self.assertTrue(block_certificate(q,j,s)["exact"])

    def test_finite_sequence_covariance(self):
        for source in (
            {1:Q(1)},
            {1:Q(1,2),3:Q(1,3),6:Q(-1,7)},
            {2:Q(-1),4:Q(1,2),8:Q(11,9)},
        ):
            for q in (2,3,5):
                for s in (1,2,3):
                    r=finite_dilation_receipt(source,q,s)
                    self.assertTrue(r["normalized_dilation_isometry_exact"])
                    self.assertTrue(r["Mellin_covariance_exact"])
                    self.assertFalse(r["isometry_is_surjective"])
                    self.assertFalse(r["RH_proved"])

    def test_sampling_is_not_dilation(self):
        f={1:Q(1),2:Q(2),3:Q(3)}
        for q in (2,3,4):
            d=arch_dilate(f,q)
            self.assertEqual(d.get(1,0),0)
            self.assertEqual(d[q],1)
            self.assertEqual(d[2*q],2)
            self.assertEqual(d[3*q],3)
            self.assertEqual(weighted_norm2(d),weighted_norm2(f)/q)
        self.assertNotEqual(arch_dilate(f,2).get(1,0),f[2])
        self.assertEqual(dilated_cell_index(2,1),0)

    def test_reject_uncertified(self):
        for fn in (lambda:arch_dilate({1:0.5},2),
                   lambda:arch_dilate({0:Q(1)},2),
                   lambda:arch_dilate({1:Q(1)},1),
                   lambda:block_certificate(3,2,0),
                   lambda:block_certificate(100_000,2,1)):
            with self.assertRaises(DilationError):
                fn()


if __name__=="__main__":
    unittest.main()
