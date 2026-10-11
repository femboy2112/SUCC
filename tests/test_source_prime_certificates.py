"""Rigorous exact-rational source-side Suzuki/prime wavefront controls.

We verify the analytic finite prime contribution with independent mpmath
holdouts, but the CERTIFICATION is the rational log/sqrt remainder
construction. No nontrivial zero input, no Gamma interval oracle,
and no Weil/RH-positive conclusion is made.
"""
import unittest
from fractions import Fraction as Q
import mpmath as mp

from observational_succ.source_prime_certificates import (
    SourceCertificateError,rational_log_ratio,
    rational_log_integer,rational_inverse_sqrt,
    finite_prime_horizon,CertifiedPrimeSource,
    prime_delta_at_fake_six,
)
from observational_succ.gamma_interferometer import GammaInterferometer
from observational_succ import Engine, Limits, Scalar, source_at
from observational_succ.observer_reflection import rational_gram_certificate


def mpr(q):
    q=Q(q)
    return mp.mpf(q.numerator)/q.denominator


class CertifiedSourceTests(unittest.TestCase):
    def test_certified_prime_journal_does_not_integrate_predictions(self):
        e=Engine(arithmetic=True,limits=Limits(max_target=24))
        for n in range(1,6):
            e.advance(source_at(n),context="zeta",probe="coefficient")
        e.predict(6,Scalar(2),"counterfeit future guess")
        e.step(Scalar(2),context="fake",probe="coefficient")
        snapshot=CertifiedPrimeSource.from_engine(e,horizon=5)
        self.assertEqual(snapshot.snapshot.horizon,5)
        self.assertEqual(snapshot.provenance()["trace_head"],e.head)
        self.assertTrue(snapshot.provenance()["source_matches_zeta"])
        with self.assertRaises(SourceCertificateError):
            CertifiedPrimeSource.from_engine(e,horizon=6)
        e.propagate()
        later=CertifiedPrimeSource.from_engine(e,horizon=6)
        self.assertEqual(later.snapshot.connected[6],1)
        self.assertFalse(later.provenance()["source_matches_zeta"])
        self.assertNotEqual(later.provenance()["trace_head"],
                            snapshot.provenance()["trace_head"])


    def test_exact_rational_log_enclosures_against_independent_mpmath(self):
        with mp.workdps(110):
            for n in (1,2,3,4,6,8,9,15,31,53,81,251):
                for terms in (8,16,24):
                    a=rational_log_integer(n,terms=terms)
                    target=mp.log(n)
                    self.assertLessEqual(mpr(a.lower),target)
                    self.assertGreaterEqual(mpr(a.upper),target)
                    if n>1:
                        self.assertGreater(a.upper,a.lower)
                    self.assertGreaterEqual(a.lower,0)
            for num,den in ((1,1),(5,4),(3,2),(2,1)):
                a=rational_log_ratio(num,den,terms=24)
                target=mp.log(mp.mpf(num)/den)
                self.assertLessEqual(mpr(a.lower),target)
                self.assertGreaterEqual(mpr(a.upper),target)
            self.assertEqual(rational_log_integer(1).lower,0)
            with self.assertRaises(SourceCertificateError):
                rational_log_ratio(3,1)
            with self.assertRaises(SourceCertificateError):
                rational_log_integer(2,terms=0)

    def test_exact_inverse_sqrt_bounds(self):
        with mp.workdps(110):
            for n in (1,2,3,4,6,9,25,27,31,53,251):
                a=rational_inverse_sqrt(n,places=20)
                x=1/mp.sqrt(n)
                self.assertLessEqual(mpr(a.lower),x)
                self.assertGreaterEqual(mpr(a.upper),x)
                self.assertLess(a.upper-a.lower,Q(1,10**18))
            self.assertEqual(rational_inverse_sqrt(4).upper,Q(1,2))
            with self.assertRaises(SourceCertificateError):
                rational_inverse_sqrt(2,places=100)

    def test_conservative_horizon_requires_actualized_future(self):
        self.assertEqual(finite_prime_horizon((Q(0),)),2)
        self.assertEqual(finite_prime_horizon((Q(1),)),3)
        self.assertEqual(finite_prime_horizon((Q(1),Q(-1))),9)
        self.assertEqual(finite_prime_horizon((Q(3,2),)),9)
        s=CertifiedPrimeSource.genuine(8)
        with self.assertRaises(SourceCertificateError):
            s.prime_psi(Q(3,2))
        with self.assertRaises(SourceCertificateError):
            s.prime_screw(1,-1)
        with self.assertRaises(SourceCertificateError):
            finite_prime_horizon((Q(5),))
        with self.assertRaises(SourceCertificateError):
            finite_prime_horizon((0.5,))

    def test_real_prime_wavefront_rational_interval_matches_independent_formula(self):
        s=CertifiedPrimeSource.genuine(81,log_terms=32,sqrt_places=28)
        with mp.workdps(105):
            for t in (Q(0),Q(1,5),Q(1,2),Q(1),Q(9,5),Q(2),Q(12,5),Q(3)):
                enclosed=s.prime_psi(t)
                diagnostic=s.snapshot.at_time(mpr(t),dps=105)
                value=-diagnostic["finite"]
                self.assertLessEqual(mpr(enclosed.lower),value)
                self.assertGreaterEqual(mpr(enclosed.upper),value)
                self.assertLess(mpr(enclosed.upper-enclosed.lower),
                                mp.mpf("1e-20"))
            for t,u in ((Q(1,2),Q(1)),(Q(9,5),Q(1)),(Q(3,2),Q(3,5))):
                K=s.prime_screw(t,u)
                target=(-s.snapshot.at_time(mpr(t),dps=105)["finite"]
                        -s.snapshot.at_time(mpr(u),dps=105)["finite"]
                        +s.snapshot.at_time(mpr(abs(t-u)),dps=105)["finite"])
                self.assertLessEqual(mpr(K.lower),target)
                self.assertGreaterEqual(mpr(K.upper),target)
                self.assertTrue(s.prime_screw(t,u).intersects(s.prime_screw(u,t)))

    def test_certified_fake_six_prime_residual_not_full_weil(self):
        interval=prime_delta_at_fake_six(
            t=Q(9,5),log_terms=32,sqrt_places=28,horizon=27)
        self.assertLess(interval.upper,0)
        with mp.workdps(108):
            actual=-mp.log(6)/mp.sqrt(6)*(mp.mpf(9)/5-mp.log(6))
            self.assertLessEqual(mpr(interval.lower),actual)
            self.assertGreaterEqual(mpr(interval.upper),actual)
        with self.assertRaises(SourceCertificateError):
            prime_delta_at_fake_six(t=Q(3,2),horizon=27)
        self.assertGreater(interval.upper-interval.lower,0)

    def test_source_prefix_and_genuine_status_are_explicit(self):
        genuine=CertifiedPrimeSource.genuine(27)
        src={n:1 for n in range(1,28)}
        src[6]=2
        fake=CertifiedPrimeSource(GammaInterferometer.from_prefix(src,27))
        self.assertTrue(genuine.provenance()["source_matches_zeta"])
        self.assertFalse(fake.provenance()["source_matches_zeta"])
        self.assertFalse(genuine.provenance()["Gamma_pole_completion_certified"])
        self.assertFalse(fake.provenance()["full_Weil_positive_form_proved"])
        t=Q(9,5)
        true=genuine.prime_psi(t)
        changed=fake.prime_psi(t)
        self.assertLess((changed-true).upper,0)
        # This is a perfectly valid CERTIFIED *prime-only* Gram oracle.
        # A negative Gram from it is NOT an RH counterexample,
        # because the Gamma/pole component has not been added.
        probe=rational_gram_certificate(
            (Q(1),Q(9,5)),(Q(1),Q(1)),
            genuine.oracle,provenance="PRIME SIDE ONLY, Gamma still missing")
        self.assertIn(probe.result,(
            "FINITE_PROBE_UNRESOLVED",
            "STRICT_NEGATIVE_WITNESS_CONDITIONAL_ON_INTERVAL_ORACLE"))
        self.assertIn("PRIME SIDE ONLY",probe.oracle_provenance)


if __name__=="__main__":
    unittest.main()
