"""30 exact Legendre derivative modes / Hilbert-space Neumann duality tests."""
import unittest
from fractions import Fraction as F
from observational_succ import suzuki_neumann_dual_gauge as g


class Rank30Geometry(unittest.TestCase):
    def test_explicit_parity_tridiagonal_inverse_all_thirty(self):
        H=g.legendre_derivative_metric(F(1,2),30)
        inv=g.inverse_derivative_metric(F(1,2),30)
        self.assertEqual(g.mul(H,inv),g.ident(30))
        self.assertEqual(g.mul(inv,H),g.ident(30))
        blocks=g.normalized_parity_blocks()
        self.assertEqual(len(blocks["low_odd"]),15)
        self.assertEqual(len(blocks["low_even"]),15)
        for i in range(1,31):
            for j in range(1,31):
                if (i+j)%2:self.assertEqual(H[i-1][j-1],0)
                if abs(i-j)>2:self.assertEqual(inv[i-1][j-1],0)
        self.assertEqual(H[0][0],F(4))
        self.assertEqual(H[1][1],F(12))
        self.assertEqual(H[0][2],F(4))
        self.assertGreater(inv[0][0],0)

    def test_independent_exact_legendre_polynomial_derivative_integrals(self):
        from observational_succ import suzuki_legendre_source as S
        a=F(1,2)
        for i,j in ((1,1),(1,2),(1,3),(3,5),(4,6),(10,12),(29,29),(29,30),(30,30)):
            pi=S.legendre_polynomial(i,a);pj=S.legendre_polynomial(j,a)
            actual=S.poly_integral(S.poly_mul(S.poly_derivative(pi),
                                              S.poly_derivative(pj)),-a,a)
            H=g.legendre_derivative_metric(a,max(i,j))
            self.assertEqual(actual,H[i-1][j-1])

    def test_rankwise_geometry_for_arbitrary_a(self):
        for a in (F(1,4),F(1,2),F(1),F(3,2)):
            for rank in (1,2,3,5,10,30):
                H=g.legendre_derivative_metric(a,rank)
                inv=g.inverse_derivative_metric(a,rank)
                self.assertEqual(g.mul(H,inv),g.ident(rank))

    def test_source_gauge_inputs_strict_not_float(self):
        for fn in (
            lambda:g.legendre_derivative_metric(0,30),
            lambda:g.legendre_derivative_metric(.5,30),
            lambda:g.inverse_derivative_metric(F(1,2),31),
            lambda:g.legendre_derivative_metric(F(1,2),False),
        ):
            with self.assertRaises(g.DualGaugeError):fn()


class ExactGaugeProjection(unittest.TestCase):
    def test_synthetic_30_dim_h1_projection_removes_large_low_part(self):
        H=g.legendre_derivative_metric(F(1,2),30)
        eps=F(1,10)
        residual=eps*eps/F(61)
        # f_1'=L_1'+eps P30(2x); f_2'=L_2'-eps P30(2x).
        # The classical Legendre mode P30 is orthogonal to all
        # first-thirty derivatives (degrees 0..29); ||P30||²=1/61.
        moments=tuple((H[j][0],H[j][1]) for j in range(30))
        T=((H[0][0]+residual,-residual),
           (-residual,H[1][1]+residual))
        out=g.finite_dual_gauge_derivative_gram(T,moments)
        self.assertEqual(out.projected_derivative_gram,
                         ((residual,-residual),(-residual,residual)))
        self.assertTrue(g.nonnegative_quadratic(out.projected_derivative_gram))
        self.assertGreater(T[0][0],out.projected_derivative_gram[0][0])
        self.assertFalse(out.true_suzuki_derivative_moments_authenticated)
        self.assertFalse(out.rh_proved)

    def test_fake_nonhilbert_gram_is_refused_not_forced_positive(self):
        H=g.legendre_derivative_metric(F(1,2),30)
        moments=tuple((H[j][0],) for j in range(30))
        with self.assertRaises(g.DualGaugeError):
            g.finite_dual_gauge_derivative_gram(((F(1),),),moments)

    def test_gauge_zero_moments_is_conservative_identity(self):
        moments=tuple((F(),F()) for _ in range(30))
        T=((F(1),F(1,2)),(F(1,2),F(1)))
        out=g.finite_dual_gauge_derivative_gram(T,moments)
        self.assertEqual(out.projected_derivative_gram,T)
        self.assertFalse(out.original_full_30mode_Schur_PSD)

    def test_synthetic_input_is_not_an_authentic_weil_certificate(self):
        H=g.legendre_derivative_metric(F(1,2),30)
        moments=tuple((H[j][0],) for j in range(30))
        v=g.finite_dual_gauge_derivative_gram(((F(4),),),moments)
        self.assertFalse(v.true_suzuki_derivative_moments_authenticated)
        self.assertFalse(v.original_full_30mode_Schur_PSD)

if __name__=="__main__":
    unittest.main()
