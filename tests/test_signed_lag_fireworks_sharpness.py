"""Finite rational checks for the coherent-seed sharpness theorem."""
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT/'research/2026-10-31/signed_lag_fireworks'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S = load('fireworks_sharpness', DOSSIER/'sharpness.py')
O = load('fireworks_sharpness_oracle', DOSSIER/'interval_oracle.py')


def bulk_certificate(m=256, b=512, A=16**6-1, depth=20):
    real_lo = real_hi = imag_lo = imag_hi = F(0)
    for n in range(m, b+1):
        tail = sum((O.source(n+j)/16**j for j in range(1, depth+1)), F(0))
        width = F(1, 16**depth*64*(n+depth)**2)
        phase = -A*(tail+width/2)
        err = F(22, 7)*A*width
        a, z = O.cosine(phase)
        c, d = O.cosine(phase-F(1, 4))
        real_lo += a-err
        real_hi += z+err
        imag_lo += c-err
        imag_hi += d+err
    unit = 10**10
    def down(x):
        return F((x.numerator*unit)//x.denominator, unit)
    def up(x):
        return F(-((-x.numerator*unit)//x.denominator), unit)
    real_lo, real_hi = down(real_lo), up(real_hi)
    imag_lo, imag_hi = down(imag_lo), up(imag_hi)
    square_upper = max(abs(real_lo), abs(real_hi))**2+max(abs(imag_lo), abs(imag_hi))**2
    return {'m': m, 'b': b, 'A': A, 'depth': depth,
            'real_interval': [real_lo, real_hi], 'imag_interval': [imag_lo, imag_hi],
            'norm_square_upper': square_upper, 'analytic_upper': S.bulk_upper(m, b, A)}


class SharpnessTests(unittest.TestCase):
    def test_independent_differentiated_four_pole_bounds(self):
        # Direct rational derivatives, with an independent crude tail from
        # retaining only the positive 32/(8(x+j)-7)^2 term.
        J = 24
        for x in (F(0), F(1, 7), F(1, 2), F(1), F(7, 3), F(4), F(10)):
            lower = F(0)
            for j in range(1, J+1):
                y = 8*(x+j)
                derivative = 32/(y-7)**2-16/(y-4)**2-8/(y-3)**2-8/(y-2)**2
                self.assertGreater(derivative, 0)
                lower += derivative/16**j
            upper = lower+F(32, 15*16**J)/(8*(x+J)+1)**2
            self.assertGreaterEqual(lower, 15/(8*x+6)**3)
            self.assertLessEqual(upper, 16/(8*x+1)**3)

    def test_nontrivial_source_bulk_bound(self):
        result = bulk_certificate()
        self.assertLess(result['analytic_upper'], result['b']-result['m']+1)
        self.assertLess(result['norm_square_upper'], result['analytic_upper']**2)

    def test_signed_limit_and_obstruction_exact(self):
        for c in (F(9, 4), F(5, 2), F(11, 4)):
            self.assertEqual(S.transport_obstruction(c), (1-F(2, 1)/c)**2)
            self.assertLess(S.coherent_score_limit(c), 1)
            self.assertGreater(S.coherent_score_limit(c), F(8, 9))
        self.assertEqual(S.coherent_score_limit(F(5, 2)), F(24, 25))
        self.assertEqual(S.transport_obstruction(F(5, 2)), F(1, 25))

    def test_rational_profile_riemann_sum(self):
        c = F(5, 2)
        for scale in (8, 16, 32, 64):
            K = int(c*scale)
            profile = sum((F(2, K)*(1-F(k, K)) for k in range(1, 2*scale+1)), F(0))
            self.assertLess(abs(profile-S.coherent_score_limit(c)), F(2, K))

    def test_scope_rejections(self):
        for c in (F(2), F(3), F(4), 2.5):
            with self.assertRaises(ValueError):
                S.coherent_score_limit(c)
        for args in ((0, 5, 1), (5, 3, 1), (1, 2, -1), (1, 2, 1.5)):
            with self.assertRaises(ValueError):
                S.bulk_upper(*args)


if __name__ == '__main__':
    unittest.main()
