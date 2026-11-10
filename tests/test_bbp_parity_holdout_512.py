"""Replay the frozen A=512 original source parity/pressure holdout.

Preregistered BEFORE sample inspection on GitHub as commit 9af9f3d3106d4a05785a7cf51dc94a47781a9ad6.
All numerics are finite. Do not extrapolate to asymptotic pi parity or normality.
"""
import hashlib
import unittest
from collections import Counter
from fractions import Fraction as F

from observational_succ import duck_bbp
from observational_succ.bbp_parity_pressure import original_zero_parity_states, parity_covariance, collision_pressure, parity_projected_haar, prime_coordinate
from observational_succ.haar_successor_junction import source_certified_digits


class Frozen512Replay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.A, cls.p, cls.N = 512,1217,1040
        cls.states=list(original_zero_parity_states(cls.N))
        cls.window=cls.states[cls.A-1:2*cls.A-1]
        cls.ds,_,_=source_certified_digits(cls.A,cls.A+4)

    def test_original_selected_signed_means(self):
        z=parity_covariance(self.window,self.p)
        self.assertEqual(z['prime_mean'],F(-1,128))
        self.assertEqual(z['real_mean'],F(5,128))
        self.assertEqual(z['complement_mean'],F(1,128))
        self.assertEqual(z['signed_covariance'],F(641,16384))
        self.assertEqual(z['tail_correction_count'],0)
        self.assertLessEqual(abs(z['signed_covariance']),F(1,4))

    def test_prime_local_support_and_pressure(self):
        counts=Counter((s.local(self.p),) for s in self.window)
        self.assertEqual(len(counts),76)
        self.assertLessEqual(len(counts),4*38)
        z=collision_pressure(counts,self.p)
        self.assertEqual(z['E'],F(2051009,131072))
        self.assertEqual(z['occupied_bins'],76)
        self.assertEqual(z['effective_volume'],F(131072,1793))
        self.assertLessEqual(self.p/F(4*38)-1,z['E'])

    def test_frozen_hex_and_pressure(self):
        text=''.join(f'{d:X}' for d in self.ds)
        self.assertEqual(len(text),516)
        self.assertEqual(text[:16],'3B3EE1411636FBC2')
        self.assertEqual(hashlib.sha256(text.encode('ascii')).hexdigest(),'de490f103f307780a0cdc92f93a3e11873d26c71cd328d6de9b7a62f932fa58d')
        self.assertEqual(parity_projected_haar(self.ds,self.A)['digit_h8_parity_mean'],F(5,128))
        expected=[(F(231,8192),F(0),F(231,8192),16),
                  (F(235,512),F(0),F(235,512),225),
                  (F(63,8),F(7),F(7,8),484),
                  (F(257,2),F(127),F(3,2),509)]
        for k,(e,floor,excess,occupied) in enumerate(expected,1):
            counts=Counter(tuple(self.ds[i:i+k]) for i in range(self.A))
            z=collision_pressure(counts,16**k)
            self.assertEqual((z['E'],z['finite_floor'],z['excess'],z['occupied_bins']),
                             (e,floor,excess,occupied))

    def test_independent_global_bulk_digit_interval(self):
        lo,hi=duck_bbp.tail_interval(0,self.N)
        for offset,d in enumerate(self.ds):
            n=self.A+offset
            A=lo*16**(n+1); B=hi*16**(n+1)
            low=A.numerator//A.denominator; high=B.numerator//B.denominator
            self.assertEqual(low,high)
            self.assertEqual(d,low%16)

    def test_odd_denominator_p_integral_wrong_seed(self):
        a,p,N=self.A,self.p,self.N
        alpha=F(self.states[N-1].numerator,self.states[N-1].denominator*16**N)
        D=p*16**(2*a+48)+1
        v=alpha*D
        seed=-F(v.numerator//v.denominator,D)
        self.assertEqual(seed.denominator%2,1)
        self.assertNotEqual(seed.denominator%p,0)
        self.assertGreater(seed+alpha,0)
        upper=16**(2*a+7)*(seed+alpha+F(duck_bbp.forcing(N+1),15*16**N))
        self.assertLess(upper,F(1,16))
        for n in (a,a+1,2*a-1):
            s=self.states[n-1]
            true=F(s.numerator,s.denominator)
            mutant=true+16**n*seed
            self.assertEqual(mutant.denominator%2,1)
            self.assertEqual(mutant.numerator%2,n%2)
            self.assertEqual(prime_coordinate(true,p),prime_coordinate(mutant,p))
        mp=parity_covariance(self.window,p)['prime_mean']
        self.assertEqual(1-mp*mp,F(16383,16384))

if __name__=='__main__':unittest.main()
