"""Source-locked directional information and q=6 primitive/cototient field.

The four rational BBP poles, retarded U_0=0 and all carried phases stay fixed.
All assertions here are exact-rational unless explicitly labelled numerical.
Research only: no physical heat, selected Weyl decay or pi normality claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial, gcd
import unittest

POLES = ((0, 4), (3, -2), (4, -1), (5, -1))
CELLS = {"00": (0, 2, 4), "01": (3,), "10": (1,), "11": (5,)}


def pos(q):
    q = F(q)
    if q <= 0: raise ValueError("positive source parameter required")
    return q


def R(a):
    a=pos(a)
    return sum((F(c)/(a+d) for d,c in POLES),F(0))


def forcing(n):
    if type(n) is not int or n < 1: raise ValueError("original integer source index")
    return R(8*n-7)


def mean(a):
    a=pos(a)
    pol=15*a*a+121*a+240
    return sum((1/(a+d) for d,_ in POLES),F(0)) - (30*a+121)/pol


def variance(a):
    a=pos(a)
    pol=15*a*a+121*a+240
    return sum((1/(a+d)**2 for d,_ in POLES),F(0)) + F(30)/pol - ((30*a+121)/pol)**2


def third_cumulant(a):
    a=pos(a)
    pol=15*a*a+121*a+240
    slope=(30*a+121)/pol
    return 2*sum((1/(a+d)**3 for d,_ in POLES),F(0)) + F(90)*slope/pol -2*slope**3


def jeffreys(a,s):
    a,s=pos(a),pos(s)
    return s*(mean(a)-mean(a+s))


def jeffreys_bounds(a,s):
    a,s=pos(a),pos(s)
    low=s*s*(1/(a*(a+s))+1/((a+5)*(a+s+5)))
    high=s*s*(1/(a*(a+s))+1/((a+3)*(a+s+3)))
    return low,high


def arrow_bounds(a,s):
    """All-rational bounds for reverse_KL-forward_KL (positive)."""
    a,s=pos(a),pos(s)
    low=s**3/F(3)*(1/(a+s)**3+1/(a+s+5)**3)
    high=s**3/F(3)*(1/a**3+1/(a+3)**3)
    return low,high


def telescoping_jeffreys(horizon):
    if type(horizon) is not int or horizon<2: raise ValueError("N>=2")
    direct=sum((jeffreys(8*n-7,8) for n in range(1,horizon)),F(0))
    closed=F(8)*(mean(1)-mean(8*horizon-7))
    assert direct==closed
    return direct, closed


def endpoint_residue(q,r):
    """Exact mass P(J=r mod q), w_j=(j+1)/2^(j+2)."""
    if type(q) is not int or type(r) is not int or q<1 or not 0<=r<q:
        raise ValueError("valid residue")
    t=F(1,2**q); p=F(1,2**(r+2))
    return p*(F(r+1)/(1-t)+F(q)*t/(1-t)**2)


def endpoint_residue_first_response(q,r):
    """Exact sum_(j=r mod q) (2-j)w_j, with X=-log endpoint."""
    t=F(1,2**q); p=F(1,2**(r+2))
    base=F(r+1)/(1-t)+F(q)*t/(1-t)**2
    derivative=F(r)*base+q*t*(F(r+1)/(1-t)**2+q*(1+t)/(1-t)**3)
    return p*(2*base-derivative)


def cell_endpoint():
    return {k:sum((endpoint_residue(6,r) for r in residues),F(0))
            for k,residues in CELLS.items()}


def cell_response():
    return {k:sum((endpoint_residue_first_response(6,r) for r in residues),F(0))
            for k,residues in CELLS.items()}


def cell_information_coefficient():
    p,c=cell_endpoint(),cell_response()
    return sum((c[k]*c[k]/p[k] for k in CELLS),F(0))


def conditional_grade(t,j):
    """Exact original two-geometric Oily packet given x=e^{-X}=t."""
    t=F(t)
    if not 0<=t<=1 or type(j) is not int or j<0: raise ValueError("source grade")
    u=t-t*t/2;v=t*t/2
    return (1-u)*(1-v)*sum((u**k*v**(j-k) for k in range(j+1)),F(0))


def grade_residue(t,q,r):
    t=F(t)
    if not 0<=t<=1 or type(q) is not int or q<1 or not 0<=r<q:
        raise ValueError("invalid source/grade residue")
    if t==1:return endpoint_residue(q,r)
    if t==0:return F(int(r==0))
    u=t-t*t/2;v=t*t/2
    return (1-u)*(1-v)/(u-v)*(u**(r+1)/(1-u**q)-v**(r+1)/(1-v**q))


def cell_given_source(t):
    return {k:sum((grade_residue(t,6,r) for r in residues),F(0))
            for k,residues in CELLS.items()}


def packet_drift_bound(a,s):
    """Global L1 bound for full grade law or any coarse q=6 projection."""
    a,s=pos(a),pos(s)
    return F(10)*s/(a*(a+s))


def preimage_carries(r,y):
    """The 16 exact inverse carry branches for y={16x+r} (0<r<1)."""
    r,y=F(r),F(y)
    if not 0<r<1 or not 0<=y<1: raise ValueError("r in (0,1), output y in circle")
    return tuple((c,(y+c-r)/16) for c in range(17) if 0<=(y+c-r)/16<1)


def circle_forward(x,r):
    return (16*F(x)+F(r))%1


def original_prefix(n,seed=F(0)):
    if type(n) is not int or n<0: raise ValueError("nonnegative horizon")
    u=F(seed); out=[u]
    for k in range(1,n+1):
        u=(16*u+forcing(k))%1
        out.append(u)
    return out



def exceptional_zero_run(n):
    """Guaranteed zero-carry run AFTER a literal carry 16 at time n>=2.

    Returns floor(log_16(n*n)) exactly, without floating logarithms.
    """
    if type(n) is not int or n < 2: raise ValueError("n>=2")
    power=1; count=0
    while power*16 <= n*n:
        power*=16;count+=1
    return count


def exceptional_count_upper(N,M):
    """Upper bound on number of carry-16 events through time N, all seeds.

    Every event from M onward forces >= L_M following zeros.
    """
    if not (type(N) is type(M) is int and 4<=M<=N):
        raise ValueError("4<=M<=N integers")
    L=exceptional_zero_run(M)
    return M + (N-M)//(L+1)


def literal_carries(history):
    """Fraction-exact literal carries; history[0] is the unwrapped seed."""
    return tuple((16*(history[n-1]%1)+forcing(n))//1 for n in range(1,len(history)))


def engineered_carry16_seed(n):
    """Countercontrol: prepare the unique rational seed making κ_n=16.

    Not an authentic prepared origin. Constructed solely to test the theorem
    for *every* seed, including adversarial preparations.
    """
    if type(n) is not int or n<3:raise ValueError("n>=3")
    target=F(1)-forcing(n)/32
    original=original_prefix(n-1)[-1]
    return (target-original)/16**(n-1)


class DirectionalTests(unittest.TestCase):
    def test_source_passport(self):
        self.assertEqual(R(1),F(47,15))
        self.assertEqual(forcing(1),F(47,15))
        for n in range(2,38): self.assertTrue(F(0)<forcing(n)<1)

    def test_cumulants_positive_and_strict_bounds(self):
        for a in (F(1),F(3,2),F(5),F(17),F(73),F(200)):
            self.assertGreater(mean(a),0)
            v=variance(a);k=third_cumulant(a)
            self.assertLess(F(1)/a**2+F(1)/(a+5)**2,v)
            self.assertLess(v,F(1)/a**2+F(1)/(a+3)**2)
            self.assertLess(2/a**3+2/(a+5)**3,k)
            self.assertLess(k,2/a**3+2/(a+3)**3)

    def test_exact_jeffreys_bounds(self):
        for a in (1,2,9,17,65,257):
            for s in (F(1,4),F(3),F(8)):
                value=jeffreys(a,s);lo,hi=jeffreys_bounds(a,s)
                self.assertLess(lo,value)
                self.assertLess(value,hi)

    def test_exact_telescoping_total(self):
        self.assertEqual(mean(1),F(6853,5640))
        self.assertEqual(8*mean(1),F(6853,705))
        for N in (2,3,4,8,12,40):
            value,closed=telescoping_jeffreys(N)
            self.assertEqual(value,closed)
            self.assertLess(value,F(6853,705))

    def test_arrow_positive_bounds(self):
        for a in (1,3,17,45,77,161):
            lo,hi=arrow_bounds(a,8)
            self.assertTrue(0<lo<hi)

    def test_q6_four_cells_endpoint(self):
        self.assertEqual(cell_endpoint(),{"00":F(5,9),"01":F(172,1323),
                                          "10":F(352,1323),"11":F(64,1323)})
        self.assertEqual(sum(cell_endpoint().values()),1)

    def test_q6_exact_first_responses(self):
        self.assertEqual(cell_response(),{"00":F(4,27),"01":F(-4468,27783),
                                          "10":F(4640,27783),"11":F(-4288,27783)})
        self.assertEqual(sum(cell_response().values()),0)
        self.assertEqual(cell_information_coefficient(),F(871588,1042965))

    def test_oily_two_geometric_conditional(self):
        for t in (F(0),F(1,8),F(1,3),F(1,2),F(4,5),F(1)):
            p=cell_given_source(t)
            self.assertTrue(all(x>=0 for x in p.values()))
            self.assertEqual(sum(p.values()),1)
            for r in range(6):
                finite=sum((conditional_grade(t,r+6*k) for k in range(18)),F(0))
                self.assertLessEqual(finite,grade_residue(t,6,r))

    def test_near_endpoint_derivatives(self):
        t=F(9999,10000)
        p0=cell_endpoint();c=cell_response();pn=cell_given_source(t)
        for key in CELLS:
            self.assertLess(abs((pn[key]-p0[key])*10000-c[key]),F(1,50))

    def test_packet_drift_order(self):
        for n in (3,8,32,100):
            a=8*n-7
            self.assertLessEqual(packet_drift_bound(a,8),F(80,a*(a+8)))
            self.assertLess(packet_drift_bound(a,8),F(10,a))

    def test_branch_inverses_all_sixteen(self):
        for n in (2,3,8,33):
            r=forcing(n)
            for y in (F(0),r/F(2),r,F(1,3),F(7,8),F(999,1000)):
                cxs=preimage_carries(r,y)
                self.assertEqual(len(cxs),16)
                self.assertTrue(all(circle_forward(x,r)==y for c,x in cxs))
                self.assertEqual(len({c for c,x in cxs}),16)

    def test_boundary_carries_based_on_output(self):
        r=forcing(2)
        csmall={c for c,x in preimage_carries(r,r/2)}
        cbig={c for c,x in preimage_carries(r,(r+1)/2)}
        self.assertEqual(csmall,set(range(1,17)))
        self.assertEqual(cbig,set(range(16)))

    def test_phase_quotient_integer_seed(self):
        a=original_prefix(16)
        b=original_prefix(16,F(-1))
        c=original_prefix(16,F(-16))
        self.assertNotEqual(a[0],b[0])
        self.assertNotEqual(a[0],c[0])
        self.assertEqual(a[1:],b[1:])
        self.assertEqual(a[1:],c[1:])


    def test_exceptional_forcing_global_upper(self):
        for n in range(2,150):
            a=8*n-7
            original=forcing(n)
            bound=F(15,16*n*n)
            self.assertGreater(original,0)
            self.assertLess(original,bound)
            self.assertLessEqual(original,F(15,a*(a+3)))

    def test_engineered_carry16_forces_logarithmic_zero_run(self):
        for n in (4,6,8,15,17,32,49,81,128):
            length=exceptional_zero_run(n)
            seed=engineered_carry16_seed(n)
            hist=original_prefix(n+length+1,seed)
            carries=literal_carries(hist)
            self.assertEqual(carries[n-1],16)
            self.assertEqual(carries[n:n+length],(0,)*length)

    def test_count_bound_invariant_for_original_and_adversarial_seed(self):
        for seed in (F(0),F(1,7),F(-1,3),engineered_carry16_seed(18)):
            c=literal_carries(original_prefix(90,seed))
            for M in (4,7,12,20):
                for N in (M,35,60,90):
                    if N<M:continue
                    self.assertLessEqual(sum(1 for v in c[:N] if v==16), exceptional_count_upper(N,M))

    def test_event_spacing_for_all_seed_carry16_occurrences(self):
        for n in (9,18,40,65):
            seed=engineered_carry16_seed(n)
            c=literal_carries(original_prefix(n+exceptional_zero_run(n)+15,seed))
            hit=[i+1 for i,v in enumerate(c) if v==16]
            for i,j in zip(hit,hit[1:]):
                self.assertGreaterEqual(j-i,exceptional_zero_run(i)+1)

    def test_stationary_oily_weight_sum_and_carrier_gradient(self):
        self.assertEqual(sum((F(j+1,2**(j+2)) for j in range(24))),F(1)-F(26,2**25))
        for N in (16,64,256,1024):
            M=max(4,int(N**0.5))
            bound=F(M,N)+F(1,exceptional_zero_run(M)+1)+F(10,N)*sum((F(1,8*n-7) for n in range(M,N+1)),F())
            self.assertGreater(bound,0)
            self.assertLess(bound,2)

    def test_original_zero_seed_is_not_constant(self):
        a=original_prefix(12)
        self.assertNotEqual(a[1],a[2])
        self.assertNotEqual(a[0],a[1])

if __name__ == '__main__':unittest.main(verbosity=2)
