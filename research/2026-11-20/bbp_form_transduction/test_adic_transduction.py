"""Finite exact arithmetic and adversarial controls for source/form transduction."""
import math
import unittest
from fractions import Fraction as F

import adic_transduction as a


class AuthenticSource(unittest.TestCase):
    def test_original_poles_and_seed(self):
        self.assertEqual(a.r(1), F(47,15))
        for n in range(1,31):
            self.assertEqual(a.state(n), 16*a.state(n-1)+a.r(n))
            self.assertGreater(a.r(n),0)
            self.assertGreater(a.r_mutant(n),a.r(n))

    def test_exact_terminal_causal_compensation(self):
        for M in (4,9,15,27):
            P=a.prefix(M)
            for n in range(M):
                self.assertEqual(a.terminal_completed(n,M),16**n*P)
                self.assertEqual(a.terminal_tail(n+1,M)-16*a.terminal_tail(n,M),-a.r(n+1))
                self.assertEqual(a.terminal_completed(n+1,M),16*a.terminal_completed(n,M))

    def test_rational_counterseed_locks_every_finite_terminal(self):
        for M in (4,9,15):
            s=-a.prefix(M)  # explicitly not the original seed
            for n in range(M+1):
                self.assertEqual(a.terminal_completed(n,M,s),0)
                self.assertEqual(a.state(n,s),-a.terminal_tail(n,M))
                self.assertEqual(a.state(n+1,s)-16*a.state(n,s),a.r(n+1))

    def test_altered_matched_jet_has_different_prime_signature(self):
        # Mutant preserves first asymptotic jet but not four signed source poles.
        for p in (7,11,13,17,19,23,29,31,37,41,43,47):
            self.assertEqual(a.event_signature(p),( -2,4))
            self.assertEqual(a.event_signature(p,mutant=True),(-2,5))

    def test_real_small_vs_p_adic_large_pole_square(self):
        # p^2 event has |r|_p=p^2 yet p^4*r -> 15 in the real metric.
        for p in (7,11,29,101,251,997):
            value=a.r(a.p2_clock(p)+1)
            self.assertEqual(a.v_p_fraction(value,p),-2)
            self.assertEqual(a.residue_mod_p(p*p*value,p),4)
            if p >= 101:
                self.assertAlmostEqual(float(p**4*value),15,delta=0.03)
                self.assertAlmostEqual(float(p**4*a.r_mutant(a.p2_clock(p)+1)),15,delta=0.03)

    def test_product_formula_is_arithmetic_not_thermodynamics(self):
        for q in (F(16),F(-3,32),F(29312,29539125),F(71,210)):
            self.assertEqual(a.rational_place_product(q),1)
        self.assertEqual(a.v_p_fraction(F(16),2),4)

    def test_pole_clock_is_integer_and_11_clock(self):
        self.assertEqual(a.p2_clock(11),15)
        self.assertEqual(a.r(16),F(29312,29539125))
        self.assertEqual(a.v_p_fraction(a.r(16),11),-2)


class CRTandPhase(unittest.TestCase):
    def test_crt_components_reassemble_in_qmodz(self):
        for q in (F(1,6),F(5,24),-F(22,105),F(71,210),F(0),F(17),
                  F(23,49),F(47,15)):
            self.assertTrue(a.canonical_reassembly(q))
            comps=a.all_primary(q)
            self.assertEqual(a.fractional(q),a.fractional(sum(comps.values(),F(0))))
            for p,x in comps.items():
                self.assertEqual(a.primary(q,p),x)

    def test_authentic_state_crt(self):
        for n in range(1,7):
            self.assertTrue(a.canonical_reassembly(a.state(n)))

    def test_cofactor_phase_product_and_gauge(self):
        q=F(137,210)
        t=F(37,819)
        for places in [(),(2,),(3,5),(2,3,5,7),(7,)]:
            A,B=a.signed_phase_split(q,t,places)
            self.assertAlmostEqual(abs(A*B-a.character(q+t)),0.,places=13)
            g=a.character(F(11,29))
            self.assertAlmostEqual(abs((A*g)*(g.conjugate()*B)-A*B),0.,places=13)
            self.assertAlmostEqual(abs(B-A.conjugate()),abs(A*B-1),places=13)

    def test_original_terminal_rational_full_phase(self):
        M=9
        for n in (1,3,6,8):
            q=a.state(n)
            t=a.terminal_tail(n,M)
            places=tuple(a.all_primary(q).keys())
            A,B=a.signed_phase_split(q,t,places)
            self.assertAlmostEqual(abs(A*B-a.character(16**n*a.prefix(M))),0,places=12)
            # finite terminal counterseed forces an *exactly* locked complex phase
            A,Bl=a.signed_phase_split(q,t+16**n*(-a.prefix(M)),places)
            self.assertAlmostEqual(abs(Bl-A.conjugate()),0,places=12)
            self.assertAlmostEqual(abs(A*Bl-1),0,places=12)


