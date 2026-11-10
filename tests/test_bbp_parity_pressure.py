"""Strict source/provenance and hostile controls for BBP parity/pressure.

The isolated local environment uses a clearly disclosed test-only duck_bbp fixture.
On GitHub the unmodified canonical observational_succ.duck_bbp is imported.
"""
import cmath
import math
import unittest
from collections import Counter
from fractions import Fraction as F
from itertools import product

from observational_succ import duck_bbp
from observational_succ.bbp_parity_pressure import (
    prime_powers, prime_coordinate, original_zero_parity_states,
    parity_covariance, parity_projected_haar, collision_pressure,
    even_residue_local_tv, parity_fourier_l1_upper, odd_denom_shadow,
)
from observational_succ.haar_successor_junction import source_certified_digits


class TestBBPParityPressure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.states = list(original_zero_parity_states(512,tail_depth=12))
        cls.ds, _, cls.rad = source_certified_digits(32, 260)

    def test_four_poles_odd_denominator_mod2(self):
        for n in range(1,513):
            r=duck_bbp.forcing(n)
            explicit=F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
            self.assertEqual(r,explicit)
            self.assertEqual(r.denominator%2,1)
            self.assertEqual(r.numerator%2,n%2)
            z=self.states[n-1]
            self.assertEqual(z.numerator%2,n%2)
            self.assertEqual(z.denominator%2,1)

    def test_first_pi_hex_original_source_offset(self):
        first,_,_=source_certified_digits(1,18)
        self.assertEqual(''.join(f'{d:X}' for d in first),'243F6A8885A308D313')
        self.assertEqual(self.states[0].completed_parity,1) # integer digit 3
        for n in range(1,18):
            self.assertEqual(self.states[n].completed_parity,first[n-1]%2)

    def test_crt_exact_global_winding_and_binary_sign(self):
        for state in self.states:
            q=state.denominator
            self.assertEqual(q,math.prod(m for _,m,_ in state.coordinates))
            self.assertEqual(F(state.remainder,q),sum((F(k,m) for _,m,k in state.coordinates),F(0))-state.winding)
            self.assertEqual(state.completed_parity,(state.numerator//q+state.tail_correction)%2)
            self.assertEqual((-1)**state.completed_parity,state.local_clock_sign*state.winding_sign)

    def test_independent_direct_reduced_orbit(self):
        value=F(0)
        for n in range(1,130):
            value=16*value+duck_bbp.forcing(n)
            z=self.states[n-1]
            self.assertEqual(value,F(z.numerator,z.denominator))
            self.assertEqual(z.remainder*z.denominator//z.denominator,z.remainder)

    def test_first_prime_full_crt_n2(self):
        z=self.states[1]
        self.assertEqual(z.denominator,4095)
        self.assertEqual({p:m for p,m,_ in z.coordinates},{3:9,5:5,7:7,13:13})
        self.assertEqual(z.winding,2)
        self.assertEqual(z.local(5),4)

    def test_factor_and_prime_coordinates(self):
        for m in (3,5,7,9,15,45,105,4095):
            fac=prime_powers(m)
            self.assertEqual(math.prod(fac.values()),m)
        with self.assertRaises(ValueError): prime_powers(0)
        with self.assertRaises(ValueError): prime_coordinate(F(1,9),3)
        self.assertEqual(prime_coordinate(F(4,5),3),0)
        self.assertEqual(prime_coordinate(F(4,5),5),4)

    def test_single_p_balanced_finite_covariance(self):
        expectation={
            (32,73):(F(1,16),F(3,8),F(91,256)),
            (128,313):(F(-5,32),F(-11,64),F(-387,2048)),
            (256,617):(F(3,64),F(1,32),F(61,2048)),
        }
        for (A,p),(mp,mr,cov) in expectation.items():
            z=parity_covariance(self.states[A-1:2*A-1],p)
            self.assertEqual(z['prime_mean'],mp)
            self.assertEqual(z['real_mean'],mr)
            self.assertEqual(z['signed_covariance'],cov)
            self.assertEqual(z['tail_correction_count'],0)

    def test_prime_phase_matches_independent_local_rational(self):
        for p,A in ((73,32),(313,128),(617,256)):
            for z in self.states[A-1:2*A-1]:
                self.assertEqual(z.local(p),prime_coordinate(F(z.numerator,z.denominator),p))
                self.assertTrue(z.denominator%p==0)
                self.assertTrue(z.denominator%(p*p)!=0)

    def test_h8_walsh_projection_versus_continuous_weyl(self):
        first=[2*a for a in range(8)]*8
        z=parity_projected_haar(first,64)
        self.assertEqual(z['digit_h8_parity_mean'],1)
        self.assertEqual(z['projected_successor_energy'],4)
        self.assertEqual(z['full_successor_energy'],4)
        zero=parity_projected_haar(list(range(16))*4,64)
        self.assertEqual(zero['digit_h8_parity_mean'],0)
        self.assertEqual(zero['full_successor_energy'],0)
        x=F(1,32)
        d=int(16*x)
        self.assertEqual((-1)**d,1)
        self.assertNotAlmostEqual(cmath.exp(2j*math.pi*8*float(x)).real,1)

    def test_source_parity_projection(self):
        ds=self.ds
        for N in (32,64,128,256):
            p=parity_projected_haar(ds,N)
            self.assertEqual(4*p['digit_h8_parity_mean']**2,p['projected_successor_energy'])
            self.assertGreaterEqual(p['other_modes_energy'],0)
            self.assertEqual(p['digit_h8_parity_mean'],F(sum((-1)**x for x in ds[:N]),N))

    def test_odd_modulus_parity_fourier_identity(self):
        for p in (3,5,7,11,17,73):
            norm=0
            for h in range(p):
                direct=sum(((-1)**k*cmath.exp(-2j*math.pi*h*k/p) for k in range(p)))/p
                closed=2/(p*(1+cmath.exp(-2j*math.pi*h/p)))
                self.assertAlmostEqual(abs(direct-closed),0,places=10)
                norm+=abs(direct)
            self.assertLessEqual(norm,parity_fourier_l1_upper(p)+1e-9)
            self.assertAlmostEqual(1/p,sum((-1)**k for k in range(p))/p)

    def test_exact_even_residue_marginal_no_go(self):
        Q=3*5*7*11
        even=[b for b in range(Q) if b%2==0]
        self.assertEqual(len(even),(Q+1)//2)
        for m in (3,5,7,11,15,21,35,77):
            counts=Counter(b%m for b in even)
            tv=sum((abs(F(counts.get(a,0),len(even))-F(1,m)) for a in range(m)),F(0))/2
            self.assertEqual(tv,even_residue_local_tv(Q,m))
            if m in (3,5,7,11): self.assertLess(tv,F(1,100))
        with self.assertRaises(ValueError):even_residue_local_tv(10,5)

    def test_sharp_pressure_equation(self):
        for B in (1,2,3,4,16,256):
            for N in range(1,21):
                # deterministic unbalanced histogram, then balanced control
                h={i:(N//B + (i<N%B)) for i in range(B) if (N//B + (i<N%B))>0}
                z=collision_pressure(h,B)
                self.assertEqual(z['E'],z['finite_floor'])
                self.assertEqual(z['excess'],0)
                alt={0:N}
                zz=collision_pressure(alt,B)
                self.assertGreaterEqual(zz['E'],z['E'])
                self.assertEqual(zz['E'],B-1)
                self.assertEqual(zz['effective_volume'],1)

    def test_pressure_on_source_digits(self):
        for N in (32,64,128,256):
            prev=F(0)
            for depth in (1,2,3,4):
                counts=Counter(tuple(self.ds[i:i+depth]) for i in range(N))
                z=collision_pressure(counts,16**depth)
                self.assertEqual(z['E'],F(16**depth*sum(c*c for c in counts.values()),N*N)-1)
                self.assertGreaterEqual(z['E'],prev)
                self.assertEqual(z['E'],z['finite_floor']+z['excess'])
                prev=z['E']

    def test_pressure_sparse_resolution_not_randomness(self):
        # Any N distinct bins, independent of whether they arise from normal digits.
        for N in (8,16,32,64):
            B=N*N
            z=collision_pressure({(i,):1 for i in range(N)},B)
            self.assertEqual(z['E'],N-1)
            self.assertEqual(z['excess'],0)
            self.assertEqual(z['occupied_bins'],N)

    def test_nonzero_rational_odd_denom_shadow(self):
        for A,p in ((8,17),(16,41),(32,73)):
            s,bound=odd_denom_shadow(A,p)
            self.assertNotEqual(s,0)
            self.assertEqual(s.denominator%2,1)
            self.assertNotEqual(s.denominator%p,0)
            self.assertLess(bound,F(1,16))
            self.assertEqual(bound>0,True)
            value_original=F(0);value_shadow=s
            for n in range(1,2*A+8):
                r=duck_bbp.forcing(n)
                value_original=16*value_original+r
                value_shadow=16*value_shadow+r
                self.assertEqual(value_shadow.denominator%2,1)
                self.assertEqual(value_shadow.numerator%2,n%2)
                if n>=A:
                    self.assertEqual(prime_coordinate(value_shadow,p),prime_coordinate(value_original,p))

    def test_local_prime_mean_does_not_force_real_mean(self):
        # In a conditional local-uniform ensemble the global representative
        # parity can still be identically +1.
        Q=3*5*7*11*13
        for m in (3,5,7,11,13):
            self.assertLess(even_residue_local_tv(Q,m),F(1,1000))
        all_even=range(0,Q,2)
        self.assertTrue(all(b%2==0 for b in all_even))

    def test_wrong_seed_does_not_preserve_original_zero(self):
        s,_=odd_denom_shadow(16,41)
        self.assertNotEqual(s,0)
        self.assertGreater(abs(s),F(1,10))
        self.assertLess(abs(s),F(1,4))

if __name__=='__main__':unittest.main()
