"""Virtual-form terminal BBP metric: exact source fractions and hostile shadows.

All source certificate assertions are exact rational arithmetic; no numerical pi
or hidden stochastic digits. R0 and pi normality are not proven by finite tests.
"""
from fractions import Fraction as F
from functools import lru_cache
import unittest


def forcing(n):
    if n < 1:
        raise ValueError('positive original BBP source index required')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


@lru_cache(None)
def terminal_state(m):
    u = F(0)
    for n in range(1, m+1):
        u = 16*u + forcing(n)
    return u


def torus_distance(y):
    residue = F(y) % 1
    return min(residue, 1-residue)


def rational_form_norm_squared(B):
    """R_B, averaged squared distance of backward terminal radix views."""
    if B < 1:
        raise ValueError('positive shell start required')
    u = terminal_state(2*B)
    return sum((torus_distance(u / (16**k))**2
                for k in range(1,B+1)), F(0))/B


def terminal_digit_count(B):
    """Count positions in 4..11 of the least significant B hex digits."""
    u = terminal_state(2*B)
    C = u.numerator//u.denominator
    return sum(4 <= ((C // (16**(k-1))) % 16) <= 11
               for k in range(1, B+1))


def phase_energy_lower(B):
    """Fully rational source-certified lower bound on 1-Re W_B(pi/16)."""
    return 8*rational_form_norm_squared(B) - F(8, 225*B)*forcing(2*B+1)


def periodic_shadow_of_prefix(x, m):
    """Repeat m base16 digits, then zero, forever; no all-F ambiguity."""
    if not (F(0) <= x < F(1)) or m < 1:
        raise ValueError('canonical unit interval and positive prefix')
    A = (x*(16**m)).numerator//(x*(16**m)).denominator
    return F(16*A,16**(m+1)-1)


class VirtualFormMetricTests(unittest.TestCase):
    def test_exact_original_zero_seed_and_endpoint_equality(self):
        for m in (1,2,4,9,32,128,512):
            direct = sum((forcing(j)/16**j for j in range(1,m+1)), F(0))
            self.assertEqual(terminal_state(m), 16**m*direct)
            self.assertGreater(terminal_state(m),0)
            self.assertGreater(forcing(m+1),0)

    def test_reversed_single_endpoint_form_equals_forward_shell_form(self):
        for B in (2,4,16,32,64):
            u = terminal_state(2*B)
            P = u / (16**(2*B))
            forward = sum((torus_distance((16**n)*P)**2
                           for n in range(B,2*B)),F(0))/B
            self.assertEqual(forward,rational_form_norm_squared(B))

    def test_exact_source_tail_upper_bound(self):
        for m in (1,2,16,32,64,128,256,512):
            beta = forcing(m+1)/15
            self.assertGreater(beta,0)
            self.assertLess(beta, F(1,(8*m+1)*(8*m+2)))

    def test_exact_radial_geometric_weight_sum(self):
        for B in (1,2,4,8,32,128):
            lhs = sum((F(1,16**(4*B-2*n))
                       for n in range(B,2*B)), F(0))/B
            rhs = (F(1)-F(1,16**(2*B)))/(255*B)
            self.assertEqual(lhs,rhs)

    def test_all_rational_finite_certificate_exceeds_three_fifths(self):
        for B in (16,32,64,128,256):
            R = rational_form_norm_squared(B)
            self.assertGreater(R, F(0))
            self.assertLessEqual(R,F(1,4))
            self.assertGreater(phase_energy_lower(B),F(3,5),f'B={B}')

    def test_terminal_middle_digit_criterion(self):
        for B in (2,4,8,16,32,64,128,256):
            M = terminal_digit_count(B)
            self.assertGreaterEqual(M,0)
            self.assertLessEqual(M,B)
            self.assertGreaterEqual(rational_form_norm_squared(B),F(M,16*B))
        self.assertEqual([terminal_digit_count(B) for B in (16,32,64,128,256)],
                         [6,14,33,66,142])

    def test_periodic_prefix_shadow_is_rational_and_shares_prefix(self):
        examples=(F(3,16)+F(7,16**3),F(5,17),F(1,256))
        for x in examples:
            for m in (1,2,3,5,8):
                q = periodic_shadow_of_prefix(x,m)
                self.assertLess(abs(x-q),F(1,16**m))
                A=(16**m*x).numerator//(16**m*x).denominator
                Aq=(16**m*q).numerator//(16**m*q).denominator
                self.assertEqual(A,Aq)
                self.assertTrue(0 <= q < 1)

    def test_horizon_alias_loses_initial_source_label(self):
        # Shell observers cannot distinguish integer /16^B source shifts.
        for B in (1,4,12):
            x=F(1,7)
            y=x+F(1,16**B)
            self.assertNotEqual(x,y)
            for n in range(B,2*B):
                self.assertEqual((16**n*(x-y))%1,0)

    def test_zero_and_fixed_nonunit_phase_controls(self):
        for n in (1,2,16):
            self.assertEqual((16**n*F(0))%1,0)
            self.assertEqual((16**n*F(1,15))%1,F(1,15))
        # A fixed nonunit orbit has R0, but periodic-form distance to zero
        # remains nonzero; being periodic is NOT equivalent to locking at 1.
        self.assertNotEqual(F(1,15)%1,F(0))

    def test_periodic_shadow_not_a_source_compatibility_claim(self):
        # A rational prefix shadow is not silently the exact infinite forcing.
        P=terminal_state(16)/16**16
        self.assertNotEqual(16*P,terminal_state(1))
        # The same original forcing with a changed seed produces U_m(s)
        # =U_m(0)+16^m*s, preserving the source but changing the phase.
        s=F(1,16)
        u_s=s
        for m in range(1,9):
            u_s=16*u_s+forcing(m)
            self.assertEqual(u_s,terminal_state(m)+16**m*s)


if __name__=='__main__': unittest.main()
