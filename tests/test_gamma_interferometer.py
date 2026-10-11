"""Source, Gamma, causality and local-sign controls for the interferometer.

No zeros are supplied and finite numerical agreement never certifies RH.
"""
import unittest
from fractions import Fraction
import mpmath as mp

from observational_succ.gamma_interferometer import (
    GammaInterferometer, InterferometerError,
    archimedean_response, individual_impulse_determinant,
)


class GammaInterferometerTests(unittest.TestCase):
    def setUp(self):
        self.source = {n: 1 for n in range(1, 50)}
        self.baseline = GammaInterferometer.from_prefix(self.source, 49)

    def test_suzuki_regression_values(self):
        # Cross-check original scripts/suzuki_psi.py regression fixtures.
        expected = {
            ".1": "0.05313043381777025410005234409146544",
            ".5": "0.0401625803820866649861141479969911",
            "1": "0.0440073052368525268602186064080838",
            "2": "0.0533411241718556689631189360507922",
        }
        with mp.workdps(70):
            for t, want in expected.items():
                got = self.baseline.at_time(t, dps=70)["psi"]
                self.assertLess(abs(got-mp.mpf(want)), mp.mpf("1e-32"))

    def test_gamma_independent_series(self):
        # Separate exponentially convergent sum, not Lerch Phi.
        with mp.workdps(70):
            t = mp.mpf(2)
            z = mp.exp(-t/2)
            tail = sum(4*z**(4*k+1)/(4*k+1)**2 for k in range(100))
            linear = (mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi))/2
            other = (4*(mp.exp(t/2)+mp.exp(-t/2)-2) + t*linear
                     + (mp.pi**2+8*mp.catalan)/4-tail)
            self.assertLess(abs(other-archimedean_response(t,dps=70)),mp.mpf("1e-65"))

    def test_exact_log_support(self):
        expected = {2:1,3:1,4:Fraction(1,2),6:0,8:Fraction(1,3),
                    9:Fraction(1,2),12:0,27:Fraction(1,3),36:0}
        for n, want in expected.items():
            self.assertEqual(self.baseline.connected[n], want)
        self.assertTrue(self.baseline.matches_zeta_prefix)
        self.assertEqual(self.baseline.diagnostic()["non_prime_power_connected_anomalies"], [])

    def test_source_causality(self):
        class Guard(dict):
            def __getitem__(self, key):
                if key > 7:
                    raise AssertionError("Future data queried")
                return super().__getitem__(key)
        one = GammaInterferometer.from_prefix(Guard(self.source), 7)
        two = GammaInterferometer.from_prefix({n:1 for n in range(1,8)}, 7)
        self.assertEqual(one.connected,two.connected)
        self.assertEqual(one.at_event(7)["psi"],two.at_event(7)["psi"])
        with self.assertRaises(InterferometerError):
            one.at_event(8)
        with self.assertRaises(InterferometerError):
            one.at_time("2")
        with self.assertRaises(InterferometerError):
            GammaInterferometer.from_prefix({n:1 for n in range(1,7)},7)

    def test_fake_six_is_slope_not_value(self):
        mutated=dict(self.source)
        mutated[6]=Fraction(3,2)
        fake=GammaInterferometer.from_prefix(mutated,49)
        self.assertEqual(fake.connected[6],Fraction(1,2))
        self.assertIn(6,fake.diagnostic()["non_prime_power_connected_anomalies"])
        self.assertEqual(fake.at_event(6)["psi"],self.baseline.at_event(6)["psi"])
        with mp.workdps(65):
            jump=-mp.log(6)/(2*mp.sqrt(6))
            self.assertLess(abs(fake.slope_jump(6,dps=65)-jump),mp.mpf("1e-60"))
            observed=fake.at_event(7,dps=65)["psi"]-self.baseline.at_event(7,dps=65)["psi"]
            self.assertLess(abs(observed-jump*mp.log(mp.mpf(7)/6)),mp.mpf("1e-60"))

    def test_prime_and_nonreal_mutation(self):
        changed=dict(self.source)
        changed[2]=Fraction(11,10)
        wrong=GammaInterferometer.from_prefix(changed,49)
        self.assertIn(2,wrong.diagnostic()["prime_power_weight_anomalies"])
        self.assertNotEqual(wrong.slope_jump(2),self.baseline.slope_jump(2))
        with self.assertRaises(InterferometerError):
            GammaInterferometer.from_prefix({1:1,2:1j},2)
        with self.assertRaises(InterferometerError):
            GammaInterferometer.from_prefix({1:1,2:1.01},2)

    def test_individual_impulse_negative_minor(self):
        with mp.workdps(60):
            a=mp.log(2)
            w=mp.log(2)/mp.sqrt(2)
            determinant=individual_impulse_determinant(a,w,dps=60)
            self.assertLess(determinant,0)
            self.assertLess(abs(determinant+(w*a/4)**2),mp.mpf("1e-58"))
            self.assertEqual(individual_impulse_determinant(a,-w,dps=60),determinant)

    def test_screw_symmetry_not_global_psd(self):
        with mp.workdps(60):
            t,u=mp.mpf(".5"),mp.mpf("1.3")
            self.assertLess(abs(self.baseline.screw(t,u,dps=60)
                                -self.baseline.screw(u,t,dps=60)),mp.mpf("1e-55"))
            self.assertLess(abs(self.baseline.screw(t,t,dps=60)
                                -2*self.baseline.at_time(t,dps=60)["psi"]),mp.mpf("1e-55"))

    def test_real_engine_pending_observation_exclusion(self):
        from observational_succ import Engine, Limits, source_at
        engine=Engine(arithmetic=True,limits=Limits(max_target=16))
        for n in range(1,6):
            engine.advance(source_at(n),context="zeta",probe="coefficient")
        engine.predict(6,2,"deliberate wrong prediction")
        engine.step(source_at(6),context="zeta",probe="coefficient")
        pending=GammaInterferometer.from_engine(engine)
        self.assertEqual(pending.horizon,5)
        with self.assertRaises(InterferometerError):
            pending.at_event(6)
        engine.propagate()
        done=GammaInterferometer.from_engine(engine)
        self.assertEqual(done.horizon,6)
        self.assertEqual(done.connected[6],0)
        self.assertTrue(done.matches_zeta_prefix)
        self.assertEqual(done.trace_head,engine.head)


if __name__=="__main__":
    unittest.main()
