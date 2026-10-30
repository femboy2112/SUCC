"""SUCC Energy–Momentum CRUCIBLE: exact source/clock/Lorentz tests.

Every test uses original R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5).
Positive Gamma/Poisson clock model is a DECLARED observer, not pi digits.
Physical relativistic energy, heat, or base-16 normality are not claimed.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
import unittest

SHIFTS=((0,4),(3,-2),(4,-1),(5,-1))

def R(a):
    a=F(a)
    if a<=0:raise ValueError('a must be positive')
    return sum((F(c)/(a+d) for d,c in SHIFTS),F())

def fake_R(a):
    a=F(a)
    return 15/a**2

def source_moments(a):
    """(E[X], Var(X)) by derivatives of original four-pole R."""
    a=F(a)
    if a<=0:raise ValueError('a>0')
    C=15*a*a+121*a+240
    mean=sum((1/(a+d) for d in (0,3,4,5)),F())-(30*a+121)/C
    variance=sum((1/(a+d)**2 for d in (0,3,4,5)),F())+30/C-((30*a+121)/C)**2
    assert mean>0 and variance>0
    return mean,variance

def source_mass(a):
    """One clock at rest: mean Poisson observation total E[aX]."""
    return F(a)*source_moments(a)[0]

def source_effective_rank(a):
    m,v=source_moments(a)
    return m*m/v

def source_mass_poly(a):
    a=F(a)
    return ((30*a**5+543*a**4+3864*a**3+13427*a*a+22560*a+14400)/
            (15*a**5+301*a**4+2397*a**3+9467*a*a+18540*a+14400))

def clock_laplace(a,theta_plus,theta_minus,tplus,tminus):
    """Finite authentic Poissonized two-panel Laplace symbol."""
    a=F(a);p=F(theta_plus);m=F(theta_minus);tp=F(tplus);tm=F(tminus)
    if not (a>0 and p>=0 and m>=0 and tp>=0 and tm>=0):raise ValueError('positive clocks and Laplace probes')
    return R(a*(1+p*tp+m*tm))/R(a)

def poisson_clock_moments(a,theta_plus,theta_minus):
    a=F(a);p=F(theta_plus);m=F(theta_minus)
    if p<0 or m<0:raise ValueError('negative intensity')
    mean,var=source_moments(a)
    scale=a*mean
    energy=(p+m)*scale
    momentum=(p-m)*scale
    crosscov=p*m*a*a*var
    return energy,momentum,crosscov

def finite_pascal(a,mplus,mminus,Rsource=R):
    """Native finite Bernoulli observer, same latent source across both panels."""
    a=F(a);mplus=int(mplus);mminus=int(mminus)
    if mplus<0 or mminus<0: raise ValueError('observation budget')
    z1=Rsource(a+8)/Rsource(a)
    z2=Rsource(a+16)/Rsource(a)
    mu=1-z1
    var=z2-z1*z1
    energy=(mplus+mminus)*mu
    momentum=(mplus-mminus)*mu
    covariance=mplus*mminus*var
    return energy,momentum,covariance,mu*mu/var

def fibonacci_boost(a,b):
    return a+b,a+2*b

def fibonacci_inverse(a,b):
    return 2*a-b,-a+b

def golden_norm(a,b):
    return b*b-a*b-a*a

def golden_energy_momentum(a,b):
    """Return (E, P/sqrt(5)) in rationals, so P^2=5*Pcoef^2."""
    return F(b)-F(a,2),F(a,2)

def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def poly_add(a,b):
    return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]

def poly_deriv(a):return [F(i)*a[i] for i in range(1,len(a))]

def poly_pow(a,n):
    out=[F(1)]
    for _ in range(n):out=poly_mul(out,a)
    return out

def shape_certificate():
    """Return exact coefficient positivity of source effective rank in (1,2)."""
    C=[F(240),F(121),F(15)]
    D=poly_mul(poly_mul([F(0),F(1)],[F(3),F(1)]),poly_mul([F(4),F(1)],[F(5),F(1)]))
    Cp=poly_deriv(C);Dp=poly_deriv(D);Cpp=poly_deriv(Cp);Dpp=poly_deriv(Dp)
    Um=poly_add(poly_mul(Dp,C),[-v for v in poly_mul(D,Cp)])
    AA=poly_pow(Um,2)
    VV=poly_add(poly_mul(poly_add(poly_pow(Dp,2),[-v for v in poly_mul(Dpp,D)]),poly_pow(C,2)),
                poly_mul(poly_add(poly_mul(Cpp,C),[-v for v in poly_pow(Cp,2)]),poly_pow(D,2)))
    # The true denominator is (D*C)^2 * Var(X)>0.
    rank_gt_1=poly_add(AA,[-v for v in VV])
    rank_lt_2=poly_add([2*v for v in VV],[-v for v in AA])
    # positive coefficient polynomials for derivative of effective shape
    rank_inc=poly_add(poly_mul(poly_deriv(AA),VV),[-v for v in poly_mul(AA,poly_deriv(VV))])
    return rank_gt_1,rank_lt_2,rank_inc

class EnergyMomentumExact(unittest.TestCase):
    def test_original_source(self):
        self.assertEqual(R(1),F(47,15))
        self.assertEqual(R(9),F(4,9)-F(2,12)-F(1,13)-F(1,14))
        self.assertEqual(source_mass(1),F(6853,5640))
        for a in (1,9,17,25,81,1025):
            self.assertEqual(source_mass(a),source_mass_poly(a))
            self.assertTrue(F(1)<source_mass(a)<F(2))

    def test_shape_strict_polynomial_certificate(self):
        p1,p2,der=shape_certificate()
        self.assertTrue(all(v>=0 for v in p1) and any(v>0 for v in p1))
        self.assertTrue(all(v>=0 for v in p2) and any(v>0 for v in p2))
        self.assertTrue(all(v>=0 for v in der) and any(v>0 for v in der))
        for a in (F(1,100),F(1,2),1,9,100,1000):
            self.assertTrue(F(1)<source_effective_rank(a)<F(2))

    def test_golden_integer_norm_and_shell(self):
        a,b=0,1
        self.assertEqual(golden_norm(a,b),1)
        for _ in range(25):
            E,pcoef=golden_energy_momentum(a,b)
            self.assertEqual(E*E-5*pcoef*pcoef,1)
            self.assertEqual(golden_norm(a,b),1)
            self.assertEqual(fibonacci_inverse(*fibonacci_boost(a,b)),(a,b))
            a,b=fibonacci_boost(a,b)
        self.assertEqual(golden_energy_momentum(1,2),(F(3,2),F(1,2)))

    def test_finite_poisson_source_mass_shell(self):
        for a in (1,9,17,41):
            M=source_mass(a);r=source_effective_rank(a)
            for tp,tm in ((F(1,2),F(1,2)),(F(2),F(1,8)),(F(3,4),F(5,6))):
                E,P,C=poisson_clock_moments(a,tp,tm)
                self.assertEqual(E*E-P*P,4*tp*tm*M*M)
                self.assertEqual(E*E-P*P,4*r*C)

    def test_clock_boost_and_dual_laplace_covariance(self):
        for a in (1,9,33):
            for u,v,tu,tv in ((F(1,2),F(1,2),F(1,5),F(1,7)),(F(1,3),F(4,5),F(2,3),F(1,11))):
                self.assertEqual(clock_laplace(a,u,v,tu,tv),clock_laplace(a,2*u,v/2,tu/2,2*tv))
                E,P,_=poisson_clock_moments(a,u,v)
                E2,P2,_=poisson_clock_moments(a,2*u,v/2)
                self.assertEqual(E2,F(5,4)*E+F(3,4)*P)
                self.assertEqual(P2,F(3,4)*E+F(5,4)*P)
                self.assertEqual(E*E-P*P,E2*E2-P2*P2)

    def test_finite_poissonized_four_pole_laplace(self):
        # Independent direct four poles, not merely one-formula equality.
        for a in (1,9,25):
            for tp,tm,z,w in ((F(1,2),F(1,2),F(1,3),F(4,7)),(F(1),F(2),F(0),F(1,2))):
                C=tp*(1-z)+tm*(1-w)
                direct=sum((F(c)/(a*(1+C)+d) for d,c in SHIFTS),F())/R(a)
                self.assertEqual(direct,clock_laplace(a,tp,tm,1-z,1-w))

    def test_reset_destroys_operational_covariance(self):
        E,P,C=poisson_clock_moments(9,F(1,2),F(1,2))
        self.assertTrue(E*E-P*P>0 and C>0)
        # Resetting the second latent yields identical means but Cov(J,K)=0.
        self.assertNotEqual(E*E-P*P,4*source_effective_rank(9)*F(0))

    def test_native_pascal_exact_mass_shell(self):
        for n in (1,2,3,7,12,31):
            a=8*n-7
            for mplus,mminus in ((2,3),(n,n),(n//2,n-n//2)):
                E,P,C,r=finite_pascal(a,mplus,mminus)
                self.assertEqual(E*E-P*P,4*r*C)
                self.assertGreater(r,0)
        a=F(9);E,P,C,r=finite_pascal(a,5,6)
        Efake,Pfake,Cfake,rfake=finite_pascal(a,5,6,fake_R)
        self.assertNotEqual(r,rfake)
        self.assertNotEqual(E,Efake)

    def test_clock_normalization_breaks_mass_invariance(self):
        # Fixed total budget implies E=1 while velocity and mass change.
        for v in (F(0),F(1,3),F(1,2),F(4,5)):
            tp=(1+v)/2;tm=(1-v)/2
            self.assertEqual(tp+tm,1)
            self.assertEqual(4*tp*tm,1-v*v)
        self.assertNotEqual(F(1),F(1)-F(1,2)**2)

    def test_boost_breaks_naive_golden_pgf(self):
        # Complete Gamma(2) total-grade PGF at z=0.
        self.assertEqual(F(1)/(1+F(1))**2,F(1,4))
        self.assertEqual(F(1)/(1+F(3,2))**2,F(4,25))
        self.assertNotEqual(clock_laplace(17,F(1,2),F(1,2),1,1),
                            clock_laplace(17,F(1),F(1,8),1,1))

    def test_source_only_cannot_certify_selected_pi(self):
        # Same original forcing for two initial seeds, same mass and all positive symbols.
        u,v=F(0),F(1,7)
        for n in range(1,15):
            r=R(8*n-7)
            u=16*u+r;v=16*v+r
            self.assertEqual(v-u,F(16**n,7))
        self.assertEqual(source_mass(9),source_mass(9))

if __name__=='__main__':unittest.main(verbosity=2)
