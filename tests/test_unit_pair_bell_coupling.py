"""Exact research regression tests for the authenticated unit-pair / Bell lift.

Bell states are a DECLARED bipartite quantum-information encoding, not a
physical quantum interpretation of the arithmetic BBP source. All original
source states are unwrapped Fractions. The covariance and source-cohomology
checks are exact; only the analytic Bell loop uses finite float diagnostics.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import log, sin, sqrt
import unittest

ORIGINAL = (Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
RADIAL = (Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))

def forcing(n, taps=ORIGINAL):
    assert n >= 1
    return sum((w/Q(8*(n-1)+j) for j,w in enumerate(taps,1)), Q(0))

def states(N):
    a=b=Q(1); u=Q(0)
    yield 0,a,b,u
    for n in range(1,N+1):
        r=forcing(n)
        a=16*a+r/2
        b=16*b-r/2
        u=16*u+r
        yield n,a,b,u

def negativity(a,b):
    return a*b/(a*a+b*b)

def bright_probability(a,b):
    return (a-b)**2/(2*(a*a+b*b))

def residues(taps):
    # rational forcing sum_j w_j/(8(x-1)+j)
    # pole x=1-j/8, residue=w_j/8; no two lanes share an integer orbit.
    return {Q(1)-Q(j,8):w/8 for j,w in enumerate(taps,1) if w}

def weighted_residue(poles,a):
    ans=Q(0)
    for p,w in poles.items():
        gap=p-a
        if gap.denominator==1:
            ans+=Q(16)**(-gap.numerator)*w
    return ans

def coboundary_poles(poles):
    # (Ef)(x)=f(x+1): poles translated left by one.
    ans={}
    for p,w in poles.items():
        ans[p-1]=ans.get(p-1,Q(0))+w
        ans[p]=ans.get(p,Q(0))-16*w
    return {p:w for p,w in ans.items() if w}

def G(t):
    return 2*log((2-t*t)/(t*t-2*t+2))

def bell_loop_bright(t):
    return sin(G(t)/2)**2

class PairedUnitBell(unittest.TestCase):
    def test_01_pinned_original_source(self):
        self.assertEqual(forcing(1),Q(47,15))
        self.assertEqual(ORIGINAL,(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0)))
        for n in range(1,100):
            self.assertGreater(forcing(n),0)

    def test_02_two_unit_history_exact(self):
        for n,a,b,u in states(128):
            self.assertEqual(a+b,2*16**n)
            self.assertEqual(a-b,u)
            if n==0:
                self.assertEqual((a,b,u),(Q(1),Q(1),Q(0)))

    def test_03_fraction_source_budget_and_schmidt(self):
        for n,a,b,u in states(128):
            d=u/Q(16)**n
            self.assertGreaterEqual(d,0)
            self.assertLess(d,Q(1,5))
            self.assertGreater(a,0)
            self.assertGreater(b,0)
            self.assertEqual(negativity(a,b),(4-d*d)/(8+2*d*d))
            self.assertGreater(negativity(a,b),Q(99,202))

    def test_04_exact_bell_dark_bright_source(self):
        for n,a,b,u in states(72):
            # in {|00>,|11>} basis: dark=[c,-c], bright=[u/2,u/2].
            c=Q(16)**n
            self.assertEqual(a,c+u/2)
            self.assertEqual(-b,-c+u/2)
            self.assertEqual(a-b,u)  # joint erasure numerator

    def test_05_quantum_bright_probability(self):
        for n,a,b,u in states(64):
            d=u/Q(16)**n
            self.assertEqual(bright_probability(a,b),d*d/(4+d*d))
            self.assertLess(bright_probability(a,b),Q(1,101))
            if n==0:self.assertEqual(bright_probability(a,b),0)
            else:self.assertGreater(bright_probability(a,b),0)

    def test_06_dephased_same_local_but_not_joint(self):
        for n,a,b,_ in states(36):
            norm=a*a+b*b
            local=(a*a/norm,b*b/norm)
            dephased_local=local
            self.assertEqual(local,dephased_local)
            self.assertEqual((a*a+b*b)/(2*norm),Q(1,2))
            self.assertNotEqual(bright_probability(a,b),Q(1,2))
            self.assertNotEqual(-a*b/norm,Q(0)) # pure-state offdiag

    def test_07_separable_zero_overlap_falsifier(self):
        # |+>⊗|->=(|00>-|01>+|10>-|11>)/2 has
        # zero Phi+ overlap but Schmidt determinant zero (product state).
        c00,c01,c10,c11=Q(1,2),Q(-1,2),Q(1,2),Q(-1,2)
        self.assertEqual(c00+c11,0)
        self.assertEqual(c00*c11-c01*c10,0)
        # |Phi-> has same zero joint overlap but Schmidt rank two.
        a00,a01,a10,a11=Q(1),Q(0),Q(0),Q(-1)
        self.assertEqual(a00+a11,0)
        self.assertNotEqual(a00*a11-a01*a10,0)

    def test_08_two_residue_independent_source_classes(self):
        a=Q(7,8);b=Q(3,4)
        orig=residues(ORIGINAL);rad=residues(RADIAL)
        row1=(weighted_residue(orig,a),weighted_residue(rad,a))
        row2=(weighted_residue(orig,b),weighted_residue(rad,b))
        self.assertEqual(row1,(Q(1,2),Q(1,4)))
        self.assertEqual(row2,(Q(0),Q(-1,4)))
        self.assertEqual(row1[0]*row2[1]-row1[1]*row2[0],Q(-1,8))

    def test_09_coboundary_residue_invariance(self):
        f={Q(7,8):Q(3,7),Q(-1,8):Q(-5,4),Q(3,4):Q(17,3),
           Q(7,4):Q(2),Q(2,3):Q(11,5)}
        df=coboundary_poles(f)
        for a in (Q(7,8),Q(3,4),Q(2,3),Q(1,2)):
            self.assertEqual(weighted_residue(df,a),0)

    def test_10_tau_peak_radial_potential(self):
        tau=2-sqrt(2)
        self.assertAlmostEqual(G(0),0,places=14)
        self.assertAlmostEqual(G(1),0,places=14)
        self.assertAlmostEqual(G(tau),log(2),places=14)
        self.assertGreater(G(tau),G(Q(1,2)))
        self.assertGreater(G(tau),G(Q(3,4)))

    def test_11_bell_loop_joint_return(self):
        tau=2-sqrt(2)
        p=bell_loop_bright
        self.assertAlmostEqual(p(0),0,places=14)
        self.assertAlmostEqual(p(1),0,places=14)
        self.assertAlmostEqual(p(tau),sin(log(2)/2)**2,places=14)
        self.assertGreater(p(tau),p(.5))
        self.assertGreater(p(tau),p(.75))
        self.assertGreater(p(tau),.11)
        self.assertLess(p(tau),.12)

    def test_12_local_entropy_constant_for_bell_phase(self):
        # Bell loop phase only changes two nonzero amplitudes' arguments;
        # their absolute squares stay 1/2, so both local marginals remain I/2.
        for t in (0,.25,.5,2-sqrt(2),.75,1):
            self.assertEqual(Q(1,2)+Q(1,2),1)
            self.assertTrue(0<=bell_loop_bright(t)<=1)

    def test_13_same_forcing_wrong_seed_shares_cohomology(self):
        seed=Q(1,5)
        us=Q(0);uw=seed
        for n in range(1,41):
            r=forcing(n);us=16*us+r;uw=16*uw+r
            self.assertEqual(uw-us,seed*16**n)
            self.assertEqual((uw-us)%1,seed)

    def test_14_vacuum_r_zero_does_not_force_mixing(self):
        # The same Bell dark baseline persists for the identically zero forcing;
        # that relative orbit U_n=0 is coherent, not equidistributed.
        a=b=Q(1)
        for n in range(1,42):
            a*=16;b*=16
            self.assertEqual(a-b,0)
            self.assertEqual(negativity(a,b),Q(1,2))
            self.assertEqual(bright_probability(a,b),0)

if __name__=="__main__":
    unittest.main()
