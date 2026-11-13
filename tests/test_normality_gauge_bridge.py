"""Exact local controls; source-complete normality is a PAPER theorem, not tested."""
import unittest
from fractions import Fraction as Q
from dataclasses import replace

from observational_succ.normality_gauge_bridge import (
    GaugeProbeError, bernoulli4, pinbed_energy,
    selected_unwrapped_states, original_lag_phases,
    source_lag_gauge_control, lag_pinbed_receipt, phase_rotation_energy,
)
from observational_succ import duck_bbp


class GaugeNormalityAuditTest(unittest.TestCase):
    def test_four_pole_source_cross_calibration(self):
        for n in range(1, 20):
            signed = Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
            self.assertEqual(signed, duck_bbp.forcing(n))
        s=selected_unwrapped_states(19)
        self.assertEqual(s[0],0)
        for n in range(1,len(s)):
            self.assertEqual(s[n],16*s[n-1]+duck_bbp.forcing(n))

    def test_b4_parity_under_circle_inversion(self):
        for a in range(-22, 22):
            t=Q(a,17)
            self.assertEqual(bernoulli4(t),bernoulli4(-t))
        self.assertEqual(bernoulli4(0),-Q(1,30))
        with self.assertRaises(GaugeProbeError):
            bernoulli4(0.1)

    def test_exact_energy_calibration_dirac_uniform_grid(self):
        self.assertEqual(pinbed_energy((Q(0),)),Q(1,180))
        for q in (2,3,7,16,17):
            sample=tuple(Q(i,q) for i in range(q))
            self.assertEqual(pinbed_energy(sample),Q(1,180*q**4))

    def test_independent_sorted_bernoulli_energy_formula(self):
        for sample in (
            (Q(0),Q(0),Q(1,7)),
            (Q(1,9),Q(4,7),Q(7,8),Q(3,5)),
            (Q(0),Q(1,2),Q(1,4),Q(3,4),Q(0)),
        ):
            xs=sorted(x%1 for x in sample)
            N=len(xs)
            correction=sum((
                (xs[i]-xs[j])**4-2*(xs[i]-xs[j])**3+(xs[i]-xs[j])**2
                for i in range(N) for j in range(i)
            ),Q())
            independent=Q(1,180)-correction/Q(3*N*N)
            self.assertEqual(pinbed_energy(sample),independent)

    def test_normality_probe_requires_every_frequency(self):
        # Law half delta_0 + half delta_(1/2): first Fourier mode vanishes
        # but the complete characteristic pinbed remains nonzero.
        self.assertEqual(pinbed_energy((Q(0),Q(1,2))),Q(1,180*2**4))
        self.assertNotEqual(pinbed_energy((Q(0),Q(1,2))),0)

    def test_global_chart_gauge_rotation_and_orientation(self):
        sample=(Q(0),Q(5,17),Q(12,17),Q(3,19))
        for theta in (Q(1,3),Q(1,15),Q(-5,7),Q(0)):
            self.assertEqual(phase_rotation_energy(sample,theta),pinbed_energy(sample))
        self.assertEqual(pinbed_energy(tuple((-x)%1 for x in sample)),pinbed_energy(sample))

    def test_illegal_samplewise_gauge_can_hide_nonnormality(self):
        # Per-index arbitrary phase offsets could convert any constant
        # sequence into an almost-uniform grid; they aren't a lawful gauge.
        signal=(Q(0),)*16
        fake=tuple(Q(i,16) for i in range(16))
        self.assertNotEqual(pinbed_energy(signal),pinbed_energy(fake))
        self.assertGreater(pinbed_energy(signal),pinbed_energy(fake))

    def test_bbp_lag_phases_cross_direct_recurrence(self):
        for B in (1,2,4):
            for ell in (1,2,4):
                sample=original_lag_phases(B,ell)
                self.assertEqual(len(sample),B)
                for j,n in enumerate(range(B,2*B)):
                    s=selected_unwrapped_states(n+ell)
                    self.assertEqual(sample[j], (s[n+ell]-s[n])%1)

    def test_torsion_source_vs_observation_gauge(self):
        for B in (1,2,4):
            for ell in (1,2,4):
                for j in (-2,0,1,7,15):
                    self.assertTrue(source_lag_gauge_control(B,ell,j))
        with self.assertRaises(GaugeProbeError):
            source_lag_gauge_control(2,1,1.0)

    def test_squared_transport_debt_is_uniform_in_lag(self):
        for B in (1,2,3,4):
            debts=[]
            for ell in (1,2,4):
                receipt=lag_pinbed_receipt(B,ell)
                self.assertGreater(receipt.energy,0)
                self.assertTrue(receipt.gauge_15torsion_invariant)
                self.assertFalse(receipt.normality_decided)
                debts.append(receipt.surface_norm_transfer_upper_square)
            self.assertEqual(debts,[Q(1,3*64*64*B**4)]*len(debts))

    def test_finite_small_signal_is_not_haar(self):
        # The q-grid becomes arbitrarily small in E but remains atomic,
        # with exact nonzero energy at every finite q.
        grid=tuple(Q(j,17) for j in range(17))
        self.assertGreater(pinbed_energy(grid), 0)
        self.assertLess(pinbed_energy(grid), Q(1,1000000))

    def test_bool_float_and_malformed_data_rejected(self):
        for bad in (True,1.0,-1,None):
            with self.assertRaises(GaugeProbeError):
                lag_pinbed_receipt(bad,1)
        with self.assertRaises(GaugeProbeError):
            pinbed_energy(())
        with self.assertRaises(GaugeProbeError):
            pinbed_energy((Q(0),0.1))
        with self.assertRaises(GaugeProbeError):
            phase_rotation_energy((Q(0),),0.1)


if __name__=='__main__':
    unittest.main()