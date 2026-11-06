"""Finite, independent quadrature controls for the chosen four-sheet Gamma clock.

This is NOT the Hilbert-Pólya zeta operator, a completed Weil form, or
an empirical BBP selected trajectory.
"""
import cmath
import math
import unittest
import numpy as np
import mpmath as mp


L = math.log(16)
G = (1, 3, 5, 7)


def char(a, kind):
    if kind == '1': return 1
    m4 = 1 if a % 4 == 1 else -1
    c8 = 1 if a % 8 in (1, 7) else -1
    return {'-4': m4, '8': c8, '-8': m4*c8}[kind]


def density(v):
    """Gamma log16 periodization; negative tail truncated below 1e-17."""
    vv = v % L
    return sum(math.exp(s-math.exp(s)) for j in range(-15,4)
               for s in [vv+j*L] if s < 700)


class TestV4GammaClock(unittest.TestCase):
    def test_four_character_orthogonality(self):
        names = ('1', '-4', '8', '-8')
        for aa in G:
            for bb in G:
                self.assertEqual(sum(char(aa,n)*char(bb,n) for n in names),
                                 4 if aa == bb else 0)
        for a in G:
            for b in G:
                for name in names:
                    self.assertEqual(char((a*b)%8,name),char(a,name)*char(b,name))

    def test_prime_character_transport_eigenvalue(self):
        for p in (3, 5, 7, 11, 13):
            for name in ('1','-4','8','-8'):
                for h in (-3,-1,0,1,3):
                    v=0.17
                    a=3
                    def phi(x,b): return cmath.exp(2j*math.pi*h*x/L)*char(b,name)
                    value=phi(v+math.log(p),(a*p)%8)
                    lam=char(p%8,name)*cmath.exp(2j*math.pi*h*math.log(p)/L)
                    self.assertLess(abs(value-lam*phi(v,a)),1e-13)

    def test_gamma_density_normalized_and_nonhaar(self):
        x,w=np.polynomial.legendre.leggauss(200)
        vs=L*(x+1)/2
        ws=w*L/2
        vals=np.array([density(v) for v in vs])
        self.assertAlmostEqual(float(np.dot(ws,vals)),1,places=13)
        for h in (1,2,3):
            obs=complex(np.dot(ws,vals*np.exp(-2j*math.pi*h*vs/L)))
            mp.mp.dps=40
            exact=complex(mp.gamma(1-2j*mp.pi*h/mp.log(16)))
            self.assertLess(abs(obs-exact),2e-13)
            self.assertGreater(abs(obs),1e-8)

    def test_gamma_jacobian_is_required_for_unitarity(self):
        # A Fourier eigencharacter divided by sqrt(density) belongs to
        # Gamma-weighted L2 and is an EXACT eigenvector under U^Gamma_p.
        for p in (3,7,11):
            a=3
            for v in (0.13,0.47,1.21,2.5):
                for h in (0,1,3):
                    chi=char(p%8,'-4')
                    def f(x,b):
                        return cmath.exp(2j*math.pi*h*x/L)*char(b,'-4')/math.sqrt(density(x))
                    shift=math.log(p)
                    transported=math.sqrt(density(v+shift)/density(v))*f(v+shift,(p*a)%8)
                    lam=chi*cmath.exp(2j*math.pi*h*shift/L)
                    self.assertLess(abs(transported-lam*f(v,a)),2e-13)
                    # Without Jacobian, a shifted Gamma-normalized state
                    # fails the same eigen-relation at some points.
            bare = abs(f(0.13+math.log(p),(p*a)%8)-lam*f(0.13,a))
            self.assertGreater(bare,1e-6)

    def test_two_primary_finite_vs_odd_dense_levels(self):
        w2=math.log(2)/math.sqrt(2)
        spec2={round(-2*w2*math.cos(math.pi*h/2),10) for h in range(20)}
        self.assertEqual(spec2,{-round(2*w2,10),0.,round(2*w2,10)})
        for p in (3,5,7):
            wp=math.log(p)/math.sqrt(p)
            alpha=math.log(p)/L
            values=np.array([-2*wp*math.cos(2*math.pi*h*alpha)
                             for h in range(1,10001)])
            self.assertLess(abs(min(values)+2*wp),1e-6)
            self.assertLess(abs(max(values)-2*wp),1e-6)
            self.assertLess(min(abs(values)),2e-3)


if __name__ == '__main__':
    unittest.main()
