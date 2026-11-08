from fractions import Fraction as F
import unittest
from oracle import node,cmul,cpow,matrix,rank,kernel,apply,recover,source_mass,discrete_grades,R

class TriangleTests(unittest.TestCase):
    def test_exact_unit_nodes(self):
        for j in range(-11,12):
            z=node(F(j,3));self.assertEqual(z[0]**2+z[1]**2,1)
            self.assertEqual(cmul(z,cpow(z,-1)),(F(1),F(0)))
    def test_minimal_real_menu(self):
        for m in range(1,10):
            nodes=[node(F(j,2)) for j in range(m+1)]
            self.assertEqual(rank(matrix(nodes,(m+1)//2)),m+1)
            self.assertLess(rank(matrix(nodes,(m-1)//2)),m+1)
    def test_triangle_mass_recovery(self):
        nodes=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0))]
        A=matrix(nodes,1);q=[F(2,7),F(3,7),F(2,7)]
        self.assertEqual(recover(A,apply(A,q)),q)
    def test_alias_is_positive(self):
        A=matrix([node(j) for j in range(5)],1);v=kernel(A)
        q=[F(1,5)]*5;eps=min(F(1,10)/abs(x) for x in v if x)
        l=[x+eps*y for x,y in zip(q,v)];r=[x-eps*y for x,y in zip(q,v)]
        self.assertTrue(all(x>0 for x in l+r));self.assertNotEqual(l,r)
        self.assertEqual(apply(A,l),apply(A,r))
    def test_posterior_countermodel(self):
        a=lambda m:discrete_grades([F(1,5),F(3,5)],[F(1,4),F(3,4)],m)
        b=lambda m:discrete_grades([F(2,5),F(4,5)],[F(3,4),F(1,4)],m)
        self.assertEqual(a(2),b(2));self.assertNotEqual(a(3),b(3))
    def test_source_mass_not_reset_binomial(self):
        q=source_mass(9,2);f=R(17)/R(9)
        self.assertGreater(q[0],f*f)
        self.assertEqual(sum(q),1)
    def test_invalid_models(self):
        with self.assertRaises(ValueError):source_mass(0,2)
        with self.assertRaises(ValueError):discrete_grades([F(0)],[F(1)],2)
        with self.assertRaises(ValueError):recover([[F(1),F(1)]],[F(1)])

if __name__=='__main__':unittest.main()
