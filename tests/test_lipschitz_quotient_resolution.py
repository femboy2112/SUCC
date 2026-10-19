"""Exact parity-specific midpoint/Lipschitz observation obstruction."""
import unittest
from fractions import Fraction as F

def prod(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return tuple(out)
def integral(a):
    return sum((c*(F(1,2)**(i+1)-F(-1,2)**(i+1))/(i+1) for i,c in enumerate(a)),F(0))
def at(a,x):return sum((c*x**i for i,c in enumerate(a)),F(0))
def lip(a):
    return sum((abs((i+1)*v)*F(1,2)**i for i,v in enumerate(a[1:])),F(0))

class ResolutionObstruction(unittest.TestCase):
    odd=(F(0),F(65,8),F(0),F(-455,2),F(0),F(1638),F(0),F(-3432))
    even=(F(0),F(0),F(10725,4),F(0),F(-75075),F(0),F(540540),F(0),F(-1132560))
    def test_local_polynomial_vanishing(self):
        for p,M,E in ((self.odd,F(1066),F(26,165)),
                      (self.even,F(212355),F(18590,17))):
            for t in (F(-1,2),F(0),F(1,2)):self.assertEqual(at(p,t),0)
            self.assertEqual(lip(p),M)
            self.assertEqual(integral(prod(p,p)),E)
            for j in range(4):self.assertEqual(integral((F(0),)*j+p),0)
    def test_exact_parity_minimax_N_inverse_square(self):
        # Divide into N cells of width h=1/N, use Lh P((x-c)/h)/M on each.
        odd=integral(prod(self.odd,self.odd))/lip(self.odd)**2
        even=integral(prod(self.even,self.even))/lip(self.even)**2
        self.assertEqual(odd,F(1,7211490))
        self.assertEqual(even,F(2,82475415))
        for N in (2,4,8,16):
            for C in (odd,even):
                self.assertGreater(C/N**2,0)
                self.assertEqual(C/N**2,4*C/(2*N)**2)
    def test_zero_midpoints_not_zero_energy(self):
        self.assertGreater(F(1,7211490*64),0)
        self.assertGreater(F(2,82475415*64),0)

if __name__=='__main__':unittest.main()
