"""Exact finite controls for original four-pole source rank-r lattice."""
import unittest
from fractions import Fraction as Q
from itertools import product
from math import pi, tau, cos, sin

from observational_succ.pi_rank_lattice import (
    authentic_r, canceled_r, original_state, pi_source_prefix,
    finite_green_tail, green_tail_upper, selected_lattice_state,
    flat_square, transverse_multiplier, certified_rank_transport_bound,
    transverse_trace_recovery, _ceil_sqrt_fraction
)


class SourceRankLatticeTests(unittest.TestCase):
    def test_source_is_signed_original_four_poles(self):
        self.assertEqual(original_state(0),0)
        for n in range(1,80):
            self.assertEqual(authentic_r(n),canceled_r(n))
            self.assertGreater(authentic_r(n),0)
            self.assertEqual(authentic_r(n).denominator%2,1)

    def test_native_four_poles_if_available(self):
        try:
            from observational_succ.succ_internal_matrix_walk import authentic_r as repo_r
        except ModuleNotFoundError:
            self.skipTest('full upstream SUCC package unavailable in isolated environment')
        for n in range(1,100):
            self.assertEqual(repo_r(n),authentic_r(n))

    def test_zero_seed_rational_states(self):
        state=Q(0)
        for n in range(1,34):
            state=16*state+authentic_r(n)
            self.assertEqual(state,original_state(n))

    def test_original_green_identity_exact(self):
        for L in (8,17,40):
            pi_L=pi_source_prefix(L)
            for n in range(1,L+1):
                tail=finite_green_tail(n,L)
                self.assertEqual(Q(16**(n-1))*pi_L-original_state(n),tail)
                self.assertGreaterEqual(tail,0)
                self.assertLess(tail,green_tail_upper(n))

    def test_flat_squares_rank_two_and_all_rank_three(self):
        for multipliers in ((3,), (3,5),(3,5,7)):
            for n in range(9):
                for multi in product(range(3),repeat=len(multipliers)):
                    for axis in range(len(multipliers)):
                        a,b=flat_square(n,multi,multipliers,axis)
                        self.assertEqual(a,b)
                        shifted=tuple(k+(j==axis) for j,k in enumerate(multi))
                        self.assertEqual(a,selected_lattice_state(n+1,shifted,multipliers))

    def test_prime_clocks_are_not_real_winding(self):
        # Exact rational states in Z2 need not have coincident real winding.
        a=Q(32,3)
        b=Q(0)
        self.assertEqual((a.numerator*pow(a.denominator,-1,16))%16,0)
        self.assertEqual((b.numerator*pow(b.denominator,-1,16))%16,0)
        self.assertNotEqual(a.numerator//a.denominator,b.numerator//b.denominator)

    def test_integer_ceil_root_no_undercount(self):
        for num in range(0,100):
            for den in range(1,17):
                r=Q(num,den)
                root=_ceil_sqrt_fraction(r)
                self.assertGreaterEqual(root**2,r)
                if root:
                    self.assertLess((root-1)**2,r)

    def test_certified_rank_bounds(self):
        for multipliers,widths in [((3,),(1,)), ((3,),(5,)), ((3,5),(4,3)), ((3,5,7),(3,2,2))]:
            for h in (0,1,3,-3):
                b=certified_rank_transport_bound(120,widths,multipliers,h)
                self.assertIsInstance(b,Q)
                self.assertGreaterEqual(b,0)
                self.assertLessEqual(b,2)
                if h==0:self.assertEqual(b,0)
        for invalid in [((3,),(0,)), ((3,5),(3,)), ((1,),(2,))]:
            with self.assertRaises(ValueError):
                certified_rank_transport_bound(10,invalid[1],invalid[0],1)

    def test_numeric_comparison_is_inside_certified_envelope(self):
        # Numeric phasors here only test the code's analytic upper bound.
        # Exact/source identities and the bound's proof are distinct.
        L=38
        alpha_L=pi_source_prefix(L)
        for N,M in ((4,2),(9,4),(13,6)):
            for h in (1,2):
                def phase(value):
                    v=value % 1  # reduce Fraction before converting to float
                    angle=tau*float(v)
                    return complex(cos(angle),sin(angle))
                s=complex(0)
                for n in range(N):
                    for m in range(M):
                        scale=3**m
                        s+=phase(h*scale*original_state(n+1))-phase(h*scale*16**n*alpha_L)
                discrepancy=abs(s)/(N*M)
                # Prefix pi_L differs from pi by <(4/15)*16**(1-L).
                prefix_error=Q(44,7)*abs(h)*Q(4,15)*Q(1,16**(L-1))*sum(16**n for n in range(N))*sum(3**m for m in range(M))/Q(N*M)
                certified=certified_rank_transport_bound(N,(M,),(3,),h)
                self.assertLess(discrepancy,float(certified+prefix_error)+1e-10)

    def test_rank_two_cochain_trace_identity(self):
        for sequence in [(Q(1),), (Q(1),Q(1),Q(1)), (Q(1),Q(-1),Q(1),Q(-1)), (Q(3),Q(7),Q(1),Q(9))]:
            avg,defect,head=transverse_trace_recovery(sequence)
            self.assertEqual(avg+defect,head)
        # Exact counterexample: Haar rank-two average zero does not
        # determine the first transverse slice.
        avg,defect,head=transverse_trace_recovery((Q(1),Q(-1)))
        self.assertEqual(avg,0)
        self.assertEqual(defect,1)
        self.assertEqual(head,1)

    def test_changed_seed_still_flat_not_selected(self):
        # Same forcing, altered initial seed; flatness is insufficient.
        pi_L=pi_source_prefix(30)
        seed= -pi_L/16
        for n in range(1,13):
            changed=original_state(n)+(16**n)*seed
            self.assertEqual(changed,-finite_green_tail(n,30))
            self.assertLess(abs(changed),green_tail_upper(n))
        # Exact original source does not determine real normality without seed.


if __name__=='__main__':unittest.main()
