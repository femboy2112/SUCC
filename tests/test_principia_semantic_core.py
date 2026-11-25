import unittest
from dataclasses import replace
from fractions import Fraction
from observational_succ.principia_semantic_core import (
    Edge, InvalidCertificate, make_cycle, verify_cycle,
    compile_null_height, verify_null_height, evaluate, multiply
)

class PathTests(unittest.TestCase):
    def test_affine_source_cycles(self):
        for n in (1, 2, 7):
            for p in (2, 3, 5, 7):
                with self.subTest(n=n,p=p):
                    boundary, response = verify_cycle(make_cycle(n,p))
                    self.assertEqual(boundary, 0)
                    self.assertLess(response, 0)
    def test_fake_composite_rejected(self):
        with self.assertRaises(InvalidCertificate): make_cycle(1, 6)
    def test_wrong_label_and_edge_rejected(self):
        c=make_cycle(2,3)
        with self.assertRaises(InvalidCertificate): verify_cycle(replace(c, source="fake"))
        with self.assertRaises(InvalidCertificate): verify_cycle(replace(c,via_prime=(Edge("S",2,3),)+c.via_prime[1:]))
    def test_distinct_zero_paths_not_falsely_exact(self):
        _,response=verify_cycle(make_cycle(1,2))
        self.assertEqual(response,-4)

class NullHeightTests(unittest.TestCase):
    def base(self, p=3, k=1, d=2, radix=16):
        f=(0,p**k)
        for j in range(1,d+1): f=multiply(f,(-1,radix**j))
        return f
    def test_exact_rigorous_cases(self):
        for p,k,d in ((2,0,0),(3,1,2),(2,3,3),(5,2,4)):
            with self.subTest(p=p,k=k,d=d):
                f=self.base(p,k,d)
                c=compile_null_height(f,depth=d,prime=p,valuation=k)
                v=verify_null_height(c)
                self.assertEqual(v["capacity_lower_bound"],p**k*16**(d*(d+1)//2))
                self.assertEqual(v["leading_abs"],v["capacity_lower_bound"])
                self.assertGreaterEqual(v["l1_norm"],v["leading_abs"])
    def test_nonconstant_quotient(self):
        f=multiply(self.base(d=2),(-2,7))
        c=compile_null_height(f,depth=2,prime=3,valuation=1)
        v=verify_null_height(c)
        self.assertEqual(v["remaining_degree"],1)
        self.assertEqual(v["leading_abs"],7*v["capacity_lower_bound"])
    def test_null_roots_explicit(self):
        f=self.base(d=3)
        self.assertEqual(evaluate(f,Fraction(0)),0)
        for j in range(1,4):self.assertEqual(evaluate(f,Fraction(1,16**j)),0)
    def test_zero_is_not_nonzero_witness(self):
        with self.assertRaises(InvalidCertificate):compile_null_height((0,),depth=2,prime=3,valuation=1)
    def test_false_local_valuation_rejected(self):
        with self.assertRaises(InvalidCertificate):compile_null_height(self.base(d=2),depth=2,prime=3,valuation=2)
    def test_missing_root_rejected(self):
        with self.assertRaises(InvalidCertificate):compile_null_height(self.base(d=1),depth=2,prime=3,valuation=1)
    def test_forged_step_rejected(self):
        c=compile_null_height(self.base(),depth=2,prime=3,valuation=1)
        s=list(c.stages);s[2]=(-1,2)
        with self.assertRaises(InvalidCertificate):verify_null_height(replace(c,stages=tuple(s)))
    def test_changed_source_passport_rejected(self):
        c=compile_null_height(self.base(),depth=2,prime=3,valuation=1)
        with self.assertRaises(InvalidCertificate):verify_null_height(replace(c,source="BBP-authentic"))
    def test_composite_prime_rejected(self):
        with self.assertRaises(InvalidCertificate):compile_null_height(self.base(2,0,1),depth=1,prime=4,valuation=0)
    def test_noninteger_source_rejected(self):
        c=compile_null_height(self.base(),depth=2,prime=3,valuation=1)
        with self.assertRaises(InvalidCertificate):verify_null_height(replace(c,coeffs=(0, Fraction(1,2), 4, 6)))
    def test_duplicated_root_has_no_new_depth(self):
        c=compile_null_height(self.base(d=1),depth=1,prime=3,valuation=1)
        self.assertEqual(verify_null_height(c)["independent_null_roots"],2)
        with self.assertRaises(InvalidCertificate):compile_null_height(self.base(d=1),depth=2,prime=3,valuation=1)

if __name__=="__main__":unittest.main()
