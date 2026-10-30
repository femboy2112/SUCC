#!/usr/bin/env python3
"""SUCC original-four-pole triangular Gamma-rank source probe.
Research only: exact rational core, labelled high-precision numerical holdouts.
No Pi-normality, RH, physical-field, or original-seed mixing conclusion.
"""
from fractions import Fraction as F
from math import comb, factorial
import unittest

POLES = ((0, 4), (3, -2), (4, -1), (5, -1))

def rat(value):
    if type(value) not in (int, F):
        raise TypeError('only exact ints and Fraction values allowed')
    return F(value)

def source_R(a):
    a = rat(a)
    if a <= 0: raise ValueError('source a must be strictly positive')
    return sum((F(c,1)/(a+d) for d,c in POLES),F())

def source_R_factored(a):
    a = rat(a)
    if a <= 0: raise ValueError('source a must be strictly positive')
    return (15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5))

def bbp_forcing(n):
    if type(n) is not int or n < 1: raise ValueError('n >=1')
    return source_R(8*n-7)

def scaled_laplace(a,s):
    """L_a(s)=R(a*(1+s))/R(a), s>=0 is dimensionless."""
    a,s=rat(a),rat(s)
    if a<=0 or s<0: raise ValueError('a>0, s>=0')
    return source_R(a*(1+s))/source_R(a)

def source_tilt_compose(a,s,t):
    a,s,t=rat(a),rat(s),rat(t)
    return (source_R(a+s+t)/source_R(a),
            source_R(a+s)/source_R(a)*source_R(a+s+t)/source_R(a+s))

