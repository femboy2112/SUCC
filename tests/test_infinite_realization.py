"""Infinite realization vs finite observation: exact tests and hostile controls.

Independent mpmath readings calibrate certified rational Taylor bounds;
zero locations are never inputs and no numerical RH conclusion is drawn.
"""
import unittest
from fractions import Fraction as Q
import mpmath as mp

from observational_succ.infinite_realization import (
    LCMIndRealization, RationalEnclosure, e_enclosure, pi_enclosure,
    zeta_euler_enclosure, escaping_defect_form, escaping_defect_limit, pinned_negative_form,
)
from observational_succ.arithmetic import factorization
from observational_succ.core import BudgetExceeded, DomainError
from observational_succ.gamma_interferometer import GammaInterferometer


def real_fraction(v):
    return mp.mpf(v.numerator) / v.denominator


class InfiniteRealizationTests(unittest.TestCase):
    def setUp(self):
        self.path = LCMIndRealization()

    def test_stagewise_ind_yoneda_representability_escape(self):
        # Finite representables exhaust all probes but no finite object is terminal.
        for stage in [1, 2, 3, 4, 5, 8, 12, 25, 96]:
            self.assertTrue(all(self.path.observed_probe(stage, j)
                                for j in range(1, stage+1)))
            self.assertTrue(self.path.verify_compatibility(stage, min(stage+3, 10000)))
            missed = self.path.first_missed_prime_power(stage)
            self.assertGreater(missed, stage)
            self.assertEqual(len(factorization(missed)), 1)
            self.assertFalse(self.path.hypothetical_probe(stage, missed))
            self.assertTrue(self.path.hypothetical_probe(missed, missed))
            self.assertTrue(all(self.path.hypothetical_probe(stage, j)
                                for j in range(1, missed)))
        for m in (1, 2, 6, 60, 2520, 9999):
            j = self.path.nonrepresentability_witness(m)
            self.assertEqual(j, m+1)
            self.assertNotEqual(m % j, 0)
            self.assertTrue(self.path.hypothetical_probe(
                self.path.activation_stage(j), j))

    def test_structural_shadow_vs_observation(self):
        # 12 is not encountered at N=4, but its divisibility structure is online.
        self.assertEqual(self.path.activation_stage(12), 4)
        self.assertTrue(self.path.hypothetical_probe(4, 12))
        with self.assertRaises(BudgetExceeded):
            self.path.observed_probe(4, 12)
        # At stage 3, full previous probes cannot distinguish L_3=6 and L_4=12.
        for j in (1,2,3):
            self.assertEqual(self.path.hypothetical_probe(3,j),
                             self.path.hypothetical_probe(4,j))
        self.assertFalse(self.path.hypothetical_probe(3,4))
        self.assertTrue(self.path.hypothetical_probe(4,4))

    def test_ind_limit_is_a_theorem_about_infinitely_many_finite_probes(self):
        report=self.path.limit_profile([6,12,30,64,81])
        self.assertEqual(report["joint_eventual_stage"],81)
        self.assertTrue(report["all_true_from_that_stage"])
        self.assertFalse(report["represented_by_finite_integer"])
        self.assertTrue(all(self.path.hypothetical_probe(81,j)
                            for j in report["queries"]))
        with self.assertRaises(BudgetExceeded):
            self.path.limit_profile([])
        with self.assertRaises(DomainError):
            self.path.verify_compatibility(4,3)

    def test_e_rational_cauchy_bounds(self):
        with mp.workdps(140):
            truth=mp.e
            previous=None
            for n in range(0,27):
                I=e_enclosure(n)
                self.assertLess(real_fraction(I.lower),truth)
                self.assertGreater(real_fraction(I.upper),truth)
                if previous is not None:
                    self.assertTrue(I.nested_in(previous), n)
                    self.assertLess(I.width, previous.width)
                previous=I
            self.assertLess(e_enclosure(23).width,Q(1,10**20))

    def test_pi_rational_cauchy_bounds_machin(self):
        with mp.workdps(140):
            previous=None
            for n in range(0,22):
                I=pi_enclosure(n)
                self.assertLess(real_fraction(I.lower),mp.pi)
                self.assertGreater(real_fraction(I.upper),mp.pi)
                if previous is not None:
                    self.assertTrue(I.nested_in(previous),n)
                    self.assertLess(I.width,previous.width)
                previous=I
            self.assertLess(pi_enclosure(16).width,Q(1,10**20))

    def test_safe_euler_zeta_bounds(self):
        with mp.workdps(130):
            for s in (2,3,5):
                previous=None
                for n in (1,2,3,5,10,30,60):
                    I=zeta_euler_enclosure(n,s)
                    self.assertLess(real_fraction(I.lower),mp.zeta(s))
                    self.assertGreater(real_fraction(I.upper),mp.zeta(s))
                    if previous:
                        self.assertTrue(I.nested_in(previous))
                    previous=I

    def test_escape_negative_at_each_finite_stage_positive_in_limit(self):
        # Explicit exact finite calculations, plus elementary universal proof
        # for all finitely supported vectors: once N>max support, defect is 0.
        for n in (1,2,3,4,8,17,1000):
            self.assertEqual(escaping_defect_form(n,{n:Q(1)}),-1)
        fixed={1:Q(2),3:Q(3,5),8:Q(-7,10)}
        target,last=escaping_defect_limit(fixed)
        self.assertEqual(last,9)
        self.assertGreater(target,0)
        for n in (9,10,20,1500):
            self.assertEqual(escaping_defect_form(n,fixed),target)
        self.assertNotEqual(escaping_defect_form(8,fixed),target)
        self.assertEqual(escaping_defect_limit({}),(Q(0),1))

    def test_late_fake_can_hide_from_each_chosen_finite_prefix(self):
        # Predeclared: a fake NON-prime-power event after the fixed wavefront
        # leaves every earlier coefficient and Gamma readout intact, yet with
        # sufficient amplitude it can force a negative *artificial* Psi later.
        # This does not construct a genuine Hecke/DH L-function or disprove RH.
        with mp.workdps(75):
            for horizon in (5, 11, 16):
                m=horizon+1
                while len(factorization(m)) == 1:
                    m+=1
                self.assertGreater(m,horizon)
                intact={n:1 for n in range(1,m+2)}
                fake=dict(intact)
                fake[m]=100001
                base=GammaInterferometer.from_prefix(intact,m+1)
                mutant=GammaInterferometer.from_prefix(fake,m+1)
                older=GammaInterferometer.from_prefix(intact,horizon)
                self.assertEqual(base.connected[2:horizon+1],
                                 mutant.connected[2:horizon+1])
                self.assertEqual(older.at_event(horizon)["psi"],
                                 base.at_event(horizon)["psi"])
                self.assertEqual(base.at_event(m)["psi"],
                                 mutant.at_event(m)["psi"])
                self.assertEqual(mutant.connected[m]-base.connected[m],100000)
                observed=(mutant.at_event(m+1,dps=75)["psi"]
                          -base.at_event(m+1,dps=75)["psi"])
                exact=(-mp.mpf(100000)*mp.log(m)/mp.sqrt(m)
                       *mp.log(mp.mpf(m+1)/m))
                self.assertLess(abs(observed-exact),mp.mpf("1e-66"))
                self.assertLess(mutant.at_event(m+1,dps=75)["psi"],0)


    def test_persistent_vs_escaping_negative_mode_distinguishes_limits(self):
        # Both source families have a negative eigenvalue at EVERY N, but
        # only the escaping family becomes PSD on each fixed finite support.
        for n in (1,2,3,4,8,30):
            basis={n:Q(1)}
            self.assertEqual(escaping_defect_form(n,basis),-1)
            self.assertEqual(pinned_negative_form(n,{1:Q(1)}),-1)
        self.assertEqual(escaping_defect_limit({1:Q(1)}),(Q(1),2))
        self.assertEqual(escaping_defect_form(30,{1:Q(1)}),1)
        self.assertEqual(pinned_negative_form(30,{1:Q(1)}),-1)
        self.assertEqual(pinned_negative_form(30,{30:Q(1)}),1)

    def test_actual_suzuki_response_eventually_stabilizes_pointwise(self):
        # Not just approximate: after an event has entered the source
        # window, future *zeta* events make zero contribution at that time.
        # This does NOT yield global sign certification.
        with mp.workdps(65):
            source={n:1 for n in range(1,50)}
            global_fixed=GammaInterferometer.from_prefix(source,49)
            for event in (2,3,4,6,8,13,16):
                prefix=GammaInterferometer.from_prefix(source,event)
                a=prefix.at_event(event,dps=65)
                b=global_fixed.at_event(event,dps=65)
                self.assertEqual(a["psi"],b["psi"])
                self.assertEqual(a["finite"],b["finite"])
                self.assertEqual(a["active_channels"],b["active_channels"])
                with self.assertRaises(Exception):
                    prefix.at_event(event+1)

    def test_negative_inputs_rejected(self):
        with self.assertRaises(DomainError):
            e_enclosure(1.0)
        with self.assertRaises(BudgetExceeded):
            pi_enclosure(65)
        with self.assertRaises(BudgetExceeded):
            zeta_euler_enclosure(10,1)
        with self.assertRaises(DomainError):
            RationalEnclosure(Q(2),Q(1),"inverse")
        with self.assertRaises(DomainError):
            escaping_defect_form(3,{1:1.1})
        with self.assertRaises(BudgetExceeded):
            self.path.hypothetical_probe(5,1_000_001)


if __name__=="__main__":
    unittest.main()
