"""Research-only finite tests for the global-prior Fejer theorem interface.

All trigonometric checks are floating probes; no normality proof or
interval certificate is claimed by this test module.
"""
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

_MODULE = (Path(__file__).resolve().parents[1] / "research" / "2026-11-02"
           / "global_prior_fejer" / "global_prior_fejer.py")
_SPEC = importlib.util.spec_from_file_location("succ_global_prior_fejer", _MODULE)
f = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(f)


class GlobalPriorFejerTests(unittest.TestCase):
    def test_original_four_signed_poles(self):
        for n in range(1,151):
            a = f.original_r(n)
            b = Fraction(120*n*n-89*n+16,
                         (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(a,b)
            self.assertGreater(a,0)

    def test_original_zero_seed_and_finite_seam(self):
        u = Fraction(0)
        for b in range(1,65):
            u = 16*u+f.original_r(b)
            self.assertEqual(u,16**b*f.alpha_cutoff(b))
        def R(x,y):
            return sum((f.original_r(j)/16**(j-x)
                        for j in range(x+1,y+1)),Fraction(0))
        for n,m,b in [(0,3,10),(2,5,12),(3,3,17),(1,7,18)]:
            self.assertEqual(R(n,b),R(n,m)+R(m,b)/16**(m-n))
            self.assertEqual(16**n*f.alpha_cutoff(b)-R(n,b),
                             16**n*f.alpha_cutoff(n))

    def test_exact_rational_gamma_energy_error(self):
        for n,h,b in [(4,2,4),(8,4,12),(32,5,32),
                      (64,8,72),(128,11,128)]:
            cap=f.finite_completion_error_bound(n,h,b)
            self.assertIsInstance(cap,Fraction)
            self.assertGreater(cap,0)
            self.assertLess(cap,Fraction(1,3))
        with self.assertRaises(ValueError):
            f.finite_completion_error_bound(9,3,8)

    def test_positive_fejer_kernel_identity(self):
        for H in [1,2,3,8]:
            for x in [0.0,0.1,0.2,0.317,0.5]:
                z=complex(math.cos(2*math.pi*x),math.sin(2*math.pi*x))
                positive=abs(sum((z**j for j in range(H+1))))**2/(H+1)
                fourier=1+2*sum((1-m/(H+1))*math.cos(2*math.pi*m*x)
                                for m in range(1,H+1))
                self.assertAlmostEqual(positive,fourier,places=11)
                self.assertGreaterEqual(positive,0)

    def test_exact_dilation_ladder_numerical_check(self):
        n=32
        q=f.alpha_cutoff(n)
        for h,k in [(1,1),(1,2),(3,1),(11,2)]:
            c=f.fourier_means(q,n,h*16**k)
            self.assertLessEqual(abs(c[h*16**k]-c[h]),2*k/n+1e-12)

    def test_constant_cap_quantitative_conclusion(self):
        for n,H,h in [(32,64,1),(64,128,1),(64,256,2)]:
            q=f.alpha_cutoff(n)
            E=f.fejer_energy(q,n,H)
            K=1
            while 2*h*16**K<=H:
                K+=1
            rhs=math.sqrt(max(E-1,0)/K)+(K-1)/n
            self.assertLessEqual(abs(f.fourier_means(q,n,h)[h]),
                                 rhs+1e-11)

    def test_same_source_changed_seed_coherent_control(self):
        for n,H in [(8,4),(32,8),(64,10)]:
            q=Fraction(1,5)
            self.assertTrue(all(a==1 and d==5
                                for a,d in f.orbit_mod_one(q,n)))
            self.assertAlmostEqual(f.fejer_energy(q,n,H),H+1,places=10)

    def test_finite_original_probe_not_asymptotic(self):
        for n,H in [(32,5),(64,8),(128,11),(256,16),(512,22)]:
            E=f.fejer_energy(f.alpha_cutoff(n),n,H)
            self.assertTrue(math.isfinite(E))
            self.assertGreaterEqual(E,1-1e-11)
            self.assertLess(E,2)

    def test_golden_two_conjugates_and_mod8(self):
        vals=[]
        for k in range(121):
            a,b=f.fib_pair_power(k)
            aa,bb=f.fib_pair_power(k+1)
            u,v=f.golden_bezout(k)
            self.assertEqual((u*a+v*aa,u*b+v*bb),(1,0))
            self.assertEqual(a*bb-aa*b,(-1)**k)
            self.assertNotEqual(f.lucas_trace(k)%8,0)
            vals.append(f.lucas_trace(k)%8)
        self.assertEqual(vals[:12],vals[12:24])

    def test_gamma_is_not_inverse_golden(self):
        gamma=0.5772156649015328606
        inverse_phi=(math.sqrt(5)-1)/2
        self.assertGreater(inverse_phi-gamma,0.04)
        self.assertLess(inverse_phi-gamma,0.041)


if __name__ == "__main__":
    unittest.main()
