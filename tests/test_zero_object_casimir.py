"""Focused tests for zero-cylinder gluing, exact radix-16 Fekete covariance,
and a separate finite Gaussian conditional-field/Casimir analogue.

Requires only Python's standard library. No pi-digit oracle or randomness.
"""
from __future__ import annotations
import unittest, math, cmath, importlib.util
from fractions import Fraction as F
from pathlib import Path

_spec=importlib.util.spec_from_file_location("source_pressure", Path(__file__).resolve().parents[1]/'research/2026-11-05/zero_object_casimir/seed_pressure_probe.py')
mod=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(mod)

def char(x):return cmath.exp(2j*math.pi*float(F(x)%1))

class SourcePressure(unittest.TestCase):
    def test_01_original_source_integrity(self):
        u=mod.original_states(23)
        self.assertEqual(u[1]%1,F(2,15))
        self.assertEqual(u[2]%1,F(1076,4095))
        self.assertEqual(u[3]%1,F(188663,765765))

    def test_02_exact_Bernoulli_covariance_A9(self):
        A=9
        coeff=mod.exact_variance_over_pi2(A)
        self.assertGreater(coeff,0)
        self.assertLessEqual(coeff,mod.variance_constant_bound(A))
        self.assertAlmostEqual(float(coeff)*math.pi**2,0.020382252392099,places=12)

    def test_03_exact_Bernoulli_covariance_A11(self):
        A=11
        coeff=mod.exact_variance_over_pi2(A)
        self.assertGreater(coeff,0)
        self.assertLessEqual(coeff,mod.variance_constant_bound(A))
        self.assertAlmostEqual(float(coeff)*math.pi**2,0.013976187474423,places=12)

    def test_04_unforced_baseline_variance_majorizes_original(self):
        for A in (3,5,9,11):
            U=mod.original_states(2*A-1)
            pairs=mod.epoch_pairs(A,U)
            actual=sum((mod.covariance_coeff(p,q) for p in pairs for q in pairs),F())/A**4
            baseline=sum((F(1,3)*F(math.gcd(p[2],q[2])**2,p[2]*q[2]) for p in pairs for q in pairs),F())/A**4
            self.assertGreaterEqual(baseline,actual)
            self.assertGreater(actual,0)

    def test_05_causal_cylinder_exact_16_roots_one_time(self):
        # s in [0,16^-K) sampled at 16-point midpoint quadrature. For
        # n=K, harmonics |h|<16 have EXACT discrete orthogonality.
        for K in (1,2,3):
            n=K
            u=mod.original_states(n)[n]
            for h in (-2,1,3):
                samples=[char(h*(u+16**n*F(2*j+1,2*16**(K+1)))) for j in range(16)]
                self.assertLess(abs(sum(samples)/16),1e-12)

    def test_06_joint_causal_resonance_is_source_exact(self):
        # 16 U_n - U_(n+1) = -original forcing at n+1
        U=mod.original_states(12)
        for n in (2,3,7,11):
            self.assertEqual(16*U[n]-U[n+1],-mod.forcing(n+1))
            self.assertLess(abs(char(16*U[n]-U[n+1])-char(-mod.forcing(n+1))),1e-12)

    def test_07_backwards_16_preimages_source_selected(self):
        for n in (2,5,11):
            r=mod.forcing(n+1)
            for y in (F(0),F(1,7),F(13,29)):
                roots=[((y-r+j)/16)%1 for j in range(16)]
                self.assertEqual(len(set(roots)),16)
                self.assertTrue(all((16*x+r)%1==y for x in roots))

    def test_08_seed_pressure_period_all_future(self):
        U=mod.original_states(18)
        for A in (2,4,7):
            for n in range(A,2*A):
                self.assertEqual(16**n*F(1,16**A),16**(n-A))
                for s in (F(),F(1,13),F(1,17)):
                    self.assertEqual((U[n]+16**n*(s+F(1,16**A)))%1,
                                     (U[n]+16**n*s)%1)

    def test_09_gaussian_bridge_rational_schur(self):
        for rho,d,k in ((F(2,5),4,1),(F(3,7),7,3),(F(1,2),5,2)):
            var=mod.conditioned_bridge_variance(rho,d,k)
            self.assertTrue(F(0)<var<1-rho**(2*k))
            ratio=1-rho**(2*d)
            self.assertTrue(F(0)<ratio<F(1))

    def test_10_stationary_causal_AR1_can_be_time_reversible(self):
        # Joint zero-mean Gaussian law is invariant under time reversal
        # because its covariance is invariant and Gaussian is determined by it.
        for rho in (F(1,2),F(3,7)):
            d=8
            C=[[rho**abs(i-j) for j in range(d+1)] for i in range(d+1)]
            self.assertEqual(C, [list(reversed(row)) for row in reversed(C)])

    def test_11_real_zero_reference_is_unforced_coherent(self):
        # At exactly s=0, r=0, every finite horizon is a fixed point;
        # but every positive-width zero cylinder has future Haar marginals.
        for A in (3,7,13):
            self.assertEqual(sum(char(16**n*F()) for n in range(A,2*A))/A,1+0j)
            for K in (0,1,2):
                if K<=A:
                    self.assertEqual(16**(A-K)%1,0)

    def test_12_high_resolution_zero_cylinder_recovers_selected_phase(self):
        # Post-prereg theorem test: the future source phases are uniformly close
        # to the EXACT zero seed once K exceeds the last epoch time.
        for A in (3,9,17):
            U=mod.original_states(2*A-1)
            K=2*A+math.ceil(3*math.log(A,16))
            H=16**math.floor(math.log(A*A*math.log(A),16))
            worst=2*math.pi*H*16**(2*A-1-K)
            self.assertLess(worst*math.log(A),.1)
            for s in (F(),F(1,2*16**K),F(15,16**(K+1))):
                for n in range(A,2*A):
                    self.assertLessEqual(16**n*s,F(1,16**(K-2*A+1)))
                    actual=char(H*(U[n]+16**n*s))
                    selected=char(H*U[n])
                    self.assertLessEqual(abs(actual-selected),worst+1e-11)

if __name__=='__main__': unittest.main()
