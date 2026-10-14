"""Exact rational orthogonal projector tests for pure dilation obstruction."""
import unittest
from fractions import Fraction as Q
from observational_succ.zero_centered_purity import (
    w,inner,norm2,range_projection,escape_receipt,PurityError)


class PureDilationTests(unittest.TestCase):
    def test_exact_projection_idempotency_orthogonality(self):
        for q in (2,3,4,5):
            a={1:Q(2),2:Q(-3,2),5:Q(1,7),9:Q(4,3)}
            b={2:Q(3,5),4:Q(-1),8:Q(2)}
            pa=range_projection(a,q)
            pb=range_projection(b,q)
            self.assertEqual(range_projection(pa,q),pa)
            self.assertEqual(inner(pa,b),inner(a,pb))
            self.assertLessEqual(norm2(pa),norm2(a))
            self.assertEqual(inner(a,pa),norm2(pa))

    def test_omitted_lower_cells(self):
        for q in (2,3,6):
            for k in range(1,q):
                self.assertEqual(range_projection({k:Q(1)},q),{})
            self.assertNotEqual(range_projection({q:Q(1)},q),{})

    def test_pure_escape_on_finite_sources(self):
        f={1:Q(1),7:Q(-2),35:Q(3)}
        for q in (2,3,5):
            for n in range(1,7):
                result=escape_receipt(f,q,n)
                self.assertEqual(result["every_finite_source_cell_escaped"],
                                 q**n>35)
                self.assertFalse(result["RH_proved"])

    def test_invalid_sources(self):
        for call in (lambda:range_projection({1:0.5},2),
                     lambda:range_projection({0:1},2),
                     lambda:range_projection({1:1},1),
                     lambda:escape_receipt({1:1},2,0)):
            with self.assertRaises(PurityError):
                call()


if __name__=="__main__":
    unittest.main()
