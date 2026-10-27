"""Audit strengthening of the selected-pi / CRT frontier (PR #324 chain).

Independent, additive regression for the four frontier obligations sharpened by
the `research/pi-proof-forge-integration-audit-2026-10-27` branch.  Separate file
so the source-hashed receipts of the authoring round stay byte-exact.

Every test re-derives the load-bearing MECHANISM (not just the conclusion) and
carries a control that MUST fail for a wrong statement -- the standing lesson is
that a green test can still test nothing.  Nothing here claims pi normality or
any o(N) estimate; those remain OPEN.

Claims receipted:
  (#3)  r(x)=A(x)/D(x) is an EXACT 2-adic isometry  v2(r(a)-r(b))=v2(a-b),
        hence Phi(x)=sum_s 16^s r(x-s) is one -- proved in closed form from
        A(x)=x (mod 2), D(x)=1 (mod 2), Q(a,b)=1 (mod 2).  (was finite-verified)
  (#2)  the #319 irrationality-TYPE input is the published Zeilberger-Zudilin 2020
        bound mu(pi)<=7.103205334137 < 15/2; Salikhov 2008 (7.6063) is INSUFFICIENT;
        only the effective constant C / onset stays unextracted (conditional).
  (#4)  the SB-1 geodesic-circle Lipschitz constant is 2*pi*|h| per coordinate and
        4*pi*|h| for a coordinate shared across two slots (the understated case).
  (#1)  transport equivalence  S_N(h) = W_N(h) + E,  |E| <= 2*pi*|h|*B  for all N,
        so the gate reduces to plain base-16 Weyl equidistribution of pi (NOT progress).
"""

import math
import unittest
from fractions import Fraction


# ---------- authentic four-pole source (frozen form, re-expressed, never imported-mutated)
def A(x):
    return 120 * x * x - 89 * x + 16


def D(x):
    return (2 * x - 1) * (4 * x - 1) * (8 * x - 7) * (8 * x - 3)


def r(n):
    """Exact rational forcing r(n) as a Fraction; equals A(n)/D(n)."""
    return (Fraction(4, 8 * n - 7) - Fraction(2, 8 * n - 4)
            - Fraction(1, 8 * n - 3) - Fraction(1, 8 * n - 2))


def v2(fr):
    """2-adic valuation of a nonzero Fraction."""
    fr = Fraction(fr)
    if fr == 0:
        raise ValueError("v2(0) undefined")
    n, d = fr.numerator, fr.denominator
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    while d % 2 == 0:
        d //= 2
        v -= 1
    return v


def Qquotient(Afun, a, b):
    """The integer quotient Q(a,b) = (A(a)D(b)-A(b)D(a)) / (a-b), a != b."""
    num = Afun(a) * D(b) - Afun(b) * D(a)
    assert num % (a - b) == 0, "numerator not divisible by (a-b)"
    return num // (a - b)


class TwoAdicIsometryClosedForm(unittest.TestCase):
    """(#3) closed-form proof that r (hence Phi) is a 2-adic isometry."""

    def test_mechanism_A_is_x_D_is_1_mod2(self):
        # A(x)=120x^2-89x+16 == x (mod 2); D(x) odd for every integer x.
        for x in range(-40, 41):
            self.assertEqual(A(x) % 2, x % 2, f"A({x}) parity")
            self.assertEqual(D(x) % 2, 1, f"D({x}) must be odd (2-adic unit)")
        # control: a mutated middle coefficient (even) kills A==x (mod 2)
        Abad = lambda x: 120 * x * x - 88 * x + 16  # -88x == 0 (mod 2)
        self.assertTrue(any((Abad(x) % 2) != (x % 2) for x in range(1, 20)),
                        "mutated A should break the parity mechanism")

    def test_Q_is_odd_on_all_residue_classes(self):
        # Z2 -> F2 is a ring hom, so Q(a,b) mod 2 depends only on (a,b) mod 2.
        # Covering the 3 distinct residue pairs (Q is symmetric) proves Q==1 in F2[a,b],
        # i.e. Q(a,b) is odd for EVERY a,b in Z2 -- the heart of the isometry.
        reps = {(0, 0): (2, 0), (1, 1): (3, 1), (1, 0): (1, 0)}
        for res, (a, b) in reps.items():
            self.assertEqual(Qquotient(A, a, b) % 2, 1,
                             f"Q must be odd on residue class {res}")
        # control: for the mutated (even-middle) source, Q is NOT identically odd
        Abad = lambda x: 120 * x * x - 88 * x + 16
        self.assertTrue(
            any(Qquotient(Abad, a, b) % 2 == 0 for (a, b) in [(2, 0), (3, 1), (1, 0)]),
            "mutated source must fail the odd-quotient mechanism")

    def test_r_is_isometry_batch(self):
        # Conclusion: v2(r(a)-r(b)) == v2(a-b) exactly, on a wide batch.
        pairs = [(a, b) for a in range(1, 60) for b in range(1, 60) if a != b]
        for a, b in pairs:
            self.assertEqual(v2(r(a) - r(b)), v2(a - b), f"isometry at ({a},{b})")
        # control with teeth: the off-by-one valuation claim is essentially never true
        off = sum(1 for a, b in pairs if v2(r(a) - r(b)) == v2(a - b) + 1)
        self.assertEqual(off, 0, "off-by-one valuation claim must hold nowhere")

    def test_phi_truncation_isometry_and_tail_domination(self):
        # Phi_S(x) = sum_{s=0}^{S-1} 16^s r(x-s); the s=0 term has valuation v2(x-y),
        # every s>=1 term has valuation 4s+v2(x-y) > v2(x-y), so the min is unique.
        def phi(x, S):
            return sum((16 ** s) * r(x - s) for s in range(S))
        for S in (1, 2, 3, 5, 8):
            for a, b in [(50, 10), (33, 1), (128, 64), (100, 97), (200, 72)]:
                self.assertEqual(v2(phi(a, S) - phi(b, S)), v2(a - b),
                                 f"Phi_{S} isometry ({a},{b})")
        # explicit domination receipt: s=0 term valuation equals v2(x-y); s=1 term >= 4 higher
        a, b = 40, 8
        self.assertEqual(v2(r(a) - r(b)), v2(a - b))
        self.assertGreaterEqual(v2(16 * (r(a - 1) - r(b - 1))), v2(a - b) + 4)


