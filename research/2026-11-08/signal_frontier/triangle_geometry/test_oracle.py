from fractions import Fraction as F
import unittest
import mpmath as mp
from oracle import Golden,ALPHA,ZERO,intervals,grade_source,grade_geometry,cayley,source,tv

class TriangleGeometryTests(unittest.TestCase):
    def test_exact_field_and_orientation(self):
        self.assertEqual(ALPHA+ALPHA**2,Golden(1))
        for a in range(-4,5):
            for b in range(-4,5):
                x=Golden(a,b)
                if x!=ZERO:self.assertEqual(x*x.inverse(),Golden(1))
        self.assertEqual((ALPHA-F(3,5)).sign(),1)
        self.assertEqual((ALPHA-F(5,8)).sign(),-1)
    def test_posterior_not_arc_probability(self):
        q=grade_source(1,2);g=grade_geometry(2)
        self.assertEqual(sum(q),1);self.assertEqual(sum(g,ZERO),Golden(1))
        self.assertTrue(any(Golden(x)!=y for x,y in zip(q,g)))
        self.assertGreater(tv(1,2).sign(),0)
    def test_same_grade_distinct_positions(self):
        row={w:(l,L) for w,l,L in intervals(2)}
        self.assertEqual(row['01'][1],row['10'][1])
        self.assertNotEqual(row['01'][0],row['10'][0])
    def test_source_refinement_and_native_failure(self):
        for a in(1,9,33):
            for m in range(7):
                q=grade_source(a,m)
                self.assertEqual(q,[source.endpoint_mass(a,m,j) for j in range(m+1)])
        self.assertNotEqual(source.R(9)/source.R(1),source.R(17)/source.R(9))
    def test_cayley_boundary(self):
        for p in range(-9,10):
            for q in range(1,8):
                x,y=cayley(p,q);self.assertEqual(x*x+y*y,1)
        self.assertEqual(cayley(1,0),(F(1),F(0)))
        self.assertNotEqual(cayley(0),cayley(1))
    def test_display_guard_does_not_change_ambient_precision(self):
        before=mp.mp.dps
        actual=(ALPHA**200).numerical()
        self.assertEqual(mp.mp.dps,before)
        self.assertGreater(actual,0)
        with mp.workdps(100):
            expected=((mp.sqrt(5)-1)/2)**200
            self.assertLess(abs(actual/expected-1),mp.mpf('1e-80'))
    def test_domains(self):
        for args in((-1,0),(1,-1)):
            with self.assertRaises(ValueError):intervals(*args)
        with self.assertRaises(ValueError):grade_source(0,3)
        with self.assertRaises(ZeroDivisionError):ZERO.inverse()

if __name__=='__main__':unittest.main()
