"""Stand-alone exact rational checks for the mathematical quotient-residual theorem.

Not a substitute for the authentic original Suzuki source gate exercised by
parent PR #149 and existing #137/WB4 regression probes.
"""
import unittest
from fractions import Fraction as F
from observational_succ.four_schur_dual_quotient import (
    DualQuotientError,polynomial_moment_gram,
    derivative_moment_projection_gram,quotient_derivative_cap,
    trace_primitive_polynomial_countermodel,
)

class PrimitiveDualTests(unittest.TestCase):
    def test_moment_gram_exact_parity(self):
        G=polynomial_moment_gram()
        self.assertEqual(G[0],(F(1),F(0),F(1,12),F(0)))
        self.assertEqual(G[1][1],F(1,12))
        self.assertEqual(G[3][3],F(1,448))
        self.assertEqual(G[0][3],F(0))

    def test_normalized_constant_moment_projection(self):
        # For h'=1, only zero-th moment of h' is nonzero. Projection energy 1.
        G=derivative_moment_projection_gram([[F(1)],[F(0)],[F(1,12)],[F(0)]])
        self.assertEqual(G,((F(1),),))

    def test_projection_of_t(self):
        # For h'=t: moments (0,1/12,0,1/80), ||h'||²=1/12.
        G=derivative_moment_projection_gram([[0],[F(1,12)],[0],[F(1,80)]])
        self.assertEqual(G,((F(1,12),),))

    def test_orthogonal_derivative_has_zero_projection(self):
        # h'=18P4(2t) is orthogonal to t^0..t^3; derivative energy 36.
        G=derivative_moment_projection_gram([[0],[0],[0],[0]])
        self.assertEqual(G,((F(0),),))

    def test_source_cap_no_moments(self):
        res=quotient_derivative_cap([[F(1,3),0],[0,F(1,5)]])
        self.assertEqual(res['residual_correction_upper'],
                         ((F(121,96),0),(0,F(121,160))))
        self.assertTrue(res['requires_independent_source_authentication'])
        self.assertFalse(res['RH_proved'])

    def test_moment_subtraction_reduces_bound(self):
        # Source budget C=2 on normGram=1, one deriv h'=1 has proj energy 1.
        r=quotient_derivative_cap([[1]],gprime_L1=2,kappa=F(1,2),
               authenticated_derivative_moments=[[1],[0],[F(1,12)],[0]])
        self.assertEqual(r['residual_correction_upper'],((F(6),),))
        self.assertEqual(r['derivative_moment_subtraction'],((F(1),),))

    def test_forged_moments_rejected(self):
        with self.assertRaises(DualQuotientError):
            quotient_derivative_cap([[1]],gprime_L1=1,kappa=1,
                 authenticated_derivative_moments=[[2],[0],[F(1,6)],[0]])

    def test_not_psd_gram_rejected(self):
        for M in ([[1,2],[2,1]], [[-1]], [[0,1],[1,0]]):
            with self.assertRaises(DualQuotientError):quotient_derivative_cap(M)

    def test_bool_float_wrong_domains(self):
        for M in ([[True]], [[1.]], [[1]],):
            if M==[[1]]: continue
            with self.assertRaises(DualQuotientError):quotient_derivative_cap(M)
        with self.assertRaises(DualQuotientError):polynomial_moment_gram(F(0))
        with self.assertRaises(DualQuotientError):polynomial_moment_gram(degree=-1)

    def test_exact_countermodel(self):
        c=trace_primitive_polynomial_countermodel()
        self.assertEqual(c['projected_derivative_energy']/c['full_derivative_energy'],F(5,3))
        self.assertEqual(c['high_K_dual_energy'],F(36))
        self.assertTrue(c['projection_derivative_contraction_refuted'])

    def test_cross_column_moment_gram(self):
        # h1'=1 and h2'=t; projections orthogonal with energies 1 and 1/12.
        M=[[1,0],[0,F(1,12)],[F(1,12),0],[0,F(1,80)]]
        r=derivative_moment_projection_gram(M)
        self.assertEqual(r,((1,0),(0,F(1,12))))

class VanishingBoundaryMomentTests(unittest.TestCase):
    def test_exact_source_row_formula_no_error(self):
        from observational_succ.four_schur_dual_quotient import vanishing_boundary_moment_lower
        M=vanishing_boundary_moment_lower([[1,0],[0,1]], [[0,0],[0,0]])
        self.assertEqual(M, ((F(15), F(0)),(F(0),F(105))))

    def test_uncertainty_penalty_is_not_silently_clamped(self):
        from observational_succ.four_schur_dual_quotient import vanishing_boundary_moment_lower
        M=vanishing_boundary_moment_lower([[0,0],[0,0]], [[F(1,10),0],[0,F(1,10)]])
        self.assertEqual(M,((-F(12,5),0),(0,-F(12,5))))

    def test_eta_boundary_rejected(self):
        from observational_succ.four_schur_dual_quotient import vanishing_boundary_moment_lower
        for eta in (F(0),F(1),F(2)):
            with self.assertRaises(DualQuotientError):
                vanishing_boundary_moment_lower([[1,0],[0,1]], [[0,0],[0,0]],eta)

    def test_symbolic_integral_shape(self):
        from observational_succ.four_schur_dual_quotient import polynomial_moment_gram
        a=F(1,2)
        G=polynomial_moment_gram(a,3)
        # exact norms for t^2-a^2 and t^3-a^2t
        even=G[2][2]-2*a*a*G[0][2]+a**4*G[0][0]
        odd=G[3][3]-2*a*a*G[1][3]+a**4*G[1][1]
        self.assertEqual(even,F(1,30))
        self.assertEqual(odd,F(1,840))