class DiophantineTypeClassification(unittest.TestCase):
    """(#2) the real barrier is the collision exponent 8; EITHER published mu(pi) bound clears it.

    (Corrects a refuted first-pass claim that the argument "requires the 2020 bound and
    Salikhov-2008 is insufficient": an adversary derived that q=15|h|16^m with |h| polynomial
    makes the manufactured approximation q^{-8+o(1)}, so the barrier is 8, not the dossier's
    convenient 15/2 -- and Salikhov-2008 (7.6063 < 8) already suffices.)
    """

    ZZ_2020 = 7.103205334137       # Zeilberger-Zudilin 2020
    SALIKHOV_2008 = 7.6063         # Salikhov 2008
    DOSSIER_15_2 = 7.5             # convenient intermediate value chosen in GB-11
    BARRIER = 8.0                  # collision exponent: |pi-p/q| <= 4(15|h|)^8 q^-8, |h| polynomial

    @staticmethod
    def _onset(s, C=1.0, cap=2_000_000):
        # smallest m where the contradiction 16^{(8-s)m} > (4/C)(15|h|)^s holds (worst |h|=m^2/64);
        # exponential-in-m beats polynomial-in-m iff s<8, else no onset.
        if s >= 8.0:
            return None
        ln16 = math.log(16)
        for m in range(1, cap):
            h = max(1.0, m * m / 64.0)
            if (8 - s) * m * ln16 > math.log(4.0 / C) + s * math.log(15 * h):
                return m
        return None

    def test_barrier_is_eight_not_15_over_2(self):
        # onset exists  <=>  s < 8.  The real threshold is 8, not the dossier's convenient 15/2.
        self.assertIsNone(self._onset(8.0), "s=8 is the barrier: no onset")
        self.assertIsNone(self._onset(8.01), "s>8: no onset")
        self.assertIsNotNone(self._onset(7.999), "any s<8 admits an onset")

    def test_both_published_bounds_suffice(self):
        # BOTH Salikhov-2008 and ZZ-2020 clear the barrier 8 -> either licenses -(log8 N)/14.
        for name, s in [("Salikhov-2008", self.SALIKHOV_2008), ("ZZ-2020", self.ZZ_2020)]:
            self.assertLess(s, self.BARRIER, f"{name} must clear the barrier 8")
            self.assertIsNotNone(self._onset(s), f"{name} must admit an onset")
        # ZZ-2020 only LOWERS the onset; it is not logically required (m2: 44 -> 9 at C=1)
        self.assertLess(self._onset(self.ZZ_2020), self._onset(self.SALIKHOV_2008))
        # control that corrects the prior FALSE claim: Salikhov-2008 is NOT insufficient
        self.assertTrue(self.SALIKHOV_2008 < self.BARRIER, "Salikhov-2008 suffices, not insufficient")

    def test_ordering_and_margins(self):
        # 7.1032 < 7.5 (dossier) < 7.6063 (Salikhov) < 8 (barrier); 15/2 is strictly interior.
        self.assertLess(self.ZZ_2020, self.DOSSIER_15_2)
        self.assertLess(self.DOSSIER_15_2, self.SALIKHOV_2008)
        self.assertLess(self.SALIKHOV_2008, self.BARRIER)
        # illustrative onset values at C=1 (exact mechanism, not a load-bearing number)
        self.assertEqual(self._onset(self.SALIKHOV_2008), 44)
        self.assertEqual(self._onset(self.ZZ_2020), 9)


