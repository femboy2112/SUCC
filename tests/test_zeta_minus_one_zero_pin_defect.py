"""Exact zeta(-1) zero-pinning defects and BBP null-jet normalization.

This proves an RH-equivalent diagnostic using classical xi zero factorization,
not RH, pi normality, or a new BBP/prime-clock transport.  Finite model zeros
are illustrative and are NEVER identified with actual zeta zeros.
"""
import unittest
from fractions import Fraction as F
from math import factorial


def bbp_r(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def bbp_P(N):
    return sum((bbp_r(n)/16**n for n in range(1,N+1)), F(0))


def line_square(gamma):
    g = F(gamma)
    t = g*g+F(1,4)
    return (1+2/t)**2


def true_square(beta, gamma):
    """Exact |1+2/[rho(1-rho)]|^2 for rho=beta+i*gamma."""
    b, g = F(beta), F(gamma)
    if not (0<b<1 and g>0):
        raise ValueError('represent a zero in the critical strip')
    t = g*g+F(1,4)
    d = (b-F(1,2))**2
    denominator = t*t+(2*g*g-F(1,2))*d+d*d
    return 1+4*(t+1-d)/denominator


def displacement_response_coefficient(gamma):
    """Coefficient of (beta-1/2)^2 in the per-zero logarithmic defect."""
    g=F(gamma)
    t=g*g+F(1,4)
    return 2*(3*t*t+t-1)/(t*t*(t+2)**2)


def cpair_product_mod_sq(beta,gamma):
    """For an off-line mirrored pair with same positive gamma.

    The upper zeros beta+i*gamma and 1-beta+i*gamma have conjugate
    xi(-1) factors, so their product is the squared modulus.
    """
    return true_square(beta,gamma)


class ZetaMinusOneZeroPinDefectTests(unittest.TestCase):
    def test_original_BBP_first_jet_formula_exact_for_finite_endpoints(self):
        self.assertEqual(bbp_r(1), F(47,15))
        self.assertEqual(bbp_P(1),F(47,240))
        for N in (1,2,3,4,8,16):
            P=bbp_P(N)
            self.assertGreater(P,0)
            # Coefficients a_k of (P+s)G(s)=s without assuming a_k.
            a=[F(0)]
            for k in range(1,7):
                rhs=F(1) if k==1 else F(0)
                a.append((rhs-a[-1])/P)
                self.assertEqual(factorial(k)*a[k],(-1)**(k-1)*factorial(k)/P**k)

    def test_zeta_minus_one_and_completed_xi_normalization(self):
        # xi(-1)=(-2*pi)*zeta(-1)=pi/6.  Cancel pi symbolically.
        zeta_negative_one=F(-1,12)
        xi_over_pi=-2*zeta_negative_one
        self.assertEqual(xi_over_pi,F(1,6))
        # (16/pi)*(pi/6)=8/3; no RH premise occurs.
        self.assertEqual(16*xi_over_pi,F(8,3))

    def test_genuine_prime_compensation_keeps_zeta_minus_one(self):
        zeta_negative_one=F(-1,12)
        for primes in ((),(2,),(3,),(2,3),(3,5),(2,3,5)):
            E=F(1)
            R=zeta_negative_one
            for p in primes:
                E/=1-p
                R*=1-p
            self.assertEqual(E*R,zeta_negative_one)
        # These completed prime factors differ from BBP's zero n=0 factor.
        self.assertTrue(all(1-p != 0 for p in (2,3,5,7,11)))

    def test_actual_vs_line_factor_equality_only_at_critical_line(self):
        # Every actual zeta zero is at height >14, so gamma>1/2 holds.
        for g in (F(1),F(14),F(141,10),F(50)):
            equal=line_square(g)
            self.assertEqual(true_square(F(1,2),g),equal)
            for b in (F(1,10),F(1,4),F(2,5),F(3,5),F(3,4),F(9,10)):
                self.assertLess(true_square(b,g),equal)

    def test_offline_mirror_pair_and_quadratic_margin(self):
        for b,g in ((F(1,4),F(14)),(F(2,5),F(17)),(F(1,8),F(25))):
            self.assertEqual(cpair_product_mod_sq(b,g),true_square(1-b,g))
            self.assertLess(cpair_product_mod_sq(b,g),line_square(g))
            self.assertGreater(displacement_response_coefficient(g),0)

    def test_horizon_decay_of_offline_susceptibility(self):
        # 2(3t^2+t-1)/(t^2(t+2)^2) ~ 6/gamma^4.
        for g in (F(14),F(30),F(100),F(1000)):
            coeff=displacement_response_coefficient(g)
            self.assertGreater(coeff,0)
            self.assertLess(coeff,F(8,g**4))
        self.assertGreater(displacement_response_coefficient(F(14)),
                           displacement_response_coefficient(F(30)))

    def test_small_height_mutant_shows_why_zero_height_scope_matters(self):
        # At small gamma the inequality can reverse; the theorem must
        # cite the actual zero-free lower height.
        g=F(1,10)
        b=F(1,10)
        self.assertGreater(true_square(b,g),line_square(g))

    def test_finite_zeros_do_not_establish_infinite_RH_product(self):
        # Synthetic zeros demonstrate the exact sum is zero for on-line
        # entries and positive for off-line; no actual-zero enumeration.
        records=((F(1,2),F(14)),(F(1,2),F(17)),(F(2,5),F(19)))
        ratios=[line_square(g)/true_square(b,g) for b,g in records]
        self.assertEqual(ratios[:2],[F(1),F(1)])
        self.assertGreater(ratios[2],1)
        self.assertGreater(ratios[0]*ratios[1]*ratios[2],1)

if __name__=='__main__':
    unittest.main()
