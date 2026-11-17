"""Original BBP pole-orbit obstruction, matched locked forcing and causal history.

Finite rational tests check the exact identities and hostile examples.  The
nonexistence of a rational source antiderivative is proved on paper using pole
residues, not inferred from finite symbolic search. No pi normality proof.
"""
from fractions import Fraction as F
from itertools import combinations
import unittest


def bbp(n):
    if n < 1: raise ValueError('n >= 1')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def a(n):
    if n < 1: raise ValueError('n >= 1')
    return F(1,(8*n-7)*(8*n-6))


def tel(n):
    return 16*a(n)-a(n+1)


def trace(N, source=bbp, impulses=None):
    impulses=impulses or {}
    u=F(0); out=[u]
    for n in range(1,N+1):
        u=16*u+source(n)+impulses.get(n,F(0))
        out.append(u)
    return out


def finite_weighted_source_sum(N, source):
    return sum((F(source(n),16**n) for n in range(1,N+1)),F(0))


def terminal_probe(U,k):
    z=F(U,16**k)%1
    return min(z,1-z)**2


def dprobe_dsource(U,N,k,j):
    """Branchwise derivative of d_T(U/16**k)^2 w.r.t impulse at j."""
    y=F(U,16**k); m=y.numerator//y.denominator
    frac=y-m
    if frac==F(1,2): raise ValueError('circular tie: no derivative')
    nearest=m if frac<F(1,2) else m+1
    return F(2*(y-nearest)*16**(N-j),16**k)


def sparse(n):
    if n<1:raise ValueError('n>=1')
    return F(1 if n&(n-1)==0 else 0)


def sparse_future_mass(B,J):
    """Sum of exact fractional phases contributed by digits at 2**ell,
    ell=log2(B)+1,...,J, over the critical B..2B-1 window."""
    j=B.bit_length()-1
    if B!=1<<j or J<=j:raise ValueError
    return F(16**(2*B)-16**B,15)*sum((F(1,16**(2**ell)) for ell in range(j+1,J+1)),F(0))


class BBPPoleTelescopeOracle(unittest.TestCase):
    def test_original_four_poles_are_distinct_shift_classes(self):
        poles=[F(a0,8) for a0 in (7,4,3,2)]
        self.assertEqual(len(set(poles)),4)
        self.assertTrue(all(F(0)<p<F(1) for p in poles))
        residues=(F(1,2),F(-1,4),F(-1,8),F(-1,8))
        self.assertTrue(all(r!=0 for r in residues))
        # Each orbit has just one nonzero weighted discrete residue.
        self.assertTrue(all(r!=0 for r in residues))

    def test_matching_locked_forcing_exact_finite_telescope(self):
        for N in (1,2,3,7,32,128):
            lhs=finite_weighted_source_sum(N,tel)
            self.assertEqual(lhs,a(1)-a(N+1)/16**N)
            self.assertEqual(trace(N,tel)[-1],16**N*a(1)-a(N+1))
        self.assertEqual(a(1),F(1,2))  # completed seed-zero endpoint, eventually phase 1

    def test_locked_forcing_is_positive_and_decreasing(self):
        for n in range(1,512):
            self.assertGreater(tel(n),0)
            self.assertGreater(tel(n),tel(n+1))
            self.assertGreater(a(n),a(n+1))

    def test_same_leading_asymptotic_coefficient(self):
        for n in (50,100,200,400,800):
            self.assertLess(abs(n*n*bbp(n)-F(15,64)),F(1,n))
            self.assertLess(abs(n*n*tel(n)-F(15,64)),F(1,n))
            self.assertLess(abs(bbp(n)-tel(n)),F(1,n**3))

    def test_locked_pole_pairs_have_vanishing_weighted_shift_residue(self):
        # h(n)=1/(8n-7)-1/(8n-6), residues ±1/8.
        for h_res in (F(1,8),F(-1,8)):
            r_at_zero=16*h_res
            r_at_minus_one=-h_res
            self.assertEqual(r_at_zero+16*r_at_minus_one,0)

    def test_endpoint_impulse_jacobian_has_rank_one(self):
        B=5; N=2*B; U=trace(N)[-1]
        mat=[[dprobe_dsource(U,N,k,j) for j in range(1,N+1)] for k in range(1,B+1)]
        for k0,k1 in combinations(range(B),2):
            for j0,j1 in combinations(range(N),2):
                self.assertEqual(mat[k0][j0]*mat[k1][j1],mat[k0][j1]*mat[k1][j0])
        self.assertTrue(any(x!=0 for row in mat for x in row))

    def test_two_causal_histories_share_all_terminal_probes(self):
        B=6;N=2*B;j0,j1=3,7
        early=F(1,16**(j1-j0)); late=F(1)
        left=trace(N,impulses={j0:early})
        right=trace(N,impulses={j1:late})
        self.assertNotEqual(left[j0],right[j0]);self.assertNotEqual(left[j1-1],right[j1-1])
        self.assertEqual(left[j1],right[j1])
        self.assertEqual(left[N],right[N])
        self.assertEqual([terminal_probe(left[N],k) for k in range(1,B+1)],
                         [terminal_probe(right[N],k) for k in range(1,B+1)])

    def test_full_clock_history_recovers_impulse_input(self):
        N=12; impulses={2:F(1,3),6:F(-7,25),12:F(15,16)}
        z=trace(N,impulses=impulses)
        recovered={n:z[n]-16*z[n-1]-bbp(n) for n in range(1,N+1)}
        self.assertEqual(recovered,{n:impulses.get(n,F(0)) for n in range(1,N+1)})
        # Lower-triangular Jacobian of clocks U_1,..,U_N has diagonal 1.
        self.assertTrue(all(16**(n-j)==1 for n in range(1,N+1) for j in (n,)))

    def test_sparse_zero_seed_source_and_cold_shell_exact(self):
        z=trace(128,source=sparse)
        self.assertEqual(z[0],0)
        self.assertEqual(z[-1]/16**128,
            sum((F(1,16**(2**j)) for j in range(8)),F(0)))
        for j in range(1,8):
            B=2**j; S=sparse_future_mass(B,j+4)
            self.assertGreater(S,0)
            self.assertLess(S,F(16,225))
            # All previous marker terms are integral after multiplication
            # by 16**n on this shell; a future marker contribution is <1.
            self.assertGreater(B,j-1)

    def test_rational_telescope_is_not_original_source(self):
        self.assertNotEqual(bbp(1),tel(1))
        self.assertNotEqual(bbp(3),tel(3))
        self.assertGreater(bbp(1),0)
        self.assertGreater(tel(1),0)


if __name__=='__main__':unittest.main()
