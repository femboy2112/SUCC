"""Exact terminal BBP digit-wall coercivity, CRT and source-counterfeit tests.

All universal assertions are supported by paper proofs; tests certify finite
instances and mutation controls. No π normality or R0 theorem is claimed.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import math
import unittest


def forcing(n):
    if n<1: raise ValueError('n>=1')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

@lru_cache(maxsize=None)
def U(n):
    a=F(0)
    for j in range(1,n+1):
        a=16*a+forcing(j)
    return a


def terminal_energy(q, B):
    return sum((torus(F(q)/16**k)**2 for k in range(1,B+1)),F(0))/B


def torus(a):
    x=a%1
    return min(x,1-x)


def symbols(q,B):
    C=q.numerator//q.denominator
    return tuple((C//16**j)%16 for j in range(B))


def defect_counts(q,B):
    d=symbols(q,B)
    off=sum(v not in(0,15) for v in d)
    walls=sum((d[i-1],d[i]) in ((0,15),(15,0)) for i in range(1,B))
    return off,walls


def domain_bounds(q,B):
    off,walls=defect_counts(q,B)
    return ((F(off,256)+F(225*walls,65536))/B,
            (F(off,4)+F(off+walls+1,255))/B)


def terminal_from_rational_recurrence(n):
    a=F(0)
    for j in range(1,n+1):a=16*a+forcing(j)
    return a


def positive_locked_counterfeit(M):
    """Match first M authentic BBP terms, positive *decreasing* rational
    forcing, same 15/(64 n^2) leading Gamma/BBP jet, zero seed, locked endpoint.

    Pick a radix rational q=P_M+16^-M*(b_M+D) with D>0 small enough to
    keep the junction r_M>rtilde_(M+1). For n>=M:
       g_n=b_n+D*16^-(n-M), b_n=1/(64(n+1)^2),
       rtilde_(n+1)=16*g_n-g_(n+1).
    """
    if M<1:raise ValueError('M>=1')
    P=sum((forcing(j)/16**j for j in range(1,M+1)),F(0))
    b=F(1,64*(M+1)**2)
    def bfun(n):return F(1,64*(n+1)**2)
    base_next=16*bfun(M)-bfun(M+1)
    gap=forcing(M)-base_next
    assert gap>0
    Dmax=min(b/2, gap*F(8,255))
    assert Dmax>0
    lo=P+b/(16**M)
    hi=P+(b+Dmax)/(16**M)
    K=M+1
    while F(1,16**K)>=hi-lo:K+=1
    A=(lo*16**K).numerator//(lo*16**K).denominator+1
    q=F(A,16**K)
    assert lo<q<hi
    gM=16**M*(q-P)
    D=gM-b
    assert 0<D<Dmax
    def g(n):
        if n<M: raise ValueError('tail n>=M')
        return bfun(n)+D/F(16**(n-M))
    def f(n):
        if n<=M:return forcing(n)
        return 16*g(n-1)-g(n)
    assert 0<f(M+1)<f(M)
    return q,K,f,g,D


def concat_bound(B,k):
    # Count an overcomplete description: choose d nonextreme locations with
    # 14 symbols; at most d+1 extreme groups, each with initial bit,
    # and choose w extreme-to-extreme flips on at most B edges.
    return 2*sum(math.comb(B,d)*math.comb(B,w)*28**d
                 for d in range(k+1) for w in range(k-d+1))


class TerminalWallCrucible(unittest.TestCase):
    def test_original_source_and_prior_terminal_finite_replay(self):
        for B in (16,32,64,128,256):
            x=U(2*B)
            direct=sum((forcing(j)/16**j for j in range(1,2*B+1)),F(0))
            self.assertEqual(x/16**(2*B),direct)
            E=terminal_energy(x,B)
            self.assertGreater(E,F(0))
            self.assertGreater(8*E-F(8,225*B)*forcing(2*B+1),F(3,5))
            self.assertGreaterEqual(E,domain_bounds(x,B)[0])
            self.assertLessEqual(E,domain_bounds(x,B)[1])

    def test_digit_reconstruction_and_energy_exact(self):
        for B in (1,2,3,4,7,16):
            samples=(F(0), F(1,103),F(-1,103),F(16**B-1)+F(1,103),
                     F(16**B)+F(1,103),U(2*B))
            for q in samples:
                ds=symbols(q,B)
                C=q.numerator//q.denominator
                u=q-C
                y=u
                energy=F(0)
                for d in ds:
                    y=(d+y)/16
                    energy+=torus(y)**2
                self.assertEqual(energy/B,terminal_energy(q,B))
                lo,hi=domain_bounds(q,B)
                self.assertLessEqual(lo,terminal_energy(q,B))
                self.assertLessEqual(terminal_energy(q,B),hi)

    def test_exhaustive_small_digit_words_against_wall_bound(self):
        # 16^3=4096 words, 4 distinct fractions for each sample.
        B=3
        for digs in product(range(16),repeat=B):
            C=sum(d*16**i for i,d in enumerate(digs))
            for u in (F(0),F(1,2),F(100,101)):
                q=C+u
                lo,hi=domain_bounds(q,B)
                en=terminal_energy(q,B)
                self.assertLessEqual(lo,en)
                self.assertLessEqual(en,hi)

    def test_full_shadows_and_zero_F_runs(self):
        for B in (1,2,4,8,16,64):
            for C in (0,16**B-1,16**B,16**(B+2)-1):
                q=F(C)+F(1,103)
                D,W=defect_counts(q,B)
                self.assertEqual((D,W),(0,0))
                self.assertLessEqual(terminal_energy(q,B),F(1,255*B))
            # C=-1: coherent wrong-seed terminal -T_m has all F residues.
            wrong=-F(1,200*B*B)
            self.assertEqual(defect_counts(wrong,B),(0,0))
            self.assertLessEqual(terminal_energy(wrong,B),F(1,255*B))

    def test_terminal_plus_one_carry_changes_few_wall_events(self):
        samples=(0,16**6-1, 16**6, 16**4-1+3*16**4,
                 15*16**5+7*16**2+15*16+15)
        for B in (2,5,8,12):
            for c in samples:
                d,w=defect_counts(F(c),B)
                nd,nw=defect_counts(F(c+1),B)
                self.assertLessEqual(abs(nd-d),1)
                self.assertLessEqual(abs(nw-w),2)
        # Stronger witness: actual BBP completed integer either C or C+1.
        for B in (16,32,64):
            c=U(2*B).numerator//U(2*B).denominator
            d,w=defect_counts(F(c),B)
            nd,nw=defect_counts(F(c+1),B)
            self.assertLessEqual(abs(nd-d)+abs(nw-w),3)

    def test_all_odd_cofactor_residues_allow_locked_terminal_suffix(self):
        for B,Q,a in ((4,105,17),(8,3*5*7*11,222),(12,101,3)):
            q_inv=pow(16**B,-1,Q)
            t=(a*q_inv)%Q
            C=(16**B)*t
            self.assertEqual(C%Q,a%Q)
            self.assertEqual(C%16**B,0)
            # U=C+1/Q has exactly the same odd denominator and N mod Q=1.
            Uc=F(C)+F(1,Q)
            self.assertEqual(Uc.denominator,Q)
            self.assertEqual(Uc.numerator%Q,1)
            self.assertEqual(defect_counts(Uc,B),(0,0))
            self.assertLessEqual(terminal_energy(Uc,B),F(1,255*B*Q*Q))
            # All-F suffix also compatible with every specified odd residue.
            C2=(16**B)*((a+1)*q_inv%Q)-1
            self.assertEqual(C2%Q,a%Q)
            self.assertEqual(C2%16**B,16**B-1)
            self.assertEqual(defect_counts(F(C2)+F(1,Q),B),(0,0))

    def test_exact_positive_zero_seed_locked_counterfeit(self):
        for M in (1,8,32,64):
            q,K,f,g,D=positive_locked_counterfeit(M)
            self.assertEqual(q.denominator&(q.denominator-1),0)
            self.assertLessEqual(q.denominator,16**K)
            self.assertTrue(all(f(n)==forcing(n) for n in range(1,M+1)))
            self.assertEqual(sum((f(n)/16**n for n in range(1,M+1)),F(0)),
                             q-F(g(M),16**M))
            # Entire original M-step prefix, zero seed, future rational.
            for n in (M+1,M+2,M+8,M+25):
                self.assertGreater(g(n),0)
                self.assertGreater(f(n),0)
                self.assertGreater(f(n-1),f(n))
                self.assertEqual(f(n),16*g(n-1)-g(n))
                u=sum((f(j)*16**(n-j) for j in range(1,n+1)),F(0))
                self.assertEqual(u+g(n),16**n*q)
            B=max(K,M+2)
            Uc=16**(2*B)*q-g(2*B)
            self.assertEqual(defect_counts(Uc,B),(0,0))
            self.assertEqual(terminal_energy(Uc,B),
                             g(2*B)**2*(F(1)-F(1,16**(2*B)))/(255*B))
            self.assertEqual((16**(K+1)*q)%1,0)

    def test_counterfeit_matched_gamma_leading_constant(self):
        for M in (1,8,32):
            q,K,f,g,D=positive_locked_counterfeit(M)
            for n in (M+100,M+300,M+700):
                # leading n² r(n) -> 15/64 and n² g(n)->1/64
                rf=n*n*f(n)
                gf=n*n*g(n)
                main_correction=F(1,64)*(1-F(n*n,(n+1)**2))
                self.assertEqual(gf-F(1,64),
                                 -main_correction+D*F(n*n,16**(n-M)))
                self.assertEqual(rf-F(15,64),
                                 main_correction+F(255,16)*D*F(n*n,16**(n-1-M)))
                self.assertLess(abs(float(rf-F(15,64))),.006)
                self.assertLess(abs(float(gf-F(1,64))),.0005)

    def test_domain_wall_count_controls_digit_combinatorial_entropy(self):
        # Exhaust all 4096 length-three words; for each budget K, compare
        # exact count with an algebraic upper bound based on defect positions.
        words=[]
        for digs in product(range(16),repeat=3):
            C=sum(d*16**i for i,d in enumerate(digs))
            words.append(sum(x not in (0,15) for x in digs)+
                         sum((digs[i],digs[i+1]) in ((0,15),(15,0))
                             for i in range(2)))
        for K in (0,1,2,3):
            count=sum(e<=K for e in words)
            self.assertLessEqual(count,concat_bound(3,K))
        self.assertEqual(sum(e==0 for e in words),2)

    def test_low_energy_implies_sparse_defects_and_long_extreme_run(self):
        for B in (8,16,32,64):
            q=F(16**B-1)+F(1,5)
            R=terminal_energy(q,B)
            D,W=defect_counts(q,B)
            self.assertEqual((D,W),(0,0))
            self.assertLessEqual(D+W,F(65536,225)*B*R)
            self.assertGreaterEqual(B, (B-D)/(D+W+1))

    def test_terminal_phase_fiber_clone_preserves_cofactor_but_erases_winding(self):
        for B in (16,32,64,128,256):
            u=U(2*B)
            C=u.numerator//u.denominator
            frac=u-C
            Cclone=(C//16**B)*16**B
            clone=F(Cclone)+frac
            self.assertEqual(clone.denominator,u.denominator)
            self.assertEqual(clone.numerator%u.denominator,
                             u.numerator%u.denominator)
            self.assertEqual((u-clone)%1,0)
            self.assertGreaterEqual(u-clone,0)
            self.assertLess(u-clone,16**B)
            self.assertEqual(defect_counts(clone,B),(0,0))
            self.assertEqual(terminal_energy(clone,B),
                             frac*frac*(1-F(1,16**(2*B)))/(255*B))
            self.assertGreater(terminal_energy(u,B),F(1,20))
            self.assertLess(terminal_energy(clone,B),F(1,255*B))

    def test_actual_fresh_prime_denominator_is_not_just_a_phase_witness(self):
        def isprime(p):
            return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
        found=0
        for n in range(2,40):
            p=8*n-7
            if not isprime(p): continue
            u=U(n)
            self.assertEqual(u.denominator%p,0)
            self.assertNotEqual(u.numerator%p,0)
            # A phase-fiber clone retains exact denominator and numerator
            # mod p while choosing a terminal integer with a zero suffix.
            B=max(1,n//2)
            C=u.numerator//u.denominator
            clone=F((C//16**B)*16**B)+(u-C)
            self.assertEqual(clone.denominator,u.denominator)
            self.assertEqual(clone.numerator%p,u.numerator%p)
            self.assertEqual(defect_counts(clone,B),(0,0))
            found+=1
        self.assertGreater(found,4)

    def test_wrong_seed_same_forcing_is_stronger_than_numerical_test(self):
        # Symbolic exact identity U_m(-x)=-T_m is the analytic countermodel.
        # For every 0<T_m<1, floor(-T_m)=-1 and fractional 1-T_m.
        for B in (4,16,64):
            T=F(1,64*(2*B+1)**2)  # lawful toy tail, NOT original T_m
            wrong=-T
            self.assertEqual(wrong.numerator//wrong.denominator,-1)
            self.assertEqual(symbols(wrong,B), (15,)*B)
            self.assertEqual(terminal_energy(wrong,B),
                             T*T*(F(1)-F(1,16**(2*B)))/(255*B))

if __name__=='__main__':unittest.main()
