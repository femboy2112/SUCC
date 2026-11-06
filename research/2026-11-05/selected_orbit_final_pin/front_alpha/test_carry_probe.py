import unittest
from fractions import Fraction as Q
import carry_probe as p


class CarryCorrectionTests(unittest.TestCase):
    def test_independent_source_and_lift_paths(self):
        for seed in (Q(),Q(1,5),Q(-7,11)):
            U,x,c=p.orbit(80,seed)
            for n in range(1,81):
                self.assertEqual(p.source(n),p.source_polynomial(n))
                self.assertEqual(U[n],16*U[n-1]+p.source(n))
                self.assertEqual(x[n],U[n]%1)
                if n>=2:
                    self.assertLessEqual(p.source(n),p.C/Q(n*n))

    def test_adversarial_correction_reset_and_spacing(self):
        # Select rational seed to place x_A just below a macro boundary.
        # It forces a correction; no random sampling or approximate phase.
        for A,m in ((20,1),(40,2),(125,3)):
            U,_,_=p.orbit(A)
            B=16**m; R=p.source_block(A,m)
            desired=(1-R/2)/B
            seed=(desired-U[A])/16**A
            lift,x,c=p.orbit(2*A+m,seed)
            row=p.exact_row(lift,x,c,A,m)
            self.assertIn(A,row['correction_indices'])
            self.assertLess(x[A+m],R)

    def test_interval_tail_nesting_and_recurrence(self):
        for n in (0,1,37,257):
            lo,hi=p.tail_interval(n,12)
            lo2,hi2=p.tail_interval(n,24)
            self.assertLess(lo,lo2);self.assertLess(hi2,hi)
            nextlo,nexthi=p.tail_interval(n+1,24)
            self.assertLessEqual(16*lo2-p.source(n+1),nexthi)
            self.assertGreaterEqual(16*hi2-p.source(n+1),nextlo)

    def test_coherent_zero_corrections_high_pressure(self):
        for m in (1,2,3):
            row=p.interval_row(125,m,Q())
            self.assertEqual(row['correction_indices'],[])
            self.assertEqual(Q(row['cell_pressure']),16**m)

    def test_periodic_completions_and_domain(self):
        beta=p.periodic_completion(11)
        self.assertEqual((16**11*beta-beta).denominator,1)
        self.assertFalse(p.bound(1,3)['applicable'])
        self.assertTrue(p.bound(125,3)['applicable'])
        self.assertEqual(p.bound(125,3)['L'],1)

    def test_pressure_bound_on_actual_source(self):
        U,x,c=p.orbit(259)
        for A in (37,125):
            for m in (1,2,3):
                row=p.exact_row(U,x,c,A,m)
                self.assertLessEqual(abs(Q(row['cell_pressure'])-Q(row['carry_pressure'])),
                                     Q(row['pressure_difference_bound']))


if __name__=='__main__':unittest.main()
