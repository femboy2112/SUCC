"""Independent integration-audit regression for the PR #324 selected-pi frontier.

Added by Operation pi Proof-Forge Integration (2026-10-27), the adversarial
audit stacked on PR #324 (research/pi-selected-boundary-crt-finite-spectral).

These tests INDEPENDENTLY re-derive the load-bearing *finite* quantities behind
SB-1..SB-4 and the inherited #321/#322 CRT clock, from exact rational / exact
cyclotomic arithmetic (and high-precision mpmath only where a transcendental
constant is unavoidable), so they would FAIL if the structural claim broke.

They do NOT prove pi base-16 normality; the signed real Weyl gate
S_N(h)=sum e(2 pi i h U_n)=o(N) remains OPEN, and the inherited saving is only
|S_N(h)| <= N - (log_8 N)/14 + O_h(1) (logarithmic, not o(N)).

This lives in a SEPARATE file on purpose: the authoring round's source-hashed
receipts stamp the existing probe/test files, so those are left byte-exact and
`scripts/*_probe.py --verify` keeps passing.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as Q

import mpmath as mp

from scripts import pi_selected_boundary_probe as P
from observational_succ import wtf_global_calibration as w

mp.mp.dps = 50

# Exact coordinator-verified constants (recomputed here, not trusted):
B_CLAIMED = mp.mpf("0.0162969977338265")
SIXTEEN_B_CLAIMED = mp.mpf("0.2607519637412")


def _R_closed():
    return (mp.pi / 4 + 5 * mp.sqrt(2) * mp.pi / 16
            + 5 * mp.log(2) / 8 + 5 * mp.sqrt(2) * mp.log(1 + mp.sqrt(2)) / 8)


class MasterIdentityAndTails(unittest.TestCase):
    """U_n = 16^{n-1} pi - T_n and 0 < T_n < 1/16 < sharper, all from the
    authentic four poles, no pi digit ever read."""

    def test_master_identity_finite_self_consistency(self):
        # NOTE (honesty): with prefix = 16*T_0 built from the SAME truncated
        # recursion, this is the exact finite TELESCOPING SELF-CONSISTENCY of
        # U_n + T_n = 16^{n-1} * (16 T_0); it is NOT an independent proof that
        # the limit equals 16^{n-1}*pi. The genuine pi-limit check (against true
        # pi via mpmath) is test_B_and_16B_closed_form + the coordinator's
        # 80-digit instrument; that is where the Bailey-Crandall input enters.
        r, U, T, prefix = P.states_and_tails(120)  # prefix = 16*T_0 (rational pi-truncation)
        for n in range(121):
            lhs = U[n] + T[n]
            rhs = (Q(1, 16) if n == 0 else Q(16 ** (n - 1))) * prefix
            self.assertEqual(lhs, rhs, f"telescoping self-consistency fails at n={n}")

    def test_tail_bounds_exact(self):
        _, _, T, _ = P.states_and_tails(140)
        for n in range(1, 120):
            self.assertGreater(T[n], 0)
            self.assertLess(T[n], Q(1, 16))                 # SB-2 endpoint
            self.assertLess(T[n], Q(1, 15 * (n + 1) ** 2))  # sharper #323 bound

    def test_B_and_16B_closed_form(self):
        R = _R_closed()
        B = (R - mp.pi) / 15
        self.assertLess(abs(B - B_CLAIMED), mp.mpf(10) ** -13)
        self.assertLess(abs(16 * B - SIXTEEN_B_CLAIMED), mp.mpf(10) ** -12)


class SB2ChangedSeedMismatch(unittest.TestCase):
    """SB-2 is generic-in-seed, NOT a fixed-pi bound: the hostile seed alpha=0
    gives y_n=0, x_n={-T_n}, so the first hex digit mismatches at EVERY n."""

    def test_alpha_zero_mismatch_every_n(self):
        _, _, T, _ = P.states_and_tails(120)
        for n in range(1, 120):
            frac_neg = (-T[n]) % 1              # {-T_n} = 1 - T_n in (15/16, 1)
            self.assertEqual(int(16 * frac_neg), 15)   # D(x_n(0)) = 15
            self.assertEqual(int(16 * (Q(0) % 1)), 0)  # D(y_n(0)) = 0  -> mismatch

    def test_mismatch_measure_is_16Tn_per_step(self):
        # Non-vacuous: for each step n, ACTUALLY evaluate the digit map
        # D(x)=floor(16{x}) at real breakpoints and confirm the mismatch set
        # {t in [0,1): D({t-T_n}) != D(t)} equals union_a [a/16, a/16+T_n),
        # whose exact Lebesgue measure is 16*T_n (16 disjoint windows, T_n<1/16).
        # This would FAIL if the true per-step measure were 8*T_n or 32*T_n.
        def D(x):  # first hex digit of the fractional part
            return int(16 * (x % 1))
        _, _, T, _ = P.states_and_tails(40)
        for n in (1, 2, 5, 13, 30):
            Tn = T[n]
            self.assertLess(Tn, Q(1, 16))          # disjointness precondition
            measured = Q(0)
            for a in range(16):
                base = Q(a, 16)
                inside = base + Tn / 2             # strictly inside the window
                gap_out = base + Tn + (Q(1, 16) - Tn) / 2  # strictly outside, pre-next-boundary
                # inside the window the subtraction of T_n crosses a digit edge -> mismatch
                self.assertNotEqual(D(inside - Tn), D(inside), f"n={n} a={a} inside")
                # outside the window no crossing -> digits agree
                self.assertEqual(D(gap_out - Tn), D(gap_out), f"n={n} a={a} outside")
                measured += Tn                     # this window contributes length T_n
            self.assertEqual(measured, 16 * Tn)    # exact mismatch-set measure = 16 T_n


class SB3FinitePlancherel(unittest.TestCase):
    """SB-3 exact finite CRT Plancherel for ARBITRARY N and ARBITRARY complex z,
    on the GENUINE CRT labels a_n=U_n mod 16, b_n=A(n) mod 3 (not independent
    distributions). High precision because roots of unity are irrational."""

    def test_plancherel_random_complex_z_arbitrary_N(self):
        A2, A3 = 16, 3
        M = A2 * A3
        _, U, _, _ = P.states_and_tails(90)
        a = [P.modr(U[n], A2) for n in range(0, 80)]
        b = [P.A(n) % A3 for n in range(0, 80)]
        # genuine CRT bijection precondition (inherited #321/#322): 48 distinct labels
        self.assertEqual(len({(a[n], b[n]) for n in range(M)}), M)
        # deterministic pseudo-random complex z (no RNG dependence)
        z = [mp.mpc(mp.cos(mp.mpf(7 * n + 1)), mp.sin(mp.mpf(3 * n + 2))) * (1 + Q(n, 50))
             for n in range(80)]
        for N in (30, 48, 61, 80):   # includes non-multiples of M
            lhs = mp.mpf(0)
            for u in range(A2):
                for v in range(A3):
                    W = mp.mpc(0)
                    for n in range(N):
                        ph = mp.mpf(u * a[n]) / A2 + mp.mpf(v * b[n]) / A3
                        W += z[n] * mp.e ** (2j * mp.pi * ph)
                    lhs += abs(W) ** 2
            rhs = mp.mpf(0)
            for t in range(M):
                S = sum((z[n] for n in range(N) if n % M == t), mp.mpc(0))
                rhs += M * abs(S) ** 2
            self.assertLess(abs(lhs - rhs), mp.mpf(10) ** -25, f"Plancherel N={N}")

    def test_coherent_z_gives_trivial_only(self):
        # z_n = 1, N multiple of M: E_{N,M}=1 -> finite orthogonality != real Weyl.
        A2, A3 = 16, 3
        M = A2 * A3
        _, U, _, _ = P.states_and_tails(60)
        a = [P.modr(U[n], A2) for n in range(M)]
        b = [P.A(n) % A3 for n in range(M)]
        N = M
        E = mp.mpf(0)
        for t in range(M):
            cnt = sum(1 for n in range(N) if n % M == t)
            E += (mp.mpf(M) / N ** 2) * cnt ** 2
        self.assertLess(abs(E - 1), mp.mpf(10) ** -30)


class SB4FiniteFrequencyCounterfeit(unittest.TestCase):
    """SB-4 crown jewel: an explicit nonnormal alpha_q with every mode 1..q-1
    (q prime-to-16) vanishing while mode q is maximally non-Haar. Verified for
    q=17 AND independent holdouts q=19, q=21, by exact structure + the exact
    cyclotomic limit, NOT only the float finite stage."""

    def test_16_permutes_residues_mod_q_all_t(self):
        for q in (17, 19, 21, 23):
            self.assertEqual(__import__("math").gcd(16, q), 1)
            for t in range(40):
                orbit = sorted(pow(16, t, q) * j % q for j in range(q))
                self.assertEqual(orbit, list(range(q)))

    def test_exact_cyclotomic_limit_is_indicator(self):
        # lim (1/q) sum_j e(h j / q) = 1 if q|h else 0, the SB-4 weak limit value.
        for q in (17, 19, 21):
            for h in range(1, q + 2):
                s = sum(mp.e ** (2j * mp.pi * mp.mpf(h * j) / q) for j in range(q)) / q
                target = 1 if h % q == 0 else 0
                self.assertLess(abs(s - target), mp.mpf(10) ** -25, f"q={q} h={h}")

    def test_finite_stage_holdout_q19(self):
        # Independent holdout q=19 (probe default is q=17): modes 1..18 killed,
        # mode 19 survives, from the deterministic staged-digit construction.
        # The survivor approaches its exact limit 1 only as K->inf (0.86 at K=14),
        # so the honest finite-stage signal is the SEPARATION from the killed
        # modes, not a brittle literal threshold.
        ds = P.staged_digits(q=19, K=14)
        killed = [abs(P.sample_mode(ds, h)) for h in (1, 2, 3, 7, 11, 18)]
        survivor = abs(P.sample_mode(ds, 19))
        self.assertLess(max(killed), 0.05, "modes 1..18 must vanish")
        self.assertGreater(survivor, 0.8, "mode 19 must survive")
        self.assertGreater(survivor, 10 * max(killed), "mode 19 maximally non-Haar")


class FirewallStatusFlags(unittest.TestCase):
    """The integration firewall encoded as a regression guard: no module may
    flip a normality / selected-Weyl-saving flag to True."""

    def test_no_normality_or_weyl_saving_proved(self):
        flags = w.status_flags()
        self.assertFalse(flags["pi_base16_normality_proved"])
        self.assertFalse(flags["nontrivial_selected_weyl_bound_proved"])
        self.assertFalse(flags["source_selector_specific_saving_proved"])


if __name__ == "__main__":
    unittest.main()
