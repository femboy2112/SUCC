"""Proof-direction oracle: authenticated BBP rational witnesses vs finite shadows.

This is a finite exact model of a *proposer* and an independent *checker*.
No test concludes an all-shell R0 bound or base-16 normality of pi.
"""
from fractions import Fraction as F
from functools import lru_cache
import unittest


def forcing(n):
    if n < 1:
        raise ValueError('original BBP indices are positive')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


@lru_cache(None)
def terminal_state(n):
    u = F(0)
    for j in range(1, n+1):
        u = 16*u + forcing(j)
    return u


def torus(y):
    frac = F(y) % 1
    return min(frac, 1-frac)


def witness_positions(B, epsilon):
    u = terminal_state(2*B)
    return tuple(k for k in range(1, B+1) if torus(u/16**k) >= epsilon)


def terminal_energy(B):
    u = terminal_state(2*B)
    return sum((torus(u/16**k)**2 for k in range(1, B+1)), F(0))/B


def check_shell_certificate(B, epsilon, theta, proposed_u, ks):
    """Verifier fixes source zero, then checks exactly the proposed directions.

    Its result is FOR ONE B, not a proof of an eventual universal theorem.
    """
    if B < 1 or not (F(0) < epsilon <= F(1, 2)) or not (F(0) < theta <= 1):
        return False
    if proposed_u != terminal_state(2*B):
        return False
    if len(set(ks)) != len(ks) or not all(1 <= k <= B for k in ks):
        return False
    if len(ks) < theta*B:
        return False
    return all(torus(proposed_u/16**k) >= epsilon for k in ks)


def opposite_r0_prefix_pair(A, m):
    """Both endpoints have prefix A, but opposite eventual R0 outcomes."""
    assert m >= 1 and 0 <= A < 16**m
    locked = F(A, 16**m)
    nonunit_fixed = (F(A)+F(1, 15)) / 16**m
    return locked, nonunit_fixed


def prefix_observation(y, m):
    return (16**m*y).numerator // (16**m*y).denominator


class ProofDirectionOracleTests(unittest.TestCase):
    def test_every_finite_cylinder_has_opposite_R0_targets(self):
        for m in (1, 2, 3, 5):
            for A in (0, 1, 16**m-1):
                x0, x1 = opposite_r0_prefix_pair(A, m)
                self.assertEqual(prefix_observation(x0, m), A)
                self.assertEqual(prefix_observation(x1, m), A)
                for n in (m, m+1, m+5):
                    self.assertEqual((16**n*x0) % 1, F(0))
                    self.assertEqual((16**n*x1) % 1, F(1, 15))

    def test_finite_trace_phase_discrepancy_has_tunable_bound(self):
        H = 8
        for m in (H+4, H+7, H+11):
            x0, x1 = opposite_r0_prefix_pair(1, m)
            for n in range(H+1):
                self.assertEqual(16**n*(x1-x0), F(16**n, 15*16**m))
                self.assertLessEqual(abs(16**n*(x1-x0)), F(1, 15*16**(m-H)))

    def test_source_blind_advice_cannot_split_equal_evidence_fiber(self):
        m, A = 3, 7
        a,b = opposite_r0_prefix_pair(A,m)
        evidence = prefix_observation
        advice = lambda x: ('inspect_digit', evidence(x,m) % 3)
        self.assertEqual(evidence(a,m), evidence(b,m))
        self.assertEqual(advice(a), advice(b))
        self.assertNotEqual((16**m*a)%1,(16**m*b)%1)

    def test_new_probe_direction_can_split_original_fiber(self):
        m,A = 3,7
        a,b = opposite_r0_prefix_pair(A,m)
        # The new result is independently obtainable by a lawful higher-clock
        # exact arithmetic probe, not an injected target-label bit.
        direction = lambda y: (16**m*y)%1
        self.assertEqual(direction(a),0)
        self.assertEqual(direction(b), F(1,15))

    def test_terminal_rational_bbpprefix_is_exactly_zero_seeded(self):
        for m in (1,2,16,32,128):
            direct = sum((forcing(j)/16**j for j in range(1,m+1)), F(0))
            self.assertEqual(terminal_state(m),16**m*direct)

    def test_finite_oracle_witnesses_recomputed_locally(self):
        eps,theta = F(1,4), F(1,4)
        for B in (16,32,64,128):
            U = terminal_state(2*B)
            ks = witness_positions(B,eps)
            self.assertTrue(check_shell_certificate(B,eps,theta,U,ks))
            self.assertGreaterEqual(terminal_energy(B),eps**2*F(len(ks),B))
            self.assertGreaterEqual(terminal_energy(B),eps**2*theta)

    def test_checker_rejects_bad_oracle_and_forged_seed(self):
        B=32
        eps,theta=F(1,4),F(1,4)
        U=terminal_state(2*B)
        good=witness_positions(B,eps)
        self.assertTrue(check_shell_certificate(B,eps,theta,U,good))
        self.assertFalse(check_shell_certificate(B,eps,theta,U+16**(2*B-1),good))
        self.assertFalse(check_shell_certificate(B,eps,theta,U,(good[0],)))
        self.assertFalse(check_shell_certificate(B,eps,theta,U,(good[0],)*B))
        self.assertFalse(check_shell_certificate(B,eps,theta,U,tuple(range(1,B+1))))
        self.assertFalse(check_shell_certificate(B,F(0),theta,U,good))

    def test_uniform_averaged_energy_forces_uniform_witness_density(self):
        # Algebra: if R_B>=delta and epsilon^2<delta, then
        # q_B >= (delta-epsilon^2)/(1/4-epsilon^2).
        eps,delta=F(1,8),F(1,20)
        theta=(delta-eps*eps)/(F(1,4)-eps*eps)
        self.assertGreater(theta,0)
        for B in (16,32,64,128):
            self.assertGreater(terminal_energy(B),delta)
            self.assertGreaterEqual(F(len(witness_positions(B,eps)),B),theta)

    def test_single_strong_direction_per_shell_does_not_force_R0(self):
        for B in (2,8,64,512):
            sample = (F(1,2),)+(F(0),)*(B-1)
            R=sum((d*d for d in sample),F(0))/B
            self.assertEqual(R,F(1,4*B))

    def test_original_seed_is_a_source_passport_not_a_hint(self):
        B=32
        U=terminal_state(2*B)
        changed_seed=F(1,16**(2*B))
        changed_U=U+16**(2*B)*changed_seed
        self.assertEqual(changed_U,U+1)
        self.assertFalse(check_shell_certificate(B,F(1,4),F(1,4),changed_U,
                                                 witness_positions(B,F(1,4))))

if __name__ == '__main__':
    unittest.main()
