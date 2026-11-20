"""Reproducible exact and finite spectral controls (stdlib unittest)."""
import cmath
import math
import unittest
from fractions import Fraction as F
import causal_fourier as c


class RadixClock(unittest.TestCase):
    def test_clock_16_recurrence(self):
        for n in range(80):
            self.assertEqual(c.clock(n+1),16*c.clock(n)+1)
            self.assertEqual(c.clock(n),sum(16**j for j in range(n)))

    def test_coupled_3_5_isometries(self):
        for p in (3,5):
            for m,n in ((0,1),(1,2),(13,24),(11,56),(0,625),(30,290),(512,911)):
                self.assertEqual(c.valuation_integer(c.clock(m)-c.clock(n),p),
                                 c.valuation_integer(m-n,p))

    def test_clock_is_single_cycle_at_3_5(self):
        for p in (3,5):
            for k in (1,2,3,4):
                m=p**k
                vals=[c.clock(n)%m for n in range(m)]
                self.assertEqual(len(set(vals)),m)
                self.assertEqual(vals[0],0)
                self.assertEqual(c.clock(m)%m,0)

    def test_joint_3_5_crt_15adic_clock(self):
        for k in (1,2,3):
            m=15**k
            self.assertEqual(len({c.clock(n)%m for n in range(m)}),m)
            self.assertEqual(c.clock(m)%m,0)

    def test_clock_inverse_log_residues(self):
        for p,k in ((3,2),(3,4),(5,2),(5,3)):
            m=p**k
            for n in range(m):
                self.assertEqual(c.clock_label(c.clock(n),p,k),n)
                self.assertEqual(c.clock_label(c.clock(n+1),p,k),(n+1)%m)

    def test_coherent_fourier_eigencharacters(self):
        for p,k,a in ((3,3,1),(3,3,7),(5,2,1),(5,2,6)):
            q=p**k
            phase=cmath.exp(2j*math.pi*a/q)
            for n in (0,1,2,q-1,q,q+2):
                before=c.clock_character(p,k,a,c.clock(n))
                after=c.clock_character(p,k,a,c.clock(n+1))
                self.assertLess(abs(after-phase*before),1e-12)

    def test_fourier_orthogonality(self):
        for p,k in ((3,3),(5,2)):
            q=p**k
            for h in (1,2,q-1):
                self.assertLess(abs(sum((c.clock_character(p,k,h,c.clock(n))
                                         for n in range(q)),0j)),1e-12)

    def test_additive_state_characters_mix_at_higher_resolution(self):
        # ψ_a(TJ)=ψ_a(1) ψ_(16a)(J), not generally ψ_a(J) times a scalar.
        for p in (3,5):
            k=2
            q=p**k
            for J in (0,1,2,q-1):
                lhs=c.additive_state_character(p,k,1,16*J+1)
                rhs=c.additive_state_character(p,k,1,1)*c.additive_state_character(p,k,16,J)
                self.assertLess(abs(lhs-rhs),2e-12)
            ratios=[c.additive_state_character(p,k,1,16*J+1)/c.additive_state_character(p,k,1,J)
                    for J in (0,1,2)]
            self.assertGreater(abs(ratios[1]-ratios[0]),0.1)

    def test_exact_causal_eigenbasis_and_unitary_transport(self):
        for p,k in ((3,2),(5,2)):
            q=p**k
            C=c.clock_to_state_fourier_change(p,k)
            for a in range(q):
                for b in range(q):
                    v=sum((C[a][j]*C[b][j].conjugate() for j in range(q)),0j)
                    self.assertLess(abs(v-(1 if a==b else 0)),2e-12)
            for a in (0,1,q-1):
                for J in range(q):
                    reconstructed=sum((C[a][b]*c.additive_state_character(p,k,b,J)
                                       for b in range(q)),0j)
                    self.assertLess(abs(reconstructed-c.clock_character(p,k,a,J)),2e-12)

    def test_2adic_trajectory_attractor_and_clock_discontinuity(self):
        for n in (0,1,2,7,31):
            gap=F(c.clock(n))+F(1,15)
            self.assertEqual(gap,F(16**n,15))
            self.assertEqual(c.valuation_integer(gap.numerator,2),4*n)
            self.assertEqual(gap.denominator%2,1)
        # n=2^k -> 0 as a 2-adic CLOCK, but J_n never tends to J_0=0.
        for k in (1,2,4,7):
            self.assertEqual(c.clock(2**k)%8,1)

    def test_rational_product_of_places(self):
        for n in (0,1,3,9,35):
            delta=F(16**n,15)
            real=delta
            norm2=F(1,16**n)
            norm3=3
            norm5=5
            self.assertEqual(real*norm2*norm3*norm5,1)


