"""Route A exact countermodels (CM1 late-crossing, CM2 L2-dense vs form-dense, CM3 Ritz upper bound). Fractions + sympy."""
import unittest
from fractions import Fraction as F
import sympy as sp

def lam_closed(a, M, m):
    a = F(a); M = F(M)
    k = sum(1 for j in range(m) if M + F(j + 1, m) <= a)
    return 1 - 2 * F(k, m)

def lam_direct(a, M, m, top=6):
    n = top * m
    phi = sp.Matrix([1 if (F(M) <= F(i, m) < F(M) + 1) else 0 for i in range(n)]) / sp.sqrt(m)
    A = sp.eye(n) - 2 * phi * phi.T
    idx = [i for i in range(n) if F(i + 1, m) <= F(a)]
    return min(sp.simplify(e) for e in A.extract(idx, idx).eigenvals())

class RouteA(unittest.TestCase):
    def test_cm1_closed_form_vs_exact_eigenvalue(self):
        M, m = 2, 3
        for k in range(1, 16):
            a = F(k, m)
            self.assertEqual(sp.Rational(lam_closed(a, M, m).numerator, lam_closed(a, M, m).denominator),
                             sp.nsimplify(lam_direct(a, M, m)), msg=str(a))
    def test_cm1_world_table_monotone_and_crossing(self):
        m = 4
        for M in (1, 5, 25):
            grid = [F(j, 4) for j in range(1, 4 * (M + 8))]
            vals = [lam_closed(a, M, m) for a in grid]
            self.assertTrue(all(x >= y for x, y in zip(vals, vals[1:])))
            self.assertEqual(lam_closed(M, M, m), 1)
            self.assertEqual(lam_closed(F(2 * M + 1, 2), M, m), 0)
            self.assertEqual(lam_closed(M + 2, M, m), -1)
        # every world with M > a0 is indistinguishable from I at horizon a0
        self.assertEqual({lam_closed(F(7, 2), M, m) for M in range(4, 61)}, {F(1)})
    def test_cm2_l2_dense_not_form_dense(self):
        x, k, al = sp.symbols('x k alpha', positive=True)
        u = sp.exp(-al * x)
        qD = sp.integrate(sp.diff(u, x) ** 2, (x, 0, sp.oo))
        nrm = sp.integrate(u ** 2, (x, 0, sp.oo))
        qR = qD - al * u.subs(x, 0) ** 2
        self.assertEqual(sp.simplify(qD - al / 2), 0)
        self.assertEqual(sp.simplify(nrm - 1 / (2 * al)), 0)
        self.assertEqual(sp.simplify(qR + al / 2), 0)
        self.assertEqual(sp.simplify(qR / nrm + al ** 2), 0)
        uk_in = k * x * sp.exp(-al * x)
        qDk = sp.integrate(sp.diff(uk_in, x) ** 2, (x, 0, 1 / k)) + sp.integrate(sp.diff(u, x) ** 2, (x, 1 / k, sp.oo))
        err = sp.integrate((uk_in - u) ** 2, (x, 0, 1 / k))
        self.assertEqual(sp.simplify(sp.limit(qDk / k, k, sp.oo) - 1), 0)
        self.assertEqual(sp.limit(err, k, sp.oo), 0)
    def test_cm3_ritz_upper_bound_direction(self):
        A = sp.Matrix([[3, 2, 0], [2, 1, 0], [0, 0, 5]])
        full = min(float(e) for e in A.eigenvals())
        self.assertAlmostEqual(full, 2 - 5 ** 0.5, places=6)  # (3+1)/2 - sqrt(((3-1)/2)^2+4)
        ritz = [float(min(A[:K, :K].eigenvals())) for K in (1, 2, 3)]
        self.assertEqual(ritz[0], 3.0)
        for r in ritz:
            self.assertGreaterEqual(r, full - 1e-12)
        self.assertLess(full, 0)

if __name__ == '__main__':
    unittest.main()
