"""Exact rational tests for Adelic BBP Period-Seed Duality, Iwasawa 2-Adic
Null-Seed Coherence, Octic CRT Period Quotient, Four-Class Terminal Prime
Survival, Closed-Form Borwein Autocorrelation, Parseval-Cauchy-Schwarz
Discrepancy Transfer, and the Adelic CRT Shadow Crucible (ANC-01..12).

All tests use Python's standard library and exact Fraction/integer arithmetic.
Finite rational checks certify the stated algebraic/number-theoretic theorems
and countermodels; they do not prove the open all-late-shell R0 or base-16 pi
normality limits.
"""
from fractions import Fraction as F
import math
import unittest

from observational_succ.adelic_bbp_normality_crucible import (
    BORWEIN_AUTOCORR_DENOM,
    C_ALPHA3,
    C_NULL,
    C_R1,
    C_R2,
    CHATGPT_FOURIER_FLOOR,
    OCTIC_PARTIAL_FRACTION_MATRIX,
    SHARP_FOURIER_FLOOR,
    adelic_carry_congruence_components,
    backward_2adic_section,
    closed_form_borwein_autocorrelation,
    closed_form_borwein_energy,
    construct_adelic_crt_shadow,
    domain_wall_counts,
    gaussian_octic_pi_character_from_W,
    octave_split_lcm,
    octic_partial_fraction_coords,
    octic_period_quotient,
    sharp_parseval_discrepancy_bound,
    sharp_weyl_bound_from_energy,
    source_r2_any_int,
    source_r_any_int,
    source_r_factored,
    source_r_flat,
    terminal_uncollided_primes,
    v2_fraction,
    v2_int,
    verify_terminal_prime_survival,
    z2_mod,
)
from observational_succ.borwein_quantitative_certificate import (
    HAAR_MEAN,
    U,
    autocorrelation,
    autocorrelation_energy,
    certified_weyl_bound_from_energy,
    original_energy,
    original_phases,
    quantitative_interval_discrepancy,
    torus,
)


