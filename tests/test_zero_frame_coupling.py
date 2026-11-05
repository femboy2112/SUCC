"""Source-exact and hostile controls for the additive zero-frame instrument."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research/2026-11-04/zero_frame_coupling"
sys.path.insert(0, str(RESEARCH))
import coupling_probe as c
import certified_phase as p


class ZeroFrameCoupling(unittest.TestCase):
    def test_unwrapped_source_and_independent_LCM(self):
        (U, Y, Z), audit = c.states(86)
        self.assertEqual(U[0], 0)
        self.assertGreater(U[-1], 16**80)
        self.assertLess(Z[-1], F(1, 32*86))
        self.assertEqual(U[-1], Y[-1]+Z[-1])
        self.assertEqual(audit["reconciled_unwrapped_states"], 258)
        self.assertEqual(len(audit["literal_carries"]), 86)

    def test_symbolic_polynomial_source_identity(self):
        import sympy as s
        n = s.symbols("n")
        ro = 4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
        rr = sum(s.Rational(q.numerator, q.denominator)/(8*(n-1)+j)
                 for j, q in enumerate(c.RAD, 1))
        opoly = (120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        rpoly = -2*(30720*n**6-93952*n**5+111840*n**4-65764*n**3+19857*n*n-2848*n+144)/((2*n-1)*(4*n-3)*(4*n-1)*(8*n-7)*(8*n-5)*(8*n-3)*(8*n-1))
        self.assertEqual(s.cancel(ro-opoly), 0)
        self.assertEqual(s.cancel(rr-rpoly), 0)

    def test_seed_one_fifth_is_rotation_not_cancellation_control(self):
        (U, Y, Z), _ = c.states(53)
        for n in (1, 17, 51):
            for lag in (0, 1, 2):
                for H in (-7, 1, 16, 65536):
                    shift = H*((Y[n]+F(16**n, 5)+Z[n+lag])-(Y[n]+Z[n+lag]))
                    self.assertEqual(shift % 1, F(H, 5) % 1)

    def test_radix_link_twist_and_wrong_frequency(self):
        (_, _, Z), _ = c.states(9)
        def D(a, b, h):
            return h*(Z[b]-16**(b-a)*Z[a])
        self.assertEqual(D(2, 9, 7), D(5, 9, 7)+D(2, 5, 16**4*7))
        self.assertNotEqual((D(2, 9, 7)-D(5, 9, 7)-D(2, 5, 7)) % 1, 0)

    def test_jet_generation_independent_from_moment_oracle(self):
        path = ROOT / "tests/test_source_jet_transport.py"
        spec = importlib.util.spec_from_file_location("parent_jet_oracle", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for m in range(1, 7):
            self.assertEqual(c.jet_weights(m), module.solve(m))
        self.assertEqual(c.radial_coefficients(4)[1:],
                         [F(1, 32), -F(5, 256), F(27, 2048), -F(209, 16384)])

    def test_certified_phase_independent_high_precision(self):
        import mpmath as mp
        with mp.workdps(90):
            for phase in (F(0), F(1, 4), -F(7, 19), F(10**500+23, 71)):
                a, b = p.character_grid(phase)
                q = phase % 1
                expected = mp.exp(2j*mp.pi*mp.mpf(q.numerator)/q.denominator)
                actual = mp.mpc(mp.mpf(a)/p.OUTPUT, mp.mpf(b)/p.OUTPUT)
                self.assertLess(abs(actual-expected), mp.mpf(1)/2**50)

    def test_huge_lift_invariance_and_cayley_failure(self):
        q = F(7, 19)
        self.assertEqual(p.character_grid(q), p.character_grid(q+10**500))
        def cayley_real(x):
            return (1-x*x)/(1+x*x)
        self.assertNotEqual(cayley_real(q), cayley_real(q+1))

    def test_true_critical_depth_and_invalid_domain(self):
        self.assertEqual(p.critical_schedule(128, 1), (4, 65536))
        self.assertEqual(p.critical_schedule(512, -3), (4, 196608))
        with self.assertRaises(ValueError):
            p.critical_schedule(307, 1)
        with self.assertRaises(ValueError):
            p.critical_schedule(128, 0)

    def test_maximal_window_not_full_window(self):
        pts = [(p.OUTPUT, 0), (p.OUTPUT, 0), (-p.OUTPUT, 0), (-p.OUTPUT, 0)]
        r = c.summary(pts, F(0), 4)
        self.assertEqual(r["signed_mean_grid"], ["0", "0"])
        self.assertEqual(F(r["M_interval"][0]), F(1, 2))
        self.assertEqual(r["chords"], 10)

    def test_exact_carry_mutant_is_phase_invisible_but_source_invalid(self):
        (U, _, _), _ = c.states(7)
        mutant = U.copy()
        mutant[5] += 1
        self.assertEqual((mutant[5]-U[5]) % 1, 0)
        self.assertNotEqual(mutant[5]-16*mutant[4], c.forcing(5))
        self.assertNotEqual(mutant[6]-16*mutant[5], c.forcing(6))

    def test_complete_factorial_and_known_interaction(self):
        rows = []
        for mask in range(16):
            rows.append({"signed_mean_grid": [str(int(bool(mask & 1) and bool(mask & 4))), "0"],
                         "complex_error": "0"})
        terms = {r["mask"]: r for r in c.factorial_contrasts(rows)}
        self.assertEqual(terms[5]["signed_grid"], ["1", "0"])
        self.assertTrue(all(v["signed_grid"] == ["0", "0"] for k, v in terms.items() if k != 5))

    def test_small_full_design_and_coherent_enclosure(self):
        raw = []
        row = c.run_case(8, 16, "test_only", c.states(17), raw)
        self.assertEqual(len(row["factor_cells"]), 16)
        self.assertEqual(len(row["complete_mixed_differences"]), 15)
        anti = next(x for x in row["controls"] if x["kind"] == "anti_companion")
        self.assertLessEqual(F(anti["M_interval"][0]), 1)
        self.assertGreaterEqual(F(anti["M_interval"][1]), 1)


if __name__ == "__main__":
    unittest.main()
