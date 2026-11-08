from fractions import Fraction as Q
import unittest
from observer import (Golden,ALPHA,sign_surd,fibonacci,golden_floor,clock_position,
                      exact_label,golden_discrepancy,alpha_interval,frame_checks,
                      cell_product,phase,Box,ONE,SCALE)


class FibonacciObserverTests(unittest.TestCase):
    def test_return_identity_independent_pair_recurrence(self):
        a,b=0,1
        for k in range(1,41):
            q,p=b,a
            self.assertEqual(q*ALPHA-p,((-1)**(k-1))*ALPHA**k)
            a,b=b,a+b
    def test_surd_sign_independent_enclosures(self):
        lo,hi=alpha_interval();sqrtlo=2*lo+1;sqrthi=2*hi+1
        for a in range(-13,14):
            for b in range(-13,14):
                lower,upper=sorted((a+b*sqrtlo,a+b*sqrthi))
                expected=0 if a==b==0 else (1 if lower>0 else -1)
                self.assertTrue(lower>0 or upper<0 or a==b==0)
                self.assertEqual(sign_surd(a,b),expected)
    def test_floor_exact_and_boundary_labels(self):
        for j in range(300):
            x=clock_position(j)
            self.assertGreaterEqual(x.sign(),0)
            self.assertGreater((1-x).sign(),0)
        for M in (1,4,16):
            for r in range(32):
                self.assertEqual(exact_label(r,32,M,0),(M*r//32)%M)
    def test_discrepancy_bound_is_nonvacuous(self):
        for k in (3,5,7,10):
            q=fibonacci(k);D=golden_discrepancy(k)
            upper=Golden(Q(1,q))+Q(q-1,q)*ALPHA**k
            self.assertGreaterEqual((upper-D).sign(),0)
            self.assertGreaterEqual((D-Q(1,q)).sign(),0)
            self.assertGreater((Q(2,q)-D).sign(),0)
    def test_interval_frame_actual_energies(self):
        rows=frame_checks()
        self.assertEqual(len(rows),32)
        self.assertTrue(all(row['certified'] for row in rows))
    def test_single_cell_keeps_only_marginals(self):
        a=[phase(j,4) for j in range(4)];b=[x.conjugate() for x in a]
        got=cell_product(a,b,[0]*4,1)
        self.assertLessEqual(got.re.lo,0);self.assertGreaterEqual(got.re.hi,0)
        self.assertLessEqual(got.im.lo,0);self.assertGreaterEqual(got.im.hi,0)
        singleton=cell_product(a,b,list(range(4)),4)
        self.assertLessEqual(singleton.re.lo,SCALE);self.assertGreaterEqual(singleton.re.hi,SCALE)
    def test_invalid_domains(self):
        for action in (lambda:fibonacci(-1),lambda:golden_floor(-1),
                       lambda:exact_label(7,7,4,0),lambda:cell_product([],[],[],1),
                       lambda:cell_product([Box(ONE)],[Box(ONE)],[],1)):
            with self.assertRaises(ValueError):action()


if __name__=='__main__':unittest.main()
