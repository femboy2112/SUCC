import unittest
from fractions import Fraction as Q
from math import gcd
from fibonacci_arithmetic import (fibonacci,forcing,states,residue,intertwiners,
    intertwines,hensel_roots,scalar_order,matrix_order,zeckendorf,
    zeckendorf_sqrt_certificate,overwrite_snapshots,word_counts,
    lambda_interval,golden_lag_intervals)


class FibonacciArithmeticTests(unittest.TestCase):
    def test_modular_intertwiners(self):
        for m in list(range(2,41))+[239,478]:
            actual=[(x,y) for x in range(m) for y in range(m)
                    if intertwines((x,y),m)]
            self.assertEqual(set(actual),set(intertwiners(m)))
            self.assertEqual(len(actual),gcd(m,239))

    def test_no_primitive_higher_lift(self):
        for m in (239**2,239**3):
            rows=intertwiners(m)
            self.assertEqual(len(rows),239)
            self.assertTrue(all(intertwines(v,m) for v in rows))
            self.assertTrue(all(gcd(gcd(x,y),m)>=239 for x,y in rows))
        for p in (257,263):self.assertEqual(intertwiners(p),[(0,0)])

    def test_hensel_clock_changes(self):
        roots=hensel_roots(5)
        for m,x in roots:self.assertEqual((x*x-x-1)%m,0)
        self.assertEqual(roots[0][1],16)
        self.assertNotEqual(roots[1][1],16)
        self.assertEqual(scalar_order(16,239),119)
        self.assertEqual(matrix_order(239),238)

    def test_exact_native_defect_all_seeds(self):
        for seed in (Q(),Q(1,16),Q(2,7)):
            u=states(98,seed)
            for n in range(97):
                d=u[n+2]-u[n+1]-u[n]-239*u[n]
                self.assertEqual(d,15*forcing(n+1)+forcing(n+2))
                self.assertGreater(d,0)
        self.assertEqual(residue(15*forcing(1)+forcing(2),239),198)

    def test_wrong_source_discriminator(self):
        authentic=15*forcing(1)+forcing(2)
        for coeff in ((5,-2,-1,-1),(8,-2,-2,-1)):
            self.assertNotEqual(15*forcing(1,coeff)+forcing(2,coeff),authentic)
            u=states(9,coefficients=coeff)
            for n in range(8):
                self.assertEqual(u[n+2]-u[n+1]-240*u[n],
                    15*forcing(n+1,coeff)+forcing(n+2,coeff))

    def test_first_conductor_birth(self):
        u=states(60)
        self.assertTrue(all(q.denominator%239 for q in u[:60]))
        self.assertEqual(u[60].denominator%239,0)
        self.assertEqual(residue(239*u[60],239),119)

    def test_fibonacci_power_defect(self):
        for k in range(2,81):
            quotient=sum(16**(k-1-j)*fibonacci(j) for j in range(1,k))
            self.assertEqual(16**k-16*fibonacci(k)-fibonacci(k-1),239*quotient)

    def test_zeckendorf_tiles_and_energy_cost(self):
        for n in list(range(1,4097))+[10007,65537,1000003]:
            blocks=zeckendorf(n)
            self.assertEqual(sum(blocks),n)
            self.assertTrue(all(2*b<=a for a,b in zip(blocks,blocks[1:])))
            self.assertTrue(zeckendorf_sqrt_certificate(n))

    def test_density_zero_edit_word_bound(self):
        digits=[(13*i*i+7*i+3)%16 for i in range(20000)]
        changed,positions=overwrite_snapshots(digits)
        for width in (1,2,3,5,8):
            before=word_counts(digits,width); after=word_counts(changed,width)
            differences=[abs(before.get(w,0)-after.get(w,0))
                         for w in set(before)|set(after)]
            self.assertLessEqual(max(differences),width*len(positions))
            self.assertLessEqual(sum(differences),2*width*len(positions))
        for k in range(2,20):
            start=fibonacci(k)
            self.assertTrue(all(v==0 for v in changed[start:start+k*k]))

    def test_golden_lag_decay(self):
        lo,hi=lambda_interval(100)
        self.assertGreater(1-hi,Q(3,8))
        for k in list(range(3,25))+[31,37]:
            a,b=golden_lag_intervals(k)
            self.assertGreater(a,0)
            self.assertLess(b,Q(1,2))
            self.assertLessEqual(a,hi**k)
            self.assertGreaterEqual(b,lo**k)
            self.assertLess(b,hi**k+Q(1,10**70))
        self.assertLess(golden_lag_intervals(37)[1],Q(1,10000000))


if __name__=='__main__':unittest.main()
