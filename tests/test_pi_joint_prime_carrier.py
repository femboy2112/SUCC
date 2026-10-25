"""Exact controls for joint-prime, source-attached BBP representation.

Finite tests establish code-level identities, never an asymptotic π theorem.
"""
from __future__ import annotations

import cmath
from fractions import Fraction as Q
from math import comb, pi
import unittest

from observational_succ.pi_joint_prime_carrier import (
    forcing, forcing_odd, states, denominator_primes, primes_through,
    local_primary, joint_primary, joint_circle, primary_window_phase,
    dyadic_integral, source_prime_bound, source_torsion,
    pascal_difference, local_pascal_difference, known_tail_upper,
    floor_hex_digit, certified_hex_digit, conditional_squared_residual,
    four_gate_interaction, six_phase_control, correlated_six_phase_control,
    hidden_prime_halfway, height_unique_threshold, common_bbp_denominator,
)
from observational_succ.pascal_lucas_quotient import lucas_unit


class JointPrimeSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.values = states(257)

    def test_original_four_poles_equal_odd_form(self):
        for n in range(1,257):
            self.assertEqual(forcing(n), forcing_odd(n))
            self.assertEqual(forcing(n).denominator % 2, 1)
            self.assertTrue(0 < forcing(n) < 5)
            self.assertEqual(self.values[n], 16*self.values[n-1] + forcing(n))
            self.assertEqual(self.values[n].denominator % 2, 1)
            self.assertTrue(0 < self.values[n] < 16**n)

    def test_prime_primary_reconstruction_independent_direct_integer_remainder(self):
        samples=[Q(0),Q(1),Q(-7,12),Q(13,35),Q(1,6),Q(1,2),Q(5,6)]
        for b in range(1,43):
            for a in range(-2*b,2*b+1,7):
                samples.append(Q(a,b))
        for x in samples:
            components=joint_primary(x)
            self.assertEqual(sum((v for _,v in components),Q())%1,x%1)
            self.assertEqual(joint_circle(x), x%1)
            self.assertEqual(len(set(p for p,_ in components)),len(components))
            for p,part in components:
                self.assertEqual(part,local_primary(x,p))
                self.assertTrue(0<=part<1)
                self.assertEqual(part.denominator & (part.denominator-1)==0,p==2)

    def test_authentic_moving_odd_prime_horizon(self):
        for n,x in enumerate(self.values):
            parts=source_torsion(n,self.values)
            self.assertTrue(all(p%2 and p<=source_prime_bound(n) for p,_ in parts))
            self.assertEqual(sum((c for _,c in parts),Q())%1,x%1)
            self.assertEqual(local_primary(x,2),0)
            self.assertEqual(joint_circle(x,primes_through(source_prime_bound(n))),x%1)

    def test_odd_torsion_recurrence_with_authentic_innovations(self):
        ps=(2,3,5,7,11,13,17,23,31,41,97,157)
        for p in ps:
            self.assertEqual(local_primary(self.values[0],p),0)
            for n in range(1,115):
                expected=(16*local_primary(self.values[n-1],p)+local_primary(forcing(n),p))%1
                self.assertEqual(local_primary(self.values[n],p),expected)

    def test_pascal_integer_rows_commute_with_full_prime_torsion(self):
        ps=(2,3,5,7,11,13,17,31)
        for k in range(0,29):
            delta=pascal_difference(self.values,k)
            for p in ps:
                self.assertEqual(local_primary(delta,p),local_pascal_difference(self.values,k,p))
                self.assertEqual(local_primary(delta,p),
                    sum(((-1)**(k-j)*comb(k,j)*local_primary(self.values[j],p)
                         for j in range(k+1)),Q())%1)

    def test_dyadic_integral_not_torsion_and_full_residue_bijections(self):
        self.assertEqual(local_primary(self.values[1],2),0)
        self.assertNotEqual(dyadic_integral(self.values[1],8),0)
        for k in range(1,9):
            residues=[dyadic_integral(self.values[n],k) for n in range(2**k)]
            self.assertEqual(sorted(residues),list(range(2**k)))
        # Exact finite replay of inherited p=2 isometry (not a new proof):
        for m in range(1,47):
            for n in range(m):
                a=m-n
                b=dyadic_integral(self.values[m]-self.values[n],9)
                self.assertEqual((a & -a),(b & -b) if b else 2**9)

    def test_source_rational_phase_characters_exact(self):
        for n in range(1,128):
            x=self.values[n]
            comps=source_torsion(n,self.values)
            for h in (-11,-3,-1,1,2,5,17):
                self.assertEqual((h*sum((c for _,c in comps),Q()))%1,(h*x)%1)

    def test_two_prime_joint_synergy_positive_full_factorial(self):
        source=six_phase_control()
        self.assertEqual(len(set(source)),6)
        e0=conditional_squared_residual(source,())
        ep=conditional_squared_residual(source,(2,))
        eq=conditional_squared_residual(source,(3,))
        epq=conditional_squared_residual(source,(2,3))
        self.assertEqual((e0,ep,eq,epq),(Q(5,36),Q(1,9),Q(1,12),Q(0)))
        self.assertEqual(four_gate_interaction(source,2,3),Q(1,18))
        self.assertGreater(ep,epq)
        self.assertGreater(eq,epq)

    def test_correlated_marginals_not_product_of_marginals(self):
        source=correlated_six_phase_control()
        p2=[local_primary(x,2) for x in source]
        p3=[local_primary(x,3) for x in source]
        self.assertEqual((p2.count(Q(0)),p2.count(Q(1,2))),(3,3))
        self.assertEqual((p3.count(Q(0)),p3.count(Q(1,3)),p3.count(Q(2,3))),(2,2,2))
        # Sum X2=0, sum X3=0. But sum X2*X3=(2-2*omega^2)/6 !=0.
        omega=cmath.exp(2j*pi/3)
        char=lambda x: cmath.exp(2j*pi*float(x))
        self.assertAlmostEqual(abs(sum(map(char,p2)))/6,0,places=12)
        self.assertAlmostEqual(abs(sum(map(char,p3)))/6,0,places=12)
        e=sum(char(x) for x in source)/6
        self.assertAlmostEqual(abs(e-(1-omega**2)/3),0,places=12)
        self.assertAlmostEqual(abs(e)**2,Q(1,3).__float__(),places=12)

    def test_all_fixed_prime_torsion_views_can_miss_half_real_phase(self):
        fixed=primes_through(19)
        for q in (23,31,101,1009):
            x=hidden_prime_halfway(q)
            self.assertTrue(all(local_primary(x,p)==0 for p in fixed))
            self.assertEqual(joint_primary(x),((q,x),))
            self.assertEqual(Q(1,2)-x,Q(1,2*q))
            self.assertGreater(x,Q(2,5))
        self.assertEqual(primary_window_phase(hidden_prime_halfway(1009),fixed),0)

    def test_all_primary_torsion_cannot_supply_missing_integer_lift(self):
        x=self.values[1]
        y=x+1
        self.assertEqual(joint_primary(x),joint_primary(y))
        self.assertEqual(x%1,y%1)
        self.assertNotEqual((x/5)%1,(y/5)%1)
        self.assertEqual(((y/5)-(x/5))%1,Q(1,5))
        self.assertEqual((dyadic_integral(y,8)-dyadic_integral(x,8))%256,1)

    def test_residue_lucas_support_not_integer_coefficient(self):
        self.assertTrue(lucas_unit(3,2,1))
        self.assertEqual(comb(2,1)%3,2)
        self.assertNotEqual(comb(2,1)%3,int(lucas_unit(3,2,1)))
        # Coefficient mod 3 times 1/3 fails any p-adic O(p) estimate.
        x=Q(1,3)
        actual=comb(3,1)*x
        lifted=(comb(3,1)%3)*x
        self.assertEqual(actual-lifted,1)
        self.assertNotEqual((actual-lifted).numerator%3,0)

    def test_rational_reconstruction_height_gate(self):
        for b in range(1,19):
            for radius in range(1,5):
                threshold=height_unique_threshold(b,radius)
                M=threshold+1
                for numerator in range(-threshold,threshold+1):
                    if numerator % M == 0:
                        self.assertEqual(numerator,0)
        for N in (2,5,12,24,40):
            b=common_bbp_denominator(N)
            self.assertTrue(all((b*x).denominator==1 for x in self.values[:N]))
            self.assertTrue(all(abs(x)<16**N for x in self.values[:N]))
            self.assertGreater(height_unique_threshold(b,16**N),b)

    def test_exact_positive_tail_digit_certification(self):
        # True interval-gate certificate uses rational BBP kernel 0<T_n<bound.
        certified={}
        for n,x in enumerate(self.values):
            digit=certified_hex_digit(n,x)
            if digit is None:
                self.assertEqual(n,0)
            else:
                self.assertEqual(digit,floor_hex_digit(x))
                self.assertLess(known_tail_upper(n),Q(1,2))
                certified[n]=digit
        self.assertEqual(len(certified),256)
        self.assertEqual(sum(1 for n in range(1,257) if certified[n]==0),17)

    def test_numeric_machin_pi_oracle_is_separate_noncertifying_control(self):
        try:
            import mpmath as mp
        except ImportError:
            self.skipTest('mpmath optional oracle absent')
        with mp.workdps(190):
            alpha=mp.pi/16
            for n in range(1,75):
                x=self.values[n]
                actual=mp.frac(alpha*16**n)
                approx=mp.mpf(x.numerator)/x.denominator
                correction=alpha*16**n-approx
                eps=known_tail_upper(n)
                self.assertGreater(correction,0)
                self.assertLess(correction,mp.mpf(eps.numerator)/eps.denominator)
                self.assertEqual(int(mp.floor(16*actual)),certified_hex_digit(n,x))

    def test_source_sample_joint_probe_is_overfit_not_certification(self):
        sample=self.values[1:151]
        self.assertEqual(conditional_squared_residual(sample,(2,)),
                         conditional_squared_residual(sample,()))
        self.assertGreater(conditional_squared_residual(sample,(3,)),0)
        self.assertEqual(conditional_squared_residual(sample,(3,5)),0)
        # This source-specific finite data fit has a trivial index memorization
        # explanation. Verify that many later (3,5) signatures were unseen.
        seen={tuple(local_primary(x,p) for p in (3,5)) for x in self.values[1:71]}
        fresh=sum(tuple(local_primary(x,p) for p in (3,5)) not in seen
                  for x in self.values[71:151])
        self.assertGreater(fresh,40)

    def test_strict_domain_rejections(self):
        bad=[lambda: forcing(0),lambda:states(0),lambda:local_primary(0,1),
             lambda:joint_primary(0.25),lambda:dyadic_integral(Q(1,2),3),
             lambda:primes_through(-2),lambda:source_prime_bound(-1),
             lambda:pascal_difference([1],2),lambda:conditional_squared_residual([], (3,)),
             lambda:conditional_squared_residual([Q(0)],(4,)),
             lambda:certified_hex_digit(-1,0),lambda:hidden_prime_halfway(2)]
        for f in bad:
            with self.subTest(call=str(f)):
                with self.assertRaises(ValueError):f()

if __name__=='__main__':
    unittest.main()