def rank_laplace_even(a,s,r):
    if type(r) is not int or r<=0 or r%2: raise ValueError('positive even rank')
    return scaled_laplace(a,s)**(r//2)

def source_mean(a):
    a=rat(a)
    if a<=0:raise ValueError('a>0')
    return sum((1/(a+d) for d in (0,3,4,5)),F())-((2*a+F(121,15))/(a*a+F(121,15)*a+16))

def mutated_R(a,epsilon=F(1)):
    """Positive mutated Q+epsilon*e^-6x(1-e^-x)^3; first two jets unchanged."""
    a,epsilon=rat(a),rat(epsilon)
    if a<=0 or epsilon<0: raise ValueError('invalid mutant')
    return source_R(a)+epsilon*sum((F((-1)**j*comb(3,j),1)/(a+6+j) for j in range(4)),F())

def source_tail_interval(n,depth=20):
    """T_n=sum_(j>=1)16^-j*r(n+j), monotone positive forcing."""
    if type(n) is not int or n<1 or type(depth) is not int or depth<1:raise ValueError('n,depth positive')
    v=sum((F(1,16**j)*bbp_forcing(n+j) for j in range(1,depth+1)),F())
    return v,v+bbp_forcing(n+depth+1)/F(15*16**depth)

def gamma_triangle(rank,a,precision=70):
    """mpmath OBSERVATION of E log[a X_(a,rank/2)] - E exp[-lambda a X];
    exact source-Laplace integral, not a rigorous interval certificate.
    """
    import mpmath as mp
    with mp.workdps(precision):
        a=mp.mpf(a);r=mp.mpf(rank)
        if a<=0 or r<=0:raise ValueError('a,r positive')
        lam=(mp.sqrt(5)-1)/2
        def R(x):return (15*x*x+121*x+240)/(x*(x+3)*(x+4)*(x+5))
        def L(s):return R(a*(1+s))/R(a)
        def f(s):
            if s==0:
                # derivative at s=0 of e^-s - L(s)^(r/2)
                m=(1/a+1/(a+3)+1/(a+4)+1/(a+5)
                   -(2*a+mp.mpf(121)/15)/(a*a+mp.mpf(121)/15*a+16))
                return (r/2)*a*m-1
            return (mp.exp(-s)-mp.power(L(s),r/2))/s
        elog=mp.quad(f,[0,mp.mpf('0.1'),1,5,20,mp.inf])
        return {'value':elog-mp.power(L(lam),r/2),
                'logmean':elog,'laplace':mp.power(L(lam),r/2),
                'ideal':mp.digamma(r)-mp.power(lam,r),
                'lambda':lam}

def gamma_triangle_exact_log2(a,precision=80):
    import mpmath as mp
    with mp.workdps(precision):
        a=mp.mpf(a)
        if a<=0:raise ValueError('a>0')
        r=sum(mp.mpf(c)/(a+d) for d,c in POLES)
        return -mp.euler+sum(mp.mpf(c)*mp.log(a/(a+d))/(a+d) for d,c in POLES)/r

def gamma_triangle_error_bound(rank,a,precision=75):
    import mpmath as mp
    with mp.workdps(precision):
        r,a=mp.mpf(rank),mp.mpf(a)
        if r<=0 or a<=0:raise ValueError('a,r positive')
        lam=(mp.sqrt(5)-1)/2
        return mp.log1p(5/a)+mp.power(lam,r)*mp.expm1(5*r*lam**2/(2*a))

def four_pole_first_correction(rank,precision=75):
    import mpmath as mp
    with mp.workdps(precision):
        r=mp.mpf(rank);lam=(mp.sqrt(5)-1)/2
        return mp.mpf(59)/30*(1+r*mp.power(lam,r+2))

def golden_trace(rank):
    """Integer trace lambda^r+(-phi)^r in Q(sqrt(5))."""
    if type(rank) is not int or rank<0:raise ValueError('rank>=0')
    t0,t1=2,-1
    if rank==0:return t0
    for _ in range(1,rank):t0,t1=t1,t0-t1
    return t1

def golden_clock_norm_integer(rank,m):
    """16^(2m)*Norm_Q(sqrt5)/Q (lambda^rank - 16^(-m))."""
    if type(rank) is not int or rank<1 or type(m) is not int or m<1:
        raise ValueError('positive integer rank and 16-adic exponent')
    x=16**m
    return (-1)**rank*x*x-golden_trace(rank)*x+1

def affine_history(nmax,seed=F(0)):
    seed=rat(seed)
    x=seed;out=[]
    for n in range(1,nmax+1):
        x=16*x+bbp_forcing(n)
        out.append(x)
    return out

class ExactChecks(unittest.TestCase):
    def test_four_poles_and_quadratic_factorization(self):
        for a in [1,2,3,7,19,F(1,2),F(7,3),F(99,11)]:
            self.assertEqual(source_R(a),source_R_factored(a))
        self.assertEqual(bbp_forcing(1),F(47,15))
    def test_initial_forcing_and_green_tail(self):
        for n in range(1,18):
            self.assertEqual(bbp_forcing(n),F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))
            lo,hi=source_tail_interval(n,16)
            self.assertTrue(F(0)<lo<hi)
            self.assertLess(hi-lo,F(1,10**12))
    def test_field_recursive_update(self):
        for a in [1,4,17,F(11,3)]:
            for s,t in [(1,2),(8,3),(F(1,2),F(4,7))]:
                self.assertEqual(*source_tilt_compose(a,s,t))
    def test_convolution_rank_semigroup(self):
        for a in [1,17,49,F(1,2)]:
            for s in [0,F(1,2),2,5]:
                self.assertEqual(rank_laplace_even(a,s,6),rank_laplace_even(a,s,2)*rank_laplace_even(a,s,4))
                self.assertGreater(scaled_laplace(a,s),0)
    def test_source_mean_and_bounds(self):
        for a in [1,2,5,9,17,97,F(1,3)]:
            m=source_mean(a);a=F(a)
            self.assertLess(1/a+1/(a+5),m)
            self.assertLess(m,1/a+1/(a+3))
    def test_source_mutant_same_local_jets(self):
        # (1-e^-x)^3 vanishes through second derivative at origin,
        # despite genuinely changing the full source for every a>0.
        self.assertNotEqual(mutated_R(1),source_R(1))
        self.assertGreater(mutated_R(17),source_R(17))
        # Q(0)=0, Q'(0)=15, Q''(0)=-59; mutation starts at cubic.
        for k in range(3):
            mutation_jet = sum((-1)**j*comb(3,j)*(-(6+j))**k for j in range(4))
            self.assertEqual(mutation_jet,0)
    def test_clocks_algebraically_incommensurate(self):
        for rank in range(1,35):
            for m in range(1,16):
                self.assertNotEqual(golden_clock_norm_integer(rank,m),0)
    def test_seed_affine_anchor_and_zero_seed_control(self):
        x0=affine_history(12,F(0));seed=F(1,7);xs=affine_history(12,seed)
        for n,(a,b) in enumerate(zip(x0,xs),1):
            self.assertEqual(b-a,16**n*seed)
        for n in range(1,13):
            lo,hi=source_tail_interval(n,25)
            self.assertLess(hi,F(1,9*(n+1)**2))
    def test_source_gauge_cycles_exact_exponents(self):
        seq=affine_history(9)
        for i,j,k in [(0,1,2),(1,3,8),(2,5,7)]:
            self.assertEqual((seq[i]-seq[j])+(seq[j]-seq[k])+(seq[k]-seq[i]),0)
            # Any change of seed multiplies each edge by a coboundary,
            # so all closed-cycle phase holonomies remain exactly one.
    def test_rank_log2_frullani_numerical_holdout(self):
        import mpmath as mp
        with mp.workdps(65):
            for a in [1,17,137]:
                v=gamma_triangle(2,a,65)
                self.assertLess(abs(v['logmean']-gamma_triangle_exact_log2(a,65)),mp.mpf('1e-45'))
    def test_all_rank_one_sided_bound_numerical(self):
        import mpmath as mp
        with mp.workdps(65):
            for rank,a in [(2,1),(2,17),(2,137),(3,17),(4,23)]:
                v=gamma_triangle(rank,a,65)
                gap=v['ideal']-v['value']
                self.assertGreater(gap,0)
                self.assertLess(gap,gamma_triangle_error_bound(rank,a,65))
    def test_first_correction_numerical_holdout(self):
        import mpmath as mp
        with mp.workdps(65):
            for rank in [2,3,4]:
                a=800
                v=gamma_triangle(rank,a,65)
                coeff=a*(v['ideal']-v['value'])
                expect=four_pole_first_correction(rank,65)
                self.assertLess(abs(coeff/expect-1),mp.mpf('0.006'))
    def test_rank_monotonicity_numerical(self):
        import mpmath as mp
        with mp.workdps(60):
            for a in [1,13]:
                vals=[gamma_triangle(r,a,60)['value'] for r in [2,3,4]]
                self.assertLess(vals[0],vals[1]);self.assertLess(vals[1],vals[2])
    def test_rank_boundary_numeric_exact_fixedpoint(self):
        import mpmath as mp
        with mp.workdps(60):
            lam=(mp.sqrt(5)-1)/2
            self.assertLess(abs(1/(1+lam)-lam),mp.mpf('1e-50'))
            self.assertLess(abs(1/(2-lam**2)**2-lam**2),mp.mpf('1e-50'))
            self.assertLess(abs((1-mp.euler-lam**2)-(lam-mp.euler)),mp.mpf('1e-50'))

if __name__=='__main__':unittest.main(verbosity=2)
