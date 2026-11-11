"""Hostile exact/approximate tests for zero-child seed microscope.

Finite tests validate implementations. No assertion estimates pi's asymptotics.
"""
import math
import unittest
from fractions import Fraction as F

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys
_module_path = Path(__file__).resolve().parents[1] / "research/2026-11-10/zero_seed_microscope/seed_microscope.py"
_spec = spec_from_file_location("succ_zero_seed_microscope", _module_path)
m = module_from_spec(_spec)
sys.modules[_spec.name] = m
_spec.loader.exec_module(m)


class ExactRadixTests(unittest.TestCase):
    def test_invalid_inputs_rejected(self):
        for k in (-1, True, 1.2, '3'):
            with self.subTest(k=k), self.assertRaises(ValueError):
                m.cell_width(k)
        for h in (0, True, False, 0.5, '8'):
            with self.subTest(h=h), self.assertRaises(ValueError):
                m.signed_frequency(1, 0, h)
        self.assertEqual(m.annealed_energy_upper(2,3),1)

    def test_exact_high_high_orthogonality(self):
        for k in range(6):
            for n in range(k, k + 9):
                for p in range(k, k + 9):
                    for h in (1, 8, 15, -3):
                        self.assertEqual(m.exactly_orthogonal(n, p, k, h), n != p)

    def test_pair_counter(self):
        for n in range(1, 30):
            for k in range(n + 1):
                self.assertEqual(m.late_orthogonal_pairs(n, k), (n-k)*(n-k-1))

    def test_kernel_zero_exact_even_at_large_frequency(self):
        for k in range(7):
            for n in range(k, k + 3):
                q = m.signed_frequency(n+1, n, 1)
                self.assertEqual(m.normalized_cell_kernel(q, k), 0j)

    def test_kernel_conjugacy(self):
        for k in range(1, 4):
            for q in (-13, -1, 1, 6, 17, 234):
                got = m.normalized_cell_kernel(q, k)
                rev = m.normalized_cell_kernel(-q, k)
                self.assertLess(abs(got.conjugate()-rev), 2e-14)

    def test_rigorous_fixed_depth_cross_pair_bound(self):
        for n in (2,4,8,16,20):
            for a in (F(0), F(1,96), F(7,19)):
                for k in (0,1,n//2,n):
                    for h in (1,8):
                        self.assertLessEqual(
                            abs(m.seed_energy(a,n,k,h)-1/n),
                            float(m.fixed_depth_deviation_upper(n,k,h))+1e-12)

    def test_fixed_depth_scaled_fingerprint_tail_bound(self):
        # The first K rows of the signed pair matrix survive as N increases.
        # A fixed-depth infinite row sum exists, with source-independent
        # rational tail bound, even for the constant-zero hostile source.
        for a in (F(0), F(1,96), F(7,19)):
            for k in (0, 1, 2, 3):
                for h in (1, 8, -3):
                    for n in (max(4,k), 8, 12):
                        trunc = m.scaled_fixed_depth_partial(a,k,h,n)
                        actual = n*n*(m.seed_energy(a,n,k,h)-1/n)
                        self.assertAlmostEqual(trunc, actual, delta=3e-12)
                        future = m.scaled_fixed_depth_partial(a,k,h,n+14)
                        self.assertLessEqual(abs(future-trunc),
                            float(m.fixed_depth_scaled_limit_tail(k,h,n)) + 3e-12)
        self.assertEqual(m.scaled_fixed_depth_partial(F(0),0,8,8),0.0)
        self.assertEqual(m.fixed_depth_scaled_limit_tail(0,8,9),F(0))

    def test_fixed_depth_h8_sign_survives_infinite_limit(self):
        c = m.certify_first_weyl8_detail()
        lo,hi = m.source_alpha_interval(32)
        a=(lo+hi)/2
        for horizon in (4,8,16):
            finite = m.scaled_fixed_depth_partial(a,1,8,horizon)
            tail = m.fixed_depth_scaled_limit_tail(1,8,horizon)
            self.assertGreater(finite-float(tail), 16/(225*float(c.pi_upper))-1e-11)
        self.assertAlmostEqual(m.scaled_fixed_depth_partial(F(0),1,8,16),0.0,delta=1e-12)

    def test_scaled_limit_strict_validation(self):
        for k,h,cutoff in [(-1,8,4),(1,0,4),(1,1,0),(5,1,4),(True,1,4)]:
            with self.subTest(k=k,h=h,cutoff=cutoff), self.assertRaises(ValueError):
                m.fixed_depth_scaled_limit_tail(k,h,cutoff)
        for a in (0.5,'0',None,True):
            with self.subTest(a=a),self.assertRaises(TypeError):
                m.scaled_fixed_depth_partial(a,1,1,5)

    def test_machin_rational_certificate(self):
        c=m.certify_first_weyl8_detail()
        self.assertEqual(c.sign,"POSITIVE_FOR_EVERY_N_GE_2")
        self.assertGreater(c.sine_lower,F(1,3))
        self.assertEqual(c.tail_absolute_bound,F(1,225))
        for n in (2,4,8,16,20):
            a=F(0)  # no pi source for rational control
            self.assertAlmostEqual(m.zero_child_detail(a,n,0,8),0.,delta=1e-11)
        try:
            from observational_succ import duck_bbp
        except ImportError:
            self.skipTest('canonical source not installed in scratch checkout')
        for n in (2,4,8,16):
            lo,hi=m.source_alpha_interval(n+32)
            actual=m.zero_child_detail((lo+hi)/2,n,0,8)
            # The strict all-N lower constant is 16/(225*pi*N^2).
            self.assertGreater(actual, 16/(225*float(c.pi_upper)*n*n))

    def test_point_and_quantization_budgets(self):
        for n in (1, 2, 8, 64, 256):
            for k in (0, n//2, n, n+3):
                self.assertGreaterEqual(m.annealed_energy_upper(n,k),0)
                self.assertLessEqual(m.annealed_energy_upper(n,k),1)
                self.assertLessEqual(m.point_recovery_error(n,k,1),2)
                if k>=n:
                    self.assertLessEqual(m.point_recovery_error(n,k,1),F(7,15*n*16**(k-n)))


class AnalyticVsIndependentQuadrature(unittest.TestCase):
    def test_uniform_seed_parseval(self):
        for a in (F(0), F(1,96), F(7,19), F(123,997)):
            for n in (1, 2, 4, 8, 12):
                for h in (1, 8, 15):
                    self.assertAlmostEqual(m.seed_energy(a,n,0,h),1/n,delta=1e-12)

    def test_child_partition_martingale(self):
        for a in (F(0), F(1,96), F(7,19)):
            for n in (2, 5, 9):
                for k in (0,1,2):
                    parent = m.seed_energy(a,n,k)
                    children = sum(m.child_energy(a,n,k,j) for j in range(16))/16
                    self.assertAlmostEqual(children,parent,delta=2e-12)

    def test_child_fourier_packet_recovers_selected_branch(self):
        for alpha in (F(0),F(1,96),F(7,19)):
            for n in (3,7,11):
                for k in (0,1):
                    packet=m.child_fourier_packet(alpha,n,k,8)
                    self.assertEqual(len(packet),16)
                    parent=m.seed_energy(alpha,n,k,8)
                    zero=m.child_energy(alpha,n,k,0,8)
                    self.assertAlmostEqual(packet[0].real,parent,delta=1e-12)
                    self.assertAlmostEqual(sum(packet).real,zero,delta=1e-12)
                    self.assertAlmostEqual(sum(packet[1:]).real,zero-parent,delta=1e-12)
                    self.assertLess(abs(sum(packet).imag),1e-12)

    def test_zero_scale_telescoping(self):
        for a in (F(0),F(11,71),F(1,96)):
            n=12
            energies=[m.seed_energy(a,n,k) for k in range(n+1)]
            increments=[m.zero_child_detail(a,n,k) for k in range(n)]
            self.assertAlmostEqual(sum(increments),energies[n]-energies[0],delta=1e-11)
            self.assertAlmostEqual(energies[0],1/n,delta=1e-12)
            self.assertLess(abs(energies[-1]-abs(m.selected_weyl_mean(a,n))**2),
                            float(m.energy_recovery_error(n,n)), 'analytic point budget')

    def test_annealed_bound_controls_hostile_zero(self):
        # Source α=0 is a coherently nonnormal completed orbit, yet its
        # near-zero cylinder ensemble obeys universal mean-square bounds.
        n=20
        for k in (0,1,3,6,10,n):
            v=m.seed_energy(F(0),n,k)
            self.assertLessEqual(v,float(m.annealed_energy_upper(n,k))+1e-11)
        self.assertAlmostEqual(abs(m.selected_weyl_mean(F(0),n)),1)

    def test_independent_quadrature(self):
        def brute(a,n,k,h,steps):
            interval=F(1,16**k)
            total=0.
            for j in range(steps):
                x= a + interval*F(2*j+1,2*steps)
                z=sum(complex(math.cos(2*math.pi*float((h*16**t*x)%1)),
                              math.sin(2*math.pi*float((h*16**t*x)%1)))
                      for t in range(n))/n
                total+=abs(z)**2
            return total/steps
        for a,n,k in [(F(0),3,1),(F(7,19),5,2),(F(1,96),4,1)]:
            self.assertAlmostEqual(m.seed_energy(a,n,k),brute(a,n,k,1,8192),delta=2e-4)

    def test_source_alpha_contract_canonical(self):
        try:
            from observational_succ import duck_bbp
        except ImportError:
            self.skipTest('canonical source not installed in scratch checkout')
        for L in (0,1,2,5,20):
            lo,hi=m.source_alpha_interval(L)
            self.assertEqual(lo, sum((duck_bbp.forcing(j)/16**j for j in range(1,L+1)),F()))
            self.assertEqual(hi-lo,duck_bbp.source_tail_budget(L)/16**L)
            self.assertGreater(hi,lo)

    def test_mutated_source_or_budget_rejected(self):
        from observational_succ import duck_bbp
        from unittest.mock import patch
        original=duck_bbp.forcing
        with patch.object(duck_bbp, "forcing", side_effect=lambda n: original(n)+F(1,16**n) if n==3 else original(n)):
            with self.assertRaisesRegex(ValueError,"source mismatch"):
                m.source_alpha_interval(5)
        with patch.object(duck_bbp, "source_tail_budget", return_value=F(0)):
            with self.assertRaisesRegex(ValueError,"budget mismatch"):
                m.source_alpha_interval(5)

    def test_first_detail_closed_form_cross_implementation(self):
        from math import sin, pi
        from observational_succ import duck_bbp
        for n in (2,4,8,16):
            low,high=m.source_alpha_interval(n+35)
            direct=m.zero_child_detail((low+high)/2,n,0,8)
            derived= -4/(pi*n*n)*sum(sin(pi*pi*(16**j-1))/(16**j-1)
                                       for j in range(1,n))
            self.assertAlmostEqual(direct,derived,delta=1e-12)
            self.assertGreater(direct,16/(225*pi*n*n))

    def test_independent_machin_bbp_interval_overlap(self):
        from observational_succ import duck_bbp
        ml,mu=m.machin_pi_bounds(10)
        bl,bu=m.source_alpha_interval(15)
        self.assertLess(bl,mu/16)
        self.assertGreater(bu,ml/16)

    def test_original_source_demo_has_separate_analytic_budget(self):
        try:
            from observational_succ import duck_bbp
        except ImportError:
            self.skipTest('canonical source not installed in scratch checkout')
        r=m.microscope_receipt(8,1,horizon=36)
        self.assertEqual(len(r.annealed_energy),9)
        self.assertEqual(len(r.signed_zero_child_details),8)
        self.assertLessEqual(abs(r.annealed_energy[-1]-r.selected_weyl_power),
                             float(r.point_recovery_budget)+1e-12)
        self.assertLess(r.truncated_phase_budget,F(1,10**20))

if __name__=='__main__':
    unittest.main()
