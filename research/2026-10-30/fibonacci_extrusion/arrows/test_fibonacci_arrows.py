import unittest
from fractions import Fraction as F
from fibonacci_arrows import (LAM,QL,R,fib,lucas,harmonic,cycle_witness,
    paired_alias,moment,tomography,projection_residual,twice_integrated,
    poly_moment,infinite_norm_bracket,zeckendorf)


class FibonacciArrowTests(unittest.TestCase):
    def test_quadratic_field(self):
        self.assertEqual(LAM*LAM,1-LAM)
        self.assertEqual(LAM/LAM,QL(1))
        for n in range(1,18):
            self.assertEqual(LAM**n,(-1)**n*QL(fib(n-1),-fib(n)))

    def test_fibonacci_lucas_translation_rank(self):
        for j in range(18):
            for n in range(1,18):
                self.assertEqual(fib(j+n),fib(n)*fib(j+1)+fib(n-1)*fib(j))
                self.assertEqual(lucas(j+n),2*fib(j+n+1)-fib(j+n))

    def test_cycle_margins(self):
        Z,rank,dim=cycle_witness()
        self.assertEqual(dim,24)
        self.assertLessEqual(rank,23)
        self.assertTrue(any(Z.values()))
        for i in range(7):
            self.assertEqual(sum(x for (r,c),x in Z.items() if r==i),0)
        for j in range(12):
            self.assertEqual(sum(x for (r,c),x in Z.items() if c==j),0)

    def test_native_positive_alias(self):
        for a in (1,17,57,97,233):
            J,K,Z,eps,rank,dim=paired_alias(a)
            self.assertEqual(sum(J.values()),1)
            self.assertEqual(sum(K.values()),1)
            self.assertTrue(all(v>0 for v in K.values()))
            self.assertNotEqual(J,K)
            funcs=[lambda j:QL(1),lambda j:QL(harmonic(j)),lambda j:LAM**j]
            funcs += [lambda j,n=n:QL(fib(j+n)) for n in (0,1,2,3,8,17)]
            funcs += [lambda j,n=n:QL(lucas(j+n)) for n in (0,1,4,9,19)]
            for f in funcs:
                for g in funcs:
                    self.assertEqual(moment(J,f,g),moment(K,f,g))

    def test_discrete_tomography(self):
        for rows,cols in ((2,3),(3,2),(4,3),(5,2)):
            weights={(i,j):F(1+i+2*j) for i in range(rows) for j in range(cols)}
            total=sum(weights.values())
            J={e:v/total for e,v in weights.items()}
            _,out=tomography(J,rows,cols)
            for (i,j),v in J.items():
                self.assertEqual(out[i][j],QL(v))

    def test_continuous_residual_and_fourth_moment(self):
        for L,last in ((0,3),(0,5),(2,5),(7,8),(12,6),(29,9)):
            h,norm2,product=projection_residual(L,last)
            self.assertEqual(norm2,product)
            self.assertGreater(norm2,0)
            g=twice_integrated(h,L)
            self.assertEqual(poly_moment(g,0),0)
            for n in range(2,last+1):
                self.assertEqual(poly_moment(g,fib(n)),0)
            self.assertEqual(poly_moment(g,4),norm2/F((L+5)*(L+6)))
            self.assertGreater(poly_moment(g,4),0)

    def test_uniform_noise_checkerboard(self):
        for M in (0,1,3,9):
            A={(M,M+1):F(1,2),(M+1,M+2):F(1,2)}
            B={(M,M+2):F(1,2),(M+1,M+1):F(1,2)}
            self.assertEqual(sum(abs(A.get(e,0)-B.get(e,0))
                                 for e in set(A)|set(B))/2,1)
            for n in range(4):
                for l in range(4):
                    q,r=LAM**fib(n+2),LAM**fib(l+2)
                    defect=moment(A,lambda i:q**i,lambda j:r**j)-moment(B,lambda i:q**i,lambda j:r**j)
                    self.assertEqual(defect,F(1,2)*q**M*(1-q)*r**(M+1)*(1-r))

    def test_source_density_polynomial_certificate(self):
        # 8Q(t^8)-15(1-t^8)=(1-t)^2 P(t), P coefficient-positive.
        P=[17,34,51,52,45,30,15]
        product=[0]*9
        for j,c in enumerate(P):
            product[j]+=c
            product[j+1]-=2*c
            product[j+2]+=c
        self.assertEqual(product,[17,0,0,-16,-8,-8,0,0,15])
        self.assertTrue(all(c>0 for c in P))

    def test_infinite_product_positive_tail(self):
        for L in (0,2,7,12,29):
            low,high,tail=infinite_norm_bracket(L)
            self.assertGreater(low,0)
            self.assertLess(low,high)
            self.assertLess(tail,1)

    def test_native_density_lower_bound_parameters(self):
        for a in (F(1),F(17),F(57),F(97),F(233),F(5,7)):
            from math import ceil
            L=max(0,ceil(a/8-1))
            delta=F(15,128)/R(a)
            # Exact squared global ratio bound, without sampling density.
            ratio2=(delta*F(64,15)*R(a))**2/F(3*(2*L+13))
            self.assertLess(ratio2,F(1,4))
            self.assertGreaterEqual(L,a/8-1)

    def test_zeckendorf_composition(self):
        for n in list(range(501))+list(range(1000,1301)):
            js=zeckendorf(n)
            self.assertEqual(sum(fib(j) for j in js),n)
            self.assertTrue(all(a-b>=2 for a,b in zip(js,js[1:])))
        self.assertEqual(zeckendorf(4),[4,2])

    def test_wrong_dense_exponent_control(self):
        # Including the omitted fourth power makes residual target belong
        # to the span, so the Cauchy product has an exact zero factor.
        for L in (0,7,29):
            q=L+6
            self.assertEqual(F(q-(L+4+2),q+(L+4+2)+1),0)


if __name__=="__main__":
    unittest.main()
