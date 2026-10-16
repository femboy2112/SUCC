"""Fast canonical-source arithmetic checks; infinite proofs remain in the dossier."""
import unittest
from fractions import Fraction as Q

from observational_succ.unit_prime_tate_bridge import (
    UnitTateBridgeError, local_prime_occupation, prime_variance_tail_bound,
    source_prime_stage, finite_prime_current, archimedean_even_source,
    completed_tate_clock, scalar_gaussian_rescaling,
    truncated_prime_product_is_adelic_schwartz_test,
    finite_coherent_vs_diagonal_gibbs, diagonal_norm_unit,
)
from observational_succ.tate_idelic_zeta import StandardTateSource, finite_euler_stage
from observational_succ.tate_weil_distribution import TateWeilSource
from observational_succ.unit_prime_succ import prime_smooth
from observational_succ.source_weil_hierarchy import log_iv,pi_iv


class TateBridgeTests(unittest.TestCase):
    def setUp(self):
        self.src=StandardTateSource("unit-prime-tate",9)

    def test_local_geometric_distribution_normalized(self):
        for p in (2,3,5,11):
            for beta in (2,3,4):
                r=local_prime_occupation(p,beta,6)
                self.assertEqual(sum((v for _,v in r["shells"]),Q())+r["tail"],1)
                self.assertEqual(r["shells"][0][1],1-Q(1,p**beta))
                self.assertEqual(r["mean_valuation"],Q(1,p**beta-1))

    def test_fake_or_malformed_local_places(self):
        for p in (1,4,6,9,15):
            with self.subTest(p=p), self.assertRaises(UnitTateBridgeError):
                local_prime_occupation(p,2)
        with self.assertRaises(UnitTateBridgeError):
            local_prime_occupation(2,True)

    def test_prime_SUCC_matches_genuine_Tate_shells(self):
        for P in (2,3,5,11):
            r=source_prime_stage(self.src,P,2,shell_depth=3,integer_prefix=55)
            self.assertEqual((r["source_id"],r["epoch"]),("unit-prime-tate",9))
            self.assertEqual(r["unit_coefficient"],1)
            self.assertLessEqual(r["finite_shell_zeta"],r["stage_zeta"])
            self.assertEqual(r["stage_zeta"],finite_euler_stage(
                r["primes"],2,3)["complete_finite_place_product"])
            self.assertFalse(r["full_infinite_Euler_product_executed"])

    def test_mass_encloses_independent_additive_prefix(self):
        direct=sum((Q(1,n*n) for n in range(1,201)),Q())
        for P in (3,5,11):
            z0,z1=source_prime_stage(self.src,P,2)["zeta_interval"]
            self.assertLess(z0,z1)
            self.assertLessEqual(z0,direct+Q(1,200))
            self.assertLess(direct,z1)

    def test_true_prime_power_tape_and_current(self):
        r=finite_prime_current(self.src,11,2)
        lo,hi=r["full_prime_current_interval"]
        self.assertTrue(0<lo<hi)
        self.assertEqual((r["source_id"],r["epoch"]),("unit-prime-tate",9))
        jets=self.src.logarithmic_coefficients(11,2)
        self.assertNotIn(6,dict(jets["prime_power_labels"]))
        self.assertEqual(dict(jets["formal_logp_coefficients"])[2],
                         Q(1,4)+Q(1,16)+Q(1,64))

    def test_variance_rational_omitted_tail(self):
        for P in (3,5,11):
            r=finite_prime_current(self.src,P,2)
            lower,upper=r["full_prime_variance_interval"]
            self.assertTrue(0<lower<upper)
            self.assertEqual(
                upper-r["prime_occupation_variance_logH_partial"].hi,
                prime_variance_tail_bound(P,2))

    def test_arch_even_mellin_ladder_and_variance(self):
        for beta in (2,4,6,8):
            r=archimedean_even_source(self.src,beta)
            self.assertEqual(r["mellin_s_to_s_plus_2_ratio"],(Q(beta,2),-1))
            self.assertGreater(r["gamma_interval"].lo,0)
            self.assertGreater(r["arch_variance_log_abs"].lo,0)
            self.assertEqual(r["real_sign_multiplier"],2)
        with self.assertRaises(UnitTateBridgeError):
            archimedean_even_source(self.src,3)

    def test_completed_zeta_log_derivative_pole_and_basel(self):
        r=completed_tate_clock(self.src,11,2)
        self.assertEqual(r["polar_zero_modes"],(-1,1))
        self.assertGreater(r["completed_Lambda_interval"].lo,0)
        self.assertGreater(r["completed_log_norm_variance_interval"].lo,0)
        self.assertTrue(r["completed_log_derivative_interval"].lo <
                        r["completed_log_derivative_interval"].hi)
        # The polar correction 1/s+1/(s-1) at s=2 is exactly 3/2; the exact entire-xi
        # identity must hold on BOTH endpoints (exact rational translation, no rounding).
        self.assertEqual(r["entire_xi_log_derivative_interval"].lo,
                         r["completed_log_derivative_interval"].lo+Q(3,2))
        self.assertEqual(r["entire_xi_log_derivative_interval"].hi,
                         r["completed_log_derivative_interval"].hi+Q(3,2))
        # The independent classical Basel identity gives Lambda(2)=pi/6.
        expected=pi_iv()/6
        self.assertLessEqual(r["completed_Lambda_interval"].lo,expected.hi)
        self.assertGreaterEqual(r["completed_Lambda_interval"].hi,expected.lo)
        self.assertFalse(r["RH_proved"])

    def test_xi_shift_is_exact_rational_translation_not_outward_rounded(self):
        """Hostile rounding regression for the completed->entire xi log-derivative shift.

        xi'/xi(s) = Lambda'/Lambda(s) + 1/s + 1/(s-1) is an exact identity; the polar
        correction is an exact rational, so the entire-xi interval must be the completed
        interval translated by that exact rational -- both endpoints exact and the width
        preserved. A prior implementation routed the correction through the engine's
        outward-rounding addition, which floors the (off-grid, prime-denominator) lower
        endpoint below the exact value by up to one 1/SCALE grid unit. This guards
        against any reintroduction of that lossy path and pins the rounding budget.
        """
        grid=Q(1,10**32)
        for P,beta in ((11,2),(5,2),(3,4),(7,6)):
            with self.subTest(P=P,beta=beta):
                r=completed_tate_clock(self.src,P,beta)
                logder=r["completed_log_derivative_interval"]
                xi=r["entire_xi_log_derivative_interval"]
                c=Q(1,beta)+Q(1,beta-1)
                # Exact identity on BOTH endpoints, width preserved exactly.
                self.assertEqual(xi.lo,logder.lo+c)
                self.assertEqual(xi.hi,logder.hi+c)
                self.assertEqual(xi.hi-xi.lo,logder.hi-logder.lo)
                # The lossy sequential-add enclosure is a valid superset whose endpoints
                # sit outside the exact ones by strictly less than one grid unit.
                lossy=logder+c
                self.assertLessEqual(lossy.lo,xi.lo)
                self.assertLess(xi.lo-lossy.lo,grid)
                self.assertGreaterEqual(lossy.hi,xi.hi)
                self.assertLess(lossy.hi-xi.hi,grid)

    def test_scaled_real_gaussian_does_not_preserve_canonical_completion(self):
        for beta in (2,4,6):
            r=scalar_gaussian_rescaling(beta,4)
            self.assertEqual(r["new_to_canonical_Mellin_ratio"],
                             Q(4)**(-(beta//2)))
            self.assertTrue(r["prime_weights_unchanged"])
            self.assertFalse(r["standard_Fourier_self_dual"])
        self.assertTrue(scalar_gaussian_rescaling(2,1)["same_canonical_Tate_test"])

    def test_prime_prefix_is_not_additive_schwartz_source(self):
        for P in (2,11):
            self.assertFalse(truncated_prime_product_is_adelic_schwartz_test(P))

    def test_pure_diagonal_Gibbs_mutation(self):
        r=finite_coherent_vs_diagonal_gibbs(2)
        self.assertEqual(r["diagonal_probs"],(Q(4,5),Q(1,5)))
        self.assertEqual(r["pure_exchange_expectation"],Q(4,5))
        self.assertEqual(r["diagonal_Gibbs_exchange_expectation"],0)
        self.assertFalse(r["same_state_on_all_observables"])

    def test_adelic_norm_one_is_not_only_integer_unit(self):
        for n in (Q(2),Q(-7,12),Q(13,35),Q(-1)):
            self.assertEqual(diagonal_norm_unit(n),1)
        with self.assertRaises(UnitTateBridgeError):
            diagonal_norm_unit(0)

    def test_wrong_character_type_rejected(self):
        bad=TateWeilSource("chi4")
        with self.assertRaises(UnitTateBridgeError):
            source_prime_stage(bad,5,2)
        with self.assertRaises(UnitTateBridgeError):
            completed_tate_clock(bad,5,2)

    def test_source_epochs_remain_distinguishable(self):
        a=source_prime_stage(StandardTateSource("sA",0),3,2)
        b=source_prime_stage(StandardTateSource("sA",1),3,2)
        self.assertNotEqual(a["epoch"],b["epoch"])

    def test_composite_jet_is_not_independent_local_place(self):
        with self.assertRaises(ValueError):
            prime_smooth((2,3,6),60,2)

    def test_log_derivative_sign(self):
        r=finite_prime_current(self.src,2,2)
        self.assertGreater(r["prime_occupation_mean_logH_partial"].lo,0)
        actual=log_iv(2)*Q(1,3)
        self.assertEqual(actual.lo,r["prime_occupation_mean_logH_partial"].lo)
        self.assertEqual(actual.hi,r["prime_occupation_mean_logH_partial"].hi)


if __name__=="__main__":
    unittest.main()
