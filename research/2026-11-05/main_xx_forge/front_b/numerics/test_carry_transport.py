"""Fast unit tests (< 60 s) for the Front B carry-transport instruments.

Run:  python test_carry_transport.py        (do NOT use python -I)
All mpmath precision is locally scoped (mp.workdps) - no global precision is ever set here.
"""
import os
import sys
import unittest
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import oracle_b as OB  # noqa: E402
import carry_transport_probe as P  # noqa: E402
import countermodel_cb3 as C  # noqa: E402

REF = P.REF_DEFAULT


class TestCalibration(unittest.TestCase):
    def test_r1_and_positivity(self):
        self.assertEqual(P.r_frac(OB.SOURCE, 1), Fraction(47, 15))
        self.assertEqual(OB.R_int(OB.SOURCE, 60, 1), 188)         # 188/60 = 47/15
        for n in range(1, 3000):
            self.assertGreater(P.r_frac(OB.SOURCE, n), 0)

    def test_green_tail_rigorous(self):
        import mpmath as mp
        LO, HI = OB.tail_intervals(300)
        for n in (1, 10, 100, 300):
            self.assertLessEqual(LO[n], HI[n])
            self.assertLess(HI[n] - LO[n], 1 << 20)                # width < 2^-380
            with mp.workdps(int(1.21 * n) + 130):
                U = Fraction(0)
                for j in range(1, n + 1):
                    U = 16 * U + P.r_frac(OB.SOURCE, j)
                ref = mp.pi * mp.mpf(16) ** (n - 1) - mp.mpf(U.numerator) / U.denominator
                lo = mp.mpf(LO[n]) / OB.SC
                hi = mp.mpf(HI[n]) / OB.SC
                self.assertTrue(lo - mp.mpf(10) ** -100 <= ref <= hi + mp.mpf(10) ** -100)
        for n in range(0, 299):                                   # 16 T_n - T_{n+1} = r(n+1)
            rl, rh = OB._r_bounds(n + 1)
            self.assertTrue(16 * LO[n] - HI[n + 1] <= rh and rl <= 16 * HI[n] - LO[n + 1])

    def test_pi_hex(self):
        h = OB.pi_hex_digits(64)
        s = "".join("0123456789abcdef"[v] for v in h)
        self.assertTrue(s.startswith("243f6a8885a308d313198a2e03707344"))


class TestCB1(unittest.TestCase):
    def test_both_oracles_zero_mismatch_and_agree(self):
        for A in (64, 173):
            dcap = P.dcap_for("source", A)
            for seed in ((0, 1), (1, 5)):
                rb = OB.IntOracle(OB.SOURCE, A, dcap, seed).run()
                ra = P.run_oracle_A(OB.SOURCE, A, dcap, seed)
                n_adm_triples = 0
                for key, v in rb.items():
                    a = ra[key]
                    self.assertEqual(a["sum_b"], v["sum_b"])
                    self.assertEqual(a["sum_delta"], Fraction(v["sum_delta_num"], v["sum_delta_den"]))
                    self.assertEqual(a["digest_b_def"], v["digest_b_def"])
                    self.assertEqual(a["digest_b_claim"], v["digest_b_claim"])
                    self.assertEqual((a["mm_b_adm"], a["mm_d_adm"]), (0, 0))
                    self.assertEqual((v["mm_b_adm"], v["mm_d_adm"]), (0, 0))
                    if v["nadm"] == A:
                        n_adm_triples += 1
                self.assertGreater(n_adm_triples, 5)
                # boundary control: first inadmissible depth does fail (identity is only claimed when S_d<1)
                dmax = max(v["d"] for v in rb.values() if v["nadm"] == A)
                bd = [v for v in rb.values() if v["d"] == dmax + 1]
                self.assertGreater(sum(v["mm_b_inadm"] for v in bd), 0)

    def test_detector_control_negated_forcing_must_fail(self):
        spec = OB.mutant_specs()["M4_negated"]
        rb = OB.IntOracle(spec, 64, 6).run()
        self.assertGreater(sum(v["mm_b_adm"] + v["mm_d_adm"] for v in rb.values()), 0)

    def test_positive_mutants_generic(self):
        for name in ("M1_pole4to5", "M2_const_1_1000", "M3_unforced"):
            spec = OB.mutant_specs()[name]
            rb = OB.IntOracle(spec, 64, P.dcap_for(name, 64)).run()
            self.assertEqual(sum(v["mm_b_adm"] + v["mm_d_adm"] for v in rb.values()), 0, name)

    def test_hand_case_plain_loops(self):
        r = lambda n: Fraction(4, 8 * n - 7) - Fraction(2, 8 * n - 4) - Fraction(1, 8 * n - 3) - Fraction(1, 8 * n - 2)
        U = [Fraction(0)]
        for n in range(1, 150):
            U.append(16 * U[-1] + r(n))
        S = lambda nn, kk: sum(16 ** (kk - j) * r(nn + j) for j in range(1, kk + 1))
        m, k, A = 2, 2, 64
        sb = 0
        for n in range(A, 2 * A):
            th = (16 ** 4 * (U[n] % 1)) % 1
            dl = (16 ** m * S(n, k)) % 1
            sb += (th + dl >= 1)
        rb = OB.IntOracle(OB.SOURCE, A, 5).run()
        self.assertEqual(sb, rb["2,2"]["sum_b"])
        self.assertEqual(sb, 8)


