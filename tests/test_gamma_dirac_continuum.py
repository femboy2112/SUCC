"""Source-chart, exact-rational and independent numerical Gamma-clock controls."""
from fractions import Fraction as F
import unittest

from observational_succ.gamma_dirac_continuum import (
    DiracGammaError, GammaClock, compact_comb_pairing, direct_comb,
    alias_sum, mutated_continuum,
)


class ExactCarrierTests(unittest.TestCase):
    def test_rational_test_pairing_and_Riemann_error(self):
        for q in (1, 2, 3, 4, 6, 11, 32, 100):
            p = compact_comb_pairing(q)
            self.assertEqual(p["events"], 2*q+1)
            self.assertEqual(p["integral"], F(16,15))
            self.assertLessEqual(p["absolute_error"], p["proved_error_ceiling"])
            self.assertEqual(p["raw_unscaled_sum"], p["sum"]*q)
            self.assertEqual(p["signed_error"], -F(1,15*q**4))
        self.assertEqual(compact_comb_pairing(2)["sum"], F(17,16))

    def test_mesh_and_cutoff_gates(self):
        for h in (0, -1, True, 0.25, "1/4", F(0)):
            with self.assertRaises(DiracGammaError):
                GammaClock(h)
        for kind in ("gamma", "zeta", "Gamma_R_wrong", None):
            with self.assertRaises(DiracGammaError):
                GammaClock(F(1, 2), kind)
        for q in (0, True, -1, 4097, 3.5):
            with self.assertRaises(DiracGammaError):
                compact_comb_pairing(q)
        self.assertEqual(GammaClock(F(1,3)).spacing, F(1,3))

    def test_exact_pole_lattices_and_residues(self):
        g=GammaClock(F(1,2), "Gamma")
        r=GammaClock(F(1,2), "Gamma_R")
        self.assertEqual(g.imaginary_period_pi_multiplier, 4)
        self.assertEqual(r.imaginary_period_pi_multiplier, 8)
        self.assertEqual(g.pole(1,2), {
            "real_part": -1, "imaginary_pi_multiplier": F(8),
            "residue_rational": F(-1), "residue_pi_exponent": 0,
            "genuine_continuum_pole": False, "sampling_alias": True,
        })
        self.assertEqual(r.pole(1,1)["residue_rational"],-2)
        self.assertEqual(r.pole(1,1)["residue_pi_exponent"],1)
        self.assertEqual(r.pole(2,0)["residue_rational"],1)
        self.assertTrue(r.pole(2,0)["genuine_continuum_pole"])
        for m,k in ((-1,0),(0,True),(0,100001)):
            with self.assertRaises(DiracGammaError):
                r.pole(m,k)


class AnalyticClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import mpmath
        except ImportError as exc:
            raise unittest.SkipTest("mpmath unavailable for optional research numeric tests") from exc
        cls.mp=mpmath

    def test_gamma_and_real_gamma_converge_with_analytic_bounds(self):
        mp=self.mp
        with mp.workdps(70):
            for kind,s in (("Gamma",mp.mpc('.25','4')),
                           ("Gamma_R",mp.mpc('.5','6'))):
                errors=[]
                for h in (F(1),F(1,2),F(1,4)):
                    obs=direct_comb(s,GammaClock(h,kind),left=-1000,right=70)
                    errors.append(obs["observed_absolute_error"])
                    self.assertLess(obs["observed_absolute_error"],obs["combined_upper"])
                    self.assertTrue(obs["left_tail_upper"]>0)
                    self.assertTrue(obs["right_tail_upper"]>=0)
                    self.assertFalse(obs["RH_proved"])
                self.assertLess(errors[2],errors[1])
                self.assertLess(errors[1],errors[0])
                self.assertLess(errors[2],mp.mpf('1e-11'))

    def test_poisson_two_independent_implementations(self):
        mp=self.mp
        with mp.workdps(70):
            for kind,s in (("Gamma",mp.mpc('1','2')),
                           ("Gamma_R",mp.mpc('.5','6'))):
                clock=GammaClock(F(1,2),kind)
                direct=direct_comb(s,clock,left=-1300,right=65)
                replica=alias_sum(s,clock,aliases=4)
                self.assertLess(abs(direct["clock_sum"]-replica),mp.mpf('1e-26'))

    def test_exact_periodicity_and_nonuniform_spectral_limit(self):
        mp=self.mp
        with mp.workdps(70):
            clock=GammaClock(F(1,2),"Gamma_R")
            period=mp.pi*clock.imaginary_period_pi_multiplier
            a=direct_comb(mp.mpc(1,0),clock,left=-500,right=50)
            b=direct_comb(mp.mpc(1,period),clock,left=-500,right=50)
            self.assertLess(abs(a["clock_sum"]-b["clock_sum"]),mp.mpf('1e-58'))
            self.assertGreater(abs(b["clock_sum"]-b["continuum"]),mp.mpf('0.5'))

    def test_one_sided_witness_and_source_mutations(self):
        mp=self.mp
        with mp.workdps(65):
            s=mp.mpc('.5','0')
            authentic=direct_comb(s,GammaClock(F(1,2),"Gamma_R"),left=-750,right=55)
            one_sided=mp.mpf('0.5')*mp.fsum(
                mp.exp((s/2)*n/2-mp.pi*mp.exp(mp.mpf(n)/2)) for n in range(56))
            self.assertGreater(abs(one_sided-authentic["continuum"]),mp.mpf('0.5'))
            wrong_pi=mutated_continuum(s,rate=2,slope=F(1,2))
            wrong_half=mutated_continuum(s,rate=2,slope=1)
            self.assertGreater(abs(wrong_pi-authentic["continuum"]),mp.mpf('0.1'))
            self.assertGreater(abs(wrong_half-authentic["continuum"]),mp.mpf('0.1'))
            for kwargs in ({"rate":0,"slope":F(1,2)},
                           {"rate":2,"slope":-1},
                           {"rate":0.2,"slope":F(1,2)}):
                with self.assertRaises(DiracGammaError):
                    mutated_continuum(s,**kwargs)

    def test_residue_from_independent_meromorphic_series(self):
        # Evaluate the independently derived negative-clock geometric series,
        # not the closed-form pole() metadata. There is NO direct comb at Re(s)<0.
        mp=self.mp
        h=mp.mpf('0.5')
        with mp.workdps(75):
            p=mp.mpc(-2,8*mp.pi)
            expected=-2*mp.pi
            for gap in (mp.mpf('1e-5'),mp.mpf('1e-8')):
                s=p+gap
                nonnegative=h*mp.fsum(mp.exp((s/2)*(n*h)-mp.pi*mp.exp(n*h))
                                        for n in range(35))
                negative=mp.fsum(((-mp.pi)**m/mp.factorial(m))*h
                    /mp.expm1(h*(s/2+m)) for m in range(45))
                residue_approx=gap*(nonnegative+negative)
                self.assertLess(abs(residue_approx-expected),10*gap)

    def test_negative_half_plane_not_sampled_and_spurious_zeta_poles(self):
        mp=self.mp
        clock=GammaClock(F(1,2),"Gamma_R")
        with self.assertRaises(DiracGammaError):
            direct_comb(-2,clock)
        with self.assertRaises(DiracGammaError):
            alias_sum(-2,clock)
        with self.assertRaises(DiracGammaError):
            direct_comb(100,GammaClock(F(1,2),"Gamma"),right=0)
        with mp.workdps(65):
            for m in (1,2):
                self.assertEqual(mp.zeta(-2*m),0)
                for k in (-2,-1,1,2):
                    pole=clock.pole(m,k)
                    s=mp.mpc(pole["real_part"],mp.pi*int(pole["imaginary_pi_multiplier"]))
                    # Numerical sanity only; the proof of nonvanishing uses FE + Re(1-s)>1.
                    self.assertGreater(abs(mp.zeta(s)),mp.mpf('1e-12'))


if __name__ == "__main__":
    unittest.main()
