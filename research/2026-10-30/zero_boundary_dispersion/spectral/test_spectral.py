import unittest
from collections import Counter
from fractions import Fraction as F
import spectral_probe as s


class SpectralTests(unittest.TestCase):
    def test_original_source(self):
        self.assertEqual(s.r(1), F(47, 15))
        self.assertEqual(s.orbit(0), [F(0)])

    def test_repunit_source_identity(self):
        for seed in (F(0), F(1,16), F(2,7)):
            u = s.orbit(257, seed)
            for n in (1,2,7,31,97,251):
                for d in range(1,7):
                    self.assertEqual(u[n+d]-u[n]-s.m(d)*(u[n+1]-u[n]), s.source_defect(n,d))

    def test_effective_defect_inequality(self):
        for n in (1,2,7,31,97,251):
            for d in range(1,7):
                x = s.source_defect(n,d)
                self.assertLessEqual(x, 0)
                self.assertLessEqual(-x, s.source_defect_bound(n,d))
                self.assertEqual(x == 0, d == 1)

    def test_pi_and_trigonometric_intervals(self):
        lo, hi = s.pi_interval()
        self.assertLess(F(314159265358979323846, 10**20), lo)
        self.assertLess(hi, F(314159265358979323847, 10**20))
        for q, value in [(F(0),1),(F(1,2),-1),(F(1,4),0),(F(1,3),F(-1,2))]:
            a,b = s.cos_interval(q)
            self.assertLessEqual(a,value)
            self.assertLessEqual(value,b)
            self.assertLess(b-a, F(1,10**20))

    def test_mark_derivative_bound(self):
        for a in (1,9,17,51,97,313,997,10009):
            ps=s.source_marks(a)
            self.assertEqual(sum(ps),1)
            ds=s.mark_derivatives(a)
            self.assertEqual(sum(ds),0)
            self.assertLessEqual(sum(abs(x) for x in ds), F(2,(a+3)**2))

    def test_mark_tail_distance(self):
        limit=(F(6,15),F(4,15),F(5,15))
        for a in (1,9,17,51,97,313,997,10009):
            self.assertLessEqual(sum(abs(x-y) for x,y in zip(s.source_marks(a),limit)),F(2,a+3))

    def test_all_walsh_characters(self):
        for a in range(16):
            for b in range(16):
                self.assertEqual(sum(s.walsh(a,x)*s.walsh(b,x) for x in range(16)),16 if a==b else 0)
        self.assertNotEqual(s.walsh(2,0),s.walsh(2,6))

    def test_noncentral_frames_are_flat(self):
        u=s.orbit(100)
        ks=s.carries(u)
        noncommuting=False
        for n in (3,7,17,31,61):
            frames=[s.marked_frame(ks[n+j]) for j in (0,1,2,3)]
            if s.compose(frames[0],frames[1]) != s.compose(frames[1],frames[0]):
                noncommuting=True
            loop=s.IDENTITY
            for i,j in ((0,1),(1,3),(3,2),(2,0)):
                loop=s.compose(s.edge_frame(frames[i],frames[j]),loop)
            self.assertEqual(loop,s.IDENTITY)
            self.assertEqual(sum((u[n+j]-u[n+i] for i,j in ((0,1),(1,3),(3,2),(2,0))),F(0)),0)
        self.assertTrue(noncommuting)

    def test_circle_aliases(self):
        u=s.orbit(31)
        for seed,start in ((F(1),0),(F(1,16),1)):
            v=s.orbit(31,seed)
            for n in range(start,32):
                self.assertEqual((v[n]-u[n])%1,0)

    def test_stoneham_full_stages(self):
        for c in (3,5):
            for j in (1,2,3):
                counts=Counter(s.stoneham_stage(c,j))
                self.assertEqual(len(counts),c**(j-1))
                self.assertEqual(set(counts.values()),{c*(c-1)})

    def test_stoneham2_transient(self):
        for j in (1,3,5,7):
            stage=s.stoneham_stage(2,j)
            self.assertEqual(stage.count(0),2**j-(j+3)//4)

    def test_de_bruijn_controls(self):
        for order in (1,2,3):
            w=s.de_bruijn(16,order)
            self.assertEqual(len(w),16**order)
            blocks=Counter(tuple(w[(n+i)%len(w)] for i in range(order)) for n in range(len(w)))
            self.assertEqual(len(blocks),16**order)
            self.assertEqual(set(blocks.values()),{1})

    def test_finite_fourier_grid_alias(self):
        q=101
        for h in range(1,7):
            residues=Counter((15*h*j)%q for j in range(q))
            # The corresponding polynomial is 1+X+...+X^100=Phi_101.
            self.assertEqual(residues,Counter(range(q)))
        self.assertEqual(Counter((15*q*j)%q for j in range(q)),{0:q})

    def test_zero_de_bruijn_mixture(self):
        for order in (2,3):
            w=s.de_bruijn(16,order)
            v=w+[0]*(3*len(w))
            self.assertEqual(F(v.count(0),len(v)),F(49,64))
            for ell in range(1,order+1):
                counts=Counter(tuple(v[(n+i)%len(v)] for i in range(ell)) for n in range(len(v)))
                for word,count in counts.items():
                    target=F(1,4*16**ell)+(F(3,4) if not any(word) else 0)
                    self.assertLessEqual(abs(F(count,len(v))-target),F(2*ell,len(v)))


if __name__ == '__main__':
    unittest.main()
