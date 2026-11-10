"""Exact source/support checks with an independent four-pole oracle."""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd
import importlib.util
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[3]))

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

ts=load('covforge_terminal_support_test',HERE/'terminal_support.py')
oracle=load('covforge_terminal_oracle_test',HERE/'independent_oracle.py')


class TerminalSupportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w=ts.construct(5,37,37,73,Q(1,8),(3,5,7,137))

    def test_independent_source_and_modular_avoidance(self):
        result=oracle.check(self.w)
        self.assertEqual(result['independent_source_states'],74)
        self.assertGreater(result['blocked_candidates'],0)

    def test_terminal_denominator_and_all_finite_observations(self):
        result=ts.verify(self.w)
        self.assertGreater(result['signed_lower'][5],Q(999999,1000000))
        self.assertEqual(self.w['shadow'][-1].denominator,self.w['original'][-1].denominator)

    def test_full_chronological_authentication_rejects(self):
        w=self.w
        self.assertEqual(w['original'][0],0)
        self.assertGreater(w['shadow'][0],0)
        self.assertGreater(w['seed'].denominator,1)
        p=next(p for p in w['used_primes'] if w['seed'].denominator%p==0)
        self.assertNotEqual(ts.prior.principal(w['shadow'][0],p),0)
        self.assertEqual(ts.prior.principal(w['original'][0],p),0)

    def test_forbidden_candidate_loses_terminal_denominator(self):
        w=self.w
        a,d=w['original'][-1].numerator,w['original'][-1].denominator
        scale=16**w['B']*2**w['K']*(d//w['q'])
        p=w['used_primes'][0]
        forbidden=(-a*pow(scale,-1,p))%p
        self.assertGreater(gcd(a+scale*forbidden,d),1)
        bad=w['original'][-1]+16**w['B']*Q(2**w['K']*forbidden,w['q'])
        self.assertLess(bad.denominator,d)

    def test_excess_precision_fails_without_new_prime(self):
        with self.assertRaisesRegex(ValueError,'insufficient seed precision'):
            ts.construct(5,37,37,self.w['precision_capacity']+1,Q(1,8),(3,5,7,137))

    def test_omitted_selected_prime_is_not_automatically_preserved(self):
        w=ts.construct(5,37,37,73,Q(1,8),(3,5,7))
        self.assertIn(137,w['used_primes'])
        self.assertNotEqual(ts.prior.principal(w['seed'],137),0)

    def test_capacity_is_exact_at_boundary(self):
        w=self.w
        k=w['precision_capacity']
        self.assertLessEqual((w['t']+1)*2**k*16**w['B'],w['eta']*w['q'])
        self.assertGreater((w['t']+1)*2**(k+1)*16**w['B'],w['eta']*w['q'])

    def test_nonexact_and_nonprime_inputs_fail_closed(self):
        for bad in [(1,), (2,), (9,), (3,3), (3.0,), (True,)]:
            with self.subTest(primes=bad),self.assertRaises((ValueError,TypeError)):
                ts.construct(5,37,37,73,Q(1,8),bad)
        for J,A,L,K,eta in [(True,37,37,73,Q(1,8)),(5,37.0,37,73,Q(1,8)),
                              (37,37,37,73,Q(1,8)),(5,37,0,73,Q(1,8)),
                              (5,37,37,-1,Q(1,8)),(5,37,37,73,0.125)]:
            with self.subTest(args=(J,A,L,K,eta)),self.assertRaises((ValueError,TypeError)):
                ts.construct(J,A,L,K,eta,(3,5,7,137))
        with self.assertRaises((ValueError,TypeError)):
            ts.precision_capacity(100,1,1,0.125)

    def test_elementary_linear_prefix_memory(self):
        A=37
        w=ts.construct((A-1)//5,A,A,2*A-1,Q(1,8),(3,5,7,137))
        ts.verify(w)
        self.assertLess(w['seed'],Q(1,16**(5*w['J'])))


if __name__=='__main__':
    unittest.main()