class CompleteFourMomentAndHodgeTests(unittest.TestCase):
    def test_parity_isolated_two_moment_no_signal_loss_and_no_cross_leakage(self):
        from observational_succ.four_schur_dual_quotient import parity_isolated_two_moment_lower
        # At zero error, preserves 100% of 30 c1^2 and 210 c2^2 (not 50%).
        M0 = parity_isolated_two_moment_lower([[1, 0], [0, 1]], [[0, 0], [0, 0]])
        self.assertEqual(M0, ((F(30), F(0)), (F(0), F(210))))
        # Even error does not contaminate odd diagonal entry [0][0]:
        M_err = parity_isolated_two_moment_lower([[1, 0], [0, 0]], [[0, 0], [0, F(1, 10)]])
        self.assertEqual(M_err[0][0], F(30))
        self.assertEqual(M_err[1][1], -F(21, 10))
        # Cross-parity nonzero entry rejected when strict_parity=True:
        with self.assertRaises(DualQuotientError):
            parity_isolated_two_moment_lower([[0, 1], [0, 0]], [[0, 0], [0, 0]])

    def test_complete_four_moment_matches_monomial_and_legendre_routes(self):
        from observational_succ.four_schur_dual_quotient import (
            monomial_moments_from_mixed_rows,
            legendre_moments_from_mixed_rows,
            complete_four_moment_lower,
            legendre_four_moment_lower,
        )
        # Arbitrary parity-respecting mixed moments M_1..M_4 on 4 columns:
        # Recall M_1 = 2 E_0, M_3 = 12(E_0 - 5 c_1) => c_1 = (M_1/2 - M_3/12)/5 = M_1/10 - M_3/60
        # M_2 = 12 E_1, M_4 = 20(2 E_1 - 7 c_2) => c_2 = (M_2/6 - M_4/20)/7 = M_2/42 - M_4/140
        M_mid = (
            (F(2), F(0), -F(1), F(0)),
            (F(0), F(6), F(0), F(3)),
            (F(12), F(0), F(6), F(0)),
            (F(0), F(20), F(0), -F(10)),
        )
        Z_err = tuple(tuple(F(0) for _ in range(4)) for _ in range(4))
        c1_row = tuple(M_mid[0][i] / 10 - M_mid[2][i] / 60 for i in range(4))
        c2_row = tuple(M_mid[1][i] / 42 - M_mid[3][i] / 140 for i in range(4))
        E_mid, _ = monomial_moments_from_mixed_rows(M_mid, Z_err)
        L_mid, L_err = legendre_moments_from_mixed_rows(M_mid, Z_err)
        gram_monomial = derivative_moment_projection_gram(E_mid)
        gram_complete = complete_four_moment_lower(
            (c1_row, c2_row), (Z_err[0], Z_err[1]),
            (M_mid[2], M_mid[3]), (Z_err[2], Z_err[3]),
        )
        gram_legendre = legendre_four_moment_lower(L_mid, L_err)
        self.assertEqual(gram_monomial, gram_complete)
        self.assertEqual(gram_monomial, gram_legendre)

    def test_hodge_legendre_general_m_endpoint_free_gram(self):
        from observational_succ.four_schur_dual_quotient import (
            hodge_legendre_endpoint_free_gram,
            general_endpoint_free_moment_lower,
        )
        h4 = hodge_legendre_endpoint_free_gram(m=4, radius=F(1, 2))
        self.assertEqual(h4["K_gram"], ((F(1, 30), F(0)), (F(0), F(1, 210))))
        self.assertEqual(h4["K_inverse"], ((F(30), F(0)), (F(0), F(210))))
        h5 = hodge_legendre_endpoint_free_gram(m=5, radius=F(1, 2))
        self.assertEqual(
            h5["K_inverse"],
            (
                (F(168, 5), F(0), F(252, 5)),
                (F(0), F(210), F(0)),
                (F(252, 5), F(0), F(3528, 5)),
            ),
        )
        # At m=4, general_endpoint_free_moment_lower equals parity_isolated_two_moment_lower
        g4 = general_endpoint_free_moment_lower([[F(1), 0], [0, F(1)]], [[0, 0], [0, 0]])
        self.assertEqual(g4, ((F(30), F(0)), (F(0), F(210))))

    def test_observer_synergy_and_cross_gauge_no_ghost(self):
        from observational_succ.four_schur_dual_quotient import (
            observer_interior_boundary_synergy_certificate,
            cross_contact_gauge_no_ghost_countermodel,
        )
        syn = observer_interior_boundary_synergy_certificate()
        self.assertEqual(syn["interior_observer_c1_c2_energy"], F(0))
        self.assertEqual(syn["joined_observer_complete_4moment_energy"], F(24))
        self.assertEqual(syn["residual_under_joined_observer"], F(0))
        self.assertTrue(syn["strict_synergy_over_sum_of_parts"])
        self.assertFalse(syn["RH_proved"])

        ng = cross_contact_gauge_no_ghost_countermodel()
        self.assertTrue(ng["violates_bessel_inequality"])
        self.assertLess(ng["forged_apparent_residual"], F(0))
        self.assertFalse(ng["RH_proved"])


if __name__=='__main__':unittest.main()

