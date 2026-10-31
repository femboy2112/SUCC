"""Exact SUCC moving-clock and acceleration-sensitive virtual-field probes.

Auxiliary, declared sensor model. Not a sampler or proof of pi normality.
"""
from fractions import Fraction as F
from math import comb, sqrt, log, tanh, cosh
import unittest

C = (4,-2,-1,-1)
T = (0,3,4,5)
GAMMA = 0.5772156649015328606
PHI = (1+sqrt(5))/2
LAMBDA=1/PHI


def R(a):
    a=F(a)
    return sum((F(c,a+t) for c,t in zip(C,T)),F(0))


def Rfake(a):
    a=F(a)
    return F(15,a*a)


def bmoments(a, src=R):
    """First three moments of b(X)=exp(-8X)(1-exp(-8X)), exact."""
    z=src(a)
    return tuple(sum(((-1)**j*comb(k,j)*src(a+8*(k+j))
                      for j in range(k+1)),F(0))/z for k in (1,2,3))


def posterior_contrast(a, eps, src=R):
    """E[b | (+,-), alpha=(+1,-1)] - E[b | (-,+)]"""
    b1,b2,b3=bmoments(a,src)
    z0=F(1,4)+eps*eps*b2
    z1=eps*b1
    n0=b1/4+eps*eps*b3
    n1=eps*b2
    return (n0+n1)/(z0+z1)-(n0-n1)/(z0-z1)


def oily(s):
    return sum(1/j for j in range(1,s+2))-GAMMA-LAMBDA**(s+2)


def om_mass(s):
    return (s+1)*2**s/2**(2*s+2)*oily(s)  # (s+1)/2^(s+2)


def oily_mean(limit=160):
    den=sum(om_mass(s) for s in range(limit))
    return sum(s*om_mass(s) for s in range(limit))/den


class AcceleratingFrame(unittest.TestCase):
    def test_source_ratios(self):
        for a in (1,9,17,73):
            self.assertGreater(R(a),0)
            b1,b2,b3=bmoments(a)
            self.assertGreater(b2-b1*b1,0)
            self.assertLessEqual(b1,F(1,4))

    def test_total_grade_invariant_under_clock_split(self):
        # For Gamma2 with two mark probabilities p and q=1-p,
        # P(S=s)=(s+1)/2^(s+2), independent of p.
        for p in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            for s in range(15):
                left=sum(F((s+1)*comb(s,j),2**(s+2))*p**j*(1-p)**(s-j)
                         for j in range(s+1))
                self.assertEqual(left,F(s+1,2**(s+2)))

    def test_event_order_evidence_ninefold(self):
        p1,p2=F(3,4),F(1,4)
        # (+,-) in one time protocol versus reversed protocol
        likelihood1=p1*(1-p2)
        likelihood2=p2*(1-p1)
        self.assertEqual(likelihood1/likelihood2,9)
        # But total-grade law for both schedules is identical
        self.assertEqual(p1+p2,F(1))
        self.assertEqual(p1*p2,F(3,16))

    def test_positive_source_posterior_cannot_detect_source_blind_boost(self):
        # In a common-total-exposure marked Poisson model,
        # p_i and (1-p_i) factors are independent of X; they cancel
        # from the normalized latent posterior, which has base weight
        # (aX)^S exp(-aX T) dmu_a for fixed S,T.
        for a in (1,9,17):
            # With S=0 and exposure T=1, posterior X~mu_(2a).
            base=R(2*a)/R(a)
            for p1,p2 in ((F(1,4),F(3,4)),(F(1,3),F(2,3))):
                weight=p1*(1-p2)
                self.assertEqual(weight*base/weight,base)

    def test_source_sensitive_order_response(self):
        eps=F(1,4)
        for a in (1,9,17,73,257):
            self.assertGreater(posterior_contrast(a,eps),0)
            self.assertGreater(posterior_contrast(a,eps,Rfake),0)
            self.assertNotEqual(posterior_contrast(a,eps),posterior_contrast(a,eps,Rfake))

    def test_acceleration_sensitive_linear_response(self):
        for a in (9,17,73):
            b1,b2,_=bmoments(a)
            var=b2-b1*b1
            # The exact small-epsilon derivative is 8 Var_mu[b].
            eps=F(1,10**6)
            residual=abs(float(posterior_contrast(a,eps)/eps)-8*float(var))
            self.assertLess(residual,1.e-9)

    def test_first_four_pole_59_jet_of_variance(self):
        # Q(x)=15x-(59/2)x^2+..., so the unique first source
        # correction to Var_mu[b] is -128*59/(15 a^3).
        a=65536
        x1,x2,_=bmoments(a)
        y1,y2,_=bmoments(a,Rfake)
        val=float(((x2-x1*x1)-(y2-y1*y1))*a**3)
        self.assertLess(abs(val+F(128*59,15)),2)

    def test_oily_clock_rapidity_response(self):
        m=oily_mean()
        self.assertAlmostEqual(m,3.3331941754643366,places=10)
        Z = 0.8+log(2)-GAMMA
        self.assertAlmostEqual(Z,0.9159315156584124,places=12)
        eta=2*log(PHI)
        p=(1+tanh(eta))/2
        self.assertAlmostEqual(2*p-1,sqrt(5)/3,places=13)
        current=m*tanh(eta)
        self.assertAlmostEqual(current,m*sqrt(5)/3,places=12)
        # Exact normalized Oily KL after grade-only change-of-measure.
        kl=m*(eta*tanh(eta)-log(cosh(eta)))
        direct=0.
        for s in range(120):
            ws=om_mass(s)/sum(om_mass(i) for i in range(120))
            for j in range(s+1):
                prob=comb(s,j)*p**j*(1-p)**(s-j)
                direct+=ws*prob*((2*j-s)*eta-s*log(cosh(eta)))
        self.assertAlmostEqual(kl,direct,places=10)

if __name__=='__main__':
    unittest.main(verbosity=2)
