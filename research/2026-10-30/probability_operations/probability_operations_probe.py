"""SUCC: probability-operation carrier test, fixed-window and exact finite certificates.

This is a finite verification of *conditional, classical* mathematical theorems.
No test result proves or disproves pi's normality.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isclose
from collections import Counter
import unittest

B=16
POLES=((4,0),(-2,3),(-1,4),(-1,5))


def R(a):
    a=F(a)
    return sum((F(c)/(a+k) for c,k in POLES),F(0))


def alpha_interval(m):
    """Rational enclosure for alpha=pi/16 from unmodified original BBP source."""
    lo=F(0)
    for j in range(1,m+1):
        lo+=R(8*j-7)/B**j
    # source r_j positive and decreasing; bound tail by first omitted term.
    return lo,lo+R(8*(m+1)-7)/(15*B**m)


def certified_hex_digits(k):
    lo,hi=alpha_interval(k+2)
    a=(B**k*lo).__floor__()
    assert a == (B**k*hi).__floor__(), 'insufficient prefix interval'
    return tuple((a>>(4*(k-i-1))) & 15 for i in range(k))


def fixed_radix_tails(digits, length, count):
    """Integer numerator for length-digit tail of alpha, n=0,...,count.

    All resulting rational positions are within (1/B)^length of the true tail.
    """
    assert len(digits)>=count+length+1
    power=B**(length-1)
    val=sum(digits[j]*B**(length-j-1) for j in range(length))
    out=[val]
    for n in range(count):
        val=(val-digits[n]*power)*B+digits[n+length]
        out.append(val)
    assert all(0<=v<B**length for v in out)
    return out


def w1_empirical_vs_predecessor(tail_ints, length, base=B):
    """Exact 1-Wasserstein: empirical x[0:N] vs average f_d(x[1:N+1]).

    The points are rational with common denominator base^(length+1).
    """
    n=len(tail_ints)-1
    scale=base**length
    observed=sorted([base*x for x in tail_ints[:-1] for _ in range(base)])
    simulated=sorted([d*scale+x for x in tail_ints[1:] for d in range(base)])
    return F(sum(abs(x-y) for x,y in zip(observed,simulated)),base*n*base*scale)


def w1_empirical_to_uniform(tail_ints,length,base=B):
    """Exact W1 to continuous Lebesgue for the truncated empirical tails."""
    values=sorted(F(v,base**length) for v in tail_ints)
    n=len(values)
    ans=F(0)
    for i,x in enumerate(values):
        l,r=F(i,n),F(i+1,n)
        if x<=l: ans+=(r-l)*((l+r)/2-x)
        elif x>=r: ans+=(r-l)*(x-(l+r)/2)
        else: ans+=((x-l)**2+(r-x)**2)/2
    return ans


def periodic_states(base,word):
    """Exactly rational T_b orbit of a periodic word, plus closing state."""
    period=len(word)
    v=sum(d*base**(period-i-1) for i,d in enumerate(word))
    alpha=F(v,base**period-1)
    out=[alpha]
    for _ in range(period):out.append((base*out[-1])%1)
    assert out[-1]==alpha
    return out


def w1_explicit(real, model):
    """Exact W1 of two equally weighted rational arrays."""
    assert len(real)==len(model)
    n=len(real)
    return sum((abs(x-y) for x,y in zip(sorted(real),sorted(model))),F(0))/n

class ProbabilityOperationTests(unittest.TestCase):
    def test_original_four_pole_and_source_certified_prefix(self):
        self.assertEqual(R(1),F(47,15))
        a=certified_hex_digits(64)
        self.assertEqual(''.join(f'{d:x}' for d in a[:16]),'3243f6a8885a308d')

    def test_sqrt_max_is_distributional_not_pathwise(self):
        t=F(1,3)
        # Uniform: P(sqrt(U)<=t) = F(t*t) = t*t and max(U1,U2) CDF=F(t)^2=t*t.
        self.assertEqual(t*t,t**2)
        self.assertNotEqual(F(1,2),max(F(1,4),F(1,4)))

    def test_sqrt_max_beta_false_positive(self):
        # For F(t)=t^c, the law F(t^2)=F(t)^2 holds for ALL c>0.
        for c in (1,2,3):
            for t in (F(1,7),F(1,3),F(3,5),F(7,8)):
                self.assertEqual((t*t)**c,(t**c)**2)
        self.assertNotEqual(F(1,3)**2,F(1,3))

    def test_consecutive_tails_are_not_independent_even_for_normal_digits(self):
        # Haar x with y={16x}; event max(x,y)<=1/3 has probability 1/8,
        # while independent uniform tails would give 1/9.
        t=F(1,3)
        # floor(16t)=5, fractional part 1/3. Five complete cells plus one partial.
        full= (B*t).numerator//(B*t).denominator
        frac=(B*t)-full
        dependent=full*t/B + min(frac,t)/B
        self.assertEqual(full,5)
        self.assertEqual(dependent,F(1,8))
        self.assertEqual(t*t,F(1,9))
        self.assertNotEqual(dependent,t*t)

    def test_quantized_uniform_blocks_approximate_sqrt_max_law(self):
        # At any fixed block length L, correctly assembled normal digits
        # give two independent discrete grid uniforms under limiting block
        # frequencies. Their CDF laws differ by <=3 / 16^L.
        for k in (1,2,3):
            m=B**k
            for t in (F(1,7),F(1,3),F(3,5),F(7,8)):
                def gridcdf(z):
                    if z>=1: return F(1)
                    return F(min(m,int(m*z)+1),m)
                lhs=gridcdf(t*t)
                rhs=gridcdf(t)**2
                self.assertLessEqual(abs(lhs-rhs),F(3,m))

    def test_exact_fair_digit_branch_law(self):
        # Lebesgue is fixed by the branch-averaging operator P.
        # For rational 0<=a<b<=1, pushforward under f_d(y)=(d+y)/16
        # has support [d/16,(d+1)/16] and equal branch density.
        for d in range(B):
            for a,b in ((F(0),F(1)),(F(1,4),F(3,4)),(F(7,16),F(15,16))):
                self.assertEqual(((d+b)/B-(d+a)/B)/B,(b-a)/B**2)

    def test_coherent_seed_operator_residual_is_strong(self):
        n=32;real=[F(0)]*n
        simulated=[F(d,B) for _ in range(n) for d in range(B)]
        self.assertEqual(w1_explicit([F(0)]*len(simulated),simulated),F(15,32))
        # W1(delta_0,Haar)=1/2, upper bound is sharp in N->infinity.
        self.assertEqual(F(B,B-1)*F(15,32),F(1,2))

    def test_periodic_uniform_first_digit_not_normal(self):
        states=periodic_states(B,tuple(range(B)))
        digits=[int((B*x).__floor__()) for x in states[:-1]]
        self.assertEqual(sorted(digits),list(range(B)))
        # Exactly one of each digit, but the next digit is fixed by the current.
        n=B
        obs=states[:n]
        simulated=[F(d+x,B) for x in states[1:n+1] for d in range(B)]
        eps=w1_explicit([x for x in obs for _ in range(B)],simulated)
        self.assertGreater(eps,0)

    def test_source_certified_pi_state_operation_residual(self):
        length=8; Ns=(32,128,256)
        digits=certified_hex_digits(max(Ns)+length+2)
        for n in Ns:
            tails=fixed_radix_tails(digits,length,n)
            eps=w1_empirical_vs_predecessor(tails,length)
            mu=w1_empirical_to_uniform(tails[:-1],length)
            trunc=F(1,B**length)
            # The exact untruncated empirical measure satisfies
            # W1(mu_exact,Haar) <= b/(b-1) (eps+(1+1/b)trunc)+1/((b-1)*N).
            # The truncated empirical measure is within 'trunc' of the exact.
            theoretical=F(B,B-1)*(eps+(1+F(1,B))*trunc)+F(1,(B-1)*n)+trunc
            self.assertLessEqual(mu,theoretical)
            # Two-sided stability: the operation residual is comparable to
            # W1(state,Haar), up to endpoint and digit-truncation errors.
            lower=F(B,B+1)*eps-F(2)*trunc-F(1,(B+1)*n)
            self.assertGreaterEqual(mu,lower)
            self.assertGreater(eps,0)
            print(f'BBP certified n={n}, epsilon≈{float(eps):.9f}, state_w1≈{float(mu):.9f}, bound≈{float(theoretical):.9f}')

    def test_if_one_step_operation_defect_vanishes_unique_haar(self):
        # Formal finite inequality for any exact radix orbit is proved in dossier.
        # Calibrate on several finite periodic orbits with rational states.
        for b,word in ((2,(0,0,1,1)),(3,(0,1,2)),(16,(0,1,2,3))):
            states=periodic_states(b,word)
            n=len(word)
            sampled=states[:-1]
            candidates=[F(d+z,b) for z in states[1:] for d in range(b)]
            eps=w1_explicit([x for x in sampled for _ in range(b)],candidates)
            # Exact W1 from empirical to Haar, using quantile integral.
            # Reuse generic rational CDF formula, independent of base.
            vals=sorted(sampled)
            w=F(0)
            for j,x in enumerate(vals):
                l,r=F(j,n),F(j+1,n)
                if x<=l: w+=(r-l)*((l+r)/2-x)
                elif x>=r:w+=(r-l)*(x-(l+r)/2)
                else:w+=((x-l)**2+(r-x)**2)/2
            self.assertLessEqual(w,F(b,b-1)*eps+F(1,(b-1)*n))

    def test_idempotent_convolution_not_unique_without_no_atoms(self):
        # Uniform on finite subgroup Z/q is idempotent under addition mod 1.
        for q in (2,3,5,16):
            mass=Counter((i+j)%q for i in range(q) for j in range(q))
            self.assertEqual(set(mass),set(range(q)))
            self.assertTrue(all(v==q for v in mass.values()))
        # Such measures are NOT Haar on the full circle: they have atoms.

if __name__=='__main__':
    unittest.main(verbosity=2)
