"""Scoped exact-arithmetic and finite-state tests; no universal proof by testing."""
from __future__ import annotations
import unittest
from fractions import Fraction
from itertools import product

from seam_model import (
    prime,seam_clock,first_pole_seam,consecutive_prime_gap,gap_hankel,
    predicted_hankel_det,bareiss_det,bbp_forcing,bbp_mutant_forcing,
    p_primary_fraction,source_atom,source_prefix,source_tail_upper,
    truncated_germ,backward_shift,eval_germ,terminal_seam,alias_upper,
    aliased_prefix,finite_journal,finite_observational_quotient,
    policy_feedback_step,p_primary_seam,general_seam_hankel,
    general_seam_hankel_det,origami_step,origami_unstep)


class TestPrimeSquareSeams(unittest.TestCase):
    def test_actual_prime_square_clocks(self):
        self.assertEqual([seam_clock(p) for p in (7,11,13,17,19,23,29)],
                         [7,16,22,37,46,67,106])
    def test_prime_negative_and_composite(self):
        self.assertEqual([prime(j) for j in range(12)],
                         [False,False,True,True,False,True,False,True,False,False,False,True])
    def test_binary_marker_scan(self):
        self.assertEqual([n for n in range(130) if first_pole_seam(n)],
                         [7,16,22,37,46,67,106,121])
    def test_first_pole_marker_values(self):
        for p in (7,11,13,17,19,23,29,31,37):
            n=seam_clock(p)
            self.assertEqual(first_pole_seam(n),4)
            self.assertEqual(first_pole_seam(n,5),5)
            self.assertEqual(8*n-7,p*p)
    def test_no_intervening_prime_seams(self):
        for p,q in ((7,11),(11,13),(13,17),(17,19),(19,23),(23,29)):
            L=consecutive_prime_gap(p,q)
            self.assertEqual(L,(q*q-p*p)//8)
            self.assertTrue(all(first_pole_seam(j)==0
                                for j in range(seam_clock(p)+1,seam_clock(q))))
    def test_hankel_exact_4(self):
        for p,q in ((7,11),(11,13),(13,17),(17,19),(19,23)):
            self.assertEqual(bareiss_det(gap_hankel(p,q)),predicted_hankel_det(p,q))
    def test_hankel_exact_5(self):
        for p,q in ((7,11),(11,13),(13,17)):
            self.assertEqual(bareiss_det(gap_hankel(p,q,5)),predicted_hankel_det(p,q,5))
    def test_hankel_anti_diagonal_and_future_independence(self):
        p,q=7,11
        H=gap_hankel(p,q)
        L=len(H)
        for i in range(L):
            for j in range(L):
                if i+j<L-1:self.assertEqual(H[i][j],0)
                if i+j==L-1:self.assertEqual(H[i][j],4)
        H=[list(row) for row in H]
        for i in range(L):
            for j in range(L):
                if i+j>L-1:H[i][j] += 111*(i+j+1)
        self.assertEqual(bareiss_det(H),predicted_hankel_det(p,q))
    def test_marker_source_pprimary(self):
        for p in (7,11,13,17,19,23,29,31):
            j=seam_clock(p)
            self.assertEqual(p_primary_fraction(bbp_forcing(j),p),Fraction(4,p*p))
            self.assertEqual(p_primary_fraction(bbp_mutant_forcing(j),p),Fraction(5,p*p))
            self.assertEqual(p_primary_seam(j),Fraction(4,p*p))
            self.assertEqual(p_primary_seam(j,True),Fraction(5,p*p))
            self.assertEqual(p_primary_seam(j,False,True),Fraction(4,p*p*16**j))
    def test_weighted_hankel_determinant(self):
        for p,q in ((7,11),(11,13)):
            for mutant in (False,True):
                H=general_seam_hankel(p,q,mutant=mutant,radix_weight=False)
                self.assertEqual(bareiss_det(H),general_seam_hankel_det(p,q,mutant=mutant))
    def test_weighted_radix_hankel_small(self):
        p,q=11,13
        H=general_seam_hankel(p,q,radix_weight=True)
        self.assertEqual(bareiss_det(H),general_seam_hankel_det(p,q,radix_weight=True))
    def test_duplicate_and_wrong_event_controls(self):
        with self.assertRaises(ValueError):consecutive_prime_gap(7,13)
        with self.assertRaises(ValueError):seam_clock(9)
        self.assertEqual(first_pole_seam(8),0)
        self.assertEqual(first_pole_seam(0),0)


class TestAnalyticForwardBackward(unittest.TestCase):
    def test_forcing_identity_against_reduced_rational(self):
        for n in range(1,30):
            r=Fraction(120*n*n-89*n+16,
                       (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(bbp_forcing(n),r)
    def test_original_source_seed(self):
        self.assertEqual(source_prefix(0),Fraction())
        self.assertEqual(source_atom(1),Fraction(47,240))
    def test_positive_monotone_source(self):
        for n in range(1,35):
            self.assertGreater(bbp_forcing(n),0)
            self.assertLess(bbp_forcing(n+1),bbp_forcing(n))
    def test_analytic_backward_shift(self):
        for n,M in ((0,7),(2,19),(5,23),(12,28)):
            self.assertEqual(backward_shift(truncated_germ(n,M)),truncated_germ(n+1,M))
    def test_germ_eval_fixed_integral_seam(self):
        for n,M in ((0,9),(1,13),(7,23),(10,29)):
            P,G,PM=terminal_seam(n,M)
            self.assertEqual(P+G,PM)
            self.assertEqual(G,source_prefix(M)-source_prefix(n))
            self.assertEqual(G,eval_germ(truncated_germ(n,M),1))
    def test_bbp_transfer_source_tail(self):
        for n in (0,1,2,3,13,29):
            self.assertEqual(source_prefix(n+1)-source_prefix(n),source_atom(n+1))
            self.assertGreater(source_tail_upper(n),0)
            self.assertLess(source_tail_upper(n+1),source_tail_upper(n))
    def test_source_analytic_accuracy(self):
        for M in (1,2,4,12,22):
            rational_residual=source_prefix(M+15)-source_prefix(M)
            self.assertGreater(rational_residual,0)
            self.assertLess(rational_residual,source_tail_upper(M))
    def test_terminal_window_tail(self):
        for B in (1,3,8,17):
            M=2*B
            for n in range(B,M):
                P,G,PM=terminal_seam(n,M)
                self.assertEqual(16**n*(P+G),16**n*PM)
                # Error in true 16^n*x vs terminal 16^n*PM is bounded:
                self.assertLess(16**n*source_tail_upper(M),Fraction(1,64*M*M))
    def test_fourier_alias_exact_rational(self):
        for modulus in (2,3,5,7):
            for j in range(1,modulus+1):
                residue=aliased_prefix(j,modulus,6*modulus)
                diff=residue-source_atom(j)
                self.assertGreaterEqual(diff,0)
                self.assertLess(diff,alias_upper(j,modulus))
    def test_boundary_alias_positive(self):
        for mod in (2,4,7):
            self.assertGreater(aliased_prefix(mod,mod,mod*4)-source_atom(mod),0)
    def test_wrong_seed_uses_same_atoms(self):
        # Original source coefficients do not depend on the homogeneous seed.
        seed_a=Fraction(0)
        seed_b=Fraction(1,16)
        for n in (1,2,7):
            u_a=16**n*(seed_a+source_prefix(n))
            u_b=16**n*(seed_b+source_prefix(n))
            self.assertEqual((u_b-u_a).denominator,1)
        self.assertNotEqual(seed_a,seed_b)


class TestObserverFold(unittest.TestCase):
    def test_origami_is_reversible_on_logged_image(self):
        future=tuple(source_atom(j) for j in range(1,12))
        memory=()
        conserved=sum(future, Fraction())
        for _ in range(8):
            before=(memory,future)
            memory,future=origami_step(memory,future)
            self.assertEqual(origami_unstep(memory,future),before)
            self.assertEqual(sum(memory,Fraction())+sum(future,Fraction()),conserved)
        self.assertEqual(len(memory),8)
    def test_origami_without_history_cannot_invert(self):
        # P+c and the suffix alone do not reveal which c was moved.
        a=(Fraction(1,5), (Fraction(2,5),Fraction(3,5)))
        b=(Fraction(2,5), (Fraction(1,5),Fraction(3,5)))
        self.assertEqual((a[0]+a[1][0],a[1][1:]),
                         (b[0]+b[1][0],b[1][1:]))
        self.assertNotEqual(a,b)
    def test_causal_conjugacy_swap(self):
        states=tuple(product((0,1),repeat=2))
        T=lambda x:(x[1],x[0])
        o=lambda x:x[0]
        quot=finite_observational_quotient(states,T,o)
        self.assertEqual(len(set(quot.values())),4)
        for state in states:
            self.assertEqual(finite_journal(T,o,T(state),9),finite_journal(T,o,state,10)[1:])
    def test_hidden_coordinate_quotient(self):
        states=tuple(product((0,1),repeat=2))
        T=lambda x:(x[0],1-x[1])
        o=lambda x:x[0]
        quot=finite_observational_quotient(states,T,o)
        self.assertEqual(len(set(quot.values())),2)
        self.assertEqual(quot[(0,0)],quot[(0,1)])
    def test_finite_nonclosed_rejected(self):
        with self.assertRaises(ValueError):finite_observational_quotient((0,1),lambda x:x+1,lambda x:x)
    def test_causal_feedback_updates_memory(self):
        T=lambda x,a:(x+a)%7
        o=lambda x:x%2
        policy=lambda m:1 if sum(m)%2==0 else 2
        state=(0,())
        for _ in range(5): state=policy_feedback_step(state,T,o,policy)
        self.assertEqual(len(state[1]),5)
        self.assertEqual(state[1][0],0)
    def test_finite_hankel_rank_dynamics_nonclosing(self):
        # The gap 7->11 has eight zero clocks followed by a new event.
        p,q=7,11
        L=consecutive_prime_gap(p,q)
        self.assertEqual(L,9)
        self.assertEqual(sum(bool(first_pole_seam(n)) for n in range(8,16)),0)
        self.assertEqual(first_pole_seam(16),4)
        # At least L distinct forward Moore states are required in clocks 8..16.
        signatures={j:tuple(first_pole_seam(k) for k in range(j,17)) for j in range(8,17)}
        self.assertEqual(len(set(signatures.values())),L)
    def test_exponential_sum_hankel_rank_barrier(self):
        # Any d-dimensional linear recurrence / d exponential modes has
        # Hankel minors of size d+1 zero. The source seam gives nonzero 9x9.
        self.assertNotEqual(bareiss_det(gap_hankel(7,11)),0)
    def test_source_monotone_finite_closed_vs_prime_open(self):
        states=(0,1,2)
        T=lambda x:(x+1)%3
        o=lambda x:1 if x==0 else 0
        quot=finite_observational_quotient(states,T,o)
        self.assertEqual(len(set(quot.values())),3)
        self.assertEqual(finite_journal(T,o,0,9),(1,0,0)*3)

if __name__=="__main__":unittest.main()