class GaussianRepresentation(unittest.TestCase):
    def test_resolution_transport_raw_commutator(self):
        # actual pushforward of Gaussian differs from smoothing the pushed point
        for lam in (0.1,0.5,1.0):
            raw=a.gaussian_form_defect(lam)
            self.assertGreater(raw,0.)
            # translating either kernel by arbitrary phase leaves norm unchanged
            for theta in (0., 0.135, 0.5):
                direct=0.
                for k in range(1,25):
                    x=math.exp(-lam*k*k/2)
                    y=math.exp(-256*lam*k*k/2)
                    # complex Fourier difference after common shift e(-k 16theta)
                    omega=a.character(F.from_float(-16*theta), k)
                    direct += 2*abs((x-y)*omega)**2
                self.assertAlmostEqual(direct, raw, places=12)

    def test_matching_width_kills_form_defect(self):
        for k in range(1,10):
            lam=0.08
            self.assertEqual(math.exp(-256*lam*k*k/2),
                             math.exp(-(16**2)*lam*k*k/2))

    def test_small_resolution_asymptotic(self):
        for lam in (0.0006,0.001,0.003):
            H=math.ceil(math.sqrt(85/lam))
            value=a.gaussian_form_defect(lam,H=H)
            predicted=math.sqrt(math.pi/lam)*a.form_defect_small_width_coefficient()
            self.assertAlmostEqual(value/predicted,1.,delta=0.0002)

    def test_gaussian_cross_term_is_mandatory(self):
        for u,t in ((F(1,7),F(1,21)),(F(37,101),F(-5,12)),(F(-1,15),F(1,15))):
            total,src,bnd,cross=a.gaussian_signed_interference(u,t)
            self.assertAlmostEqual(total,src+bnd+cross,places=12)
        total,src,bnd,cross=a.gaussian_signed_interference(F(-1,15),F(1,15))
        self.assertAlmostEqual(total,0.,places=12)
        self.assertGreater(src,0.1)
        self.assertAlmostEqual(src,bnd,places=12)
        self.assertAlmostEqual(cross,-src-bnd,places=12)
        self.assertGreater(src+bnd,0.1)  # false positive if cross omitted

    def test_exact_rational_terminal_cancelled_energy(self):
        M=8
        seed=-a.prefix(M)
        for n in range(1,M):
            u=a.state(n,seed)
            t=a.terminal_tail(n,M)
            total,src,bnd,cross=a.gaussian_signed_interference(u,t)
            self.assertAlmostEqual(total,0.,places=11)
            self.assertAlmostEqual(src+bnd+cross,0.,places=11)

    def test_prime_signed_decomposition_does_not_change_target(self):
        q=F(47,15)
        t=F(1,123)
        target=a.gaussian_displacement(q+t)
        for places in [(),(3,),(5,),(3,5)]:
            s=sum((a.primary(q,p) for p in places),F(0))
            energy,source,bnd,cross=a.gaussian_signed_interference(s,q-s+t)
            self.assertAlmostEqual(energy,target,places=12)
            self.assertAlmostEqual(energy,source+bnd+cross,places=12)


class SparsityAndFeedback(unittest.TestCase):
    def test_pole_square_sparse_support(self):
        # This is a *counting bound*, not a claim real BBP influence is local.
        for B in (100,10000,1000000):
            self.assertLessEqual(a.sparse_pulse_mass_upper(B,1),a.shell_pulse_count(B)/B)
            self.assertLessEqual(a.sparse_pulse_mass_upper(B,10),10*a.shell_pulse_count(B)/B)
        self.assertLess(a.sparse_pulse_mass_upper(100000000,64),0.03)

    def test_feedback_requires_a_real_coupled_action(self):
        zero=lambda n,s:0
        one=lambda n,s:1
        self.assertNotEqual(a.feedback_history(0,zero,8,True),
                            a.feedback_history(0,one,8,True))
        self.assertEqual(a.feedback_history(0,zero,8,False),
                         a.feedback_history(0,one,8,False))

    def test_invalid_domains_rejected(self):
        for fn,args in ((a.r,(0,)),(a.prefix,(-1,)),(a.state,(-1,)),
                        (a.primary,(F(1,2),1)),(a.terminal_tail,(3,2)),
                        (a.v_p_fraction,(F(0),7))):
            with self.assertRaises(ValueError):fn(*args)


if __name__=='__main__':unittest.main()
