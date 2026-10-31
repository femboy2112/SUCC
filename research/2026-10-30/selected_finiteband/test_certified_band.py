import unittest
from fractions import Fraction as F
import certified_band as c


def atan_bounds(q, terms):
    a=sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms)), F(0))
    b=a+F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(a,b),max(a,b)


class IntervalCertificates(unittest.TestCase):
    def test_original_four_signed_poles(self):
        for n in range(1,301):
            self.assertEqual(F(*c.source_pair(n)), F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))

    def test_pi_against_independent_machin_interval(self):
        a,b=atan_bounds(5,100)
        d,e=atan_bounds(239,40)
        lo,hi=16*a-4*e,16*b-4*d
        for bits in (64,128,256):
            x,y=c.pi_interval(bits)
            self.assertLess(F(x,2**bits),lo)
            self.assertGreater(F(y,2**bits),hi)

    def test_exact_original_rational_prefix_containment(self):
        u=F(0)
        for n,iv in c.selected_intervals(64):
            r=F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
            u=(16*u+r)%1
            low,high=F(iv[0],c.S),F(iv[1],c.S)
            self.assertTrue(any(low<=u+k<=high for k in (-1,0,1)))

    def test_trig_exact_quarter_turns_and_wrap(self):
        for n in range(-12,13):
            z=c.trig(c.fraction(n,4))
            a,b=((1,0),(0,1),(-1,0),(0,-1))[n%4]
            self.assertLessEqual(z[0][0],a*c.S)
            self.assertGreaterEqual(z[0][1],a*c.S)
            self.assertLessEqual(z[1][0],b*c.S)
            self.assertGreaterEqual(z[1][1],b*c.S)

    def test_unit_disk_powers_exact_rational_circle(self):
        z=(c.fraction(3,5),c.fraction(4,5))
        r,i=F(1),F(0)
        for iv in c.unit_powers(z,80):
            r,i=F(3,5)*r-F(4,5)*i,F(4,5)*r+F(3,5)*i
            for t,bounds in zip((r,i),iv):
                self.assertLessEqual(F(bounds[0],c.S),t)
                self.assertGreaterEqual(F(bounds[1],c.S),t)

    def test_tail_independent_long_fraction(self):
        for n in (1,3,19,73,4096):
            iv=c.tail_interval(n)
            exact=sum((F(*c.source_pair(n+j))/16**j for j in range(1,70)),F(0))
            rem=F(*c.source_pair(n+70))/(15*16**69)
            self.assertLessEqual(F(iv[0],c.S),exact)
            self.assertGreaterEqual(F(iv[1],c.S),exact+rem)

    def test_lower_floor_and_upper_ceiling(self):
        for a in (-10**30,-1,0,1,10**30):
            self.assertLessEqual(F(c.decimal_out(a,True)),F(a,c.S))
            self.assertGreaterEqual(F(c.decimal_out(a,False)),F(a,c.S))


if __name__=="__main__":unittest.main(verbosity=2)
