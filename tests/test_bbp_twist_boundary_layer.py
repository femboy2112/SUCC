"""Independent exact seam/source checks and certified boundary observables."""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_twist_boundary_layer import (
    twisted_window, edge_loss_interval, edge_complex_error,
    scaled_deficit_budget, edge_loss_power_coefficient,
)
from observational_succ.bbp_prime_window_signed_intervals import box_phase


class TwistBoundaryLayerTests(unittest.TestCase):
    def test_direct_backward_endpoint_reconstruction(self):
        for m in (1,3,7,13):
            initial, window = twisted_window(m)
            state = -initial
            reverse = [state]
            for n in range(4*m,m+1,-1):
                force=Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
                state=(state-force)/16
                reverse.append(state)
            self.assertEqual(tuple(reversed(reverse)),window)
            self.assertLess(initial,0)
            self.assertGreater(window[-1],Q(19,100))
            self.assertNotEqual(window[-1],initial)

    def test_edge_loss_positive_null_and_conjugation_controls(self):
        self.assertEqual(edge_loss_interval(0),(0,0))
        for h in (1,2,7):
            lo,hi=edge_loss_interval(h,depth=8,phase_terms=10)
            self.assertGreater(lo,0)
            self.assertLess(hi-lo,Q(1,10**6))
            self.assertEqual((lo,hi),edge_loss_interval(-h,depth=8,phase_terms=10))

    def test_finite_character_loss_against_asymptotic_certificate(self):
        # Bound the finite squared modulus with independently summed rational
        # character rectangles; compare a squared, sqrt-free target interval.
        for m,h in ((2,1),(4,2),(9,1)):
            _,window=twisted_window(m)
            boxes=[box_phase(h*x,terms=10) for x in window]
            rl=sum((b[0] for b in boxes),Q())/(3*m)
            rh=sum((b[1] for b in boxes),Q())/(3*m)
            il=sum((b[2] for b in boxes),Q())/(3*m)
            ih=sum((b[3] for b in boxes),Q())/(3*m)
            low,high=edge_loss_interval(h,phase_terms=10)
            err=scaled_deficit_budget(m,h)
            delta_lo=max(Q(),(low/3-err)/m)
            delta_hi=min(Q(1),(high/3+err)/m)
            # Re(mean)>0; imaginary interval may straddle zero.
            sq_lo=rl*rl+(min(abs(il),abs(ih))**2 if il*ih>0 else 0)
            sq_hi=rh*rh+max(il*il,ih*ih)
            self.assertGreaterEqual(sq_lo,(1-delta_hi)**2)
            self.assertLessEqual(sq_hi,(1-delta_lo)**2)

    def test_boundary_layer_distinguished_from_m4_control(self):
        lower,_=edge_loss_interval(1)
        # A uniform certificate proves a positive m*deficit, incompatible
        # with a deficit O(m^-4) for this particular seam family.
        self.assertLess(scaled_deficit_budget(100,1),lower/6)
        self.assertLess(edge_complex_error(100,1),edge_complex_error(20,1))

    def test_power_series_geometric_moment(self):
        from math import factorial
        for k in (1,2,5):
            exact=edge_loss_power_coefficient(k)*factorial(2*k)*(-1)**(k+1)
            prefix=sum((Q(1,16**(2*k*j)) for j in range(5)),Q())
            remainder=Q(1,16**(10*k))/(1-Q(1,16**(2*k)))
            self.assertEqual(exact,prefix+remainder)

    def test_invalid_and_insufficient_domains_rejected(self):
        for m in (0,-1,True,Q(2)):
            with self.assertRaises(ValueError):twisted_window(m)
        with self.assertRaises(ValueError):edge_loss_interval(Q(1))
        with self.assertRaises(ValueError):edge_loss_power_coefficient(0)
        with self.assertRaises(ValueError):scaled_deficit_budget(1,100)


if __name__ == '__main__':
    unittest.main()
