"""Rational hostile tests for inverse observation and source authentication."""
import unittest
from fractions import Fraction
from finite_alias import (moment,monic_orthogonal,root_certificate,
    first_moment_differences,inner,evaluate)


class FiniteAliasTests(unittest.TestCase):
    def test_explicit_N_zero(self):
        self.assertEqual(monic_orthogonal(0),[Fraction(-1,45),Fraction(1)])

    def test_exact_every_finite_prefix_has_nonzero_kernel(self):
        for N in range(9):
            dif=first_moment_differences(N)
            self.assertTrue(all(x==0 for x in dif[:N+1]))
            self.assertGreater(dif[N+1],0)  # monic q: equals squared L² norm
            self.assertEqual(dif[N+1],inner(monic_orthogonal(N),monic_orthogonal(N)))

    def test_positive_kernel_and_distinct_completed_values(self):
        for N in range(8):
            cert=root_certificate(N)
            c=cert['coefficients'];eps=cert['epsilon']
            self.assertEqual(c[-1],Fraction(1))
            self.assertGreater(cert['q16'],0)
            self.assertGreater(cert['lower_delta_pi'],0)
            self.assertGreater(cert['upper_delta_pi'],cert['lower_delta_pi'])
            self.assertLessEqual(sum(abs(a) for a in c)*eps,1)
            # For any t in [0,1], |epsilon q(t)|<=1, M(x)>=4.
            for i in range(101):
                t=Fraction(i,100)
                self.assertLess(abs(eps*evaluate(c,t)),Fraction(2))

    def test_independent_sympy_nullspace_oracle(self):
        try:
            import sympy as sp
        except ImportError:
            self.skipTest('sympy optional for independent nullspace oracle')
        for N in range(5):
            M=sp.Matrix([[sp.Rational(1,(8*(i+j)+1)*(8*(i+j)+2))
                          for j in range(N+2)] for i in range(N+1)])
            self.assertEqual(M.rank(),N+1)
            v=M.nullspace()
            self.assertEqual(len(v),1)
            v0=v[0]/v[0][-1]
            self.assertEqual([Fraction(int(x.p),int(x.q)) for x in v0],monic_orthogonal(N))

    def test_completion_difference_positive_first_terms(self):
        for N in range(5):
            d=first_moment_differences(N)
            self.assertEqual(d[N+1],inner(monic_orthogonal(N),monic_orthogonal(N)))
            # First unobserved moment is already strictly different.
            self.assertGreater(d[N+1],0)


if __name__=='__main__':unittest.main(verbosity=2)
