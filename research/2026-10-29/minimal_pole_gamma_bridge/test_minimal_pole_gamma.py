"""Research only; full declared-grammar exact tests; no π normality claim."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import minimal_pole_gamma as p
from fractions import Fraction as F
import unittest

class PoleRigidityTests(unittest.TestCase):
    def test_original_four_poles_are_retained(self):
        self.assertEqual(p.numerator_coefficients(),(15,121,240))
        self.assertEqual(p.R(1),F(47,15))
        for n in range(1,50):
            a=p.native_a(n)
            self.assertEqual(p.R(a),F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5))

    def test_positive_source_for_all_declared_weights(self):
        for m in range(2,9):
            for d in range(1,m):
                for pp,qq,rr in ((2,1,1),(3,2,1),(2,2,1),(6,4,1)):
                    for a in (F(1,3),F(1),F(5),F(93)):
                        self.assertGreater(p.positive_source(a,m,d,pp,qq,rr),0)

    def test_numerator_quadratic_exact_independent_values(self):
        for m,d,pp,qq,rr in ((4,1,2,1,1),(6,2,2,1,1),(5,1,2,2,1),(3,1,3,2,1),(7,2,5,4,2)):
            u,v,w=m-d,m,m+d
            S,L,C=p.numerator_coefficients(m,d,pp,qq,rr)
            self.assertEqual(S,pp*u+qq*v+rr*w)
            self.assertEqual(C,(pp+qq+rr)*u*v*w)
            for a in (1,2,5,11,37):
                value=p.positive_source(a,m,d,pp,qq,rr)
                self.assertEqual(value*F(a*(a+u)*(a+v)*(a+w)),S*a*a+L*a+C)

    def test_minimal_integer_weight_rigidity(self):
        self.assertEqual(p.minimal_weight_solution(),[(4,2,1,1,F(4))])
        for W in range(3,11):
            for pp in range(1,W-1):
                for qq in range(1,W-pp):
                    rr=W-pp-qq
                    if pp<=rr:continue
                    center=F(W,pp-rr)
                    if center<=1:continue
                    # For primitive gap d=1, m=center if integral.
                    if center.denominator==1:
                        m=int(center)
                        self.assertEqual(p.self_dual_residual(m,1,pp,qq,rr),0)
                        self.assertEqual(p.numerator_root_product(m,1,pp,qq,rr),m*m)
                        if W==4:self.assertEqual((pp,qq,rr,m),(2,1,1,4))
        self.assertEqual(p.self_dual_residual(4,1,2,1,1),0)

    def test_scale_equivariance_and_minimal_unit(self):
        for d in range(1,8):
            self.assertEqual(p.numerator_root_product(4*d,d),16*d*d)
            self.assertEqual(p.self_dual_residual(4*d,d),0)
            for a in (F(1),F(3,2),F(100)):
                self.assertEqual(p.positive_source(a,4*d,d),p.R(F(a,d))/d)

    def test_nonminimal_selfdual_and_perturbations(self):
        self.assertEqual(p.self_dual_residual(5,1,2,2,1),0)
        self.assertEqual(p.self_dual_residual(3,1,3,2,1),0)
        self.assertEqual(p.self_dual_residual(2,1,4,1,1),0)
        for case in ((4,1,2,2,1),(5,1,2,1,1),(4,2,2,1,1)):
            self.assertNotEqual(p.self_dual_residual(*case),0)
        for bad in ((1,1,2,1,1),(2,0,2,1,1),(2,1,1,0,1),(2,1,1,1,0)):
            with self.assertRaises(ValueError): p.weights_and_poles(*bad)

    def test_original_roots_real_and_product_16(self):
        S,L,C=p.numerator_coefficients()
        self.assertEqual(L*L-4*S*C,241)
        self.assertEqual(F(C,S),16)
        self.assertEqual(p.numerator_root_product(5,1,2,2,1),25)

class GammaClockTests(unittest.TestCase):
    def test_reciprocal_discrepancy_and_first_crossing(self):
        self.assertEqual(p.inversion_ratio(4),1)
        self.assertEqual(p.native_ratio(1),F(128,133))
        self.assertEqual(p.native_ratio(2),F(2688,2623))
        for a in (F(1,16),F(1),F(2),F(4),F(9),F(16),F(64),F(1024)):
            self.assertEqual(p.inversion_ratio(a)*p.inversion_ratio(F(16,a)),1)
            self.assertEqual(p.inversion_ratio(a)-1,
                             F(a*a-16,(3*a+16)*(5*a+16)))

    def test_prime_channel_exact_factorization(self):
        for n in range(1,1001):
            x,y=p.native_log_gap_factors(n)
            self.assertEqual(x,F(24*n-5,24*n-6))
            self.assertEqual(y,F(40*n-19,40*n-20))
            self.assertEqual(x*y,F(16,15)/p.native_ratio(n))
            self.assertEqual(p.normalized_native_inversion(n)*x*y,1)
            self.assertLess(p.normalized_native_inversion(n),1)

    def test_native_series_inversion_crossing_not_stepwise(self):
        for n in range(1,100):
            self.assertEqual(p.native_a(n)%8,1)
            self.assertNotEqual(F(16,p.native_a(n))%8,1)
        # Only a=1 among native values divides 16; the paired 16 is not native.
        native_divisors=[n for n in range(1,100) if 16%p.native_a(n)==0]
        self.assertEqual(native_divisors,[1])

    def test_product_is_exact_gamma_rising_factorial(self):
        for N in range(0,90):
            self.assertEqual(p.gamma_product_exact(N),p.gamma_product_closed_finite(N))
        for N in range(0,60):
            self.assertEqual(p.gamma_product_exact(N+1)/p.gamma_product_exact(N),
                             p.normalized_native_inversion(N+1))

    def test_atanh_bound_is_a_certified_log_enclosure(self):
        for N in (1,2,3,10,100,1000):
            lo,hi=p.native_log_gap_bounds(N,3)
            self.assertLess(lo,hi)
            self.assertLess(F(1,15*N),lo)
            self.assertLess(hi,F(1,15*N)+F(7,180*N*N))
        for n in (1,2,3,19):
            l3,u3=p.native_log_gap_bounds(n,3)
            l5,u5=p.native_log_gap_bounds(n,5)
            self.assertLess(l3,l5)
            self.assertLess(u5,u3)

    def test_finite_part_intervals_and_convergence(self):
        l32,u32=p.harmonic_finite_part_interval(32,4)
        l128,u128=p.harmonic_finite_part_interval(128,4)
        self.assertLess(F(0),l32)
        self.assertLess(l32,l128)
        self.assertLess(u128,u32)
        self.assertLess(u128-l128,F(7,180*128)+F(1,10**10))
        self.assertLess(u128,F(7,180)*F(2)) # simple valid zeta2<2

    def test_scalar_reweighting_no_saving(self):
        # The exact ratio is positive, tends to 1, and cannot force all signed sequences to cancel.
        for N in (1,2,5,20,100):
            weighted=sum((p.normalized_native_inversion(n) for n in range(1,N+1)),F())
            deficit=F(N)-weighted
            self.assertGreater(deficit,0)
            self.assertLess(deficit,F(1,15)*p.harmonic(N)+F(7,90))
            # For coherent constant phase z_n=1 the average is >0, and tends to 1.
            self.assertGreater(weighted,0)

    def test_seed_shift_does_not_change_source(self):
        u=p.zero_seed_history(23)
        self.assertEqual(u[0],0)
        self.assertEqual(u[1],F(47,15))
        for seed in (F(-1),F(-16),F(1,15),F(1,2),F(-1,8)):
            v=seed
            for n in range(1,24):
                v=16*v+p.original_bbp_forcing(n)
                self.assertEqual(v-u[n],16**n*seed)
        self.assertEqual(u[2]%1,F(1076,4095))

    def test_invalid_inputs(self):
        for v in (0,-1):
            with self.assertRaises(ValueError):p.native_a(v)
            with self.assertRaises(ValueError):p.native_log_gap_factors(v)
            with self.assertRaises(ValueError):p.R(v)
        with self.assertRaises(ValueError):p.gamma_product_exact(-1)
        with self.assertRaises(ValueError):p.harmonic_finite_part_interval(0)
        with self.assertRaises(ValueError):p.atanh_log_one_plus_bounds(0)
        with self.assertRaises(ValueError):p.atanh_log_one_plus_bounds(1,0)

if __name__=='__main__':unittest.main(verbosity=2)
