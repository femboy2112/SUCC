"""Exact finite C4 noise-coupling and zero-seeded BBP phase-step controls.

C4 has exact Haar marginals only when the tested source Z is in C4.
The paper theorem extends to every Z on the circle with continuous Haar masks.
No randomized BBP digits, physical probe, entropy-of-pi, or R0 proof is asserted.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import math
import unittest

ROOTS = ((Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1)))
ONE = ROOTS[0]
ZERO = (Q(0), Q(0))

def conj(a): return (a[0], -a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(a,p): return (a[0]*p,a[1]*p)
def sub(a,b): return (a[0]-b[0],a[1]-b[1])

def joint_c4(z,p):
    """Two readouts: A=R, B=z*R with probability p else z*R'."""
    p=Q(p)
    if not 0 <= p <= 1: raise ValueError('p in [0,1]')
    if z not in ROOTS: raise ValueError('C4 exact marginal needs z in C4')
    law=defaultdict(lambda:Q(0))
    for r in ROOTS:
        law[(r,mul(z,r))]+=p/4
        for rp in ROOTS: law[(r,mul(z,rp))]+=(1-p)/16
    return dict(law)

def marginals(law):
    a=defaultdict(lambda:Q(0));b=defaultdict(lambda:Q(0))
    for (y0,y1),p in law.items():
        a[y0]+=p;b[y1]+=p
    return dict(a),dict(b)

def correlation(law):
    out=ZERO
    for (y0,y1),p in law.items():
        out=add(out,scale(mul(conj(y0),y1),p))
    return out

def moment(law,channel):
    out=ZERO
    for y,p in law.items():
        out=add(out,scale(y[channel],p))
    return out

def third_order_law(z):
    """A=R, B=S, C=z*R*S. All 1/2-channel laws are blind to z."""
    if z not in ROOTS: raise ValueError('finite exact test scope')
    law={}
    for r,s in product(ROOTS,repeat=2):
        law[(r,s,mul(z,mul(r,s)))]=Q(1,16)
    return law

def pair_marginal(law,i,j):
    out=defaultdict(lambda:Q(0))
    for row,p in law.items():out[(row[i],row[j])]+=p
    return dict(out)

def triple_syndrome(law):
    res=ZERO
    for (a,b,c),p in law.items():
        res=add(res,scale(mul(mul(conj(a),conj(b)),c),p))
    return res

def forcing(n):
    if n<1:raise ValueError('n>=1')
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)

def circle_dist(y):
    x=Q(y)%1
    return min(x,1-x)

def original_source(end=513):
    u=Q(0);states={}
    for n in range(1,end+1):
        u=16*u+forcing(n)
        states[n]=u
    return states

def speed_cert(B,states,enhanced=False):
    total=Q(0)
    for n in range(B,2*B):
        if enhanced:
            # T_n>T_(n+1)>0 from strictly decreasing original forcing.
            d=max(Q(0),circle_dist(states[n+1]-states[n])-forcing(n+1)/15)
        else:
            d=max(Q(0),circle_dist(15*states[n])-forcing(n+1))
        total+=d*d
    return Q(16,B)*total

class BoundaryOrderLiftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.source=original_source(513)

    def test_first_order_and_full_marginals_null_all_couplings(self):
        for z,p in product(ROOTS,(Q(0),Q(1,4),Q(1,2),Q(1))):
            law=joint_c4(z,p)
            self.assertEqual(sum(law.values()),1)
            aa,bb=marginals(law)
            self.assertEqual(aa,{q:Q(1,4) for q in ROOTS})
            self.assertEqual(bb,{q:Q(1,4) for q in ROOTS})
            self.assertEqual(moment(law,0),ZERO)
            self.assertEqual(moment(law,1),ZERO)
            self.assertEqual(sum((v for (a,b),v in law.items() if a==ONE),Q(0)),Q(1,4))

    def test_second_order_exact_phase_and_probe_response(self):
        for z,p in product(ROOTS,(Q(0),Q(1,4),Q(3,5),Q(1))):
            self.assertEqual(correlation(joint_c4(z,p)),scale(z,p))
        for z in ROOTS:
            a,b=Q(1,4),Q(3,5)
            difference=sub(correlation(joint_c4(z,b)),correlation(joint_c4(z,a)))
            self.assertEqual(difference,scale(z,b-a))

    def test_zero_coupling_identical_independent_law_all_sources(self):
        baseline=joint_c4(ROOTS[0],Q(0))
        for z in ROOTS:
            self.assertEqual(joint_c4(z,Q(0)),baseline)
            self.assertEqual(correlation(joint_c4(z,Q(0))),ZERO)
        self.assertEqual(len(baseline),16)

    def test_full_coupling_recovers_hidden_phase_per_joint_outcome(self):
        for z in ROOTS:
            law=joint_c4(z,Q(1))
            for (a,b),prob in law.items():
                if prob:self.assertEqual(mul(conj(a),b),z)
        with self.assertRaises(ValueError):joint_c4(ROOTS[0],Q(-1))
        with self.assertRaises(ValueError):joint_c4(ROOTS[0],Q(2))

    def test_one_channel_variance_is_null_control_not_source(self):
        # |A|²=|B|²=1 in every output, including truly independent noise.
        for z,p in product(ROOTS,(Q(0),Q(1,2),Q(1))):
            law=joint_c4(z,p)
            self.assertEqual(sum((prob*(a[0]**2+a[1]**2) for (a,b),prob in law.items()),Q(0)),1)
            self.assertEqual(sum((prob*(b[0]**2+b[1]**2) for (a,b),prob in law.items()),Q(0)),1)

    def test_third_order_hides_from_every_pair(self):
        ref=third_order_law(ROOTS[0])
        for z in ROOTS:
            law=third_order_law(z)
            self.assertEqual(triple_syndrome(law),z)
            for i,j in ((0,1),(0,2),(1,2)):
                self.assertEqual(pair_marginal(law,i,j),pair_marginal(ref,i,j))
                self.assertEqual(pair_marginal(law,i,j),{pair:Q(1,16) for pair in product(ROOTS,repeat=2)})

    def test_exact_source_dynamics_are_not_randomized(self):
        for n in (1,2,3,32,63,64,127,255,511):
            u,up=self.source[n],self.source[n+1]
            self.assertEqual(up-u,15*u+forcing(n+1))
            self.assertEqual((up-u)%1,(15*u+forcing(n+1))%1)
            # Co-moving gauge g(n)=2*n² only changes integer winding.
            self.assertEqual((up-u+2*(n+1)**2-2*n**2)%1,(up-u)%1)

    def test_strict_monotone_forcing_finite_replay(self):
        for n in (1,2,8,32,64,255,512):
            self.assertGreater(forcing(n),forcing(n+1))
            self.assertGreater(forcing(n+1)/15,0)

    def test_enhanced_second_order_step_certificate(self):
        for B in (16,32,64,128,256):
            before=speed_cert(B,self.source,False)
            after=speed_cert(B,self.source,True)
            self.assertGreater(after,before, f'B={B}: new cross-probe certificate weaker')
            self.assertGreater(after,Q(1))
            if B>=32:self.assertGreater(after,Q(6,5))

    def test_stronger_bound_is_finite_not_an_infinite_claim(self):
        # Every tested late-ish shell passes the same 1/10 finite lower R0 margin.
        for B in (32,64,128,256):
            lb=speed_cert(B,self.source,True)
            self.assertGreater(lb/Q(8)-Q(1,B),Q(1,10))

    def test_information_gain_is_source_prior_relative(self):
        # In the finite C4 source, a uniform prior has 2 bits and at p=1
        # every joint outcome gives Z exactly; p=0 yields no information.
        for p in (Q(0),Q(1)):
            joint={(z,a,b):prob/Q(4) for z in ROOTS
                   for (a,b),prob in joint_c4(z,p).items()}
            triples={(a,b):Q(0) for a,b in product(ROOTS,repeat=2)}
            for (z,a,b),pr in joint.items():triples[(a,b)]+=pr
            info=0.0
            for (z,a,b),pr in joint.items():
                if pr:
                    info+=float(pr)*math.log2(float(pr/(Q(1,4)*triples[(a,b)])))
            self.assertAlmostEqual(info,2.0 if p==1 else 0.0,places=13)

if __name__=='__main__':unittest.main()
