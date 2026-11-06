"""Front A regression tests (< 60 s). Finite checks of PROVED identities and of
the receipt; none of them bears on pi's normality."""
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path
import unittest

from mpmath import iv, mp

HERE = Path(__file__).resolve().parent
_S = importlib.util.spec_from_file_location('front_a_probe', HERE/'front_a_probe.py')
P = importlib.util.module_from_spec(_S)
_S.loader.exec_module(P)

XS = P.orbit(last=420)


def enclosure(phases, A):
    rec, lo, hi = P.clausen_record(phases, 't', A)
    return lo, hi


class FrontA(unittest.TestCase):
    def test_source_and_rational_seed_rotation(self):
        xs5 = P.orbit(last=420, seed=F(1, 5))
        for n in range(len(XS)):
            self.assertEqual(xs5[n], (XS[n]+F(1, 5)) % 1)
            for h in (1, 3, 16):
                self.assertEqual((h*xs5[n]) % 1, (h*XS[n]+F(h, 5)) % 1)

    def test_cb1_identity_zero_mismatch(self):
        A = 40
        for k in (1, 2):
            m = 1
            while P.admissible(A, m+k):
                J, mism, _ = P.carry_epoch(XS, A, m, k)
                self.assertEqual(mism, 0)
                m += 1
            self.assertGreater(m, 1)

    def test_fa1_identity_and_rc3(self):
        A = 32
        with P.local_prec():
            lo, hi = enclosure(P.exact_phases(XS, A), A)
        E, Pv = P.pair_energies(XS, A)
        self.assertLess(abs(E+(lo+hi)/2-math.log(2)/A), 1e-12)
        self.assertLessEqual(abs(Pv-E), 4*math.pi/(30*A))
        self.assertLessEqual(Pv, math.log(2)/A+4*math.pi/(30*A))   # universal upper half

    def test_coherent_band(self):
        A = 32
        with P.local_prec():
            lo, hi = enclosure(P.shifted_phases(lambda n: F(0), A), A)
        Ts = [P.green(n) for n in range(A, 2*A)]
        Delta = float(max(t[1] for t in Ts)-min(t[0] for t in Ts))
        self.assertLess(Delta, 1/(64*A*A))
        self.assertLessEqual(lo, math.log(2)+1e-15)
        self.assertGreaterEqual(hi, math.log(2)-2*math.pi**2*Delta**2)

    def test_periodic_closed_form_and_rate(self):
        lo, hi, _ = P.periodic_closed_form(F(1, 15), 1)
        self.assertTrue(lo <= math.log(2) <= hi)
        alpha, p, A = F(10, 51), 2, 32
        self.assertEqual(P.nearest_periodic(2), alpha)
        clo, chi, _ = P.periodic_closed_form(alpha, p)
        with P.local_prec():
            qlo, qhi = enclosure(P.shifted_phases(lambda n: (16**n*alpha) % 1, A), A)
        bound = 4*(p-1)*math.log(2)/A+4*math.pi*float(P.green(A)[1])
        self.assertTrue(qhi >= clo-bound and qlo <= chi+bound)
        self.assertGreater(clo, 0.5)

    def test_onesided_bernoulli_countermodel(self):
        r = P.bernoulli_onesided()
        self.assertEqual(r['min_F_minus_a_on_grid'], '0')
        self.assertGreater(float(r['abs_nu_hat_1']), 0)

    def test_receipt_reproduces(self):
        R = json.loads((HERE/'FINITE_RECEIPT.json').read_text())
        self.assertTrue(all(R['verdicts'].values()))
        self.assertEqual([r['A'] for r in R['true_seed_clausen']], list(P.PREREG_A))
        with P.local_prec():
            lo, hi = enclosure(P.exact_phases(XS, 64), 64)
        r64 = R['true_seed_clausen'][0]
        self.assertTrue(lo <= float(r64['Q_hi']) and float(r64['Q_lo']) <= hi)
        rows = P.carry_survey(XS, 173)
        self.assertEqual([(r['m'], r['k'], r['bits_sha256'], r['J']) for r in rows],
                         [(r['m'], r['k'], r['bits_sha256'], r['J']) for r in R['true_seed_carries']['173']])
        mx = max(float(r['sqrtA_absJ']) for rr in R['true_seed_carries'].values() for r in rr)
        self.assertLess(mx, 4)

    def test_precision_is_local(self):
        before_iv, before_mp = iv.prec, mp.dps
        with P.local_prec():
            self.assertEqual(iv.prec, P.PREC)
        self.assertEqual((iv.prec, mp.dps), (before_iv, before_mp))


if __name__ == '__main__':
    unittest.main()
