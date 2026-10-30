"""Exact and independently implemented checks for SUCC extruded-triangle research."""
from fractions import Fraction as F
from math import comb
import unittest
import extruded_triangle as M

class SpacetimeTriangleExact(unittest.TestCase):
    def test_original_source_passport(self):
        self.assertEqual(M.R1, F(47,15))
        self.assertEqual(M.C_SPINE, F(225,3008))
        for n in range(1,20):
            a=8*n-7
            self.assertEqual(M.r(n),M.R(a))
            lo,hi=M.source_R_bounds(a)
            self.assertLessEqual(lo,M.R(a))
            self.assertLessEqual(M.R(a),hi)

    def test_conditioned_spine_telescope(self):
        for n in range(1,20):
            product=F(1)
            for k in range(1,n):
                product*=M.spine_next(k)
                self.assertEqual(M.spine_hazard(k)+M.spine_next(k),1)
            self.assertEqual(product,M.spine_mass(n))

    def test_native_spine_hazard_and_n2_constant(self):
        self.assertEqual(M.spine_mass(1),1)
        self.assertTrue(all(0<M.spine_hazard(n)<1 for n in range(1,20)))
        for n in (100,1000):
            self.assertLess(abs(F(n*n)*M.spine_mass(n)-M.C_SPINE),F(1,n))
            self.assertLess(abs(F(n)*M.spine_hazard(n)-2),F(2,n))

    def test_pascal_finite_flatness_and_bayes(self):
        for a in (1,9,17):
            for m in range(0,7):
                self.assertEqual(sum((M.endpoint_mass(a,m,j) for j in range(m+1)),F(0)),1)
                for j in range(m+1):
                    fail,success=M.posterior_transition(a,m,j)
                    self.assertEqual(fail+success,1)
                    self.assertTrue(0<fail<1 and 0<success<1)
                    expected = (M.endpoint_mass(a,m,j)*fail
                                +(M.endpoint_mass(a,m,j-1)*M.posterior_transition(a,m,j-1)[1]
                                  if j else 0))
                    self.assertEqual(expected,M.endpoint_mass(a,m+1,j))

    def test_fan_mass_independent_route(self):
        for n in range(1,13):
            row=[M.fan_mass(n,j) for j in range(n+1)]
            self.assertEqual(sum(row,F(0)),M.spine_mass(n))
            for j,v in enumerate(row):
                self.assertGreater(v,0)
                self.assertEqual(v,M.fan_mass_independent(n,j))

    def test_grade_fourier_exact_two_routes(self):
        for n in range(1,12):
            for z in (F(-1),F(0),F(1,2),F(1),F(3,2)):
                self.assertEqual(M.fan_fourier(n,z),M.fan_fourier_by_endpoints(n,z))
            self.assertEqual(M.fan_fourier(n,1),M.spine_mass(n))

    def test_zero_spine_and_fan_are_not_independent(self):
        for n in (2,3,7):
            a=8*n-7
            z=M.R(a+8)/M.R(a)
            self.assertGreater(M.R(a+16)/M.R(a),z*z)
            # shared-X failures differ from prematurely resetting after each failure

    def test_chernoff_moment_original_source(self):
        for n in range(3,13):
            for z in (F(9,8), F(5,4)):
                a=8*n-7
                if a-8*n*(z-1)>0:
                    exact=M.fan_fourier(n,z)/M.spine_mass(n)
                    self.assertLessEqual(exact,M.moment_bound(n,z))

    def test_uniform_moving_grade_bound(self):
        for L in range(4,18):
            rhs=M.high_grade_bound(L)
            for n in range(max(1,L-1),min(25,L+5)):
                val=sum(M.native_row(n)[L:],F(0))
                self.assertLessEqual(val,rhs)
            self.assertGreater(rhs,0)

    def test_rigorous_source_constant_without_fake_uniform_gap(self):
        # Limit grade characteristic G(-1)=1/9 is nonzero; n=64 holds nearby.
        n=64
        s=M.fan_fourier(n,-1)/M.spine_mass(n)
        self.assertLess(abs(float(s)-1/9),0.02)
        self.assertNotEqual(s,0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
