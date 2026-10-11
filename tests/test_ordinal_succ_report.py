"""Ordinal ω/ω+1 semantics and exact second-order observer interactions.

The bounded test suite NEVER claims an executed infinite process or a
constructed Hilbert embedding for the completed Weil form.

Core adversaries:
  - Valid local positive observations + positive curvature but Gram NEGATIVE
    (Psi=t^4), detected by rational (-1,+1) observer probes.
  - A genuine PSD observation geometry with sign-changing Psi''
    (Psi=1-cos t), showing pointwise covariance sign is not the test.
  - An honest new composite source a(6)=2, detected as b(6)=1
    and as a **second derivative** jump in the Suzuki report.
  - An incomplete observer cannot use a future unactualized event.
"""
import unittest
from fractions import Fraction as Q

import mpmath as mp

from observational_succ import Engine, Limits, Scalar, source_at
from observational_succ.ordinal_succ_report import (
    OrdinalObservationError, OrdinalFiniteStage,
    exact_bounded_time_horizon, quartic_observer_report,
    exact_polynomial_rectangle, oscillator_observer_report,
    synthetic_ordinal_semantics,
    harmonic_number,harmonic_half_density_observer,
    harmonic_dyadic_divergence_certificate,mellin_hilbert_threshold,
)
from observational_succ.gamma_interferometer import individual_impulse_determinant


