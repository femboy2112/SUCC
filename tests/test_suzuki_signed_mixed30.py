"""Original genuine signed Suzuki first-prime 30-coordinate derivative mixed moments.

Strictly separates M_ji=<u_j',(G_Ju_i)'> from the unresolved derivative
Gram T_ij=< (G_J u_i)',(G_J u_j)'> and the full low/high residual B-DY.
"""
import unittest
from fractions import Fraction as F
from dataclasses import replace
from observational_succ import suzuki_signed_mixed30 as m
from observational_succ import suzuki_neumann_source_flux as flux

class ExactPolynomialSourceTest(unittest.TestCase):
    def test_shifted_legendre_true_rational_basis(self):
        from observational_succ import suzuki_legendre_source as S
        for n in range(1,31):
            p=m.shifted_legendre(n)
            self.assertEqual(m.polynomial_integral(p),0)
            self.assertEqual(S.poly_eval(p,F(0)),1)
            self.assertEqual(S.poly_eval(p,F(1)),(-1)**n)
        for n in (1,2,3,8,15,30):
            p=m.shifted_legendre(n)
            norm=m.polynomial_integral(S.poly_mul(p,p))
            self.assertEqual(norm,F(1,2*n+1))

    def test_original_prime2_hinge_interval_uses_same_log2_source_monotonically(self):
        from observational_succ import suzuki_legendre_source as S
        lo,hi=S.tight_log2(digits=190)
        src=S._pinned_source()
        old=src.log2_iv()
        self.assertLessEqual(lo,old.hi)
        self.assertGreaterEqual(hi,old.lo)
        self.assertGreater(lo,F(0))
        self.assertLess(hi,F(1))
        # ∫_b^1 (t-b)dt=(1-b)^2/2. Endpoints are TRUE
        # monotonic rational bounds, no illicit src.I exponentiation.
        constant=m.original_prime2_hinge_integral((F(1),))
        self.assertEqual(constant.lo,(1-hi)**2/2)
        self.assertEqual(constant.hi,(1-lo)**2/2)
        # The independent linear moment has primitive
        # 1/3-b/2+b^3/6; again it is strictly decreasing in b.
        moment=m.original_prime2_hinge_integral((F(0),F(1)))
        H=lambda b:F(1,3)-b/2+b**3/6
        self.assertEqual(moment.lo,H(hi))
        self.assertEqual(moment.hi,H(lo))
        # Signed polynomial coefficients must reverse outward endpoints.
        negative=m.original_prime2_hinge_integral((F(-1),))
        self.assertEqual((negative.lo,negative.hi),
                         (-constant.hi,-constant.lo))
        self.assertLessEqual(negative.lo,negative.hi)

    def test_genuine_polynomial_exponential_moments(self):
        for alpha in (F(-1,2),F(-5,2),F(-33,2),F(1,2)):
            a=m.exponential_moments(alpha,30)
            self.assertEqual(len(a),31)
            self.assertTrue(all(x.lo<=x.hi for x in a))
            self.assertTrue(all(x.hi>0 for x in a))
        with self.assertRaises(m.OriginalMixedGaugeError):
            m.exponential_moments(F(300),3)
        with self.assertRaises(m.OriginalMixedGaugeError):
            m.polynomial_exp_integral((0.5,),F(1,2))

    def test_source_polynomial_signed_gamma_flux_matches_independent_adapter(self):
        p=m.shifted_legendre(1)
        for J in (1,2,3):
            a=m.signed_source_poly_moment(p,J)
            b=flux.finite_signed_first_flux(J)
            # µ_J=2∫g_J P1(1-2t)dt; different polynomial integration
            # vs separately coded weighted source exponential.
            self.assertLessEqual(2*a.lo,b.hi)
            self.assertGreaterEqual(2*a.hi,b.lo)
            self.assertLess(a.hi-a.lo,F(1,10**5))

    def test_only_true_prime2_and_original_contact(self):
        from observational_succ import suzuki_legendre_source as S
        original=S._pinned_source()
        self.assertEqual(original.authenticated_prime_wavefront(F(1,2)),((2,2),))
        self.assertEqual(m.polynomial_integral(m.shifted_legendre(1),1),-F(1,6))
        for n in (2,3,4,10,29,30):
            self.assertEqual(m.polynomial_integral(m.shifted_legendre(n),1),0)

    def test_genuine_even_constant_channel_is_not_automatically_zero(self):
        p1=m.original_G_constant_channel(1,1)
        p2=m.original_G_constant_channel(2,1)
        self.assertEqual((p1.lo,p1.hi),(0,0))
        self.assertLessEqual(p2.lo,p2.hi)
        self.assertNotEqual((p2.lo,p2.hi),(0,0))