class TestGaugeAndCoherent(unittest.TestCase):
    def test_gauge_matches_exact_and_coherent_b_zero(self):
        A = 173
        T = C.Tails(2 * A + 400)
        Dpi = np.concatenate([[3], OB.pi_hex_digits(2 * A + 400)[:-1]]).astype(np.uint8)
        Z = C.zfloat(Dpi)
        dmax = T.dmax(A)
        rb = OB.IntOracle(OB.SOURCE, A, dmax + 2).run()
        self.assertEqual(dmax, max(v["d"] for v in rb.values() if v["nadm"] == A))
        for d in range(2, dmax + 1):
            for m in range(1, d):
                b, mg, na, nu = C.b_vector(Dpi, Z, T, A, m, d - m)
                self.assertEqual(OB.digest_bits(bytes(b.astype("uint8"))), rb["%d,%d" % (m, d - m)]["digest_b_def"])
                self.assertEqual(nu, 0)
        # coherent seed alpha = 0  (all digits zero): b == 0 and J = -avg delta
        D0 = np.zeros(2 * A + 400, dtype=np.uint8)
        Z0 = C.zfloat(D0)
        for (m, k) in ((1, 1), (2, 3), (3, 2)):
            b, mg, na, nu = C.b_vector(D0, Z0, T, A, m, k)
            self.assertFalse(b.any())
            sd = C.delta_sum_exact(T, A, m, k)
            self.assertGreater(sd, 0)
            sd_oracle = Fraction(rb["%d,%d" % (m, k)]["sum_delta_num"], rb["%d,%d" % (m, k)]["sum_delta_den"])
            self.assertLess(abs(float(sd - sd_oracle)), 1e-100)  # gauge delta sum == exact delta sum


class TestCB3Construction(unittest.TestCase):
    def test_calibrated_laws(self):
        import mpmath as mp
        for fr in (Fraction(1, 2), Fraction(2, 5), Fraction(1, 3) + Fraction(1, 7), Fraction(13, 20), Fraction(7, 10) - Fraction(1, 997)):
            with mp.workdps(C.DPS_MP):
                p = C.build_p_mp(mp, fr)
                res = C.verify_p_mp(mp, p, fr)
                self.assertLess(abs(res), mp.mpf(10) ** -30)
                self.assertEqual(p[0], mp.mpf(1) / 16)
                self.assertLess(abs(sum(p) - 1), mp.mpf(10) ** -60)
                self.assertGreaterEqual(min(p), 0)
        # non-uniform inside the bump, uniform outside
        with mp.workdps(C.DPS_MP):
            p = C.build_p_mp(mp, Fraction(1, 2))
            self.assertGreater(max(abs(x - mp.mpf(1) / 16) for x in p), mp.mpf("0.019"))
            q = C.build_p_mp(mp, Fraction(1, 5))
            self.assertEqual(max(abs(x - mp.mpf(1) / 16) for x in q), 0)

    def test_float_laws_match_mp(self):
        import mpmath as mp
        L = C.Laws(3000)
        self.assertTrue(np.all(L.PJ[:, 0] == 1 / 16))
        self.assertLess(L.float_resid_max, 1e-14)
        with mp.workdps(C.DPS_MP):
            for s in range(3):
                pm = C.build_p_mp(mp, L.bump_fr[s])
                for a in range(16):
                    self.assertLess(abs(float(pm[a]) - L.PJ[L.bump_idx[s]][a]), 1e-14)

    def test_expectation_algebra(self):
        r = C.selfcheck_cb3(nsamp=300000)
        self.assertLess(r["uniform_joint_vs_closed_form_max_diff"], 1e-14)
        self.assertLess(r["mc_max_abs_zscore"], 4.5)
        self.assertGreater(r["nonuniformity_visible_max_|exact-uniform|"], 0.01)

    def test_uniform_window_has_zero_expected_bias(self):
        A = 1024                                    # tau-window (1/16,1/4] lies outside the bump
        T = C.Tails(2 * A + 300)
        L = C.Laws(2 * A + 300)
        self.assertLess(abs(C.expectedJ(T, L, A, 3, 3)), 1e-15)


class TestThird(unittest.TestCase):
    def test_reference_module_agrees(self):
        if not os.path.isdir(REF):
            self.skipTest("reference checkout not present")
        r = P.stage_third(REF, quick=True)
        if "UNVERIFIED" in r:
            self.skipTest(r["UNVERIFIED"])
        for row in r["rows"]:
            self.assertEqual(row["J_disagreements"], 0)
            self.assertTrue(row["our_dmax_equals_ref"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
