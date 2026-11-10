"""Standalone, bounded Omega-Haar research tests. No repo suite/CI needed."""
import unittest
import math
from fractions import Fraction
from cmath import exp, pi
from omega_haar import *

class TestOmegaHaar(unittest.TestCase):
    def test_omega_source_multiclock_diamond(self):
        self.assertEqual((2*3, 3*2), (6,6))
        for n in (0,1,3,10,257,1024):
            for x in (Fraction(0),Fraction(1,19),Fraction(-133,17)):
                self.assertEqual(grouped_fold(n,(2,2,2),x), grouped_fold(n,(3,3),x))
                self.assertEqual(grouped_fold(n,(2,2,2),x), fold(n,6,x))
                self.assertEqual(grouped_fold(n,(1,1,1,1,1,1),x), fold(n,6,x))
                self.assertEqual(grouped_fold(n,(3,3),x,mutate=True), fold(n,6,x,mutate=True))

    def test_projection_commutator_exact(self):
        for n in (0,1,2,10,257,1024,10_000):
            v=source_block(n)
            self.assertEqual(commutator(v),commutator_closed(v))
            self.assertEqual(energy(commutator(v)),norm_squared_formula(v))
            self.assertGreater(energy(commutator(v)),0)
            self.assertGreater(source(n),source(n+1))
            self.assertEqual(energy(commutator(reversal(v))),energy(commutator(v)))
        self.assertEqual(commutator((Fraction(1),)*6),(Fraction(0),)*6)
        self.assertEqual(commutator(tuple(Fraction(i) for i in range(6))),
                         commutator_closed(tuple(Fraction(i) for i in range(6))))

    def test_skew_and_rank_2(self):
        basis=[tuple(Fraction(int(i==j)) for i in range(6)) for j in range(6)]
        col=[commutator(e) for e in basis]
        mat=[[col[j][i] for j in range(6)] for i in range(6)]
        for i in range(6):
            for j in range(6):
                self.assertEqual(mat[i][j],-mat[j][i])
        # C^3 = -(2/9)C, and C nonzero. Hence nonzero singular value sqrt(2)/3.
        for e in basis:
            ce=commutator(e)
            c3=commutator(commutator(ce))
            self.assertEqual(c3,tuple(-Fraction(2,9)*x for x in ce))

    def test_source_order_and_mutation(self):
        for n in (1024,4096,16384):
            d=math.sqrt(float(energy(commutator(source_block(n)))))
            const=(15/64)*math.sqrt(44/3)
            self.assertLess(abs(n**3*d/const-1),0.07)
            d_mut=math.sqrt(float(energy(commutator(source_block(n,mutate=True)))))
            const_mut=(1/8)*math.sqrt(33)/3
            self.assertLess(abs(n**2*d_mut/const_mut-1),0.07)
            self.assertGreater(n*n*d_mut,0.0)

    def test_missing_5_dimensions_of_inverse(self):
        for n in (0,12,1024):
            v=source_block(n)
            scalar, reconstruction, defect=inverse_scalar_reconstruction(v)
            self.assertEqual(sum(Q**j*reconstruction[j] for j in range(6)),scalar)
            self.assertEqual(tuple(reconstruction[j]+defect[j] for j in range(6)),v)
            self.assertGreater(energy(defect),0)
        const=(Fraction(1),)*6
        _,_,d=inverse_scalar_reconstruction(const)
        self.assertGreater(energy(d),0)   # even constants don't align with weighted observation

    def test_branch_harmonics_and_mobius_holonomy(self):
        for t in (0.0,0.13,0.5,0.91):
            for h in (1,7,8,9,24,40,16,32,-8):
                f=lambda s: exp(2j*pi*h*s)
                a=branch_dft(fiber_at(t,f))
                b=branch_dft(fiber_at(t+1,f))
                for m in range(16):
                    self.assertLess(abs(b[m] - exp(2j*pi*m/16)*a[m]),1e-12)
                    if h%16 == m:
                        self.assertLess(abs(a[m] - exp(2j*pi*h*t/16)),1e-12)
                    else:
                        self.assertLess(abs(a[m]),1e-12)
                self.assertLess(abs(branch_parity_detail(fiber_at(t,f))-a[8]),1e-12)

    def test_unitary_filter_bank(self):
        for t in (.001,.44,.94):
            f=lambda s: exp(2j*pi*9*s) + .37*exp(-2j*pi*8*s) + 0.43
            v=fiber_at(t,f)
            d=branch_dft(v)
            vr=branch_idft(d)
            self.assertLess(max(abs(a-b) for a,b in zip(v,vr)),1e-12)
            self.assertLess(abs(sum(abs(x)**2 for x in v)/16-
                                sum(abs(x)**2 for x in d)),1e-12)
            self.assertLess(abs(sum(abs(x-d[0])**2 for x in v)/16-
                                sum(abs(x)**2 for x in d[1:])),1e-12)

    def test_mobius_cos_zeros(self):
        for t in (0.0, .25,.5,.75,1.0,1.25):
            v=fiber_at(t,lambda s: math.cos(2*math.pi*8*s))
            self.assertLess(abs(branch_parity_detail(v)-math.cos(math.pi*t)),2e-13)

    def test_strict_source_chronological_area(self):
        for n in (0,1,2,7,20,100,1024,4096,10_000):
            area=chronological_area(n)
            self.assertGreater(area,0)
            v=source_block(n)
            w=source_block(n+1)
            # Source-independent exact skew pairing, zero under orientation swap.
            self.assertEqual(area, -sum((x*y for x,y in zip(w,commutator(v))), Fraction()))
            a=lambda v: v[0]+v[1]-v[4]-v[5]
            b=lambda v: v[3]-v[2]
            self.assertEqual(area,(b(v)*a(w)-a(v)*b(w))/6)
        for n in (10000,100000):
            self.assertLess(abs(float(chronological_area(n))*n**9/(675/128)-1),0.04)

    def test_crt_2x3_mixed_haar_not_same_as_chronological_overlap(self):
        for n in (0,1,7,100):
            v=source_block(n)
            first,second=residue_23_mixed(v)
            self.assertGreater(first,0)
            self.assertNotEqual((first,second),(Fraction(0),Fraction(0)))
            self.assertEqual(first, v[0]-v[3]-v[4]+v[1])
        # Independent CRT row/column averaging commutes, contrasting with
        # adjacent chronological 2/3 partitions. This is a hostile basis control.
        v=source_block(17)
        grid=((v[0],v[4],v[2]),(v[3],v[1],v[5]))
        row_avg=tuple(sum(row,Fraction())/3 for row in grid)
        col_avg=tuple((grid[0][k]+grid[1][k])/2 for k in range(3))
        overall=sum(v,Fraction())/6
        self.assertEqual(sum(row_avg,Fraction())/2,overall)
        self.assertEqual(sum(col_avg,Fraction())/3,overall)

    def test_forward_branches_coalesce_but_lift_restores(self):
        for t in (Fraction(0),Fraction(1,13),Fraction(8,19)):
            before=forward_branch_erasure(t,0)
            self.assertEqual(len(set(before)),16)
            for j in (1,2,3,4):
                after=forward_branch_erasure(t,j)
                self.assertEqual(len(set(after)),1)
                self.assertEqual(after[0],(16**(j-1)*t)%1)

    def test_exact_carry_phase_and_finite_coherent_counterseed(self):
        # Exact finite-source identity: theta_n=(d_n+theta_(n+1))/16.
        # The half-angle phase of the parity bundle is 8*theta_n=(d+t)/2.
        for L in (8, 13, 24):
            prefix=sum((Fraction(1,16**(j+1))*source(j) for j in range(L)), Fraction())
            for n in range(L):
                u=16**n*prefix
                theta=u-u.numerator//u.denominator
                t=(16*theta)
                d=t.numerator//t.denominator
                t-=d
                self.assertEqual(16*theta, d+t)
                self.assertEqual(8*theta, Fraction(d,2)+t/2)
                self.assertEqual((-1)**d, (1 if d%2==0 else -1))
                # Rational wrong seed -P_L produces identically zero completed orbit.
                self.assertEqual(16**n*(-prefix+prefix),Fraction())
            # Verify that the ORIGINAL four-pole recurrence with seed -P_L
            # and its actual finite tail gives that identical zero completion.
            u=-prefix
            for n in range(L+1):
                T=sum((Fraction(1,16**(j-n))*source(j-1)
                       for j in range(n+1,L+1)),Fraction())
                self.assertEqual(u+T,Fraction())
                if n<L:
                    u=16*u+source(n)
        self.assertEqual(commutator((Fraction(0),)*6),(Fraction(0),)*6)

if __name__=='__main__':
    unittest.main(verbosity=2)
