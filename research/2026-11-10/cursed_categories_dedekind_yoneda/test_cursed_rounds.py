"""Independent exact-rational calibrations of earlier cursed-category mechanisms."""
import unittest
from fractions import Fraction as Q
from math import gcd
from cut_graph import bbp_r, divisors


def matmul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def matminus(a,b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def projector(blocks):
    out=[[Q(0) for _ in range(6)] for _ in range(6)]
    for block in blocks:
        for i in block:
            for j in block:
                out[i][j]=Q(1,len(block))
    return out


def rank(a):
    mat=[r[:] for r in a]
    m=len(mat); n=len(mat[0]); piv=0
    for col in range(n):
        found=next((i for i in range(piv,m) if mat[i][col]),None)
        if found is None: continue
        mat[piv],mat[found]=mat[found],mat[piv]
        d=mat[piv][col]
        mat[piv]=[z/d for z in mat[piv]]
        for i in range(m):
            if i!=piv and mat[i][col]:
                f=mat[i][col]
                mat[i]=[mat[i][j]-f*mat[piv][j] for j in range(n)]
        piv+=1
        if piv==m:break
    return piv


class CursedRoundChecks(unittest.TestCase):
    def test_two_idempotents_and_oscillator(self):
        p=projector([(0,1),(2,3),(4,5)])
        q=projector([(0,1,2),(3,4,5)])
        self.assertEqual(matmul(p,p),p)
        self.assertEqual(matmul(q,q),q)
        c=matminus(matmul(p,q),matmul(q,p))
        self.assertEqual(rank(c),2)
        self.assertEqual(matmul(matmul(c,c),c),[[-Q(2,9)*z for z in row] for row in c])
        self.assertEqual(c,[[-c[j][i] for j in range(6)] for i in range(6)])

    def test_source_selected_wavelet_orientation_finite(self):
        p=projector([(0,1),(2,3),(4,5)])
        q=projector([(0,1,2),(3,4,5)])
        c=matminus(matmul(p,q),matmul(q,p))
        for n in range(0,8):
            a=[bbp_r(n+j+1) for j in range(6)]
            b=[bbp_r(n+j+2) for j in range(6)]
            oriented=sum((a[i]*c[i][j]*b[j] for i in range(6) for j in range(6)),Q(0))
            self.assertGreater(oriented,0)
        # Finite positivity calibrates, but does not prove, the all-n theorem in SUCC #582.

    def test_idempotent_haar_lie_exact_w1(self):
        # Q delta_0 places mass 1/16 at a/16 (a=0..15), NOT Lebesgue.
        area=sum((Q(1,2*16*16) for _ in range(16)),Q(0))
        self.assertEqual(area,Q(1,32))

    def test_divisor_gcd_right_adjoint_and_coherence(self):
        for n in (12,30,60):
            for m in divisors(n):
                for x in divisors(m):
                    for y in divisors(n):
                        self.assertEqual(y%x==0,gcd(y,m)%x==0)
        for k in (30,60):
            for n in divisors(k):
                for m in divisors(n):
                    for d in divisors(k):
                        self.assertEqual(gcd(gcd(d,n),m),gcd(d,m))

if __name__=='__main__':unittest.main()
