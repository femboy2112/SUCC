import math
import random
import unittest
from collections import Counter
from fractions import Fraction
from finite_band import (
    r, prefix, tail_truncated, hard_collision, fejer, fejer_pair_fourier,
    fejer_pair_kernel, max_unit_arc_mass, stoneham_surrogate,
)

class FejerCertificateTests(unittest.TestCase):
    def test_authentic_source_frozen(self):
        self.assertEqual(r(1), Fraction(47,15))
        self.assertEqual(r(2), Fraction(106,819))
        self.assertGreater(r(1),r(2))

    def test_truncated_green_conjugacy(self):
        xs=prefix(13)
        for n in range(1,10):
            t=tail_truncated(n,10)
            tnext=tail_truncated(n+1,9)
            self.assertEqual(16*t-tnext, r(n+1))
            y=(xs[n-1]+t)%1
            ynext=(xs[n]+tnext)%1
            self.assertEqual(ynext,(16*y)%1)

    def test_fejer_nonnegative_and_value_at_zero(self):
        for H in (2,3,8,16,128):
            self.assertEqual(fejer(0.0,H),float(H))
            for j in range(1,50):
                self.assertGreaterEqual(fejer(j/137.0,H),0)

    def test_closed_form_against_fourier(self):
        points=[Fraction(1,37), Fraction(3,17), Fraction(4,5), Fraction(2,7)]
        for H in (2,3,8,16,64):
            self.assertAlmostEqual(fejer_pair_kernel(points,H),fejer_pair_fourier(points,H),places=10)

    def test_hard_by_fejer_for_source(self):
        pts=prefix(48)
        for m in (1,2):
            q=16**m; H=q//2
            Q=float(hard_collision(pts,q)); F=fejer_pair_fourier(pts,H)
            self.assertLessEqual(Q,math.pi**2/2*F+1e-9)

    def test_hard_by_fejer_adversarial_seams(self):
        pts=[Fraction(0), Fraction(1,16)-Fraction(1,100000),Fraction(1,16),
             Fraction(1,16)+Fraction(1,100000),Fraction(1,2),Fraction(15,16)]
        for q in (16,256):
            H=q//2
            self.assertLessEqual(float(hard_collision(pts,q)),math.pi**2/2*fejer_pair_fourier(pts,H)+1e-8)

    def test_generic_hard_by_fejer_random(self):
        random.seed(0xC0DE)
        for q in (16, 256):
            H=q//2
            for n in (1,3,8,40):
                pts=[Fraction(random.randrange(q*31),q*31) for _ in range(n)]
                self.assertLessEqual(float(hard_collision(pts,q)),math.pi**2/2*fejer_pair_fourier(pts,H)+1e-8)

    def test_fejer_arc_hotspot_bound(self):
        random.seed(33)
        for H in (2,3,8,16,32):
            pts=[Fraction(random.randrange(10000),10000) for _ in range(50)]
            F=fejer_pair_fourier(pts,H)
            arc=3*H*float(max_unit_arc_mass(pts,H))
            self.assertLessEqual(F,arc+1e-8)

    def test_source_green_pair_transfer(self):
        N=32
        xs=prefix(N)
        ys=[(x+tail_truncated(i,10))%1 for i,x in enumerate(xs,1)]
        # Actual partial Green correction has sum <= true B < 1/32.
        for H in (8,16,32):
            delta=abs(fejer_pair_fourier(ys,H)-fejer_pair_fourier(xs,H))
            bound=math.pi*(H*H-1)/(24*N)
            self.assertLess(delta,bound+1e-8)

    def test_coherent_seed_is_not_normal(self):
        for H in (8,128):
            pts=[Fraction(0)]*24
            self.assertAlmostEqual(fejer_pair_fourier(pts,H),H,places=8)
            self.assertEqual(hard_collision(pts,2*H),Fraction(2*H))

    def test_periodic_order_two_debruijn_example(self):
        # Build a deterministic de Bruijn cycle from a directed Eulerian traversal.
        base=16
        adj=[list(range(base-1,-1,-1)) for _ in range(base)]
        path=[]
        def visit(v):
            while adj[v]:
                a=adj[v].pop()
                visit(a)
                path.append(a)
        visit(0)
        digits=path[::-1]
        self.assertEqual(len(digits),256)
        def Q(m):
            counts=Counter(tuple(digits[(i+j)%256] for j in range(m)) for i in range(256))
            return Fraction(base**m * sum(c*c for c in counts.values()), 256**2)
        self.assertEqual(Q(1),1)
        self.assertEqual(Q(2),1)
        self.assertEqual(Q(3),16)

    def test_normal_stoneham_stage_residues(self):
        for c,p in ((3,2),(5,2)):
            stage=stoneham_surrogate(c,p)
            counts=Counter(int(c**p * x) for x in stage)
            expected={j for j in range(c**p) if j%c==1}
            self.assertEqual(set(counts),expected)
            self.assertTrue(all(counts[j]==c*(c-1) for j in expected))
            self.assertEqual(len(stage),(c-1)*c**p)

if __name__ == "__main__": unittest.main(verbosity=2)
