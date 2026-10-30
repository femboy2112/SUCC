"""Source-locked Pascal/Binomial -> Oily endpoint, signed phase lift.

Research-only. No claim of pi-normality. Exact fractions for finite
source/grade probabilities, a bounded complex phase toy as a control.

Derived from original SUCC four-pole r(n), unchanged U0=0.
No optional packages; run `python pascal_oily_probe.py`.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, isclose, sqrt, pi, cos, sin
import unittest


def forcing(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("authentic positive integer source time required")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def positive_carrier_r(a: int | F) -> F:
    a=F(a)
    if a<=0:
        raise ValueError("positive Laplace parameter required")
    return F(4)/a-F(2)/(a+3)-F(1)/(a+4)-F(1)/(a+5)


def laplace_moment(n: int,k:int) -> F:
    if type(k) is not int or k<0:
        raise ValueError("nonnegative moment required")
    return forcing(n+k)/forcing(n)


def pascal_packet(n:int) -> tuple[F,...]:
    """J|X ~ Bin(n,1-e^{-8X}), X~authentic BBP mu_(8n-7)."""
    forcing(n)
    den=forcing(n)
    return tuple(F(comb(n,j))*sum((F((-1)**k*comb(j,k))*forcing(2*n-j+k)
                                  for k in range(j+1)),F(0))/den
                 for j in range(n+1))


def pascal_pgf_direct(n:int,z:F) -> F:
    """Independent Pascal orientation via E[(z+(1-z)e^{-8X})**n]."""
    forcing(n)
    z=F(z)
    return sum((F(comb(n,k))*z**(n-k)*(1-z)**k*forcing(n+k)
                for k in range(n+1)),F(0))/forcing(n)


def oily_limit_weight(j:int) -> F:
    if type(j) is not int or j<0:
        raise ValueError("grade >=0 required")
    return F(j+1,2**(j+2))


def oily_limit_pgf(z:F)->F:
    return 1/(2-F(z))**2


def moment(n:int,order:int)->F:
    """E[X**order] exact from four-pole Laplace representation."""
    forcing(n)
    if type(order) is not int or order<0:
        raise ValueError("moment order")
    from math import factorial
    a=8*n-7
    return F(factorial(order))*sum((F(c, (a+d)**(order+1))
                         for d,c in ((0,4),(3,-2),(4,-1),(5,-1))),F(0))/forcing(n)


def tv_bound(n:int) -> F:
    """Rigorous, non-optimal TV distance to NB(2,1/2); valid n>=3."""
    if type(n) is not int or n<3:
        raise ValueError("n>=3 needed for Gamma2 density budget")
    a=8*n-7
    return min(F(1),F(576*n,a*a)+F(20,a))


def weight_tv_partial(n:int)->F:
    """Exact TV incl. all infinite Oily tail (no floating truncation)."""
    weights=pascal_packet(n)
    leftovers=F(n+3,2**(n+2))  # sum_{j>=n+1} (j+1)/2^(j+2)
    return (sum((abs(p-oily_limit_weight(j)) for j,p in enumerate(weights)),F(0))
            +leftovers)/2


def golden_fixed(n:int,steps=90)->tuple[F,F]:
    """Rational enclosure of the unique interior PGF fixed point for n>=2."""
    if n<2:
        raise ValueError("n=1 has no interior fixed point")
    weights=pascal_packet(n)
    def diff(z):return sum((p*z**j for j,p in enumerate(weights)),F())-z
    low,high=F(0),F(1)
    assert diff(low)>0 and diff(F(1)-F(1,10**6))<0
    for _ in range(steps):
        mid=(low+high)/2
        if diff(mid)>0:low=mid
        else:high=mid
    return low,high


def source_pgf_correction(z:F)->F:
    """First 1/n coefficient from four-pole Q''(0)=-59 and a=8n-7."""
    z=F(z)
    t=1-z
    return t*(209-511*t)/(120*(1+t)**4)


def original_state_prefix(length:int, seed:F=F(0)) ->tuple[F,...]:
    if type(length) is not int or length<0: raise ValueError("length")
    u=F(seed)
    out=[u]
    for k in range(1,length+1):
        u=(16*u+forcing(k))%1
        out.append(u)
    return tuple(out)


def lifted_readout(n:int, state_prefix:tuple[F,...],h:int=1)->complex:
    """Finite source-Pascal weighted selected absolute circle phase."""
    if len(state_prefix) <=2*n:raise ValueError("needs original U through 2n")
    z=[complex(cos(2*pi*h*float(x)),sin(2*pi*h*float(x))) for x in state_prefix]
    return sum(complex(float(p))*z[n+j] for j,p in enumerate(pascal_packet(n)))


def oily_readout(n:int, z:tuple[complex,...]) ->complex:
    if len(z)<=n+1:raise ValueError("need future states")
    return sum(float(oily_limit_weight(j))*z[n+j] for j in range(len(z)-n))


def mean_first(n:int)->F:
    """E[J_n] = n(1-r(n+1)/r(n)), source exact."""
    return n*(1-laplace_moment(n,1))


def pascal_packet_power(n: int, power: int) -> tuple[F, ...]:
    """Pascal thinning of power independent copies of BBP mu_(8n-7).

    The corresponding continuum Gamma rank is 2*power.  This is a
    DECLARED convolution product, not another physical BBP source.
    """
    forcing(n)
    if type(power) is not int or power < 1:
        raise ValueError("positive integer convolution power")
    den=forcing(n)**power
    return tuple(F(comb(n,j))*sum((F((-1)**k*comb(j,k))*forcing(2*n-j+k)**power
                                   for k in range(j+1)),F(0))/den
                 for j in range(n+1))


def pascal_pgf_power(n: int, power: int, z: F) -> F:
    forcing(n)
    if type(power) is not int or power<1: raise ValueError("power")
    z=F(z)
    den=forcing(n)**power
    return sum((F(comb(n,k))*z**(n-k)*(1-z)**k*forcing(n+k)**power
               for k in range(n+1)),F(0))/den


def pascal_rank_weight(rank:int, grade:int)->F:
    if type(rank) is not int or rank<1 or type(grade) is not int or grade<0:
        raise ValueError("integer shape rank and grade required")
    return F(comb(grade+rank-1,rank-1),2**(grade+rank))


def general_first_correction(rank:int,z:F)->F:
    """Asymptotic n*(PGF_n(z)-(2-z)^(-rank)) at fixed integer rank."""
    if type(rank) is not int or rank<1:raise ValueError("positive rank")
    t=1-F(z)
    return F(rank)*t/(1+t)**(rank+2) * (F(-151,240)*(1+t)+F(rank+1,2)*(1-t))


def signed_pascal_inverse_coefficients(rank:int)->tuple[int,...]:
    """Coefficients of (2-S)^rank: genuine signed Pascal row."""
    if type(rank) is not int or rank<0:raise ValueError("rank")
    return tuple((-1)**j*comb(rank,j)*2**(rank-j) for j in range(rank+1))


class PascalOilySourceTests(unittest.TestCase):
    def test_original_poles_and_positive_source(self):
        self.assertEqual(forcing(1),F(47,15))
        self.assertEqual(positive_carrier_r(F(8*7-7)),forcing(7))
        for n in range(1,50):self.assertGreater(forcing(n),0)

    def test_exact_mass_and_strict_positivity(self):
        for n in range(1,37):
            p=pascal_packet(n)
            self.assertEqual(sum(p),1)
            self.assertTrue(all(x>0 for x in p))

    def test_exact_pgf_independent_binomial_orientation(self):
        for n in range(1,18):
            p=pascal_packet(n)
            for z in (F(0),F(1,7),F(1,2),F(5,6),F(1)):
                self.assertEqual(sum((x*z**j for j,x in enumerate(p)),F()),
                                 pascal_pgf_direct(n,z))

    def test_exact_source_moments(self):
        for n in range(3,40):
            a=8*n-7
            self.assertLess(moment(n,1),F(2,a))
            self.assertLess(moment(n,2),F(6,a*a))
            self.assertEqual(moment(n,0),F(1))

    def test_exact_mean(self):
        for n in range(1,24):
            self.assertEqual(sum((F(j)*v for j,v in enumerate(pascal_packet(n))),F()),mean_first(n))

    def test_fixed_point_birth(self):
        self.assertLess(mean_first(1),1)
        for n in range(2,40):
            self.assertGreater(mean_first(n),1)
            low,high=golden_fixed(n,steps=35)
            self.assertTrue(F(0)<low<high<F(1))
        low,high=golden_fixed(2)
        self.assertTrue(low<=F(576147,1824887)<=high)

    def test_oily_limit_probability(self):
        self.assertEqual(sum((oily_limit_weight(j) for j in range(100)),F()),
                         F(1)-F(102,2**101))
        self.assertEqual(oily_limit_pgf(F(0)),F(1,4))
        self.assertEqual(oily_limit_pgf(F(1,2)),F(4,9))
        self.assertEqual(oily_limit_pgf(F(1)),F(1))

    def test_total_variation_exact_finite_vs_bound(self):
        for n in (3,4,5,8,12,20,30,40,50,60):
            dist=weight_tv_partial(n)
            self.assertLessEqual(dist,tv_bound(n))
            self.assertLessEqual(dist,F(22,n))

    def test_first_coefficient_exact_source_fingerprint(self):
        for n in (10,20,50,100,200,1000):
            val=F(n)*(forcing(2*n)/forcing(n)-F(1,4))
            self.assertLess(abs(val-F(-151,960)),F(1,2))
        self.assertLess(abs(F(1000)*(forcing(2000)/forcing(1000)-F(1,4))+F(151,960)),F(1,1000))
        self.assertNotEqual(forcing(2*100)/forcing(100),F(1,4))
        self.assertEqual((F(100)**2)/(F(200)**2),F(1,4)) # mutant r(n)=1/n²

    def test_full_pgf_first_correction(self):
        for z in (F(0),F(1,4),F(1,2),F(3,4)):
            for n in (20,50,100,200):
                value=pascal_pgf_direct(n,z)
                self.assertLess(abs(F(n)*(value-oily_limit_pgf(z)) - source_pgf_correction(z)),F(1,2))
            value=pascal_pgf_direct(200,z)
            self.assertLess(abs(F(200)*(value-oily_limit_pgf(z))-source_pgf_correction(z)),F(1,30))

    def test_seed_sensitive_readout_not_weight_mutation(self):
        n=5
        a=original_state_prefix(2*n,F(0))
        b=original_state_prefix(2*n,F(1,7))
        self.assertEqual(pascal_packet(n),pascal_packet(n))
        self.assertGreater(abs(lifted_readout(n,a)-lifted_readout(n,b)),0.02)


    def test_rank_four_pascal_row_and_base_16_resonance(self):
        self.assertEqual(signed_pascal_inverse_coefficients(4),(16,-32,24,-8,1))
        self.assertEqual(sum(signed_pascal_inverse_coefficients(4)),1)
        self.assertEqual(sum(abs(x) for x in signed_pascal_inverse_coefficients(4)),81)
        self.assertEqual(pascal_rank_weight(4,0),F(1,16))
        self.assertEqual(pascal_rank_weight(2,0),F(1,4))

    def test_rank_four_exact_pascal_law(self):
        for n in range(2,27):
            p=pascal_packet_power(n,2)
            self.assertTrue(all(x>0 for x in p))
            self.assertEqual(sum(p),1)
            for z in (F(0),F(1,3),F(1,2),F(1)):
                self.assertEqual(sum((v*z**j for j,v in enumerate(p)),F()),
                                 pascal_pgf_power(n,2,z))
        self.assertEqual(pascal_packet_power(8,1),pascal_packet(8))

    def test_rank_four_source_specific_first_correction(self):
        for z in (F(0),F(1,2),F(3,4)):
            c=general_first_correction(4,z)
            for n in (100,200):
                obs=pascal_pgf_power(n,2,z)
                baseline=1/(2-z)**4
                self.assertLess(abs(n*(obs-baseline)-c),F(1,15))
            n=200
            obs=pascal_pgf_power(n,2,z)
            self.assertLess(abs(n*(obs-1/(2-z)**4)-c),F(1,20))
        self.assertEqual(general_first_correction(2,F(0)),F(-151,960))
        self.assertEqual(general_first_correction(4,F(0)),F(-151,1920))

    def test_rank_four_oily_inverse(self):
        z=tuple(complex(cos(i/9),sin(i/9)) for i in range(500))
        def average(k):
            return sum(float(pascal_rank_weight(4,j))*z[k+j] for j in range(500-k))
        coef=signed_pascal_inverse_coefficients(4)
        for n in range(7,35):
            self.assertLess(abs(sum(coef[j]*average(n+j) for j in range(5))-z[n]),1e-10)

    def test_15_torsion_absolute_origin_control(self):
        n=5
        a=original_state_prefix(2*n,F(0))
        b=original_state_prefix(2*n,F(1,15))
        c=complex(cos(2*pi/15),sin(2*pi/15))
        self.assertLess(abs(lifted_readout(n,b)-c*lifted_readout(n,a)),1e-12)

    def test_coherent_constant_readout_is_not_cancelled(self):
        n=8
        q=pascal_packet(n)
        self.assertEqual(sum(q),F(1))
        self.assertEqual(sum(q[j]*F(1) for j in range(n+1)),F(1))

    def test_infinite_oily_inverse_on_bounded_sequence(self):
        z=tuple(complex(cos(k/7),sin(k/7)) for k in range(350))
        for n in range(10,50):
            s=[oily_readout(k,z) for k in (n,n+1,n+2)]
            self.assertLess(abs(z[n]-(4*s[0]-4*s[1]+s[2])),1e-10)

    def test_oily_cesaro_gain_without_cancellation(self):
        z=tuple(complex(cos(k/13),sin(k/13)) for k in range(1000))
        start,N=3,150
        oot=[oily_readout(n,z) for n in range(start,start+N)]
        gap=abs(sum(oot)/N-sum(z[start:start+N])/N)
        self.assertLess(gap, F(4,N)+1e-9)

    def test_pascal_readout_to_oily_estimate(self):
        # Actual source phases plus their infinite Oily smoothing.
        n=16
        hist=original_state_prefix(200)
        z=tuple(complex(cos(2*pi*float(x)),sin(2*pi*float(x))) for x in hist)
        T=lifted_readout(n,hist)
        S=oily_readout(n,z)
        self.assertLessEqual(abs(T-S),2*float(tv_bound(n))+1e-12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