class OriginalSignedGaugeSourceTests(unittest.TestCase):
    def test_true_second_derivative_legendre_expansions(self):
        self.assertEqual(m.original_second_derivative_expansion(1),())
        self.assertEqual(m.original_second_derivative_expansion(2),((0,F(12)),))
        self.assertEqual(m.original_second_derivative_expansion(3),((1,F(60)),))
        for j in (5,10,15,29,30):
            c=m.original_second_derivative_expansion(j)
            self.assertTrue(all(k<j-1 and (k+j)%2==0 for k,v in c))

    def test_true_first_mode_gauge_all_thirty_j_coordinates(self):
        out=m.original_mixed_derivative_gram(1,30,(1,))
        self.assertEqual(out.rank,30)
        self.assertEqual(out.low_modes,(1,))
        self.assertEqual(len(out.matrix_intervals),30)
        self.assertEqual(out.source,"AUTHENTIC_Q_ZETA_SUZUKI_G_J_TRUE_LOWHIGH_DERIVATIVE")
        self.assertFalse(out.true_pure_H1_derivative_Gram_done)
        self.assertFalse(out.high_response_Y_calculated)
        self.assertFalse(out.rh_proved)
        for j,row in enumerate(out.matrix_intervals,1):
            self.assertEqual(len(row),1)
            self.assertLessEqual(row[0].lo,row[0].hi)
            if j%2==0:self.assertEqual((row[0].lo,row[0].hi),(0,0))
        actual=m.original_boundary_F(1,1)*4
        self.assertEqual((actual.lo,actual.hi),
                         (out.matrix_intervals[0][0].lo,out.matrix_intervals[0][0].hi))
        e=m.projected_gauge_diag_energy(out)
        self.assertEqual(len(e),1)
        self.assertGreater(e[0][0],0)
        self.assertLessEqual(e[0][0],e[0][1])

    def test_real_suzuki_mixed_moments_parity_of_first_three_modes(self):
        out=m.original_mixed_derivative_gram(1,5,(1,2,3))
        self.assertEqual(out.low_modes,(1,2,3))
        for j,row in enumerate(out.matrix_intervals,1):
            for i,c in zip((1,2,3),row):
                if (i+j)%2:self.assertEqual((c.lo,c.hi),(0,0))
                else:self.assertLessEqual(c.lo,c.hi)
        self.assertFalse(out.original_full_infinite_Gamma_done)

    def test_forged_same_number_source_fields_cannot_claim_gauge(self):
        out=m.original_mixed_derivative_gram(1,30,(1,))
        with self.assertRaises(m.OriginalMixedGaugeError):
            m.projected_gauge_diag_energy(replace(out,
                original_source_blob="forged"))
        with self.assertRaises(m.OriginalMixedGaugeError):
            m.projected_gauge_diag_energy(replace(out,
                source="AUTHENTIC_Q_ZETA_SUZUKI_FAKE"))
        if out.matrix_intervals[0][0].lo==F(0):
            self.skipTest("source first moment zero, choose different mutation")
        data=[list(row) for row in out.matrix_intervals]
        from observational_succ import suzuki_legendre_source as S
        orig=S._pinned_source()
        data[0][0]=orig.I(F(),F())
        with self.assertRaises(m.OriginalMixedGaugeError):
            m.projected_gauge_diag_energy(replace(out,
                matrix_intervals=tuple(tuple(row) for row in data)))

    def test_source_scope_guards(self):
        for fn in (
            lambda:m.shifted_legendre(31),
            lambda:m.shifted_legendre(.5),
            lambda:m.signed_source_poly_moment((F(1),),0),
            lambda:m.original_mixed_derivative_gram(1,31,(1,)),
            lambda:m.original_mixed_derivative_gram(1,30,(31,)),
            lambda:m.original_mixed_derivative_gram(1,30,(1,1)),
        ):
            with self.assertRaises(m.OriginalMixedGaugeError):fn()

if __name__=="__main__":
    unittest.main()