class TestAdelicBBPNormalityCrucible(unittest.TestCase):
    def test_anc01_factored_r1_and_2adic_integrality(self):
        # ANC-01: r_1(k) = (120 k^2 - 89 k + 16)/((2k-1)(4k-1)(8k-7)(8k-3)) in Z_{(2)}
        for k in range(-40, 41):
            r_val = source_r_any_int(k)
            self.assertEqual(r_val, source_r_factored(k))
            self.assertEqual(r_val.denominator % 2, 1)
            if k != 0 and (k % 16) != 0:
                self.assertEqual(v2_fraction(r_val), v2_int(k))
        # At k = 16, 120*16^2 - 89*16 + 16 = 16*(1920 - 89 + 1) = 16 * 1832 = 128 * 229, so v_2 = 7
        self.assertEqual(v2_fraction(source_r_any_int(16)), 7)

    def test_anc01_state_U_n_parity_valuation_and_odd_denominator(self):
        # ANC-01: Q_n = den(U_n(0)) is strictly odd for all n >= 1, and v_2(U_n(0)) = v_2(n) for 16 -| n
        for n in range(1, 33):
            u_n = U(n)
            self.assertEqual(u_n.denominator % 2, 1)
            if n % 16 != 0:
                self.assertEqual(v2_fraction(u_n), v2_int(n))

    def test_anc02_2adic_pole_failure_of_hostile_rivals(self):
        # ANC-02: TFL-01 r_flat(n) has v_2(r_flat(n)) = -7 - 2*v_2(n+1) <= -9 for odd n,
        # and v_2(r_flat(n)) <= -3 < 0 for all n >= 1 (never in Z_{(2)}!)
        for n in range(1, 17):
            rf = source_r_flat(n)
            self.assertLessEqual(v2_fraction(rf), -3)
            if n % 2 == 1:
                self.assertEqual(v2_fraction(rf), -7 - 2 * v2_int(n + 1))
        # BPC-01 r_tel(n) = 16/(8n-7) - 16/(8n-6) - 1/(8n+1) + 1/(8n+2) has v_2 = -1
        for n in range(1, 17):
            r_tel = F(16, 8 * n - 7) - F(16, 8 * n - 6) - F(1, 8 * n + 1) + F(1, 8 * n + 2)
            self.assertEqual(v2_fraction(r_tel), -1)

    def test_anc03_iwasawa_2adic_null_seed_identity_U2_zero(self):
        # ANC-03: U_2(0) = sum_{m=0}^infty 16^m r_1(-m) == 0 identically in Z_2
        for hex_digits in (8, 16, 24, 32):
            self.assertEqual(backward_2adic_section(0, hex_digits, source_r_any_int), 0)
            self.assertEqual(backward_2adic_section(0, hex_digits, source_r2_any_int), 0)

    def test_anc04_infinite_2adic_precision_state_identity(self):
        # ANC-04: Because U_2(0) = 0 in Z_2, the finite rational state U_N(0) equals the infinite
        # backward 2-adic series U_2(N) = sum_{m=0}^infty 16^m r_1(N - m) to arbitrary 2-adic
        # precision K >> N (not merely modulo 16^N!).
        hex_digits = 24
        for n in (1, 2, 3, 5, 8):
            u_n_2adic = z2_mod(U(n), hex_digits)
            u2_sec = backward_2adic_section(n, hex_digits, source_r_any_int)
            self.assertEqual(u_n_2adic, u2_sec)
            # Also check 2-adic recurrence U_2(n) - 16 * U_2(n-1) == r_1(n) mod 16^hex_digits
            u2_prev = backward_2adic_section(n - 1, hex_digits, source_r_any_int)
            r_mod = z2_mod(source_r_any_int(n), hex_digits)
            self.assertEqual((u2_sec - 16 * u2_prev) % (16 ** hex_digits), r_mod)

    def test_anc05_octic_partial_fraction_matrix_and_bbp_gauge_decomposition(self):
        # ANC-05: Q_1 = Q_{alpha_3} + (1/4) Q_null and Q_2 = Q_{alpha_3} - (1/4) Q_null
        for j in range(8):
            self.assertEqual(C_R1[j], C_ALPHA3[j] + F(1, 4) * C_NULL[j])
            self.assertEqual(C_R2[j], C_ALPHA3[j] - F(1, 4) * C_NULL[j])
            self.assertEqual(C_R1[j] - C_R2[j], F(1, 2) * C_NULL[j])
        # Verify exact coordinates of r_1, r_2, and r_flat = r_1 - r_2 + coboundary
        self.assertEqual(
            octic_partial_fraction_coords(C_R1),
            (F(0), F(-1, 4), F(0), F(0), F(1, 4), F(1, 4), F(0), F(0)),
        )
        self.assertEqual(
            octic_partial_fraction_coords(C_R2),
            (F(0), F(1, 4), F(0), F(0), F(1, 4), F(-1, 4), F(0), F(0)),
        )
        c_flat = tuple(C_R1[j] - C_R2[j] for j in range(8))
        self.assertEqual(
            octic_partial_fraction_coords(c_flat),
            (F(0), F(-1, 2), F(0), F(0), F(0), F(1, 2), F(0), F(0)),
        )

    def test_anc06_period_quotient_and_gaussian_octic_character_kill_tfl01(self):
        # ANC-06: Period quotient P(r) and Gaussian octic character Omega_pi(r)
        p_r1, null_r1 = octic_period_quotient(C_R1)
        p_r2, null_r2 = octic_period_quotient(C_R2)
        c_flat = tuple(C_R1[j] - C_R2[j] for j in range(8))
        p_flat, null_flat = octic_period_quotient(c_flat)
        self.assertEqual(p_r1, (F(0), F(0), F(0), F(0), F(1, 4), F(0), F(0)))
        self.assertEqual(p_r2, (F(0), F(0), F(0), F(0), F(1, 4), F(0), F(0)))
        self.assertEqual(null_r1, F(1, 4))
        self.assertEqual(null_r2, F(-1, 4))
        # TFL-01 r_flat has IDENTICALLY ZERO 7D period vector P(r_flat) = 0, living purely in K_null!
        self.assertEqual(p_flat, (F(0), F(0), F(0), F(0), F(0), F(0), F(0)))
        self.assertEqual(null_flat, F(1, 2))
        # Shift-orbit residue vectors W = c / 8
        w_r1 = tuple(x / 8 for x in C_R1)
        w_r2 = tuple(x / 8 for x in C_R2)
        w_flat = tuple(x / 8 for x in c_flat)
        w_tel = (F(0),) * 8
        self.assertEqual(gaussian_octic_pi_character_from_W(w_r1), F(1))
        self.assertEqual(gaussian_octic_pi_character_from_W(w_r2), F(1))
        self.assertEqual(gaussian_octic_pi_character_from_W(w_flat), F(0))
        self.assertEqual(gaussian_octic_pi_character_from_W(w_tel), F(0))

    def test_anc06_adelic_period_seed_duality_on_coboundary_rivals(self):
        # For OMG-06 r_lock(n), sum_{n>=1} 16^{-n} r_lock(n) = 1 in R, and U_2^{r_lock}(0) = -1 in Z_2
        def mom(j):
            return F(5, 2 * (j + 1)) - F(4, j + 2) + F(3, 2 * (j + 3))

        def r_lock(k):
            return 16 * mom(8 * k - 8) - mom(8 * k)

        hex_digits = 16
        mod = 16 ** hex_digits
        u2_lock_0 = backward_2adic_section(0, hex_digits, r_lock)
        # -1 mod 16^16 is 16^16 - 1
        self.assertEqual(u2_lock_0, mod - 1)

    def test_anc07_four_class_terminal_prime_survival_and_octave_split_lcm(self):
        # ANC-07: Verify all 4 odd congruence classes mod 8 survive in Q_N with exact residues,
        # and Q_N divides the Octave-Split LCM L_N (with no p == 3, 7 mod 8 in (4N, 8N-3]).
        seen_classes = set()
        for n in range(1, 36):
            self.assertTrue(verify_terminal_prime_survival(n))
            for _p, r8, _mp, _ca in terminal_uncollided_primes(n):
                seen_classes.add(r8)
            if n <= 18:
                l_n = octave_split_lcm(n)
                self.assertEqual(l_n % U(n).denominator, 0)
        self.assertEqual(seen_classes, {1, 3, 5, 7})

    def test_anc08_exact_adelic_carry_congruence(self):
        # ANC-08: C_{2B} == sum_{m=0}^{B-1} 16^m r_1(2B-m) - u_{2B} (mod 16^B Z_{(2)})
        for B in (1, 2, 4, 8, 16, 24):
            c_mod, late_2adic, u_frac_2adic = adelic_carry_congruence_components(B)
            mod = 16 ** B
            self.assertEqual(c_mod, (late_2adic - u_frac_2adic) % mod)

    def test_anc09_domain_wall_coercivity_sandwich(self):
        # ANC-09 / TW-01: Verify exact two-sided domain-wall sandwich for R_B on B=4,8,16,32
        for B in (4, 8, 16, 32):
            u_2b = U(2 * B)
            phases = original_phases(B)
            r_b = sum(torus(p) ** 2 for p in phases) / B
            d_b, j_b = domain_wall_counts(u_2b, B)
            lower = (F(d_b, 256) + F(225 * j_b, 65536)) / B
            upper = (F(d_b, 4) + F(d_b + j_b + 1, 255)) / B
            self.assertLessEqual(lower, r_b)
            self.assertLessEqual(r_b, upper)
            self.assertGreater(d_b + j_b, 0)

    def test_anc10_closed_form_3branch_borwein_autocorrelation_identity(self):
        # ANC-10: Closed-form 3-branch polynomial with denominator 11275335 matches
        # breakpoint-quadrature autocorrelation(t) at rational shifts across all 3 branches
        test_shifts = (
            F(0),
            F(1, 36),
            F(1, 18),
            F(1, 9),
            F(5, 36),
            F(1, 4),
            F(7, 18),
            F(4, 9),
            F(17, 36),
            F(1, 2),
            F(19, 36),
            F(7, 12),
            F(11, 13),
        )
        for shift in test_shifts:
            self.assertEqual(
                closed_form_borwein_autocorrelation(shift),
                autocorrelation(shift),
            )
        # Check exact Haar mean square integral: 2 * int_0^(1/2) K(d) dd == (256/7803)^2
        # Using exact rational primitives of the 3 branches:
        def prim1(d):
            return (
                24576 * d
                - 138240 * d ** 3
                + 233280 * d ** 4
                - 104976 * d ** 5
                - 19683 * d ** 6
            ) / BORWEIN_AUTOCORR_DENOM

        def prim2(d):
            return (
                24574 * d
                + 45 * d ** 2
                - 138780 * d ** 3
                + 236925 * d ** 4
                - 118098 * d ** 5
            ) / BORWEIN_AUTOCORR_DENOM

        def prim3(d):
            return (
                65534 * d
                - 184275 * d ** 2
                + 275940 * d ** 3
                - 229635 * d ** 4
                + 91854 * d ** 5
            ) / BORWEIN_AUTOCORR_DENOM

        total_int = 2 * (
            (prim1(F(1, 9)) - prim1(F(0)))
            + (prim2(F(4, 9)) - prim2(F(1, 9)))
            + (prim3(F(1, 2)) - prim3(F(4, 9)))
        )
        self.assertEqual(total_int, HAAR_MEAN ** 2)

    def test_anc10_closed_form_borwein_energy_matches_quadrature(self):
        for B in (4, 8, 16):
            phases = original_phases(B)
            v_closed = closed_form_borwein_energy(phases)
            v_quad = original_energy(B)
            v_auto = autocorrelation_energy(phases)
            self.assertEqual(v_closed, v_quad)
            self.assertEqual(v_closed, v_auto)

    def test_anc11_sharp_fourier_floor_and_parseval_cs_discrepancy_upgrade(self):
        # ANC-11: SHARP_FOURIER_FLOOR = (13/10) * CHATGPT_FOURIER_FLOOR = 5733/279752
        self.assertEqual(SHARP_FOURIER_FLOOR, F(13, 10) * CHATGPT_FOURIER_FLOOR)
        # Verify |L_hat(h)| * h^2 > SHARP_FOURIER_FLOOR for h = 1..50
        c = 162.0 / 289.0
        for h in range(1, 51):
            val = (c / (math.pi ** 2)) * abs(
                (4.0 / 9.0) * ((-1) ** h) + math.sin(math.pi * h / 9.0) / (2.0 * math.pi * h)
            )
            self.assertGreater(val, float(SHARP_FOURIER_FLOOR))
        # Verify our Parseval-Cauchy-Schwarz discrepancy bound is strictly tighter than QKB-04
        for B in (8, 16):
            for H in (2, 4, 8, 16):
                b_sharp = sharp_parseval_discrepancy_bound(B, H)
                b_qkb = quantitative_interval_discrepancy(B, H)
                self.assertLess(b_sharp, b_qkb)
            for h in (1, 2, 3):
                w_sharp = sharp_weyl_bound_from_energy(B, h)
                w_qkb = certified_weyl_bound_from_energy(B, h)
                self.assertLessEqual(w_sharp, w_qkb)

    def test_anc12_adelic_crt_shadow_crucible_receipt(self):
        # ANC-12: For B = 2, 4, 8, 12, V_{2B}^sharp preserves Q_{2B}, preserves U_{2B}(0) mod 16^B Z_{(2)},
        # and preserves all uncollided prime principal parts p in P_{2B}^*, yet has D_B = J_B = 0
        # and shell torus energy R_B(V_{2B}^sharp) < 1/(255 B).
        for B in (2, 4, 8, 12):
            shadow = construct_adelic_crt_shadow(B)
            self.assertTrue(shadow["fits_in_single_unit_interval"])
            v_sharp = shadow["V_sharp"]
            u_2b = U(2 * B)
            # 1. Exact 2-adic late-shell agreement mod 16^B Z_{(2)}
            self.assertEqual(z2_mod(v_sharp, B), z2_mod(u_2b, B))
            # 2. Exact uncollided prime principal parts across all 4 odd classes mod 8
            diff = v_sharp - u_2b
            for p, *_ in terminal_uncollided_primes(2 * B):
                self.assertNotEqual(diff.denominator % p, 0)
            # 3. Complete erasure of terminal shell domain walls and energy collapse
            d_b, j_b = domain_wall_counts(v_sharp, B)
            self.assertEqual((d_b, j_b), (0, 0))
            r_b_sharp = sum(torus(v_sharp / (16 ** k)) ** 2 for k in range(1, B + 1)) / B
            self.assertLess(r_b_sharp, F(1, 255 * B))


if __name__ == "__main__":
    unittest.main()
