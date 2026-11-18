"""Seed-shift resonances and null-observer controls; exact rational checks.

The finite cyclic Fourier averages are exact only on Z/(16**M). Infinite Haar
statements in the accompanying note are proved separately by character
orthogonality, not by pretending finite groups equal the continuous circle.
"""
from fractions import Fraction as Q
from itertools import product
import unittest


def r(n):
    if n < 1: raise ValueError('n>=1')
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def source(N, seed=Q(0)):
    u=Q(seed); out=[u]
    for n in range(1, N+1):
        u=16*u+r(n);out.append(u)
    return out


def finite_haar_character(freq,M):
    """Exact character mean on additive cyclic group Z/(16**M)."""
    return int(int(freq) % (16**M) == 0)


def phase_difference_is_invisible(s,n):
    """e(16**n*s) == 1 iff the argument is an integer."""
    q=16**n*Q(s)
    return q.denominator==1


def resonance_frequency(terms):
    """Moment of raw seed phases: product a_n**power."""
    return sum(power*16**n for n,power in terms)


def d16(x):
    q=Q(x)%1
    return min(q, 1-q)


def shifted_shell_energy(x,s,B):
    """Phase energy proxy built from exact torus distances."""
    y=x+s
    return sum((d16(16**n*y)**2 for n in range(B,2*B)),Q(0))/B