class AuthenticSource(unittest.TestCase):
    def test_four_original_poles(self):
        self.assertEqual(c.forcing(1),F(47,15))
        self.assertEqual(c.forcing(2),F(106,819))
        for n in range(1,55):
            self.assertEqual(c.forcing(n),
                             F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))
            self.assertGreater(c.forcing(n),0)

    def test_exact_source_time_coefficient(self):
        self.assertEqual(c.source_coefficient(1),F(47,240))
        self.assertEqual(c.source_coefficient(2),F(53,104832))
        self.assertEqual(c.source_time_gap_constant(),F(2491,12579840))

    def test_source_time_gap_for_all_sampled_frequencies(self):
        for M in (2,3,8,20):
            mass=float(c.source_prefix(M))
            for j in range(1,100):
                omega=2*math.pi*j/100
                measured=mass**2-abs(c.source_time_fourier(omega,M))**2
                self.assertGreaterEqual(measured+2e-14,c.finite_source_time_gap_lower(omega))
                self.assertGreater(measured,0)

    def test_source_time_first_moments(self):
        # -d²|F|²/dω² at zero = 2(M0*M2-M1²), positive by exact variance.
        M=15
        m0=sum((c.source_coefficient(n) for n in range(1,M+1)),F(0))
        m1=sum((n*c.source_coefficient(n) for n in range(1,M+1)),F(0))
        m2=sum((n*n*c.source_coefficient(n) for n in range(1,M+1)),F(0))
        self.assertGreater(m0*m2-m1*m1,0)
        self.assertGreaterEqual(m0*m2-m1*m1,F(1)*c.source_coefficient(1)*c.source_coefficient(2))

    def test_seed_blindness_of_source_time_fourier(self):
        # The FORCING spectrum is independent of any homogeneous seed.
        for s in (F(0),F(1,16),F(-1,3)):
            self.assertEqual(c.state(5,s)-16**5*s,c.state(5))
        self.assertAlmostEqual(c.source_time_fourier(0,22).real,math.pi/16,places=13)

    def test_mutant_generic_source_time_gap(self):
        for n in (1,2,7,30):
            self.assertGreater(c.mutant_forcing(n),c.forcing(n))
        self.assertLess(abs(c.source_time_fourier(0.3,10,True)),
                        float(sum((c.mutant_forcing(n)/16**n for n in range(1,11)),F(0))))


class CausalAtoms(unittest.TestCase):
    def test_exact_affine_source_atom(self):
        for h in (1,3,-7):
            for n in (1,2,3,5,11):
                pulses=tuple(c.forcing(j) for j in range(1,n+1))
                self.assertLess(abs(c.affine_causal_atom(pulses,h)-c.character(c.state(n),h)),2e-12)

    def test_source_order_twist_is_essential(self):
        a,b=F(1,7),F(2,11)
        u=16*a+b
        correct=c.character(16*a)*c.character(b)
        naive=c.character(a)*c.character(b)
        self.assertLess(abs(c.character(u)-correct),1e-12)
        self.assertGreater(abs(c.character(u)-naive),0.1)
        self.assertEqual(c.affine_swap_defect(a,b),15*(a-b))

    def test_terminal_split_exact(self):
        for M in (5,12,25):
            P=c.source_prefix(M)
            for n in range(M+1):
                self.assertEqual(c.completed_terminal(n,M),16**n*P)
                self.assertLess(abs(c.character(c.completed_terminal(n,M))-
                                    c.phase_from_terminal(n,M)),1e-12)
            for n in range(M):
                self.assertEqual(c.finite_tail(n+1,M)-16*c.finite_tail(n,M),
                                 -c.forcing(n+1))

    def test_locked_changed_seed_control(self):
        M=18
        locked=-c.source_prefix(M)
        for n in range(M+1):
            self.assertEqual(c.completed_terminal(n,M,locked),0)
            self.assertEqual(c.state(n,locked)-c.state(n),16**n*locked)

    def test_shell_tail_error_uniform_and_frequency_cost(self):
        for B in (2,4,8):
            M=2*B
            large=c.source_prefix(M+55)
            for h in (1,7,31):
                bound=c.terminal_shell_error_bound(B,h)
                for n in range(B,2*B):
                    real=c.character(16**n*large,h)
                    approx=c.phase_from_terminal(n,M,h)
                    self.assertLessEqual(abs(real-approx),bound+1e-13)
                self.assertLessEqual(abs(sum((c.character(16**n*large,h)-c.phase_from_terminal(n,M,h)
                                              for n in range(B,2*B)),0j)/B),bound+1e-13)

    def test_koopman_frequency_dilation(self):
        x=F(8,179)
        for h in (1,7,-3):
            self.assertLess(abs(c.character(16*x,h)-c.character(x,16*h)),1e-12)
            self.assertLess(abs(c.character(16**5*x,h)-c.character(x,16**5*h)),1e-12)

    def test_finite_fourier_support_unbounded_under_radix(self):
        support={-7,1,5}
        image=set(support)
        for k in range(1,8):
            image={16*s for s in image}
            self.assertFalse(image & support)

    def test_finite_terminal_integer_alias_not_seed_identity(self):
        s=F(1,16)
        for n in range(1,8):
            self.assertLess(abs(c.character(c.state(n,s))-c.character(c.state(n))),1e-12)
        self.assertNotEqual(c.state(0,s),c.state(0))


if __name__ == '__main__':
    unittest.main()
