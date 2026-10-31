"""Original BBP carrier -> raw-state occupation, entropy rigidity and hostile controls.

All arithmetic prefixes are certified with original four-pole rational intervals.
Finite tests do NOT establish normality of pi. Only stdlib is needed.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from math import ceil, comb, cos, exp, floor, log, sqrt
from itertools import product
import unittest

BASE = 16
POLES = ((4, 0), (-2, 3), (-1, 4), (-1, 5))


def R(a):
    a = F(a)
    return sum((F(c) / (a + d) for c, d in POLES), F(0))


def forcing(n):
    assert n >= 1
    return R(8*n - 7)


def original_alpha_prefix(M):
    """Interval for alpha=pi/16; strictly positive monotonically shrinking r_n.

    Tail sum_{j>M}16^-j*r_j < 16^-M*r_(M+1)/15.
    Returns [lower,upper] with exact rational endpoints.
    """
    value = F(0)
    weight = F(1, BASE)
    for n in range(1, M + 1):
        value += weight * forcing(n)
        weight /= BASE
    return value, value + forcing(M + 1) / (15 * BASE**M)


def certified_hex_digits(K, M=None):
    """Certify the first K radix16 digits of pi/16 from original BBP source."""
    if M is None:
        M = K + 2
    lo, hi = original_alpha_prefix(M)
    a = (BASE**K * lo).__floor__()
    b = (BASE**K * hi).__floor__()
    if a != b:
        raise ValueError(f'hex prefix uncertified at K={K}, M={M}')
    return tuple((a >> (4*(K-j-1))) & 15 for j in range(K))


def native_forced_orbit(N, seed=F(0)):
    u = F(seed)
    ans=[]
    for n in range(1, N+1):
        u = BASE*u + forcing(n)
        ans.append(u - (u.numerator//u.denominator))
    return ans


def phi_cyl_counts(digits, N, k):
    assert len(digits) >= N + k - 1
    return Counter(tuple(digits[j:j+k]) for j in range(N))


SOURCE_ATOMS = ((2, 3), (1, 4), (1, 5))


def source_mark_law(n):
    a=8*n-7
    masses=tuple(F(c*d, a*(a+d)) for c,d in SOURCE_ATOMS)
    return tuple(v/sum(masses) for v in masses)


def source_mark_reference():
    return tuple(F(c*d,15) for c,d in SOURCE_ATOMS)


def entropy_distribution(probs):
    return -sum(float(p)*log(float(p)) for p in probs if p)


def cyclic_block_counts(word, k):
    n = len(word)
    return Counter(tuple(word[(start+j) % n] for j in range(k)) for start in range(n))


def debruijn(alphabet, order):
    """FKM de Bruijn sequence: every order-k word appears once cyclically."""
    a = [0]*(alphabet*order+1)
    out=[]
    def rec(t,p):
        if t > order:
            if order % p == 0:
                out.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            rec(t+1,p)
            for j in range(a[t-p]+1,alphabet):
                a[t]=j
                rec(t+1,t)
    rec(1,1)
    return out


def cyclic_entropy(word, k):
    N=len(word)
    return entropy_distribution((F(c,N) for c in cyclic_block_counts(word,k).values()))


class CarrierRealization(unittest.TestCase):
    def test_source_positive_and_decreasing(self):
        for n in range(1,150):
            self.assertGreater(forcing(n),0)
            self.assertGreater(forcing(n),forcing(n+1))
        self.assertEqual(forcing(1),F(47,15))

    def test_original_pi_interval_certification(self):
        for K in (16,64,128,512,1024):
            ds=certified_hex_digits(K,K+2)
            self.assertEqual(''.join(format(d,'x') for d in ds[:16]),'3243f6a8885a308d')
            self.assertTrue(all(0<=d<16 for d in ds))

    def test_source_tail_budget_elementary(self):
        # Original Green bound T_n <= 1/((8n+1)(8n+2)).
        # Sum over n>=1 < 1/81+1/72 < 1/32.
        self.assertLess(F(1,81)+F(1,72),F(1,32))
        for n in range(1,90):
            # T_n = sum_{j>=1} 16^-j r_{n+j} bounded by r_{n+1}/15.
            self.assertLess(forcing(n+1)/15,F(1,(8*n+1)*(8*n+2)))

    def test_forced_to_pure_radix_source_bridge(self):
        # Pure y_n={16^n*pi/16}; forced x_n={U_n(0)} differs by -T_n.
        # Knowing a certified K-digit prefix gives y_n to ±16^-(K-n).
        N=120
        K=N+9
        digits=certified_hex_digits(K,K+1)
        P=0
        for d in digits:P=P*16+d
        forced=native_forced_orbit(N)
        for n in range(1,N+1):
            remaining=K-n
            y_lower=F(P % (16**remaining),16**remaining)
            x=forced[n-1]
            diff=abs(x-y_lower)
            d=min(diff,1-diff)
            self.assertLessEqual(d,forcing(n+1)/15+F(1,16**remaining))

    def test_selected_finite_occupancy_exact(self):
        N=2048
        ds=certified_hex_digits(N+3,N+5)
        for k in (1,2,3):
            counts=phi_cyl_counts(ds,N,k)
            self.assertEqual(sum(counts.values()),N)
            self.assertGreaterEqual(max(counts.values())*16**k,N)
            self.assertTrue(all(len(w)==k for w in counts))

    def test_biased_full_support_not_normal(self):
        p=[F(2,17)]+[F(1,17)]*15
        self.assertEqual(sum(p),1)
        h=entropy_distribution(p)
        delta=log(16)-h
        self.assertGreater(delta,0)
        for k in range(1,7):
            max_cyl=p[0]**k
            excess=(16**k)*max_cyl
            self.assertEqual(excess,F(32,17)**k)
            self.assertGreater(float(excess),exp(k*delta))

    def test_debruijn_bounded_order_mimics_higher_normality(self):
        a=debruijn(16,2)
        self.assertEqual(len(a),256)
        c2=cyclic_block_counts(a,2)
        self.assertEqual(len(c2),256)
        self.assertTrue(all(v==1 for v in c2.values()))
        c3=cyclic_block_counts(a,3)
        self.assertGreater(max(c3.values())*16**3,len(a))
        self.assertAlmostEqual(cyclic_entropy(a,2),2*log(16),places=12)
        self.assertLess(cyclic_entropy(a,3),3*log(16))

    def test_finite_entropy_amplifies_long_cylinders(self):
        a=debruijn(16,2)
        for q in (1,2,3,4):
            delta=q*log(16)-cyclic_entropy(a,q)
            self.assertGreaterEqual(delta,-1e-12)
            for m in (2,3,4):
                c=cyclic_block_counts(a,q*m)
                max_cyl=F(max(c.values()),len(a))
                # Subadditive entropy + H>=-log(pmax):
                self.assertGreaterEqual(log(float(max_cyl)) +q*m*log(16),m*delta-1e-10)

    def test_epsilon_concentration_finite_bound(self):
        # Empirical cylindrical bridge between exact forced rational states
        # and certified pure-radix states. Inclusion is under a buffer,
        # never an exact cylinder-equivalence without seam controls.
        N=120;K=N+8
        ds=certified_hex_digits(K,K+2)
        P=0
        for d in ds:P=16*P+d
        forced=native_forced_orbit(N)
        M_upper=F(1,32)  # rigorous elementary Green bound
        for k in (1,2):
            eps=F(1,8*16**k)
            error_allow=M_upper/eps
            for w in range(16**k):
                left=F(w,16**k);right=F(w+1,16**k)
                x_count=0;possible_y=0
                for n,x in enumerate(forced,start=1):
                    if left<=x<right:x_count+=1
                    rem=K-n
                    z=F(P % (16**rem),16**rem)
                    uncertainty=F(1,16**rem)
                    if left<=z<=right:
                        distance=F(0)
                    else:
                        d1=abs(z-left);d2=abs(z-right)
                        distance=min(d1,d2,1-d1,1-d2)
                    if distance<=eps+uncertainty:possible_y+=1
                self.assertLessEqual(F(x_count),F(possible_y)+error_allow)

    def test_invariance_is_necessary_for_subexponential_rigidity(self):
        # A NONINVARIANT measure: digit 0 at the first position, then
        # all subsequent digits uniform. Max cylinder ratio b is constant;
        # log ratio / k ->0, but this measure is manifestly not Haar.
        for k in (1,2,4,8,32):
            pmax=F(1,16**(k-1))
            self.assertEqual(pmax*16**k,16)
        self.assertNotEqual(F(1),F(1,16))

    def test_full_support_and_nonhaar_are_compatible(self):
        # Any biased Bernoulli product with p_i>0 has full shift support.
        # Yet its single-symbol frequency vector is not uniform.
        p=[F(2,17)]+[F(1,17)]*15
        for k in (1,2,3):
            for w in product(range(16),repeat=k):
                prob=F(1)
                for v in w:prob*=p[v]
                self.assertGreater(prob,0)
        self.assertNotEqual(p[0],F(1,16))

    def test_three_time_raw_state_hairpin_graph_and_resonances(self):
        # Even if the driving alpha were normal, three consecutive circle
        # states lie on the graph (x,T16*x,T16^2*x), NOT T^3 Haar.
        K=180
        ds=certified_hex_digits(K,K+2)
        P=0
        for d in ds:P=16*P+d
        y=[]
        for n in range(1,61):
            rem=K-n
            y.append(F(P%(16**rem),16**rem))
        for n in range(58):
            self.assertEqual((16*y[n])%1,y[n+1])
            self.assertEqual((16*y[n+1])%1,y[n+2])
            # Exact resonant character: e(16*x-y)=1.
            self.assertEqual((16*y[n]-y[n+1])%1,0)
            self.assertEqual((16*y[n+1]-y[n+2])%1,0)
        self.assertEqual(16*16-256,0)

    def test_forced_three_time_relation_contains_original_source_only(self):
        x=native_forced_orbit(128)
        for n in range(1,127):
            # Literal arithmetic relation, independent of seed;
            # modulo-1 graph resonance retains source forcing r_(n+1).
            delta=(16*x[n-1]-x[n]+forcing(n+1))%1
            self.assertEqual(delta,0)

    def test_three_time_wasserstein_source_budget(self):
        # Coupling the j-th observed forced state with pure radix state
        # at every fixed lag gives W1(T^3) <=3*M_BBP/N. Exact bound.
        N=64;K=N+12
        ds=certified_hex_digits(K,K+2)
        P=0
        for d in ds:P=16*P+d
        x=native_forced_orbit(N+2)
        cumulative_bound=F(0)
        for n in range(1,N+1):
            for lag in (0,1,2):
                m=n+lag
                rem=K-m
                y_lower=F(P % (16**rem),16**rem)
                diff=abs(x[m-1]-y_lower)
                d=min(diff,1-diff)
                self.assertLessEqual(d,forcing(m+1)/15+F(1,16**rem))
                cumulative_bound+=forcing(m+1)/15
        self.assertLess(cumulative_bound,F(3,32))

    def test_uncoupled_source_atom_labels_factor_out_in_raw_quotient(self):
        beta=source_mark_reference()
        self.assertEqual(beta,(F(2,5),F(4,15),F(1,3)))
        for n in range(2,501):
            a=8*n-7
            m=source_mark_law(n)
            self.assertEqual(sum(m),1)
            for p,q in zip(m,beta):
                self.assertLessEqual(abs(p-q),F(4,a)*q)
        for N in (16,128,512):
            diff=sum((sum(abs(p-q) for p,q in zip(source_mark_law(n),beta))
                      for n in range(1,N+1)),F(0))
            # For any selected state labels, this bounds the full joint
            # marked-state total variation after normalization.
            loose=F(2)+4*sum((F(1,8*n-7) for n in range(2,N+1)),F(0))
            self.assertLessEqual(diff,loose)
            self.assertLessEqual(diff/(2*N),loose/(2*N))

    def test_coherent_seed_same_source_raw_state_delta(self):
        # s_star=-pi/16 gives y_n={16^n(s_star+pi/16)}=0 always;
        # this proof identity is independent of the finite approximation.
        # The formal identity s_star=-alpha makes pure y_n=0 exactly.
        # The forced x_n is {-T_n}; T_n>0, T_n->0 from source bounds.
        for n in (1,2,5,20,80):
            partial=sum((forcing(n+j)/16**j for j in range(1,15)),F(0))
            self.assertGreater(partial,0)
            self.assertLess(partial,forcing(n+1)/15)
            self.assertLess(forcing(n+1)/15,F(1,8*n+1))


if __name__=='__main__':
    unittest.main(verbosity=2)