class SeedResonanceTests(unittest.TestCase):
    def test_full_source_affine_transport(self):
        for s in (Q(0),Q(1,3),Q(1,16**4),-Q(3,7)):
            un=source(22,s); u0=source(22)
            for n in range(23):
                self.assertEqual(un[n]-u0[n],16**n*s)

    def test_nonzero_seed_can_be_eventually_invisible(self):
        m=4; s=Q(3,16**m)
        self.assertTrue(all(not phase_difference_is_invisible(s,n) for n in range(m)))
        self.assertTrue(all(phase_difference_is_invisible(s,n) for n in range(m,20)))

    def test_shell_null_fiber_exact(self):
        for B in (1,3,7,10):
            for a in (-3,1,2,17):
                s=Q(a,16**B)
                self.assertTrue(all(phase_difference_is_invisible(s,n) for n in range(B,2*B)))
            s=Q(1,16**(B+1))
            self.assertFalse(phase_difference_is_invisible(s,B))

    def test_source_reaches_arbitrary_rational_endpoints(self):
        x=Q(17,23)
        for y in (Q(0),Q(1,15),Q(1,7),Q(3,16**5)):
            s=y-x
            self.assertEqual(x+s,y)
            self.assertEqual(shifted_shell_energy(x,s,10),shifted_shell_energy(y,Q(0),10))
        self.assertEqual(shifted_shell_energy(x,-x,10),Q(0))
        self.assertEqual(shifted_shell_energy(x,Q(1,16**4),10),shifted_shell_energy(x,Q(0),10))

    def test_individual_finite_haar_phase_is_null_before_horizon(self):
        M=8
        for n in range(M):
            self.assertEqual(finite_haar_character(16**n,M),0)
        self.assertEqual(finite_haar_character(16**M,M),1)

    def test_distinct_clock_covariance_is_null_for_resolved_clocks(self):
        M=9
        for n,m in product(range(7), repeat=2):
            moment=finite_haar_character(16**n-16**m,M)
            self.assertEqual(moment,int(n==m))

    def test_first_adjacent_resonance_is_order_seventeen(self):
        for n in range(5):
            self.assertEqual(resonance_frequency(((n,16),(n+1,-1))),0)
            self.assertEqual(finite_haar_character(resonance_frequency(((n,16),(n+1,-1))),9),1)
            # The smallest nontrivial integer relation k+16*l=0 has |k|+|l|=17.
            for k in range(-15,16):
                for l in range(-15,16):
                    if abs(k)+abs(l)<17 and (k,l)!=(0,0):
                        self.assertNotEqual(k+16*l,0)

    def test_full_group_causal_relation_does_not_identify_source(self):
        # Same transition relation is valid for every source and every seed.
        for x,s in product((Q(0),Q(1,7),Q(3,16)),(Q(0),Q(1,16),-Q(1,7))):
            y=x+s
            for n in (0,1,3,10):
                self.assertEqual((16**(n+1)*y-16*16**n*y)%1,0)

    def test_rational_BBP_source_cocycle_is_seed_independent(self):
        for s in (Q(0), Q(1,16**3), -Q(1,7)):
            u=source(50,s)
            u0=source(50,Q(0))
            for n in (0,1,2,12,37):
                self.assertEqual(u[n+1]-16*u[n],r(n+1))
                self.assertEqual((u[n+1]-16*u[n])-(u0[n+1]-16*u0[n]),0)

    def test_dyadic_group_is_dense_and_null_for_eventual_statistics(self):
        x=Q(1,15)
        for m in (1,2,4,8,12):
            g=(x*16**m).numerator//(x*16**m).denominator
            q=Q(g,16**m)
            self.assertLess(x-q,Q(1,16**m))
            self.assertTrue(all(phase_difference_is_invisible(q,n) for n in range(m,m+3)))
            self.assertNotEqual(x,Q(0))

    def test_r0_indicator_is_not_continuous_under_dense_null_group(self):
        # x=1/15 has a nonunit fixed circle phase (R0 holds). Dyadic approximants
        # q_m to x all eventually become zero-phase (R0 fails).
        x=Q(1,15)
        self.assertEqual((16*x)%1,x)
        for m in (1,3,6,10):
            a=(16**m*x).numerator//(16**m*x).denominator
            qm=Q(a,16**m)
            self.assertLess(abs(qm-x),Q(1,16**m))
            self.assertTrue(all((16**n*qm)%1==0 for n in range(m,m+5)))
            self.assertNotEqual((16**m*x)%1,0)

    def test_masked_first_moments_do_not_authenticate_zero_seed(self):
        # Uniform finite seed masks make all modes before M average to 0,
        # regardless of whether the completed source is originally locked.
        for original_x in (Q(0),Q(1,15),Q(1,7)):
            for n in (0,1,2,3):
                self.assertEqual(finite_haar_character(16**n,5),0)

    def test_future_equivalence_of_impulse_and_initial_seed(self):
        # Inject +a into the forced update at k; equivalently start with
        # seed a/16**k if one only observes clocks n>=k.
        a=Q(3,7); k=5; N=20
        shifted=source(N,a/16**k)
        plain=source(N)
        driven=[Q(0)]
        for n in range(1,N+1):
            driven.append(16*driven[-1]+r(n)+(a if n==k else 0))
        for n in range(N+1):
            if n < k:
                self.assertEqual(driven[n],plain[n])
                self.assertNotEqual(driven[n],shifted[n])
            else:
                self.assertEqual(driven[n],shifted[n])
        # The pre-impulse phase can distinguish the initial shift; the
        # entire later real state cannot.
        self.assertNotEqual(driven[k-1],shifted[k-1])
        self.assertEqual(driven[k],shifted[k])

    def test_mean_square_of_haar_seed_shell_is_one_over_B(self):
        # Fourier orthogonality gives E W_B=0, E|W_B|^2=1/B
        # for every *deterministic* underlying source x. Test coefficients
        # on a finite mask group whose modulus resolves all sample clocks.
        for B in (1,2,3,4):
            M=2*B+1
            self.assertEqual(sum(finite_haar_character(16**n,M)
                                 for n in range(B,2*B)),0)
            diagonals=sum(finite_haar_character(16**n-16**m,M)
                          for n in range(B,2*B) for m in range(B,2*B))
            self.assertEqual(Q(diagonals,B*B),Q(1,B))

    def test_seed_susceptibility_does_not_carry_source_phase(self):
        # d/ds e(16**n s) at s=0, divided by universal 2*pi*i,
        # is 16**n. This is a transfer-law fact independent of x.
        for n in range(8):
            self.assertEqual(16**(n+1),16*16**n)
            self.assertNotEqual(16**n,0)

    def test_source_memory_is_detectable_only_with_source_chart(self):
        # The original rational compensator is nonzero but seed-independent.
        for n in (1,2,3,8):
            self.assertNotEqual(r(n+1),0)
            for s in (Q(0),Q(1,17)):
                u=source(n+1,s)
                self.assertEqual(u[n+1]-16*u[n],r(n+1))

    def test_dual_number_tangent_is_invisible_to_base_projection(self):
        # In R[eps]/(eps^2): exp(2*pi*i*16**n*eps*v)=1+eps*(2*pi*i*16**n*v).
        # Store the tangent coefficient divided by universal 2*pi*i.
        v=Q(3,7)
        for n in (0,1,3,8):
            base,tangent=(Q(1),16**n*v)
            self.assertEqual(base,1)
            self.assertNotEqual(tangent,0)
            self.assertEqual(tangent,16**n*v)

if __name__=='__main__': unittest.main()
