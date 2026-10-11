"""Discriminating tests: SUCC does not respect premature scalar path quotient.

Exact factorial/prime valuations and finite Euler data are primary. High
precision mpmath and the known functional equation are calibration/holdouts,
not sources for constructing the finite prime path. No zeros used.
"""
from fractions import Fraction
import unittest
import mpmath as mp

from observational_succ.gamma_succ_path import (
    FactorialSuccPath, MomentChannel, PrimeMomentPath, PathDomainError,
    gamma_periodic_gauge, gamma_periodic_log_curvature,
)


def as_mp(q):
    return mp.mpf(q.numerator)/q.denominator


class SuccGammaProvenanceTests(unittest.TestCase):
    def test_factorial_succ_history_and_prime_tower(self):
        for n in (2,3,5,10,20,64):
            path=FactorialSuccPath(n)
            self.assertTrue(path.verify_bridge())
            self.assertEqual(path.event_trace()[-1]["factorial_prefix"],path.endpoint())
            self.assertEqual(path.multipliers(),tuple(range(1,n+1)))
        self.assertEqual(FactorialSuccPath(10).prime_tower_exponents(),
                         ((2,8),(3,4),(5,2),(7,1)))
        self.assertEqual(FactorialSuccPath(10).endpoint(),3628800)
        # Same factorial endpoint; different word/order and SUCC history.
        self.assertNotEqual(FactorialSuccPath(5).multipliers(),
                            tuple(reversed(FactorialSuccPath(5).multipliers())))

    def test_finite_gamma_does_not_yet_satisfy_succ_ratio(self):
        for n in (2,3,10,50,256):
            path=FactorialSuccPath(n)
            for z in (1,2,3,5):
                left=path.gamma_cutoff_integer(z+1)/path.gamma_cutoff_integer(z)
                expected=path.gamma_succ_ratio(z)
                self.assertEqual(left,expected)
                self.assertEqual(Fraction(z)-left,path.gamma_boundary_defect(z))
                self.assertGreater(path.gamma_boundary_defect(z),0)
                self.assertNotEqual(left,z)
            self.assertEqual(path.gamma_cutoff_integer(2),
                             Fraction(n*n,(n+1)*(n+2)))
        for z in (1,2,3):
            defects=[FactorialSuccPath(n).gamma_boundary_defect(z)
                     for n in (2,10,50,200)]
            self.assertEqual(sorted(defects,reverse=True),defects)
            self.assertLess(defects[-1],Fraction(z*(z+1),200))

    def test_gamma_euler_limit_positive_and_complex(self):
        with mp.workdps(65):
            for z in (mp.mpf(1),mp.mpf(2),mp.mpf("1.4"),mp.mpc("1.1","0.07")):
                expected=mp.gamma(z)
                errors=[abs(FactorialSuccPath(n).gamma_euler(z,dps=65)-expected)
                        for n in (12,48,128,256)]
                self.assertLess(errors[-1],errors[0]/3,(z,errors))
                self.assertLess(errors[-1],mp.mpf("0.035"),(z,errors))

    def test_moment_two_prime_cutoff_reconstructs_pi_proxy_three(self):
        p=PrimeMomentPath.genuine(3)
        self.assertEqual(p.zeta_two_rational(),Fraction(3,2))
        self.assertEqual(p.pi_squared_proxy(),9)
        self.assertEqual(p.paths()["evaluated_ratio_at_u_1"],"1")
        self.assertEqual(p.scalar_ratio_at_one(),1)
        self.assertTrue(p.is_genuine_prefix())

    def test_pi_proxy_converges_with_proved_arithmetic_tail(self):
        with mp.workdps(75):
            previous=0
            for p in (2,3,5,7,13,37,101,257,509):
                product=PrimeMomentPath.genuine(p)
                pp=as_mp(product.pi_squared_proxy())
                self.assertGreater(pp,previous)
                self.assertLess(pp,mp.pi**2)
                self.assertGreaterEqual(as_mp(product.genuine_pi_squared_tail_bound()),
                                        mp.pi**2-pp)
                previous=pp

    def test_point_evaluation_fails_to_recover_path_jet(self):
        with mp.workdps(80):
            old=PrimeMomentPath.genuine(2)
            new=PrimeMomentPath.genuine(3)
            fake=PrimeMomentPath(3,(MomentChannel(2,Fraction(3,2)),MomentChannel(3)))
            for P in (old,new,fake):
                self.assertEqual(P.scalar_ratio_at_one(),1)
                self.assertLess(abs(P.ratio(1,dps=80)-1),mp.mpf("1e-73"))
                self.assertLess(P.first_jet(dps=80),0)
                self.assertGreater(P.second_jet(dps=80),0)
            self.assertLess(new.first_jet(dps=80),old.first_jet(dps=80))
            self.assertGreater(abs(new.first_jet(dps=80)-fake.first_jet(dps=80)),
                               mp.mpf("0.01"))
            self.assertTrue(new.is_genuine_prefix())
            self.assertFalse(fake.is_genuine_prefix())
            self.assertNotEqual(new.paths()["numerator"],new.paths()["denominator"])

            h=mp.mpf("1e-13")
            derivative=(new.ratio(1+h,dps=80)-new.ratio(1-h,dps=80))/(2*h)
            self.assertLess(abs(derivative-new.first_jet(dps=80)),mp.mpf("1e-22"))
            second=(mp.log(new.ratio(1+h,dps=80))
                    -2*mp.log(new.ratio(1,dps=80))
                    +mp.log(new.ratio(1-h,dps=80)))/h**2
            self.assertLess(abs(second-new.second_jet(dps=80)),mp.mpf("1e-20"))

    def test_fake_composite_and_nonunit_source_pass_scalar_cancel(self):
        f=PrimeMomentPath(6,(MomentChannel(2),MomentChannel(3),MomentChannel(6)))
        self.assertFalse(f.is_genuine_prefix())
        self.assertEqual(f.scalar_ratio_at_one(),1)
        self.assertNotEqual(f.paths()["numerator"],f.paths()["denominator"])
        with self.assertRaises(PathDomainError):
            f.genuine_first_jet_tail_bound()
        with self.assertRaises(PathDomainError):
            f.genuine_pi_squared_tail_bound()
        with self.assertRaises(PathDomainError):
            MomentChannel(2,Fraction(2))
        with self.assertRaises(PathDomainError):
            MomentChannel(2,1.2)

    def test_prime_jets_have_provable_global_tail(self):
        with mp.workdps(70):
            target=(2*mp.diff(mp.zeta,2)/mp.zeta(2)-mp.log(mp.zeta(2)))
            for cutoff in (3,5,17,61,257,509):
                P=PrimeMomentPath.genuine(cutoff)
                error=abs(target-P.first_jet(dps=70))
                self.assertLess(error,P.genuine_first_jet_tail_bound(dps=70))
            self.assertLess(abs(target-PrimeMomentPath.genuine(509).first_jet(dps=70)),
                            mp.mpf("0.035"))

    def test_two_finite_paths_meet_negative_one_only_in_limit(self):
        with mp.workdps(65):
            vals=[]
            for primeh,gamman in ((2,2),(3,5),(11,20),(41,64),(131,256)):
                prime=PrimeMomentPath.genuine(primeh)
                gamma=FactorialSuccPath(gamman)
                v=prime.at_u_one(gamma,dps=65)
                self.assertLess(abs(v-prime.reflected_transport(1,gamma,dps=65)),mp.mpf("1e-60"))
                self.assertNotEqual(v,mp.mpf(-1)/12)
                vals.append(abs(v+mp.mpf(1)/12))
            self.assertEqual(vals,sorted(vals,reverse=True))
            self.assertLess(vals[-1],vals[0]/20)
            self.assertLess(vals[-1],mp.mpf("0.0015"))

    def test_complex_reflection_path_recovers_safe_functional_equation(self):
        with mp.workdps(70):
            u=mp.mpc("1.18","0.07")
            truth=mp.zeta(1-2*u)
            errors=[]
            for P,N in ((3,8),(17,48),(71,128),(251,256)):
                got=PrimeMomentPath.genuine(P).reflected_transport(
                    u,FactorialSuccPath(N),dps=70)
                errors.append(abs(got-truth))
            self.assertLess(errors[-1],errors[0]/4,(errors,truth))

    def test_full_reflection_first_jet_matches_independent_zeta_derivative(self):
        # Independent analytic calibration. No RH, zeros or fitted phases.
        with mp.workdps(75):
            actual=-2*mp.diff(mp.zeta,-1)/mp.zeta(-1)
            prime=2*mp.diff(mp.zeta,2)/mp.zeta(2)-mp.log(mp.zeta(2))
            from_parts=(2*mp.digamma(2)-2*mp.log(2)-mp.log(6)+prime)
            self.assertLess(abs(from_parts-actual),mp.mpf("1e-68"))
            P=PrimeMomentPath.genuine(509)
            parts=P.reflected_log_jet_one(FactorialSuccPath(256),dps=75)
            self.assertLess(abs(parts["total"]-actual),mp.mpf("0.15"))
            self.assertLess(abs(parts["finite_prime_jet"]-prime),
                            P.genuine_first_jet_tail_bound(dps=75))
            self.assertEqual(parts["scalar_quotient_only"],1)

    def test_gamma_succ_factorial_data_do_not_select_continuation(self):
        # Periodic gauge retains all factorials and Gamma's recurrence;
        # global log-convexity rejects it (Bohr-Mollerup uniqueness).
        with mp.workdps(65):
            eps=mp.mpf(".01")
            for n in (1,2,3,6,20):
                self.assertLess(abs(gamma_periodic_gauge(n,eps,dps=65)
                                    -mp.gamma(n)),mp.mpf("1e-56"))
            for z in (mp.mpf("1.2"),mp.mpf("2.7"),mp.mpf("20.2")):
                lhs=gamma_periodic_gauge(z+1,eps,dps=65)
                rhs=z*gamma_periodic_gauge(z,eps,dps=65)
                self.assertLess(abs(lhs-rhs)/abs(rhs),mp.mpf("1e-57"))
            self.assertLess(gamma_periodic_log_curvature(
                mp.mpf("100.25"),eps,dps=65),0)
            self.assertLess(gamma_periodic_log_curvature(
                mp.mpf("100.75"),-eps,dps=65),0)
            self.assertGreater(mp.polygamma(1,mp.mpf("100.25")),0)


    def test_real_observational_succ_source_and_journal_provenance(self):
        from observational_succ import Engine, Limits, source_at
        from observational_succ.core import Scalar
        engine=Engine(arithmetic=True,limits=Limits(max_target=24))
        for k in range(1,7):
            engine.advance(source_at(k),context="zeta",probe="coefficient")
        moment=PrimeMomentPath.from_engine(engine)
        self.assertEqual(moment.horizon,6)
        self.assertEqual(moment.paths()["source_journal_head"],engine.head)
        self.assertEqual(tuple(c.base for c in moment.channels),(2,3,5))
        self.assertTrue(moment.is_genuine_prefix())
        engine.predict(7,Scalar(1),"not an observation")
        engine.step(Scalar(2),context="mutant",probe="coefficient")
        pending=PrimeMomentPath.from_engine(engine)
        self.assertEqual(pending.horizon,6)
        self.assertNotEqual(pending.source_head,moment.source_head)
        engine.propagate()
        with self.assertRaises(PathDomainError):
            PrimeMomentPath.from_engine(engine)
        with self.assertRaises(PathDomainError):
            PrimeMomentPath.from_engine(engine,horizon=8)

    def test_source_and_domain_mismatch_controls(self):
        P=PrimeMomentPath.genuine(7)
        with self.assertRaises(PathDomainError):
            P.ratio(".5")
        with self.assertRaises(PathDomainError):
            P.reflected_transport(".5",FactorialSuccPath(10))
        with self.assertRaises(PathDomainError):
            FactorialSuccPath(10).gamma_euler(-1)
        with self.assertRaises(PathDomainError):
            PrimeMomentPath(7,(MomentChannel(3),MomentChannel(2)))
        with self.assertRaises(PathDomainError):
            FactorialSuccPath(1)
        with self.assertRaises(PathDomainError):
            P.reflected_transport(1,object())


if __name__=="__main__":
    unittest.main()