class OrdinalObservationTests(unittest.TestCase):

    def test_normalized_hilbert_half_density_escapes_at_omega(self):
        # Each finite Hilbert state has norm one. At Re(s)=1/2,
        # for a fixed local projector P_M, its expectation decays
        # exactly as H_M/H_N, even though <I>=1 at every stage.
        fixed_m=3
        mass=[harmonic_half_density_observer(N,fixed_m)
              for N in (3,6,12,24,48,96,192,384)]
        self.assertTrue(all(x["finite_vector_norm_squared"]==1 for x in mass))
        self.assertTrue(all(x["identity_expectation"]==1 for x in mass))
        self.assertTrue(all(x["Weil_identification_proved"] is False for x in mass))
        fractions=[x["finite_projector_expectation"] for x in mass]
        self.assertEqual(fractions[0],Q(1))
        self.assertTrue(all(a>b for a,b in zip(fractions,fractions[1:])))
        self.assertEqual(fractions[-1],
                         harmonic_number(fixed_m)/harmonic_number(384))
        self.assertTrue(all(x["phase_independent_local_expectations"] for x in mass))
        self.assertFalse(mass[-1]["infinite_vector_summable"])
        for sigma,finite in ((Q(0),False),(Q(1,3),False),
                             (Q(1,2),False),(Q(3,5),True),(Q(1),True)):
            self.assertEqual(mellin_hilbert_threshold(sigma)[
                             "sum_of_squared_amplitudes_finite"],finite)
        self.assertTrue(mellin_hilbert_threshold(Q(1,2))[
                        "is_critical_harmonic_boundary"])
        with self.assertRaises(OrdinalObservationError):
            mellin_hilbert_threshold(0.5)

    def test_exact_dyadic_lower_bound_proves_harmonic_escape(self):
        for k in range(0,9):
            r=harmonic_dyadic_divergence_certificate(k)
            self.assertEqual(r["stage_N"],2**k)
            self.assertGreaterEqual(r["exact_H_N"],r["provable_lower_bound"])
            self.assertEqual(r["provable_lower_bound"],Q(1)+Q(k,2))
            self.assertFalse(r["physical_infinite_time_executed"])
        with self.assertRaises(OrdinalObservationError):
            harmonic_dyadic_divergence_certificate(13)

    def test_exact_arithmetic_horizon_from_rational_probe_clock(self):
        self.assertEqual(
            exact_bounded_time_horizon((Q(1),Q(-1)))["certified_source_SUCC_horizon"],9)
        self.assertEqual(
            exact_bounded_time_horizon((Q(0),))["certified_source_SUCC_horizon"],2)
        self.assertEqual(
            exact_bounded_time_horizon((Q(1,2),Q(3,2)))["certified_source_SUCC_horizon"],9)
        with self.assertRaises(OrdinalObservationError):
            exact_bounded_time_horizon(())
        with self.assertRaises(OrdinalObservationError):
            exact_bounded_time_horizon((1.5,))
        with self.assertRaises(OrdinalObservationError):
            exact_bounded_time_horizon((Q(6),))

    def test_finite_ordinal_successor_preserves_source_prefix(self):
        a=OrdinalFiniteStage.genuine(5)
        b=a.successor(1)
        self.assertEqual((a.n,b.n),(5,6))
        self.assertEqual(a.source,b.source[:a.n+1])
        self.assertTrue(b.agrees_with_earlier(a))
        self.assertTrue(b.restrict(5).agrees_with_earlier(a))
        mutant=a.successor(2)
        self.assertEqual(mutant.connected_pair_curvature(2,3)[
                         "connected_second_order_residual"],Q(1))
        self.assertEqual(b.connected_pair_curvature(2,3)[
                         "connected_second_order_residual"],Q(0))
        with self.assertRaises(OrdinalObservationError):
            b.agrees_with_earlier(mutant)
        with self.assertRaises(OrdinalObservationError):
            b.successor(1.2)
        with self.assertRaises(OrdinalObservationError):
            a.connected_pair_curvature(2,3)
        with self.assertRaises(OrdinalObservationError):
            mutant.connected_pair_curvature(2,4)
        with self.assertRaises(OrdinalObservationError):
            mutant.connected_pair_curvature(2,2)

    def test_exact_semantic_Hessian_correlation_is_PSD_even_for_fake(self):
        # A physically interpretable finite log-partition has a positive
        # Hessian, including for the WRONG arithmetic source a(6)=2.
        true=OrdinalFiniteStage.genuine(6)
        src={n:1 for n in range(1,7)};src[6]=2
        fake=OrdinalFiniteStage.from_prefix(src,6)
        x=true.semantic_log_partition_hessian(2,3)
        y=fake.semantic_log_partition_hessian(2,3)
        self.assertEqual(x["Hessian_log_Z"],
                         ((Q(5,9),Q(-1,18)),(Q(-1,18),Q(2,9))))
        self.assertEqual(x["determinant"],Q(13,108))
        self.assertEqual(y["Hessian_log_Z"],
                         ((Q(24,49),Q(-1,49)),(Q(-1,49),Q(12,49))))
        self.assertEqual(y["determinant"],Q(287,2401))
        self.assertTrue(x["is_positive_semidefinite"])
        self.assertTrue(y["is_positive_semidefinite"])
        self.assertTrue(x["source_matches_zeta_prefix"])
        self.assertFalse(y["source_matches_zeta_prefix"])
        self.assertNotEqual(x["Hessian_log_Z"],y["Hessian_log_Z"])
        with self.assertRaises(OrdinalObservationError):
            fake.semantic_log_partition_hessian(2,4)
        bad={n:1 for n in range(1,7)};bad[6]=-1
        with self.assertRaises(OrdinalObservationError):
            OrdinalFiniteStage.from_prefix(bad,6).semantic_log_partition_hessian(2,3)

    def test_omega_plus_one_report_is_formal_and_has_finite_restrictions(self):
        semantics=synthetic_ordinal_semantics(20)
        self.assertTrue(semantics["report_property_is_RH_equivalent"])
        self.assertFalse(semantics["report_property_proved"])
        self.assertFalse(semantics["omega_computation_executed"])
        self.assertIn("not a largest finite",semantics["omega"])
        with mp.workdps(75):
            early=OrdinalFiniteStage.genuine(6)
            times=(Q(0),Q(1),Q(-1))
            with self.assertRaises(OrdinalObservationError):
                early.report(times,dps=75)
            stage=OrdinalFiniteStage.genuine(9)
            after=OrdinalFiniteStage.genuine(28)
            a=stage.report(times,dps=75)
            b=after.report(times,dps=75)
            self.assertEqual(a["stabilization_horizon"],9)
            self.assertEqual(a["ordinal_stage"],"finite successor n")
            self.assertFalse("report_property_proved" in a)
            self.assertEqual(a["finite_query_times"],("0","1","-1"))
            self.assertTrue(a["source_matches_zeta_prefix"])
            for i in range(3):
                for j in range(3):
                    self.assertLess(abs(a["kernel"][i][j]-b["kernel"][i][j]),
                                    mp.mpf("1e-69"))
                    self.assertLess(abs(a["kernel"][i][j]-a["kernel"][j][i]),
                                    mp.mpf("1e-70"))
            self.assertEqual(a["kernel"][0][0],0)
            self.assertIn("not observed",a["archimedean_term"])

    def test_genuine_source_reconstructs_suzuki_at_named_rational_events(self):
        with mp.workdps(72):
            a=OrdinalFiniteStage.genuine(12)
            report=a.report((Q(0),Q(1,2),Q(1)),dps=72)
            psi=a._gamma_snapshot().at_time(mp.mpf(1),dps=72)["psi"]
            self.assertLess(abs(report["kernel"][2][2]-2*psi),mp.mpf("1e-68"))
            self.assertGreater(psi,0)
            self.assertTrue(report["source_matches_zeta_prefix"])
            self.assertIn("omega+1",report["formal_report_stage"])

    def test_engine_pending_observer_is_not_integrated_source(self):
        e=Engine(arithmetic=True,limits=Limits(max_target=20))
        for n in range(1,6):
            e.advance(source_at(n),context="zeta",probe="coefficient")
        old=OrdinalFiniteStage.from_engine(e)
        self.assertEqual(old.n,5)
        e.predict(6,Scalar(2),"fictional future prime-composite")
        e.step(Scalar(2),context="test",probe="coefficient")
        still=OrdinalFiniteStage.from_engine(e)
        self.assertEqual(still.n,5)
        with self.assertRaises(OrdinalObservationError):
            OrdinalFiniteStage.from_engine(e,horizon=6)
        e.propagate()
        new=OrdinalFiniteStage.from_engine(e)
        self.assertEqual(new.n,6)
        self.assertEqual(new.head,e.head)
        self.assertTrue(new.agrees_with_earlier(old))
        self.assertEqual(new.connected_pair_curvature(2,3)[
                         "connected_second_order_residual"],Q(1))

    def test_fake_composite_second_order_arithmetic_curvature_is_suzuki_jet(self):
        N=14
        source={n:1 for n in range(1,N+1)}
        true=OrdinalFiniteStage.from_prefix(source,N)
        altered=dict(source)
        altered[6]=2
        fake=OrdinalFiniteStage.from_prefix(altered,N)
        self.assertEqual(true.connected_pair_curvature(2,3)[
                         "connected_second_order_residual"],0)
        self.assertEqual(fake.connected_pair_curvature(2,3)[
                         "connected_second_order_residual"],1)
        with mp.workdps(90):
            good=true._gamma_snapshot()
            bad=fake._gamma_snapshot()
            event=mp.log(6)
            self.assertEqual(
                good.at_event(6,dps=90)["psi"],bad.at_event(6,dps=90)["psi"])
            jump=bad.slope_jump(6,dps=90)-good.slope_jump(6,dps=90)
            self.assertLess(abs(jump+mp.log(6)/mp.sqrt(6)),mp.mpf("1e-85"))
            # The first-order observation is continuous at event 6;
            # the NEXT observation reveals a first-derivative jump.
            # Its 2nd finite difference makes the NEW interaction
            # visible as a 1/h-normalized cusp exactly.
            for h in ("0.02","0.01","0.005"):
                hh=mp.mpf(h)
                val_at=bad.at_event(6,dps=90)["psi"]-good.at_event(6,dps=90)["psi"]
                right=bad.at_time(event+hh,dps=90)["psi"]-good.at_time(
                    event+hh,dps=90)["psi"]
                left=bad.at_time(event-hh,dps=90)["psi"]-good.at_time(
                    event-hh,dps=90)["psi"]
                second=(right-2*val_at+left)/hh
                self.assertLess(abs(second-jump),mp.mpf("1e-80"))
                self.assertLess(abs(left),mp.mpf("1e-80"))
            query=Q(9,5)  # 1.8, just above log6, no next prime power
            rp=fake.report((Q(0),query),dps=90)
            rg=true.report((Q(0),query),dps=90)
            expect=-mp.log(6)/mp.sqrt(6)*(_mpq(query)-event)
            self.assertLess(abs((rp["kernel"][1][1]-rg["kernel"][1][1])/2
                                -expect),mp.mpf("1e-80"))

    def test_delayed_composite_anomaly_is_unseen_on_every_prior_window(self):
        # Both sources are known through N=64; finite observer queries
        # up to log(e^2)=2 cannot detect the fake a(15)=2. A later
        # SUCC query t=3 can, through a source-derived psi kink.
        N=64
        good={n:1 for n in range(1,N+1)}
        bad=dict(good);bad[15]=2
        a=OrdinalFiniteStage.from_prefix(good,N)
        b=OrdinalFiniteStage.from_prefix(bad,N)
        self.assertEqual(b.connected_pair_curvature(3,5)[
                         "connected_second_order_residual"],1)
        with mp.workdps(82):
            for times in (
                (Q(0),Q(1)),(Q(0),Q(1),Q(2)),
                (Q(1,4),Q(3,4),Q(3,2))
            ):
                x=a.report(times,dps=82)["kernel"]
                y=b.report(times,dps=82)["kernel"]
                for i in range(len(times)):
                    for j in range(len(times)):
                        self.assertLess(abs(x[i][j]-y[i][j]),
                                        mp.mpf("1e-77"))
            x=a.report((Q(0),Q(3)),dps=82)["kernel"][1][1]
            y=b.report((Q(0),Q(3)),dps=82)["kernel"][1][1]
            pred=-2*mp.log(15)/mp.sqrt(15)*(3-mp.log(15))
            self.assertLess(abs((y-x)-pred),mp.mpf("1e-75"))
            self.assertLess(y,x)

    def test_mixed_second_difference_of_two_observation_times_is_exact(self):
        with mp.workdps(85):
            a=OrdinalFiniteStage.genuine(27)
            t,u,h,k=Q(3,5),Q(1,5),Q(1,20),Q(1,30)
            corner=a.rectangle_increment(t,u,h,k,dps=85)
            p=a._gamma_snapshot()
            def psi(v):
                return p.at_time(abs(_float_rational(v)),dps=85)["psi"]
            direct=(psi(t+h-u)+psi(t-u-k)-psi(t+h-u-k)-psi(t-u))
            self.assertLess(abs(corner-direct),mp.mpf("1e-79"))

    def test_second_order_positive_curvature_and_positive_samples_NOT_PSD(self):
        c=quartic_observer_report()
        self.assertEqual(c["psi_at_1"],Q(1))
        self.assertEqual(c["psi_second_derivative_at_1"],Q(12))
        self.assertEqual(c["kernel"],((Q(2),Q(-14)),(Q(-14),Q(2))))
        self.assertEqual(c["determinant"],Q(-192))
        self.assertEqual(c["quadratic_vector_ones"],Q(-24))
        for den in (10,100,1000):
            r=exact_polynomial_rectangle(1,0,Q(1,den),Q(1,den))
            self.assertEqual(r["corners"],r["relative"])
            self.assertLess(abs(r["normalized"]-12),Q(30,den))

    def test_Hilbert_positive_observer_can_have_negative_curvature(self):
        with mp.workdps(82):
            model=oscillator_observer_report((Q(0),Q(1),Q(2),Q(3)),dps=82)
            self.assertLess(model["identity_error"],mp.mpf("1e-76"))
            # Psi''(pi)=-1 negative, yet the Gram kernel is PSD.
            self.assertLess(mp.cos(3),0)
            mat=model["kernel"]
            for c in ((1,1,1,1),(1,-3,2,0),(3,-2,1,4)):
                q=mp.fsum(c[i]*c[j]*mat[i][j] for i in range(4) for j in range(4))
                self.assertGreaterEqual(q,-mp.mpf("1e-77"))
            # The physical Hilbert covariance model is positive, but
            # this identifies K for 1-cos, NOT for prime/Gamma Psi.

    def test_one_prime_impulse_kernel_not_an_independent_positive_energy(self):
        with mp.workdps(85):
            a=mp.log(2);w=mp.log(2)/mp.sqrt(2)
            det=individual_impulse_determinant(a,w,dps=85)
            self.assertLess(det,0)
            self.assertLess(abs(det+(w*a/4)**2),mp.mpf("1e-78"))


def _mpq(q):
    z=Q(q)
    return mp.mpf(z.numerator)/z.denominator


def _float_rational(q):
    return _mpq(q)


if __name__=="__main__":
    unittest.main()
