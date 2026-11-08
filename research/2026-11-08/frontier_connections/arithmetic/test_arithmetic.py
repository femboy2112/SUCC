import itertools
from collections import Counter
from math import factorial
from fractions import Fraction as F
import random
import unittest

from mixed_quadratic import Box, Interval, SCALE, Q, scan, direct_box, quantize, root_table


def add(z,w):return (z[0]+w[0],z[1]+w[1])
def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def conj(z):return (z[0],-z[1])
def norm2(z):return z[0]*z[0]+z[1]*z[1]


def weighted_collision(p, values):
    fibers={}
    for x,z in values.items():
        for y,w in values.items():
            key=((x+y)%p,(x*x+y*y)%p)
            fibers[key]=add(fibers.get(key,(F(0),F(0))),mul(z,w))
    return sum(norm2(z) for z in fibers.values())


class QuadraticAlgebraTests(unittest.TestCase):
    def test_exact_fourth_moment_all_subsets(self):
        cases=0
        for p in (3,5,7):
            for mask in range(1,1<<p):
                vals={x:(F((x%3)-1,2),F((x%2),3)) for x in range(p) if mask>>x&1}
                energy=sum(norm2(z) for z in vals.values())
                fourth=sum(norm2(z)**2 for z in vals.values())
                self.assertEqual(weighted_collision(p,vals),2*energy**2-fourth)
                cases+=1
        self.assertEqual(cases,165)

    def test_higher_moment_curve_weighted_collision(self):
        cases=0
        for p,D,xs in ((5,3,[0,1,2,3]),(7,3,[0,1,3,5,6]),(7,4,[0,1,2,4])):
            values={x:(F((x%3)+1,4),F((x%2)-1,5)) for x in xs}
            fibers={}
            multisets={}
            for word in itertools.product(xs,repeat=D):
                key=tuple(sum(pow(x,j,p) for x in word)%p for j in range(1,D+1))
                product=(F(1),F(0))
                for x in word:product=mul(product,values[x])
                fibers[key]=add(fibers.get(key,(F(0),F(0))),product)
                mult=tuple(sorted(Counter(word).items()))
                multisets[mult]=True
            lhs=sum(norm2(z) for z in fibers.values())
            rhs=F(0)
            for mult in multisets:
                c=factorial(D);weight=F(1)
                for x,k in mult:
                    c//=factorial(k)
                    weight*=norm2(values[x])**k
                rhs+=c*c*weight
            self.assertEqual(lhs,rhs);cases+=len(fibers)
        self.assertEqual(cases,90)

    def test_odd_prime_pair_uniqueness_and_tomography(self):
        cases=0
        for p in (3,5,7,11,13,17):
            for x in range(p):
                for y in range(p):
                    if x==y:continue
                    s,t=(x*x-y*y)%p,(x-y)%p
                    xx=((s*pow(t,-1,p)+t)*pow(2,-1,p))%p
                    yy=((s*pow(t,-1,p)-t)*pow(2,-1,p))%p
                    self.assertEqual((xx,yy),(x,y));cases+=1
        self.assertEqual(cases,606)

    def test_affine_transport_exact_exponent_identity(self):
        count=0
        for p in (3,5,7):
            rng=random.Random(p)
            for _ in range(200):
                u=rng.randrange(1,p)
                v,c,d,e,a,b=[rng.randrange(p) for _ in range(6)]
                aa=(a-c)*u*u%p
                bb=u*(b-d+2*(a-c)*v)%p
                anchor=((c-a)*v*v+(d-b)*v+e)%p
                for x in range(p):
                    y=(u*x+v)%p
                    self.assertEqual(((c-a)*y*y+(d-b)*y+e)%p,
                                     (anchor-aa*x*x-bb*x)%p)
                    count+=1
        self.assertEqual(count,3000)

    def test_two_point_tomography_ambiguity(self):
        z1,z2=(F(2),F(0)),(F(3),F(0))
        w1,w2=z2,z1
        self.assertEqual(mul(z1,conj(z2)),mul(w1,conj(w2)))
        self.assertEqual(norm2(z1)+norm2(z2),norm2(w1)+norm2(w2))
        self.assertNotEqual(norm2(z1),norm2(w1))

    def test_characteristic_two_failure(self):
        values={0:(F(1),F(0)),1:(F(1),F(0))}
        self.assertEqual(weighted_collision(2,values),8)
        self.assertNotEqual(weighted_collision(2,values),6)

    def test_phase_blind_moments(self):
        p=13
        original={x:(F((x%4)+1,5),F(0)) for x in (1,3,4,9,10,12)}
        rotations=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
        mutated={x:mul(z,rotations[x%4]) for x,z in original.items()}
        self.assertEqual(weighted_collision(p,original),weighted_collision(p,mutated))
        self.assertNotEqual(original,mutated)

    def test_integer_scanner_every_small_coefficient(self):
        count=0
        for p in (3,5,11):
            xs=list(range(1,p))
            boxes=[Box(Interval.ratio((x%3)-1,3),Interval.ratio((x%4)-2,5)) for x in xs]
            result=scan(xs,boxes,p,1,chunk=3,retain=True)
            radius=F(result['correlation_L1_error']['numerator'],result['correlation_L1_error']['denominator'])
            den=result['correlation_denominator']
            for a,centers in result['centers']:
                for b,(x,y) in enumerate(centers):
                    box=direct_box(xs,boxes,p,a,b)
                    distance=F(max(abs(box.re.lo*den-x*SCALE),abs(box.re.hi*den-x*SCALE)),SCALE*den)
                    distance+=F(max(abs(box.im.lo*den-y*SCALE),abs(box.im.hi*den-y*SCALE)),SCALE*den)
                    self.assertLessEqual(distance,radius);count+=1
        self.assertEqual(count,155)

    def test_int64_matches_python_integers_all_small_coefficients(self):
        count=0
        for p in (3,5,11):
            xs=list(range(1,p))
            boxes=[Box(Interval.ratio((x%3)-1,3),Interval.ratio((x%4)-2,5)) for x in xs]
            result=scan(xs,boxes,p,1,chunk=3,retain=True)
            table,_=root_table(p)
            roots=[(int(x),int(y)) for x,y in table]
            centers=[quantize(z)[0] for z in boxes]
            for a,computed in result['centers']:
                for b,actual in enumerate(computed):
                    real=imag=0
                    for x,z in zip(xs,centers):
                        qr,qi=roots[a*x*x%p]
                        zr=(z[0]*qr-z[1]*qi)//Q
                        zi=(z[0]*qi+z[1]*qr)//Q
                        lr,li=roots[b*x%p]
                        real+=zr*lr-zi*li
                        imag+=zr*li+zi*lr
                    self.assertEqual(actual,(real,imag));count+=1
        self.assertEqual(count,155)

    def test_wrong_sign_and_scaling_rejected(self):
        p=11;xs=[1,2,4,5,7]
        boxes=[Box(Interval.ratio(x,11),Interval.ratio(1-x,13)) for x in xs]
        result=scan(xs,boxes,p,1,chunk=3,retain=True)
        a,b=1,2;centers=dict(result['centers']);x,y=centers[a][b]
        den=result['correlation_denominator']
        good=direct_box(xs,boxes,p,a,b)
        wrong=direct_box(xs,boxes,p,-a,b)
        self.assertFalse(good.re.overlaps(wrong.re) and good.im.overlaps(wrong.im))
        radius=F(result['correlation_L1_error']['numerator'],result['correlation_L1_error']['denominator'])
        scaled_distance=abs(F(x,2*den)-F(good.re.lo,SCALE))+abs(F(y,2*den)-F(good.im.lo,SCALE))
        self.assertGreater(scaled_distance,radius)


if __name__=='__main__':unittest.main()
