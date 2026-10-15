"""Original signed Suzuki prime-power area integrals vs exact midpoint hinge controls."""
import unittest
from fractions import Fraction as Q
from observational_succ import hilbert_prime_hinge_integrals as h
from observational_succ import source_weil_hierarchy as original


class RationalDoubleHingeTests(unittest.TestCase):
    def test_independent_unit_square_probability_triangle_identity(self):
        for b in (Q(),Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1)):
            integrated=h.absolute_hinge_rect(0,1,0,1,b)
            self.assertEqual(integrated,(1-b)**3/3)
            self.assertEqual(
                h.oriented_hinge_rect(0,1,0,1,b),integrated/2)
        self.assertEqual(h.absolute_hinge_rect(0,1,0,1,2),0)

    def test_disjoint_activated_rectangle_analytic(self):
        # |x-y|>=1 on rectangles x=[2,3], y=[0,1].
        for b in (Q(),Q(1,2),Q(1)):
            self.assertEqual(h.absolute_hinge_rect(2,3,0,1,b),2-b)
            self.assertEqual(h.absolute_hinge_rect(0,1,2,3,b),2-b)

    def test_independent_midpoint_Riemann_sum_bound(self):
        # Does not invoke the 4-corner antiderivative on the oracle side.
        for b in (Q(1,4),Q(1,2),Q(3,4)):
            target=h.absolute_hinge_rect(0,1,0,1,b)
            m=32
            samples=sum((max(abs(Q(2*i+1,2*m)-Q(2*j+1,2*m))-b,0)
                        for i in range(m) for j in range(m)),Q())/m**2
            # Since (|x-y|-b)_+ has coordinate-Lipschitz constants 1,
            # the cell midpoint Lipschitz integral error is <=1/m.
            self.assertLessEqual(abs(samples-target),Q(1,m))

    def test_positive_part_and_source_domains(self):
        for fn in (
            lambda:h.oriented_hinge_rect(1,0,0,1,0),
            lambda:h.absolute_hinge_rect(0,1,0,1,-1),
            lambda:h.absolute_hinge_rect(0,1,0,1,0.5),
            lambda:h.source_rect(0.5,2,1,1),
            lambda:h.source_rect(Q(1,2),2,4,0),
        ):
            with self.assertRaises(h.HilbertHingeError):fn()


class GenuineArithmeticCellIntegralTests(unittest.TestCase):
    def test_first_prime_inactive_vs_activated_cell(self):
        a=Q(1,2)
        diag=h.authenticated_hinge_cell(a,2,0,0,2)
        self.assertEqual(diag.lower,0)
        self.assertEqual(diag.upper,0)
        opposite=h.authenticated_hinge_cell(a,2,0,3,2)
        self.assertEqual(opposite.prime,2)
        self.assertGreater(opposite.lower,0)
        self.assertGreaterEqual(opposite.upper,opposite.lower)
        self.assertFalse(opposite.midpoint_sampling_used)
        self.assertFalse(opposite.all_complete_weil_terms_included)
        other=h.authenticated_hinge_cell(a,2,3,0,2)
        self.assertEqual((other.lower,other.upper),(opposite.lower,opposite.upper))

    def test_all_real_original_prime_powers_and_never_fake_six(self):
        a=Q(1)
        self.assertEqual(original.authenticated_prime_wavefront(a),
                         ((2,2),(3,3),(4,2),(5,5),(7,7)))
        for n,p in original.authenticated_prime_wavefront(a):
            c=h.authenticated_hinge_cell(a,2,0,3,n)
            self.assertEqual(c.prime,p)
            self.assertEqual(c.n,n)
        for n in (1,6,8,9):
            with self.assertRaises(h.HilbertHingeError):
                h.authenticated_hinge_cell(a,2,0,3,n)
        with self.assertRaises(h.HilbertHingeError):
            h.authenticated_hinge_cell(Q(1,2),2,0,3,3)

    def test_true_original_log_sqrt_n_outward_holdout(self):
        try:import mpmath as mp
        except ImportError:self.skipTest("optional original-source mpmath diagnostic")
        mp.mp.dps=70
        for a,k,i,j,n in (
            (Q(1,2),2,0,3,2),
            (Q(1),2,0,3,2),
            (Q(1),2,0,3,3),
            (Q(1),2,0,3,4),
        ):
            c=h.authenticated_hinge_cell(a,k,i,j,n)
            l,r,y0,y1=h.source_rect(a,k,i,j)
            def M(v):return mp.mpf(v.numerator)/v.denominator
            b=mp.log(n)
            def cubed(z):return max(mp.mpf("0"),z)**3
            def orient(xlo,xhi,ylo,yhi):
                return (cubed(xhi-ylo-b)-cubed(xlo-ylo-b)
                       -cubed(xhi-yhi-b)+cubed(xlo-yhi-b))/6
            integral=orient(M(l),M(r),M(y0),M(y1))
            integral+=orient(M(y0),M(y1),M(l),M(r))
            original_weight=mp.log(c.prime)/mp.sqrt(n)
            actual=original_weight*integral
            self.assertLessEqual(M(c.lower),actual)
            self.assertGreaterEqual(M(c.upper),actual)

    def test_complete_prime_part_original_row_column_symmetry(self):
        for k in (1,2,3):
            result=h.hilbert_prime_cell_stream(Q(1,2),k)
            self.assertTrue(result["all_original_pair_cells_visited"])
            self.assertTrue(result["source_interval_symmetric"])
            self.assertEqual(len(result["Hilbert_order_entries"]),4**k)
            self.assertEqual(result["prime_hinge_spatial_quadrature_error"],0)
            self.assertFalse(result["full_original_signed_Weil_matrix_constructed"])
            self.assertFalse(result["global_positive_form_proved"])
            self.assertFalse(result["rh_proved"])

    def test_full_source_signed_operator_is_not_prime_only_positive_entries(self):
        p=h.original_prime_cell_sum(Q(1,2),3,0,7)
        self.assertEqual(p["prime_power_atoms"],((2,2),))
        self.assertFalse(p["full_signed_Gamma_pole_contact_included"])
        self.assertFalse(p["positive_complete_Weil_form_proved"])
        self.assertEqual(p["prime_hinge_spatial_error"],0)

if __name__=="__main__":
    unittest.main()