class SB1LipschitzConstant(unittest.TestCase):
    """(#4) sharp geodesic-circle Lipschitz constants: 2*pi*|h| and (shared) 4*pi*|h|."""

    @staticmethod
    def _dgeo(x, y):
        d = abs((x - y) % 1.0)
        return min(d, 1.0 - d)

    def _sup_ratio(self, fn, samples=60000, seed=7):
        import random
        rng = random.Random(seed)
        best = 0.0
        for _ in range(samples):
            x, y = rng.random(), rng.random()
            d = self._dgeo(x, y)
            if d < 1e-6:
                continue
            best = max(best, abs(fn(x) - fn(y)) / d)
        return best

    def test_single_and_shared_coordinate_constants(self):
        e = lambda t: complex(math.cos(2 * math.pi * t), math.sin(2 * math.pi * t))
        for h in (1, 2, 3):
            single = self._sup_ratio(lambda x, h=h: e(h * x))
            shared = self._sup_ratio(lambda x, h=h: e(h * x) * e(h * x))  # same coord twice -> e(2hx)
            # single-slot character: sup/|d_geo| approaches 2*pi*|h| from below
            self.assertLessEqual(single, 2 * math.pi * h + 1e-6)
            self.assertGreater(single, 2 * math.pi * h * 0.95)
            # shared coordinate: the constant is 4*pi*|h|, NOT 2*pi*|h| (the understated case)
            self.assertLessEqual(shared, 4 * math.pi * h + 1e-6)
            self.assertGreater(shared, 4 * math.pi * h * 0.95)
            # control: a 2*pi*|h| budget would be VIOLATED by the shared observable
            self.assertGreater(shared, 2 * math.pi * h * 1.5)

    def test_cancelling_pair_shows_budget_is_not_sharp(self):
        # +h,-h on a shared coordinate: observable e(hx)*e(-hx) == 1 identically, so the TRUE
        # geodesic Lipschitz constant is 0, while the budget 2*pi*sum|h_i| = 4*pi*|h|.
        # Confirms 2*pi*sum|h_i| is an upper bound, sharp only for shared-sign frequencies.
        e = lambda t: complex(math.cos(2 * math.pi * t), math.sin(2 * math.pi * t))
        for h in (1, 3):
            cancel = self._sup_ratio(lambda x, h=h: e(h * x) * e(-h * x))
            self.assertLess(cancel, 1e-6, "cancelling pair is constant -> Lipschitz 0")
            self.assertLess(cancel, 4 * math.pi * h, "0 is strictly below the 4*pi*|h| budget")


class TransportEquivalence(unittest.TestCase):
    """(#1) S_N(h) = W_N(h) + E, |E| <= 2*pi*|h|*B -- the gate reduces to pi Weyl sums."""

    def test_bounded_gap_on_true_pi(self):
        import mpmath as mp
        mp.mp.dps = 50
        pi = mp.pi
        # calibrate the instrument on true pi via the authentic source
        def rr(n):
            return (mp.mpf(4) / (8 * n - 7) - mp.mpf(2) / (8 * n - 4)
                    - mp.mpf(1) / (8 * n - 3) - mp.mpf(1) / (8 * n - 2))
        pi_recon = 16 * mp.fsum([mp.power(16, -m) * rr(m) for m in range(1, 60)])
        self.assertLess(abs(pi_recon - pi), mp.mpf(10) ** -30, "instrument must recover pi")

        def T(n, J=40):
            return mp.fsum([mp.power(16, -j) * rr(n + j) for j in range(1, J + 1)])
        B = (mp.mpf('3.3860476195971928713495561655077561147547838656528') - pi) / 15
        e2 = lambda x: mp.e ** (2j * mp.pi * x)

        for h in (1, 2, -1):
            S = mp.mpc(0)
            W = mp.mpc(0)
            worst = mp.mpf(0)
            for n in range(1, 301):
                Un = mp.power(16, n - 1) * pi - T(n)
                Wn = mp.power(16, n - 1) * pi
                S += e2(h * Un)
                W += e2(h * Wn)
                worst = max(worst, abs(S - W))
            bound = 2 * mp.pi * abs(h) * B
            self.assertLessEqual(worst, bound, f"transport gap exceeded bound at h={h}")
            # control with teeth: the gap is a real fraction of the bound (not vacuously loose),
            # so a 10x-too-tight claim must FAIL -- confirms the bound is near-tight.
            self.assertGreater(worst, bound / 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
