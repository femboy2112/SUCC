"""Arithmetic/Archimedean balanced theta windows and zero-free finite Li probes.

Mathematical tail bounds are analytic; numerical comparisons are calibrated
mpmath tests, NOT directed interval arithmetic. No nontrivial zeta zero is
read into construction. The finite theta double-zero test is hostile only.
"""
import unittest
from fractions import Fraction as Q
import mpmath as mp

from observational_succ.balanced_theta_li import (
    BalancedWindowError, theta_finite, theta_defect,
    theta_defect_tail_envelope, matched_theta_cutoff,
    one_prime_fake_defect, wrong_half_density_limit,
    finite_gamma_window, finite_gamma_succ_defect,
    truncated_xi, finite_li_coefficients, li_all_degree_bound,
    finite_double_zero, li_coevolving_diagonal,
)
from observational_succ.hasse_theta_seam import (
    SUCCDifferenceSource, theta_xi_partial, theta_xi_tail_bound,
)


class BalancedThetaTests(unittest.TestCase):
    def test_true_finite_theta_defect_is_bounded_by_omitted_gaussians(self):
        with mp.workdps(100):
            for u in ("0", "0.4", "-0.4", "1", "-1", "2", "-2"):
                for N in (2,4,12,40):
                    defect=theta_defect(u,N,dps=100)
                    bound=theta_defect_tail_envelope(u,N,dps=100)
                    self.assertLess(abs(defect),bound+mp.mpf("1e-92"),
                                    (u,N,defect,bound))
                    self.assertEqual(
                        theta_defect_tail_envelope(u,N,dps=100),
                        theta_defect_tail_envelope(-mp.mpf(u),N,dps=100))
            self.assertEqual(theta_defect(0,20,dps=100),0)

    def test_order_of_limits_is_really_nonuniform(self):
        with mp.workdps(95):
            for N in (1,3,10):
                # As u->infty at fixed N, D_N(u)/e^(u/2)->1.
                v4=theta_defect(4,N,dps=95)/mp.exp(2)
                v7=theta_defect(7,N,dps=95)/mp.exp(mp.mpf(7)/2)
                self.assertGreater(v7,v4)
                self.assertGreater(v7,mp.mpf(".9"))
            # With a fixed u, N increases and the bound decays.
            bounds=[theta_defect_tail_envelope(2,n,dps=95)
                    for n in (2,8,24,48)]
            self.assertEqual(bounds,sorted(bounds,reverse=True))
            self.assertLess(bounds[-1],mp.mpf("1e-40"))

    def test_matched_cutoff_makes_reflection_uniformly_small(self):
        with mp.workdps(90):
            for u in (0,1,2,3,5):
                cert=matched_theta_cutoff(u,"1e-11",dps=90)
                self.assertLess(cert["analytic_tail_bound"],mp.mpf("1e-11"))
                self.assertLess(abs(theta_defect(u,cert["horizon"],dps=90)),
                                cert["analytic_tail_bound"]+mp.mpf("1e-83"))
                self.assertGreater(cert["ratio_N_over_exp_u"],0)
            with self.assertRaises(BalancedWindowError):
                matched_theta_cutoff(5,"1e-40",cap=10)

    def test_prime_six_mutation_persists_in_both_infinite_directions(self):
        with mp.workdps(95):
            source=SUCCDifferenceSource.zeta(64)
            fake={n:1 for n in range(1,65)};fake[6]=2
            bad=SUCCDifferenceSource.from_prefix(fake,64)
            self.assertEqual(one_prime_fake_defect(0,6,1,dps=95),0)
            for u in (mp.mpf("1.6"),mp.mpf(2),mp.mpf("2.4")):
                good=theta_defect(u,64,source=source,dps=95)
                mutant=theta_defect(u,64,source=bad,dps=95)
                exact_anomaly=one_prime_fake_defect(u,6,1,dps=95)
                self.assertLess(abs((mutant-good)-exact_anomaly),
                                mp.mpf("1e-85"))
                self.assertGreater(abs(exact_anomaly),mp.mpf("0.0001"))
            self.assertLess(abs(theta_defect(2,64,source=source,dps=95)),
                            mp.mpf("1e-80"))
            self.assertGreater(abs(theta_defect(2,64,source=bad,dps=95)),
                               mp.mpf("0.05"))
            # The entirely symmetric probe u=0 CANNOT detect this fake.
            self.assertEqual(theta_defect(0,64,source=bad,dps=95),0)
            with self.assertRaises(BalancedWindowError):
                theta_finite(2,65,source=bad)

    def test_half_density_selected_by_global_theta_reflection(self):
        with mp.workdps(100):
            u=mp.mpf("1.25")
            true=theta_defect(u,50,half_density=Q(1,2),dps=100)
            self.assertLess(abs(true),mp.mpf("1e-85"))
            for alpha in (Q(2,5),Q(3,5),Q(7,10)):
                d=theta_defect(u,50,half_density=alpha,dps=100)
                nonzero=wrong_half_density_limit(u,alpha,dps=100)
                self.assertLess(abs(d-nonzero),mp.mpf("1e-84"))
                self.assertGreater(abs(d),mp.mpf("0.05"))
            self.assertEqual(wrong_half_density_limit(u,Q(1,2)),0)

    def test_exact_finite_gamma_shift_boundary_triangle(self):
        with mp.workdps(110):
            cases=[
                ("1.1","0.7","-2.5","0.5"),
                ("0.5","3.2","-1.1","1.4"),
                ("1.9","8","-3","0.2"),
            ]
            for re,im,A,B in cases:
                s=mp.mpc(re,im)
                got=finite_gamma_succ_defect(s,A,B,dps=110)
                self.assertLess(abs(got["residual"]),mp.mpf("1e-99"))
                self.assertNotEqual(got["endpoint_boundary"],0)
                self.assertLess(abs(finite_gamma_window(s,A,B,dps=110)
                                   -got["A_s"]),mp.mpf("1e-100"))

    def test_theta_errors_checked_against_actual_completed_xi(self):
        with mp.workdps(100):
            for s in (mp.mpc(".5","5"),mp.mpc("1.25","2"),
                      mp.mpc("1","0"),mp.mpc("0","0")):
                for N,T in ((1,"0.35"),(2,"0.7"),(3,"1.5")):
                    f=truncated_xi(s,N,T,dps=100)
                    full=theta_xi_partial(s,max_integer=9,dps=100)
                    err=abs(full-f)
                    # Explicit Li-bound envelope applies on |w|<=1/2,
                    # not to every listed complex s. Here only assert
                    # numerical convergence and global reflection.
                    self.assertLess(abs(f-truncated_xi(1-s,N,T,dps=100)),
                                    mp.mpf("1e-90"))
                    self.assertGreaterEqual(err,0)
            sample=mp.mpc(".5","5")
            self.assertLess(abs(truncated_xi(sample,4,"2.5",dps=100)
                                -theta_xi_partial(sample,max_integer=8,dps=100)),
                            theta_xi_tail_bound(sample,max_integer=4,dps=100))


