"""Exact source and hostile finite two-chiral-tower regression."""
import unittest
from fractions import Fraction as Q
from observational_succ import rank_two_chiral_towers as m


class RankTwoChiral(unittest.TestCase):
    def test_gaussian_ring_and_involution(self):
        cases=(m.ZERO,m.ONE,m.G,m.G_BAR,m.Gaussian(-3,Q(2,7)))
        for a in cases:
            for b in cases:
                self.assertEqual((a*b).conj(),a.conj()*b.conj())
                self.assertEqual((a*b).norm(),a.norm()*b.norm())
                self.assertEqual((a+b).conj(),a.conj()+b.conj())
        self.assertEqual(m.G*m.G_BAR,m.Gaussian(Q(1,2)))

    def test_independent_multiplications_commute_but_J_exchanges_them(self):
        states=[m.RankTwo(m.Gaussian(a,b),m.Gaussian(c,d))
                for a,b,c,d in ((1,2,3,4),(-2,1,0,1),(0,0,1,0))]
        for x in states:
            self.assertEqual(m.independent_left(m.independent_right(x)),
                             m.independent_right(m.independent_left(x)))
            self.assertEqual(m.chirality(m.chirality(x)),x)
            self.assertEqual(m.chirality(m.independent_left(m.chirality(x))),
                             m.independent_right(x))
            self.assertEqual(m.chirality(m.independent_right(m.chirality(x))),
                             m.independent_left(x))
            self.assertEqual(x.multiply(m.UNIT),x)
            self.assertEqual(m.chirality(x.multiply(x)),
                             m.chirality(x).multiply(m.chirality(x)))

    def test_even_odd_parity_and_product_grading(self):
        a=m.from_sectors(m.Gaussian(2,3),m.ZERO)
        b=m.from_sectors(m.ZERO,m.Gaussian(1,-1))
        self.assertEqual(m.chirality(a),a)
        self.assertEqual(m.chirality(b),-b)
        self.assertEqual(m.chirality(a.multiply(b)),-a.multiply(b))
        self.assertEqual(m.chirality(b.multiply(b)),b.multiply(b))
        for x in (m.ORIGIN,a,b,a+b):
            e,o=m.split(x)
            self.assertEqual(e+o,x)
            self.assertEqual(m.chirality(e),e)
            self.assertEqual(m.chirality(o),-o)
            self.assertEqual(m.source_readout(x),sum(m.chiral_readouts(x)))

    def test_chiral_successor_twist_and_eighth_return(self):
        for z,w in ((m.ONE,m.ZERO),(m.G,m.G_BAR),
                    (m.Gaussian(1,2),m.Gaussian(3,4)),(m.ZERO,m.ONE)):
            x=m.RankTwo(z,w)
            self.assertEqual(m.iterate(x,4),m.chirality(x).scale(Q(-1,4)))
            self.assertEqual(m.iterate(x,8),x.scale(Q(1,16)))
            self.assertEqual(m.source_successor(m.chirality(x)),
                             m.chirality(m.source_successor(x)))

    def test_transfer_polynomial_minimal_rational_dimension(self):
        self.assertEqual(m.polynomial_denominator(),
                         (Q(1),Q(-1),Q(0),Q(1,2),Q(-1,4)))
        self.assertEqual(m.transfer_numerator_from_first_terms(),
                         (Q(4),Q(-4),Q(0),Q(0),Q(0)))
        self.assertEqual(m.G.norm(),Q(1,2))

    def test_all_128_source_impulses_and_8_return(self):
        state=m.ORIGIN
        for n in range(128):
            self.assertEqual(m.source_readout(state),m.impulse(n))
            state=m.source_successor(state)

    def test_exact_chiral_cancellation_and_first_moment(self):
        even,odd=m.first_shell_channels()
        self.assertEqual(even,(Q(4),Q(2),Q(0),Q(-1),Q(-1),Q(-1,2),Q(0),Q(1,4)))
        self.assertEqual(odd,(Q(0),Q(-2),Q(0),Q(-1),Q(0),Q(-1,2),Q(0),Q(-1,4)))
        self.assertEqual(m.source_8_shell_sums(),(Q(15,4),Q(-15,4),Q(-15)))
        self.assertEqual(tuple(a+b for a,b in zip(even,odd)),m.TAPS)

    def test_actual_original_four_poles_and_zero_seed(self):
        state=Q(0)
        for n in range(1,48):
            a=m.source_moment(n)
            self.assertEqual(a,m.authentic_four_poles(n))
            self.assertEqual(m.source_moment(n,channel='even')+m.source_moment(n,channel='odd'),a)
            self.assertGreater(a,0)
            state=16*state+a
            self.assertEqual(state,m.original_zero_seed_prefix(n))

    def test_complete_eight_shell_integral_matches_original_bbp(self):
        for N in (1,2,3,5,8,12):
            impulse_moment=sum((m.impulse(k)/Q(k+1) for k in range(8*N)),Q(0))
            bbp_prefix=sum((m.authentic_four_poles(n)/16**(n-1) for n in range(1,N+1)),Q(0))
            self.assertEqual(impulse_moment,bbp_prefix)

    def test_no_ghost_correlation_not_independence(self):
        x=m.Gaussian(1,2)
        self.assertEqual(m.validate_common_source_even(x,x.conj()),m.RankTwo(x,x.conj()))
        with self.assertRaises(ValueError): m.validate_common_source_even(x,x)
        joint=m.conditional_binary_joint()
        self.assertEqual(sum(joint.values(),Q(0)),Q(1))
        self.assertEqual(joint[(0,0)],Q(5,16))
        self.assertEqual(joint[(1,1)],Q(5,16))
        self.assertEqual(m.covariance_binary(joint),Q(1,16))
        self.assertTrue(all(v>0 for v in joint.values()))
        # Correlated diagonal data would not support one-sided bit flips.
        diagonal={(0,0):Q(1,2),(1,1):Q(1,2)}
        self.assertNotIn((1,0),diagonal)

    def test_mutations_break_source_identity(self):
        # Loss of relative chirality: replacing bar(g) by g fails J intertwining.
        x=m.RankTwo(m.ONE,m.ONE)
        wrong=lambda v:m.RankTwo(v.left,m.G*v.right)
        self.assertNotEqual(m.chirality(m.independent_left(m.chirality(x))),wrong(x))
        # Removing the odd E tower destroys the first sparse zero tap.
        even,odd=m.first_shell_channels()
        self.assertNotEqual(even[1],m.TAPS[1])
        # Flipping the relative odd readout sign destroys cancellation.
        self.assertNotEqual(even[1]-odd[1],m.TAPS[1])
        self.assertNotEqual(sum(even,Q(0)),0)

    def test_global_point_conserves_source_tags_and_quantifies_work(self):
        p=m.MacroEPoint.original()
        for n in range(20):
            self.assertEqual(p.source,m.SOURCE)
            self.assertEqual(p.time,n)
            self.assertEqual(p.views()[2],m.impulse(n))
            p=p.advance()
        with self.assertRaises(ValueError):
            m.MacroEPoint('unauthenticated',0,m.ORIGIN).advance()

    def test_linear_source_phase_cannot_prove_real_normality(self):
        self.assertEqual(m.signed_phase_no_go_bound_pi_units(1),Q(256,15))
        self.assertEqual(m.signed_phase_no_go_bound_pi_units(-2),Q(512,15))
        with self.assertRaises(ValueError): m.signed_phase_no_go_bound_pi_units(0)
        self.assertEqual(sum(abs(t) for t in m.TAPS)*Q(16,15),Q(128,15))


    def test_independent_zero_seed_towers_and_phase_multiplication(self):
        for n in range(0,64):
            left,right=m.chiral_zero_seed_states(n)
            self.assertEqual(left+right,m.original_zero_seed_prefix(n))
            for h in (1,-2,3):
                a,b,c=m.chiral_phase_remainders(n,h)
                self.assertEqual((a+b)%1,c)
                self.assertEqual(c,(h*m.original_zero_seed_prefix(n))%1)

    def test_source_hankel_rank_four_and_mutated_single_lane(self):
        self.assertEqual(m.shell_hankel_det(),Q(4))
        self.assertEqual(m.source_8_shell_sums(),(Q(15,4),Q(-15,4),Q(-15)))
        for n in (1,2,3,8,17,31):
            self.assertNotEqual(m.source_moment(n,channel="even"),
                                m.authentic_four_poles(n))

    def test_two_lane_harmonic_leading_terms(self):
        # Exact asymptotic coefficient is 15/32 for the separate lanes,
        # and 15/64 for the coherent sum after cancellation.
        for n in (12,32,128,512):
            u=m.source_moment(n,channel="even")
            v=m.source_moment(n,channel="odd")
            self.assertGreater(u,0)
            self.assertLess(v,0)
            self.assertLess(abs(n*u-Q(15,32)),Q(2,n))
            self.assertLess(abs(n*v+Q(15,32)),Q(2,n))
            self.assertLess(abs(n*n*(u+v)-Q(15,64)),Q(3,n))

    def test_input_budget_and_type_guard(self):
        for bad in (-1,1.5,20001,True):
            with self.assertRaises(ValueError):m.iterate(m.ORIGIN,bad)
        for bad in (0,-1,1.1):
            with self.assertRaises(ValueError):m.source_moment(bad)
        with self.assertRaises(ValueError):m.source_moment(1,channel='impossible')

if __name__=='__main__':unittest.main()
