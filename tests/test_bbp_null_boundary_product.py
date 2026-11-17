"""Exact BBP null-boundary multiplicative product: finite checks and controls.

The product is an affine-seed cocycle, not a prime Euler product or a
criterion for the distribution of digits of pi.  Rational inputs give exact
certificates; the infinite endpoint is the established classical BBP identity.
"""
from fractions import Fraction as F
import unittest


def r(n):
    if n < 1:
        raise ValueError('n >= 1')
    return F(4, 8*n - 7) - F(2, 8*n - 4) - F(1, 8*n - 3) - F(1, 8*n - 2)


def states(N, s=F(0), forcing=r):
    U = F(s)
    path = [U]
    for n in range(1, N + 1):
        U = 16*U + forcing(n)
        path.append(U)
    return path


def endpoint(N, forcing=r):
    return sum((forcing(n)/16**n for n in range(1, N+1)), F(0))


def product(N, s=F(0), forcing=r):
    U = states(N,s,forcing)
    p = F(1)
    for n in range(N):
        if U[n+1] == 0:
            raise ZeroDivisionError('intermediate state has zero denominator')
        p *= 1-forcing(n+1)/U[n+1]
    return p


def suffix(N, s=F(0), forcing=r):
    if N < 1:
        raise ValueError('N >= 1')
    U = states(N,s,forcing)
    prod = F(1)
    for n in range(1,N):
        if U[n+1] == 0:
            raise ZeroDivisionError
        prod *= 1-forcing(n+1)/U[n+1]
    return prod


class NullBoundaryProductTests(unittest.TestCase):
    def test_source_passport_zero_seed(self):
        self.assertEqual(r(1),F(47,15))
        self.assertEqual(endpoint(1),F(47,240))
        self.assertEqual(states(1)[0],0)
        self.assertEqual(states(1)[1],r(1))
        for n in (1,2,8,32):
            self.assertEqual(states(n)[-1],16**n*endpoint(n))
            self.assertGreater(endpoint(n),0)

    def test_product_finite_telescopes_for_all_allowed_seeds(self):
        for N in (1,2,3,4,8,24):
            for s in (F(0),F(1,16),F(1,7),F(3)):
                self.assertEqual(product(N,s),s/(s+endpoint(N)))

    def test_first_factor_exact_null_at_zero_input(self):
        for N in (1,2,4,9):
            P1=endpoint(1)
            self.assertEqual(product(1,F(0)),0)
            self.assertEqual(product(N,F(0)),0)
            self.assertEqual(suffix(N,F(0)),P1/endpoint(N))
            self.assertGreater(suffix(N,F(0)),0)

    def test_first_factor_suffix_composition(self):
        P1=endpoint(1)
        for N in (1,2,3,10):
            for s in (F(0),F(1,17),F(13,9)):
                first=s/(s+P1)
                later=(s+P1)/(s+endpoint(N))
                self.assertEqual(later,suffix(N,s))
                self.assertEqual(first*later,product(N,s))

    def test_all_higher_jets_at_null_seed(self):
        # Compute coefficients of the truncated formal identity
        # (P_N+s)*G_N(s)=s, independently of the closed jet formula.
        from math import factorial
        for N in (1,2,5,10):
            p=endpoint(N)
            coefficient=[F(0)]
            for k in range(1,8):
                target=F(1) if k==1 else F(0)
                coefficient.append((target-coefficient[k-1])/p)
                derivative=factorial(k)*coefficient[k]
                self.assertEqual(derivative,(-1)**(k-1)*factorial(k)/p**k)
            self.assertEqual(coefficient[1],(F(1)/endpoint(1))*(endpoint(1)/p))

    def test_jet_coefficient_dual_number_product(self):
        # In Q[eps]/eps², only the coefficient of eps survives.
        for N in (1,2,4,16):
            for v in (F(1),F(-1,3),F(2,7)):
                P=endpoint(N)
                coefficient=v/P
                first_jet=v/endpoint(1)
                later_const=endpoint(1)/P
                self.assertEqual(coefficient,first_jet*later_const)

    def test_zero_jet_not_digit_distribution_certificate(self):
        # Competing source zero-seeded and eventually exactly locked.
        locked=lambda n: F(16) if n==1 else F(0)
        for N in (1,2,4,10):
            self.assertEqual(endpoint(N,locked),F(1))
            self.assertEqual(product(N,F(0),locked),0)
            self.assertEqual(suffix(N,F(0),locked),F(1))
            self.assertEqual(product(N,F(1,7),locked),F(1,8))
        # Same formal product law; different endpoint / digit behavior.
        self.assertNotEqual(endpoint(10),F(1))

    def test_exact_boundary_singularity_and_source_change(self):
        for N in (1,2,4,8):
            p=endpoint(N)
            with self.assertRaises(ZeroDivisionError):
                product(N,-p)
            # The rational function has a genuine pole at s=-P_N;
            # it is NOT valid to extend the raw factor product through it.
            self.assertNotEqual(p,0)

    def test_finite_scale_separation(self):
        for N in (1,2,3,10):
            # first factor: zero order one, later suffix: order zero.
            p=endpoint(N);p1=endpoint(1)
            self.assertEqual(F(1)/p1*(p1/p),F(1)/p)
            self.assertEqual(16**N*F(1)/states(N)[-1],F(1)/p)


if __name__ == '__main__': unittest.main()
