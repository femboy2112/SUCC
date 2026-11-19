"""Isolated, exact standards-based tests for the Jacobian/objective observatory.
No full-repository CI coverage or asymptotic normality assertions.
"""
import importlib.util
import math
from fractions import Fraction
from pathlib import Path
import unittest

SCRIPT = (Path(__file__).resolve().parents[1] / 'research' / '2026-11-19' /
          'jacobian_objective_gluing' / 'probe.py')
spec = importlib.util.spec_from_file_location('jacobian_objective_gluing_probe', SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class JacobianObjectiveGluingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.states = mod.zero_seed_history(2*128+56)

    def test_original_zero_seed_and_signed_poles(self):
        self.assertEqual(mod.forcing(1), Fraction(47, 15))
        self.assertEqual(self.states[0], 0)
        for n in range(1, 15):
            self.assertEqual(self.states[n]-16*self.states[n-1], mod.forcing(n))

    def test_finite_completed_boundary_and_history(self):
        for N in (3,7,17):
            P = mod.finite_completed_seed(N)
            self.assertEqual(16**N*P, self.states[N])
            tail = sum((mod.forcing(N+k)*Fraction(1,16**k) for k in range(1, 35)), Fraction())
            self.assertGreater(tail, 0)
            self.assertLess(tail, mod.source_tail_bound(N))

    def test_cauchy_formula(self):
        for times in ((1,2,3,4),(55,89,144,233),(55,89,147,233)):
            rows = [mod.source_row(t) for t in times]
            self.assertEqual(mod.det_exact(rows), mod.cauchy_det(times))
            self.assertNotEqual(mod.cauchy_det(times), 0)

    def test_seed_anchor_jacobian(self):
        for depth in (2,10,25):
            self.assertEqual(mod.det_exact(mod.five_channel_jacobian((55,89,144,233),depth)),
                             mod.cauchy_det((55,89,144,233)))

    def test_3_and_11_adic_defects(self):
        r = mod.prime_schedule_report(mod.FIBONACCI_TIMES)
        self.assertEqual(r[3]['rank'], 3)
        self.assertEqual(r[11]['rank'], 3)
        self.assertEqual(r[5]['rank'], 4)
        self.assertEqual(r[7]['rank'], 4)
        self.assertEqual(r[29]['rank'], 4)

    def test_forward_adaptive_repairs(self):
        self.assertEqual(mod.admissible_next_clock((55,89,144),3,(145,146,147)),146)
        self.assertEqual(mod.admissible_next_clock((55,89,144,146),11,(147,148)),147)
        r = mod.prime_schedule_report(mod.REPAIRED_CHRONOLOGY)
        for p in mod.PRIME_CHANNELS:
            self.assertEqual(r[p]['rank'],4)
        self.assertEqual({p:max(r[p]['scales']) for p in mod.PRIME_CHANNELS},
                         {3:3,5:2,7:2,11:1,29:0})

    def test_prime_pole_row_separation(self):
        self.assertEqual(mod.normalized_prime_row(146,3)[0],3)
        self.assertEqual(mod.normalized_prime_row(233,7)[0],2)
        self.assertEqual(mod.normalized_prime_row(147,11)[0],0)
        for p in (3,5,7,11,29):
            for n in mod.REPAIRED_CHRONOLOGY:
                scale,row = mod.normalized_prime_row(n,p)
                self.assertGreaterEqual(scale,0)
                self.assertTrue(any(row))

    def test_clean_residue_capacity(self):
        for p,expected in ((3,0),(5,2),(7,3),(11,7),(29,25)):
            residues = {b%p for b in mod.BETA}
            admissible = [n for n in range(p) if all((8*n-b)%p for b in mod.BETA)]
            self.assertEqual(len(admissible),p-len(residues))
            self.assertEqual(len(admissible),expected)

    def test_history_reconstruction(self):
        for n in range(1,42):
            self.assertEqual(self.states[n]-16*self.states[n-1],mod.forcing(n))

    def test_all_local_observers_can_lock_and_global_cancel(self):
        for M in (16,32,64):
            W,D = mod.uniform_grid_control(M,1)
            self.assertLess(abs(W),1e-12)
            self.assertAlmostEqual(D,1,places=12)

    def test_fixed_orbit_objective_lock_control(self):
        # For x = 1/15, 16^n x mod 1 is fixed forever.
        x = Fraction(1,15)
        phases = [mod.phase((16**n)*x) for n in range(30,60)]
        self.assertLess(max(abs(a-b) for a in phases for b in phases),1e-12)
        self.assertAlmostEqual(abs(sum(phases)/len(phases)),1,places=12)

    def test_original_phase_partition_variance(self):
        for B in (16,32,64,128):
            r = mod.shell_phase_partition(self.states,B,bins=16)
            self.assertLess(abs(r['variance']-r['within']-r['between']),1e-12)
            self.assertGreaterEqual(r['min_local_coherence'],math.cos(math.pi/16)-1e-12)

    def test_preregistered_holonomy_identity(self):
        for B in (16,32,64,128):
            for ell,h in mod.WEYL_PROBES:
                H = mod.holonomy(self.states,B,ell,h)
                self.assertGreaterEqual(H,0)
                self.assertLessEqual(H,Fraction(1,4))

    def test_valid_r0_lower_bound_rational_phase(self):
        for B in (16,64,128):
            W = sum(mod.phase(self.states[n]) for n in range(B,2*B))/B
            for ell,h in mod.WEYL_PROBES:
                H,lb = mod.r0_lower_certificate(self.states,B,ell,h)
                self.assertGreaterEqual(1-W.real+1e-12,lb)

    def test_same_forcing_seed_blind_jacobian(self):
        # Affine seeds change states by 16^n s but leave every innovation unchanged.
        seed = Fraction(19,37)
        other = mod.zero_seed_history(12)
        changed = [other[n]+16**n*seed for n in range(13)]
        for n in range(1,13):
            self.assertEqual(changed[n]-16*changed[n-1],other[n]-16*other[n-1])

    def test_parameter_derivative_independence_of_depth(self):
        # Last row changes with finite completion, block determinant does not.
        jac1 = mod.five_channel_jacobian((55,89,144,233),2)
        jac2 = mod.five_channel_jacobian((55,89,144,233),50)
        self.assertNotEqual(jac1[4][:4],jac2[4][:4])
        self.assertEqual(mod.det_exact(jac1),mod.det_exact(jac2))

    def test_signed_gram_reconstructs_pair_correlations(self):
        for B in (16,32,64,128):
            for h in mod.SIGNED_FREQUENCIES:
                E,recon = mod.signed_shift_gram(self.states,B,h)
                self.assertAlmostEqual(E,recon,places=11)
                self.assertGreaterEqual(E,-1e-12)
                self.assertLessEqual(E,1+1e-12)

    def test_weyl_upper_is_genuine_bound_for_rational_proxy(self):
        for B in (64,128):
            for h in mod.SIGNED_FREQUENCIES:
                W = sum(mod.phase(self.states[n],h) for n in range(B,2*B))/B
                self.assertLessEqual(abs(W),mod.shifted_weyl_upper(self.states,B,h)+1e-12)

    def test_wrong_seed_same_forcing_stays_locked(self):
        for B in (32,64,128):
            E = mod.locked_same_forcing_gram(B,1)
            self.assertGreater(E,0.99)

    def test_source_lag_signed_character_is_bounded(self):
        for B in (32,64):
            for ell,h in mod.WEYL_PROBES:
                self.assertLessEqual(abs(mod.signed_lag(self.states,B,ell,h)),1+1e-12)

    def test_no_asymptotic_claim_from_finite_r0(self):
        H,lb = mod.r0_lower_certificate(self.states,64,1,1)
        self.assertTrue(0 < H < Fraction(1,4))
        self.assertGreater(lb,0)
        self.assertEqual(mod.WEYL_PROBES,((1,1),(4,11),(6,7)))


if __name__=='__main__':
    unittest.main()
