"""Focused exact and synthetic numerical checks; not a π-normality test."""
import math
import unittest
from fractions import Fraction
from source_reflection_haar import (
    H_ASCENDING, Q_ASCENDING, EIGHT_MOTIF, ROOT_ANGLES,
    poly_mul, impulse, filter_residual, total_hardy_energy,
    root_phase_fourth, source_class, complementary_arc_lengths,
    coherent_haar_ports, source_mask_winding, model_summary)


class ExactAlgebra(unittest.TestCase):
    def test_H_factors(self):
        self.assertEqual(poly_mul((2,0,1),(2,2,1)), H_ASCENDING)

    def test_Q_factor(self):
        self.assertEqual(poly_mul(H_ASCENDING, (1,-1)), Q_ASCENDING)

    def test_h8_complement(self):
        # t^8-16 = H(t) * (t^4-2t^3+4t-4)
        self.assertEqual(poly_mul(H_ASCENDING,(-4,4,0,-2,1)),(-16,0,0,0,0,0,0,0,1))

    def test_h4_eight_motif(self):
        self.assertEqual(EIGHT_MOTIF,
            (Fraction(1,4),Fraction(-1,4),Fraction(0),Fraction(1,8),
             Fraction(-1,16),Fraction(0),Fraction(0),Fraction(0)))

    def test_eight_renormalization(self):
        for n in range(160):
            self.assertEqual(impulse(n+8),impulse(n)/16)

    def test_recurrence(self):
        for n in range(150):
            self.assertEqual(filter_residual(n),int(n==0))

    def test_energy(self):
        self.assertEqual(total_hardy_energy(),Fraction(37,255))

    def test_root_signs(self):
        self.assertEqual({i:root_phase_fourth(i) for i in (2,3,5,6)},
                         {2:1,3:-1,5:-1,6:1})

    def test_bad_root_index(self):
        for i in [0,1,4,7,8,-1]:
            with self.assertRaises(ValueError):
                root_phase_fourth(i)

    def test_source_prime_pairing(self):
        for k in ('top','bottom'):
            self.assertEqual(source_class(k),(1,11))
        for k in ('upper_left','lower_left'):
            self.assertEqual(source_class(k),(-1,5))

    def test_winding_regions(self):
        self.assertEqual([source_mask_winding(x) for x in
                          (Fraction(1,2),Fraction(5,4),Fraction(3,2))],[0,1,5])

    def test_critical_winding(self):
        self.assertIsNone(source_mask_winding(Fraction(1)))
        self.assertIsNone(source_mask_winding(math.sqrt(2)))

    def test_radius_errors(self):
        with self.assertRaises(ValueError):
            source_mask_winding(0)
        with self.assertRaises(ValueError):
            impulse(-1)


class CoherentHaar(unittest.TestCase):
    def test_complementarity(self):
        for theta in ROOT_ANGLES.values():
            d,e = complementary_arc_lengths(theta)
            self.assertAlmostEqual(d+e,math.pi*math.sqrt(2),places=13)

    def test_exact_root_ports(self):
        for name,theta in ROOT_ANGLES.items():
            pplus,pminus=coherent_haar_ports(theta)
            self.assertAlmostEqual(pplus,1 if source_class(name)[0]==1 else 0, places=12)
            self.assertAlmostEqual(pminus,1 if source_class(name)[0]==-1 else 0, places=12)

    def test_unitarity_everywhere(self):
        for n in range(121):
            theta=math.pi/2+math.pi*n/120
            plus,minus=coherent_haar_ports(theta)
            self.assertAlmostEqual(plus+minus,1,places=12)

    def test_reference_phase_swaps_ports(self):
        for theta in ROOT_ANGLES.values():
            p0=coherent_haar_ports(theta)
            p1=coherent_haar_ports(theta,reference_phase=math.pi)
            self.assertAlmostEqual(p0[0],p1[1],places=12)
            self.assertAlmostEqual(p0[1],p1[0],places=12)

    def test_quadratic_angle_error(self):
        for name,theta in ROOT_ANGLES.items():
            if theta > math.pi/2+0.01 and theta < 3*math.pi/2-0.01:
                for eps in (0.001,0.01):
                    pp=coherent_haar_ports(theta+eps)
                    wrong=pp[1] if source_class(name)[0]==1 else pp[0]
                    self.assertLessEqual(wrong,4*eps*eps+1e-13)

    def test_invalid_semicircle(self):
        for theta in (0,math.pi/4,7*math.pi/4):
            with self.assertRaises(ValueError):
                coherent_haar_ports(theta)

    def test_different_frequency_not_perfect(self):
        p = coherent_haar_ports(ROOT_ANGLES['upper_left'],wavenumber=1.5)
        self.assertGreater(p[0],0.005)
        self.assertLess(p[0],0.99)

    def test_summary_type_boundary(self):
        self.assertIn("not a BBP phase conjugacy",model_summary()["model_status"])


if __name__=='__main__':
    unittest.main()
