"""Exact finite controls for the scope of the Young/triangle obstruction."""
from fractions import Fraction as Q
import unittest
from scripts import institute_eta_probe as E


class YoungTriangleObstruction(unittest.TestCase):
    def test_parameter_can_change_sufficient_sign(self):
        self.assertTrue(E.calibrate()['eta_choice_can_change_sufficient_sign'])

    def test_offdiagonal_direction_can_fail_when_axes_pass(self):
        T=((Q(5),Q(4)),(Q(4),Q(5)))
        M=((Q(1),Q(0)),(Q(0),Q(1)))
        errors=(Q(1),Q(1))
        for c in ((Q(1),Q(0)),(Q(0),Q(1))):
            self.assertFalse(E.triangle_obstruction(T,M,Q(1),errors,c)
                             ['triangle_certificate_strictly_negative'])
        witness=E.triangle_obstruction(T,M,Q(1),errors,(Q(1),Q(-1)))
        self.assertTrue(witness['triangle_certificate_strictly_negative'])
        self.assertFalse(witness['genuine_source_negative'])

    def test_error_allocations_dominate_true_column_triangle(self):
        errors=(Q(2,7),Q(3,11))
        for theta in (Q(1,8),Q(1),Q(9)):
            for c in ((Q(1),Q(-2)),(Q(3,5),Q(7,2))):
                majorant=(1+theta)*errors[0]**2*c[0]**2+(1+1/theta)*errors[1]**2*c[1]**2
                triangle=(abs(c[0])*errors[0]+abs(c[1])*errors[1])**2
                self.assertGreaterEqual(majorant,triangle)

    def test_no_square_sign_laundering(self):
        # H<0 is a failure even when H² exceeds 4me².
        T=((Q(-10),Q(0)),(Q(0),Q(1)))
        M=((Q(1),Q(0)),(Q(0),Q(1)))
        w=E.triangle_obstruction(T,M,Q(1),(Q(1),Q(0)),(Q(1),Q(0)))
        self.assertLess(w['H'],0)
        self.assertLess(w['four_m_e_squared_minus_H_squared'],0)
        self.assertTrue(w['triangle_certificate_strictly_negative'])


if __name__=='__main__':
    unittest.main()
