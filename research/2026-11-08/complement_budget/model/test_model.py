from fractions import Fraction as Q
import unittest
from model import law_at, law_defects, orbit, transform, rigidity_hypotheses, exact_source_angles


class ModelTests(unittest.TestCase):
    def test_linear_laws_are_exactly_covariant(self):
        for p in (41,73,137):
            for slopes in ((0,), (1,2), (0,1,p-1)):
                polys=[(0,c) for c in slopes]
                self.assertEqual(law_defects(polys,[Q(1,len(polys))]*len(polys),p),
                                 [Q(0)]*len(law_defects(polys,[Q(1,len(polys))]*len(polys),p)))
    def test_nonlinear_closed_orbit_shows_budget_is_necessary(self):
        for p in (41,73,137):
            polys=orbit((0,0,1),p)
            self.assertFalse(rigidity_hypotheses(polys,p))
            self.assertTrue(all(x==0 for x in law_defects(polys,[Q(1,len(polys))]*len(polys),p)))
    def test_missing_orbit_bound_not_just_formula(self):
        for p in (41,73,137):
            full=orbit((0,0,1),p)
            m=len(full)
            for K in (1,2):
                polys=full[:K];D=2
                if K*D>=m: continue
                defects=law_defects(polys,[Q(1,K)]*K,p)
                actual=sum(defects)/len(defects)
                self.assertGreaterEqual(actual,Q(1,K)*(1-Q(K*D,m)))
                self.assertGreater(actual,0)
    def test_positive_unequal_weights(self):
        p=41;polys=[(0,0,1),(0,0,16)]
        defects=law_defects(polys,[Q(1,7),Q(6,7)],p)
        self.assertGreaterEqual(sum(defects)/5,Q(1,7)*(1-Q(4,5)))
    def test_constant_offset_requires_own_sector(self):
        self.assertEqual(transform((1,3),41),(18,3))
        self.assertTrue(any(law_defects([(1,3)],[Q(1)],41)))
        self.assertFalse(any(law_defects([(0,3)],[Q(1)],41)))
    def test_literal_source_cocycle(self):
        for p in (41,73,113):
            data=exact_source_angles(p)
            self.assertEqual(len(data['angles']),data['L'])
            self.assertEqual(data['L'],data['q']*data['m'])
    def test_invalid_law_inputs(self):
        for weights in ((0,1),(-1,2),(Q(1,3),Q(1,3))):
            with self.assertRaises(ValueError):law_at([(0,),(0,1)],weights,1,41)
        self.assertFalse(rigidity_hypotheses([(0,1),(0,1)],41))


if __name__=='__main__':unittest.main()