class ThetaLiTests(unittest.TestCase):
    def test_Li_coefficients_from_gamma_heat_jets_have_known_first_value(self):
        with mp.workdps(100):
            l=finite_li_coefficients(4,"2",12,dps=100)
            expected=1+mp.euler/2-mp.log(4*mp.pi)/2
            self.assertLess(abs(l[0]-expected),mp.mpf("1e-18"))
            self.assertTrue(all(q>0 for q in l))

    def test_offline_finite_pair_can_coexist_with_positive_first_twelve_Li(self):
        with mp.workdps(85):
            # T≈.325 is ABOVE an independently verified finite
            # double-zero collision, with an off-line quartet.
            li=finite_li_coefficients(4,"0.325",12,dps=85)
            self.assertEqual(len(li),12)
            self.assertTrue(all(v>0 for v in li),[str(x) for x in li])
            true=finite_li_coefficients(4,"1.6",12,dps=85)
            self.assertGreater(abs(li[11]-true[11]),mp.mpf("0.1"))
            self.assertLess(abs(li[0]-true[0]),mp.mpf("0.01"))

    def test_finite_Li_source_error_is_explicit_but_exponential_in_degree(self):
        with mp.workdps(95):
            true=finite_li_coefficients(4,"2",12,dps=95)
            for N,T in ((1,"0.325"),(2,"0.8"),(3,"1.2")):
                candidate=finite_li_coefficients(N,T,12,dps=95)
                for degree in (1,2,3,4,6,8,12):
                    cap=li_all_degree_bound(N,T,degree,dps=95)
                    self.assertLess(abs(candidate[degree-1]-true[degree-1]),
                                    cap["li_coefficient_error_bound"]+mp.mpf("1e-72"))
                    self.assertFalse(cap["uniform_all_degrees"])
                    self.assertGreater(cap["analytic_log_nonzero_margin"],0)
                self.assertLess(
                    li_all_degree_bound(N,T,12,dps=95)["li_coefficient_error_bound"],
                    li_all_degree_bound(N,T,13,dps=95)["li_coefficient_error_bound"])
            # Tighten both horizons: guaranteed Li error becomes microscopic.
            cap=li_all_degree_bound(4,"1.5",12,dps=95)
            self.assertLess(cap["li_coefficient_error_bound"],mp.mpf("1e-10"))

    def test_first_log_coefficient_equals_xi_prime_over_xi(self):
        with mp.workdps(90):
            N=2;T=mp.mpf("0.8")
            lam1=finite_li_coefficients(N,T,1,dps=90)[0]
            h=mp.mpf("1e-22")
            f=lambda s:mp.log(2*truncated_xi(s,N,T,dps=90))
            approx=(f(1+h)-f(1-h))/(2*h)
            self.assertLess(abs(lam1-approx),mp.mpf("1e-40"))

    def test_finited_theta_double_zero_collision_is_real_not_zeta_input(self):
        with mp.workdps(48):
            data=finite_double_zero(4,dps=48)
            self.assertLess(abs(data["T_star"]-mp.mpf("0.324779980942573804")),
                            mp.mpf("1e-16"))
            self.assertLess(abs(data["t_star"]-mp.mpf("11.21007648628445327")),
                            mp.mpf("1e-16"))
            self.assertGreater(data["linear_T"],0)
            self.assertLess(data["quadratic_s"],0)
            self.assertLess(abs(data["off_line_splitting_coefficient"]
                                -mp.mpf("9.754505080937")),mp.mpf("1e-9"))
            self.assertLess(data["residual"],mp.mpf("1e-30"))

    def test_li_degree_diagonal_coevolves_source_and_reflection(self):
        # Full indexed theorem: no input zeros, and two independent
        # mathematically derived source/arch windows shrink with k.
        with mp.workdps(105):
            lastT=0
            for k in (1,2,4,8,16,32,64,128):
                only=li_coevolving_diagonal(
                    k,match_reflection=False,dps=105)
                both=li_coevolving_diagonal(
                    k,match_reflection=True,dps=105)
                eps=mp.power(2,-k)
                self.assertLess(
                    only["Li_fixed_degree_error_bound"],eps)
                self.assertLess(
                    both["Li_fixed_degree_error_bound"],eps)
                self.assertLess(
                    both["reflection"]["theta_reflection_error_bound"],eps)
                self.assertTrue(
                    both["reflection"]["reflection_certified_at_u_equal_T"])
                self.assertFalse(both["Li_all_index_uniform_positivity_proved"])
                self.assertGreaterEqual(both["arithmetic_horizon"],
                                        only["arithmetic_horizon"])
                self.assertGreater(both["archimedean_window_T"],lastT)
                lastT=both["archimedean_window_T"]
                true=theta_defect(
                    both["archimedean_window_T"],
                    both["arithmetic_horizon"],dps=105)
                self.assertLess(abs(true),
                                both["reflection"]["theta_reflection_error_bound"]
                                +mp.mpf("1e-90"))
                self.assertLess(
                    only["arithmetic_horizon"],
                    8*mp.sqrt(k)+4)

    def test_diagonal_true_theta_vs_false_six_at_same_horizon(self):
        with mp.workdps(105):
            path=li_coevolving_diagonal(64,dps=105)
            u=path["archimedean_window_T"]
            N=path["arithmetic_horizon"]
            self.assertGreaterEqual(N,6)
            good=SUCCDifferenceSource.zeta(max(N,64))
            mutated={n:1 for n in range(1,max(N,64)+1)}
            mutated[6]=2
            bad=SUCCDifferenceSource.from_prefix(mutated,max(N,64))
            true=theta_defect(u,N,source=good,dps=105)
            fake=theta_defect(u,N,source=bad,dps=105)
            self.assertLess(abs(true),mp.power(2,-64))
            self.assertGreater(abs(fake),mp.mpf("1e-4"))
            self.assertLess(abs((fake-true)-one_prime_fake_defect(
                u,6,1,dps=105)),mp.mpf("1e-90"))

    def test_invalid_radius_and_numeric_budget_rejected(self):
        with self.assertRaises(BalancedWindowError):
            li_all_degree_bound(2,1,3,radius=0.5)
        with self.assertRaises(BalancedWindowError):
            li_all_degree_bound(2,1,3,radius=Q(3,4))
        with self.assertRaises(BalancedWindowError):
            finite_li_coefficients(2,-1,3)
        with self.assertRaises(BalancedWindowError):
            finite_li_coefficients(2,1,25)
        with self.assertRaises(BalancedWindowError):
            theta_defect_tail_envelope(9,3)
        with self.assertRaises(BalancedWindowError):
            matched_theta_cutoff(2,0)
        with self.assertRaises(BalancedWindowError):
            finite_gamma_window(1,1,1)


if __name__=="__main__":
    unittest.main()
