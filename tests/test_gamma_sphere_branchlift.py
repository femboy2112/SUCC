"""Post-prereg SUCC sphere double-cover, Blaschke and arithmetic controls."""
import unittest
import sympy as s
import mpmath as mp

I=s.I
z,t=s.symbols('z t')
alpha=1+2*I
beta=1-2*I
B=s.cancel((alpha*z+1)/(z+beta))
Bi=lambda v: s.cancel((1-beta*v)/(v-alpha))
J=s.factor(Bi(-B))
z0=s.simplify(-1/alpha)
c=s.simplify(alpha/beta)
u=(1+I)/2
ub=(1-I)/2
eta=s.simplify(-B.subs(z,0)**2)

class SourceBranchLiftTests(unittest.TestCase):
    def setUp(self): self._dps=mp.mp.dps
    def tearDown(self): mp.mp.dps=self._dps
    def zero(self,v): self.assertEqual(s.simplify(s.cancel(v)),0)

    def test_01_cayley_to_blaschke(self):
        tangent=-I*(z-1)/(z+1)
        q=lambda x:(x-1-I)/(x-1+I)
        self.zero(q(tangent)-B)
        self.zero(B-c*(z-z0)/(1-s.conjugate(z0)*z))
        self.zero(z0*s.conjugate(z0)-s.Rational(1,5))
        self.zero(c*s.conjugate(c)-1)

    def test_02_golden_ratio_sharp_distortion(self):
        radius=s.sqrt(s.Rational(1,5))
        phi=(1+s.sqrt(5))/2
        self.zero((1+radius)/(1-radius)-phi**2)
        self.zero((1-radius)/(1+radius)-phi**(-2))
        # The sharp bounds follow by minimizing/maximizing |z-z0| on |z|=1.
        self.zero((1-radius**2)/(1-radius)**2-phi**2)
        self.zero((1-radius**2)/(1+radius)**2-phi**(-2))

    def test_03_sphere_double_cover_and_deck(self):
        q=lambda x:(x-1-I)/(x-1+I)
        W=lambda x: -I*(2-x*x)/(x-1+I)**2
        self.zero((W(-I*(z-1)/(z+1))-u)/ub + B**2)
        self.zero(B.subs(z,J)+B)
        self.zero(J.subs(z,J)-z)
        self.zero(J.subs(z,-1)-I)
        self.zero(J.subs(z,I)+1)
        self.zero(J.subs(z,0)-(-1+2*I)/3)

    def test_04_nonhaar_expected_sphere_measure(self):
        self.zero(eta-(3-4*I)/25)
        self.zero(eta*s.conjugate(eta)-s.Rational(1,25))
        # Analytic mean-value property: for Haar z on unit circle,
        # E[(-B(z)^2)^h] = (-B(0)^2)^h = eta^h, not zero.
        mp.mp.dps=55
        for n in (53,97):
            zs=[mp.exp(2j*mp.pi*k/n) for k in range(n)]
            bs=[((1+2j)*zz+1)/(zz+1-2j) for zz in zs]
            target=complex(s.N(eta,45))
            for h in (1,2,3):
                avg=sum(((-b*b)**h for b in bs))/n
                self.assertLess(abs(avg-mp.mpc(target)**h),mp.mpf('1e-10' if n==53 else '1e-16'))

    def test_05_branch_flip_same_sphere_observation_not_same_source(self):
        # The free involution J changes source circle law but W is unchanged.
        mp.mp.dps=55
        for n in (53,97):
            roots=[mp.exp(2j*mp.pi*k/n) for k in range(n)]
            Bs=[((1+2j)*v+1)/(v+1-2j) for v in roots]
            flipped=[(1-(1-2j)*(-b))/((-b)-(1+2j)) for b in Bs]
            for b,bflip in zip(Bs,flipped):
                bnew=((1+2j)*bflip+1)/(bflip+1-2j)
                self.assertLess(abs(bnew+b),mp.mpf('1e-48'))
            self.assertLess(abs(sum(roots)/n),mp.mpf('1e-48'))
            self.assertGreater(abs(sum(flipped)/n),mp.mpf('0.70'))
        # J(root) need not be a root of unity: no SUCC admissibility claim.
        self.zero(J.subs(z,1)-(-3+4*I)/5)

if __name__ == '__main__': unittest.main()
