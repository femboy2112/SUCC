"""Focused, dependency-free calibrations; never a pi normality test."""
import unittest
from fractions import Fraction as Q
from cut_graph import (Interval, bbp_r, pi_over_16_bounds, sqrt2_bounds,
    affine_oracle, cut_probe, radix_prefix, winding, stern_brocot_prefix,
    FareyBounds, prime_valuations, mobius_quotient, divisors)


class ArithmeticCutTests(unittest.TestCase):
    def test_frozen_four_poles(self):
        self.assertEqual(bbp_r(1), Q(47,15))
        for n in range(1,20):
            a=8*n-7
            self.assertEqual(bbp_r(n), Q(6,a*(a+3))+Q(4,a*(a+4))+Q(5,a*(a+5)))
            self.assertGreater(bbp_r(n), 0)
            self.assertGreater(bbp_r(n), bbp_r(n+1))
        with self.assertRaises(ValueError): bbp_r(True)

    def test_pi_cut_interval_nesting_and_width(self):
        old=pi_over_16_bounds(1)
        self.assertEqual(old.lo, Q(47,240))
        for d in range(2,40):
            new=pi_over_16_bounds(d)
            self.assertGreater(new.lo,old.lo)
            self.assertLess(new.hi,old.hi)
            self.assertLess(new.width,old.width)
            old=new
        self.assertLess(old.width,Q(1,16**37))

    def test_sqrt2_exact_bounds(self):
        for d in range(1,24):
            v=sqrt2_bounds(d)
            self.assertLess(v.lo**2,2)
            self.assertGreater(v.hi**2,2)
            self.assertEqual(v.width,Q(1,2**d))

    def test_rational_cut_probes(self):
        self.assertTrue(cut_probe(pi_over_16_bounds,Q(3,16)))
        self.assertFalse(cut_probe(pi_over_16_bounds,Q(1,5)))
        self.assertTrue(cut_probe(sqrt2_bounds,Q(7,5)))
        self.assertFalse(cut_probe(sqrt2_bounds,Q(3,2)))
        with self.assertRaises(RuntimeError):
            cut_probe(lambda d: Interval(Q(1)-Q(1,2**d),Q(1)+Q(1,2**d)),Q(1),max_depth=5)

    def test_affine_yoneda_naturality(self):
        for a,b in [(Q(16),Q(-3)),(Q(3,2),Q(5,7)),(Q(7,4),Q(-11,13))]:
            q_oracle=affine_oracle(pi_over_16_bounds,a,b)
            for q in [Q(-1),Q(0),Q(1,10),Q(1,3),Q(3),Q(8)]:
                self.assertEqual(cut_probe(q_oracle,q),cut_probe(pi_over_16_bounds,(q-b)/a))
        f=affine_oracle(affine_oracle(pi_over_16_bounds,Q(3,2),Q(1,5)),Q(7,3),Q(-1,8))
        g=affine_oracle(pi_over_16_bounds,Q(7,2),Q(7,15)+Q(-1,8))
        for d in range(1,10): self.assertEqual(f(d),g(d))
        with self.assertRaises(ValueError): affine_oracle(pi_over_16_bounds,Q(0),Q(1))

    def test_hex_prefix_and_carry(self):
        digits=radix_prefix(pi_over_16_bounds,16)
        self.assertEqual(''.join('0123456789ABCDEF'[d] for d in digits),'3243F6A8885A308D')
        for k in (1,2,3,5,8,12,16):
            self.assertEqual(radix_prefix(pi_over_16_bounds,k),digits[:k])
            if k < len(digits):
                self.assertEqual(winding(digits[:k+1]),16*winding(digits[:k])+digits[k])
        with self.assertRaises(ValueError): winding((True,))

    def test_wrong_rational_seed_alias_after_one_step(self):
        base=radix_prefix(pi_over_16_bounds,13)
        shifted=radix_prefix(affine_oracle(pi_over_16_bounds,Q(1),Q(1,16)),13)
        self.assertEqual(shifted[0],base[0]+1)
        self.assertEqual(shifted[1:],base[1:])

    def test_farey_stern_brocot_unimodular(self):
        for oracle in (pi_over_16_bounds,sqrt2_bounds):
            path,state=stern_brocot_prefix(oracle,32)
            self.assertEqual(len(path),32)
            self.assertEqual(state.b*state.c-state.a*state.d,1)
            self.assertIsNotNone(state.finite_width)
            self.assertLess(state.finite_width,Q(1,20))
            if state.d:
                self.assertTrue(cut_probe(oracle,Q(state.a,state.b)))
                self.assertFalse(cut_probe(oracle,Q(state.c,state.d)))
        path,_=stern_brocot_prefix(pi_over_16_bounds,6)
        self.assertEqual(path,'LLLLLR')

    def test_incidence_mobius_convolution(self):
        for n in (12,30,60,180):
            ds=divisors(n)
            for a in ds:
                for b in ds:
                    if b%a: continue
                    s=sum((mobius_quotient(d,b) for d in ds if d%a==0 and b%d==0))
                    self.assertEqual(s,1 if a==b else 0)
        self.assertEqual(prime_valuations(360),{2:3,3:2,5:1})

    def test_finite_probes_alias_distinct_irrationals(self):
        x=affine_oracle(sqrt2_bounds,Q(1,2),Q(0))
        y=affine_oracle(sqrt2_bounds,Q(1,2),Q(1,100))
        probes=[Q(-1),Q(0),Q(1,4),Q(1,2),Q(2,3),Q(3,4),Q(1),Q(2)]
        self.assertEqual([cut_probe(x,q) for q in probes],[cut_probe(y,q) for q in probes])
        self.assertNotEqual(radix_prefix(x,2),radix_prefix(y,2))

if __name__=='__main__':unittest.main()
