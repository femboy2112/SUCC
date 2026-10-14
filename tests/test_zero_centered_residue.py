"""Zero-independent exact, independent-oracle controls for residue observers."""
import unittest
from fractions import Fraction as Q
from observational_succ.zero_centered_residue import (
    clock,cell_of,direct_probe,mobius,coefficients,value,arbitrary_target,
    blackout,distance_interval,gram_interval,mellin_cell,fake_cell_delta,receipt,
    ZeroCenteredError)


class ZeroCenteredTests(unittest.TestCase):
    def test_cell_identity_against_literal_fractional_parts(self):
        for k in range(1,35):
            for u in (Q(1,5),Q(1,2),Q(4,5)):
                x=1/(k+u)
                self.assertEqual(cell_of(x),k)
                for n in range(2,14):
                    self.assertEqual(direct_probe(x,n),clock(k,n))

    def test_dirichlet_inverse_and_exact_prefix(self):
        for K in range(2,27):
            mu=mobius(K)
            for k in range(2,K+1):
                self.assertEqual(sum(mu[d] for d in range(1,k+1) if k%d==0),0)
            a=coefficients(K)
            self.assertEqual([value(k,a) for k in range(1,K+1)],[Q(1)]*K)
            self.assertTrue(receipt(K)["all_prefix_cells_exact"])

    def test_arbitrary_finite_target(self):
        for t in ((Q(1),Q(0)),(Q(-1),Q(5),Q(3)),tuple(Q(i*i,3) for i in range(1,19))):
            a=arbitrary_target(t)
            self.assertEqual([value(k,a) for k in range(1,len(t)+1)],list(t))
        self.assertEqual(arbitrary_target((Q(1),)*8),coefficients(8))

    def test_fake_composite_six_rejected(self):
        for K in (6,8,12):
            r=receipt(K,{6:-1})
            self.assertFalse(r["genuine_source"])
            self.assertFalse(r["all_prefix_cells_exact"])
            self.assertEqual(r["first_bad_divisor"],6)
            self.assertEqual(value(6,coefficients(K,{6:-1})),Q(-1))

    def test_lcm_blackout_and_certified_tail(self):
        for K in (2,3,4,6,9,12):
            a=coefficients(K)
            c=blackout(a)
            self.assertEqual(value(c["lcm_cell"],a),0)
            lower,upper=distance_interval(a,512)
            self.assertLessEqual(Q(c["global_squared_error_lower_bound"]),lower)
            self.assertLess(lower,upper)
            self.assertFalse(c["RH_proved"])

    def test_mellin_mutation_and_gram(self):
        self.assertEqual(fake_cell_delta(2,6,Q(1,2)),Q(13,7056))
        for k in range(1,20):
            self.assertEqual(mellin_cell(1,k),Q(1,k*(k+1)))
        for m,n in ((2,2),(2,3),(3,5),(6,7)):
            a,b=gram_interval(m,n,48)
            c,d=gram_interval(m,n,128)
            self.assertLessEqual(a,c)
            self.assertLessEqual(c,b)
            self.assertLessEqual(d,b)

    def test_invalid_inputs(self):
        for fn in (lambda:clock(0,2),lambda:clock(1,1),
                   lambda:cell_of(0.5),lambda:arbitrary_target((Q(1),0.5)),
                   lambda:distance_interval({2:0.5}),
                   lambda:fake_cell_delta(2,6,0.5)):
            with self.assertRaises(ZeroCenteredError):
                fn()


if __name__=="__main__":
    unittest.main()
