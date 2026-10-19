"""Exact topological source controls; global separation proven in paper."""
import unittest
from fractions import Fraction
from observational_succ.topological_clock_factors import (
    RationalContraction,odometer_cylinder_projection,
    hidden_contraction_same_profinite_point,
)
from observational_succ.orbit_clock_genesis import ClockSourceError


class ContinuousClockFactorTests(unittest.TestCase):
    def test_strictly_increasing_bounded_infinite_orbit(self):
        c=RationalContraction()
        x=c.state(0)
        for n in range(1,110):
            y=c.successor(x)
            self.assertEqual(y,c.state(n))
            self.assertGreater(y,x)
            self.assertLess(y,1)
            x=y
        self.assertEqual(c.state(0),0)

    def test_distinct_residues_get_arbitrarily_close_in_contraction(self):
        c=RationalContraction()
        for m in (2,3,5,7,12):
            for epsilon in (Fraction(1,10),Fraction(1,10**6),Fraction(1,10**15)):
                witness=c.close_different_clock_residues(m,epsilon)
                self.assertTrue(witness['distinct_residues'])
                self.assertTrue(witness['gap_strictly_below_tolerance'])

    def test_odometer_finite_cylinders_preserve_equivariance_and_root(self):
        for source in (1,6,10,12,30,60,120):
            for target in range(1,source+1):
                if source%target: continue
                f=odometer_cylinder_projection(source,target)
                self.assertEqual(len(f),source)
                self.assertEqual(f[0],0)
                self.assertTrue(all(f[(k+1)%source]==(f[k]+1)%target for k in range(source)))

    def test_nondividing_cylinder_map_cannot_exist(self):
        with self.assertRaises(ClockSourceError):odometer_cylinder_projection(4,3)
        with self.assertRaises(ClockSourceError):odometer_cylinder_projection(15,4)

    def test_source_can_have_profinite_factor_but_hidden_distinct_fiber(self):
        witness=hidden_contraction_same_profinite_point(8,(2,3,4,5,6,7,8,9,10,12,15))
        self.assertTrue(witness['all_sampled_profinite_residues_zero'])
        self.assertEqual(witness['root_hidden_coordinate'],'0')
        self.assertEqual(witness['limit_hidden_coordinate'],'1')
        self.assertTrue(witness['no_finite_check_proves_infinite_noninjective_fiber'])

    def test_earlier_factorial_depth_may_not_resolve_later_clock(self):
        early=hidden_contraction_same_profinite_point(4,(2,3,4,5))
        late=hidden_contraction_same_profinite_point(5,(2,3,4,5))
        self.assertFalse(early['all_sampled_profinite_residues_zero'])
        self.assertTrue(late['all_sampled_profinite_residues_zero'])

    def test_continuity_probe_types_fail_closed(self):
        c=RationalContraction()
        with self.assertRaises(ClockSourceError):c.close_different_clock_residues(1,Fraction(1,10))
        with self.assertRaises(ClockSourceError):c.close_different_clock_residues(2,0)
        with self.assertRaises(ClockSourceError):c.close_different_clock_residues(2,0.1)
        with self.assertRaises(ClockSourceError):c.successor(0.5)
        with self.assertRaises(ClockSourceError):hidden_contraction_same_profinite_point(0,(2,))

if __name__=='__main__':unittest.main()
