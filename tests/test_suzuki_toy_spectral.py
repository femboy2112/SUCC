"""Route C: exact toy-model facts (one-lag self-reciprocal toy ell=2, Gamma=pi(Z+1/2)) + Jensen window. sympy/mpmath."""
import unittest
import sympy as sp
import mpmath as mp
mp.mp.dps = 50

class Toy(unittest.TestCase):
    def test_nyquist_identity_and_a_lt_b_closed_form(self):
        a, z, th = sp.symbols('a z theta')
        # theta=pi: sinh(a+iza)+e^{i pi} sinh(-a+iza) == 2 sinh(a) cos(a z)  (W even, Spec=Gamma/a-lattice)
        expr = sp.sinh(a * (1 + sp.I * z)) + sp.exp(sp.I * sp.pi) * sp.sinh(a * (sp.I * z - 1)) - 2 * sp.sinh(a) * sp.cos(a * z)
        self.assertEqual(sp.simplify(expr.rewrite(sp.exp)), 0)
        # a<b closed-form spectrum solves sinh(a+iza)=e^{i th} sinh(a-iza)
        for aa, tt in ((mp.mpf('0.5'), mp.pi / 2), (mp.mpf('0.75'), mp.pi / 3), (mp.mpf('0.9'), mp.mpf('1.0') * mp.pi), (mp.mpf('0.75'), 3 * mp.pi / 2)):
            for k in (-3, -1, 0, 2, 5):
                zz = (mp.pi * k + mp.atan(mp.tanh(aa) * mp.tan(tt / 2))) / aa
                lhs = mp.sinh(aa + 1j * zz * aa); rhs = mp.exp(1j * tt) * mp.sinh(aa - 1j * zz * aa)
                self.assertLess(abs(lhs - rhs), mp.mpf(10) ** -40)
        # theta=pi, a=1: spectrum is exactly Gamma = pi(k+1/2)
        for k in range(-5, 5):
            zz = mp.pi * (2 * k + 1) / 2
            self.assertLess(abs(mp.sinh(1 + 1j * zz) + mp.sinh(1 - 1j * zz)), mp.mpf(10) ** -40)
    def test_C6_null_vector_beyond_critical_width(self):
        # v=psi(x)+psi(x-2): vhat(g)=psihat(g)(1+e^{2ig}); e^{2ig}=-1 on Gamma  => Q(v)=0, lambda_a=0 for a>1
        for n in range(-6, 7):
            g = sp.pi / 2 + sp.pi * n
            self.assertEqual(sp.simplify(1 + sp.exp(2 * sp.I * g)), 0)
    def test_B8_fake_nonreal_pair_form_exact(self):
        c = lambda j: sp.Rational((-1) ** j) * (sp.Rational(2) ** j + sp.Rational(1, 2) ** j) / 2
        self.assertEqual([c(0), c(1), c(2)], [1, sp.Rational(-5, 4), sp.Rational(17, 8)])
        C2 = sp.Matrix(2, 2, lambda i, j: c(abs(i - j)))
        self.assertEqual(sorted(C2.eigenvals().keys()), [sp.Rational(-1, 4), sp.Rational(9, 4)])
        C3 = sp.Matrix(3, 3, lambda i, j: c(abs(i - j))); u = sp.Matrix([1, 0, -1])
        self.assertEqual(C3 * u, sp.Rational(-9, 8) * u)
        C1 = sp.Matrix([[c(0)]]); self.assertEqual(list(C1.eigenvals().keys()), [1])  # size-1 probe is blind
        S2 = sp.Matrix(2, 2, lambda i, j: (-1) ** abs(i - j)); self.assertEqual(sorted(S2.eigenvals().keys()), [0, 2])
    def test_B9_q_topology_normalizability_exact(self):
        from fractions import Fraction as Fr
        ell = Fr(2)
        for N in (1, 2, 3, 4, 6, 12):
            a = Fr(N) * ell / 2; n = N  # a=N*ell/2: every residue class has exactly N points
            intn2 = ell * n * n   # int_0^ell n(t)^2 dt
            self.assertEqual(intn2, 2 * N * N)
            self.assertEqual((2 * a) ** 2 / (ell * intn2), 1)        # gamma-share of Q-energy
            self.assertEqual(Fr(2 * a) / (2 * intn2), Fr(1, 2 * N))  # L2 mass /pi
    def test_B5_jensen_window_crossing(self):
        mp.mp.dps = 30
        expect = {1: 307.357, 2: 2489.14}
        for a, e in expect.items():
            f = lambda r: mp.quad(lambda t: 2 * (mp.siegeltheta(t) / mp.pi + 1) / t, [14, r]) - 2 * a * r / mp.pi
            r = mp.findroot(f, 2 * mp.pi * mp.e ** (2 * a + 2))
            self.assertLess(abs(r - e) / e, 1e-4)
        mp.mp.dps = 50

if __name__ == '__main__':
    unittest.main()
