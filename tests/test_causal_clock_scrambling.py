"""Exact causal-clock alignment and BBP compensation controls.

Source status: this is an illustrative clock-synchronization apparatus, not a
metric of spacetime or a proof of pi normality.  It uses the literal four-pole
forcing and exact rational arithmetic to test the causal transport laws.
"""
from fractions import Fraction as F
from itertools import product
import unittest


def forcing(n):
    if n < 1:
        raise ValueError("n >= 1 required")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def source_path(m, seed=F(0)):
    u = F(seed)
    out = {0: u}
    for n in range(1, m+1):
        u = 16*u + forcing(n)
        out[n] = u
    return out


def chronological_forcing(n, steps):
    if steps < 0:
        raise ValueError("nonnegative steps")
    return sum((16**(steps-j)*forcing(n+j)
                for j in range(1, steps+1)), F(0))


def affine_pair_step(u, t, n):
    r = forcing(n+1)
    return 16*u+r, 16*t-r


def phase_mask_law(z, p):
    """C4 calibration only: A=R, B=z*(R if shared else R')."""
    if not isinstance(z, int) or not (0 <= z < 4):
        raise ValueError("source must be an element of C4")
    p = F(p)
    if not 0 <= p <= 1:
        raise ValueError("coupling must be in [0, 1]")
    joint = {(a, b): F(0) for a, b in product(range(4), repeat=2)}
    for a in range(4):
        joint[a, (z+a) % 4] += p/4
        for rp in range(4):
            joint[a, (z+rp) % 4] += (1-p)/16
    return joint


def edge_residuals(edge_observations, offsets):
    return {(a,b): observed - (offsets[b]-offsets[a])
            for (a,b), observed in edge_observations.items()}


class CausalClockTests(unittest.TestCase):
    def test_original_zero_seed(self):
        u = source_path(30)
        self.assertEqual(u[0], 0)
        self.assertEqual(u[1], forcing(1))
        self.assertNotEqual(u[1], 0)
        for n in range(1, 30):
            self.assertEqual(u[n+1], 16*u[n]+forcing(n+1))

    def test_two_step_direct_equals_composed_forward(self):
        u = source_path(30)
        for n in (0, 1, 2, 4, 12, 20):
            self.assertEqual(u[n+2], 256*u[n]
                             + 16*forcing(n+1)+forcing(n+2))

    def test_causal_path_cocycle_on_arbitrary_lengths(self):
        for n,h,k in product((0,1,4,17), (0,1,2,4), (0,1,3,5)):
            self.assertEqual(chronological_forcing(n,h+k),
                             16**k*chronological_forcing(n,h)
                             + chronological_forcing(n+h,k))

    def test_dual_observers_composite_exact(self):
        for n in (0,1,8,20):
            for u,t in ((F(0),F(1,7)),(F(3,5),F(2,9)),
                        (F(-1,7),F(1,7))):
                u1,t1 = affine_pair_step(u,t,n)
                u2,t2 = affine_pair_step(u1,t1,n+1)
                self.assertEqual(u1+t1,16*(u+t))
                self.assertEqual(u2+t2,256*(u+t))
                self.assertEqual(u2,256*u+chronological_forcing(n,2))
                self.assertEqual(t2,256*t-chronological_forcing(n,2))

    def test_exact_carry_keeps_original_winding(self):
        u = source_path(60)
        for n in range(1,59):
            cn = u[n].numerator//u[n].denominator
            fn = u[n]-cn
            theta = 16*fn+forcing(n+1)
            carry = theta.numerator//theta.denominator
            cp = u[n+1].numerator//u[n+1].denominator
            fp = u[n+1]-cp
            self.assertEqual(cp,16*cn+carry)
            self.assertEqual(fp,theta-carry)
            self.assertTrue(F(0)<=fn<F(1))
            self.assertTrue(F(0)<=fp<F(1))

    def test_consistent_clock_diamond(self):
        # Two ways of comparing A and C: AB+BC and direct AC.
        e = {('A','B'):F(2),('B','C'):F(3),('A','C'):F(5)}
        offsets = {'A':F(0),'B':F(2),'C':F(5)}
        self.assertEqual(edge_residuals(e,offsets),{k:F(0) for k in e})
        self.assertEqual(e['A','B']+e['B','C']-e['A','C'],0)

    def test_inconsistent_clock_cycle_and_least_squares_projection(self):
        # The unique least-squares offsets after anchor theta_A=0.
        e = {('A','B'):F(2),('B','C'):F(3),('A','C'):F(6)}
        offsets={'A':F(0),'B':F(7,3),'C':F(17,3)}
        residual=edge_residuals(e,offsets)
        self.assertEqual(residual[('A','B')], F(-1,3))
        self.assertEqual(residual[('B','C')], F(-1,3))
        self.assertEqual(residual[('A','C')], F(1,3))
        self.assertEqual(e['A','B']+e['B','C']-e['A','C'],-1)
        self.assertEqual(sum((x*x for x in residual.values()),F(0)),F(1,3))
        # The residual has zero weighted divergence at each free vertex.
        self.assertEqual(residual[('A','B')]-residual[('B','C')],0)
        self.assertEqual(residual[('B','C')]+residual[('A','C')],0)

    def test_locked_different_seed_has_identical_causal_transport(self):
        # U=-T describes a locked *completed* source. It cannot be confused
        # with the genuine U_0=0 BBP ancestry. This test is finite algebra,
        # not a claim that arbitrary t has the authentic positive future tail.
        t=F(1,19)
        u=-t
        for n in range(0,5):
            self.assertEqual(u+t,0)
            u,t=affine_pair_step(u,t,n)
            self.assertEqual(u+t,0)

    def test_masked_marginals_are_source_blind(self):
        for z,p in product(range(4),(F(0),F(1,3),F(1))):
            law=phase_mask_law(z,p)
            self.assertEqual(sum(law.values()),1)
            for x in range(4):
                self.assertEqual(sum(prob for (a,b),prob in law.items() if a==x),F(1,4))
                self.assertEqual(sum(prob for (a,b),prob in law.items() if b==x),F(1,4))

    def test_masked_pair_correlation_is_coupling_not_chaos(self):
        for z,p in product(range(4),(F(0),F(1,4),F(1,2),F(1))):
            law=phase_mask_law(z,p)
            # If the shared-mask switch is ON, b-a=z mod 4.
            self.assertEqual(sum(prob for (a,b),prob in law.items() if (b-a)%4==z),
                             p+(1-p)/4)
        independent = phase_mask_law(0,F(0))
        for z in range(1,4):
            self.assertEqual(phase_mask_law(z,F(0)),independent)

    def test_clock_alignment_can_be_oracle_if_unconstrained(self):
        # For any observed path f_n, selecting theta_n=f_n makes the
        # co-moving residual zero. Optimization without source constraints
        # therefore cannot prove delocalization or BBP anti-locking.
        obs=[F(1,5),F(3,7),F(2,11),F(8,19)]
        gauges=obs[:]
        self.assertEqual([v-g for v,g in zip(obs,gauges)],[F(0)]*len(obs))

if __name__=='__main__':
    unittest.main()
