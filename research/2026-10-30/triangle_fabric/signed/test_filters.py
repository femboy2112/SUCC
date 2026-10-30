import unittest
from fractions import Fraction as Q
from math import ceil
from filters import *

CASES=((0,1),(0,2),(1,1),(1,2),(2,3),(3,2),(4,4),(5,3),(7,4),(8,5),(11,6))

class TestFilters(unittest.TestCase):
    def test_orthogonal(self):
        for n,m in CASES:
            p=orthogonal(n,m)
            self.assertEqual(p[-1],1)
            self.assertGreater(square_norm(p,m),0)
            for k in range(n):
                self.assertEqual(sum((c*moment(j+k,m) for j,c in enumerate(p)),Q(0)),0)

    def test_filter_degree_and_annihilation(self):
        for n,m in CASES:
            f=matched_filter(n,m)
            self.assertEqual(len(f)-1,n+m)
            self.assertEqual(evaluate(f,16),0)
            for j in range(m):
                self.assertEqual(evaluate(derivative(add(f,(-1,)),j),1),0)
            self.assertNotEqual(evaluate(derivative(add(f,(-1,)),m),1),0)

    def test_kernel_jets(self):
        for n,m in CASES:
            f=matched_filter(n,m)
            for k in range(m+1):
                self.assertEqual(pole_jet(f,k),pole_jet((Q(1),),k))
            self.assertNotEqual(pole_jet(f,m+1),pole_jet((Q(1),),m+1))

    def test_prefix_and_first_failure(self):
        for n,m in CASES:
            f=matched_filter(n,m)
            for k in range(1,n+1):
                self.assertEqual(apply_filter(f,k),force(k))
            p=orthogonal(n,m)
            predicted=-(-1)**m*square_norm(p,m)/(15**m*evaluate(p,16))
            self.assertEqual(apply_filter(f,n+1)-force(n+1),predicted)
            self.assertNotEqual(predicted,0)

    def test_positive_relative_bounds(self):
        for n,m in CASES:
            f=matched_filter(n,m); eps=Q(1,15**(n+m))
            for k in range(1,max(32,2*n+4)+1):
                value=apply_filter(f,k)
                self.assertGreater(value,0)
                self.assertLessEqual(abs(value-force(k)),eps*force(k))
            for j in range(257):
                self.assertLessEqual(abs(evaluate(f,Q(j,256))-1),eps)

    def test_exact_telescope(self):
        for n,m in CASES:
            f=matched_filter(n,m); u=orbit(f,48); q0=tail_from_filter(f,0)
            for k in range(49):
                self.assertEqual(u[k],16**k*q0-tail_from_filter(f,k))

    def test_pi_brackets(self):
        for n,m in CASES:
            _,a=boundary(matched_filter(n,m))
            lo,hi=bbp_pi_interval(100)
            lower,upper=sign_error_bounds(n,m)
            if m%2:
                self.assertGreater(a,hi)
                self.assertGreaterEqual(a-hi,lower)
                self.assertLessEqual(a-lo,upper)
            else:
                self.assertLess(a,lo)
                self.assertGreaterEqual(lo-a,lower)
                self.assertLessEqual(hi-a,upper)

    def test_dyadic_coherence(self):
        for n,m in ((0,2),(2,4),(5,4),(8,6)):
            f,row=dyadic_filter(n,m)
            onset=1+(row['denominator_power']+3)//4
            u=orbit(f,onset+32)
            for j in range(onset,onset+33):
                self.assertEqual((16**(j-1)*row['dyadic']).denominator,1)
                self.assertEqual((u[j]+tail_from_filter(f,j)).denominator,1)
            for j in range(1,n+1):
                self.assertEqual(apply_filter(f,j),force(j))
            for k in range(m+1):
                self.assertEqual(pole_jet(f,k),pole_jet((Q(1),),k))

    def test_period_affine_classification(self):
        for f in ((Q(1),),(Q(2),Q(-3),Q(1)),(Q(7,9),Q(-1,11),Q(2,13)),(Q(16),Q(-1))):
            a,b=quotient(f)
            self.assertEqual(add((a,),mul((Q(16),Q(-1)),b)),trim(f))
            u=orbit(f,24); original=orbit((Q(1),),24)
            b0=apply_filter(b,1)
            for n in range(25):
                self.assertEqual(u[n],a*original[n]+16**n*b0-apply_filter(b,n+1))

    def test_controls(self):
        self.assertEqual(evaluate((Q(1),),16),1)
        with self.assertRaises(ValueError): tail_from_filter((Q(1),),0)
        self.assertEqual(force(1),Q(47,15))
        # Authentic four-pole passport does not survive the nonconstant filter.
        for n,m in CASES:
            self.assertGreater(len(matched_filter(n,m)),1)

    def test_invalid_domain(self):
        for n,m in ((-1,1),(1,0)):
            with self.assertRaises(ValueError): orthogonal(n,m)
        with self.assertRaises(ValueError): dyadic_filter(2,3)

if __name__=='__main__': unittest.main()
