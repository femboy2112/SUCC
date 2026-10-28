"""Non-vacuous integration-audit tests for PR #316 WTF global calibration.

Added by the adversarial integration audit (Operation Global WTF). The
authoring round's crown-jewel checks were VACUOUS: the countermodel test
(tests/test_wtf_global_calibration.py::test_perfect_compatibility_on_
provably_nonnormal_same_forcing_seed) only asserted the HARDCODED dict
constants (selected_digit=15, literal_carry=15, spill=0) that
coherent_changed_seed_countermodel returns as integer literals, and
expected_postselected_frame_score's tests echoed its closed form q**(m-1).
Those checks would pass even if the underlying paper claim were false.

These tests INDEPENDENTLY re-derive the load-bearing quantities from exact
rational arithmetic (no pi, no floating point) and from an exact
integer-polynomial positivity certificate, so they would FAIL if the
structural claim broke. They do NOT prove pi base-16 normality; the signed
Weyl gate S_N(h)=o(N) remains OPEN.

This lives in a SEPARATE file on purpose: the authoring round's
source-hashed receipt (research/2026-10-26/WTF_GLOBAL_CALIBRATION_RECEIPT.json)
stamps the sha256 of tests/test_wtf_global_calibration.py, so that file is
left byte-exact and `scripts/wtf_global_calibration_probe.py --verify` keeps
passing.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as Q

from observational_succ import wtf_global_calibration as w
from observational_succ.succ_internal_matrix_walk import authentic_r

# The n at which the committed receipt stamps the countermodel.
STAMPED_N = (1, 2, 3, 8, 29, 97, 257, 1024)


class CountermodelDigitCarryIndependentlyDerived(unittest.TestCase):
    """Derive j_n=15, c_(n+1)=15, spill=0 for V_n=-T_n from an exact rational
    upper bound on T_n, WITHOUT reading the module's hardcoded dict values and
    WITHOUT ever evaluating pi, then assert the module agrees.

    Exact bound: for n>=1, j>=1, m=n+j>=2, the four-pole term obeys
        0 < r(m) < 4/(8m-7)         (the three subtracted terms are positive),
    and 4/(8m-7) is strictly decreasing in m, so r(n+j) < 4/(8n+1). Hence
        0 < T_n = sum_(j>=1) 16^-j r(n+j) < (4/(8n+1)) sum_(j>=1) 16^-j
                = (4/(8n+1)) * (1/15) = 4/(15(8n+1)) =: T_upper.
    T_upper < 1/16  <=>  64 < 15(8n+1)  <=>  n >= 1.  So 0 < T_n < 1/16, giving
    V_n = -T_n in (-1/16, 0): floor(V_n) = -1, {V_n} = 1 - T_n in (15/16, 1),
    16{V_n} in (15, 16) so floor = 15 = j_n; literal carry
    c_(n+1) = floor(V_(n+1)) - 16 floor(V_n) = -1 - 16(-1) = 15; spill = 0.
    """

    def test_digit_carry_spill_derived_matches_module(self):
        for n in STAMPED_N:
            r1 = authentic_r(n + 1)
            self.assertGreater(r1, 0, f"r({n + 1}) must be positive")
            # exact per-term ceiling ingredient: r(n+1) < 4/(8n+1)
            self.assertLess(r1, Q(4, 8 * n + 1))
            t_upper = Q(4, 15 * (8 * n + 1))  # proven upper bound on T_n
            self.assertGreater(t_upper, 0)
            self.assertLess(t_upper, Q(1, 16),
                            f"T_upper(n={n}) must be < 1/16 for floor to force digit 15")
            # structural derivation from 0 < T_n < 1/16 (independent of the dict)
            floor_vn = -1
            derived_digit = 15               # floor(16 - 16 T_n), 0 < 16 T_n < 1
            derived_carry = -1 - 16 * floor_vn  # floor(V_(n+1)) - 16 floor(V_n) = 15
            derived_spill = derived_carry - derived_digit  # 0
            self.assertEqual((derived_digit, derived_carry, derived_spill), (15, 15, 0))

            d = w.coherent_changed_seed_countermodel(n)
            self.assertEqual(d["selected_digit"], derived_digit)
            self.assertEqual(d["literal_carry"], derived_carry)
            self.assertEqual(d["spill"], derived_spill)
            # both q16 compatibility projectors are 1 at this (digit, carry)
            self.assertEqual(d["full_compatibility"], w.full_projection(16, 0))
            self.assertEqual(d["primitive_compatibility"], w.primitive_projection(16, 0))
            self.assertEqual(d["full_compatibility"], 1)
            self.assertEqual(d["primitive_compatibility"], 1)
            # firewall flag must stay false
            self.assertFalse(d["pi_normality_proved"])


class ForcingUpperBoundAllM(unittest.TestCase):
    """The all-n countermodel/#313 chain rests on 0 < r(m) < 15/(64 (m-1)^2)
    for ALL m >= 2 (the module only checks it pointwise and raises otherwise).
    Prove it for all m by an exact integer-polynomial positivity certificate
    (sympy exact real roots), not by sampling.

    r(m) = A(m)/P(m) with P(m) = (8m-7)(8m-4)(8m-3)(8m-2) > 0 for m >= 2.
    Positivity:  A(m) > 0 on [2, inf).
    Upper bound: B(m) = 15 P(m) - 64 (m-1)^2 A(m) > 0 on [2, inf)
                 (equivalent to r(m) < 15/(64 (m-1)^2) since P, (m-1)^2 > 0).
    A polynomial with rational coefficients is > 0 on [2, inf) iff it has no
    real root in [2, inf) and is positive at m = 2.
    """

    def test_bound_and_positivity_for_all_m_ge_2(self):
        import sympy as sp

        m = sp.symbols("m")
        P = (8 * m - 7) * (8 * m - 4) * (8 * m - 3) * (8 * m - 2)
        A = (4 * (8 * m - 4) * (8 * m - 3) * (8 * m - 2)
             - 2 * (8 * m - 7) * (8 * m - 3) * (8 * m - 2)
             - 1 * (8 * m - 7) * (8 * m - 4) * (8 * m - 2)
             - 1 * (8 * m - 7) * (8 * m - 4) * (8 * m - 3))
        B = sp.expand(15 * P - 64 * (m - 1) ** 2 * A)

        def positive_on_from_2(expr):
            poly = sp.Poly(sp.expand(expr), m)
            no_root_ge_2 = all(bool(r < 2) for r in poly.real_roots())
            positive_at_2 = sp.Rational(expr.subs(m, 2)) > 0
            return no_root_ge_2 and positive_at_2

        self.assertTrue(positive_on_from_2(A), "r(m) > 0 for all m >= 2")
        self.assertTrue(positive_on_from_2(B), "r(m) < 15/(64(m-1)^2) for all m >= 2")

        # cross-check the symbolic r = A/P against the native authentic_r, and
        # confirm the pointwise bound the module itself enforces.
        for mm in (2, 3, 8, 30, 98, 1025):
            self.assertEqual(authentic_r(mm),
                             Q(int(A.subs(m, mm)), int(P.subs(m, mm))))
            self.assertGreater(authentic_r(mm), 0)
            self.assertLess(authentic_r(mm), Q(15, 64 * (mm - 1) ** 2))


class PostselectionInflationEnumerated(unittest.TestCase):
    """expected_postselected_frame_score(q, m) returns the closed form q**(m-1)
    and the authoring tests only echo that formula. Verify it instead by DIRECT
    enumeration of E0[(q 1_{X=a})^m] under the preset uniform null P0(X=x)=1/q.
    m=1 is a valid mean-1 e-value; m>=2 is the invalid reuse that inflates.
    """

    def test_null_expectation_enumerated(self):
        for q in (2, 3, 4, 8, 16):
            a = 0  # a PRESET frame (chosen before observing X)
            for mm in (1, 2, 3, 4):
                enum = sum(Q((q if x == a else 0) ** mm) for x in range(q)) / q
                self.assertEqual(enum, w.expected_postselected_frame_score(q, mm))
                self.assertEqual(enum, Q(q) ** (mm - 1))
            # m=1 is a genuine unit-expectation e-value; m>=2 is inflated.
            self.assertEqual(w.expected_postselected_frame_score(q, 1), 1)
            self.assertEqual(w.expected_postselected_frame_score(q, 2), q)


if __name__ == "__main__":
    unittest.main()
